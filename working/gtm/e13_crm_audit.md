# GTM Era 13 — CRM Adoption Audit — Cielito Egypt (base 360, 2026-07-09)
ANNOUNCE: Frames the CRM maturity audit for Cielito — the internal state is client-side data we do not hold, so this era ships the audit FRAMEWORK + the 10 WOM discovery questions, with every internal cell marked "requires client data".

## Agents Run
- **GTM CRM Auditor** (era owner, per GTM matrix row)
- Skills invoked: `revops`, `data:analyze`

## Findings

### 1. Headline: Cielito's CRM state = GAP
Cielito's actual CRM stack, customer database size, repeat-purchase rate, email/SMS lists, and any loyalty program are **client-internal and uncaptured** [S13 context; GAP]. Per binding rule 1: this is *inaccessible, not absent*. Everything in this era is either (a) externally observable CRM *surface* evidence, or (b) framework awaiting client data.

### 2. What the external evidence already tells us (the auditable perimeter)

| Observation | Evidence | Grade | CRM implication |
|---|---|---|---|
| Store runs Shopify (open `products.json`, 250 SKUs) | [S04] | HELD | A customer table with orders, phones, emails **exists by default** in Shopify admin. The raw material for CRM is already there even if unused. |
| Fulfilment = Bosta + in-house couriers, Cairo/Alex 2 days, check-on-delivery | [S03] | HELD | COD culture means **every completed order carries a courier-verified phone number** — the single most valuable CRM key in Egypt (WhatsApp-addressable). |
| 0 of 17 owned IG captions contain a WhatsApp CTA (n=17, window 2026-05-31→2026-07-04) | [S08] | HELD | No visible WhatsApp funnel on the top acquisition surface. |
| IG bio external link = website only; no WhatsApp link, 17 highlights (88,903 followers, 1,368 posts, verified) | [S10] | HELD (for captured surfaces) | No WhatsApp entry point on the profile either. HYPOTHESIS: no systematic WhatsApp-commerce layer exists. |
| 0 of 17 owned captions contain offer language | [S08] | HELD | Promotions (38% of catalog on sale [S04]) are not being pushed through owned social — suggests offers are site-only, i.e., no CRM-triggered promo cycle. HYPOTHESIS. |
| Catalog tags show a mature promo calendar: Ramadan (77–78 product collections), Black Friday, Eid 30% OFF, B1G1 kimonos | [S04][S05] | HELD | The brand *runs* campaigns — the question is whether any are audience-targeted (CRM) vs. blanket site banners. Requires client data. |
| Email popup / signup incentive on site | — | GAP | Text captures [S01–S03] did not capture dynamic popups; cannot claim presence or absence. |
| IG DMs / comments as an order channel | — | HYPOTHESIS | Common in Egyptian D2C; latest-comments exist in raw capture [S08] but order-taking via DM was not verified. Requires client data. |

### 3. Audit framework — 6 pillars × maturity ladder (L0–L4)
Score each pillar L0 (nothing) → L4 (automated, measured) **once client data arrives**. All cells currently: *requires client data*.

| Pillar | L0 | L2 (typical Egyptian D2C) | L4 (target) | Status |
|---|---|---|---|---|
| P1 Data foundation | Orders live only in Shopify, never exported | Periodic exports, no dedupe | Unified customer record keyed on phone, deduped across Shopify/IG/WhatsApp | requires client data |
| P2 Channel capture | No opt-in anywhere | Email popup only | WhatsApp opt-in at checkout + IG bio + post-delivery | requires client data (external surfaces suggest L0–L1 [S08][S10], HYPOTHESIS) |
| P3 Segmentation | None | Manual "bought Ramadan" lists | RFM + category affinity (footwear vs kimono buyer) auto-segments | requires client data |
| P4 Lifecycle automation | None | Abandoned-cart email only | Welcome → post-COD-delivery WhatsApp → replenish/season → win-back | requires client data |
| P5 Attribution | None | Last-click Shopify report | UTM + CTWA + coupon-code attribution per channel | requires client data |
| P6 Team & tooling | Founder's phone | Shared inbox | Named owner + CRM tool (even Shopify-native) + weekly KPI review | requires client data |

### 4. The 10 discovery questions WOM asks (verbatim, for the client call)
1. Where does your customer data live today — Shopify only, a spreadsheet, or a CRM tool? Who can access it?
2. How many unique customers have ever ordered, and how many ordered more than once in the last 12 months? (If unknown: may we run the Shopify export?)
3. What percentage of orders are COD vs prepaid, and what is your COD refusal/return-at-door rate? [Policy context: S03]
4. Do you collect WhatsApp opt-in at checkout or after delivery? Is there a business WhatsApp number, and who answers it?
5. How are orders that start in Instagram DMs or comments recorded — do they enter Shopify or bypass it?
6. Do you have an email/SMS list? Size, last send date, open rate?
7. When you run Ramadan / Black Friday / Eid promotions [S04 tags], do you notify past buyers directly, or does the offer only live on the site?
8. Who is your best customer — can you name your top-10 repeat buyers and what they buy (leather footwear vs kimonos)?
9. What happens after a delivery is confirmed — any thank-you, review request, or reorder prompt?
10. Which single number do you check weekly to know the business is healthy — and where does it come from?

### 5. Data-availability matrix (what the audit can compute from a Shopify export alone)
- **Derivable without any CRM tool**: repeat rate, RFM segments, AOV by category, COD share, geographic split (Cairo/Alex vs other), Ramadan-cohort LTV — one Shopify orders export suffices. [Method note; grade of outputs will be HELD once export received]
- **Requires client interviews/tooling**: DM-order volume, WhatsApp conversation history, refusal-at-door reasons, team workflow. All GAP until discovery.

## Harness Enrichment — revops
**Pattern captured: "COD-verified phone = CRM primary key" (Egyptian D2C).** In check-on-delivery markets [S03 HELD], every fulfilled order yields a courier-verified phone number — higher quality than any email popup. The revops play is to treat the Bosta/in-house delivery confirmation event as the CRM ingestion trigger (post-delivery WhatsApp opt-in message), inverting the Western email-first stack. Reusable across all Egypt D2C audits; added as a default P2/P4 probe in the 6-pillar ladder above.

## Harness Enrichment — data:analyze
**Pattern captured: external-perimeter CRM inference table.** When CRM state is client-internal, build the audit from externally observable exhaust: open `products.json` (proves platform + promo calendar) [S04], published shipping/refund policy (proves COD + courier stack) [S03], owned-caption scan for WhatsApp/offer CTAs (n= and window disclosed) [S08], and bio-link inventory [S10]. This yields a defensible L0–L1 *hypothesis* band before a single client call — and turns discovery question 10 into a validation test rather than a cold ask.

## Era Snapshot
- Cielito's internal CRM state is entirely uncaptured — every maturity cell is "requires client data"; framework + 10 discovery questions shipped instead. [GAP, by design]
- Shopify platform is proven via open products.json, so a customer/order table exists even if unexploited. [S04, HELD]
- COD via Bosta/in-house couriers means every order carries a verified phone number — a dormant WhatsApp-CRM asset. [S03, HELD]
- Zero WhatsApp CTAs across 17 owned IG captions (2026-05-31→07-04) and none in bio → no visible WhatsApp funnel on captured surfaces. [S08][S10, HELD for surfaces; systematic absence = HYPOTHESIS]
- Brand demonstrably runs a promo calendar (Ramadan/Black Friday/Eid tags on catalog) but no offer language reaches owned social — promo-to-CRM loop likely broken. [S04][S05][S08; HYPOTHESIS]
