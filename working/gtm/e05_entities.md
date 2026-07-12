# [GTM] Era 5 — Entity Resolution — Cielito Egypt (base 360, 2026-07-09)

ANNOUNCE: Resolves every identity in the estate — the two "Cielito" domains, the brand's handles across three platforms, the founder entity, the creator/UGC entities (including a duplicate-handle merge), and the rival roster dedup — so downstream eras never mix entities.

## Agents Run
- **GTM Entity Resolver** (era owner) — canonical entity table + alias merges
- domain-identity-forensics (sub-pass) — mycielito.com Shopify internals inspection
- handle-crosswalk (sub-pass) — site↔IG↔TikTok↔FB identity chain verification

## Findings

### 1. cielitoeg.com vs mycielito.com — RESOLVED (major finding)
The prior anchor treated the relationship as a full GAP. Direct inspection of the persisted `raw_mycielito.html` [S12] resolves most of it:

| Signal (from raw_mycielito.html) | Value | Implication |
|---|---|---|
| `Shopify.shop` | `my-cielito-artesanias-mexicanas.myshopify.com` | "Artesanías Mexicanas" = Mexican handicrafts store |
| `Shopify.currency` | USD (rate 1.0) | Not an EGP storefront |
| `Shopify.country` / locale | US / en_US | US-market shop |
| `<title>` | "My Cielito – My Cielito" | Different brand name form |
| Shop ID | 53887107269 | Distinct Shopify tenant from cielitoeg.com |

**Resolution: mycielito.com is LIKELY an unrelated business — a US-based Mexican-artisan-crafts Shopify store that happens to share the Spanish word "Cielito".** Its earlier description as showing "shoes collections" [S11] is consistent with Mexican huarache/artisan footwear, not the Egyptian brand. Contradicting evidence in the files: none (grep for egypt/EGP/cairo in S12 = 0 brand-relevant hits). Residual GAP: no registrar/ownership record captured, so common ownership cannot be 100% excluded — but every captured signal points away from it. **Action: demote the watch-register severity; stop treating mycielito.com as a client surface; keep as a name-collision disambiguator.** [S12, LIKELY]

**Entity-resolution rule minted for this estate:** "Cielito" is a high-collision Spanish diminutive (cf. Cielito Lindo, Cielito Querido). Require an Egypt signal (EGP/"LE" pricing, cielitoeg.com reference, @cielitoegypt handle, Arabic content) before attributing ANY "Cielito"-named asset to the client. [HELD as rule]

### 2. Brand handle crosswalk — @cielitoegypt across platforms

