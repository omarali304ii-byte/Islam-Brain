# GTM Era 14 — Power BI Intelligence — Cielito Egypt (base 360, 2026-07-09)
ANNOUNCE: Specifies the Power BI intelligence layer for the Cielito estate — data model, feeds, refresh cadence, and 6–8 report pages, every page mapped to persisted evidence and its grade.

## Agents Run
- Era owner not individually named in this lane's matrix row — executed by the GTM era-synthesis agent under Era 14.
- Skills invoked: `powerbi-survey-analytics`, `weighted-dashboard-builder`

## Findings

### 1. Design doctrine (binding)
- **Never plot HYPOTHESIS or GAP.** Missing data renders as a "To be baselined — requires client data" card, never a zero.
- **Every social visual carries n= and capture window** in its subtitle (owned IG n=17, 2026-05-31→07-04 [S08]; mixed IG n=60, 2026-05-21→07-08 [S08]; TikTok n=60, 2026-04-13→07-01 [S09]).
- **Market size is banded, never a point**: EGP 31.4bn retail 2025 (+9% YoY) vs USD-source ~$635M — unit/scope conflict, show as a band with both sources [S11, ESTIMATE_ONLY].
- No internal vocab (HELD/GAP/era codes) on any client-facing page; internal build pages may keep grades.

### 2. Data model (star schema)

| Table | Grain | Source / feed | Refresh | Grade ceiling |
|---|---|---|---|---|
| `FactCatalogSnapshot` | product × snapshot-date | Open `https://www.cielitoeg.com/products.json` (paginated) → Power Query; 250 SKUs, prices, availability, type, created/updated [S04] | Daily (free, no auth) | HELD |
| `DimProduct` | product handle | Derived from catalog feed: title, type (128/250 untyped — model must tolerate blank type), price band, first-seen date (2022-11-13→2026-06-15) [S04] | Daily | HELD |
| `DimCollection` + `BridgeProductCollection` | collection / product-collection pair | `raw_collections.json` capture: 30 collections incl. duplicates (Best Sellers/Best Selling/BestSelling; mules ×2) [S05] | Weekly | HELD |
| `FactSocialPost` | post × capture | Apify pulls: IG owned (17 posts), IG mixed/tagged (60 items), TikTok (60 videos) [S08][S09] | Weekly–monthly, **paid** (~$0.25 IG + $0.18 TikTok per pull [S08][S09]) — cost-gated per estate $25 rule | HELD (n, window mandatory) |
| `FactUGCLedger` | earned/tagged post | Subset of mixed capture: 34 tagged/UGC posts incl. 8 by founder `awadlolwa` [S08][S11] | With social pull | HELD |
| `FactInstrument` | audit × date | PageSpeed (mobile 55 / desktop 98 / SEO 100 / accessibility 91 mobile, 82 desktop) [S06]; agent-readiness (Grade B, 72/100, security CLEAN) [S07] | Monthly (free APIs/scripts) | HELD |
| `DimDate` | day | Generated; flag columns for Ramadan/Eid windows (catalog tags prove seasonal merchandising [S04][S05]) | Static | — |
| `DimChannel` | channel | IG-owned / IG-earned / TikTok / FB (placeholder) / Site | Static | — |
| `FactOrders` *(placeholder)* | order | **Requires client data** — Shopify export (see Era 13) | On receipt | GAP until delivered |

Relationships: single-direction from Dims to Facts; `FactCatalogSnapshot[snapshot_date]` enables catalog-drift measures (sale-share over time, stock-outs, new-SKU velocity) — the daily free snapshot is the model's heartbeat.

### 3. Refresh cadence & cost gate
| Feed | Cadence | Cost | Note |
|---|---|---|---|
| Catalog (products.json) | Daily | $0 | Open endpoint verified 2026-07-09 [S04] |
| Collections | Weekly | $0 | [S05] |
| Instruments (PSI + agent-readiness) | Monthly | $0 | [S06][S07] |
| Social (Apify IG + TikTok) | Monthly default; weekly during campaign | ~$0.43/pull | Paid — logged against the cumulative $25 estate gate; each pull appends, never overwrites (longitudinal ER tracking) |
| Orders/CRM | On client delivery | $0 | GAP until Era-13 discovery completes |

### 4. Report pages (7 pages, each mapped to evidence)

