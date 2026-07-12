"""Cielito Pricing + Product-Design engine — REAL catalog analysis (no fabrication).
Reads _sources/website/products_p1.json (250 products: prices, compare_at, types, tags, options/sizes, images).
Emits _intel/cielito_pricing_design.json + downloads a product-image sample for design review."""
import json, re, sys, io, urllib.request, statistics
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from pathlib import Path
from collections import Counter, defaultdict

BASE = Path(r"C:/Users/eslam/MyKnoweldgeBase/SmartProds/Research/cielito-egypt/Claude-Fable-5")
RAW = BASE / "_sources/website/products_p1.json"
MED = BASE / "_media/products"; MED.mkdir(parents=True, exist_ok=True)
OUT = BASE / "_intel" / "cielito_pricing_design.json"
UA = {"User-Agent": "Mozilla/5.0 Chrome/126.0"}

prods = json.loads(RAW.read_text(encoding="utf-8"))["products"]

def price_of(p):
    vs = [float(v["price"]) for v in p.get("variants", []) if v.get("price")]
    return min(vs) if vs else None
def compare_of(p):
    vs = [float(v["compare_at_price"]) for v in p.get("variants", []) if v.get("compare_at_price")]
    return max(vs) if vs else None

# ── category normalization (footwear vs apparel vs bags) ──
def category(p):
    t = (p.get("product_type") or "").lower(); title = (p.get("title") or "").lower(); tags = " ".join(p.get("tags", [])).lower()
    blob = f"{t} {title} {tags}"
    if any(k in blob for k in ["slipper", "sandal", "mule", "boot", "loafer", "ballerina", "heel", "espadrille", "shoe", "footwear"]): return "Footwear"
    if any(k in blob for k in ["bag", "shoulder", "clutch", "tote"]): return "Bags"
    if any(k in blob for k in ["kimono", "set", "dress", "jacket", "vest", "pants", "top", "shirt", "skirt", "cardigan", "abaya", "shorts"]): return "Apparel"
    return "Other / untyped"

def subfamily(p):
    t = (p.get("product_type") or "untyped").strip().lower()
    return t if t and t != "" else "untyped"

rows = []
for p in prods:
    pr = price_of(p); cp = compare_of(p)
    rows.append({"title": p.get("title"), "cat": category(p), "sub": subfamily(p), "price": pr, "compare": cp,
                 "on_sale": bool(cp and pr and cp > pr), "discount_pct": round((1 - pr / cp) * 100) if (cp and pr and cp > pr) else 0,
                 "available": any(v.get("available") for v in p.get("variants", [])),
                 "sizes": [v.get("option1") for v in p.get("variants", []) if v.get("option1")],
                 "n_sizes": len({v.get("option1") for v in p.get("variants", []) if v.get("option1")}),
                 "created": (p.get("created_at") or "")[:7], "img": (p.get("images", [{}])[0] or {}).get("src")})

priced = [r for r in rows if r["price"]]

# ── price architecture per category ──
def band(price):
    return "<800" if price < 800 else "800-1,200" if price < 1200 else "1,200-1,800" if price < 1800 else "1,800-2,500" if price < 2500 else "2,500+"
BANDS = ["<800", "800-1,200", "1,200-1,800", "1,800-2,500", "2,500+"]
cat_price = {}
for cat in ["Footwear", "Apparel", "Bags", "Other / untyped"]:
    cr = [r for r in priced if r["cat"] == cat]
    if not cr: continue
    ps = [r["price"] for r in cr]
    cat_price[cat] = {"n": len(cr), "min": min(ps), "max": max(ps), "median": statistics.median(ps), "mean": round(statistics.mean(ps)),
                      "on_sale_pct": round(sum(1 for r in cr if r["on_sale"]) / len(cr) * 100),
                      "avg_discount": round(statistics.mean([r["discount_pct"] for r in cr if r["on_sale"]])) if any(r["on_sale"] for r in cr) else 0,
                      "bands": {b: sum(1 for r in cr if band(r["price"]) == b) for b in BANDS}}

