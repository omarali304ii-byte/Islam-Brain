# Cielito 360 — Per-Tab Deepening Master Prompt (20 charts/tab · footwear-category · no fabrication)

> **Purpose.** Take the Cielito 360 dashboard from ~1–6 charts/tab to a target of **≥20 evidence-backed charts per tab**, doing the *proper analysis for a women's fashion & footwear D2C brand in Egypt* — with a **hard no-fabrication contract**. Every chart must be tagged with a real data source. Where the data does not exist yet, the chart is a **RequiresData card** (labelled, not invented) plus a costed route to obtain it.

## 0. THE CONTRACT (fail-closed — read first)
1. **No fabricated series, ever.** Each chart declares a `data_source` tag from the ledger below. If the source is not `HAVE`, the chart renders as a **"Requires data — [route]"** placeholder card, never as invented numbers.
2. **Every KPI/number carries its source + n= + capture window.** Social metrics disclose sample size; market numbers are banded; financials are "To be baselined".
3. **Client-safe vocabulary** (banned_vocab.py) + the WOM/agency-vs-earned disambiguation (creator = earned public posts, NOT agency-owned).
4. **Category doctrine (Egypt fashion/footwear):** masri-first content, WhatsApp = the conversion bridge, Ramadan/Eid/Sahel/winter-boots = the demand calendar, sizing/returns = the #1 friction, jewel-tone + crystal + heritage-luxe = the design equity, price is emotional (desire > discount).

## 1. DATA-SOURCE LEDGER (what "HAVE" means)
| Tag | Meaning | Examples already captured |
|---|---|---|
| **HAVE** | Real data on disk now | 250-SKU catalog (price, compare-at, type, tags, sizes, images, created dates); 210 posts; 1,050 scored comments; 63 creators; PageSpeed + agent-readiness; 22 reviewed product images; verbatims 4-pillar coding |
| **SCRAPE-FREE** | Buildable with a free pass | product-page bodies (materials/care copy), collection structure, more owned posts, IG highlights |
| **SCRAPE-PAID** | Needs an approved Apify route | rival catalogs+prices (Dejavu/Shoe Room/etc.), rival socials, Facebook stats, follower-quality audit, full comment history, TikTok Shop signals |
| **CLIENT** | Only the client has it | revenue, orders, AOV, conversion, returns %, CAC, repeat-rate, ad-account, GA4, IG/TikTok Insights (reach, geo, age) |
| **SURVEY** | Primary research (Era-28) | brand funnel/awareness, price elasticity (Van Westendorp), perceptual attributes |

**Rule:** a tab hits "20 charts" by combining HAVE charts (build now) + RequiresData cards (SCRAPE/CLIENT/SURVEY, shown honestly). A dashboard that shows 8 real + 12 labelled "requires data" cards is **more honest and more useful** than 20 fabricated charts.

## 2. PER-TAB DEEPENING PLANS

### SOCIAL COMMAND CENTER (target 20)
Category lens: owned-vs-earned engine, format economics, posting ROI.
HAVE: 1 owned-vs-earned log bar · 2 platform vitals · 3 language AR/EN split · 4 format×engagement · 5 posting cadence · 6 engagement timeline · 7 reach-vs-engagement scatter (all posts) · 8 hashtag frequency×avg-likes · 9 caption-length vs engagement · 10 emoji-vs-text caption performance · 11 owned vs earned volume share · 12 top-post decay curve.
REQUIRES: 13 reach/impressions funnel (CLIENT-Insights) · 14 follower growth curve (CLIENT) · 15 story completion (CLIENT) · 16 save/share rate (CLIENT) · 17 best-time-to-post heatmap (CLIENT day×hour) · 18 follower geo map (CLIENT) · 19 follower age/gender (CLIENT) · 20 paid-vs-organic split (CLIENT ad-account).

