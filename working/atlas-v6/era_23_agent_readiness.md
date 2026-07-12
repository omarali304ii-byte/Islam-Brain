# [ATLAS-v6] Era 23 — Agent Readiness (GEO/AEO + Injection Security) — Cielito Egypt (base 360, 2026-07-09)
ANNOUNCE: Interprets the already-run own-endpoint agent-readiness instrument (Grade B 72/100), converts category deficits into a concrete fix list usable as pitch ammunition, and names the competitor GEO benchmark as the missing data-pass route.

## Agents Run
- A98 agent-readiness-auditor — interpretation of `instruments/agent_readiness_audit.json` (instrument already executed; no re-run)
- A99 geo-competitive-bench — attempted; NO rival audits exist in this run → declared GAP + data-pass route
- A100 prompt-injection-scanner — verdict read-through from the same instrument (security section)

## Findings

### 1. Overall posture — Grade B (72/100), unusually strong for an Egyptian D2C [S07, HELD]
`cielitoeg.com` scores **72/100 (B)** on the six-category own-endpoint audit. Category breakdown [S07, HELD]:

| Category | Score | What the instrument actually found |
|---|---|---|
| Content Accessibility | 100 | `llms.txt` ✅, `llms-full.txt` ✅, markdown negotiation ✅ |
| Structured Data & Meta | 100 | JSON-LD present (types detected: `Organization` only), meta description ✅, Open Graph ✅, Twitter card ✅, canonical ✅ |
| Security (prompt-injection) | 100 | **CLEAN** — 0 injection hits, 0 suspicious hidden blocks |
| Discoverability | 75 | robots.txt ✅ + sitemap directive ✅ (`/sitemap.xml`); Link header ❌ |
| Protocol Discovery | 33 | OAuth endpoints ✅✅ (Shopify platform defaults); `mcp.json` ❌, `ai-plugin.json` ❌, `agent.json` ❌, `security.txt` ❌ |
| Bot Access Control | 25 | **Zero explicit AI-bot rules** in robots.txt; no content-signals |

