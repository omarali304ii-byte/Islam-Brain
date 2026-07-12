"""Download IG post images + TikTok covers locally for VISUAL REVIEW (not for dashboard hotlinking).
Also fetch TikTok transcripts (video content) where available. Saves to _media/."""
import json, sys, io, urllib.request, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from pathlib import Path

BASE = Path(r"C:/Users/eslam/MyKnoweldgeBase/SmartProds/Research/cielito-egypt/Claude-Fable-5")
SOC = BASE / "_sources/social"
MED = BASE / "_media"; (MED / "ig").mkdir(parents=True, exist_ok=True); (MED / "tt").mkdir(parents=True, exist_ok=True)
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/126.0"}

def get(url, out, timeout=30):
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=timeout) as r:
            out.write_bytes(r.read()); return True
    except Exception as e:
        return False

def gettext(url, timeout=20):
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read().decode("utf-8", "replace")
    except Exception:
        return None

ig = json.loads((SOC / "instagram_posts_deep.json").read_text(encoding="utf-8"))
# curate: owned posts + top earned by likes + format variety — index for review
ig_sorted = sorted(ig, key=lambda p: -(p.get("likesCount", 0) or 0))
manifest = []
n_ok = 0
for i, p in enumerate(ig_sorted):
    u = p.get("displayUrl")
    if not u: continue
    fn = MED / "ig" / f"{i:03d}_{'own' if p.get('ownerUsername')=='cielitoegypt' else 'wom'}_{p.get('type','x')}.jpg"
    if get(u, fn):
        n_ok += 1
        manifest.append({"file": fn.name, "owner": p.get("ownerUsername"), "owned": p.get("ownerUsername")=="cielitoegypt",
                         "type": p.get("type"), "likes": p.get("likesCount",0), "views": p.get("videoViewCount"),
                         "caption": (p.get("caption") or "")[:120], "url": p.get("url"), "date": (p.get("timestamp") or "")[:10]})
print(f"IG images downloaded: {n_ok}")

tt = json.loads((SOC / "tiktok_videos.json").read_text(encoding="utf-8"))
tt_sorted = sorted([v for v in tt if v.get("id")], key=lambda v: -(v.get("playCount",0) or 0))
tt_manifest = []; transcripts = []
n_tt = 0
for i, v in enumerate(tt_sorted):
    vm = v.get("videoMeta") or {}
    cov = vm.get("coverUrl") or vm.get("originalCoverUrl")
    fn = MED / "tt" / f"{i:03d}_cover.jpg"
    ok = get(cov, fn) if cov else False
    if ok: n_tt += 1
    # transcript (video content!)
    tr = None
    tl = vm.get("subtitleLinks") or []
    tlink = vm.get("transcriptionLink") or (tl[0].get("downloadLink") if tl and isinstance(tl[0], dict) else None)
    if tlink:
        raw = gettext(tlink)
        if raw:
            # strip webvtt/srt timing -> plain text
            lines = [l.strip() for l in raw.splitlines() if l.strip() and "-->" not in l and not re.match(r"^\d+$", l) and not l.upper().startswith("WEBVTT")]
            tr = " ".join(lines)[:600]
    tt_manifest.append({"file": fn.name if ok else None, "plays": v.get("playCount",0), "diggs": v.get("diggCount",0),
                        "text": (v.get("text") or "")[:120], "duration": vm.get("duration"), "url": v.get("webVideoUrl"),
                        "transcript": tr})
    if tr: transcripts.append({"url": v.get("webVideoUrl"), "text": (v.get("text") or "")[:80], "transcript": tr, "plays": v.get("playCount",0)})
print(f"TikTok covers: {n_tt} · transcripts: {len(transcripts)}")

(MED / "ig_manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8")
(MED / "tt_manifest.json").write_text(json.dumps(tt_manifest, ensure_ascii=False, indent=1), encoding="utf-8")
(MED / "tt_transcripts.json").write_text(json.dumps(transcripts, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"DONE. ig manifest {len(manifest)} · tt manifest {len(tt_manifest)}")