### POST EXPLORER (target 20)
HAVE: 1 sortable all-posts table · 2 reach-vs-likes scatter · 3 likes distribution histogram · 4 comments distribution · 5 by-type box (Reel/Sidecar/Image) · 6 owned-vs-earned facet · 7 monthly volume · 8 engagement-rate per post · 9 lang split per post · 10 hashtag-count vs reach · 11 top-10 / bottom-10 boards · 12 caption-theme tag per post.
REQUIRES: 13 watch-time/completion per reel (CLIENT) · 14 sound/audio used (SCRAPE-FREE) · 15 posting-gap vs next-post reach (HAVE-derivable — add) · 16 CTA-present vs engagement (HAVE from captions — add) · 17 product-tagged vs not (SCRAPE-FREE) · 18 first-comment timing · 19 shares per post (CLIENT) · 20 saves per post (CLIENT).

### CREATOR DIRECTORY (target 20)
Category lens: micro-creator ambassador economics.
HAVE: 1 creators by total likes · 2 by total reach · 3 posts-per-creator · 4 avg-engagement-per-creator · 5 founder-vs-others contribution · 6 follower-band mix (from handles where captured) · 7 new-vs-returning creators over time · 8 creator-content format mix · 9 language per creator · 10 tag-only vs styled content.
REQUIRES: 11 creator follower counts (SCRAPE-PAID per-handle) · 12 creator audience geo (SCRAPE-PAID) · 13 creator engagement-rate (SCRAPE-PAID) · 14 estimated media value (needs 11–13) · 15 category affinity (SCRAPE) · 16 overlap with rival brands (SCRAPE) · 17 CAC per creator (CLIENT) · 18 conversion per creator link (CLIENT) · 19 gifting-cost vs return (CLIENT) · 20 exclusivity/contract status (CLIENT).

### SENTIMENT + WORDS & VERBATIMS (target 20 across the two)
HAVE: 1 overall donut · 2 by-channel bars · 3 theme×polarity stacked · 4 words-exercise frequency (AR/EN) · 5 4-pillar counts (functional/emotional/frustration/need-gap) · 6 pillar verbatim cards · 7 brand-dipstick words · 8 benefit ladder · 9 3 motivations · 10 tag-a-friend rate · 11 tension→opportunity · 12 intent-signal count · 13 sentiment over time (HAVE-derivable from comment timestamps — add) · 14 emoji-sentiment split · 15 positive-word cloud vs negative-word cloud.
REQUIRES: 16 sentiment vs star-rating validation (needs Google/marketplace reviews — SCRAPE-PAID) · 17 rival sentiment benchmark (SCRAPE-PAID) · 18 complaint-resolution time (CLIENT) · 19 NPS (SURVEY) · 20 attribute importance×satisfaction 2×2 (SURVEY).

### PRICING & VALUE (target 20)
Category lens: footwear price ladders, discount discipline, size economics.
HAVE: 1 price architecture by category · 2 price tiers donut · 3 discount-depth distribution · 4 sub-family price ladder · 5 apparel-vs-footwear discount gap · 6 size availability · 7 avg-sizes-per-product · 8 price vs created-date (new-arrival trend) · 9 on-sale share by month · 10 compare-at vs price gap · 11 price-per-band × availability · 12 premium-tier composition · 13 price distribution histogram (fine bins) · 14 SKU count by price point.
REQUIRES: 15 price vs rivals per category (SCRAPE-PAID rival catalogs) · 16 price-index vs Dejavu/Shoe Room (SCRAPE-PAID) · 17 sell-through by price (CLIENT) · 18 margin by category (CLIENT) · 19 discount → sell-through elasticity (CLIENT) · 20 willingness-to-pay per hero SKU (SURVEY Van Westendorp).