Important honesty note vs. the run brief: the lane briefing listed "llms.txt" as a fix item, but the instrument shows **llms.txt and llms-full.txt are already live** (Content Accessibility 100 — almost certainly Shopify's platform-served llms.txt) [S07, HELD]. The real deficits are the two red categories: **Bot Access Control 25** and **Protocol Discovery 33**.

### 2. What the two red categories mean commercially
- **Bot Access Control 25 [S07, HELD]:** robots.txt contains no directives for GPTBot, ClaudeBot, Google-Extended, PerplexityBot, etc. The site is neither deliberately open nor deliberately closed to AI crawlers — it is *undecided by default*. For a 250-SKU catalog with an open `products.json` [S04, HELD], the store is de-facto fully readable by agents but gets zero strategic credit (or control) for it.
- **Protocol Discovery 33 [S07, HELD]:** no `/.well-known/agent.json`, `mcp.json`, `ai-plugin.json`, or `security.txt`. The OAuth endpoints that DO exist are Shopify infrastructure, not brand intent. No agent can discover a sanctioned way to interact with the store programmatically.
- **Schema depth caveat [S07, HELD for the audited surface]:** the instrument detected only `Organization` schema on the audited surface. Product-level schema (`Product`/`Offer`/`AggregateRating`) on PDPs was **not evidenced by this instrument** — verifying/adding PDP schema is a checkable follow-up, not a confirmed defect (audit scope = own-endpoint homepage-level scan).

### 3. Security — CLEAN, a sellable positive [S07, HELD]
Prompt-injection scan: 0 hits, 0 hidden-instruction blocks, verdict "CLEAN — no hidden instructions or prompt-injection vectors." In a pitch, this is a *positive* differentiator slide: the site is safe for AI agents to read today.

### 4. Concrete fix list — pitch ammunition (ordered by effort→impact)
1. **robots.txt AI-bot rules (minutes, biggest single score jump):** add explicit allow rules for `GPTBot`, `ClaudeBot`, `Google-Extended`, `PerplexityBot`, `Applebot-Extended` + content-signals. This is the instrument's own #1 recommendation [S07, HELD]. Moves Bot Access 25 → ~100.
2. **`/.well-known/security.txt` (minutes):** standard contact disclosure; cheap Protocol Discovery points and a trust signal.
3. **`/.well-known/agent.json` (+ optional `mcp.json`) (hours):** declare the brand, catalog endpoint (`/products.json` already open [S04, HELD]), and contact — makes Cielito one of the first Egyptian fashion D2Cs an agent can *discover on purpose*. Forward-looking pitch line, not table stakes.
4. **PDP `Product`+`Offer` JSON-LD verification pass (hours):** confirm Shopify theme emits product schema with price (EGP), availability, and images on all 250 SKUs; add `BreadcrumbList` + FAQ schema on policy pages (shipping/refund copy already exists as clean text [S03, HELD]).
5. **Citeability content layer (days):** the brand's most citeable asset — the "first Egyptian fruit-leather" story — exists only in 2021 press [S11, LIKELY] and has **zero trace on the live site** (HYPOTHESIS: differentiator dropped). Reviving it as an About/FAQ page would give LLMs a unique, ownable fact to cite; today an AI answering "Egyptian leather shoe brands" has nothing distinctive to quote about Cielito.
6. **Mobile performance guard-rail:** PageSpeed mobile 55 vs desktop 98, SEO 100 [S06, HELD] — agent-readiness fixes should ride the same ticket as mobile perf remediation; agents don't care about LCP, but the humans they refer do.

### 5. Competitor GEO bench — GAP (the named data-pass route)
**No rival agent-readiness audits were run in this base 360.** Whether Dejavu (289K IG, market leader [S11, LIKELY]), Shoe Room, Pixie, Achilles, Jayda Hany, Bulga, Elia, Ramla, CHOU, Morena, or Parfois expose llms.txt / AI-bot rules / product schema is **unknown — inaccessible-in-this-run, not absent** [GAP]. **Data-pass route: `geo-competitive-bench` — run the same own-endpoint instrument against 5–11 rival domains ($0, script re-run, ~30 min).** Until then, "Cielito is ahead of its rivals on agent readiness" is a HYPOTHESIS, not a claim; the pitch-safe version is "Grade B with two cheap fixes to A — and we can benchmark the whole rival set on request."

## Harness Enrichment — agent-readiness-audit
Instrument already executed this run (own-endpoint script; NOT the client-side isitagentready.com scanner). Enrichment for the skill's benchmark memory: **Shopify-stack baseline profile** = Content Accessibility 100 (platform llms.txt) + Structured Data 100 + OAuth-only Protocol Discovery (scores 33 from platform defaults alone) + Bot Access 25 when merchant never touched robots.txt. Second Egyptian-market data point after shutterstudio.ai (D 48/100): cielitoeg.com **B 72/100, security CLEAN**. Pattern emerging: platform-hosted stores start ~B on infrastructure alone; merchant-intent categories (bot rules, .well-known) are where grades separate. [S07, HELD]

## Harness Enrichment — ai-seo
Real signal: Cielito's GEO problem is not crawlability (llms.txt live, products.json open [S04/S07, HELD]) — it is **having nothing distinctive for an answer engine to say**. Only `Organization` schema detected; no citeable brand facts on-site; the one unique story (fruit leather, aloe/prickly pear/pineapple [S11, LIKELY]) was dropped from live messaging (HYPOTHESIS). AEO play: publish an Arabic+English brand-facts page (founded ~2021 [S11, LIKELY], handmade in Egypt, materials from Italy/Spain/Germany/India/UK [S02, SELF_REPORTED]), FAQ schema on shipping/COD policy ("check items while the courier waits" [S03, HELD] is a genuinely quotable, Egypt-specific policy), and the fruit-leather revival if the client confirms it is still true (verify first — never re-publish a stale claim). Egypt context: answer-engine queries will come in masri/Arabic; current site copy surface is English-dominant.

## Harness Enrichment — schema-markup
Detected on audited surface: `Organization` only [S07, HELD]. Recommended additive set for a Shopify fashion D2C: `Product` + `Offer` (price EGP, availability — 218/250 in stock [S04, HELD]) on all PDPs; `BreadcrumbList` site-wide; `FAQPage` on shipping/refund (source copy already clean [S03, HELD]); `sameAs` links to IG (@cielitoegypt, verified, 88.9K [S10, HELD]) and TikTok (@cielitoegypt [S09, HELD]) inside Organization. Caveat carried: PDP schema presence unverified by this instrument — verify before claiming absence in any client-facing artifact.

## Era Snapshot
- Grade B 72/100 on own-endpoint audit; Content Accessibility, Structured Data, Security all 100 — HELD [S07]
- Two red categories: Bot Access Control 25 (no AI-bot rules) and Protocol Discovery 33 (no agent/.well-known files beyond Shopify OAuth) — HELD [S07]
- Prompt-injection scan CLEAN (0 hits) — a sellable trust positive — HELD [S07]
- Fix ladder: robots AI-bot rules → security.txt → agent.json → PDP schema verify → citeability content (fruit-leather revival pending client confirmation) — derived from HELD instrument + LIKELY press
- Competitor GEO bench not run for any rival — GAP; named data-pass route `geo-competitive-bench` ($0 script re-run across 5–11 rival domains)
