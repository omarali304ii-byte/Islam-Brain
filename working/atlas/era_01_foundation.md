# [ATLAS] Era 1 — Foundation — Cielito Egypt (base 360, 2026-07-09)

ANNOUNCE: Establishes who Cielito is — identity, founder, ownership, product portfolio evolution (from catalog created-dates), the dropped fruit-leather story, and the dual-domain question.

## Agents Run
A01 company-profiler · A02 industry-classifier · A03 ownership-mapper · A04 leadership-profiler · A05 product-portfolio · A06 timeline-historian

## Findings

### A01/A02 — Identity & classification
Cielito Egypt is an Egyptian women's fashion D2C brand on Shopify at cielitoeg.com [S01, HELD]. Self-description: "Effortless style, premium quality. Handmade in Egypt. Affordable luxury. Fashion & footwear for every occasion" [S10, HELD as published bio / SELF_REPORTED as claims]. About page: "Crafted by Egyptian hands with internationally sourced materials — Italy, Spain, Germany, India, UK"; genuine-leather heels/sandals/mules with nappa lining plus a vegan-leather line [S02, SELF_REPORTED]. Taglines in use: "Moment of Style" (title tag) and "TIMELESS DESIGNS" (homepage banner) [S01, HELD]. Industry classification: women's footwear + apparel retail, D2C e-commerce, Egypt; Instagram business category is literally "Clothing (Brand)" — the platform label already reflects the apparel identity, not shoes [S10, HELD]. Verified IG (88,903 followers, 1,368 posts) [S10, HELD].

### A04 — Founder profile (LIKELY tier)
Founder: **Lolwa Awad** — International Relations (QMUL), economics/development (LSE), ex-PR career in UK + Egypt; founded ~Feb 2021 from a "one shoe, morning-to-soirée" insight [S11, LIKELY — two press sources: Fustany interview + Identity Magazine]. Founder-as-face is a captured, current asset: her personal IG `awadlolwa` posted 8 of the 34 earned brand-tagged posts in the R1 capture [S08, HELD; n=34 tagged posts, window 2026-05-21→07-08]. No LinkedIn/registry confirmation captured — founder identity stays LIKELY, route to watch-register.

### A03 — Ownership (GAP)
No corporate-registry, legal-entity, shareholder, or funding data was captured. Ownership structure, incorporation form, and any outside investment = **GAP** (inaccessible, not absent — GAFI/registry lookups are a data-pass route). Working assumption for internal modeling only: founder-owned bootstrapped D2C [HYPOTHESIS].

### A05 — Product portfolio & its evolution (computed from S04 created-dates)
250 live SKUs, EGP 400–7,600, median 1,200, 218 in stock, 96 on sale (38%) [S04, HELD]. Category bucketing (Shopify `type` field + title-keyword inference for the 128 untyped SKUs; 4 unresolvable) yields ~100 footwear, ~133 apparel, ~13 bags [S04, HELD data / ESTIMATE_ONLY bucketing]. New-SKU creation by half-year:

| Half | New SKUs | Footwear | Apparel | Bags | Read |
|---|---|---|---|---|---|
| 2022-H2 | 1 | 1 | 0 | 0 | oldest live SKU 2022-11-13 |
| 2023-H2 | 1 | 1 | 0 | 0 | thin surviving history |
| 2024-H1 | 27 | 16 | 7 | 4 | footwear-led build-out |
| 2024-H2 | 21 | 13 | 5 | 3 | footwear-led |
| 2025-H1 | 104 | 52 | 47 | 5 | peak drop rate (~4/wk); apparel arrives at parity |
| 2025-H2 | 47 | 17 | 26 | 1 | apparel overtakes |
| 2026-H1 | 49 | **0** | **48** | 0 | new-product energy is 100% apparel |

[S04, HELD counts; bucket labels ESTIMATE_ONLY]. **Caveat:** created-dates on the live catalog carry survivorship bias — deleted/archived SKUs are invisible, which is why a ~Feb-2021 brand shows its oldest live product in Nov 2022. The 2026-H1 pattern is still decisive: **zero new footwear in six months** while the site's largest structural collection remains "footwear" (76 products) and the About page is written entirely around leather footwear [S02/S05, HELD]. The brand has pivoted its launch cadence to apparel (Ramadan jalabeyas/abayas/kaftans clustered 2026-02-01→02-11, corsets/sets/blouses in May 2026 [S05, HELD]) while its stated identity is still a shoe brand — a live identity/assortment split. Taxonomy debt: 128/250 SKUs untyped, duplicate collections (Best Sellers/Best Selling/BestSelling; mules twice) [S04/S05, HELD].