### PRODUCT DESIGN (target 20)
Category lens: design-language mix, colour, motif, material story.
HAVE: 1 real product-image gallery · 2 design-language families · 3 palette chips · 4 category mix · 5 sub-family counts · 6 colour distribution (from titles/tags — add parse) · 7 material mentions (leather/velvet/crystal/cactus — from tags/body_html, SCRAPE-FREE) · 8 motif tags (leaf/knot/gem — from titles) · 9 heel-type mix (mule/sandal/boot/slipper) · 10 price × design-language · 11 new-arrival design trend · 12 botanical/fruit-leather line inventory (1000 Leaves, Cactus).
REQUIRES: 13 design-language × sell-through (CLIENT) · 14 colour × sell-through (CLIENT) · 15 returns by design/fit (CLIENT) · 16 rival design-language comparison (SCRAPE-PAID visual) · 17 trend-alignment score vs runway/Pinterest (SCRAPE) · 18 review-sentiment by design (needs reviews) · 19 repeat-purchase by design (CLIENT) · 20 which design language the audience actually tags most (HAVE-derivable — cross post images to products, add).

### CATALOG & PRICING / MARKET / COMPETITIVE / WEBSITE / PERSONAS / PLAN / STRATEGY / EVIDENCE
- **Catalog:** HAVE 8 (bands, families, availability, untyped share, created-date cohort, dup-collection flags, in-stock by category, tag cloud); REQUIRES sell-through, stock-turn, bestseller rank (CLIENT).
- **Market:** HAVE 4 (women-share, offline-share, banded size, category CAGR); REQUIRES real TAM/SAM/SOM bottom-up (needs sales), search-trend (SCRAPE-FREE Google Trends), marketplace share (SCRAPE-PAID).
- **Competitive:** HAVE 3 (Dejavu IG, positioning map, rival table); the **other 17 are the single biggest unlock → approve the competitive data-pass (SCRAPE-PAID P1)**: rival followers, post cadence, price ladders, discount cadence, SoV, sentiment, hero categories, WhatsApp usage, ad-library activity, growth curves.
- **Website:** HAVE 6 (mobile/desktop/SEO/agent-readiness gauges, agent bars, gap list); REQUIRES real Lighthouse LCP/CLS/TTI series (SCRAPE-FREE re-run), Core-Web-Vitals field data (CLIENT/CrUX), funnel drop-off (CLIENT GA4), search console (CLIENT).
- **Personas:** HAVE 4 persona cards + evidence; REQUIRES segment sizing + attribute maps (SURVEY).
- **Plan / Strategy:** feed-mix, calendar, pillars, positioning, message-house (HAVE, qualitative — keep as frameworks, not fake charts).
- **Evidence:** source table + gap register + confidence distribution (HAVE) + a "data-pass menu" cost table.

## 3. EXECUTION ORDER (highest leverage first)
1. **Add the HAVE-derivable charts** flagged "add" above (CTA-present, sentiment-over-time, colour/material parse, post↔product cross-map, posting-gap) — free, real, immediate.
2. **Approve the competitive data-pass (P1, ~$1.5–2.5)** — unlocks ~17 charts across Competitive + Pricing + Market + Sentiment-benchmark.
3. **Request the client data pack** (Shopify export + GA4 + IG/TikTok Insights) — unlocks every CLIENT chart (reach, geo, funnel, sell-through, returns, CAC) and turns "to be baselined" into real ROI.
4. **Field the Era-28 survey** (brand funnel + price elasticity) — unlocks the SURVEY charts.

## 4. CHART-QUALITY RULES (per the dataviz doctrine)
- One business question per chart; insight-led title; So-What line.
- Log scale where ranges span orders of magnitude (owned-vs-earned).
- Colour by meaning (owned=grey, earned/creator=terracotta, positive=green, negative=red, category-consistent).
- RequiresData cards use the dashed-orange placeholder style already in the build.
- Every chart cites its `data_source` tag in the card footer.

**This prompt is the build contract. A tab is "done" when it shows ≥20 cards, each either a real chart (source-tagged) or an honest RequiresData card with its route — and zero fabricated series.**
