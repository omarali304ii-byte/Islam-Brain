# [ATLAS] Era 10 — Supply Chain — Cielito Egypt (base 360, 2026-07-09)

ANNOUNCE: Maps Cielito's make-and-move chain — materials sourcing, local manufacture claims, last-mile logistics, and import-cost exposure — from captured site copy, policy pages, and catalog structure.

## Agents Run
- A43 — Sourcing & Materials Mapper
- A44 — Logistics & Last-Mile Analyst
- A45 — Cost-Exposure & Inventory Signal Reader

## Findings

### 1. The chain as the brand tells it: Egyptian hands, imported inputs
The About page states the product is "Crafted by Egyptian hands with internationally sourced materials and accessories — from Italy, Spain, Germany, India, UK, and more" with "international-standard heels made in Egypt" and nappa lining on genuine-leather lines [S02 SELF_REPORTED — brand's own copy; HELD that the page says it]. A parallel vegan-leather line is claimed on the same page [S02 SELF_REPORTED]. This is a **hybrid chain**: local assembly/manufacture + imported raw materials — the classic Egyptian premium-footwear configuration. Whether manufacture is owned-factory or contract workshops is **GAP** (no evidence either way).

The launch-era press differentiator — fruit leather (aloe vera, prickly pear, pineapple), positioned as first in Egypt [S11 LIKELY at launch, press-only] — has **zero trace** on cielitoeg.com or mycielito.com today (grep: 0 hits) [S11 + S01/S12 HELD for captured surfaces]. If that supply line existed, it has been dropped or gone silent → HYPOTHESIS: fruit-leather sourcing discontinued. This is simultaneously a supply-chain fact-gap and a positioning loss (handed to Era 11/12).

### 2. Last mile: dual-courier model tuned to Egyptian COD culture
Shipping policy [S03 HELD as published policy]:
| Element | Detail | Read |
|---|---|---|
| Carriers | Bosta + in-house couriers | Dual model = flexibility hedge |
| Cairo/Alex SLA | 2 days | Competitive for local D2C |
| Express | 24h in Cairo | Premium service tier exists |
| Check-on-delivery | Customer inspects while courier waits; refuse = pay shipping only | Deep COD-culture accommodation |
| Multi-item try-on | Routed to in-house couriers because "Bosta does not allow partial delivery" | In-house fleet exists specifically to absorb try-and-return behavior |

The in-house courier line is the notable operational asset: it converts Egypt's try-before-you-pay expectation from a returns cost into a service feature. It also implies real fixed logistics cost (riders/vehicles) carried by the brand — scale of that fleet = **GAP**. No physical stores evidenced on any captured surface [S01/S11 HELD for captured surfaces — inaccessible ≠ absent for offline presence]; contrast rival Dejavu which runs online + physical stores at 289K IG scale [S11 LIKELY].

### 3. Import-cost exposure and the pricing evidence
Materials invoiced in EUR/GBP/USD against EGP retail prices (EGP 400–7,600, median 1,200 across 250 SKUs [S04 HELD]) creates direct FX margin exposure in a purchasing-power-erosion market [S11 LIKELY for the macro context; exposure mechanism = ESTIMATE_ONLY inference]. Signals consistent with margin/inventory pressure (each individually weak, together suggestive — graded honestly):
- **96/250 SKUs on sale (38%)**, typically at −20% [S04 HELD]. Could be promo strategy or stock-clearing; cause = GAP.
- **Catalog spans 2022-11 → 2026-06** [S04 HELD] — nearly 4-year-old SKUs still listed; 218/250 in stock (32 unavailable-but-live) suggests long-tail inventory kept alive rather than pruned.
- **Inverted anchors on some SKUs** (e.g., corsets priced EGP 1,200 with compare_at 900 [S05 HELD]) — a data-hygiene error that would display a negative "sale", hinting price rises outpacing catalog maintenance (consistent with FX pass-through, ESTIMATE_ONLY).
- **Catalog ops discipline is weak**: 128/250 products untyped, three duplicate best-seller collections (Best Sellers / Best Selling / BestSelling), mules collection duplicated [S04/S05 HELD]. Weak PIM discipline usually correlates with weak inventory/supply planning upstream — flagged as HYPOTHESIS, not claimed.

### 4. What we cannot see (data-pass routes, not absences)
Production capacity, supplier identities, MOQs, lead times, landed-cost structure, returns rate, Bosta vs in-house volume split, warehouse location, and the mycielito.com relationship (second live Shopify storefront [S12 HELD it exists]) are all **GAP / inaccessible** — client-side interview or data-pass routes, never claims of absence.

## Harness Enrichment — competitive-intel
Supply-chain positioning map vs discovered rival set [S11 LIKELY]: Dejavu = scale + physical retail (mass); Elia/Bulga/Ramla = artisan-handcraft heritage narratives (Makramya/Taly, sarma silk tassels); Jayda Hany = designer-led premium; Parfois = imported mass-fashion. Cielito's "Egyptian hands + European materials" sits in the contested middle: more premium story than Dejavu, less distinct craft narrative than Elia/Ramla — and its one chain-level differentiator (fruit leather) is currently unclaimed by anyone visible in the rival set. Enrichment: add "materials provenance" as a standing competitive-intel comparison axis for the competitive wave; capture rivals' about/materials pages when that wave runs.

## Harness Enrichment — data-collection-agent
Concrete collection routes this era exposes for the data-pass menu: (1) client-side ops interview — factory model, fleet size, returns %, Bosta split; (2) Bosta public tracking/coverage pages (free) for SLA verification outside Cairo/Alex; (3) mycielito.com full catalog diff vs cielitoeg.com (free, resolves ownership question S12); (4) Facebook page transparency/ads library for offline-event or store signals (currently blocked route). Each route costed at the pipeline level; none executed here (era is analysis-only).

## Era Snapshot
- Hybrid chain: made-in-Egypt assembly + Italy/Spain/Germany/India/UK materials — brand's own claim, unverified externally [S02 SELF_REPORTED].
- Dual last-mile (Bosta + in-house couriers) purpose-built for Egyptian check-on-delivery culture; 2-day Cairo/Alex, 24h express [S03 HELD].
- FX exposure on imported materials against EGP retail is structural; 38% of catalog on sale and inverted price anchors are consistent-with (not proof-of) margin pressure [S04/S05 HELD facts; ESTIMATE_ONLY inference].
- Launch differentiator (fruit leather) has vanished from all owned surfaces — supply line status unknown [S11 LIKELY at launch; HYPOTHESIS dropped].
- Factory model, costs, returns rate, mycielito.com relationship = GAP (inaccessible, routed to data pass) [S12].
