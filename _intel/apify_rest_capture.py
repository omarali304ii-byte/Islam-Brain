"""Approved paid routes R1 (Instagram) + R2 (TikTok) for cielito-egypt base 360.
Apify REST transport per SCRAPING_PROTOCOL.md — token read at runtime from .secrets, never printed.
Approval: Eslam, 2026-07-09 intake (est. $1.0-1.6 total)."""
import json, time, sys, urllib.request, urllib.parse
from pathlib import Path

SECRETS = Path(r"C:\Users\eslam\.secrets\gtm-saas.env")
OUT = Path(__file__).resolve().parent.parent / "_sources" / "social"
OUT.mkdir(parents=True, exist_ok=True)

def token():
    for line in SECRETS.read_text(encoding="utf-8", errors="ignore").splitlines():
        if line.strip().startswith("APIFY_API_TOKEN"):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    sys.exit("APIFY_API_TOKEN not found in secrets env")

TOK = token()

def api(path, payload=None, method="GET"):
    url = f"https://api.apify.com/v2/{path}{'&' if '?' in path else '?'}token={TOK}"
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(url, data=data, method=method,
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode())

JOBS = [
    {
        "route": "R1",
        "actor": "apify~instagram-scraper",
        "outfile": "instagram_posts.json",
        "input": {
            "directUrls": ["https://www.instagram.com/cielitoegypt/"],
            "resultsType": "posts",
            "resultsLimit": 60,
            "addParentData": True,
            "searchType": "hashtag",
        },
    },
    {
        "route": "R2",
        "actor": "clockworks~tiktok-scraper",
        "outfile": "tiktok_videos.json",
        "input": {
            "profiles": ["cielitoegypt"],
            "resultsPerPage": 60,
            "profileScrapeSections": ["videos"],
            "shouldDownloadVideos": False,
            "shouldDownloadCovers": False,
            "shouldDownloadSubtitles": False,
        },
    },
]

summary = []
for job in JOBS:
    print(f"[{job['route']}] starting {job['actor']} ...", flush=True)
    try:
        run = api(f"acts/{job['actor']}/runs", job["input"], "POST")["data"]
        run_id = run["id"]
        status = run["status"]
        waited = 0
        while status in ("READY", "RUNNING") and waited < 420:
            time.sleep(15); waited += 15
            run = api(f"actor-runs/{run_id}")["data"]
            status = run["status"]
            print(f"[{job['route']}] {status} after {waited}s", flush=True)
        usage = run.get("usageTotalUsd", None)
        if status == "SUCCEEDED":
            ds = run["defaultDatasetId"]
            items = api(f"datasets/{ds}/items?clean=true&format=json")
            (OUT / job["outfile"]).write_text(json.dumps(items, ensure_ascii=False, indent=1), encoding="utf-8")
            summary.append({"route": job["route"], "actor": job["actor"], "status": status,
                            "items": len(items), "usage_usd": usage, "file": job["outfile"]})
            print(f"[{job['route']}] SUCCEEDED: {len(items)} items, usage ${usage}", flush=True)
        else:
            summary.append({"route": job["route"], "actor": job["actor"], "status": status,
                            "items": 0, "usage_usd": usage, "file": None})
            print(f"[{job['route']}] ENDED {status} (usage ${usage}) — recorded as inaccessible-not-absent", flush=True)
    except Exception as e:
        summary.append({"route": job["route"], "actor": job["actor"], "status": f"ERROR: {e}", "items": 0,
                        "usage_usd": None, "file": None})
        print(f"[{job['route']}] ERROR: {e}", flush=True)

(OUT / "_capture_summary.json").write_text(json.dumps(summary, indent=1), encoding="utf-8")
print("DONE " + json.dumps(summary))
