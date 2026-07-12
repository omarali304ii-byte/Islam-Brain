# 10 — Design Principles

> **System:** Dashboard Intelligence Operating System (DIOS)  
> **Repository:** `omarali304ii-byte/Islam-Brain`  
> **Repository baseline:** `44cea987cd42f077cc0f6e448bcdc69f2683ecb1`  
> **DIOS working branch:** `docs/dios-phase-0-inventory`  
> **Principles date:** 2026-07-12  
> **Phase status:** Phase 10 — Complete, awaiting validation  
> **Previous artifacts:** [`00_Project_Inventory.md`](./00_Project_Inventory.md) · [`01_Understanding.md`](./01_Understanding.md) · [`02_Dashboard_Architecture.md`](./02_Dashboard_Architecture.md) · [`03_Design_System.md`](./03_Design_System.md) · [`04_System_Architecture.md`](./04_System_Architecture.md) · [`05_Prompt_Analysis.md`](./05_Prompt_Analysis.md) · [`06_Project_Decisions.md`](./06_Project_Decisions.md) · [`07_Project_Brain.md`](./07_Project_Brain.md) · [`08_Gap_Report.md`](./08_Gap_Report.md) · [`09_Learning_Guide.md`](./09_Learning_Guide.md)  
> **Next phase:** Phase 11 may proceed only after this document passes its quality gate

---

## Table of Contents

