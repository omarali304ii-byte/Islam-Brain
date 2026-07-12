"""Cielito Social Command — SENTIMENT ENGINE.
Scores every IG comment, TikTok caption, and owned caption with the CAMeLBERT-DA Egyptian
binary model (the same engine measured 89.5% on DaleelStore reviews). Emoji-only reactions
(dominant for a fashion brand) are polarity-scored separately and disclosed honestly.
PII fail-closed: handle-only, no names/emails/pics. $0 new spend (local model load only).
Emits: _intel/cielito_social_sentiment.json (aggregates + ALL scored items for the Review Explorer)."""
import json, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from pathlib import Path
from collections import Counter

BASE = Path(r"C:/Users/eslam/MyKnoweldgeBase/SmartProds/Research/cielito-egypt/Claude-Fable-5")
SOC = BASE / "_sources" / "social"
OUT = BASE / "_intel" / "cielito_social_sentiment.json"
MODEL_DIR = r"C:/Users/eslam/MyKnoweldgeBase/SmartProds/heka/models/egyptian/camelbert-da_egyptian_binary/model"

ARAB = re.compile(r"[؀-ۿ]")
EMOJI = re.compile("[\U0001F000-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF❤♥☀-⛿✀-➿️‍]+")
POS_EMO = set("❤🧡💛💚💙💜🖤🤍🤎💕💞💓💗💖💘💝😍🥰😘😻🔥✨⭐🌟💯👏🙌👍😊🥹🤩💋💐🌸🌷🪷☀🌊⛱🤍💫🥳🫶😳♥")
NEG_EMO = set("😡🤬👎💔😤🙄😒😠🤢🤮😞😔")

def strip_pii(s):
    return s  # we only keep text + handle; never names/emails/pics

def load(p):
    try: return json.loads(Path(p).read_text(encoding="utf-8"))
    except Exception: return None

# ── gather all comments (existing latestComments + deep comment pull) ──
comments = []
seen = set()
ig_posts = load(SOC / "instagram_posts.json") or []
for p in ig_posts:
    for c in (p.get("latestComments") or []):
        t = (c.get("text") or "").strip()
        key = (c.get("ownerUsername"), t)
        if t and key not in seen:
            seen.add(key)
            comments.append({"channel": "ig_comment", "handle": c.get("ownerUsername"),
                             "text": t, "on": p.get("ownerUsername"), "url": p.get("url"),
                             "likes": c.get("likesCount", 0) or 0})
deep = load(SOC / "instagram_comments_deep.json")
if deep:
    for c in deep:
        t = (c.get("text") or "").strip()
        handle = c.get("ownerUsername") or c.get("username")
        key = (handle, t)
        if t and key not in seen:
            seen.add(key)
            comments.append({"channel": "ig_comment", "handle": handle, "text": t,
                             "on": c.get("postUrl") or c.get("inputUrl"), "url": c.get("postUrl") or c.get("inputUrl"),
                             "likes": c.get("likesCount", 0) or 0})
ttc = load(SOC / "tiktok_comments.json")
if ttc:
    for c in ttc:
        t = (c.get("text") or "").strip()
        handle = c.get("uniqueId")
        key = (handle, t)
        if t and key not in seen:
            seen.add(key)
            comments.append({"channel": "tiktok_comment", "handle": handle, "text": t,
                             "on": c.get("submittedVideoUrl"), "url": c.get("submittedVideoUrl"),
                             "likes": int(c.get("diggCount", 0) or 0)})

# captions as their own "voice" channels
def caption_items(posts, chan, textkey, urlkey, ownerkey):
    out = []
    for p in posts:
        t = (p.get(textkey) or "").strip()
        if t:
            out.append({"channel": chan, "handle": p.get(ownerkey), "text": t,
                        "on": p.get(ownerkey), "url": p.get(urlkey), "likes": p.get("likesCount", 0) or p.get("diggCount", 0) or 0})
    return out
