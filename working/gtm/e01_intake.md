# [GTM] Era 1 — Intake & GTM Maturity Assessment — Cielito Egypt (base 360, 2026-07-09)

ANNOUNCE: Establishes what kind of business Cielito actually is today — channel model, GTM maturity stage per motion, and the intake baseline every later GTM era builds on.

## Agents Run
- **GTM ICP Strategist** (era owner) — maturity staging + intake framing
- research-planner agent — evidence-route planning (which sources answer which intake question)
- market-research agent — business-model classification against Egypt D2C norms
- gtm-okr-builder agent — baseline-metric extraction for OKR seeding

## Findings

### Business classification
Cielito Egypt is a **single-channel Shopify D2C** women's fashion brand (leather footwear + bags + kimonos/clothes) at cielitoeg.com [S01, HELD], founded ~Feb 2021 [S11, LIKELY], founder Lolwa Awad [S11, LIKELY — two press sources]. Bio positioning: "Effortless style, premium quality. Handmade in Egypt. Affordable luxury." [S10, HELD]. About page claims Egyptian craftsmanship with materials from Italy/Spain/Germany/India/UK [S02, SELF_REPORTED].

### GTM maturity scorecard (evidence-staged)

| Motion | Stage | Evidence |
|---|---|---|
| D2C web store | **OPERATING** | Shopify live, 250 SKUs, 218 in stock, open products.json [S04, HELD]; SEO 100, desktop 98 [S06, HELD] |
| Fulfillment/COD | **OPERATING, Egypt-native** | Bosta + in-house couriers; Cairo/Alex 2 days; check-while-courier-waits (COD culture served) [S03, HELD] |
| Seasonal merchandising | **PROVEN MUSCLE** | Ramadan machinery: 77-product Ramadan collection, Ramadan 2026 tags, Eid 30%-off tags, Black Friday tags [S05, HELD] |
| Catalog hygiene | **IMMATURE** | 128/250 untyped products; duplicate collections (Best Sellers/Best Selling/BestSelling; mules ×2); 96/250 on sale (38%) [S04/S05, HELD] |
| Social audience asset | **BUILT** | IG 88,903 followers, 1,368 posts, verified [S10, HELD] |
| Social activation | **BROKEN** | Owned IG median 3 likes, ER 0.006% median, n=17, window 2026-05-31→07-04 [S08, HELD]; TikTok 7,608 followers vs 584 videos, median 0 comments, n=60, window 2026-04-13→07-01 [S09, HELD] |
| Conversion bridge (WhatsApp) | **ABSENT on captured surfaces** | 0 WhatsApp CTAs in 17 owned captions [S08, HELD]; bio link = website only [S10, HELD]. Egypt context law: WhatsApp is THE conversion bridge — this is the single largest funnel hole. HELD for captured surfaces only |
| Offer/promo activation in content | **ABSENT** | 0 offer-language captions in n=17 owned window [S08, HELD] despite 38% of catalog being on sale [S04, HELD] — the store discounts, the content never says so |
| Marketplace / wholesale / retail | **GAP** | Noon/Amazon EG/Jumia presence = uncaptured blocked route (inaccessible ≠ absent) [registry blocked-list]; no physical stores evidenced on captured surfaces [S01/S02, HELD-for-captured] |
| Positioning consistency | **DRIFTED** | Press-era "first Egyptian fruit-leather brand" (aloe/prickly pear/pineapple) has ZERO trace on live site (grep: 0 hits) [S11, HYPOTHESIS: differentiator dropped] |
| Second storefront | **GAP** | mycielito.com resolves (Shopify) [S12, HELD it exists]; relationship to main domain = GAP |
| Mobile web performance | **DRAG** | PageSpeed mobile 55 vs desktop 98 [S06, HELD] — Egypt traffic is mobile-first; this taxes every paid/organic click |

### Intake verdict
Cielito is a **Stage-2 D2C: infrastructure-mature, demand-immature**. The hard parts most Egyptian D2Cs fail at (COD-native fulfillment, Ramadan merchandising cycles, verified 89K audience, clean security posture [S07, HELD]) already exist. What is missing is the entire *activation layer*: no WhatsApp bridge, no offer language, English-only captions to a masri-commenting audience (16/17 owned captions English [S08, HELD] vs Arabic purchase-intent comments like "مقاس البنطلون بليز" [S08, HELD]), and a ~200x gap between earned UGC reach (5,930 likes / 124,937 views max) and owned median (3 likes) [S08, HELD]. The GTM problem is not audience acquisition — it is conversion of an audience already built.

### Bound code — free-stub log
`gtm_maturity_assessment.py` **NOT RUN** — reason: bound to internal GTM System state, not wired for external-client estates. Assessment above performed manually from persisted evidence under the same rubric (motion × stage × evidence). Logged as free-stub; wiring it for Mega estates is a candidate GTM-System upgrade.

## Harness Enrichment — research-planner
Evidence-route map produced for downstream eras: (1) persona evidence lives in S08 raw comments + UGC creator posts, NOT in any demographic instrument — route e02 to raw captures; (2) market numbers only exist at S11 secondary tier with a known EGP-vs-USD scope conflict — route e03 to banded framing, never point estimates; (3) revenue/conversion questions have NO local route — pre-register as data-pass proposals (GA4/Meta pixel access = client-side). Planning rule captured: for Shopify targets, products.json + collections.json are the highest-density free intake source — always pull before any paid route.

## Harness Enrichment — market-research
Enrichment: Egypt D2C maturity rubric refined with a COD-culture dimension — "check-on-delivery while courier waits" [S03] is a trust feature, not a logistics footnote; rubric now scores COD-flexibility as a GTM asset class for Egypt clients. Also captured: 38% catalog-on-sale with 0% offer-language-in-content is a reusable diagnostic pattern ("silent discounting") for Egyptian fashion D2C audits.

## Harness Enrichment — gtm-okr-builder
Baseline metrics extracted for OKR seeding (all measured, dated, n-disclosed):
- O1 Activate the owned audience: KR1 owned IG median ER 0.006% → ≥0.5% (baseline n=17, 2026-05-31→07-04 [S08]); KR2 masri/Arabic caption share 1/17 → ≥60%; KR3 median video views 655 → ≥5,000.
- O2 Build the conversion bridge: KR1 WhatsApp CTA coverage 0% → 100% of product posts [S08]; KR2 WhatsApp link in IG bio 0 → 1 [S10].
- O3 Fix the funnel floor: KR1 PageSpeed mobile 55 → ≥75 [S06]; KR2 untyped SKUs 128 → 0 [S04]; KR3 duplicate collections 3 Best-Seller variants → 1 [S05].
Targets are direction-setting seeds; validation requires client-side data (GAP).

## Era Snapshot
- Cielito = Stage-2 D2C: fulfillment, COD culture, Ramadan merchandising and an 89K verified audience already OPERATING; activation layer absent — HELD [S03/S04/S05/S08/S10]
- Single-channel dependence: no marketplace/wholesale/retail evidenced; those routes are uncaptured, not disproven — GAP (inaccessible ≠ absent)
- Largest funnel hole = no WhatsApp bridge anywhere on captured surfaces (0/17 captions, bio = website only) — HELD [S08/S10]
- Silent discounting: 38% of catalog on sale yet 0 offer-language posts in the owned window — HELD [S04+S08]
- Press-era fruit-leather differentiator absent from live site → positioning drift — HYPOTHESIS [S11]; mycielito.com relationship — GAP [S12]
