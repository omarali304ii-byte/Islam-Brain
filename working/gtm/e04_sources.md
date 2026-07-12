# [GTM] Era 4 — Source Mapping — Cielito Egypt (base 360, 2026-07-09)

ANNOUNCE: Mirrors the run's SOURCE_REGISTRY into the GTM lane with a per-source quality assessment (tier, freshness, independence, known bias, coverage) and converts the blocked-route list into a costed future-source queue for the data pass.

## Agents Run
- **GTM Source Harvester** (era owner) — registry mirror + quality grading
- source-quality-assessor (sub-pass) — independence/bias/coverage scoring per source
- blocked-route-cataloguer (sub-pass) — future-source queue construction

## Findings

### Source quality map (mirror of SOURCE_REGISTRY, S01–S13)

| ID | Source | Tier | Freshness | Independence | Quality assessment | Grade ceiling |
|----|--------|------|-----------|--------------|--------------------|---------------|
| S01 | cielitoeg.com homepage | Primary capture | 2026-07-09 (same-day) | Brand-controlled surface | Clean capture; nav confirms two-line business (FOOTWEAR + CLOTHES); footer social links = Instagram + Threads only — no Facebook/TikTok/WhatsApp link on site [S01] | HELD |
| S02 | About-us page | Primary capture | 2026-07-09 | Brand-controlled (marketing copy) | Rich positioning copy ("Moment of Style", Egyptian hands + materials from Italy/Spain/Germany/India/UK, genuine + vegan leather lines). NOTE: zero mention of fruit leather — key negative evidence for Era 5/strategy [S02] | SELF_REPORTED for quality claims; HELD for what-the-page-says |
| S03 | Shipping + refund policy | Primary capture | 2026-07-09 | Brand-controlled (operational policy) | High-value ops detail: Bosta + in-house couriers, Cairo/Alex 2 days, Cairo 24h express, check-while-courier-waits (COD culture), partial-delivery workaround via in-house courier [S03] | HELD (as published policy) |
| S04 | Full Shopify catalog (250 products, open products.json) | Primary capture | 2026-07-09 | Machine-read, not copy — highest-trust commercial surface | 250 SKUs, EGP 400–7,600, median 1,200, 218 in stock, 96 on sale (38%), 128/250 untyped, catalog span 2022-11-13 → 2026-06-15. Data-hygiene defects (untyped products, stale seasonal tags) are themselves findings [S04] | HELD |
| S05 | Collections structure (30 collections) | Primary capture | 2026-07-09 | Machine-read | Duplicate-collection defect confirmed: Best Sellers (4) / Best Selling (60) / BestSelling (20); merchandising taxonomy quality is weak — feeds the site-hygiene recommendation [S05] | HELD |
| S06 | PageSpeed audit | Instrument (Google PSI API) | 2026-07-09 | Independent instrument | Mobile 55 / Desktop 98 / SEO 100. Mobile perf is the credible conversion-drag signal; SEO 100 means the gap is NOT discoverability basics [S06] | HELD |
| S07 | Agent-readiness audit | Instrument (own-endpoint script) | 2026-07-09 | Independent instrument | Grade B 72/100 (bot access 25, protocol discovery 33), security CLEAN — better than most Egypt SMBs; sub-scores define the GEO backlog [S07] | HELD |
| S08 | Instagram captures (mixed 60 + corrective owned 50) | Primary capture (paid R1/R1b, $0.253) | Windows: mixed 2026-05-21→07-08 (n=60); owned 2026-05-31→07-04 (n=17 unique owned) | Platform data via Apify — independent of brand claims | Two-capture design is a strength: mixed pull captures earned/UGC universe; corrective owned pull isolates brand-account truth (median 3 likes, ER 0.006%). CAVEAT: mixed-capture digest keys `handle: haninemoussaa` — it is a tag/mention-based pull, NOT an owned-account pull; never quote its blended stats (median 3 likes but mean 175, max 5,930) as owned performance [S08] | HELD (n + window MUST be disclosed) |
| S09 | TikTok capture (60 videos) | Primary capture (paid R2, $0.181) | Window 2026-04-13→07-01, n=60 of 584 account videos | Platform data | Account-level (7,608 followers, 35.3K hearts, 584 videos) + per-video stats. Capture covers ~10% of account history — recent-window truth only, not lifetime [S09] | HELD (n=60 disclosed) |
| S10 | IG profile parent data | Primary capture | 2026-07-09 | Platform data | 88,903 followers / 1,368 posts / verified / business "Clothing (Brand)" / 17 highlights / bio link → cielitoeg.com ONLY (no WhatsApp). Bidirectionally confirms site↔IG identity chain with S01 footer [S10] | HELD |
| S11 | Web-search corpus | Secondary | 2026-07-09 capture of undated/older pages | Mixed independence: press interviews (founder-friendly), paid market reports (methodology opaque) | Founder identity (2 press sources), fruit-leather origin story (press-only, absent from live site → HYPOTHESIS), market size EGP 31.4bn 2025 +9% vs ~$635M USD source — UNIT/SCOPE CONFLICT, band both, plot neither as settled. Rival roster (11 names) is discovery-grade, not enriched [S11] | LIKELY max; market sizes ESTIMATE_ONLY; fruit-leather HYPOTHESIS |
| S12 | mycielito.com raw HTML | Primary capture | 2026-07-09 | Machine-read | Existence HELD. Era 5 finding: internal Shopify identifiers point to a DIFFERENT business (see e05_entities.md) — this source's value flipped from "possible second brand domain" to "name-collision disambiguator" [S12] | HELD that it exists; relationship resolved to LIKELY-distinct in Era 5 |
| S13 | Operator intake | Operator | 2026-07-09 | Operator context | Lens stack, WOM pitch trigger, approvals. Context only — never cite in client-facing evidence [S13] | context only |

