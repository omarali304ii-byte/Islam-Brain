# Cielito 360 — React Dashboard Spec (WOM pitch centerpiece)
> Route: `esm-landing /dashboard/cielito-360` · Audience lens: **Executive (primary)** + Marketer (secondary) · Built from `strategy.json` + `_intel/` + `instruments/` (all HELD/graded) · Compile contract: `build_cielito_data.py` **fails closed** on banned vocab, unsourced KPIs, unguarded money numbers, missing media.
> Client-safe: NO internal labels (ATLAS/MIDAS/eras/HELD/lens/L0-L3 codes) appear in rendered copy. GapPlaceholder cards used for every "to be baselined" number — nothing fabricated.

## Why this beats a generic report deck
A tactical agency ships a slide deck of screenshots. This ships a **living command center**: the owner sees a verdict in 30 seconds, the marketer drills into a Social Command Center with real post-level data, and every claim is one click from its evidence. The differentiator WOM demonstrates is the **owned-vs-earned engine diagnosis** — the single chart that reframes the whole account — backed by real scraped data, not opinion.

## Information Architecture (Executive shell)

**L0 — Decision Dock (persistent top strip, every screen):**
Verdict headline · 3 load-bearing decisions (D-02 WhatsApp → D-03 Hygiene+Arabic → D-01 Creator engine) · one "financial impact: to be baselined" honesty chip · north-star = owned engagement-rate recovery.

**L1 — The Five-Screen Story (the pitch spine):**
| Screen | Answers | Hero visual |
|---|---|---|
| 1. What's happening | 89K followers, 3-like posts, ~190× UGC gap | Owned-vs-earned bar (THE chart) |
| 2. Why | English in a masri market · no WhatsApp · identity drift | Language-performance split + funnel-with-gap |
| 3. Financial impact | What a fixed engine is worth (to be baselined) | Baseline cards + scenario shell (locked until client data) |
| 4. Decide | 3 sequenced decisions + first moves | Decision dock expanded + 60-day plan |
| 5. Watch | KPI covenant with live baselines | Vital-signs gauges (8 KPIs) |

**L2 — Diagnostic Rooms (drill-downs):** Social Command Center · Catalog & Pricing · Website & Discoverability · Competitive · Audience & Personas · Content Engine.

**L3 — Evidence Room:** source registry (S01–S13), capture windows, n= disclosures, confidence grades, data-pass gaps.

## The Social Command Center (the "social commands like different dashboards" ask — 6 sub-panels)
1. **Owned-vs-Earned Engine** — the flagship. Bar: owned median 3 likes / 655 views vs earned peak 5,930 / 124,937; ratio badge ~190×. [S08]
2. **Platform Vitals** — IG (88,903 followers, 1,368 posts, ER 0.006%, n=17) · TikTok (7,608 followers, 584 videos, 13 followers/video, n=60). Each with capture window. [S08/S09/S10]
3. **Content Leaderboard** — sortable table of top IG + TikTok posts (permanent URLs, owned/earned badge, likes/views/date), from `CONTENT_INTELLIGENCE.md`. Filter by language → shows Arabic-wins pattern live.
4. **Language Performance Split** — Arabic vs English post performance; the free-uplift lever, quantified. [S08/S09]
5. **UGC Flywheel** — creator roster (12 handles, handle-only), founder-channel contribution (8/34), UGC-velocity KPI. [S08]
6. **Voice of Customer** — comment analysis: 254 comments, emoji-praise dominant, size/price intent landing on creators not brand (WhatsApp-gap proof). [S08] RTL verbatims preserved with gloss.

