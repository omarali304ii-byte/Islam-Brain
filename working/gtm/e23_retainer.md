# [GTM] Era 23 — Retainer Pipeline — Cielito Egypt (base 360, 2026-07-09)
ANNOUNCE: Neutral-run design of Cielito's RETENTION engine — repeat-purchase levers extracted from captured evidence, a post-purchase journey blueprint, and a retention KPI set whose baselines all await client data.

## Agents Run
- Retention Engine Designer
- Post-Purchase Journey Architect
- Insight Generator (skill-bridged)
- Retention Dashboard Spec Writer

## Findings

### 1. Why retention is the under-priced lever here
Cielito's acquisition surfaces are weak today (owned IG ER 0.006%, median 3 likes, n=17 owned, window 2026-05-31→07-04 [S08] HELD; TikTok 7,608 followers from 584 videos [S09] HELD), which makes every already-acquired customer disproportionately valuable. Three structural assets in the captures are natively retention-shaped, and none is currently operated as a retention system:

**Lever A — Exchange-friendly trust policy (HELD [S03]).** Check-on-delivery ("check the items while the courier waits"), 7-day refund, 14-day exchange, express 24h Cairo shipping via Bosta + in-house couriers, and even multi-item try-on orders via in-house courier ("adding multiple items to the order to choose between"). This is a genuinely differentiated doorstep try-on experience in Egyptian COD culture — but it is buried on a policy page. It appears in 0 of 17 owned IG captions [S08] HELD. As a retention lever: customers who exchange successfully are prime repeat buyers; today no journey captures them post-exchange (process = GAP, requires client input).

**Lever B — Seasonal drop cadence (HELD [S04][S05]).** The catalog proves a repeatable seasonal rhythm: Ramadan collection 77 SKUs + Ramadan Sale 2026 78 SKUs + Ramadan Kimono 22; Summer 2024/2025 lines; Black Friday tags; Eid 30%-OFF tag; Buy-1-Get-1 on Kimonos; catalog spans 2022-11→2026-06 with fresh drops as recent as 2026-06-15. Seasonal drops are a natural reactivation calendar — each drop is a legitimate reason to re-contact past buyers. Today there is no evidence any past-buyer re-contact channel exists (no WhatsApp presence on captured surfaces [S08][S10] HELD; email/SMS list status = GAP).

**Lever C — Cross-category ladder (HELD [S04]).** 250 SKUs across footwear (slippers 31, sandals 11, cowboy boots 8, espadrilles 7, ballerinas/loafers/mules), bags (12+ shoulder bags, Bags collection 13), and clothes (kimonos 33+, sets, dresses, abayas/kaftans) with price bands EGP 400–7,600 (median 1,200; 88 SKUs under 1,000). A footwear buyer has an under-1,000 accessory entry point and a kimono/set upsell path — cross-sell mapping is buildable from order data (basket pairs = GAP, requires client orders).

**Lever D — Size/fit confidence content (HELD [S03][S09], partially).** Footwear D2C's #1 return driver is fit. Cielito already has the operational answer (doorstep try-on) and even organic content instinct — the TikTok "بقي عندك fitting room في بيتك" ("you now have a fitting room at home") clip, 2,471 plays vs 1,220 median (n=60, window 2026-04-13→07-01) [S09] HELD. Fit-content as a pre-purchase objection-killer and post-purchase exchange-reducer is evidenced but unsystematized.

### 2. Post-purchase journey blueprint (design deliverable; channel = WhatsApp once built, else SMS/email)
| Stage | Trigger | Message job | Evidence hook |
|---|---|---|---|
| D0 | Order placed | Confirm + set doorstep try-on expectation ("check it while the courier waits") | [S03] HELD policy, currently unmarketed |
| Delivery day | Courier dispatched | Fit-check prep (size guide, styling) — reduces refusal | Lever D; COD refusal baseline = GAP |
| D+2 | Delivered | Thank-you + fit confirmation ask; open exchange path early (14-day window [S03]) | Exchange = retention moment, not cost |
| D+7 | Refund window closes | UGC/review ask — earned content outperforms owned ~200x (5,930 vs 3 median likes [S08] HELD) so customer content is the cheapest acquisition asset | [S08] HELD |
| D+30 | Post-purchase | Cross-category offer from basket-pair logic (footwear→bag under EGP 1,000 entry [S04]) | Lever C |
| Seasonal | Pre-Ramadan / summer drop | Reactivation: early access to drop (77-SKU Ramadan engine [S05]) | Lever B |

