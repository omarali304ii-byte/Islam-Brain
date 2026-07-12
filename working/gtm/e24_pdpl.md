# [GTM] Era 24 — PDPL Compliance Sprint — Cielito Egypt (base 360, 2026-07-09)
ANNOUNCE: Egypt PDPL (Law 151/2020) readiness sprint for a Shopify D2C — data inventory, Oct 31 2026 deadline duties, DPO question, processor posture (Shopify/Bosta/in-house couriers), UGC/creator PII, and WhatsApp opt-in design — as a concrete checklist for Cielito.

## Agents Run
- GTM Compliance Auditor (owner)
- Data Inventory Mapper
- Processor Posture Assessor
- Risk Register Builder

## Findings

### 1. Regulatory frame
Egypt's Personal Data Protection Law (Law 151/2020) applies to Cielito as a controller processing Egyptian customers' personal data; the estate's standing compliance guidance (mena-compliance-implementation-guide) flags **Oct 31, 2026 as the critical Egypt PDPL compliance deadline** — under 4 months from this run date (estate compliance doctrine; statutory interpretation should be confirmed by counsel — LIKELY, not legal advice). PDPL requires lawful basis, consent for direct marketing, breach notification to the Data Protection Center, controller/processor licensing-permits, and appointment of a Data Protection Officer for qualifying controllers. Nothing in the captures shows any PDPL-facing artifact beyond a privacy-policy nav link: the page EXISTS in site navigation [S03] HELD, but its CONTENT was not captured (GAP) — whether it is a localized PDPL-aware policy or a default Shopify template is a HYPOTHESIS to verify in the next pass.

### 2. Data inventory — what personal data Cielito demonstrably or necessarily processes
| # | Data set | Evidence | Grade | PDPL sensitivity |
|---|---|---|---|---|
| 1 | Order PII: name, mobile number, delivery address | Inherent to Shopify checkout + COD delivery model [S03] HELD (shipping policy describes courier delivery) | HELD (existence) | Core — highest volume |
| 2 | Customer accounts (login, order history, profile) | Site nav shows Sign in / Orders / Profile [S03] HELD | HELD | Core |
| 3 | Payment data | COD culture (check-on-delivery [S03] HELD); online card acceptance status = GAP | HELD/GAP | If cards: gateway-held, verify scope |
| 4 | Courier-side PII copies: phone + address on Bosta manifests AND in-house courier run sheets | Shipping policy names both channels [S03] HELD | HELD (existence) | HIGH — in-house courier handling is the least-governed copy |
| 5 | Cookies / pixels / analytics IDs | Shopify default cookies certain; Meta/TikTok pixel presence NOT captured | GAP | Consent-banner question |
| 6 | Marketing lists (email/SMS) | Account system implies email capture [S03]; list size/opt-in records = GAP | GAP | Direct-marketing consent required |
| 7 | UGC/creator PII: tagged creators' handles, faces, reposted content (e.g., @ayaaraffa repost in owned feed; creator posts n=34 tagged incl. 8 by founder account) | [S08] HELD (window 2026-05-21→07-08) | HELD | Consent/release for reuse = GAP |
| 8 | WhatsApp conversation data | Currently ZERO WhatsApp presence on captured surfaces [S08][S10] HELD — but every growth era (E22/E23) recommends building it → opt-in design is a PRE-launch duty | HELD (absence) | Future — design-stage |

### 3. Processor posture
- **Shopify (platform processor):** stores all order/customer data outside Egypt — PDPL's cross-border transfer provisions (permit/adequacy) apply; Cielito needs Shopify's DPA on file and a documented transfer rationale. Shopify's own OAuth well-known endpoints are live on the domain [S07] HELD (standard Shopify infrastructure). Action: download Shopify DPA, record it in the processing register. (Posture = LIKELY; contractual state = GAP.)
- **Bosta (delivery processor):** receives name/phone/address per shipment [S03] HELD. Action: confirm a data-processing clause exists in the Bosta agreement; Bosta's retention of delivered-order PII = GAP.
- **In-house couriers (internal processing, highest practical risk):** shipping policy explicitly routes multi-item try-on orders to in-house couriers [S03] HELD. Run sheets/phones used by couriers are an ungoverned PII copy — device policy, sheet destruction, and access rules = GAP (requires client input).
- **Meta/TikTok (if pixels present):** pixel firing = data sharing with a foreign processor; status = GAP — verify before the deadline.

