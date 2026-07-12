# [ATLAS] Era 19 — Evolution — Cielito Egypt (base 360, 2026-07-09)
ANNOUNCE: This era extracts what the cielito-egypt base-360 run teaches the Mega Research Pipeline itself — capture-pattern lessons, corrective-run doctrine, and wave-template recommendations — so the next estate run starts smarter.

## Agents Run
- **A82 — Run Retrospector** (replays the capture ledger and flags anomalies)
- **A83 — Pattern Extractor** (converts anomalies into reusable pipeline patterns)
- **A84 — Skill-Gap Mapper** (maps patterns to existing/needed skills)
- **A85 — Template Mutator** (drafts wave-template amendments)
- **A86 — Knowledge Router** (routes lessons to pass-knowledge targets)

## Findings

### Lesson 1 — IG scraper searchType pollution → the corrective-run pattern (HELD, this run's own ledger)
The first paid Instagram pull (R1, $0.138 [S08]) came back as a **mixed corpus**: 60 items of which only 26 were owned posts; 34 were tagged/UGC items, including 8 posts by founder account awadlolwa [S08, HELD]. The pollution is visible in the digest itself: `social_intel.json` records the capture "handle" as `haninemoussaa` — a UGC creator, not the brand [S08, HELD]. The scraper's searchType had drifted from profile-owned to tag/mention scope.
The run recovered with a **corrective re-pull (R1b)**: a 50-item owned-only request that yielded 17 unique owned posts, window 2026-05-31→07-04, bringing total IG spend to $0.253 [S08, HELD]. Total paid social this run: $0.434 (IG $0.253 + TikTok R2 $0.181) [S08/S09, HELD].
**Pattern to codify:** every Apify social pull must pass a *provenance assertion* before digest-build — `ownerUsername == expected handle` on ≥90% of items, else auto-flag POLLUTED and queue a corrective run with pinned searchType. Cost of the corrective pattern here was ~$0.12 — trivially cheap versus shipping a polluted ER baseline.