Journey language rule: masri-first — Arabic content outperforms English across both platforms ([S08] caption set 16/17 English-only with floor engagement; [S09] Arabic clips outperform) — and 0 WhatsApp CTAs exist today (n=17 [S08] HELD), so the entire journey is net-new infrastructure.

### 3. Retention KPI set (ALL baselines: requires client data)
| KPI | Definition | Baseline status |
|---|---|---|
| Repeat purchase rate (90/180/365d) | % of buyers with 2nd order in window | GAP — Shopify order export needed |
| Time-to-second-purchase | median days order1→order2 | GAP |
| COD refusal rate | doorstep rejections / dispatched | GAP — courier + Bosta logs |
| Exchange rate vs refund rate | exchanges (retained revenue) vs refunds (lost) | GAP — policy exists [S03], data absent |
| Post-exchange repurchase rate | % of exchangers who buy again | GAP |
| Cross-category adoption | % of repeat buyers crossing footwear↔clothes↔bags | GAP |
| Seasonal reactivation rate | % of prior-Ramadan buyers purchasing next Ramadan | GAP — 2 Ramadan cycles exist in catalog [S04] |
| List coverage | % of buyers reachable on WhatsApp/SMS/email opt-in | GAP — currently ~0 evidenced WhatsApp [S08][S10] |

## Harness Enrichment — insight-generator
New reusable insight pattern from this run: **"policy-as-content gap"** — when a D2C brand has a genuinely differentiated service policy (doorstep try-on, multi-item try-on via in-house courier [S03] HELD) that appears in zero owned social captions (0/17 [S08] HELD), the retention brief writes itself: the cheapest content pillar is marketing the policy you already operate. Second pattern: **"exchange = retention moment"** — in COD markets, an exchange interaction is a second doorstep touchpoint; treat it as a journey stage, not a cost line.

## Harness Enrichment — data:build-dashboard
Retention dashboard spec (Power BI, buildable the day client order data lands): Tab 1 Cohort repeat-rate matrix (order-month × months-since-first); Tab 2 COD funnel (dispatched → delivered → refused → exchanged → refunded) — this funnel shape is Egypt-specific and absent from stock e-com templates; Tab 3 Cross-category Sankey (first-category → second-category); Tab 4 Seasonal reactivation (Ramadan/Summer cohort return rates, seeded from the catalog's proven drop calendar [S05] HELD); Tab 5 List coverage & journey delivery (WhatsApp/SMS opt-in %, message→session→order). Every visual carries a "requires client data" placeholder state — no fabricated baselines, per Dashboard-Creation-OS evidence gate.

## Era Snapshot
- Cielito already operates Egypt-grade retention infrastructure (doorstep try-on, 14-day exchange, in-house courier flexibility) but markets it nowhere — 0/17 owned captions mention it [S03][S08] HELD.
- The catalog is a ready-made reactivation calendar: 77-SKU Ramadan engine + summer drops + BOGO mechanics [S04][S05] HELD.
- No re-contact channel to past buyers is evidenced on any captured surface (no WhatsApp, list status unknown) [S08][S10] HELD (absence on captured surfaces) / GAP (email/SMS).
- Post-purchase journey blueprint delivered (6 stages, masri-first, WhatsApp-anchored) — design HELD to evidence, execution net-new.
- All 8 retention KPI baselines = GAP, requires client Shopify order export + courier logs; dashboard spec is pre-wired to receive them.