# ── price tiers (entry / core / premium) ──
allp = sorted([r["price"] for r in priced])
q1, q3 = allp[len(allp) // 4], allp[3 * len(allp) // 4]
tiers = {"Entry (< EGP %d)" % q1: sum(1 for r in priced if r["price"] < q1),
         "Core (EGP %d-%d)" % (q1, q3): sum(1 for r in priced if q1 <= r["price"] <= q3),
         "Premium (> EGP %d)" % q3: sum(1 for r in priced if r["price"] > q3)}

# ── discount depth distribution ──
disc = [r["discount_pct"] for r in priced if r["on_sale"]]
disc_dist = {"10-20%": sum(1 for d in disc if 10 <= d < 20), "20-30%": sum(1 for d in disc if 20 <= d < 30),
             "30-40%": sum(1 for d in disc if 30 <= d < 40), "40-50%": sum(1 for d in disc if 40 <= d < 50), "50%+": sum(1 for d in disc if d >= 50)}

# ── size availability (footwear sizing anxiety = a verbatim theme) ──
size_counter = Counter()
for r in priced:
    for s in r["sizes"]: size_counter[str(s)] += 1
size_dist = [{"size": s, "n": n} for s, n in size_counter.most_common(14)]
avg_sizes = round(statistics.mean([r["n_sizes"] for r in priced if r["n_sizes"]]), 1)

# ── sub-family price ladder (top families) ──
fam = defaultdict(list)
for r in priced: fam[r["sub"]].append(r["price"])
fam_ladder = sorted([{"family": k, "n": len(v), "median": round(statistics.median(v))} for k, v in fam.items() if len(v) >= 4], key=lambda x: -x["n"])[:12]

# ── new-arrival price trend (by created month) ──
mon = defaultdict(list)
for r in priced:
    if r["created"]: mon[r["created"]].append(r["price"])
price_trend = [{"month": m, "median": round(statistics.median(v)), "n": len(v)} for m, v in sorted(mon.items()) if len(v) >= 3][-8:]

# ── DESIGN: download a representative product-image sample for visual review ──
sample = []
seen_cat = Counter()
for r in sorted(priced, key=lambda x: -(x["price"] or 0)):
    if not r["img"]: continue
    if seen_cat[r["cat"]] >= 6: continue
    seen_cat[r["cat"]] += 1
    fn = MED / f"{r['cat'][:4]}_{len(sample):02d}.jpg"
    try:
        req = urllib.request.Request(r["img"], headers=UA)
        with urllib.request.urlopen(req, timeout=25) as resp: fn.write_bytes(resp.read())
        sample.append({"file": fn.name, "cat": r["cat"], "sub": r["sub"], "title": r["title"], "price": r["price"]})
    except Exception:
        pass
    if len(sample) >= 22: break

out = {
  "n_products": len(prods), "n_priced": len(priced),
  "category_mix": dict(Counter(r["cat"] for r in rows)),
  "cat_price": cat_price, "tiers": tiers, "disc_dist": disc_dist,
  "size": {"avg_sizes_per_product": avg_sizes, "distribution": size_dist,
           "note": "Sizing is a real conversion friction (a recurring verbatim theme). Avg sizes/product and the size mix show where availability is thin."},
  "family_ladder": fam_ladder, "price_trend": price_trend,
  "sample_products": sample,
  "source": "Public Shopify catalog (products.json) · 250 products · 2026-07-09",
}
OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"WROTE {OUT.name}")
print(f"  category mix: {out['category_mix']}")
print(f"  cat price medians: " + " · ".join(f"{k}=EGP{v['median']:.0f} ({v['n']}, {v['on_sale_pct']}% sale)" for k, v in cat_price.items()))
print(f"  tiers: {tiers}")
print(f"  avg sizes/product: {avg_sizes} · size mix top: {[s['size'] for s in size_dist[:6]]}")
print(f"  product images downloaded for design review: {len(sample)}")
