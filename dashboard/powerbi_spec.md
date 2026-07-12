# Cielito 360 — Power BI Spec
> Parallel Power BI build for a client who prefers a refreshable BI file over a web app. Same evidence base, same fail-closed discipline (no fabricated measures; GAP = disclosed).

## Data model (star schema)
**Fact tables**
- `fct_social_posts` — one row per captured post (platform, type, date, likes, comments, views, owner_handle, owned_earned_flag, language_flag, permanent_url). Seed from `_intel/social_intel.json` + owned/earned captures. n=120 (60 IG mixed + 60 TikTok).
- `fct_catalog` — one row per SKU (title, type, collection, price_egp, compare_at, on_sale_flag, in_stock, created_date, images). Seed from `catalog_full.json` (250 rows).
- `fct_instruments` — PageSpeed + agent-readiness scores (metric, device, value, captured_at).

**Dimensions:** `dim_date`, `dim_platform`, `dim_persona`, `dim_pillar`, `dim_competitor` (Dejavu populated; rest GAP flag), `dim_source` (S01–S13 with confidence grade).

## Core measures (DAX)
- `Owned ER % = DIVIDE(SUM(likes)+SUM(comments), [Follower Base]) ` (filtered owned) — baseline 0.006%.
- `Owned-vs-Earned Ratio = DIVIDE([Earned Median Views],[Owned Median Views])` — ~190.
- `Discount Surface % = DIVIDE(COUNTROWS(on_sale), COUNTROWS(catalog))` — 38%.
- `Catalog Hygiene % = 1 - DIVIDE(untyped_count, total_skus)` — 49% typed.
- `Followers per Video (TikTok) = DIVIDE([TikTok Followers],[TikTok Video Count])` — 13.
- Revenue/AOV/Conversion measures = **placeholder measures returning BLANK() with a "requires client data" label** (never 0).

## Report pages (8)
1. **Executive Summary** — verdict card, 3 decisions, owned-vs-earned KPI, north-star gauge.
2. **Social Command Center** — owned/earned bar, platform vitals, content leaderboard (with permanent URLs), language split.
3. **Content & Calendar** — pillars, feed-mix donut, 90-day timeline.
4. **Catalog & Pricing** — price-band histogram, discount surface, hygiene flags, category treemap.
5. **Website & Discoverability** — PageSpeed dual gauge, agent-readiness bars, security = clean.
6. **Competitive** — Dejavu comparison + rival framework table (GAP rows visible as "not yet measured").
7. **Audience & Market** — personas, market-size cards (ESTIMATE_ONLY banded), women-52% context.
8. **Evidence & Confidence** — source table with grades + data-pass gap list.

## Refresh & handoff
- Manual/scheduled refresh once client grants Shopify export + IG/TikTok Insights (closes G-01/G-03).
- Ships with seed CSVs (from `_intel/`) + a `validate_cielito_pbi.py` that checks: no null source ids, no plotted self-reported KPIs, GAP measures render as labels not zeros.
- Bilingual field labels (AR/EN) since the client audience is masri-first.

## Honesty rules (identical to React build)
Blocked routes = disclosed gaps, never zeros. Market sizes labeled ESTIMATE_ONLY. Fruit-leather = HYPOTHESIS caveat. No revenue fabrication — all financial measures BLANK+label until client data lands.