| # | Page | Key visuals | Evidence |
|---|---|---|---|
| 1 | **Executive Overview** | Follower base 88,903 [S10] vs owned median 3 likes / ER 0.006% (n=17, 2026-05-31→07-04) [S08]; earned max 5,930 likes / 124,937 views (~200× owned median) [S08]; catalog 250 SKUs / 218 in stock / 38% on sale [S04]; banded market card [S11 ESTIMATE_ONLY] | S04, S08, S10, S11 |
| 2 | **Catalog Health** | Untyped share 128/250; price bands (88 <1,000 / 156 1,000–2,500 / 4 2,500–5,000 / 2 >5,000 EGP, median 1,200) [S04]; duplicate-collection audit table (3× best-seller variants, mules ×2) [S05]; stock-out list (32 unavailable) | S04, S05 |
| 3 | **Seasonality & Promo Calendar** | Ramadan collections 77/78 products; Black Friday, Eid 30% OFF, B1G1 tags [S04][S05]; SKU-creation timeline 2022-11→2026-06; DimDate Ramadan flags for planning Ramadan 2027 | S04, S05 |
| 4 | **Social Performance — Owned vs Earned** | Owned IG: median 3 likes, mean 5.1, video views median 655, cadence 3.5/wk, 16/17 English-only captions, 0 WhatsApp CTAs, 0 offers (n=17) [S08]; earned/tagged benchmark; TikTok: 7,608 followers vs 584 videos, plays median 1,220, comments median 0 (n=60, 2026-04-13→07-01) [S09]; Arabic-content outperformance callout (باشا مصر 14.8K plays) [S09] | S08, S09, S10 |
| 5 | **UGC & Creator Ledger** | 34 tagged posts, 8 founder posts; per-creator reach table w/ URLs; whitelist-candidate ranking | S08, S11 |
| 6 | **Website & Agent Instruments** | PSI trend (mobile 55 / desktop 98 / SEO 100) [S06]; agent-readiness Grade B 72/100, bot access 25, protocol discovery 33, security CLEAN [S07]; monthly trendline | S06, S07 |
| 7 | **Competitive Watch** | Dejavu 289K IG / FB ~2.3M vs Cielito 88.9K [S10][S11 LIKELY]; rival roster (Shoe Room, Pixie, Achilles, Jayda Hany, Bulga, Elia, Ramla, CHOU, Morena, Parfois) as a watch-list table — metrics beyond Dejavu = *inaccessible, not absent* → greyed "pending data pass" cells | S10, S11 |
| 8 *(dormant)* | **Sales & CRM** | Ships as a locked page of "To be baselined" cards until the Era-13 Shopify export lands | GAP |

### 5. Measures (illustrative DAX targets)
`Owned ER % = DIVIDE(median likes+comments, 88903)` with n/window in tooltip [S08][S10]; `Sale Share % = on_sale / total SKUs` per snapshot [S04]; `Earned-vs-Owned Multiple` [S08]; `Untyped SKU %` data-quality KPI (target <10%, currently 51.2%) [S04]; `Catalog Drift` = week-over-week availability delta [S04].

## Harness Enrichment — powerbi-survey-analytics
**Pattern captured: open Shopify `products.json` as a free daily Power Query feed with snapshot dating.** Any Shopify client (Cielito verified [S04]) exposes a paginated, auth-free JSON catalog; ingesting it daily with a `snapshot_date` column turns a static catalog into a longitudinal fact table — enabling sale-share drift, stock-out alerts, and new-SKU velocity at $0. Added as the default "heartbeat feed" for all D2C Power BI estates; pairs with the incremental-refresh policy (RangeStart/RangeEnd on snapshot_date).

## Harness Enrichment — weighted-dashboard-builder
**Pattern captured: disclosure-gated visuals for banded/thin evidence.** Two rules generalized: (1) every sampled-metric visual carries n= and capture window in the subtitle (owned IG n=17 is a 5-week window, NOT account history — plotting it unlabelled would overstate certainty) [S08]; (2) conflicting market sizes render as a two-source band visual (EGP 31.4bn local-currency vs ~$635M USD-source), never a single KPI card [S11 ESTIMATE_ONLY]. These are the honest-display equivalents of survey weighting: when you can't weight to the population, you disclose the frame.

## Era Snapshot
- Model heartbeat = free daily snapshot of the open products.json endpoint (250 SKUs); catalog-drift measures come from snapshot dating. [S04, HELD]
- 7 live report pages + 1 dormant CRM page fully mapped to persisted evidence; nothing plotted from HYPOTHESIS/GAP. [S04–S11, mixed grades as tabled]
- Social feed is the only paid refresh (~$0.43/pull IG+TikTok), cost-gated and append-only for longitudinal ER tracking. [S08][S09, HELD]
- Flagship diagnostic visual: owned ER 0.006% median (n=17) vs earned 200× multiple — the single chart that justifies the turnaround plan. [S08][S10, HELD]
- Data-quality KPI built in: 51.2% of SKUs untyped + duplicate collections — a client-visible hygiene metric with a target. [S04][S05, HELD]
