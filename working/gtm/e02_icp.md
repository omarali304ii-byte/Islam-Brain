# [GTM] Era 2 — ICP Intelligence — Cielito Egypt (base 360, 2026-07-09)

ANNOUNCE: Builds the consumer persona set strictly from captured evidence — catalog mix, UGC creator profiles, hashtags, and comment language — with no invented demographics.

## Agents Run
- **GTM ICP Strategist** (era owner) — persona synthesis + evidence gating
- customer-research agent — comment-language + purchase-intent mining from S08 raw
- market-research agent — catalog-to-demand-segment mapping from S04/S05
- gtm-icp-persona-builder agent — persona card assembly with n-disclosure

## Findings

### Evidence base for personas (disclosed up front)
- Catalog: 250 SKUs with type/tag/collection structure [S04/S05, HELD]
- Social: 60 mixed IG items (26 owned + 34 tagged/UGC incl. 8 founder posts), window 2026-05-21→07-08 [S08, HELD]; 17 unique owned posts, window 2026-05-31→07-04 [S08, HELD]; 60 TikTok videos, window 2026-04-13→07-01 [S09, HELD]
- **No age/geo/income data was captured anywhere.** Audience demographics = GAP (IG/TikTok audience insights are client-side; data-pass route). Every persona below is behavior- and product-anchored, not demographic.

### Persona 1 — The Modest-Fashion Kimono/Abaya Buyer
- **Product anchor:** 34 kimonos (33 "Kimonos" + 1 "kimono" type) [S04, HELD]; abayas, Moroccan jalabeyas/kaftans on page-1 detail (Basic Open Abaya, Dome Abaya, Morroccan Jalabeya ×5 colorways, Morroccan Kaftan) [S05, HELD]; Ramadan is the brand's biggest single collection — 77 products, plus Ramadan Kimono (22) and Ramadan Sale 2026 (78) [S05, HELD].
- **Social anchor:** #hijabers / #hijaber hashtags appear in the mixed capture [S08, HELD]; top UGC creator "Nina" (haninemoussaa) posts hijab-friendly styling of Cielito pants/vests, incl. the 124,937-view post [S08, HELD].
- **Price band:** EGP 900–1,600 core (kimonos 900–1,400, abayas/jalabeyas 960–1,280) [S04/S05, HELD].
- **Buying rhythm:** Ramadan/Eid peak — proven by catalog tag machinery ("Celebrate Eid with 30% OFF", "ramadan 2026" 12 tags on page 1 alone) [S05, HELD]. This is the seasonal revenue engine persona.

### Persona 2 — The Occasion-Heels Buyer
- **Product anchor:** Heels collection carries the handle **"wedding-season"** (13 products) [S05, HELD] — the store's own information architecture names the occasion. Genuine-leather heels with nappa lining, "international-standard heels made in Egypt" [S02, SELF_REPORTED]; vegan-leather heel line alongside [S02, SELF_REPORTED].
- **Founder framing:** brand founded on a "one shoe, morning-to-soirée" insight [S11, LIKELY — press]. The versatile-occasion shoe is the founding persona.
- **Price context:** footwear sits mostly in the 1,000–2,500 band (156/250 SKUs catalog-wide) [S04, HELD].
- **Note:** no wedding/occasion UGC was present in the captured social window — content-to-persona coverage gap for the brand's own named occasion segment [S08, HELD absence within window].

### Persona 3 — The Everyday-Comfort Footwear Buyer (slippers/mules/ballerinas)
- **Product anchor:** 31 slippers + 11 sandals + mules + ballerinas/loafers + 7 espadrilles [S04/S05, HELD]; summer-slipper tags across 2024/2025 seasons [S05, HELD]; Sahel/summer content ("Don't miss your perfect Sahel look", 3,592 plays) [S09, HELD].
- **Owned content anchor:** "Coolest slippers ever?" (3 likes, 145 views) [S08, HELD] — the brand targets this persona but the content does not reach her.
- **Price band:** ~EGP 1,200 typical (Diamo slippers 1,200) [S05, HELD]; entry price point of catalog = EGP 400 [S04, HELD].
- **Rhythm:** summer/Sahel season counterweight to Persona 1's Ramadan peak [S05/S09, HELD].