1. [Phase Entry Decision](#1-phase-entry-decision)
2. [Purpose of the Principles](#2-purpose-of-the-principles)
3. [Principle Authority and Usage](#3-principle-authority-and-usage)
4. [Principle Format](#4-principle-format)
5. [Executive Principle Set](#5-executive-principle-set)
6. [Truth and Evidence Principles](#6-truth-and-evidence-principles)
7. [Decision and Product Principles](#7-decision-and-product-principles)
8. [Dashboard and Information-Architecture Principles](#8-dashboard-and-information-architecture-principles)
9. [Visual and Interaction Principles](#9-visual-and-interaction-principles)
10. [Data and Metric Principles](#10-data-and-metric-principles)
11. [System and Engineering Principles](#11-system-and-engineering-principles)
12. [AI and Prompt Principles](#12-ai-and-prompt-principles)
13. [Permission, Security, Privacy, and Rights Principles](#13-permission-security-privacy-and-rights-principles)
14. [Operations and Governance Principles](#14-operations-and-governance-principles)
15. [Principle Tensions and Resolution Rules](#15-principle-tensions-and-resolution-rules)
16. [Principle-to-Gap Traceability](#16-principle-to-gap-traceability)
17. [Principle Acceptance Checklist](#17-principle-acceptance-checklist)
18. [Anti-Principles](#18-anti-principles)
19. [Phase 10 Validation Gate](#19-phase-10-validation-gate)
20. [Glossary](#20-glossary)
21. [Document Control](#21-document-control)

---

## 1. Phase Entry Decision

The repository owner requested **Phase 11** while Phase 10 did not yet exist. DIOS forbids skipping phases.

The instruction is therefore interpreted as:

- **Phase 9 acceptance:** Accepted by owner with all documented learning-guide limitations.
- **Phase 10 authorization:** Authorized as the mandatory prerequisite to Phase 11.
- **Conditional Phase 11 authorization:** Phase 11 may be created only after Phase 10 passes its quality gate.
- **Forbidden work:** Do not redesign the dashboard, select canonical data, approve unresolved decisions, write production code, generate media, scrape, ingest private data, build, or deploy.

> [!IMPORTANT]
> These principles govern future design and implementation choices. They do not prove that any principle is currently implemented.

---

## 2. Purpose of the Principles

The principles provide durable rules for making future choices when the repository does not contain an exact answer.

They are designed to:

- Preserve evidence honesty.
- Keep the dashboard decision-oriented.
- Prevent implementation from hard-coding unresolved assumptions.
- Align React and Power BI behavior.
- Protect privacy, rights, permissions, and costs.
- Make future AI and human work predictable.
- Resolve tradeoffs consistently.

A principle is broader than a component specification and more stable than a particular technology.

Example:

- “Use React” is a technology decision.
- “Presentation systems consume one validated contract” is a design principle.

---

## 3. Principle Authority and Usage

### 3.1 Authority order

When a principle conflicts with an explicit approved decision, the approved decision governs unless it violates evidence, privacy, legal, or permission constraints.

```text
Law, rights, privacy, and explicit permission
→ Latest owner-approved decision
→ Truth and evidence principles
→ Product and user principles
→ System and engineering principles
→ Visual and implementation preferences
```

### 3.2 Principles do not invent missing decisions

A principle can identify the correct way to decide but cannot choose:

- React versus Power BI launch priority
- Canonical social generation
- Exact KPI formulas or targets
- Founder story or fruit-leather truth
- Creator licensing terms
- Client-data handling terms
- Production hosting

### 3.3 Deviation rule

A team may deviate from a principle only when the record includes:

- Principle ID
- Reason
- Owner and approver
- Evidence
- Expected benefit
- Risk and mitigation
- Scope and expiry
- Validation plan

---

## 4. Principle Format

Every principle includes:

| Field | Meaning |
|---|---|
| ID | Stable reference |
| Statement | Short governing rule |
| Rationale | Why the rule exists |
| Project application | What it means for Cielito 360 |
| Anti-pattern | Behavior the rule rejects |
| Tradeoff | Cost or limitation |
| Acceptance test | Observable proof of compliance |
| Status | Accepted doctrine, specified doctrine, or required doctrine |

---

## 5. Executive Principle Set

The complete system can be summarized in twelve executive principles:

1. **Truth before polish.**
2. **Decisions before dashboards.**
3. **Definitions before calculations.**
4. **Canonical contracts before implementation.**
5. **Missing data must remain visibly missing.**
6. **Evidence must travel with claims.**
7. **One question per chart.**
8. **Progressive disclosure over information dumping.**
9. **Real media and real rights before synthetic realism.**
10. **Permission before side effects.**
11. **Validation before publication or deployment.**
12. **Implementation proof before status claims.**

---

## 6. Truth and Evidence Principles

### DP-TRU-001 — Truth before polish

**Statement:** A less attractive truthful output is better than a polished unsupported output.

**Rationale:** Executive confidence can be damaged more by one misleading flagship claim than by several visible data gaps.

**Project application:** The `~190×` narrative must remain caveated or excluded until its aggregation is canonical.

**Anti-pattern:** Using the most dramatic available number because it improves the story.

**Tradeoff:** Some executive surfaces will look less complete.

**Acceptance test:** Every load-bearing claim has reproducible evidence, or an explicit caveat/gap state.

**Status:** Accepted doctrine.

---

### DP-TRU-002 — Evidence class must remain visible

**Statement:** Facts, derived values, interpretations, hypotheses, decisions, and unknowns must not be blended.

**Rationale:** Different evidence classes require different confidence and language.

**Project application:** Fruit leather remains a founder-gated hypothesis; a catalog row count is a repository fact; “repair, do not rebuild” is a strategic decision.

**Anti-pattern:** Presenting a strategic interpretation as a measured fact.

**Tradeoff:** Copy becomes more qualified.

**Acceptance test:** Claim metadata or surrounding language identifies its evidence class.

**Status:** Accepted doctrine.

---

### DP-TRU-003 — Claims trace backward

**Statement:** Every governed claim must trace to exact source generations and transformations.

**Rationale:** A source name without exact lineage is insufficient when multiple generations exist.

**Project application:** A social KPI must identify the post population, window, capture, transformation, and formula.

**Anti-pattern:** Linking a chart to a final report that repeats the same claim.

**Tradeoff:** Lineage metadata and tooling are required.

**Acceptance test:** A reviewer can reconstruct the value from versioned inputs.

**Status:** Required doctrine.

---

### DP-TRU-004 — Contradictions are data

**Statement:** Contradictions must be preserved until an authorized process resolves them.

**Rationale:** Silent reconciliation hides uncertainty and destroys auditability.

**Project application:** 120, 150, and 210 social populations remain visible until a canonical manifest selects a use-specific generation.

**Anti-pattern:** Choosing the newest or largest file without authority.

**Tradeoff:** Documentation remains messier.

**Acceptance test:** Conflicting values remain registered with status, source, and resolution owner.

**Status:** Accepted doctrine.

---

### DP-TRU-005 — Blocked does not mean absent

**Statement:** Failure to collect evidence cannot support a claim that the observed thing does not exist.

**Rationale:** Access failures, platform limits, and deferred routes are not negative evidence.

**Project application:** A failed competitor or review route cannot prove there are no reviews, ads, creators, or signals.

**Anti-pattern:** Showing zero after a blocked scrape.

**Tradeoff:** More results remain unresolved.

**Acceptance test:** Blocked routes use blocked/unknown states, not zero or none.

**Status:** Accepted doctrine.

---

### DP-TRU-006 — Snapshots are not trends

**Statement:** Point-in-time captures must never be described as change over time without comparable historical observations.

**Rationale:** Trend language implies temporal evidence.

**Project application:** Follower count, PageSpeed, catalog discount surface, and creator rank are snapshots unless multiple governed captures exist.

**Anti-pattern:** Saying “improved” from one current snapshot.

**Tradeoff:** Trend charts remain unavailable initially.

**Acceptance test:** Trend language requires at least two comparable time points and a consistent method.

**Status:** Required doctrine.

---

### DP-TRU-007 — Model output is derived evidence

**Statement:** AI or statistical classifications must retain engine, version, fallback, validation, and limitations.

**Rationale:** Models can produce false positives, drift, and domain mismatch.

**Project application:** Sentiment and purchase-intent outputs must disclose model/fallback engine and Cielito-specific validation.

**Anti-pattern:** Calling model sentiment “customer truth.”

**Tradeoff:** More metadata and manual review are needed.

**Acceptance test:** Governed outputs expose model provenance and quality gate status.

**Status:** Required doctrine.

---

### DP-TRU-008 — Freshness is part of truth

**Statement:** Volatile facts require capture dates, review periods, and stale states.

**Rationale:** A once-correct value can become misleading.

**Project application:** Prices, followers, availability, PageSpeed, and creator rankings require freshness metadata.

**Anti-pattern:** Displaying an old number with current wording.

**Tradeoff:** Refresh work and stale-state design are required.

**Acceptance test:** Every volatile metric has `captured_at`, freshness policy, and stale behavior.

**Status:** Required doctrine.

---

## 7. Decision and Product Principles

### DP-DEC-001 — Decisions before dashboards

**Statement:** Define the decisions a user must make before selecting pages, cards, or charts.

**Rationale:** Available data should not determine the product structure by itself.

**Project application:** The persistent sequence—WhatsApp, catalog/Arabic, creators, mobile, financial baseline—organizes the executive experience.

**Anti-pattern:** Creating a page for every dataset folder.

**Tradeoff:** Some collected data may not appear in the MVP.

**Acceptance test:** Every major surface names its user, decision, and expected action.

**Status:** Accepted doctrine.

---

### DP-DEC-002 — Recommendation is not approval

**Statement:** Recommendations, hypotheses, queued work, and accepted decisions must use distinct statuses.

**Rationale:** Strategy documents often sound authoritative even when stakeholder approval is missing.

**Project application:** Paid routes remain pending, fruit leather remains founder-gated, and the Noon route remains dropped.

**Anti-pattern:** Moving a recommendation into the roadmap as committed work.

**Tradeoff:** More decision administration is required.

**Acceptance test:** Binding work links to an approved decision record.

**Status:** Accepted doctrine.

---

### DP-DEC-003 — Decision age must be visible

**Statement:** Persistent decisions require version, owner, evidence date, and review trigger.

**Rationale:** A Decision Dock can preserve clarity or freeze stale strategy.

**Project application:** Executive decisions must be updated when client data, founder input, or campaign evidence changes.

**Anti-pattern:** Treating the first strategic narrative as permanent.

**Tradeoff:** Governance and review cadence are needed.

**Acceptance test:** Persistent decisions display or link to current version and review state.

**Status:** Required doctrine.

---

### DP-DEC-004 — Product scope must be explicit

**Statement:** MVP capabilities and exclusions must be approved before implementation.

**Rationale:** React and Power BI specifications contain different strengths and scopes.

**Project application:** Launch target, pages, access, editability, export, refresh, and evidence behavior must be selected.

**Anti-pattern:** Letting developers infer scope from all repository documents combined.

**Tradeoff:** Some desired features are deferred.

**Acceptance test:** An approved product brief defines users, pages, capabilities, exclusions, and acceptance criteria.

**Status:** Required doctrine.

---

### DP-DEC-005 — Client value precedes agency theater

**Statement:** The dashboard must prioritize Cielito decision usefulness over WOM showcase density.

**Rationale:** A pitch centerpiece can tempt the team to add impressive but low-value charts.

**Project application:** The ≥20-card target cannot override usefulness, confidence, and user comprehension.

**Anti-pattern:** Adding cards to reach a quota.

**Tradeoff:** The product may appear smaller in a sales demonstration.

**Acceptance test:** Every included card supports a named decision or evidence obligation.

**Status:** Required doctrine.

---

### DP-DEC-006 — Financial honesty is a product requirement

**Statement:** Financial metrics remain blank or RequiresData until governed client data and methodology exist.

**Rationale:** Public data cannot establish revenue, CAC, returns, or conversion.

**Project application:** Financial-impact areas must explain the required client route rather than show invented scenarios.

**Anti-pattern:** Using realistic dummy values in a client-facing dashboard.

**Tradeoff:** The executive story has an intentional financial gap.

**Acceptance test:** No financial number appears without source, method, permission, and confidence.

**Status:** Accepted doctrine.

---

## 8. Dashboard and Information-Architecture Principles

### DP-IA-001 — Verdict before detail

**Statement:** The experience begins with what matters, why, and what should be decided.

**Rationale:** Executives should not reconstruct the story from dozens of charts.

**Project application:** L0 Decision Dock and L1 executive story precede L2 diagnostics and L3 evidence.

**Anti-pattern:** Opening on a dense analytical grid.

**Tradeoff:** Summary language must be maintained carefully.

**Acceptance test:** A first-time executive can state the core diagnosis and next decisions in approximately 30 seconds.

**Status:** Specified doctrine.

---

### DP-IA-002 — Progressive disclosure over information dumping

**Statement:** Show the smallest useful answer first and reveal complexity on demand.

**Rationale:** Executives, marketers, analysts, and developers require different detail.

**Project application:** Cards lead to diagnostics and evidence rather than displaying all metadata at once.

**Anti-pattern:** Putting raw rows, confidence notes, formulas, and strategy copy in one card.

**Tradeoff:** Additional navigation and state logic are needed.

**Acceptance test:** Every deep detail has a discoverable path without overloading the summary.

**Status:** Specified doctrine.

---

### DP-IA-003 — Evidence within two interactions

**Statement:** Important claims must have a short, predictable path to sources and caveats.

**Rationale:** Trust collapses when evidence is technically present but practically inaccessible.

**Project application:** KPI → evidence drawer/room → exact source record.

**Anti-pattern:** Requiring users to search the repository manually.

**Tradeoff:** Evidence components and links require implementation effort.

**Acceptance test:** A reviewer reaches source, sample, window, formula, and confidence in no more than two deliberate interactions.

**Status:** Specified doctrine.

---

### DP-IA-004 — Stable orientation, current content

**Statement:** Navigation and semantic structure should remain stable while decisions and data remain versioned and current.

**Rationale:** Users need familiarity without stale content.

**Project application:** L0–L3 structure may remain stable; Decision Dock text and metrics must be reviewable.

**Anti-pattern:** Freezing strategy because the layout is persistent.

**Tradeoff:** Content governance and UI stability must be separated.

**Acceptance test:** Updating a decision does not require redesigning the entire navigation.

**Status:** Required doctrine.

---

### DP-IA-005 — Internal rigor, client-safe surface

**Statement:** Internal protocols and technical labels remain available underneath but are translated on client-facing surfaces.

**Rationale:** Evidence rigor should not create jargon-heavy client experiences.

**Project application:** ATLAS, MIDAS, internal grades, and era codes should not dominate client cards.

**Anti-pattern:** Exposing internal vocabulary because it exists in source files.

**Tradeoff:** A translation layer and evidence detail view are needed.

**Acceptance test:** Client copy is understandable while evidence retains exact internal provenance.

**Status:** Specified doctrine.

---

## 9. Visual and Interaction Principles

### DP-VIS-001 — One question per chart

**Statement:** Every chart must answer one primary business question.

**Rationale:** Multi-purpose charts obscure interpretation.

**Project application:** Language effectiveness, price distribution, creator performance, and availability need separate questions and views.

**Anti-pattern:** Combining every social metric into one chart.

**Tradeoff:** More focused charts may increase page count.

**Acceptance test:** The chart title can be written as a clear question or insight without “and.”

**Status:** Accepted doctrine.

---

### DP-VIS-002 — Titles state insight, not field names

**Statement:** Chart titles should communicate the observed pattern or decision context.

**Rationale:** Users should not interpret raw field labels before understanding relevance.

**Project application:** Prefer “Creator posts dominate high-view outliers” over “Views by ownership.”

**Anti-pattern:** Titles like “Metric 1 by Category.”

**Tradeoff:** Dynamic titles must remain accurate under filtering.

**Acceptance test:** Title and “So what?” remain true for the active filter context.

**Status:** Specified doctrine.

---

### DP-VIS-003 — Visual encoding must preserve comparison truth

**Statement:** Scale, aggregation, and color may clarify differences but must not distort them.

**Rationale:** Extreme owned-versus-earned gaps can create unreadable or deceptive charts.

**Project application:** Log or broken scales require labels and explanation; peak and median cannot share an unlabeled comparison.

**Anti-pattern:** Truncating axes to amplify a small difference.

**Tradeoff:** Honest charts may be less dramatic.

**Acceptance test:** A reviewer can identify scale, unit, aggregation, population, and caveat from the card.

**Status:** Accepted doctrine.

---

### DP-VIS-004 — Color communicates meaning

**Statement:** Color is assigned by semantic role rather than decoration.

**Rationale:** Repeated meaning improves comprehension and cross-target parity.

**Project application:** Owned grey, earned terracotta, positive green, negative red, RequiresData orange/dashed.

**Anti-pattern:** Giving each chart a random palette.

**Tradeoff:** Semantic collisions and accessibility must be managed.

**Acceptance test:** The same semantic state uses the same token and non-color cue across React, Power BI, and exports.

**Status:** Specified doctrine.

---

### DP-VIS-005 — Missing data is designed, not hidden

**Statement:** Missing, blocked, stale, unsupported, and not-applicable states require distinct visual treatment.

**Rationale:** Blank charts and zero values conceal meaning.

**Project application:** RequiresData cards identify route, owner, permission, cost, and decision impact.

**Anti-pattern:** Empty white space with no explanation.

**Tradeoff:** State-system complexity increases.

**Acceptance test:** Users can distinguish missing, zero, blocked, stale, and not applicable without reading source code.

**Status:** Accepted doctrine.

---

### DP-VIS-006 — Real media first

**Statement:** Use verified real product, creator, and founder media whenever the surface implies factual representation.

**Rationale:** Synthetic realism can accidentally create product, founder, manufacturing, or sustainability claims.

**Project application:** Synthetic founder and fruit-leather concepts remain labeled and gated.

**Anti-pattern:** Using generated shoes as if they are current catalog products.

**Tradeoff:** Real assets may be incomplete or require licensing.

**Acceptance test:** Every media asset has provenance, rights state, factual role, and synthetic label where applicable.

**Status:** Accepted doctrine.

---

### DP-VIS-007 — Accessibility is a definition-of-done condition

**Statement:** Accessibility is validated behavior, not an aesthetic intention.

**Rationale:** Contrast alone does not prove keyboard, screen-reader, chart, or focus usability.

**Project application:** Evidence interactions, charts, tables, modals, and Decision Dock require keyboard and assistive-technology validation.

**Anti-pattern:** Claiming accessibility because colors look readable.

**Tradeoff:** Design and testing scope increases.

**Acceptance test:** Approved accessibility criteria and automated/manual test evidence pass.

**Status:** Required doctrine.

---

### DP-VIS-008 — Arabic and RTL are structural

**Statement:** Arabic, English, mixed-direction content, and Egyptian context shape layout, content, testing, and components from the start.

**Rationale:** RTL cannot be added safely as a final mirror operation.

**Project application:** Handles, URLs, numbers, metric abbreviations, product names, and Arabic copy must coexist correctly.

**Anti-pattern:** Duplicating English screens and flipping flex direction.

**Tradeoff:** Component and QA effort increases.

**Acceptance test:** Approved RTL/mixed-direction tests pass across supported breakpoints and exports.

**Status:** Required doctrine.

---

### DP-VIS-009 — Responsive means task-preserving

**Statement:** Mobile adaptation must preserve the user’s task, not merely fit pixels.

**Rationale:** Dense charts and tables often need alternate patterns on small screens.

**Project application:** Decision Dock, post tables, evidence details, and chart comparisons require mobile-specific behavior.

**Anti-pattern:** Shrinking a desktop dashboard until text becomes unreadable.

**Tradeoff:** Responsive variants require design and development work.

**Acceptance test:** Core decisions and evidence remain usable on approved screen classes.

**Status:** Required doctrine.

---

### DP-VIS-010 — Provisional direction is not a token system

**Statement:** Creative direction may guide exploration but cannot become canonical implementation values without approval.

**Rationale:** Warm tan, cream, terracotta, and charcoal are directional, not confirmed exact tokens.

**Project application:** No invented hex values, fonts, spacing, shadows, radii, or motion rules.

**Anti-pattern:** Treating repeated mood-board language as approved design tokens.

**Tradeoff:** Implementation must wait for design approval or use explicitly temporary tokens.

**Acceptance test:** Production tokens have owner, version, source, accessibility validation, and cross-target mapping.

**Status:** Accepted doctrine.

---

## 10. Data and Metric Principles

### DP-DAT-001 — Define grain before measure

**Statement:** No metric is governed until the row grain and entity relationships are explicit.

**Rationale:** Product, variant, SKU, post, comment, creator, and source counts answer different questions.

**Project application:** Catalog measures remain blocked until product/variant/SKU relationships are defined.

**Anti-pattern:** Counting rows without stating what a row represents.

**Tradeoff:** Domain modeling precedes quick charting.

**Acceptance test:** Every analytical table has a one-row definition and uniqueness test.

**Status:** Required doctrine.

---

### DP-DAT-002 — Canonical inputs before governed outputs

**Statement:** Production metrics consume versioned canonical inputs, not whichever file is convenient.

**Rationale:** Multiple data generations create divergent results.

**Project application:** Social, voice, creator, catalog, and spend inputs require a manifest.

**Anti-pattern:** Selecting the most recent modification timestamp.

**Tradeoff:** Canonical-selection governance is required.

**Acceptance test:** Build input manifest records ID, version, checksum, grain, window, schema, and owner.

**Status:** Required doctrine.

---

### DP-DAT-003 — Definitions before calculations

**Statement:** Formula, population, filters, unit, target, and caveat are approved before a metric is implemented.

**Rationale:** A calculation can be reproducible and still answer the wrong question.

**Project application:** Owned ER, `~190×`, UGC velocity, hygiene, and discount discipline require metric contracts.

**Anti-pattern:** Implementing a label first and documenting the formula later.

**Tradeoff:** Metric delivery slows initially.

**Acceptance test:** Every governed metric exists in the metric registry before React or DAX implementation.

**Status:** Required doctrine.

---

### DP-DAT-004 — Missing is not zero

**Statement:** Unknown, unavailable, blocked, not applicable, and zero are separate states.

**Rationale:** Zero is a measured value; unknown is an evidence condition.

**Project application:** Revenue, CAC, conversion, returns, and demographic values cannot default to zero.

**Anti-pattern:** Numeric fallbacks such as `value || 0` for missing business data.

**Tradeoff:** Consumers must handle nullable/stateful data.

**Acceptance test:** Schema and UI preserve state reason independently from numeric value.

**Status:** Accepted doctrine.

---

### DP-DAT-005 — Raw data is immutable

**Statement:** Raw captures are preserved; cleaning and derivation create new versioned artifacts.

**Rationale:** Reproducibility and correction require original evidence.

**Project application:** Collection outputs must not be silently rewritten by analysis scripts.

**Anti-pattern:** Editing raw JSON to fix a category.

**Tradeoff:** Storage and version-management needs increase.

**Acceptance test:** Raw input checksum remains stable and transformations identify parents.

**Status:** Required doctrine.

---

### DP-DAT-006 — Transformations disclose loss

**Statement:** Deduplication, normalization, classification, filtering, and fallback rules must report what they changed or removed.

**Rationale:** Data cleaning can materially change the represented population.

**Project application:** Comment deduplication, sentiment fallback, option parsing, and normalized catalog type counts require before/after records.

**Anti-pattern:** Publishing normalized data without transformation counts.

**Tradeoff:** More audit metadata is required.

**Acceptance test:** Transformation report contains rule version, input/output counts, exceptions, and quality results.

**Status:** Required doctrine.

---

### DP-DAT-007 — Shared semantics across targets

**Statement:** React and Power BI use the same metric, source, state, confidence, and identity definitions.

**Rationale:** Two presentation systems must not create two truths.

**Project application:** Shared registry and parity tests govern both targets.

**Anti-pattern:** Reimplementing business logic independently in TypeScript and DAX.

**Tradeoff:** Cross-target coordination increases.

**Acceptance test:** Fixture-based parity tests produce equivalent governed outputs.

**Status:** Required doctrine.

---

## 11. System and Engineering Principles

### DP-ENG-001 — Presentation consumes one validated contract

**Statement:** React and Power BI must not consume heterogeneous research artifacts directly.

**Rationale:** Source files have conflicting schemas, generations, vocabulary, and assumptions.

**Project application:** `build_cielito_data.py` or an approved equivalent forms the trust boundary.

**Anti-pattern:** Importing `_intel/*.json` inside UI components.

**Tradeoff:** Compiler development becomes prerequisite work.

**Acceptance test:** Presentation builds depend only on versioned validated outputs and approved media.

**Status:** Specified doctrine.

---

### DP-ENG-002 — Fail closed on governed truth

**Statement:** Invalid sources, schemas, metrics, rights, permissions, or claims block governed output.

**Rationale:** Continuing with silent coercion creates polished corruption.

**Project application:** Unsupported finance, banned internal vocabulary, missing source IDs, invalid media, and unresolved canonical inputs must block affected output.

**Anti-pattern:** Logging validation errors but publishing anyway.

**Tradeoff:** Builds may fail frequently during early maturity.

**Acceptance test:** Negative fixtures prove each stop-ship rule blocks output.

**Status:** Specified doctrine.

---

### DP-ENG-003 — Deterministic builds

**Statement:** The same versioned inputs and configuration should produce the same governed output.

**Rationale:** Reproducibility is essential for audit and debugging.

**Project application:** Prompt/model-generated transformations must be versioned or isolated from deterministic compilation.

**Anti-pattern:** Depending on live external pages during frontend build.

**Tradeoff:** Live freshness requires a separate collection process.

**Acceptance test:** Repeated builds produce matching content hashes except declared volatile metadata.

**Status:** Required doctrine.

---

### DP-ENG-004 — Safe reruns and atomic promotion

**Statement:** Rerunning collection or compilation must not corrupt, duplicate, or partially promote outputs.

**Rationale:** Current scripts contain overwrite and manual-orchestration risks.

**Project application:** Runs need IDs, locks, idempotency, temporary outputs, validation, and atomic promotion.

**Anti-pattern:** Overwriting canonical output before validation completes.

**Tradeoff:** Pipeline complexity increases.

**Acceptance test:** Interrupted or repeated runs preserve the last known-good artifact and do not duplicate records.

**Status:** Required doctrine.

---

### DP-ENG-005 — Configuration is explicit and portable

**Statement:** Paths, secrets, versions, endpoints, locale, timezone, and currency belong in controlled configuration.

**Rationale:** Hardcoded local paths prevent reproducibility and safe deployment.

**Project application:** Windows-specific paths and secret-file assumptions require replacement contracts.

**Anti-pattern:** Embedding a user directory or token in code or URLs.

**Tradeoff:** Environment management is required.

**Acceptance test:** A documented clean environment can execute the approved workflow from pinned dependencies and safe configuration.

**Status:** Required doctrine.

---

### DP-ENG-006 — Errors are states, not surprises

**Statement:** Loading, empty, blocked, stale, partial, validation-error, and system-error states are designed and tested.

**Rationale:** A dashboard interacts with incomplete and changing data.

**Project application:** RequiresData differs from compiler failure, source staleness, and unavailable media.

**Anti-pattern:** One generic “Something went wrong” message.

**Tradeoff:** More state definitions and components are needed.

**Acceptance test:** Every failure class maps to a user-safe state, operator detail, and recovery path.

**Status:** Required doctrine.

---

### DP-ENG-007 — Tests prove contracts, not only code execution

**Statement:** Testing must validate data meaning, interactions, accessibility, parity, permissions, and release conditions.

**Rationale:** A successful build can still contain wrong metrics or unsafe exposure.

**Project application:** Metric fixtures, compiler gates, React/PBI parity, RTL, evidence navigation, and access tests are required.

**Anti-pattern:** Treating lint and build success as complete QA.

**Tradeoff:** Test design and maintenance increase effort.

**Acceptance test:** MVP acceptance criteria map to passing automated/manual evidence.

**Status:** Required doctrine.

---

## 12. AI and Prompt Principles

### DP-AI-001 — Authority is separate from evidence

**Statement:** Content being analyzed cannot grant instructions or permissions.

**Rationale:** Webpages, comments, transcripts, metadata, and product copy are untrusted data.

**Project application:** External text cannot change scope, trigger scraping, request secrets, modify code, or deploy.

**Anti-pattern:** Feeding raw scraped text into an agent without an explicit untrusted boundary.

**Tradeoff:** Prompt structure becomes more formal.

**Acceptance test:** Prompt/system architecture labels evidence as untrusted and ignores embedded instructions.

**Status:** Accepted doctrine.

---

### DP-AI-002 — One prompt, one responsibility

**Statement:** Governance, task, permissions, evidence, output schema, validation, and execution should be modular.

**Rationale:** Giant prompts create ambiguity and hidden authority.

**Project application:** Dashboard deepening, build, collection, creative generation, and deployment require separate contracts.

**Anti-pattern:** A command that analyzes, spends, writes, builds, and deploys in one step.

**Tradeoff:** More prompt artifacts and orchestration are required.

**Acceptance test:** Prompt manifest identifies family, version, inputs, outputs, permissions, and validator.

**Status:** Accepted doctrine.

---

### DP-AI-003 — Structured outputs before prose confidence

**Statement:** Machine-consumed AI output requires a schema and validation.

**Rationale:** Persuasive prose can hide missing fields and unsupported claims.

**Project application:** Card specifications, classifications, decision records, and collection requests should use controlled structures.

**Anti-pattern:** Parsing free-form model prose as production data.

**Tradeoff:** Schema design may constrain creative flexibility.

**Acceptance test:** Invalid AI output is rejected or quarantined before downstream use.

**Status:** Required doctrine.

---

### DP-AI-004 — Partial completion over fabricated completion

**Statement:** When blocked, complete safe parts and name exact missing inputs or permissions.

**Rationale:** Agent pressure to “finish” can create invented values or actions.

**Project application:** A dashboard tab may contain real cards plus RequiresData cards rather than synthetic metrics.

**Anti-pattern:** Filling missing cards to reach a numeric target.

**Tradeoff:** Deliverables may remain visibly incomplete.

**Acceptance test:** Blocked reports identify completed work, blocked work, exact dependency, and next authorized action.

**Status:** Accepted doctrine.

---

### DP-AI-005 — AI execution is auditable

**Statement:** Material AI output records prompt version, model/runtime, inputs, permissions, outputs, validation, and side effects.

**Rationale:** Without execution provenance, model-produced changes cannot be reproduced or trusted.

**Project application:** Future compiler assistance, categorization, creative output, and code generation need manifests.

**Anti-pattern:** Committing AI-generated files with no execution record.

**Tradeoff:** Additional logging and storage are required.

**Acceptance test:** Every governed AI artifact links to an execution record.

**Status:** Required doctrine.

---

## 13. Permission, Security, Privacy, and Rights Principles

### DP-SEC-001 — Permission before side effect

**Statement:** Reading, deriving, writing docs, writing code, collecting data, spending, ingesting private data, generating media, previewing, and deploying are separate authorities.

**Rationale:** A harmless-sounding task can hide expensive or irreversible effects.

**Project application:** `Mega Run`-style commands require decomposition.

**Anti-pattern:** Treating code-build permission as production-deploy approval.

**Tradeoff:** Work may require more approvals.

**Acceptance test:** Every side-effecting task includes an explicit permission envelope and approver.

**Status:** Accepted doctrine.

---

### DP-SEC-002 — Free does not mean permissionless

**Statement:** External collection requires scope, terms, privacy, retention, and rate consideration even at zero monetary cost.

**Rationale:** Legal, platform, reputational, and PII risks are independent of price.

**Project application:** F1–F3 remain deferred unless explicitly authorized.

**Anti-pattern:** Running public-page crawls automatically because they are free.

**Tradeoff:** Research speed may decrease.

**Acceptance test:** Every external route has target, purpose, data class, retention, permission, and retry policy.

**Status:** Accepted doctrine.

---

### DP-SEC-003 — Private data enters only through governance

**Statement:** Client data cannot be ingested before purpose, access, storage, encryption, retention, deletion, isolation, export, audit, and incident rules are approved.

**Rationale:** Financial and customer data create material contractual and privacy obligations.

**Project application:** Shopify, GA4, Meta Insights, orders, revenue, and returns remain blocked.

**Anti-pattern:** Uploading client exports to a convenient local folder or external model.

**Tradeoff:** Financial analysis is delayed.

**Acceptance test:** Approved policy and implemented controls pass security/privacy validation before ingestion.

**Status:** Accepted doctrine.

---

### DP-SEC-004 — Public data still deserves minimization

**Statement:** Public handles, comments, media, and URLs must be collected and exposed only when necessary.

**Rationale:** Public availability does not eliminate privacy expectations or deletion concerns.

**Project application:** Comment evidence and creator directories should minimize identity exposure.

**Anti-pattern:** Exporting all handles and verbatims because they are public.

**Tradeoff:** Some evidence richness is reduced.

**Acceptance test:** Each personal-data field has purpose, access, retention, and display rule.

**Status:** Required doctrine.

---

### DP-SEC-005 — Rights travel with media

**Statement:** Media requires provenance, permission basis, attribution, scope, duration, territory, modification, and revocation state.

**Rationale:** Public visibility is not a commercial reuse license.

**Project application:** Creator media and UGC templates remain blocked until rights workflow exists.

**Anti-pattern:** Downloading and embedding creator content without documented rights.

**Tradeoff:** Media availability may decrease.

**Acceptance test:** The build rejects media without an approved rights state for its intended surface.

**Status:** Required doctrine.

---

### DP-SEC-006 — Secrets never travel in content

**Statement:** Secrets must not appear in prompts, URLs, logs, source files, generated reports, or client exports.

**Rationale:** URL tokens and copied logs spread credentials beyond controlled storage.

**Project application:** Current token-in-query behavior must be replaced before new integrations.

**Anti-pattern:** Passing API tokens inside collection URLs.

**Tradeoff:** Secure secret management is required.

**Acceptance test:** Secret scanning, rotation, redaction, and runtime injection controls pass.

**Status:** Required doctrine.

---

## 14. Operations and Governance Principles

### DP-OPS-001 — Implementation proof governs status

**Statement:** Accepted, specified, queued, implemented, deployed, and validated remain separate lifecycle states.

**Rationale:** Documentation-rich projects can accidentally claim progress that has not occurred.

**Project application:** React and Power BI remain unconfirmed despite detailed specifications.

**Anti-pattern:** Calling a feature complete when only its prompt exists.

**Tradeoff:** Status reporting is less flattering but more reliable.

**Acceptance test:** Each status claim links to the required evidence type.

**Status:** Accepted doctrine.

---

### DP-OPS-002 — Closure includes propagation

**Statement:** A gap or decision is not fully resolved until all dependent artifacts and systems are updated.

**Rationale:** Metric and decision drift occurs when only one target changes.

**Project application:** Changing a formula requires registry, compiler, React, Power BI, Decision Dock, reports, Brain, and tests.

**Anti-pattern:** Closing a gap after editing one Markdown file.

**Tradeoff:** Change management becomes broader.

**Acceptance test:** Closure record lists downstream updates and validation.

**Status:** Accepted doctrine.

---

### DP-OPS-003 — Build and deployment are different gates

**Statement:** Code completion, preview release, and production release require separate validation and approval.

**Rationale:** Technical ability to deploy is not business authorization.

**Project application:** Future `/dashboard/cielito-360` deployment must record environment, commit, data/compiler versions, tests, approval, and rollback.

**Anti-pattern:** Auto-deploying production after a coding task.

**Tradeoff:** Release speed may decrease.

**Acceptance test:** Production deploy cannot occur with only code-write or preview approval.

**Status:** Accepted doctrine.

---

### DP-OPS-004 — Last known good is preserved

**Statement:** Canonical data, compiled artifacts, and deployments require rollback targets.

**Rationale:** New data or code can be structurally valid but semantically harmful.

**Project application:** Compiler promotion and dashboard deployment must retain previous-good versions.

**Anti-pattern:** Overwriting the only dashboard contract.

**Tradeoff:** Storage and release management increase.

**Acceptance test:** Rollback is documented and tested.

**Status:** Required doctrine.

---

### DP-OPS-005 — Handoffs eliminate rediscovery

**Statement:** Every handoff names exact state, evidence, decisions, permissions, files, blockers, validation, and next action.

**Rationale:** Vague handoffs waste tokens and recreate mistakes.

**Project application:** The Project Brain and structured handoff contract are mandatory entry/exit points.

**Anti-pattern:** “Continue from where I stopped.”

**Tradeoff:** Contributors spend time documenting state.

**Acceptance test:** A new agent can begin the bounded next task without rescanning the full repository.

**Status:** Accepted doctrine.

---

### DP-OPS-006 — Observability includes data truth

**Statement:** Monitor data freshness, validation, lineage, and metric drift in addition to application uptime.

**Rationale:** A dashboard can be online while its data is stale or wrong.

**Project application:** Future operations must track compiler status, source age, missing routes, parity, and stale decisions.

**Anti-pattern:** Reporting 99.9% uptime as complete dashboard health.

**Tradeoff:** More operational signals and alerts are required.

**Acceptance test:** Health reporting includes app, build, data, evidence, and permission state.

**Status:** Required doctrine.

---

## 15. Principle Tensions and Resolution Rules

### 15.1 Executive simplicity versus evidence completeness

**Tension:** Executives need speed; evidence requires nuance.

**Resolution:** Use progressive disclosure. Keep source, sample, window, and confidence visible at card level while moving detailed lineage into Evidence Room.

### 15.2 Real media versus rights minimization

**Tension:** Real media improves credibility; rights may be unavailable.

**Resolution:** Use real media only with approved rights. Otherwise use labeled concepts that do not imply factual representation, or no media.

### 15.3 Fail-closed versus partial delivery

**Tension:** Strict validation can block useful work.

**Resolution:** Fail closed for governed claims and unsafe side effects; allow partial output only through explicit RequiresData/blocked states.

### 15.4 Stable Decision Dock versus changing strategy

**Tension:** Persistent orientation can become stale.

**Resolution:** Keep the component stable but version its content and require review triggers.

### 15.5 React flexibility versus Power BI consistency

**Tension:** React enables custom experience; Power BI enables mature BI workflows.

**Resolution:** Share data and semantic contracts. Allow target-specific interactions while preserving metric, evidence, state, and color meaning.

### 15.6 Dashboard richness versus cognitive load

**Tension:** The estate contains many analyses; users cannot process all at once.

**Resolution:** Use decision value, evidence quality, and user task—not card count—to prioritize inclusion.

### 15.7 Freshness versus collection cost

**Tension:** Current data is valuable; repeated collection costs money and privacy risk.

**Resolution:** Define freshness by decision need. Refresh only approved evidence classes at justified cadence.

### 15.8 Arabic-first versus bilingual reach

**Tension:** Masri-first supports local relevance; English may support brand or stakeholder needs.

**Resolution:** Define channel and surface rules rather than universal translation percentages; test meaning, not literal language mirroring.

---

## 16. Principle-to-Gap Traceability

| Principle group | Main gaps governed |
|---|---|
| Truth and evidence | `GAP-EVD-*`, `GAP-DAT-004` to `009`, `GAP-MET-001` |
| Decision and product | `GAP-BIZ-*`, `GAP-GOV-*`, `GAP-PRD-*` |
| IA and visual | `GAP-PRD-*`, `GAP-DES-*` |
| Data and metrics | `GAP-DAT-*`, `GAP-MET-*`, `GAP-ANA-*` |
| System and engineering | `GAP-ENG-*`, `GAP-OPS-003`, `GAP-OPS-004` |
| AI and prompts | Prompt-debt register, `GAP-OPS-001`, `GAP-OPS-002` |
| Security and rights | `GAP-SEC-*`, `GAP-CNV-003`, founder/creator gaps |
| Operations and governance | `GAP-GOV-*`, `GAP-OPS-*` |

### 16.1 Stop-ship principle mapping

| Stop-ship gap | Governing principles |
|---|---|
| Canonical dataset manifest | DP-TRU-003, DP-DAT-002 |
| `~190×` conflict | DP-TRU-001, DP-DAT-003, DP-VIS-003 |
| Product/SKU grain | DP-DAT-001 |
| Missing compiler | DP-ENG-001, DP-ENG-002 |
| Missing metric registry | DP-DAT-003, DP-DAT-007 |
| MVP/target unresolved | DP-DEC-004 |
| Acceptance criteria absent | DP-ENG-007, DP-VIS-007 |
| Ownership absent | DP-DEC-003, DP-OPS-002 |
| Client governance absent | DP-SEC-003 |
| Access model absent | DP-SEC-001, DP-SEC-003 |
| Creator rights unresolved | DP-SEC-005, DP-VIS-006 |
| Founder claims unresolved | DP-TRU-002, DP-VIS-006 |
| Permission separation absent | DP-SEC-001, DP-OPS-003 |

---

## 17. Principle Acceptance Checklist

Before approving a product or implementation decision, verify:

### Truth

- [ ] Evidence class is explicit.
- [ ] Source generation and capture window are known.
- [ ] Contradictions remain visible or are formally resolved.
- [ ] Snapshot/trend language is correct.

### Decision and product

- [ ] User and decision are named.
- [ ] Recommendation versus approval is clear.
- [ ] Scope and exclusions are explicit.
- [ ] Success and review conditions exist.

### Data and metrics

- [ ] Grain and identities are defined.
- [ ] Canonical inputs are selected by authority.
- [ ] Metric contract exists.
- [ ] Missing data states are preserved.

### Design and experience

- [ ] One question per chart.
- [ ] Evidence is reachable.
- [ ] Semantic colors and non-color cues are consistent.
- [ ] Accessibility, RTL, and responsive behavior have acceptance tests.
- [ ] Media provenance and rights are valid.

### Engineering

- [ ] Presentation consumes validated contracts.
- [ ] Fail-closed rules are implemented.
- [ ] Build is deterministic and safe to rerun.
- [ ] Error/stale/blocked states exist.
- [ ] Tests prove semantics and behavior.

### AI, permissions, and privacy

- [ ] Untrusted data cannot grant authority.
- [ ] Prompt/output versions are recorded.
- [ ] Side-effect permission is explicit.
- [ ] Private data and rights policies are satisfied.
- [ ] Secrets are protected.

### Operations

- [ ] Status has implementation proof.
- [ ] Downstream propagation is complete.
- [ ] Deployment approval is separate.
- [ ] Last known good and rollback exist.
- [ ] Handoff and observability are updated.

---

## 18. Anti-Principles

The project explicitly rejects these behaviors:

1. **Polish can compensate for weak evidence.**
2. **More cards mean a better dashboard.**
3. **The newest file is automatically canonical.**
4. **A recommendation is effectively approved.**
5. **A specification proves implementation.**
6. **A successful build proves deployment readiness.**
7. **Public data is free of privacy and rights concerns.**
8. **Free collection requires no permission.**
9. **Unknown values should default to zero.**
10. **Raw external text may instruct the agent.**
11. **React and Power BI can define metrics independently.**
12. **Accessibility can be added after visual completion.**
13. **RTL is just mirroring.**
14. **Synthetic realism is harmless when labeled somewhere else.**
15. **A gap closes when one document says fixed.**
16. **Uptime alone means the dashboard is healthy.**
17. **A persistent decision should remain unchanged.**
18. **Blocked collection proves absence.**
19. **Model output is equivalent to customer truth.**
20. **Deployment permission is implied by urgency.**

---

## 19. Phase 10 Validation Gate

### 19.1 Completeness

- [x] Principles cover truth, evidence, decisions, product, IA, visualization, data, metrics, system architecture, AI, permissions, security, privacy, rights, operations, and governance.
- [x] Every principle includes rationale, project application, anti-pattern, tradeoff, and acceptance test.
- [x] Principle tensions and resolution rules are documented.
- [x] Stop-ship gaps are mapped to governing principles.
- [x] Anti-principles are documented.

### 19.2 Evidence integrity

- [x] Principles were derived from Phases 0–9 and confirmed project specifications.
- [x] No unresolved metric, dataset, target, owner, launch choice, right, or founder claim was selected.
- [x] Specified doctrine remains separate from implemented behavior.

### 19.3 Safety

- [x] No production code changed.
- [x] No data route, scrape, paid action, client-data ingestion, media generation, build, or deployment occurred.
- [x] No permission or stakeholder approval was invented.

### 19.4 Quality result

**Phase 10 result:** PASS — GOVERNING DESIGN PRINCIPLES ESTABLISHED.

The principles are sufficiently complete to support Phase 11 best-practice procedures without skipping the required conceptual layer.

### 19.5 Phase transition

The owner’s Phase 11 request becomes actionable because Phase 10 has now passed its quality gate.

---

## 20. Glossary

| Term | Meaning |
|---|---|
| Design principle | Durable rule used to guide choices across technologies and deliverables |
| Anti-principle | Explicitly rejected behavior or belief |
| Doctrine | Governing project rule; may be accepted, specified, or required |
| Acceptance test | Observable evidence that a principle was applied |
| Deviation record | Approved explanation for temporarily or intentionally violating a principle |
| Principle tension | Situation where two valid principles compete |
| Semantic parity | Equivalent meaning across React, Power BI, exports, and documentation |
| Governed output | Output that passed required evidence, metric, permission, and validation rules |

---

## 21. Document Control

| Field | Value |
|---|---|
| Document | `docs/DIOS/10_Design_Principles.md` |
| Phase | 10 |
| Created | 2026-07-12 |
| Authoring system | DIOS analysis through connected GitHub workflow |
| Repository | `omarali304ii-byte/Islam-Brain` |
| Working branch | `docs/dios-phase-0-inventory` |
| Governing principles | 48 |
| Production code changed | No |
| External actions executed | No |
| Next phase | `11_Best_Practices.md`, authorized by owner request |
