# ATLAS Era 4 — Financial — Cielito Egypt (base 360, 2026-07-09)

ANNOUNCE: Reconstructs Cielito's financial architecture from public evidence only — price bands, discount posture, COD/fulfillment cost mechanics, working-capital signals — and builds a parameterized break-even skeleton whose money inputs are all flagged as client-data requirements. NO revenue, order, AOV, CAC, or COGS data exists in any captured source (GAP — client-side).

## Agents Run
- **A19 — Price-Architecture Analyst** (bands, dispersion, positioning tier)
- **A20 — Discount & Margin-Pressure Auditor** (sale share, depth, promo hygiene)
- **A21 — Fulfillment-Cost Economist** (COD, Bosta vs in-house, reverse logistics)
- **A22 — Unit-Economics Modeler** (break-even skeleton, client data-request list)

## Findings

**1. Price architecture — mass-affordable core with a vestigial premium tail.** 250 SKUs, EGP 400–7,600, median 1,200, mean 1,324 [S04, HELD]. Band structure:

| Band (EGP) | SKUs | Share | Read |
|---|---|---|---|
| <1,000 | 88 | 35.2% | entry/basics (tops from 400, kimonos 600–900) |
| 1,000–2,500 | 156 | 62.4% | the core: leather footwear, sets, abayas |
| 2,500–5,000 | 4 | 1.6% | silk-velvet 3-piece sets (3,400→2,720) |
| >5,000 | 2 | 0.8% | "1000 Leaves" jacket 8,500→6,800 / vest 9,500→7,600 [S01/S02, HELD] |

97.6% of the catalog sits under EGP 2,500 — consistent with the bio claim "Affordable luxury" [S10, SELF_REPORTED] and with purchasing-power erosion as the market's principal demand risk [S11, LIKELY]. Median list price 1,200 is a *list-price* proxy only; actual AOV = GAP (requires client order data; multi-item try-on orders invited by the shipping policy [S03] could push AOV above single-SKU median or crater it via rejections).

**2. Discount posture — 38.4% of the catalog is on sale; evidenced depths run 20–50%.** 96/250 SKUs discounted [S04, HELD]. Depths verified from captures: 20% (1000 Leaves pieces, silk-velvet sets [S01/S02]), 29% (Morroccan Jalabeyas 1,200→960 [S05]), 36% (maxi kimonos 1,400→900 [S05]), 50% (Casual Blazer 1,200→600 [S05]). Promo tags embed a permanent-promotion culture: "50% OFF", "Buy 1 Get 1 on Kimonos", "Celebrate Eid with 30% OFF", "Black Friday", "Ramadan Sale" [S05, HELD]. A structurally discounted catalog at this share is a margin-pressure signal (grade: HELD as signal; actual margin impact = GAP, requires COGS). The strategic irony (flagged for Era 5/creative): 38% of the store is on sale yet **0 of 17 owned IG captions contain any offer language** [S08, HELD, n=17, window 2026-05-31→07-04] — the discounts are financed but not marketed.

**3. Pricing hygiene defect — inverted compare-at anchors.** Three corsets (Indian Nights, Siwa, Fleurie) show price 1,200 vs compare_at 900 [S05, HELD] — the "was" price is *below* the selling price. Either stale data after a price increase or entry error; both suppress the sale badge and, if surfaced, read as a fake-anchor consumer-trust problem. Cheap fix, real risk.

**4. COD / check-on-delivery cost mechanics.** Policy [S03, HELD]: customers may open and inspect at the door while the courier waits; rejection costs the customer only the shipping fee; multi-item "choose between" orders are explicitly invited and routed to in-house couriers because Bosta does not allow partial delivery. Financial implications (qualitative, HELD as mechanics / GAP as magnitudes): (a) rejection risk is a designed-in CX feature, so failed/partial-delivery rate is structurally elevated versus prepaid e-commerce; (b) Cielito carries reverse-logistics coordination, re-stocking, and cash-collection float on every COD order; (c) the dual fleet (Bosta + in-house couriers, Cairo/Alex 2 days, Cairo express 24h) buys flexibility at the cost of in-house fixed courier capacity whose utilization is unknown (GAP). Refunds 7-day / exchanges 14-day with delivery charges applying [S03, HELD] partially offloads return freight to the customer.

