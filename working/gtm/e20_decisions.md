# [GTM] Era 20 — GTM Decision Layer — Cielito Egypt (base 360, 2026-07-09)
ANNOUNCE: Converts the base-360 evidence into three concrete GTM-side decisions (channel priority · creator program · WhatsApp funnel), each with evidence, sequence, and owner-role — distinct from ATLAS Era-20 but consistent with it.

## Agents Run
- GTM Product Manager (era owner) — decision arbitration and sequencing
- insight-generator operator — evidence-to-decision distillation from S04/S08/S09/S10
- strategic-report operator — decision-record formatting and dependency mapping

## Findings

The base-360 produced one dominant structural insight the whole decision layer hangs on: **Cielito's attention economy is inverted.** The brand's owned Instagram output earns a median of 3 likes and 0.006% median ER (n=17 owned posts, window 2026-05-31→07-04) [S08, HELD], while earned/UGC posts that merely *tag* the brand reach up to 5,930 likes / 124,937 views — roughly 200x the owned median [S08, HELD]. The brand has a verified 88,903-follower account [S10, HELD] that behaves like a dead channel, next to an accidental creator engine (tagging creators + the founder's own account, 8 of 34 earned posts [S08, HELD]) that actually works. Every decision below is a response to that inversion.

### D1 — Channel Priority Decision
**Decision:** Reallocate effort from polished owned-feed IG posting to (a) earned/creator-amplified Instagram and (b) Arabic-language TikTok — BEFORE any paid spend.
**Evidence:**
- Owned IG: median 3 likes, mean 5.1, median video views 655, cadence 3.5/wk — effort is being spent (17 posts in 5 weeks) for near-zero return [S08, HELD].
- Best owned post is the one masri-language skit (تسنيم وزعت رقم مديرتها…): 39 likes / 926 views — 13x the owned like median [S08, HELD]. 16/17 owned captions are English-only [S08, HELD]; Egypt context law: masri outperforms.
- TikTok: Arabic videos outperform — باشا مصر at 14.8K plays and skit-style Arabic clips at 2.4–3.3K plays vs 1,220 median plays (n=60, window 2026-04-13→07-01) [S09, HELD]. But the account dilutes itself: #startyourbusinessnow / #contentcreationtips founder-journey content shares the brand handle [S09, HELD].
- Website can receive traffic: SEO 100, desktop 98 — but mobile 55 taxes every mobile click [S06, HELD].
**Sequence:** Week 1–2 — content mix flips to masri-first skit/UGC formats on both platforms; TikTok brand account stops posting content-creation-tips material (move to founder's personal channel). Paid amplification decision deferred until D3 funnel exists.
**Owner-role:** GTM Product Manager sets the mix; Content/Community Lead executes.
**Grade of decision basis:** HELD (all inputs primary captures).

### D2 — Creator-Program Decision
**Decision:** Formalize the accidental creator engine into a structured, zero/low-cost creator program (seed products → track → repost rights) before any influencer spend.
**Evidence:**
- The mechanism already works unmanaged: top earned post 5,930 likes / 124,937 views; a pyramids-outfit sidecar tagging @cielitoegypt drew 2,473 likes / 86 comments [S08, HELD].
- The founder (awadlolwa) is already an in-house creator — 8 of 34 earned posts [S08/S11, HELD/LIKELY], and owned posts tag creators (e.g., @ayaaraffa) [S08, HELD].
- Creators use #ugc/#ugccreator on brand-tagged content [S08, HELD] — they are signalling availability for exactly this program.
- Catalog supports gifting economics: median SKU EGP 1,200; 88 SKUs under EGP 1,000 [S04, HELD] — seedable inventory exists, 218 SKUs in stock [S04, HELD].
**Sequence:** After D1 content flip (week 2–4): identify the 10–20 creators already tagging the brand (capture shows at least several distinct accounts; full roster = GAP, needs a tagged-mentions sweep), ledger them, seed product, negotiate whitelisting/repost. Paid creator fees only after organic seeding shows repeatable lift.
**Owner-role:** GTM Product Manager owns program design; Community/Partnerships Lead runs the creator CRM (scaffolded in Era 21).
**Grade of decision basis:** HELD for mechanism; GAP for full creator roster.

### D3 — WhatsApp Funnel Decision
**Decision:** Stand up a WhatsApp Business funnel (catalog + click-to-WhatsApp CTAs on IG bio, site, and captions) as the missing conversion bridge. This is the cheapest, highest-certainty fix and sequences FIRST.
**Evidence:**
- 0 of 17 owned captions contain a WhatsApp CTA; 0 contain offer language [S08, HELD] — despite 96/250 SKUs (38%) being on sale on-site [S04, HELD]. The discounts exist but are never merchandised socially.
- No WhatsApp link on site or IG bio (HELD for captured surfaces) [S01/S10]; bio links to website only [S10, HELD].
- Egypt context law: WhatsApp is THE conversion bridge; the brand's own shipping policy is conversational by design — check-on-delivery, in-house couriers for multi-item try-ons "inform us so we can send it via an in-house courier" [S03, HELD] — an operations model that begs for a chat channel and currently has no captured entry point.
- Mobile PageSpeed 55 [S06, HELD] makes chat-first conversion MORE valuable: WhatsApp sidesteps the slow mobile web path.
**Sequence:** Week 1 (before D1/D2 fully land): WhatsApp Business + product catalog + bio/site CTAs; then every D1 post and D2 creator brief carries the WhatsApp CTA. Measurement = message volume and order attribution (baseline = GAP; no conversion data captured — client-side, inaccessible not absent).
**Owner-role:** GTM Product Manager owns funnel spec; Store/Ops owner (client-side) owns WhatsApp number and reply SLA.
**Grade of decision basis:** HELD (absence verified on all captured surfaces; Egypt-context law applied as doctrine, not data).

**Decision dependencies:** D3 → D1 → D2 → (only then) paid media → (only after funnel proof) Era 18/19 GCC playbooks. Consistent with ATLAS Era-20's decision set; this layer owns the GTM sequencing, not the venture-level bets.

## Harness Enrichment — insight-generator
New reusable pattern: **"attention inversion ratio"** — owned-median engagement vs earned-top engagement on the same platform (here ~3 likes vs 5,930 = ~200x within one capture window [S08, HELD]). When the ratio exceeds ~10x, the insight-generator should auto-flag "creator engine > owned polish" as the lead GTM insight and route channel decisions accordingly. Second pattern: **CTA-absence scan** (WhatsApp mentions=0, offer language=0 across owned captions) as a standard fast check for Egypt/MENA D2C — absence of a conversion bridge is itself a top-3 insight, cheap to verify from any owned-posts digest.

## Harness Enrichment — strategic-report
Enrichment for the decision-record format: each GTM decision now carries five mandatory fields — Decision · Evidence (S-id + grade + n/window) · Sequence (with explicit dependency arrows D3→D1→D2) · Owner-role (agency-side AND client-side split, as in D3's funnel-spec vs reply-SLA split) · Grade-of-decision-basis. The D3 record demonstrates the strongest template: a decision justified by verified *absence* (0 CTAs on all captured surfaces) plus a context law, with baseline metrics honestly marked GAP rather than projected. Adopt this as the strategic-report house pattern for "missing infrastructure" decisions.

## Era Snapshot
- Attention inversion is the master insight: owned median 3 likes vs earned top 5,930 likes / 124,937 views (~200x) on the same IG [S08, HELD]
- D1: flip channel effort to masri-first earned/UGC formats on IG + Arabic TikTok; de-mix founder-journey content from the brand TikTok [S08/S09, HELD]
- D2: formalize the already-working creator engine (founder = 8/34 earned posts; creators self-tag #ugc) into a seeded program; full roster = GAP [S08, HELD/GAP]
- D3 fires first: WhatsApp funnel — 0 CTAs on any captured surface despite 38% of catalog on sale and a chat-native ops model [S08/S04/S03, HELD]
- Paid media and GCC playbooks (Eras 18/19) stay gated behind D3 funnel proof; conversion baseline = GAP (client-side, inaccessible not absent)