### Lesson 2 — Owned-vs-earned accidental capture = a feature, formalize it (HELD)
The "polluted" R1 corpus accidentally produced the single most decision-relevant finding of the whole 360: the owned/earned gap. Owned posts: median 3 likes, median ER 0.006%, median video views 655 (n=17, 2026-05-31→07-04) [S08, HELD]. Earned/tagged posts in the same mixed window (2026-05-21→07-08, n=34 of 60): max 5,930 likes / 124,937 views — roughly **~200x owned median** [S08, HELD]. Without the pollution, the earned side would never have been captured at base-360 cost.
**Pattern to codify:** promote this from accident to a deliberate **dual-scope social capture** — one owned-profile pull + one tagged/mention pull per platform, digested separately, with an owned-vs-earned ratio computed as a standard KPI. For Egyptian D2C fashion this ratio is arguably the wedge-detection metric (here it exposed that the brand's distribution problem is owned-channel execution, not brand appeal).

### Lesson 3 — Open products.json as the standard retail probe (HELD)
The Shopify open `products.json` endpoint delivered the entire 250-SKU catalog — prices (EGP 400–7,600, median 1,200), availability (218 in stock), sale flags (96/250 = 38%), type hygiene (128/250 untyped), duplicate collections (Best Sellers/Best Selling/BestSelling; mules twice), and a dated catalog span 2022-11→2026-06 — at **$0, HELD grade** [S04/S05]. This one free probe powered the catalog, merchandising-hygiene, and seasonality (Ramadan/Eid tag) analyses.
**Pattern to codify:** make `GET /products.json` (paginated) + `GET /collections.json` the mandatory first probe for ANY retail/D2C client on Shopify (and equivalents on Salla/Zid/WooCommerce). It should run before any paid route is even proposed — several data-pass routes become unnecessary when the catalog is free.

### Lesson 4 — Social-audit bridge value (HELD)
Running the instrument audits (PageSpeed M55/D98, SEO 100 [S06]; agent-readiness Grade B 72/100, security CLEAN [S07]) in the same run as the social capture created cross-signal findings neither lane produces alone: a technically healthy, SEO-perfect site starved of social-driven demand (owned ER 0.006% [S08]), 0 WhatsApp CTAs across captured captions [S08, HELD for captured surfaces] against Egypt's WhatsApp-conversion norm, and 16/17 English-only captions against masri-outperforms evidence (باشا مصر: 14.8K TikTok plays vs 1,220 median [S09, HELD]). The bridge — instruments × social × catalog — is where the strategy writes itself.
**Pattern to codify:** wave templates should declare an explicit BRIDGE section consuming ≥2 lanes' outputs, not just per-lane findings.

### Wave-template recommendations (for the generalized Haj-Arafa-derived templates)
| # | Template | Amendment | Basis |
|---|----------|-----------|-------|
| 1 | base-360 social lane | Add provenance assertion + corrective-run trigger (Lesson 1) | S08 |
| 2 | base-360 social lane | Dual-scope owned+earned capture, owned/earned ratio KPI (Lesson 2) | S08 |
| 3 | base-360 intake | products.json/collections.json free probe = mandatory pre-paid gate (Lesson 3) | S04/S05 |
| 4 | hero wave | Owned/earned gap chart + language-split (masri vs EN) panel as standard modules | S08/S09 |
| 5 | commercial waves | Catalog-hygiene score (untyped %, duplicate collections, stale tags) as a reusable metric | S04/S05 |
| 6 | all waves | Second-domain check (here: mycielito.com resolves, relationship GAP [S12]) as a standard 1-min probe | S12 |

## Harness Enrichment — agent-skill-builder
Candidate skill spawn: **`social-provenance-gate`** — a small fail-closed validator run after every Apify social pull: asserts owner-handle purity ≥90%, splits owned vs earned into separate digests, computes the owned/earned ratio KPI, emits POLLUTED/CLEAN verdict + corrective-run spec (actor, searchType, est. cost). Inputs: raw posts JSON + expected handle. Outputs: `provenance_verdict.json` + split digests. Evidence base: this run's R1 pollution + R1b corrective ($0.12 marginal cost) [S08]. Fits the existing free-first/paid-approve doctrine; no new credentials needed.

## Harness Enrichment — audit-run
Cross-platform audit value confirmed for the INSTRUMENT lane specifically: PageSpeed and agent-readiness are deterministic own-endpoint scripts [S06/S07], so audit-run's multi-platform comparison adds nothing there — SKIP instruments in future audit-run passes. Where audit-run DOES add value on this estate: the interpretation layer (e.g., is owned ER 0.006% "catastrophic" or "typical for 89K-follower Egyptian fashion"? [S08 vs no rival owned-ER baseline = GAP]). Recommend audit-run target = the synthesis eras, not the capture eras, with the rival-ER gap flagged as the claim most needing cross-model validation.

## Harness Enrichment — pass-knowledge
Routing map for this run's lessons: (1) provenance-gate + dual-scope pattern → `mega-research-pipeline` skill master prompt (capture doctrine section) and Apify REST notes in memory (`apify-rest-scrape-unlock`); (2) products.json standard probe → mega intake checklist + GTM scrape-engine free-first ladder (it belongs on rung 1, before cloudscraper); (3) owned/earned ratio KPI + masri-language-split module → hero-wave template and `media-analyzer-run` (MENA-aware recommendation engine already models language effects); (4) catalog-hygiene score → dashboard compile contract for the queued hero-wave build (Era 21 trigger). All routes are file-level recommendations only — no cross-system writes performed by this era (out of lane scope).

## Era Snapshot
- R1 IG pull was scope-polluted (26/60 owned); corrective R1b recovered a clean owned baseline for +$0.115 — corrective-run pattern proven cheap and should be automatic [S08, HELD].
- The pollution accidentally captured the run's biggest finding: earned/UGC posts reach ~200x owned median engagement — dual-scope capture should be formalized as a standard KPI [S08, HELD].
- Open Shopify products.json delivered the full 250-SKU catalog at $0 with HELD grade — mandatory first probe for all retail clients before any paid route [S04/S05, HELD].
- Instrument × social × catalog bridging produced the core strategic contradiction (healthy site, dead owned social, zero WhatsApp bridge) — wave templates need explicit BRIDGE sections [S06/S07/S08, HELD].
- One skill spawn proposed (`social-provenance-gate`) + 6 wave-template amendments drafted; no baseline exists yet for rival owned-ER, so the "catastrophic" framing keeps a comparative caveat [GAP: rival owned-ER metrics inaccessible, not absent].