| Platform | Handle | Verification | Evidence | Grade |
|---|---|---|---|---|
| Website | cielitoeg.com ("Cielitoegypt" in title/footer, © 2026) | canonical | S01/S02 | HELD |
| Instagram | @cielitoegypt — 88,903 followers, 1,368 posts, verified badge, business "Clothing (Brand)", 17 highlights | **Bidirectional chain:** IG bio externalUrl → `http://www.cielitoeg.com/` AND site footer → Instagram | S10 + S01 | HELD |
| TikTok | @cielitoegypt — 7,608 followers, 584 videos, 35.3K hearts | Same handle string; content = same products/campaigns (e.g., "باشا مصر" video appears on BOTH IG mixed capture 2026-05-28 and TikTok 2026-05-28) — cross-platform content fingerprint match | S09 + S08 | HELD |
| Facebook | "cielitoegypt" page exists, posts in Arabic | Search-tier only; stats blocked (route FQ1) | S11 | LIKELY (existence); metrics GAP |
| Threads | Footer link present on site | Never captured; live status unknown (route FQ8) | S01 | HELD link exists; content GAP |
| WhatsApp | — | No WhatsApp link on site footer, IG bio, or any of 17 owned captions (n=17, window 2026-05-31→07-04) | S01/S10/S08 | HELD absent on captured surfaces (Egypt's #1 conversion bridge is missing) |

### 3. Founder entity — Lolwa Awad
- Canonical: **Lolwa Awad**, founder (~Feb 2021), IG **@awadlolwa** (`ownerFullName: "Lolwa Awad"` in captured posts). Press bio: International Relations (QMUL), economics/development (LSE), ex-PR UK+Egypt. [S11, LIKELY for bio; S08 HELD for handle identity]
- Behavioral fact: @awadlolwa authored 8 of 34 earned/tagged posts in the mixed capture (n=60, window 2026-05-21→07-08) — founder-as-face is an ACTIVE asset, posting brand content in masri Arabic (e.g., "العالم كله بقى شبه بعضه" video 2026-06-11). [S08, HELD]
- The fruit-leather origin story (aloe/prickly pear/pineapple, "first in Egypt") attaches to this entity via press only; zero trace on live site [S02 grep = 0]. Keep as HYPOTHESIS (differentiator dropped) on the founder node, not the brand node.

### 4. Creator/UGC entity dedup (from mixed IG capture, n=60 items + comment authors)
- **Duplicate-handle merge: `haninemoussaa` (20 occurrences) and `haninemoussa__` (7 occurrences) are two handles of the same creator (Hanine Moussa)** — the #haninemoussa hashtag appears in the capture's top hashtags. Merge into one entity before any creator-leaderboard is built. [S08, LIKELY]
- **Provenance caveat (binding):** the mixed-capture digest (`social_intel.json`) records `"handle": "haninemoussaa"` at the top level — an artifact of the tag/mention-based pull, NOT ownership. Its blended stats (median 3 / mean 175 / max 5,930 likes) mix owned + earned; only `instagram_owned_intel.json` (n=17) speaks for the brand account. [S08, HELD]
- Top distinct creator entities by capture presence: Hanine Moussa (merged, 27), sameha_kira (15), awadlolwa (10, = founder), zreelcreator (7), fatma_gamal99 (7), zeinab_mohamedx1 (5), yasmeendabees (5). One outlier: `wafferlyclub` (1 item) — appears to be a deals/offers account, flagged to Era 6 as a potential channel-partner signal. [S08, HELD counts]

### 5. Rival entity dedup
- **Dejavu:** only **@dejavu.egypt** (289K IG, 653 posts, "Egypt's leading brand of Footwear & Bags", FB ≈ 2.3M) is evidenced in the corpus [S11, LIKELY]. The alias "dejavushoes" appears in NO captured file — treat as an UNVERIFIED possible alias; do NOT merge or cite until the competitive wave verifies which handle(s) are official. [GAP, flagged]
- **Morena / Pellame:** the corpus lists them on one row ("newer leather heels/flats entrants", cairoscene) — unresolved whether this is one entity or two. Keep as TWO provisional entities pending verification. [S11, GAP]
- **Elia Shoewear** (eliashoewear.com, founded 2015): keep the full form as canonical — "Elia" alone is too generic to be a safe key. [S11, LIKELY]
- **CHOU** canonical handle @chou.egypt; **Parfois Egypt** is the local arm of international chain Parfois (parfoisegypt.com) — tag as INTERNATIONAL-CHAIN class, different competitive logic. [S11, LIKELY]
- No captured evidence connects any rival to the mycielito.com store. [HELD]

## Harness Enrichment — wiki-linker
Canonical entity nodes proposed for the estate wiki (aliases → canonical, with owning route ATLAS-DM for social identities, ATLAS-WB for domains):
- `entities/cielito_egypt.md` ← aliases: Cielito, Cielitoegypt, @cielitoegypt (IG/TikTok/FB), cielitoeg.com. NOT an alias: mycielito.com, My Cielito.
- `entities/my_cielito_artesanias.md` ← mycielito.com, my-cielito-artesanias-mexicanas.myshopify.com — tagged `name-collision`, `not-client`, backlink to cielito_egypt.md with a disambiguation note (one-way "confusable-with" edge, never an ownership edge).
- `entities/lolwa_awad.md` ← @awadlolwa, "Lolwa Awad" — edges: founder-of → cielito_egypt; carries the fruit-leather HYPOTHESIS.
- `entities/hanine_moussa.md` ← haninemoussaa + haninemoussa__ (merged) — edge: top-UGC-creator-for → cielito_egypt.
- `entities/dejavu_egypt.md` ← @dejavu.egypt (canonical); `dejavushoes` recorded as unverified-alias field, not a link.
- Rival stubs: shoe_room, pixie_eg, achilles_eg, jayda_hany, bulga, elia_shoewear, ramla, chou_egypt, morena_eg (provisional), pellame (provisional), parfois_egypt — all `## Related` discovery edges to cielito_egypt, ownership stays with the competitive wave.

## Era Snapshot
- mycielito.com resolved: LIKELY an unrelated US Mexican-crafts Shopify store (`my-cielito-artesanias-mexicanas`, USD, shop 53887107269) — watch-register severity demoted; residual ownership-record GAP only. [LIKELY]
- Brand identity chain site↔Instagram is bidirectionally verified (bio URL + footer link), and TikTok matches by handle + same-day content fingerprint ("باشا مصر", 2026-05-28 both platforms). [HELD]
- Founder entity Lolwa Awad (@awadlolwa) is an active earned-media asset: 8/34 tagged posts in mixed capture (n=60, 2026-05-21→07-08), posting in masri while the brand posts in English. [HELD activity / LIKELY bio]
- Creator dedup merged haninemoussaa + haninemoussa__ into one entity (27 capture items) — and the mixed-capture digest's top-level handle field is a provenance artifact, never ownership. [LIKELY merge / HELD caveat]
- Dejavu's only evidenced handle is @dejavu.egypt; "dejavushoes" is unverified — merge blocked until the competitive wave confirms. [GAP]