### The dropped fruit-leather story
Press at launch positioned Cielito as the **first Egyptian fruit-leather brand** (aloe vera, prickly pear, pineapple) [S11, LIKELY that this was true at launch — press-only]. Grep of current cielitoeg.com and mycielito.com captures: **0 hits** [S11/S01/S12, HELD for captured pages]. The live About page mentions only genuine leather + vegan leather [S02]. **HYPOTHESIS:** the fruit-leather differentiator was dropped; the "vegan leather" line may be its residue. This matters strategically — it was the only defensible uniqueness claim vs the whole rival set, and it is currently unowned messaging territory.

### The dual-domain question
mycielito.com resolves as a live Shopify store ("My Cielito" — shoes collections) [S12, HELD that it exists]. Relationship to cielitoeg.com = **GAP**: test store, abandoned migration, sub-brand, or regional split are all open [HYPOTHESIS options only]. Risk if truly parallel: split SEO equity and brand confusion. Data-pass route + watch-register.

### A06 — Timeline
~Feb 2021 founded [S11, LIKELY] → 2022-11-13 oldest surviving SKU [S04, HELD] → 2024 footwear-led catalog build-out → 2025-H1 peak SKU creation and apparel parity → 2026-02 Ramadan apparel wave (77-product Ramadan umbrella collection; Ramadan Sale 2026 = 78) [S05, HELD] → 2026-H1 apparel-only drops → newest SKU "Safari set" 2026-06-15 [S04, HELD]. Ops identity throughout: Bosta + in-house couriers, Cairo/Alex 2-day, check-on-delivery, 7-day refund / 14-day exchange [S03, HELD]. No physical stores evidenced on any captured surface (absence on captured surfaces = HELD; true absence = unverified).

## Harness Enrichment — wiki-research
Entity-node candidate for `wiki/entities/cielito_egypt.md`: fields = {name: Cielito Egypt; domain: cielitoeg.com (+ mycielito.com, relationship GAP); founded: ~2021-02 (LIKELY); founder: Lolwa Awad (LIKELY); platform: Shopify; category: women's footwear→apparel D2C; IG: 88.9K verified; TikTok: 7.6K}. Relations: founder→awadlolwa (person node), rival→Dejavu (entity), market→egypt-footwear (concept). Key lesson for the skill: for young D2C brands, the Shopify `products.json` created-date series is a free, HELD-grade proxy for strategy evolution — capture it before reading any press.

## Harness Enrichment — agent-entity-reader
Canonical machine-readable record: `{"entity":"cielito-egypt","grade_map":{"identity":"HELD","founder":"LIKELY","founded":"LIKELY","ownership":"GAP","revenue":"GAP","portfolio_counts":"HELD","portfolio_buckets":"ESTIMATE_ONLY","fruit_leather_origin":"LIKELY(launch)/HYPOTHESIS(dropped)","second_domain":"HELD(exists)/GAP(relationship)"}}`. Reader rule reinforced: SELF_REPORTED (About-page quality claims) must never be upgraded by repetition across the brand's own surfaces — bio + About page are one voice, not two sources.

## Harness Enrichment — agent-retail-mr (retail vertical)
Retail read: this is a **category-migration case** (shoes → modest-wear apparel) executed silently through drop cadence rather than repositioning — the classic Egyptian D2C pattern of chasing Ramadan apparel margins while the storefront IA still sells the old identity. MR-dashboard implication: any tracker for this client needs a category-mix time axis (new SKUs by month × bucket), a sale-penetration KPI (38% baseline), and a taxonomy-hygiene flag (128 untyped SKUs break any automated category reporting).

## Era Snapshot
- Identity split confirmed: About page + largest collection say footwear, but 2026-H1 new SKUs are 48/49 apparel, 0 footwear [S04/S02 — HELD].
- Founder Lolwa Awad (QMUL/LSE, ex-PR), founded ~Feb 2021; her personal IG actively carries brand content [S11 LIKELY / S08 HELD].
- Launch-era fruit-leather differentiator has zero trace on live surfaces — likely dropped, currently unowned messaging territory [S11 — HYPOTHESIS].
- Ownership, legal entity, funding, revenue: all GAP (inaccessible, not absent) — registry lookup is a data-pass route.
- mycielito.com is live Shopify with unclear relationship to the main store — brand-confusion/SEO risk until resolved [S12 — HELD exists / GAP relationship].