### Blocked routes → future-source queue (inaccessible ≠ absent)

| FQ | Future source | Why blocked now | Route type / est. cost | What it would unlock |
|----|--------------|-----------------|------------------------|----------------------|
| FQ1 | Facebook page stats (cielitoegypt) | FB blocks anonymous scrape | Paid Apify FB actor, ~$0.10–0.50 | Largest-audience channel truth (rival Dejavu shows FB ≈ 2.3M likes — FB may dwarf IG for this category) [S11 LIKELY] |
| FQ2 | Rival IG/TikTok metrics (10 rivals beyond Dejavu snippet) | Not yet captured | Paid Apify profile scrapes, ~$0.05–0.15 total | Real competitive ER/cadence benchmark — currently the 200x owned-vs-UGC gap has no rival baseline |
| FQ3 | Rival Shopify catalogs (achilleseg.com, jaydahany.com, bulga.co, eliashoewear.com, parfoisegypt.com) | Not yet probed | **FREE** — /products.json endpoint probe (same technique as S04) | Price-band war map vs Cielito's EGP 400–7,600; zero-cost, highest ROI route in queue |
| FQ4 | Google reviews / Maps presence | Not captured | Free-first (Maps search) → paid actor if blocked | Service-quality voice-of-customer; COD/exchange friction signals |
| FQ5 | Marketplace presence (Noon / Amazon EG / Jumia) | Not captured | Free search probes | Channel-strategy fact: D2C-only vs marketplace-diversified |
| FQ6 | Meta Ad Library (Cielito + rivals) | Not captured | **FREE** — public ads.facebook.com library | Paid-media activity: is anyone buying the demand Cielito's organic isn't capturing? |
| FQ7 | Conversion/revenue data | Client-side only | Requires client engagement (WOM pitch) | The only route to ROAS/AOV truth; everything else stays top-of-funnel |
| FQ8 | Threads account content | Footer links Threads [S01] but never captured | Free/cheap probe | Confirms whether Threads is live or a dead footer link |

## Harness Enrichment — source-validator
Cross-validation checks executed on the registry (real, this run):
1. **Follower consistency:** S08 mixed capture `followers_from_capture` 88,903 == S10 profile 88,903 → PASS (same-day coherence).
2. **Catalog coherence:** S04 total 250 vs S05 page-1 detail (30 returned, price min 400 / max 2,720 subset within S04's 400–7,600 envelope) → PASS; S05 duplicate collections independently corroborate S04's untyped-product hygiene defect.
3. **Identity chain:** S10 bio externalUrl `cielitoeg.com` ↔ S01 footer Instagram link → bidirectional PASS (HELD).
4. **Currency sanity:** S04 prices in EGP ("LE" on site [S02]) vs S12 mycielito.com `Shopify.currency = USD`, `country = US` → domains FAIL to co-validate → escalated to Era 5 as distinct-entity evidence.
5. **Market-size conflict:** S11 EGP 31.4bn (+9% YoY) vs ~$635M USD source — at plausible 2025 FX (~EGP 47–50/USD) EGP 31.4bn ≈ $630–670M, so the two MAY reconcile, but scope definitions unverified → keep ESTIMATE_ONLY, band as "EGP ~31bn / ~$0.6–0.7bn retail 2025", never plot a single point.
6. **Window discipline:** all social stats carry n= and window per rule 2; S09 covers only ~10% of TikTok account history — flagged so no one extrapolates lifetime performance from a 79-day window.

## Era Snapshot
- 13 sources registered; 10 carry HELD ceilings, all same-day (2026-07-09) captures — freshness is uniform, decay clock starts now. [HELD]
- Strongest evidence spine = machine-read surfaces (S04 catalog, S06/S07 instruments, S08–S10 social captures); weakest = S11 secondary corpus where market size stays ESTIMATE_ONLY due to unit/scope conflict. [HELD]
- S12 (mycielito.com) flipped in value: from "possible second domain" to name-collision disambiguator — internal Shopify IDs indicate an unrelated US/Mexican-crafts store. [LIKELY, detailed in Era 5]
- Two FREE future routes (rival products.json probes FQ3; Meta Ad Library FQ6) offer the highest intelligence-per-dollar and should lead the next data pass. [HELD as routes; findings pending]
- 8 blocked/uncaptured routes are catalogued as future sources — none may ever be cited as absence of the underlying fact. [HELD, binding]
