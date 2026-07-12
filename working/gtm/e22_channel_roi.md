# [GTM] Era 22 — Channel-ROI Simulator — Cielito Egypt (base 360, 2026-07-09)
ANNOUNCE: Builds the per-channel ROI simulation STRUCTURE (formula chains, Egypt-specific variables, scenario matrix) for Cielito's paid + earned mix — every monetary input is ILLUSTRATIVE and gated on client ad-account data.

## Agents Run
- GTM Channel Strategist (owner)
- Channel Economics Modeler
- Egypt D2C Cost-Band Curator
- Scenario Sensitivity Analyst

## Findings

### 1. What the evidence licenses us to model (and what it does not)
The simulator is a STRUCTURE deliverable. We have HELD unit-economics anchors (AOV proxy, catalog bands, conversion-friction instruments) but ZERO spend-side truth: no ad-account access, no Meta Ads Library capture (blocked route — inaccessible, not absent [S-registry blocked list]), no revenue data (GAP). Therefore all CPM/CPC/CVR cells below are **ESTIMATE_ONLY — industry-typical band, requires client ad-account data** and are flagged ILLUSTRATIVE. The channel PRIORS, however, are evidence-ranked from owned captures.

**HELD demand-side anchors feeding the model:**
| Variable | Value | Source/Grade |
|---|---|---|
| AOV proxy (catalog median price) | EGP 1,200 (mean 1,324; band 400–7,600) | [S04] HELD — proxy only; true AOV requires client order data (GAP) |
| Price-band mass | 88 SKUs <1,000 · 156 SKUs 1,000–2,500 (of 250) | [S04] HELD |
| Discount posture | 96/250 on sale (38%) | [S04] HELD — implies margin pressure; contribution margin = GAP |
| Mobile CVR friction | PageSpeed mobile 55 vs desktop 98 | [S06] HELD — direction: mobile paid traffic converts below potential until fixed |
| Owned IG reach floor | median 3 likes / ER 0.006% / 655 median video views (n=17 owned, 2026-05-31→07-04) | [S08] HELD |
| Earned/UGC ceiling | 5,930 likes / 124,937 views on tagged posts (n=60 mixed, 2026-05-21→07-08) — ~200x owned median | [S08] HELD |
| TikTok organic | median 1,220 plays, median 0 comments (n=60, 2026-04-13→07-01); Arabic clips outperform (باشا مصر 14.8K plays) | [S09] HELD |
| Conversion bridge | 0 WhatsApp CTAs in captions (n=17); no WhatsApp link on site/bio (captured surfaces) | [S08][S10] HELD |
| COD reality | check-on-delivery + return-with-courier policy | [S03] HELD — forces a **COD refusal rate** variable in every channel chain |

### 2. Simulator formula chain (identical spine per channel)
```
Spend → Impressions (Spend/CPM×1000) → Clicks (×CTR) → Sessions (×land-rate)
→ Orders (×CVR_mobile-adjusted) → Delivered orders (× (1 − COD_refusal))
→ Net revenue (×AOV) → Contribution (×margin) → ROAS / CAC / payback
```
Egypt-specific variables no generic template has: **COD_refusal** (client data required; policy actively invites doorstep rejection [S03] HELD), **masri-vs-English creative multiplier** (Arabic content outperforms in both owned captures [S08][S09] HELD — modeled as a creative-language lever, not a number), **Ramadan/Eid seasonality index** (77-product Ramadan collection + Eid tags prove peak concentration [S05] HELD).