**5. Working-capital & inventory signals.** 218/250 in stock (87.2%); 32 unavailable SKUs still listed [S04, HELD]. Catalog spans 2022-11-13 → 2026-06-15 [S04, HELD] — multi-year-old SKUs remain live, consistent with aging-inventory drag (ESTIMATE_ONLY as inference; sell-through = GAP). The Ramadan-dominated collection structure (All Ramadan Products 77, Ramadan Sale 2026 78, Ramadan 2026 Collection 39 [S05, HELD]) implies a cash cycle that concentrates inventory build pre-Ramadan and discount-led liquidation after — a seasonal working-capital peak the brand must finance annually (mechanism HELD from catalog structure; magnitudes GAP).

**6. Revenue and everything downstream of it — GAP.** No revenue, orders, conversion rate, CAC, ROAS, payment mix, or refund-rate data exists in any captured source. Facebook page stats, marketplace presence (Noon/Amazon EG/Jumia), and paid-ads library status are **inaccessible, not absent** (blocked routes per source registry). All money-forward statements above are ESTIMATE_ONLY or GAP and require client data.

## Harness Enrichment — mr-validator
Validation pass over this era's quantitative claims:
- Band arithmetic: 88+156+4+2 = 250 ✓ matches total_products [S04]. Sale share 96/250 = 38.4% ✓.
- Price stats internally consistent (min 400 ≤ median 1,200 ≤ mean 1,324 ≤ max 7,600; right-skew explained by the two >5K outliers) ✓.
- Anomaly flagged: 3× compare_at < price (inverted anchor) — routed to findings §3; recommend watch-register entry until client confirms intent.
- Market-size conflict enforced as band: EGP 31.4bn retail 2025 (+9% YoY) vs ~$635M USD-terms source — units/scope conflict; NEVER quote a single settled number [S11, ESTIMATE_ONLY].
- Disclosure check: every social metric cited in this era carries n= and window ✓ (n=17 owned, 2026-05-31→07-04).
- List-price ≠ transaction-price caveat applied to all AOV-adjacent statements ✓.

## Harness Enrichment — break-even-economics
Parameterized per-order break-even skeleton (structure HELD; every input value = GAP, requires client data):

`Contribution/order = AOV − COGS − last-mile fee − packaging − COD cash-handling fee − (failed-delivery rate × failed-trip cost) − allocated CAC`

Break-even orders/month = Fixed monthly costs (in-house couriers, studio/content, team, Shopify + apps) ÷ contribution/order.

| Input | Status | Where to get it |
|---|---|---|
| AOV, orders/mo, conversion | GAP | Shopify admin export |
| COGS per category (leather vs clothes) | GAP | client costing sheet; note imported materials (Italy/Spain/Germany/India/UK [S02, SELF_REPORTED]) = FX-exposed COGS |
| Bosta rate card + COD fee | GAP | Bosta contract |
| Failed/partial-delivery rate | GAP | courier logs (structurally elevated by check-at-door policy [S03]) |
| Return/exchange rate | GAP | Shopify + Judge.me records |
| CAC / ad spend | GAP | Meta Ads (pixel + CAPI installed — see Era 6) |
| In-house courier fixed cost & utilization | GAP | payroll/ops |
Only the price distribution feeding AOV scenarios is HELD [S04]. No illustrative numbers are asserted — the model runs the day the client shares the seven inputs above.

## Era Snapshot
- 97.6% of the 250-SKU catalog is priced under EGP 2,500 (median 1,200) — mass-affordable positioning with only a 6-SKU premium tail [S04/S01 — HELD].
- 38.4% of the catalog is on sale at evidenced depths of 20–50%, with a permanent-promo tag culture (Ramadan/Eid/BF/BOGO) = structural margin-pressure signal; yet owned IG carries zero offer language (n=17) [S04/S05/S08 — HELD].
- Check-on-delivery + multi-item try-on policy makes elevated rejection rates a designed cost of doing business; dual Bosta/in-house fleet adds unquantified fixed cost [S03 — HELD mechanics, GAP magnitudes].
- Pricing hygiene defect: 3 SKUs with compare-at below selling price (inverted anchors) [S05 — HELD].
- All revenue/margin/CAC economics = GAP, requires client data; blocked external routes (FB stats, marketplaces, ads library) are inaccessible, not absent [registry — GAP].