### Persona 4 — The "Cielito Girl": trend-led young follower of the brand's world
- **Social anchor:** brand's own community label #cielitogirl / #cielitolooks in owned captions [S08, HELD]; TikTok mixes product content with founder-journey/creator content (#startyourbusinessnow ×6, #contentcreationtips ×3, #250k ×4) [S09, HELD]; the skit characters (e.g., "تسنيم") recur across TikTok and the single Arabic owned-IG video — which is the ONLY owned post that broke out (39 likes / 926 views vs median 3 / 655) [S08, HELD].
- **Language evidence:** she comments in Egyptian Arabic. Raw comment stream on brand posts: "مقاس البنطلون بليز" (size request = purchase intent), "ماشاءالله جميله في كل حاجه", emoji chains [S08, HELD]. Meanwhile 16/17 owned captions are English-only [S08, HELD] — **the brand speaks English to a masri-speaking buyer.** Arabic-language videos outperform on both platforms (باشا مصر: 14.8K TikTok plays + 7,454 IG views) [S08/S09, HELD].
- **Role:** engagement engine and UGC amplifier rather than necessarily the highest-AOV buyer; she follows creators (Nina et al.) more than the brand account — earned posts reach ~200x owned median [S08, HELD].

### Cross-persona observations
1. Comment purchase-intent arrives as **size/availability questions in Arabic** on social [S08, HELD] — with no WhatsApp bridge to catch them [S08/S10, HELD]. Persona demand is visibly leaking in the comments.
2. Founder Lolwa Awad (awadlolwa) posts brand content from her personal account (8/34 earned posts) [S08, HELD] — founder-as-face is an existing asset for Persona 4.
3. Persona weighting by catalog share: clothes/kimonos ≈ modest-fashion lead, footwear = 76-product collection [S05, HELD]. Revenue weighting = GAP (no sales data).

## Harness Enrichment — customer-research
Enrichment: comment-mining rule added — in Egyptian fashion D2C, treat Arabic size/price questions in comments ("مقاس... بليز") as bottom-funnel intent signals and count them as leads-lost when no DM/WhatsApp routing exists. Also captured: UGC-creator handles (haninemoussaa, zeinab mohamed, fatma_gamal99, hoda.arafa1 as repeat commenter) form a seed list for a future creator-audience overlap study (data-pass route).

## Harness Enrichment — market-research
Enrichment: catalog-as-persona-proxy method validated — collection handles chosen by the merchant ("wedding-season", "ramadan-collection", "casual-summer-2024") are self-declared demand segments and outrank inferred taxonomy. Reusable for any Shopify client: read handles, not just titles. Limitation logged: 128/250 untyped SKUs [S04] degrade type-level persona weighting — hygiene fix is a research-quality prerequisite, not just UX.

## Harness Enrichment — gtm-icp-persona-builder
Persona cards assembled with hard evidence gates: 4 personas, each anchored to ≥2 independent sources (catalog + social). Builder rule enforced and worth keeping: **demographics left blank rather than modeled** — Egypt-typical age/SEC bands were NOT imputed because zero demographic capture exists; card schema now carries an explicit `demographics: GAP (client-side insights required)` field instead of silently borrowing market-report averages.

## Era Snapshot
- 4 evidence-anchored personas: Modest-fashion kimono/abaya (Ramadan engine), Occasion-heels ("wedding-season" handle), Everyday-comfort slippers (Sahel/summer), and the "Cielito Girl" trend follower — HELD [S04/S05/S08/S09]
- Language mismatch is the defining ICP finding: buyers comment in masri with purchase intent; brand posts 16/17 English-only — HELD [S08, n=17 owned, 2026-05-31→07-04]
- Bottom-funnel demand leaks in comments (Arabic size requests) with no WhatsApp/DM bridge to capture it — HELD [S08/S10]
- Occasion-heels persona has zero UGC coverage in the captured window despite being a named store segment — HELD-for-window [S08]
- All persona demographics (age/geo/income/SEC) = GAP — requires client-side IG/TikTok audience insights via data pass