## Full tab list (360 coverage)
| Tab | Content | Source |
|---|---|---|
| Command (L0+L1) | Decision dock + 5-screen story | strategy.json, era_20 bundle |
| Social Command Center | 6 panels above | social_intel, instagram_owned_intel, CONTENT_INTELLIGENCE, VOICE_VALIDATION |
| Catalog & Pricing | 250 SKUs, price bands, 38% discount surface, hygiene score, untyped/dup-collection flags | catalog_full.json |
| Website & Discoverability | PageSpeed M55/D98, SEO 100, agent-readiness B72 (bot access 25, protocol 33), security CLEAN | website_audit.json, agent_readiness_audit.json |
| Competitive | Dejavu comparison + rival framework (10 GAP rows = data-pass) | SOV_BATTLE_MAP |
| Audience & Personas | 4 personas + market context (EGP 31.4bn, women 52%) | strategy.json, search_corpus |
| Content Engine | Pillars, feed-mix %, 90-day calendar, content ideas | CAMPAIGN_CALENDAR, strategy.json |
| Strategy | Positioning map, message house, objectives | strategy.json |
| Evidence (L3) | Source registry, confidence grades, gaps, data-pass menu | SOURCE_REGISTRY, gaps.yaml |

## Chart specs (per esm-landing CHART_LEARNING_PROTOCOL)
- Owned-vs-earned: grouped/log-scale bar (the ~190× needs log or a broken axis + callout).
- Price bands: histogram (4 bands).
- Positioning map: scatter with drift arrow (today → target), white-space quadrant shaded.
- Funnel: horizontal funnel with the Conversion stage flagged red (WhatsApp gap).
- KPI covenant: 8 gauge/bullet charts with baseline markers.
- PageSpeed: dual radial (mobile 55 red / desktop 98 green).
- Content leaderboard: sortable data table + thumbnail (permanent URL only, no CDN hotlink).
- Language split: paired bars (AR vs EN) per platform.

## D3 surface-mapping table (Executive-lens requirement — every parity surface → home)
| Parity surface | L1 screen / L2 room | Max clicks from L2 |
|---|---|---|
| Owned-vs-earned engine | L1-1 + Social Command Center | 0 |
| Language performance | L1-2 + Social Command Center #4 | 1 |
| Funnel + WhatsApp gap | L1-2 | 0 |
| Financial baselines | L1-3 (GapPlaceholder cards) | 0 |
| 3 decisions + first moves | L0 dock + L1-4 | 0 |
| KPI covenant (8) | L1-5 (Watch) | 0 |
| Website Health (PageSpeed) | L2 Website & Discoverability | 1 |
| Agent-Readiness / GEO | L2 Website & Discoverability | 1 |
| Catalog & pricing | L2 Catalog & Pricing | 1 |
| Competitive / SoV | L2 Competitive | 1 |
| Personas + market | L2 Audience | 1 |
| Content plan / calendar | L2 Content Engine | 1 |
| Evidence & Confidence | L3 Evidence Room | 2 |
| Data-pass gaps | L3 Evidence Room | 2 |
**Survival Ledger:** every module in this run (audit §, era_20, marketer files, instruments) maps to a home above — 0 removed = compile assertion.

## Buildability (compile contract)
- `dashboard/build_cielito_data.py` reads `_intel/*.json` + `instruments/*.json` + `strategy.json` → emits `cielito_360_data.json` for the React app.
- **Fails closed on:** banned vocab (imports `scripts/banned_vocab.py`), any `{label,value}` KPI without a source id, unguarded money number mirrored in copy, missing/oversized media (>24MB), CDN-hotlinked images.
- **GapPlaceholder doctrine:** revenue/AOV/conversion render as "To be baselined — requires client data" cards, never zeros or invented numbers. Blocked routes (FB stats, rival socials) render as "Not yet measured — [unlock via data pass]", never as "0" or "none".
- Self-reported KPIs (none plotted) and HYPOTHESIS grades (fruit-leather) get a data-layer caveat bar.

## Build trigger
This spec is the input to the **hero wave** (`Mega Run cielito-egypt wave hero`) which scaffolds `build_cielito_data.py` + the React components and deploys to `esm-landing /dashboard/cielito-360`. Registered, not yet built (Era 21 bootstrap trigger).
