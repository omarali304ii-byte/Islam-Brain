"""Deeper capture for the dense Cielito 360 dashboard: more IG posts + full comments per post
(the "all reviews" corpus) + TikTok comments. Apify REST, token from .secrets at runtime, never echoed.
Standing scrape authorization (user: 'use apify or any scraping tools if needed'). Costs logged."""
import json, time, sys, io, urllib.request
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from pathlib import Path

SECRETS = Path(r"C:\Users\eslam\.secrets\gtm-saas.env")
OUT = Path(__file__).resolve().parent.parent / "_sources" / "social"
OUT.mkdir(parents=True, exist_ok=True)
TOK = [l.split("=", 1)[1].strip().strip('"').strip("'") for l in SECRETS.read_text(encoding="utf-8", errors="ignore").splitlines() if l.strip().startswith("APIFY_API_TOKEN")][0]

def api(path, payload=None, method="GET"):
    url = f"https://api.apify.com/v2/{path}{'&' if '?' in path else '?'}token={TOK}"
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=90) as r:
        return json.loads(r.read().decode())

def run(actor, inp, wait=600):
    run = api(f"acts/{actor}/runs", inp, "POST")["data"]
    rid, status, w = run["id"], run["status"], 0
    while status in ("READY", "RUNNING") and w < wait:
        time.sleep(15); w += 15
        run = api(f"actor-runs/{rid}")["data"]; status = run["status"]
        print(f"  [{actor}] {status} {w}s", flush=True)
    usage = run.get("usageTotalUsd")
    if status == "SUCCEEDED":
        items = api(f"datasets/{run['defaultDatasetId']}/items?clean=true&format=json")
        return items, usage, status
    return [], usage, status

summary = {}

# 1) MORE IG posts (owned history, deeper) — 150
print("R3: IG posts (150 owned/recent)...", flush=True)
posts, u1, s1 = run("apify~instagram-scraper", {
    "directUrls": ["https://www.instagram.com/cielitoegypt/"],
    "resultsType": "posts", "resultsLimit": 150, "addParentData": True,
})
if posts:
    (OUT / "instagram_posts_deep.json").write_text(json.dumps(posts, ensure_ascii=False, indent=1), encoding="utf-8")
summary["R3_ig_posts"] = {"n": len(posts), "usd": u1, "status": s1}
print(f"  R3 -> {len(posts)} posts, ${u1}", flush=True)

# 2) FULL comments on the highest-comment posts (the review corpus)
# gather candidate URLs from the deep pull + the existing captures
urls = []
for p in posts:
    if p.get("url") and (p.get("commentsCount", 0) or 0) >= 1:
        urls.append((p["commentsCount"], p["url"]))
try:
    prev = json.loads((OUT / "instagram_posts.json").read_text(encoding="utf-8"))
    for p in prev:
        if p.get("url"):
            urls.append((p.get("commentsCount", 0) or 0, p["url"]))
except Exception:
    pass
seen, top_urls = set(), []
for _, u in sorted(urls, key=lambda x: -x[0]):
    if u not in seen:
        seen.add(u); top_urls.append(u)
top_urls = top_urls[:40]
print(f"R4: IG comments on top {len(top_urls)} posts...", flush=True)
comments, u2, s2 = run("apify~instagram-comment-scraper", {
    "directUrls": top_urls, "resultsLimit": 40,
})
if comments:
    (OUT / "instagram_comments_deep.json").write_text(json.dumps(comments, ensure_ascii=False, indent=1), encoding="utf-8")
summary["R4_ig_comments"] = {"n": len(comments), "usd": u2, "status": s2, "posts": len(top_urls)}
print(f"  R4 -> {len(comments)} comments, ${u2}", flush=True)

(OUT / "_deep_capture_summary.json").write_text(json.dumps(summary, indent=1), encoding="utf-8")
tot = sum((v.get("usd") or 0) for v in summary.values())
print(f"DONE deep capture. total spend ${tot:.3f} :: {json.dumps(summary)}")