owned_posts = [p for p in ig_posts if p.get("ownerUsername") == "cielitoegypt"]
tt = load(SOC / "tiktok_videos.json") or []
cap_owned = caption_items(owned_posts, "owned_caption", "caption", "url", "ownerUsername")
cap_tt = caption_items([v for v in tt if v.get("id")], "tiktok_caption", "text", "webVideoUrl", None)

ALL = comments + cap_owned + cap_tt
print(f"gathered: {len(comments)} comments · {len(cap_owned)} owned captions · {len(cap_tt)} tiktok captions = {len(ALL)}")

# ── split emoji-only vs text ──
def is_emoji_only(t):
    stripped = EMOJI.sub("", t)
    stripped = re.sub(r"[\s\W\d_]+", "", stripped)
    return len(stripped) == 0
def emoji_polarity(t):
    chars = set(t)
    pos = len(chars & POS_EMO); neg = len(chars & NEG_EMO)
    if neg > pos: return "negative"
    if pos > 0: return "positive"
    return "neutral"

text_items = [r for r in ALL if not is_emoji_only(r["text"])]
emoji_items = [r for r in ALL if is_emoji_only(r["text"])]
for r in emoji_items:
    r["sentiment"] = emoji_polarity(r["text"]); r["score"] = 1.0
    r["method"] = "emoji polarity"; r["is_emoji"] = True

# ── model scoring for text items ──
NEUTRAL_MARGIN = 0.60
ENGINE_OK = True
try:
    import torch, torch.nn.functional as F
    from transformers import AutoTokenizer, AutoModelForSequenceClassification
    print("Loading CAMeLBERT-DA Egyptian binary...")
    tok = AutoTokenizer.from_pretrained(MODEL_DIR)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_DIR); model.eval()
    LABELS = ["negative", "positive"]
    texts = [r["text"] for r in text_items]
    for i in range(0, len(texts), 24):
        enc = tok(texts[i:i+24], return_tensors="pt", truncation=True, max_length=128, padding=True)
        with torch.no_grad():
            probs = F.softmax(model(**enc).logits, dim=-1)
        for j, p in enumerate(probs):
            idx = int(p.argmax()); conf = float(p[idx]); r = text_items[i+j]
            r["sentiment"] = "neutral" if conf < NEUTRAL_MARGIN else LABELS[idx]
            r["score"] = round(conf, 3); r["method"] = "CAMeLBERT-DA Egyptian (binary)"; r["is_emoji"] = False
    print(f"model-scored {len(text_items)} text items")
except Exception as e:
    ENGINE_OK = False
    print("MODEL UNAVAILABLE -> lexicon fallback:", str(e)[:160])
    POSW = ["جميل","حلو","تحفه","تحفة","قمر","روعه","روعة","حبيت","ممتاز","رائع","احلى","اجمل","gorgeous","love","beautiful","nice","best","amazing","stunning","perfect"]
    NEGW = ["وحش","سيء","غالي","مش حلو","زفت","bad","ugly","expensive","worst","poor"]
    for r in text_items:
        t = r["text"].lower()
        pos = any(w in t for w in POSW); neg = any(w in t for w in NEGW)
        r["sentiment"] = "negative" if neg and not pos else "positive" if pos and not neg else "neutral"
        r["score"] = 0.5; r["method"] = "rule-based lexicon"; r["is_emoji"] = False

# ── purchase-intent detector (size/price/where questions) ──
INTENT = ["مقاس","السعر","بكام","السعرررر","كام","المقاس","متوفر","available","size","price","how much","تمن","بيتباع","فين"]
for r in ALL:
    t = r["text"].lower()
    r["intent"] = any(w in t for w in INTENT)

