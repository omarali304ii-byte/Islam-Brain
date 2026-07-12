# Source Registry — cielito-egypt base 360 (2026-07-09)

All sources persisted locally under the run folder. Every era claim must cite an S-id + grade.
Grades: HELD (primary capture, verified) · LIKELY (strong secondary / single primary) · ESTIMATE_ONLY (banded/derived) · SELF_REPORTED (client/brand's own claim) · HYPOTHESIS (plausible, unverified — never plotted) · GAP (missing).

| ID | Source | Type | Path | Grade ceiling |
|----|--------|------|------|---------------|
| S01 | cielitoeg.com homepage (2026-07-09) | primary capture | `_sources/website/raw_homepage.txt` | HELD |
| S02 | About-us page text | primary capture (brand's own copy) | `_sources/website/text_about.txt` | SELF_REPORTED for claims about quality; HELD for what-the-page-says |
| S03 | Shipping + refund policy text | primary capture | `_sources/website/text_shipping.txt`, `text_refund.txt` | HELD (as published policy) |
| S04 | Full Shopify catalog — 250 products, prices, types, availability, dates | primary capture (open products.json) | `_intel/catalog_full.json` (+ raw `_sources/website/products_p1.json`) | HELD |
| S05 | Collections structure — 30 collections w/ counts | primary capture | `_sources/website/raw_collections.json.txt` + `_intel/catalog_intel.json` | HELD |
| S06 | PageSpeed audit M55/D98 (perf), SEO 100 | instrument (Google PSI API) | `instruments/pagespeed_audit.json` | HELD |
| S07 | Agent-readiness audit Grade B 72/100, security CLEAN | instrument (own-endpoint script) | `instruments/agent_readiness_audit.json` | HELD |
| S08 | Instagram captures: 60 mixed items (26 owned + 34 tagged/UGC incl. 8 founder posts) + 50-item corrective owned pull (17 unique owned posts, window 2026-05-31→07-04) | primary capture (paid R1/R1b, $0.253) | `_sources/social/instagram_posts.json`, `instagram_owned_posts.json`, digests `_intel/social_intel.json`, `_intel/instagram_owned_intel.json` | HELD (n= and window MUST be disclosed) |
| S09 | TikTok capture: 60 videos, window 2026-04-13→07-01; account 7,608 followers / 584 videos / 35.3K hearts | primary capture (paid R2, $0.181) | `_sources/social/tiktok_videos.json` + digest in `_intel/social_intel.json` | HELD (n=60 disclosed) |
| S10 | IG profile parent data: 88,903 followers · 1,368 posts · verified · business "Clothing (Brand)" · 17 highlights · bio + external link | primary capture | `_intel/instagram_profile.json` | HELD |
| S11 | Web-search corpus: founder (Lolwa Awad), fruit-leather press story, market size (EGP 31.4bn 2025, +9%), rival set (Dejavu 289K IG etc.) | secondary sources | `_sources/search/search_corpus.md` | LIKELY max; market sizes ESTIMATE_ONLY (source conflict); fruit-leather = HYPOTHESIS (dropped from live site) |
| S12 | mycielito.com second domain (resolves, Shopify) | primary capture | `_sources/website/raw_mycielito.html` | HELD that it exists; relationship = GAP |
| S13 | Operator intake (WOM pitch trigger, lens stack, approvals) | operator | `../ESTATE_STATE.json` | context only, not client-facing evidence |

**Known blocked/uncaptured (inaccessible ≠ absent):** Facebook page stats · rival social metrics beyond Dejavu snippet · Google reviews/ratings · marketplace presence (Noon/Amazon EG/Jumia) · paid-ads library status · conversion/revenue data (client-side). These are data-pass routes, never claims of absence.
