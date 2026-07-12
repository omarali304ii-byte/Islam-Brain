"""Full review scrape: TikTok comments + Noon marketplace reviews. Apify REST, token from .secrets.
Standing scrape authorization. Costs logged. Feeds the sentiment engine + Review Explorer."""
import json, time, sys, io, urllib.request
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from pathlib import Path

SECRETS = Path(r"C:\Users\eslam\.secrets\gtm-saas.env")
OUT = Path(__file__).resolve().parent.parent / "_sources" / "social"
TOK = [l.split("=", 1)[1].strip().strip('"').strip("'") for l in SECRETS.read_text(encoding="utf-8", errors="ignore").splitlines() if l.strip().startswith("APIFY_API_TOKEN")][0]

def api(path, payload=None, method="GET"):
    url = f"https://api.apify.com/v2/{path}{'&' if '?' in path else '?'}token={TOK}"
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read().decode())

def run(actor, inp, wait=720):
    try:
        run = api(f"acts/{actor}/runs", inp, "POST")["data"]
    except Exception as e:
        return [], None, f"START_ERR:{str(e)[:80]}"
    rid, status, w = run["id"], run["status"], 0
    while status in ("READY", "RUNNING") and w < wait:
        time.sleep(15); w += 15
        run = api(f"actor-runs/{rid}")["data"]; status = run["status"]
        print(f"  [{actor}] {status} {w}s", flush=True)
    usage = run.get("usageTotalUsd")
    if status == "SUCCEEDED":
        return api(f"datasets/{run['defaultDatasetId']}/items?clean=true&format=json"), usage, status
    return [], usage, status

summary = {}

# 1) TikTok comments on top videos
tt = json.loads((OUT / "tiktok_videos.json").read_text(encoding="utf-8"))
tt_urls = [v["webVideoUrl"] for v in sorted([x for x in tt if x.get("id")], key=lambda x: -(x.get("playCount",0) or 0))[:30] if v.get("webVideoUrl")] if tt else []
tt_urls = [v["webVideoUrl"] for v in sorted([x for x in tt if x.get("id") and x.get("webVideoUrl")], key=lambda x: -(x.get("playCount",0) or 0))[:30]]
print(f"R5: TikTok comments on top {len(tt_urls)} videos...", flush=True)
ttc, u5, s5 = run("clockworks~tiktok-comments-scraper", {"postURLs": tt_urls, "commentsPerPost": 40, "maxRepliesPerComment": 0})
if ttc: (OUT / "tiktok_comments.json").write_text(json.dumps(ttc, ensure_ascii=False, indent=1), encoding="utf-8")
summary["R5_tiktok_comments"] = {"n": len(ttc), "usd": u5, "status": s5}
print(f"  R5 -> {len(ttc)} comments, ${u5} [{s5}]", flush=True)

# 2) Noon marketplace reviews (Cielito store)
print("R6: Noon Cielito reviews...", flush=True)
noon, u6, s6 = run("epctex~noon-scraper", {"search": ["cielito"], "country": "eg", "maxItems": 120, "proxy": {"useApifyProxy": True}})
if noon: (OUT / "noon_products.json").write_text(json.dumps(noon, ensure_ascii=False, indent=1), encoding="utf-8")
summary["R6_noon"] = {"n": len(noon), "usd": u6, "status": s6}
print(f"  R6 -> {len(noon)} items, ${u6} [{s6}]", flush=True)

(OUT / "_reviews_capture_summary.json").write_text(json.dumps(summary, indent=1), encoding="utf-8")
tot = sum((v.get("usd") or 0) for v in summary.values())
print(f"DONE reviews capture. total ${tot:.3f} :: {json.dumps(summary)}")