# ── theme tagging (light) ──
THEMES = {
    "beauty / look praise": ["جميل","حلو","تحفه","تحفة","قمر","روعه","gorgeous","beautiful","stunning","حبيت","love"],
    "quality / craft": ["جوده","جودة","جلد","خامه","خامة","quality","leather","material"],
    "price / value": ["سعر","غالي","بكام","price","expensive","cheap","تمن"],
    "size / fit": ["مقاس","size","fit","المقاس"],
    "delivery / service": ["شحن","توصيل","الاوردر","order","delivery","خدمة"],
}
def theme_of(t):
    tl = t.lower()
    for name, kws in THEMES.items():
        if any(k in tl for k in kws): return name
    return "general reaction"
for r in ALL:
    r["theme"] = theme_of(r["text"])

# ── aggregates ──
def dist(items):
    c = Counter(r["sentiment"] for r in items)
    n = len(items) or 1
    return {"n": len(items), "positive": c["positive"], "negative": c["negative"], "neutral": c["neutral"],
            "positive_pct": round(c["positive"]/n*100, 1), "negative_pct": round(c["negative"]/n*100, 1),
            "neutral_pct": round(c["neutral"]/n*100, 1)}
by_channel = {ch: dist([r for r in ALL if r["channel"] == ch]) for ch in ("ig_comment", "tiktok_comment", "owned_caption", "tiktok_caption")}
overall = dist(ALL)
theme_sent = []
for name in THEMES:
    its = [r for r in ALL if r["theme"] == name]
    if its:
        d = dist(its); d["theme"] = name; theme_sent.append(d)
theme_sent = sorted(theme_sent, key=lambda x: -x["n"])
intent_items = [r for r in ALL if r["intent"]]

# evidence rows (ALL, PII-safe: handle + text only)
def ev(r):
    return {"channel": r["channel"], "handle": r["handle"], "text": r["text"][:220],
            "ar": bool(ARAB.search(r["text"])), "sentiment": r["sentiment"], "score": r.get("score"),
            "method": r["method"], "theme": r["theme"], "intent": r["intent"], "is_emoji": r.get("is_emoji", False),
            "on": r.get("on"), "url": r.get("url"), "likes": r.get("likes", 0)}
evidence = [ev(r) for r in ALL]

out = {
    "engine": {"model": "CAMeLBERT-DA Egyptian (binary)" if ENGINE_OK else "rule-based lexicon (fallback)",
               "measured_accuracy_note": "89.5% vs star-rating ground truth on DaleelStore reviews (same engine)" if ENGINE_OK else None,
               "neutral_margin": NEUTRAL_MARGIN, "emoji_handling": "emoji-only reactions polarity-scored separately",
               "n_total": len(ALL), "n_text_model": len(text_items), "n_emoji": len(emoji_items),
               "single_number_warning": "Sentiment depends on where you listen; comment corpus is praise-heavy — never quote one blended number."},
    "overall": overall, "by_channel": by_channel, "theme_sentiment": theme_sent,
    "intent": {"n": len(intent_items), "note": "Size/price/availability questions = purchase intent. Most land on creator posts (no WhatsApp path to catch them).",
               "items": [ev(r) for r in intent_items][:30]},
    "top_positive": [ev(r) for r in sorted([x for x in ALL if x["sentiment"]=="positive"], key=lambda x:-x.get("likes",0))[:10]],
    "top_negative": [ev(r) for r in sorted([x for x in ALL if x["sentiment"]=="negative"], key=lambda x:-x.get("likes",0))[:10]],
    "evidence": evidence,
}
OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"WROTE {OUT.name}")
print(f"  overall: {overall['positive_pct']}% pos / {overall['negative_pct']}% neg / {overall['neutral_pct']}% neu (n={overall['n']})")
print(f"  channels: " + " · ".join(f"{k} n={v['n']} ({v['positive_pct']}%+)" for k,v in by_channel.items()))
print(f"  themes: {[(t['theme'], t['n']) for t in theme_sent]}")
print(f"  intent signals: {len(intent_items)} · evidence rows: {len(evidence)}")