### 3. Channel worksheets (all cost cells ILLUSTRATIVE / ESTIMATE_ONLY)
| Channel | Illustrative cost band (ESTIMATE_ONLY, industry-typical, requires client ad-account data) | Evidence-based prior for Cielito | Grade of prior |
|---|---|---|---|
| Meta (IG+FB) paid | CPM $0.5–2.5 · CPC $0.05–0.30 (Egypt fashion typical band) | Necessary spine: 88.9K IG followers [S10] but organic reach dead (ER 0.006% [S08]) — paid is the only IG reach path today | HELD (prior) / ESTIMATE_ONLY (costs) |
| Influencer/UGC seeding | per-post fee band unknown (GAP); gifting cost ≈ COGS | STRONGEST prior: earned posts reach ~200x owned median; a creator (88.9K-audience capture: 5,930 likes/124.9K views) already outperforms the brand [S08] HELD; founder account posts brand content free [S11] LIKELY | HELD |
| TikTok (organic + Spark Ads) | CPM $0.3–1.5 ILLUSTRATIVE | 584 videos → 7,608 followers = weak organic yield [S09] HELD, but Arabic/masri clips spike; Spark-boosting proven Arabic winners is the testable play | HELD (prior) |
| WhatsApp (conversion/retention bridge) | session/msg costs per Meta rate card — requires setup | Currently ZERO presence [S08][S10] HELD → modeled as a CVR multiplier on all other channels, not a standalone spend line; in Egypt WhatsApp is THE conversion bridge (context law) | HELD (absence) |
| Google Search/Shopping | CPC $0.05–0.40 ILLUSTRATIVE | SEO 100 + clean structured data [S06][S07] HELD = low technical barrier; brand-demand volume = GAP | ESTIMATE_ONLY |
| Email/SMS (owned) | near-zero marginal cost | Site has account login [S03] HELD; list size = GAP | GAP-gated |

### 4. Scenario matrix + sensitivity (structure)
Three scenarios per channel — Conservative / Base / Stretch — each varying ONLY: CPM band edge, CVR (with/without mobile-speed fix [S06]), COD_refusal (low/mid/high placeholder), AOV (median 1,200 vs mean 1,324 [S04]). Sensitivity ranking to pre-wire in the workbook: (1) COD_refusal, (2) mobile CVR (PageSpeed 55 fix), (3) creative language mix (masri share), (4) AOV mix-shift toward 1,000–2,500 band. **No ROAS number is quotable until client fills the 6 red inputs: ad spend history, true AOV, contribution margin, COD refusal %, list sizes, Meta pixel status (GAP).**

## Harness Enrichment — paid-ads
Egypt-fashion channel plan skeleton enriched with this run's evidence: (a) always model COD_refusal as a post-click leak — Cielito's own policy invites doorstep rejection [S03] HELD, so ROAS computed on placed orders will overstate; (b) when owned ER < 0.05%, treat paid social as reach REPLACEMENT not amplification — set organic-assist to zero in attribution assumptions [S08] HELD; (c) creative-language lever: brief masri-first variants before budget scaling — both platforms' Arabic posts outperform English (باشا مصر 14.8K TikTok plays vs 1,220 median [S09] HELD).

## Harness Enrichment — campaign-plan
Campaign calendar must be anchored to catalog-proven peaks, not generic retail dates: Ramadan collection = 77 SKUs, Ramadan Sale 2026 = 78 SKUs, Eid 30%-OFF tags present [S05] HELD — so the annual plan front-loads ~60–90 days pre-Ramadan testing to enter the peak with winning creative. Summer drop is the secondary proven peak (Summer 2024/2025 tags + "Sahel look" TikTok content [S04][S09] HELD). Buy-1-Get-1-on-Kimonos tag [S05] HELD = existing offer mechanic to reuse in paid hooks (currently absent from IG captions — 0 offer language, n=17 [S08] HELD).

## Harness Enrichment — data:analyze
Analysis contract for when client data lands: rebuild AOV from orders (catalog median is a proxy that ignores basket size and discount realization — 38% of SKUs on sale [S04] HELD); segment CVR mobile vs desktop before/after PageSpeed fix (55→target ≥80, [S06] HELD baseline); compute COD refusal by channel and by price band (hypothesis to test: refusal rises above EGP 2,500 band — HYPOTHESIS, requires order data).

## Era Snapshot
- Simulator spine built: 6 channels × formula chain with 3 Egypt-specific variables (COD_refusal, masri multiplier, Ramadan index) — structure HELD, all cost cells ESTIMATE_ONLY.
- Strongest evidence-backed channel prior = influencer/UGC seeding: earned posts reach ~200x owned median (5,930 vs 3 likes; n=60 mixed vs n=17 owned, windows disclosed) [S08] HELD.
- Owned IG paid spend is mandatory for reach (ER 0.006%, n=17) but must route through a WhatsApp bridge that does not exist yet [S08][S10] HELD.
- Mobile PageSpeed 55 [S06] HELD is a pre-spend gate: fixing it multiplies every paid channel's CVR cell.
- No quotable ROAS exists: spend, margin, AOV, COD refusal, pixel status all GAP — 6 red client inputs listed in the workbook.