### 4. Cielito PDPL sprint checklist (concrete, sequenced)
1. **Week 1 — Inventory & register:** confirm the 8-row inventory above with the team; open a Records-of-Processing register (controller entry per row).
2. **Week 1 — DPO question:** decide DPO appointment (internal vs outsourced). Given single-brand D2C scale, an outsourced/part-time DPO is the proportionate route; register with the Data Protection Center as required (LIKELY interpretation — counsel to confirm licensing/permit class for controller status).
3. **Week 2 — Privacy policy rewrite:** replace/verify the uncaptured policy page (GAP) with a PDPL-aware bilingual (Arabic-first) policy: lawful bases, retention periods, courier/Bosta/Shopify disclosures, DSR contact channel.
4. **Week 2 — Consent surfaces:** cookie/pixel audit (GAP #5) → consent banner if pixels found; add explicit marketing opt-in checkbox at checkout (unticked by default) for email/SMS.
5. **Week 3 — Courier hardening:** in-house courier SOP — minimum data on run sheets, end-of-day destruction, no personal-phone storage of customer numbers; Bosta DPA check.
6. **Week 3 — UGC/creator releases:** lightweight repost-consent record (DM confirmation archive) for every creator whose content is reposted (row 7 [S08] HELD shows reposting is current practice, e.g., @ayaaraffa).
7. **Week 4 — WhatsApp opt-in design (pre-build):** if/when the E23 journey launches, use checkout-stage explicit opt-in + WhatsApp Business verified profile; log opt-in timestamp per number BEFORE first message.
8. **Week 4 — Breach playbook:** 72-hour-style internal notification path (owner → DPO → Data Protection Center template letter), courier-loss scenario included.
9. **Ongoing:** DSR (access/delete) response procedure — Shopify admin export/redact covers most requests; assign a named owner.

## Harness Enrichment — mena-compliance-implementation-guide
New Egypt-D2C pattern for the guide: **the COD/in-house-courier PII copy** is the compliance blind spot generic (EU-templated) checklists miss — Shopify-side data gets DPA coverage, but physical run sheets and courier phones carry the same PII with zero contractual or technical control [S03] HELD (channel existence). Add a "last-mile PII" module: run-sheet minimization, destruction SOP, courier device rules. Second addition: **repost-consent archive** as the minimum-viable UGC compliance artifact for brands whose growth engine is creator content (Cielito's earned posts outperform owned ~200x [S08] HELD — the compliance surface grows exactly where the growth plan points).

## Harness Enrichment — least-privilege-audit
Access-scope question set generated for Cielito (all answers = requires client input, GAP): (1) How many Shopify admin/staff accounts exist, and does the in-house courier team have any Shopify access beyond order-fulfillment view? (2) Who holds the Instagram/TikTok credentials — brand phone, founder personal device [S11 shows founder account posting brand content — LIKELY], or agency? (3) Is customer data ever exported to spreadsheets for courier routing, and where do those files live? (4) Shared accounts/MFA status on Shopify, Meta Business, and the domain registrar (two domains exist: cielitoeg.com + mycielito.com [S12] HELD, relationship GAP — orphaned second-store admin access is itself a least-privilege risk). Audit verdict: cannot score until client answers; question set is the deliverable.

## Harness Enrichment — smartprods-risk-register
| Asset | Threat | Vulnerability | Impact | Control |
|---|---|---|---|---|
| Order PII in Shopify | Cross-border processing without documented basis | No DPA/transfer record evidenced (GAP) | Regulatory exposure at Oct 2026 deadline | Shopify DPA on file + processing register (Checklist #1/#2) |
| Courier run sheets (in-house) | Physical loss / photo leak of names+phones+addresses | Ungoverned paper/phone copies [S03] HELD channel | PDPL breach + customer trust loss in COD market | Last-mile SOP: minimization + destruction (Checklist #5) |
| Marketing contact list | Unconsented SMS/WhatsApp campaigns | No opt-in surface evidenced; 0 current WhatsApp [S08][S10] HELD | Direct-marketing violation on first campaign | Checkout opt-in + timestamp log BEFORE launch (Checklist #4/#7) |
| Creator/UGC content | Repost without release | Reposting is current practice, releases GAP [S08] | Takedown + PII/name-image claim | DM-consent archive (Checklist #6) |
| Second store mycielito.com | Forgotten admin surface w/ customer data | Relationship + access model GAP [S12] | Unmonitored breach vector | Clarify ownership; decommission or govern (least-privilege Q4) |

## Era Snapshot
- Cielito processes 8 identifiable personal-data sets; the least-governed copy is the in-house courier run sheet, an evidence-backed channel [S03] HELD with zero visible controls (GAP).
- Privacy-policy page exists in nav [S03] HELD but content uncaptured — PDPL-aware vs default-template status = GAP, verify first.
- Oct 31, 2026 deadline gives a ~16-week runway; the 9-step sprint above fits it with weeks 1–4 sequenced (estate compliance doctrine, LIKELY — counsel to confirm).
- WhatsApp opt-in must be designed BEFORE the E23 retention journey launches — currently zero WhatsApp presence [S08][S10] HELD, which is a clean-slate compliance advantage.
- Risk register seeded with 5 rows; least-privilege audit blocked on 4 client questions (Shopify roles, social credentials, exports, mycielito.com [S12] HELD/GAP).
