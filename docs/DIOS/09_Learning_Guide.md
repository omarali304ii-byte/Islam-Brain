# 09 — Learning Guide

> **System:** Dashboard Intelligence Operating System (DIOS)  
> **Repository:** `omarali304ii-byte/Islam-Brain`  
> **Repository baseline:** `44cea987cd42f077cc0f6e448bcdc69f2683ecb1`  
> **DIOS working branch:** `docs/dios-phase-0-inventory`  
> **Learning-guide date:** 2026-07-12  
> **Phase status:** Phase 9 — Complete, awaiting validation  
> **Previous artifacts:** [`00_Project_Inventory.md`](./00_Project_Inventory.md) · [`01_Understanding.md`](./01_Understanding.md) · [`02_Dashboard_Architecture.md`](./02_Dashboard_Architecture.md) · [`03_Design_System.md`](./03_Design_System.md) · [`04_System_Architecture.md`](./04_System_Architecture.md) · [`05_Prompt_Analysis.md`](./05_Prompt_Analysis.md) · [`06_Project_Decisions.md`](./06_Project_Decisions.md) · [`07_Project_Brain.md`](./07_Project_Brain.md) · [`08_Gap_Report.md`](./08_Gap_Report.md)  
> **Next phase:** Blocked until this document passes its quality gate

---

## Table of Contents

1. [Phase Entry Decision](#1-phase-entry-decision)
2. [Learning Mode Contract](#2-learning-mode-contract)
3. [How to Use This Guide](#3-how-to-use-this-guide)
4. [Curriculum Map](#4-curriculum-map)
5. [The Project in Plain Language](#5-the-project-in-plain-language)
6. [Dashboard, Report, BI, and Command Center](#6-dashboard-report-bi-and-command-center)
7. [Decision Intelligence](#7-decision-intelligence)
8. [Users, Decisions, and Jobs to Be Done](#8-users-decisions-and-jobs-to-be-done)
9. [Current State Versus Intended State](#9-current-state-versus-intended-state)
10. [Evidence Classes and Truth Precedence](#10-evidence-classes-and-truth-precedence)
11. [Provenance, Source Registry, and Lineage](#11-provenance-source-registry-and-lineage)
12. [Data Grain, Entities, Keys, and Relationships](#12-data-grain-entities-keys-and-relationships)
13. [Canonical Data, Schemas, and Versioning](#13-canonical-data-schemas-and-versioning)
14. [Metrics, KPIs, Measures, Dimensions, and Targets](#14-metrics-kpis-measures-dimensions-and-targets)
15. [Sample Size, Capture Window, Confidence, and Freshness](#15-sample-size-capture-window-confidence-and-freshness)
16. [Missing Data and RequiresData States](#16-missing-data-and-requiresdata-states)
17. [Normalization, Deduplication, and Transformation](#17-normalization-deduplication-and-transformation)
18. [Star Schemas and Analytical Models](#18-star-schemas-and-analytical-models)
19. [Decision-First Information Architecture](#19-decision-first-information-architecture)
20. [Charts and Visual Encoding](#20-charts-and-visual-encoding)
21. [Design Systems and Semantic Tokens](#21-design-systems-and-semantic-tokens)
22. [Filters, State, and Interaction Design](#22-filters-state-and-interaction-design)
23. [Accessibility, RTL, and Responsive Design](#23-accessibility-rtl-and-responsive-design)
24. [Data Pipelines, Compilers, and Data Contracts](#24-data-pipelines-compilers-and-data-contracts)
25. [Fail-Closed Validation](#25-fail-closed-validation)
26. [React Dashboard Fundamentals](#26-react-dashboard-fundamentals)
27. [Power BI Fundamentals](#27-power-bi-fundamentals)
28. [Testing and Quality Assurance](#28-testing-and-quality-assurance)
29. [Deployment, Observability, and Operations](#29-deployment-observability-and-operations)
30. [Prompt Engineering and Untrusted Data](#30-prompt-engineering-and-untrusted-data)
31. [Permissions and Side Effects](#31-permissions-and-side-effects)
32. [Security, Privacy, PII, and Media Rights](#32-security-privacy-pii-and-media-rights)
33. [Decisions, Gaps, Risks, and Readiness](#33-decisions-gaps-risks-and-readiness)
34. [Project Case Studies](#34-project-case-studies)
35. [Role-Based Learning Paths](#35-role-based-learning-paths)
36. [Practical Exercises](#36-practical-exercises)
37. [Exercise Answer Guide](#37-exercise-answer-guide)
38. [Professional Terminology Reference](#38-professional-terminology-reference)
39. [Learning Resources](#39-learning-resources)
40. [Mastery Checklist](#40-mastery-checklist)
41. [Phase 9 Validation Gate](#41-phase-9-validation-gate)
42. [Glossary](#42-glossary)
43. [Document Control](#43-document-control)

---

## 1. Phase Entry Decision

Phase 8 was complete but awaiting owner validation. On 2026-07-12, the repository owner explicitly instructed the system to proceed with **Phase 9**.

This is recorded as:

- **Phase 8 acceptance:** Accepted by owner with all documented stop-ship gaps, readiness limitations, and closure conditions.
- **Authorized work:** Explain the project and the professional concepts required to understand, govern, design, and eventually implement it.
- **Forbidden work:** Do not close gaps, choose canonical datasets, redefine metrics, build software, deploy, execute data routes, ingest client data, generate creative media, or grant approvals.
- **Audience assumption:** The reader may have limited dashboard, analytics, data-modeling, design-system, architecture, or AI-governance knowledge.

> [!IMPORTANT]
> This phase teaches concepts. It does not convert recommended practices into implemented controls or resolve any open project decision.

---

## 2. Learning Mode Contract

Every major concept in this guide explains:

1. **Definition** — what the concept means.
2. **Purpose** — why professionals use it.
3. **Advantages** — what improves when it is applied well.
4. **Disadvantages or tradeoffs** — what it costs or complicates.
5. **Real-world example** — how it appears in practice.
6. **Cielito project example** — how it applies here.
7. **Best practices** — the professional way to use it.
8. **Common mistakes** — how teams misuse it.
9. **Learning resources** — where to continue learning inside this repository.
10. **Professional terminology** — words a product, data, design, engineering, or analytics team would use.

### 2.1 Project-specific rule

No concept is taught as isolated theory. Every explanation returns to the Cielito 360 estate and answers:

- What does this concept explain about the current repository?
- Which project risk does it prevent?
- Which project artifact demonstrates it?
- Which gap must close before it can be implemented safely?

### 2.2 Learning outcome

After completing this guide, a reader should be able to:

- Explain what the project is and is not.
- Distinguish evidence, interpretation, hypothesis, decision, specification, implementation, and deployment.
- Trace an executive claim back to raw evidence.
- Identify unsafe metrics and data-model assumptions.
- Understand the dashboard architecture and design philosophy.
- Explain why the compiler is the central technical boundary.
- Recognize privacy, rights, permission, and prompt-injection risks.
- Use the Project Brain, Decision Ledger, and Gap Report correctly.
- Join the project without rescanning the entire repository.

---

## 3. How to Use This Guide

### 3.1 First-time reader

Read in this order:

1. Sections 5–9 for the project mental model.
2. Sections 10–18 for evidence, data, and metrics.
3. Sections 19–23 for dashboard product and design.
4. Sections 24–29 for engineering and operations.
5. Sections 30–33 for AI, permissions, privacy, decisions, and gaps.
6. Section 34 for project case studies.
7. Section 35 for your role-specific path.
8. Sections 36–40 for practice and validation.

### 3.2 Returning contributor

Use the guide as a concept reference, then use [`07_Project_Brain.md`](./07_Project_Brain.md) as the current project router.

### 3.3 Important distinction

This guide explains **why** a practice matters. The specialist DIOS documents describe **what the project currently says**. Raw and derived source files provide **evidence**. Future implementation will show **whether the practice was actually applied**.

---

## 4. Curriculum Map

| Learning block | Questions answered | Primary DIOS sources |
|---|---|---|
| Project mental model | What is being built and why? | Phases 1, 2, 7 |
| Evidence literacy | What is true, derived, interpreted, or unknown? | Phases 0, 1, 7 |
| Data literacy | What is a grain, schema, canonical dataset, metric, or dimension? | Phases 2, 4, 8 |
| Dashboard literacy | How should users move from verdict to evidence? | Phases 2, 3 |
| Engineering literacy | Why are compiler, validation, tests, and deployment separate? | Phases 4, 8 |
| AI governance | How should prompts, permissions, and untrusted data be controlled? | Phase 5 |
| Decision governance | What has been chosen, blocked, deferred, or dropped? | Phase 6 |
| Readiness literacy | What blocks implementation and what proves closure? | Phase 8 |

---

## 5. The Project in Plain Language

### Definition

The repository is a **research-and-dashboard estate** for Cielito Egypt. It contains collected evidence, derived analysis, strategic conclusions, dashboard specifications, media, and client-facing documents.

### Purpose

Its purpose is to help Cielito and WOM understand the business, decide what to fix, and eventually present that intelligence through an evidence-linked dashboard.

### Advantages

- Preserves a large amount of business evidence.
- Connects social, catalog, website, customer-language, and strategic analysis.
- Makes uncertainty and missing data visible.
- Provides a detailed blueprint for future React and Power BI products.

### Disadvantages and tradeoffs

- The repository can look more complete than it is because specifications and polished reports are abundant.
- Truth is spread across many files.
- Several data generations and metric definitions conflict.
- There is no confirmed running dashboard.

### Real-world example

A consultancy may deliver research, data extracts, analysis notebooks, and a proposed executive dashboard before the software product is implemented. The deliverables can be valuable while still being different from a production application.

### Cielito project example

The evidence and decision-intelligence systems exist as files. The React dashboard, Power BI file, compiler, database, backend, CI/CD, and deployment are not confirmed.

### Best practices

- Describe the estate as research and specifications until implementation proof exists.
- Use the Project Brain as the front door.
- Use raw evidence and specialist artifacts to verify claims.
- Keep “specified,” “implemented,” “deployed,” and “validated” separate.

### Common mistakes

- Calling a specification “the dashboard.”
- Assuming a route mentioned in a document is deployed.
- Treating a final report as proof of its own claims.
- Starting UI coding before canonical data and metrics are defined.

### Learning resources

- [`01_Understanding.md`](./01_Understanding.md)
- [`04_System_Architecture.md`](./04_System_Architecture.md)
- [`07_Project_Brain.md`](./07_Project_Brain.md)

### Professional terminology

- Evidence estate
- Decision-intelligence layer
- Dashboard blueprint
- Current state
- Target state
- Implementation proof
- Production readiness

---

## 6. Dashboard, Report, BI, and Command Center

### Definition

- A **report** presents information, often as a fixed document or page.
- A **dashboard** presents monitored metrics and interactive analysis.
- **Business intelligence (BI)** is the broader practice of converting data into analysis and decisions.
- A **command center** combines monitoring, diagnosis, decisions, actions, and evidence.

### Purpose

The distinction helps define user expectations and product scope.

### Advantages

A command-center model can:

- Keep priority decisions visible.
- Connect metrics to actions.
- Support both executive and specialist users.
- Provide traceable evidence.

### Disadvantages and tradeoffs

- It is more complex than a report.
- It requires stronger information architecture.
- It can become overloaded if every analysis is placed on the same surface.
- It needs clear ownership so decisions do not become stale.

### Real-world example

A monthly PDF is a report. A Power BI page with filters is a dashboard. A product that keeps a verdict, actions, alerts, drill-downs, and evidence together behaves more like a command center.

### Cielito project example

The intended product is not merely a chart collection. It uses:

- L0 persistent Decision Dock
- L1 five-screen executive story
- L2 diagnostic rooms
- L3 Evidence Room

The journey is:

```text
Verdict → Why → Decision → Diagnosis → Evidence
```

### Best practices

- Define whether the initial product is report, dashboard, or command center.
- Keep the executive path short.
- Separate monitoring from deep diagnosis.
- Make evidence available without forcing every user to read raw data.

### Common mistakes

- Calling any page with charts a dashboard.
- Opening with dozens of metrics and no story.
- Creating interactions that do not support a decision.
- Treating the dashboard as a substitute for operational ownership.

### Learning resources

- [`02_Dashboard_Architecture.md`](./02_Dashboard_Architecture.md)
- `dashboard/react_dashboard_spec.md`
- `dashboard/powerbi_spec.md`

### Professional terminology

- Executive dashboard
- Analytical dashboard
- Operational dashboard
- Command center
- Drill-down
- Progressive disclosure
- Information hierarchy

---

## 7. Decision Intelligence

### Definition

Decision intelligence is the discipline of connecting evidence, analysis, choices, actions, and monitoring.

### Purpose

It prevents analytics from ending at “interesting insight” and asks what decision the insight should support.

### Advantages

- Reduces chart-for-chart’s-sake work.
- Makes analysis more actionable.
- Clarifies ownership and consequences.
- Supports review when evidence changes.

### Disadvantages and tradeoffs

- Requires decision owners.
- Requires explicit assumptions and alternatives.
- Can expose that the organization has data but no authority to act.
- Decisions can become stale if not reviewed.

### Real-world example

A retailer learns that mobile checkout is slow. Decision intelligence does not stop at the performance score; it defines whether paid acquisition should be delayed, who owns remediation, what target must be reached, and how results will be monitored.

### Cielito project example

The accepted sequence is:

1. Install the WhatsApp conversion bridge.
2. Clean the catalog and use Arabic-first owned content.
3. Formalize the creator engine.
4. Improve mobile performance before scaling paid acquisition.
5. Use client data for financial baselines.

The dashboard should operationalize this sequence rather than merely display social and catalog metrics.

### Best practices

- Give every major chart a decision question.
- Record owner, rationale, evidence, alternatives, dependencies, and review condition.
- Separate accepted decisions from implementation proof.
- Update the Decision Dock when decisions change.

### Common mistakes

- Treating recommendations as approved decisions.
- Treating accepted decisions as implemented.
- Keeping old decisions visible after evidence changes.
- Measuring activity instead of decision outcomes.

### Learning resources

- [`06_Project_Decisions.md`](./06_Project_Decisions.md)
- `final/DECISION_DOCK.md`
- [`08_Gap_Report.md`](./08_Gap_Report.md)

### Professional terminology

- Decision record
- Decision owner
- Approver
- Tradeoff
- Reopen condition
- Supersession
- Monitoring covenant

---

## 8. Users, Decisions, and Jobs to Be Done

### Definition

A user is not only a demographic or job title. In product design, a user is understood by the decisions and tasks they need to complete.

### Purpose

User-centered dashboard design ensures that information is organized around real work rather than the available columns in a dataset.

### Advantages

- Makes page structure easier to justify.
- Reduces irrelevant metrics.
- Improves prioritization.
- Creates clearer acceptance criteria.

### Disadvantages and tradeoffs

- Different users may want conflicting levels of detail.
- Executive simplicity can hide analyst nuance.
- Analyst rigor can overload executive surfaces.

### Real-world example

A CEO needs a verdict and decision sequence. An analyst needs source definitions and row-level evidence. A marketer needs content and creator diagnostics.

### Cielito project example

- **Executive:** What is happening, why, what should be decided, and what should be watched?
- **Marketer:** Which posts, languages, formats, creators, and themes work?
- **Analyst:** What is the source, sample, formula, and confidence?
- **Developer:** What contract, state, and validation rule must be implemented?

### Best practices

- Define each user’s decisions before defining pages.
- Give each dashboard level a primary user.
- Avoid making every surface satisfy every user.
- Test whether a user can answer their key question without reading the whole estate.

### Common mistakes

- Designing around organizational departments rather than decisions.
- Assuming executives want fewer facts instead of better hierarchy.
- Hiding important caveats from executives.
- Giving analysts only screenshots instead of source access.

### Learning resources

- [`01_Understanding.md`](./01_Understanding.md), target-user sections
- [`02_Dashboard_Architecture.md`](./02_Dashboard_Architecture.md)

### Professional terminology

- Persona
- User role
- Job to be done
- Decision journey
- Primary user
- Secondary user
- User story

---

## 9. Current State Versus Intended State

### Definition

- **Current state** describes what exists now.
- **Intended state** describes what is planned or specified.

### Purpose

Separating the two prevents plans from being mistaken for implementation.

### Advantages

- Produces honest roadmaps.
- Makes technical debt visible.
- Prevents false deployment claims.
- Supports realistic estimation.

### Disadvantages and tradeoffs

- The current-state description may look less impressive.
- Stakeholders may prefer a cleaner story than the evidence permits.
- Maintaining both views requires discipline.

### Real-world example

A system diagram showing a database, API, and dashboard may be a target architecture. If the repository currently contains CSV files and scripts, both diagrams are needed.

### Cielito project example

**Current:** local scripts, JSON/Markdown/YAML/HTML/TXT/JPG files, manual orchestration, no confirmed app.

**Intended:** fail-closed compiler, versioned dashboard contract, React dashboard, Power BI report, validation, deployment, and evidence interactions.

### Best practices

- Label diagrams “current” or “target.”
- Require implementation proof before changing status.
- Track “accepted,” “specified,” “queued,” “implemented,” “deployed,” and “validated” separately.
- Preserve missing systems in the Gap Report.

### Common mistakes

- Using future-state diagrams in status reports without labels.
- Calling “buildable” equivalent to “built.”
- Assuming a generated file was produced because a compiler is specified.
- Assuming deployment because a target URL appears in a prompt.

### Learning resources

- [`04_System_Architecture.md`](./04_System_Architecture.md)
- [`07_Project_Brain.md`](./07_Project_Brain.md)

### Professional terminology

- As-is architecture
- To-be architecture
- Target state
- Implementation status
- Deployment status
- Architecture gap

---

## 10. Evidence Classes and Truth Precedence

### Definition

Evidence classes distinguish how a statement became known.

The project uses:

- Repository fact
- Captured fact
- Derived fact
- Declared state
- Interpretation
- Hypothesis
- Unknown

### Purpose

The classification prevents a conclusion, model output, or polished narrative from being treated as raw truth.

### Advantages

- Improves trust.
- Makes uncertainty explicit.
- Helps reviewers challenge claims.
- Supports safe AI reasoning.

### Disadvantages and tradeoffs

- Adds metadata and documentation work.
- Makes some executive statements more qualified.
- Requires reviewers to understand evidence levels.

### Real-world example

“Revenue increased 20%” can mean a directly measured database result, a spreadsheet calculation, a stakeholder statement, or a forecast. The words may look identical while the evidence quality differs.

### Cielito project example

- `catalog_full.json` containing 250 products is a repository fact about that file.
- “96 products are on sale” is a derived fact if calculated from that dataset.
- “Cielito has a broken owned engine” is an interpretation.
- “Fruit leather is a current differentiator” is a hypothesis until founder confirmation.
- “The React dashboard exists” remains unknown/unconfirmed.

### Best practices

- Label important claims with evidence class.
- Trace final narrative backward to raw evidence.
- Keep hypotheses visually and structurally separate.
- Let later explicit owner decisions supersede earlier recommendations, not raw facts.

### Common mistakes

- Treating a final report as primary evidence.
- Treating model sentiment as objective truth.
- Treating a declared workflow state as proof of implementation.
- Deleting contradictions to simplify the story.

### Learning resources

- [`01_Understanding.md`](./01_Understanding.md), facts and unknowns
- [`07_Project_Brain.md`](./07_Project_Brain.md), truth precedence
- `_intel/SOURCE_REGISTRY.md`

### Professional terminology

- Evidence class
- Primary evidence
- Secondary evidence
- Derived measure
- Interpretation
- Hypothesis
- Confidence
- Epistemic status

---

## 11. Provenance, Source Registry, and Lineage

### Definition

- **Provenance** explains where data or a claim came from.
- A **source registry** lists sources and their meaning or confidence.
- **Lineage** records how raw data became a metric, chart, report, or decision.

### Purpose

These practices make results reproducible, reviewable, and correctable.

### Advantages

- A reviewer can inspect the source behind a claim.
- Corrections can propagate to affected outputs.
- Data can be rebuilt from known inputs.
- Confidence can be displayed honestly.

### Disadvantages and tradeoffs

- Requires IDs, manifests, and transformation records.
- Lineage becomes complex across many artifacts.
- Manual lineage is expensive and easy to forget.

### Real-world example

A KPI card should not only say “38% discounted.” It should identify the catalog version, formula, capture date, denominator, and transformation.

### Cielito project example

The source registry exists, but there is no complete machine-readable claim-to-source graph. Final claims may reference source IDs, while transformation paths remain partly manual.

### Best practices

- Give every source, dataset, metric, and claim a stable ID.
- Store version, checksum, capture window, owner, and confidence.
- Record transformation steps.
- Update downstream artifacts when a source grade changes.

### Common mistakes

- Linking only to a final narrative.
- Using filenames as the only identity.
- Overwriting datasets without preserving run versions.
- Showing a source ID that does not identify the exact input generation.

### Learning resources

- `_intel/SOURCE_REGISTRY.md`
- [`04_System_Architecture.md`](./04_System_Architecture.md)
- [`08_Gap_Report.md`](./08_Gap_Report.md), evidence gaps

### Professional terminology

- Provenance
- Lineage
- Source registry
- Data catalog
- Manifest
- Checksum
- Audit trail
- Traceability

---

## 12. Data Grain, Entities, Keys, and Relationships

### Definition

- An **entity** is a thing the system represents, such as product, variant, post, creator, or source.
- **Grain** defines what one row represents.
- A **key** identifies an entity.
- A **relationship** connects entities.

### Purpose

Correct grain prevents incorrect joins, counts, averages, inventory measures, and prices.

### Advantages

- Metrics have clear denominators.
- Duplicates are easier to detect.
- React and Power BI can share definitions.
- Data can scale and refresh safely.

### Disadvantages and tradeoffs

- Modeling product variants is more complex than storing one product row.
- Multiple grains require multiple tables or nested structures.
- Stable external IDs may be unavailable.

### Real-world example

A shoe product may have one product identity, several color variants, and several size SKUs. Counting product rows as SKUs produces false availability and assortment metrics.

### Cielito project example

The Power BI specification says one row per SKU, while the confirmed catalog structure appears product-centered and may contain variants. `option1` includes values that are not always sizes. Product/SKU grain is therefore a P0 gap.

### Best practices

- Write a sentence for every table: “One row represents…”
- Separate product, variant, and SKU identities.
- Define keys and parent-child relationships.
- Validate uniqueness and referential integrity.
- Do not infer semantic meaning from a generic option field.

### Common mistakes

- Counting products and SKUs interchangeably.
- Assuming `option1` always means size.
- Joining posts to creators by display name alone.
- Using changing rank/index values as stable IDs.

### Learning resources

- [`04_System_Architecture.md`](./04_System_Architecture.md), domain and grain sections
- [`06_Project_Decisions.md`](./06_Project_Decisions.md), catalog decisions
- [`08_Gap_Report.md`](./08_Gap_Report.md), `GAP-DAT-002`

### Professional terminology

- Entity
- Grain
- Primary key
- Foreign key
- Natural key
- Surrogate key
- Cardinality
- Referential integrity
- Slowly changing dimension

---

## 13. Canonical Data, Schemas, and Versioning

### Definition

- **Canonical data** is the formally selected authoritative version.
- A **schema** defines structure, types, required fields, and constraints.
- **Versioning** records change over time.

### Purpose

These concepts ensure that the same inputs produce the same governed outputs.

### Advantages

- Prevents silent dataset switching.
- Makes builds reproducible.
- Enables safe migrations.
- Supports React/Power BI parity.

### Disadvantages and tradeoffs

- Selecting canonical data requires authority.
- Old datasets must be preserved or migrated.
- Schema evolution requires compatibility rules.

### Real-world example

If one analyst uses a 120-row social file and another uses a 210-post file, both can produce valid calculations for different populations. Without a canonical manifest, the dashboard cannot claim one official number.

### Cielito project example

Social volume is represented as initial captures, deeper captures, and a Power BI seed concept. Voice data appears as 254, 964, and 1,050 items. No canonical generation is confirmed.

### Best practices

- Create a versioned canonical manifest.
- Record dataset ID, path, checksum, grain, window, schema version, owner, and status.
- Never overwrite authoritative history silently.
- Add migration and compatibility tests.

### Common mistakes

- Choosing the newest file automatically.
- Choosing the largest dataset automatically.
- Treating file modification time as data freshness.
- Updating the React dataset but not Power BI.

### Learning resources

- [`08_Gap_Report.md`](./08_Gap_Report.md), canonical data gaps
- [`07_Project_Brain.md`](./07_Project_Brain.md), canonicality warnings
- [`04_System_Architecture.md`](./04_System_Architecture.md)

### Professional terminology

- Canonical dataset
- Schema registry
- Schema version
- Data contract
- Backward compatibility
- Migration
- Immutable snapshot
- Promotion workflow

---

## 14. Metrics, KPIs, Measures, Dimensions, and Targets

### Definition

- A **metric** is a quantified measure.
- A **KPI** is a metric chosen to monitor an important objective.
- A **measure** is a calculated value, especially in BI.
- A **dimension** is a category used to slice data, such as date, platform, or language.
- A **target** defines desired performance.

### Purpose

These definitions turn data into consistent monitoring and decision rules.

### Advantages

- Creates shared language across teams.
- Makes charts reproducible.
- Supports gauges and alerts.
- Enables React and Power BI parity.

### Disadvantages and tradeoffs

- KPIs can oversimplify behavior.
- Targets can encourage gaming.
- A metric can be mathematically correct but strategically misleading.

### Real-world example

“Engagement rate” is incomplete until the numerator, denominator, population, platform, and period are defined.

### Cielito project example

The proposed watch list includes owned engagement rate, owned-versus-earned performance, WhatsApp conversations, TikTok efficiency, mobile performance, catalog hygiene, UGC velocity, and discount discipline. Several formulas and targets remain undefined.

### Best practices

Every governed metric should define:

- Metric ID and name
- Business question
- Formula
- Grain
- Population and filters
- Numerator and denominator
- Unit
- Source
- Capture window
- Minimum sample
- Confidence rule
- Target and threshold
- Owner
- Caveat

### Common mistakes

- Using a label without a formula.
- Comparing a peak to a median without saying so.
- Mixing views, plays, reach, and impressions.
- Showing a gauge without an approved target.
- Treating missing values as zero.

### Learning resources

- [`02_Dashboard_Architecture.md`](./02_Dashboard_Architecture.md), chart and metric model
- [`06_Project_Decisions.md`](./06_Project_Decisions.md), KPI decisions
- [`08_Gap_Report.md`](./08_Gap_Report.md), metric gaps

### Professional terminology

- KPI
- Measure
- Dimension
- Metric registry
- Baseline
- Target
- Threshold
- Numerator
- Denominator
- Aggregation
- Filter context

---

## 15. Sample Size, Capture Window, Confidence, and Freshness

### Definition

- **Sample size (`n`)** is the number of observations.
- **Capture window** is the period or moment when data was collected.
- **Confidence** describes evidence strength.
- **Freshness** describes whether the evidence is current enough for the claim.

### Purpose

These fields prevent snapshots from appearing universal or permanently current.

### Advantages

- Users can judge reliability.
- Small samples become visible.
- Old metrics can be flagged.
- Different data generations can be compared honestly.

### Disadvantages and tradeoffs

- More metadata consumes interface space.
- Confidence can be difficult to summarize.
- Frequent refresh adds cost and operational work.

### Real-world example

A post-performance average based on 17 posts should not be interpreted the same as one based on 1,000 posts across a year.

### Cielito project example

The React specification includes follower counts, post counts, engagement rates, and capture windows. Yet different social generations and comment populations mean the displayed `n` must identify the exact dataset.

### Best practices

- Put `n`, window, source, and confidence in the card footer or evidence view.
- Define freshness thresholds by evidence class.
- Label a point-in-time capture as a snapshot.
- Block trend language when only one capture exists.

### Common mistakes

- Saying “growth” from one snapshot.
- Hiding a small sample.
- Showing current wording beside old evidence.
- Assuming a recently modified file contains recently captured data.

### Learning resources

- [`03_Design_System.md`](./03_Design_System.md), evidence-card anatomy
- [`07_Project_Brain.md`](./07_Project_Brain.md), freshness rules
- [`08_Gap_Report.md`](./08_Gap_Report.md), evidence freshness gaps

### Professional terminology

- Sample size
- Observation
- Capture window
- Point-in-time snapshot
- Time series
- Freshness SLA
- Confidence grade
- Statistical power

---

## 16. Missing Data and RequiresData States

### Definition

A **RequiresData** or **GapPlaceholder** state explicitly shows that a value cannot yet be populated and explains what input or route is needed.

### Purpose

It prevents unknown values from being displayed as zero, blank, or fabricated estimates.

### Advantages

- Builds trust.
- Makes data acquisition actionable.
- Prevents false financial claims.
- Allows honest product completeness.

### Disadvantages and tradeoffs

- The initial dashboard may contain many placeholders.
- Stakeholders may perceive the product as incomplete.
- Placeholder design and wording require care.

### Real-world example

Revenue cannot be calculated from public Instagram posts. The correct state is “Requires client order data,” not `0 EGP`.

### Cielito project example

Revenue, AOV, conversion, returns, CAC, repeat rate, and private audience demographics are client-only. Competitive and survey surfaces may require paid collection or primary research.

### Best practices

A missing-data card should show:

- What is missing
- Why it matters
- Required source class
- Acquisition route
- Permission/cost status
- Owner
- Whether the gap blocks a decision

### Common mistakes

- Using zero for unknown.
- Using “none” when collection was blocked.
- Creating realistic-looking dummy series in client-facing views.
- Treating a RequiresData card as a defect when it is an intentional honesty state.

### Learning resources

- `CIELITO_TAB_DEEPENING_MASTER_PROMPT.md`
- [`02_Dashboard_Architecture.md`](./02_Dashboard_Architecture.md)
- [`03_Design_System.md`](./03_Design_System.md)

### Professional terminology

- Missingness
- Null
- Unknown
- Not applicable
- RequiresData
- GapPlaceholder
- Data acquisition route
- Suppression rule

---

## 17. Normalization, Deduplication, and Transformation

### Definition

- **Normalization** converts inconsistent source data into a controlled structure.
- **Deduplication** identifies repeated records.
- **Transformation** derives new fields, classifications, or aggregates.

### Purpose

These steps make heterogeneous raw captures usable for analytics.

### Advantages

- Creates consistent categories.
- Reduces duplicate counts.
- Supports stable joins and metrics.
- Makes source-specific formats easier to compare.

### Disadvantages and tradeoffs

- Transformations can hide source nuance.
- Deduplication can incorrectly remove legitimate repeats.
- Classification rules may contain bias or errors.

### Real-world example

Two comments with identical text may be duplicates, or they may be two different customers saying the same thing. The deduplication key determines which interpretation wins.

### Cielito project example

Sentiment deduplication reportedly uses `(handle, text)`, which can collapse repeated comments from the same handle. Arabic purchase-intent substring rules can produce false positives. Raw product types and normalized “Other/untyped” counts represent different definitions.

### Best practices

- Preserve raw data.
- Document transformation rules.
- Record before/after counts.
- Create test cases for Arabic text and catalog options.
- Keep classification engine and version in output.

### Common mistakes

- Editing raw files in place.
- Deduplicating without a reasoned identity key.
- Mixing model and fallback outputs without disclosure.
- Treating normalized categories as raw facts.

### Learning resources

- Confirmed scripts in `_intel/`
- [`04_System_Architecture.md`](./04_System_Architecture.md)
- [`08_Gap_Report.md`](./08_Gap_Report.md), analytical gaps

### Professional terminology

- ETL
- ELT
- Normalization
- Deduplication
- Transformation
- Feature engineering
- Classification
- False positive
- False negative

---

## 18. Star Schemas and Analytical Models

### Definition

A **star schema** organizes data into:

- **Fact tables** containing measurable events or observations.
- **Dimension tables** containing descriptive context.

### Purpose

It supports consistent BI analysis and filter behavior.

### Advantages

- Easy for analysts to understand.
- Efficient for aggregations.
- Encourages clear grain.
- Works naturally with Power BI.

### Disadvantages and tradeoffs

- Requires disciplined entity modeling.
- Complex many-to-many relationships need care.
- A poor grain creates misleading measures.

### Real-world example

A social fact table may contain one row per post, while platform, date, creator, and source are dimensions.

### Cielito project example

The Power BI specification proposes:

- `fct_social_posts`
- `fct_catalog`
- `fct_instruments`
- Date, platform, persona, pillar, competitor, and source dimensions

However, product/SKU grain and canonical datasets remain unresolved, so the star schema is still a specification.

### Best practices

- Define fact-table grain first.
- Keep dimensions descriptive and reusable.
- Avoid ambiguous bidirectional relationships.
- Create a source dimension for evidence metadata.
- Test measures under different filter contexts.

### Common mistakes

- Putting mixed grains in one fact table.
- Counting rows without understanding grain.
- Duplicating dimensions across reports with different labels.
- Building DAX before the data model is stable.

### Learning resources

- `dashboard/powerbi_spec.md`
- [`04_System_Architecture.md`](./04_System_Architecture.md), Power BI architecture
- [`08_Gap_Report.md`](./08_Gap_Report.md)

### Professional terminology

- Fact table
- Dimension table
- Star schema
- Snowflake schema
- Semantic model
- Filter context
- Relationship cardinality
- DAX

---

## 19. Decision-First Information Architecture

### Definition

**Information architecture (IA)** organizes content, pages, navigation, hierarchy, and relationships so users can find and understand information.

**Decision-first IA** begins with the decision journey rather than the dataset structure.

### Purpose

It helps executives and operators move from situation to action without becoming lost in charts.

### Advantages

- Reduces cognitive load.
- Keeps the business story visible.
- Supports different levels of detail.
- Makes evidence available through progressive disclosure.

### Disadvantages and tradeoffs

- Requires difficult prioritization.
- Persistent executive elements can become stale.
- Deep navigation can hide useful analysis.

### Real-world example

A decision-first dashboard might open with “Conversion is leaking at mobile checkout” and then allow users to inspect page speed, funnel stages, and raw analytics.

### Cielito project example

The specified structure is:

- L0 Decision Dock
- L1 five-screen story
- L2 diagnostic rooms
- L3 Evidence Room

This is stronger than opening with a chart wall, but it requires review rules so the Decision Dock does not freeze outdated strategy.

### Best practices

- Lead with verdict and decisions.
- Use progressive disclosure.
- Keep evidence within a small number of interactions.
- Define page purpose and primary user.
- Test navigation with real tasks.

### Common mistakes

- Organizing pages only by source system.
- Giving every metric equal prominence.
- Mixing executive summary and analyst workbench.
- Keeping old strategic copy persistent after decisions change.

### Learning resources

- [`02_Dashboard_Architecture.md`](./02_Dashboard_Architecture.md)
- [`03_Design_System.md`](./03_Design_System.md)

### Professional terminology

- Information architecture
- Navigation model
- Progressive disclosure
- Drill-down
- Drill-through
- Hierarchy
- Wayfinding
- Cognitive load

---

## 20. Charts and Visual Encoding

### Definition

A chart maps data values to visual properties such as position, length, color, size, or shape.

### Purpose

Charts help users compare values, identify patterns, understand distributions, and detect relationships.

### Advantages

- Faster pattern recognition than raw tables.
- Supports comparison and prioritization.
- Can reveal outliers and distributions.

### Disadvantages and tradeoffs

- Poor chart choice can mislead.
- Color and scale can exaggerate differences.
- Dense dashboards can create cognitive overload.

### Real-world example

A histogram answers “How are prices distributed?” A scatterplot answers “How are two variables related?” A line chart answers “How did a measure change over time?”

### Cielito project example

- Owned-versus-earned comparison requires a log or carefully explained broken scale because values span orders of magnitude.
- Price bands can use a histogram.
- Positioning can use a scatterplot.
- Language performance can use paired bars.
- Individual posts may require a table with links and thumbnails.

### Best practices

- One business question per chart.
- Use insight-led titles.
- Add a “So what?” statement.
- Use consistent metric definitions.
- Explain unusual scales.
- Provide accessible summaries or tables.

### Common mistakes

- Using a donut for precise comparison.
- Using a line chart for unordered categories.
- Showing a log scale without labeling it.
- Comparing peak and median as if they were the same aggregation.
- Using color decoratively instead of semantically.

### Learning resources

- [`02_Dashboard_Architecture.md`](./02_Dashboard_Architecture.md), chart model
- [`03_Design_System.md`](./03_Design_System.md), chart semantics
- `CIELITO_TAB_DEEPENING_MASTER_PROMPT.md`

### Professional terminology

- Visual encoding
- Axis
- Scale
- Logarithmic scale
- Distribution
- Outlier
- Small multiples
- Annotation
- Data-ink ratio

---

## 21. Design Systems and Semantic Tokens

### Definition

A **design system** is a governed collection of principles, tokens, components, patterns, and documentation.

A **semantic token** names meaning rather than a raw value, such as `color-data-earned` instead of a hex code.

### Purpose

Design systems create consistency across screens, teams, and platforms.

### Advantages

- Faster implementation.
- Consistent meaning.
- Easier accessibility updates.
- Better React/Power BI parity.

### Disadvantages and tradeoffs

- Requires ownership and versioning.
- Premature tokens can lock in weak visual choices.
- Cross-platform parity has implementation cost.

### Real-world example

If “missing data” always uses the same orange dashed treatment, users learn the meaning across every page.

### Cielito project example

Confirmed semantic roles include:

- Owned content: grey
- Earned/creator: terracotta
- Positive: green
- Negative: red
- RequiresData: orange dashed

Warm tan, cream, terracotta, and charcoal are provisional creative direction, not approved exact tokens.

### Best practices

- Separate semantic role from exact value.
- Approve brand tokens against real assets.
- Define states, not only default components.
- Version the system.
- Validate contrast and accessibility.
- Maintain React and Power BI semantic parity.

### Common mistakes

- Inventing hex values because the direction is described.
- Treating a creative concept color as a global token.
- Defining components without loading, error, empty, stale, and disabled states.
- Using color as the only meaning carrier.

### Learning resources

- [`03_Design_System.md`](./03_Design_System.md)
- `creative/IMAGE_GENERATION_BRIEFS.md`

### Professional terminology

- Design token
- Semantic token
- Primitive token
- Component library
- Pattern library
- Theme
- State variant
- Design-system governance

---

## 22. Filters, State, and Interaction Design

### Definition

- A **filter** limits the data shown.
- **Application state** records current selections, route, open panels, and other interface conditions.
- An **interaction** is how users change or inspect the interface.

### Purpose

These concepts let users explore data without losing context.

### Advantages

- Supports different analytical questions.
- Makes one dashboard useful to several roles.
- Enables drill-down and evidence inspection.

### Disadvantages and tradeoffs

- Too many filters create confusion.
- Hidden filter state can produce misleading screenshots.
- Global and local filters can conflict.

### Real-world example

A platform filter may change every social chart. A local table sort should affect only the table.

### Cielito project example

Likely global state includes route, language, platform, date, selected evidence, and overlays. Local state includes row sorting, card expansion, and modal visibility. No implementation is confirmed.

### Best practices

- Distinguish global, route, and component state.
- Display active filters clearly.
- Define reset behavior.
- Preserve evidence context when drilling down.
- Use URLs for shareable analytical state when appropriate.

### Common mistakes

- Applying a filter to some cards but not others without disclosure.
- Resetting user state unexpectedly.
- Hiding the active comparison population.
- Adding controls that do not support a real question.

### Learning resources

- [`02_Dashboard_Architecture.md`](./02_Dashboard_Architecture.md), controls and states
- [`04_System_Architecture.md`](./04_System_Architecture.md), state-management architecture

### Professional terminology

- Global state
- Local state
- Filter context
- Cross-filtering
- Drill-through
- Query state
- URL state
- Interaction contract

---

## 23. Accessibility, RTL, and Responsive Design

### Definition

- **Accessibility** makes products usable by people with different abilities and assistive technologies.
- **RTL** supports right-to-left languages such as Arabic.
- **Responsive design** adapts layout to different screen sizes and input methods.

### Purpose

These are product-quality requirements, not optional visual polish.

### Advantages

- Expands usability.
- Reduces legal and reputational risk.
- Improves clarity for all users.
- Supports the Masri-first strategy.

### Disadvantages and tradeoffs

- Increases design and testing scope.
- Mixed Arabic/English content creates direction complexity.
- Dense tables and charts need alternative mobile patterns.

### Real-world example

A chart must have a text summary or accessible data table. Keyboard users must be able to open evidence. Arabic labels should not reverse English URLs or numbers incorrectly.

### Cielito project example

The dashboard is specified as bilingual and Arabic-first in context, but no breakpoints, focus behavior, ARIA rules, contrast validation, chart summaries, or mixed-direction implementation are confirmed.

### Best practices

- Select an accessibility standard before implementation.
- Test keyboard navigation and focus order.
- Provide chart summaries and data tables.
- Use logical CSS properties for RTL.
- Test mixed Arabic, English, numbers, handles, and URLs.
- Define mobile alternatives for wide tables and persistent docks.

### Common mistakes

- Mirroring the entire interface mechanically.
- Using color alone for sentiment or missing data.
- Claiming accessibility from contrast alone.
- Shrinking desktop charts until they technically fit mobile.

### Learning resources

- [`03_Design_System.md`](./03_Design_System.md), accessibility/RTL sections
- [`08_Gap_Report.md`](./08_Gap_Report.md), design stop-ship gaps

### Professional terminology

- WCAG
- ARIA
- Focus management
- Keyboard navigation
- Screen reader
- Bidirectional text
- Logical properties
- Breakpoint
- Reflow

---

## 24. Data Pipelines, Compilers, and Data Contracts

### Definition

- A **data pipeline** moves and transforms data through stages.
- A **compiler** in this project means a controlled program that reads research artifacts, validates them, and emits one dashboard-ready contract.
- A **data contract** defines the structure and rules consumers can rely on.

### Purpose

The compiler prevents the UI from reading heterogeneous research files directly.

### Advantages

- Centralizes validation.
- Creates one stable interface for React and Power BI.
- Blocks unsupported claims.
- Records missing-data states consistently.
- Makes builds reproducible.

### Disadvantages and tradeoffs

- Requires schemas and canonical inputs first.
- Becomes a critical dependency.
- Needs versioning, testing, and rollback.

### Real-world example

Instead of every chart independently parsing raw social JSON, a compiler emits normalized posts, metrics, source metadata, caveats, and validation results.

### Cielito project example

The specified `dashboard/build_cielito_data.py` should read intelligence, instruments, strategy, gaps, source rules, and media manifests, then emit `cielito_360_data.json`. It is missing, making it the central technical blocker.

### Best practices

- Define input and output schemas.
- Use canonical manifests.
- Emit build/version metadata.
- Validate source IDs, metric definitions, media, vocabulary, and gaps.
- Preserve a previous-good output.
- Produce a human-readable build report.

### Common mistakes

- Letting UI components parse raw research files.
- Writing the compiler before deciding canonical data.
- Silently coercing invalid data.
- Emitting output without version and lineage.

### Learning resources

- [`04_System_Architecture.md`](./04_System_Architecture.md)
- `dashboard/react_dashboard_spec.md`
- [`08_Gap_Report.md`](./08_Gap_Report.md), compiler gaps

### Professional terminology

- Pipeline
- Compiler
- Data contract
- Schema validation
- Build artifact
- Normalizer
- Validator
- Consumer
- Producer

---

## 25. Fail-Closed Validation

### Definition

A system **fails closed** when invalid or unsafe input blocks output rather than being accepted silently.

### Purpose

It protects users from unsupported claims, malformed data, missing sources, and permission violations.

### Advantages

- Reduces silent corruption.
- Makes failures visible.
- Enforces governance in code.
- Improves auditability.

### Disadvantages and tradeoffs

- Builds may fail more often initially.
- Teams must define error handling and recovery.
- Strict rules can block useful partial output if poorly designed.

### Real-world example

A KPI without a source ID should fail validation rather than render as an authoritative card.

### Cielito project example

The compiler is specified to block banned internal vocabulary, unsourced KPIs, unguarded financial values, missing or oversized media, and CDN hotlinks. This behavior is documented but not implemented.

### Best practices

- Define blocking versus warning rules.
- Emit actionable error messages.
- Allow safe partial completion only when explicitly designed.
- Test every fail-closed rule.
- Preserve the last known-good artifact.

### Common mistakes

- Catching every exception and continuing.
- Replacing missing values with zero.
- Logging errors while still publishing invalid output.
- Making every warning fatal without business justification.

### Learning resources

- [`04_System_Architecture.md`](./04_System_Architecture.md)
- [`05_Prompt_Analysis.md`](./05_Prompt_Analysis.md)
- [`08_Gap_Report.md`](./08_Gap_Report.md)

### Professional terminology

- Fail closed
- Fail open
- Validation error
- Warning
- Invariant
- Guardrail
- Quarantine
- Last known good

---

## 26. React Dashboard Fundamentals

### Definition

React is a component-based JavaScript library used to build interactive web interfaces.

### Purpose

The specified React target would provide a story-oriented, navigable dashboard with custom interactions and evidence views.

### Advantages

- Flexible user experience.
- Strong custom navigation and component control.
- Can support bilingual, responsive, and evidence-rich interactions.
- Suitable for the L0–L3 command-center model.

### Disadvantages and tradeoffs

- Requires frontend engineering, hosting, testing, and operations.
- Metrics and filters must be implemented manually or through libraries.
- Accessibility and state management require discipline.

### Real-world example

A React application can provide a persistent Decision Dock, route-based diagnostic rooms, evidence drawers, shareable filters, and custom RequiresData cards.

### Cielito project example

The React specification names `/dashboard/cielito-360`, but no React source, package manifest, routes, components, theme, or deployment are confirmed.

### Best practices

- Consume the compiled contract only.
- Organize by feature/domain.
- Use reusable semantic components.
- Define loading, error, stale, empty, and blocked states.
- Keep calculations out of presentation components.
- Test RTL, accessibility, and responsive behavior.

### Common mistakes

- Importing raw `_intel` files directly into components.
- Recalculating KPIs differently across cards.
- Building UI before schemas and acceptance criteria.
- Treating a successful local build as production readiness.

### Learning resources

- `dashboard/react_dashboard_spec.md`
- [`02_Dashboard_Architecture.md`](./02_Dashboard_Architecture.md)
- [`03_Design_System.md`](./03_Design_System.md)
- [`04_System_Architecture.md`](./04_System_Architecture.md)

### Professional terminology

- Component
- Prop
- State
- Hook
- Route
- Feature module
- Client-side rendering
- Static generation
- Bundle
- Hydration

---

## 27. Power BI Fundamentals

### Definition

Power BI is a business-intelligence platform for data modeling, DAX measures, interactive reports, refresh, and controlled sharing.

### Purpose

The specified Power BI target offers a familiar, refreshable report option for clients who prefer BI tooling over a custom web app.

### Advantages

- Strong analytical modeling and filtering.
- Mature report authoring.
- Familiar enterprise distribution.
- Natural support for star schemas and DAX.

### Disadvantages and tradeoffs

- Custom story and interaction flexibility is lower than React.
- Licensing, workspaces, gateways, and refresh require governance.
- Pixel-level parity with React is difficult.

### Real-world example

A Power BI report can provide executive, social, catalog, website, competitive, audience, and evidence pages using one semantic model.

### Cielito project example

The specification describes eight pages and a star schema, but no `.pbix`, seed CSV package, DAX implementation, workspace, refresh, RLS, or validator is confirmed.

### Best practices

- Stabilize fact-table grains before DAX.
- Use a metric registry shared with React.
- Define workspace, licensing, refresh, and RLS.
- Validate missing-data labels and source IDs.
- Document measures and filter behavior.

### Common mistakes

- Building measures before relationships are correct.
- Using calculated columns where measures are required.
- Duplicating business logic separately from React.
- Publishing to a workspace without an access model.

### Learning resources

- `dashboard/powerbi_spec.md`
- [`04_System_Architecture.md`](./04_System_Architecture.md)
- [`08_Gap_Report.md`](./08_Gap_Report.md)

### Professional terminology

- PBIX
- DAX
- Semantic model
- Workspace
- Gateway
- Scheduled refresh
- Row-level security
- Measure
- Slicer

---

## 28. Testing and Quality Assurance

### Definition

Testing verifies that data, calculations, components, interactions, accessibility, and deployments behave as intended.

### Purpose

It converts a specification into validated implementation proof.

### Advantages

- Prevents regressions.
- Makes releases repeatable.
- Supports safe metric changes.
- Provides evidence that “done” means something testable.

### Disadvantages and tradeoffs

- Tests require maintenance.
- Poorly chosen tests can create false confidence.
- Visual, accessibility, data, and integration testing require different tools.

### Real-world example

A metric test can use a small fixture where the expected result is known. An end-to-end test can verify that clicking a KPI opens the correct evidence.

### Cielito project example

No confirmed unit, schema, compiler, integration, end-to-end, visual, accessibility, security, or Power BI validation suite exists.

### Best practices

Test layers should include:

- Schema and contract tests
- Metric fixtures
- Compiler fail-closed tests
- React component tests
- Filter and interaction tests
- React/Power BI parity tests
- Accessibility tests
- Visual regression tests
- Security and permission tests
- Deployment smoke tests

### Common mistakes

- Testing only that code runs.
- Comparing screenshots without testing data correctness.
- Using production data as the only test fixture.
- Marking a feature complete without acceptance criteria.

### Learning resources

- [`04_System_Architecture.md`](./04_System_Architecture.md), testing architecture
- [`08_Gap_Report.md`](./08_Gap_Report.md), testing gaps

### Professional terminology

- Unit test
- Integration test
- End-to-end test
- Fixture
- Regression
- Smoke test
- Visual regression
- Acceptance test
- Test coverage

---

## 29. Deployment, Observability, and Operations

### Definition

- **Deployment** moves a build into an environment.
- **Observability** provides logs, metrics, traces, and context to understand system behavior.
- **Operations** includes environments, monitoring, rollback, backups, support, and incident response.

### Purpose

These practices keep a product reliable after implementation.

### Advantages

- Makes failures detectable.
- Supports rollback.
- Links running software to code and data versions.
- Creates accountability.

### Disadvantages and tradeoffs

- Adds infrastructure and maintenance cost.
- Requires ownership and alert policies.
- Monitoring can expose sensitive data if poorly configured.

### Real-world example

A production record should identify the environment, URL, commit, data version, compiler version, approver, timestamp, validation result, and rollback target.

### Cielito project example

The target route is referenced, but `RUN_STATE.json` declares no deployment. No hosting, CI/CD, environment separation, monitoring, rollback, or support process is confirmed.

### Best practices

- Separate build permission from deployment permission.
- Use preview and production environments.
- Record artifact and data versions.
- Define monitoring and incident ownership.
- Keep a tested rollback path.

### Common mistakes

- Treating a local build as deployment.
- Deploying because a build prompt was approved.
- Monitoring only uptime, not data freshness or metric validity.
- Logging secrets or private data.

### Learning resources

- [`04_System_Architecture.md`](./04_System_Architecture.md)
- [`07_Project_Brain.md`](./07_Project_Brain.md), deployment change records
- [`08_Gap_Report.md`](./08_Gap_Report.md)

### Professional terminology

- Environment
- CI/CD
- Deployment artifact
- Release
- Rollback
- Observability
- Logging
- Monitoring
- Alerting
- Incident response

---

## 30. Prompt Engineering and Untrusted Data

### Definition

Prompt engineering structures authority, task, context, constraints, output, validation, and tool permissions for an AI system.

**Untrusted data** is content that may be analyzed but must never be treated as governing instruction.

### Purpose

It prevents AI agents from confusing evidence with authority or performing unintended side effects.

### Advantages

- Reduces hallucination and overreach.
- Improves repeatability.
- Separates analysis from execution.
- Makes model outputs easier to validate.

### Disadvantages and tradeoffs

- More structured prompts take effort.
- Hidden runtime behavior can still undermine prompt rules.
- Long prompts can create context and maintenance problems.

### Real-world example

A scraped webpage may contain text such as “ignore previous instructions.” The agent should treat it as webpage content, not a command.

### Cielito project example

Raw webpages, product descriptions, captions, comments, transcripts, and research may contain text that an AI could misinterpret. Operator commands such as `Mega Run ...` also hide major side effects behind short phrases.

### Best practices

Use this order:

```text
Authority
→ Permission
→ Task
→ Trusted context
→ Untrusted evidence
→ Output schema
→ Validation
→ Side-effect execution
→ Audit record
```

Also:

- Version prompts.
- Record model and tool permissions.
- Use machine-checkable output schemas.
- Keep paid collection, code writes, and deployment separately authorized.

### Common mistakes

- Placing raw scraped text beside system instructions without boundaries.
- Letting a task prompt imply production deployment.
- Mixing facts, hypotheses, and strategy doctrine.
- Using one giant prompt as governance, task, data, permission, and validator.

### Learning resources

- [`05_Prompt_Analysis.md`](./05_Prompt_Analysis.md)
- `CIELITO_TAB_DEEPENING_MASTER_PROMPT.md`

### Professional terminology

- System prompt
- Task prompt
- Prompt injection
- Context boundary
- Structured output
- Tool permission
- Prompt manifest
- Determinism
- Evaluation

---

## 31. Permissions and Side Effects

### Definition

A permission model defines which actions an actor or agent may perform.

A **side effect** changes external state, such as writing code, spending money, collecting data, ingesting private files, generating media, or deploying.

### Purpose

It prevents a harmless-looking instruction from triggering an expensive or irreversible action.

### Advantages

- Protects budget, privacy, and production systems.
- Makes approvals auditable.
- Supports safe partial automation.

### Disadvantages and tradeoffs

- More approvals can slow work.
- Permission granularity requires design.
- Free external calls still need governance.

### Real-world example

“Analyze competitors” is not the same permission as “run a paid scraper against eight competitors and store handles.”

### Cielito project example

The project needs separate levels for:

- Read
- Analyze/derive
- Documentation write
- Code write
- Free external collection
- Paid collection
- Client-data ingestion
- Creative generation
- Preview deployment
- Production deployment
- Decision change

### Best practices

- Define maximum authorized level in every task.
- Require route ID and cost ceiling for paid work.
- Separate one-time and recurring approval.
- Record retries, data categories, PII level, retention, owner, and approver.
- Never infer deployment approval from coding approval.

### Common mistakes

- Assuming “free” means permissionless.
- Treating a prior route approval as permanent.
- Reusing approval for a broader target.
- Hiding deployment inside a build command.

### Learning resources

- [`05_Prompt_Analysis.md`](./05_Prompt_Analysis.md)
- [`07_Project_Brain.md`](./07_Project_Brain.md), permission model
- `_intel/data_pass_menu_base360.md`

### Professional terminology

- Authorization
- Permission envelope
- Least privilege
- Side effect
- Approval gate
- Cost ceiling
- Scope of consent
- Audit log

---

## 32. Security, Privacy, PII, and Media Rights

### Definition

- **Security** protects systems and data from unauthorized access or change.
- **Privacy** governs appropriate collection and use of personal data.
- **PII** is information that can identify or relate to a person.
- **Media rights** determine whether content can be reused, modified, published, or retained.

### Purpose

These disciplines protect users, creators, clients, the agency, and the brand.

### Advantages

- Reduces legal and reputational exposure.
- Builds client trust.
- Supports safe private-data ingestion.
- Clarifies creator attribution and usage.

### Disadvantages and tradeoffs

- Adds policy, legal, and technical work.
- Public data may still require careful handling.
- Rights can limit attractive dashboard media.

### Real-world example

A public Instagram post is visible, but that does not automatically grant permission to reuse its image in a public commercial dashboard or advertising campaign.

### Cielito project example

- Handles, exact comments, URLs, and media are retained.
- `strip_pii` is reportedly a no-op.
- Creator rights and attribution are undefined.
- Client-data governance is absent.
- An Apify token is placed in URL query parameters by current scripts.
- Founder and sustainability claims remain gated.

### Best practices

Before private-data ingestion, define:

- Purpose
- Access control
- Storage
- Encryption
- Retention
- Deletion
- Isolation
- Export controls
- Audit logging
- Incident response

Before creator-media reuse, define:

- Permission basis
- Attribution
- Paid scope
- Duration
- Territory
- Modification rights
- Revocation

### Common mistakes

- Calling public data risk-free.
- Calling handles “anonymous.”
- Assuming public availability equals reuse license.
- Logging secrets in URLs.
- Publishing synthetic founder or sustainability imagery without clear disclosure.

### Learning resources

- [`04_System_Architecture.md`](./04_System_Architecture.md), security/privacy sections
- [`05_Prompt_Analysis.md`](./05_Prompt_Analysis.md), creative safety
- [`07_Project_Brain.md`](./07_Project_Brain.md), rights rules
- [`08_Gap_Report.md`](./08_Gap_Report.md), security gaps

### Professional terminology

- PII
- Data minimization
- Purpose limitation
- Retention
- Deletion request
- Access control
- Encryption
- Consent
- License
- Attribution
- Revocation

---

## 33. Decisions, Gaps, Risks, and Readiness

### Definition

- A **decision** is a chosen direction.
- A **gap** is a missing or unresolved condition that blocks reliable work.
- A **risk** is a possible harmful outcome.
- **Readiness** describes whether required evidence and controls exist.

### Purpose

Separating these concepts makes planning and status reporting honest.

### Advantages

- Prevents “not done” from being confused with “not decided.”
- Prioritizes stop-ship issues.
- Makes closure evidence explicit.
- Supports safe partial progress.

### Disadvantages and tradeoffs

- Creates more governance records.
- A project may appear less ready when assessed rigorously.
- Gap counts can overwhelm teams if not prioritized.

### Real-world example

“No authentication” is a gap. “Private dashboard exposure” is a risk. “Client-only first release” is a decision. “Authentication tested and approved” is closure evidence.

### Cielito project example

Phase 8 contains 100 controlled gaps, but they are not 100 equal tasks. P0 gaps define stop-ship boundaries. One canonical manifest or privacy policy may close several gaps.

### Best practices

- Give gaps severity, priority, status, owner, dependencies, block, and closure proof.
- Do not mark a gap closed until downstream artifacts are updated.
- Distinguish intentional boundaries from defects.
- Use event-driven reviews when data or decisions change.

### Common mistakes

- Treating a recommendation as a decision.
- Treating a documented rule as an implemented control.
- Closing a gap with a meeting note but no implementation proof.
- Counting gaps instead of managing dependencies.

### Learning resources

- [`06_Project_Decisions.md`](./06_Project_Decisions.md)
- [`08_Gap_Report.md`](./08_Gap_Report.md)
- [`07_Project_Brain.md`](./07_Project_Brain.md)

### Professional terminology

- Decision ledger
- Gap register
- Risk register
- P0/P1/P2/P3
- Stop ship
- Closure proof
- Readiness gate
- Dependency
- Blocker

---

## 34. Project Case Studies

### 34.1 Case Study A — The `~190×` Claim

#### Situation

The flagship story says earned/creator content outperforms owned content by approximately `190×`.

#### Learning concepts

- Metric definition
- Aggregation
- Population
- Evidence lineage
- Executive communication
- Stop-ship governance

#### Problem

One specification describes a peak earned-view value divided by an owned median. Another names the metric median-to-median.

#### Why this matters

Both calculations may produce a number, but they answer different questions. Calling peak-to-median “median-to-median” materially misrepresents the comparison.

#### Correct professional response

- Freeze or caveat the KPI.
- Define numerator, denominator, platform, population, window, and aggregation.
- Create a reproducible fixture.
- Update executive copy, React, Power BI, decisions, and tests together.

#### Lesson

A metric is not a label plus a number. It is a governed definition.

---

### 34.2 Case Study B — Product Versus SKU

#### Situation

The catalog analysis discusses products, prices, availability, types, options, and sizes.

#### Learning concepts

- Grain
- Entity modeling
- Keys
- Schema
- Analytical validity

#### Problem

The Power BI specification expects one row per SKU, while the confirmed catalog structure appears product-centered. Generic option fields contain colors, defaults, and other values, not only sizes.

#### Correct professional response

- Define product, variant, and SKU entities.
- Define stable IDs and relationships.
- Parse option semantics.
- Recalculate availability and size metrics at the correct grain.

#### Lesson

A clean chart cannot repair a wrong data grain.

---

### 34.3 Case Study C — 120, 150, or 210 Social Posts

#### Situation

Different project artifacts reference different social populations.

#### Learning concepts

- Canonical datasets
- Versioning
- Capture windows
- Sample disclosure
- Reproducibility

#### Problem

The numbers may represent different runs or inclusion rules. None is automatically “wrong,” but only one controlled generation can power a governed build for a defined use.

#### Correct professional response

- Create a canonical manifest.
- Preserve all generations.
- Define inclusion rules and windows.
- Update every `n` disclosure.

#### Lesson

More rows do not automatically mean more truth.

---

### 34.4 Case Study D — Revenue and ROI

#### Situation

The dashboard wants to explain financial impact.

#### Learning concepts

- Missing data
- Client-owned data
- Scenario modeling
- Privacy
- RequiresData

#### Problem

Public social and catalog data cannot provide revenue, AOV, conversion, returns, CAC, or repeat rate.

#### Correct professional response

- Render “To be baselined — requires client data.”
- Define client-data governance before ingestion.
- Define scenario methodology before publishing estimates.
- Never use zero as unknown.

#### Lesson

Financial honesty is a product feature.

---

### 34.5 Case Study E — Creator Content and Founder Claims

#### Situation

The dashboard and creative strategy want to use real creator media, founder storytelling, and a fruit-leather concept.

#### Learning concepts

- Rights
- Consent
- Attribution
- Hypothesis
- Synthetic media
- Public claims

#### Problem

Public creator content is not automatically licensed for commercial reuse. The founder image and fruit-leather status are not confirmed.

#### Correct professional response

- Obtain rights and define attribution.
- Use actual founder photography for real founder claims.
- Keep fruit leather founder-gated.
- Label synthetic concepts through export and handoff.

#### Lesson

Visual realism can create factual claims even when the caption is cautious.

---

### 34.6 Case Study F — Build Versus Deploy

#### Situation

A short operator command references scaffolding, building, and deployment.

#### Learning concepts

- Permissions
- Side effects
- Environments
- Implementation proof
- Deployment proof

#### Problem

A build instruction can be interpreted as production authorization when permission levels are not separated.

#### Correct professional response

- Separate code write, preview deployment, and production deployment.
- Record commit, data version, validation result, approver, environment, and rollback.

#### Lesson

“Can build” and “may deploy” are different authorities.

---

### 34.7 Case Study G — Sentiment and Purchase Intent

#### Situation

Comments are scored by a local model with fallback logic and keyword-based purchase-intent detection.

#### Learning concepts

- Model provenance
- Fallback behavior
- False positives
- Dataset population
- Canonical gating

#### Problem

The validation context references another brand, and Arabic substring logic may match unrelated words. Model fallback can enter output without a publication gate.

#### Correct professional response

- Record engine and version per item.
- Validate on Cielito-relevant samples.
- Test Arabic token boundaries.
- Separate comments and captions when appropriate.
- Block or caveat fallback-derived governed metrics.

#### Lesson

An AI model output is a derived measurement, not raw customer truth.

---

## 35. Role-Based Learning Paths

### 35.1 Executive or founder

Read:

1. Sections 5–9
2. Sections 14–16
3. Sections 33–34
4. `final/DECISION_DOCK.md`
5. [`06_Project_Decisions.md`](./06_Project_Decisions.md)

Must understand:

- What has been decided versus recommended
- Why financial impact remains unbaselined
- Which founder and rights decisions are required
- Which P0 gaps block trustworthy release

### 35.2 Product manager

Read:

1. Sections 6–9
2. Sections 19–23
3. Sections 33–34
4. [`02_Dashboard_Architecture.md`](./02_Dashboard_Architecture.md)
5. [`08_Gap_Report.md`](./08_Gap_Report.md)

Must understand:

- Users and decision journeys
- MVP scope and exclusions
- Acceptance criteria
- Intentional boundaries versus defects
- React/Power BI launch choice

### 35.3 Data analyst

Read:

1. Sections 10–18
2. Sections 24–25
3. Case studies A, B, C, D, and G
4. Source registry and relevant datasets

Must understand:

- Evidence classes
- Grain and canonicality
- Metric registry design
- Reproducibility
- Sample and confidence disclosure

### 35.4 Dashboard/UX designer

Read:

1. Sections 6–8
2. Sections 19–23
3. Case studies A, D, and E
4. [`03_Design_System.md`](./03_Design_System.md)

Must understand:

- Decision-first hierarchy
- Evidence and missing-data states
- Semantic color
- RTL/accessibility/responsive requirements
- Why provisional direction is not an approved token set

### 35.5 Frontend engineer

Read:

1. Sections 12–16
2. Sections 19–26
3. Sections 28–29
4. [`04_System_Architecture.md`](./04_System_Architecture.md)

Must understand:

- Compiled contract boundary
- Metric centralization
- State and filter contracts
- Error/loading/stale/blocked states
- Testing and deployment separation

### 35.6 Power BI developer

Read:

1. Sections 12–18
2. Sections 20 and 27–29
3. `dashboard/powerbi_spec.md`
4. Metric and canonicality gaps

Must understand:

- Fact-table grain
- Dimensions and relationships
- DAX parity
- Missing-data labels
- Source and confidence dimensions

### 35.7 AI agent or prompt engineer

Read:

1. Sections 10–16
2. Sections 30–33
3. [`05_Prompt_Analysis.md`](./05_Prompt_Analysis.md)
4. [`07_Project_Brain.md`](./07_Project_Brain.md)

Must understand:

- Truth precedence
- Untrusted evidence
- Permission envelopes
- Fail-closed behavior
- Partial completion
- Memory and handoff updates

### 35.8 Privacy, legal, or governance reviewer

Read:

1. Sections 11, 15, 31–33
2. Case studies D and E
3. Security/rights sections of Phases 4, 5, 7, and 8

Must understand:

- Client-data handling
- Creator rights
- PII limitations
- Synthetic-media disclosure
- Approval and retention gaps

---

## 36. Practical Exercises

### Exercise 1 — Classify statements

Classify each as repository fact, captured fact, derived fact, declared state, interpretation, hypothesis, or unknown:

1. The React dashboard exists.
2. A catalog file contains 250 product records.
3. Cielito should repair its owned engine rather than rebrand.
4. Fruit leather is a current active product differentiator.
5. A run-state file says the base 360 is closed.

### Exercise 2 — Define a metric

Create a complete metric contract for “Owned Engagement Rate.” Include formula, population, filters, period, source, target, minimum sample, owner, and caveat.

### Exercise 3 — Find the grain

For each proposed table, complete “One row represents…”:

- Social posts
- Products
- Variants
- SKUs
- Comments
- Creators
- Sources

### Exercise 4 — Design a RequiresData card

Design the content structure for “Revenue Impact” without inventing data.

### Exercise 5 — Map a claim to evidence

Take “Arabic-first content can improve owned performance” and identify:

- Evidence needed
- Current evidence class
- Assumptions
- Required sample/window
- Decision supported
- What would falsify the claim

### Exercise 6 — Separate permissions

Define permissions for:

1. Read the repository.
2. Recompute a local metric.
3. Modify documentation.
4. Modify compiler code.
5. Run a free external crawl.
6. Run paid route P1.
7. Ingest Shopify exports.
8. Deploy preview.
9. Deploy production.

### Exercise 7 — Review a dashboard card

For a proposed card showing `~190×`, list every field and validation check required before publication.

### Exercise 8 — Close a gap

Write closure evidence for `GAP-DAT-002` product/variant/SKU grain.

### Exercise 9 — Create a handoff

Write a structured handoff for an AI that reviewed the metric registry but was blocked by missing canonical social generations.

### Exercise 10 — Identify intentional boundaries

Explain why each may be acceptable:

- Read-only MVP
- Manual refresh
- No database
- RequiresData cards
- Deferred paid route

---

## 37. Exercise Answer Guide

### Answer 1

1. React dashboard exists → **Unknown/unconfirmed**.
2. Catalog file contains 250 product records → **Repository fact** about that file.
3. Repair rather than rebrand → **Accepted decision/strategic interpretation**, not raw fact.
4. Fruit leather is active differentiator → **Hypothesis/founder-gated**.
5. Run-state says closed → **Declared state**.

### Answer 2

A valid answer must avoid inventing the formula. It should mark unresolved fields and require approval. It should specify whether engagement uses likes plus comments, which follower base, which platform, which post population, and which period.

### Answer 3

A correct answer separates product, variant, and SKU rather than forcing them into one grain. Comment and creator identity rules must be explicit.

### Answer 4

The card should show:

- “To be baselined”
- Required client data
- Why the metric matters
- Owner/request status
- No numeric zero
- No invented scenario
- Source and gap reference

### Answer 5

The current project contains language-performance interpretations, but a governed claim requires a canonical post population, language classification rule, platform separation, metric definition, sample, window, and confounder caveats.

### Answer 6

Each step requires a distinct permission level. Free collection still requires approval. Paid collection requires route and ceiling. Client data requires privacy governance. Preview and production deployment require separate approvals.

### Answer 7

Required fields include formula, numerator, denominator, aggregation, platform, population, window, sample, source IDs, caveat, owner, target use, reproducible test, React/PBI parity, and executive-copy review.

### Answer 8

Closure requires an approved domain model, stable IDs, schemas, normalization rules, migration notes, uniqueness/referential tests, updated metric definitions, compiler implementation, and downstream documentation changes.

### Answer 9

The handoff must name branch, commit, files read, metrics reviewed, unresolved generation conflict, work completed, work blocked, exact missing approval, and next action. “Use latest social data” is not acceptable.

### Answer 10

Each is acceptable only when intentionally selected, documented, and matched to the product requirement. An explicit bounded limitation is different from an accidental missing capability.

---

## 38. Professional Terminology Reference

| Term | Practical meaning in this project |
|---|---|
| Acceptance criteria | Testable conditions required to call the MVP complete |
| Aggregation | How values are combined, such as median, mean, sum, peak, or count |
| Audit trail | Record of sources, decisions, permissions, changes, and execution |
| Baseline | Starting measured value used for comparison |
| Canonical | Formally selected as authoritative |
| Capture window | Time period or timestamp represented by collected data |
| Cardinality | Relationship count, such as one product to many variants |
| Compiler | Program that validates project artifacts and emits dashboard-ready data |
| Confidence grade | Project label describing evidence strength |
| Data contract | Agreed structure and behavior between data producer and consumer |
| Data grain | What one row represents |
| Data lineage | Transformation path from source to output |
| Decision Dock | Persistent executive verdict, decisions, honesty, north star, and watch list |
| Dimension | Category used to filter or group facts |
| Evidence estate | Collection of raw, derived, media, audit, and provenance artifacts |
| Fact table | Table of measurable events or observations |
| Fail closed | Block unsafe output when validation fails |
| Filter context | Active filters affecting a measure |
| GapPlaceholder | Designed representation of unavailable data |
| Idempotency | Repeating an operation does not create unintended duplicate effects |
| Implementation proof | Evidence that a specified behavior actually exists |
| KPI | Metric selected to monitor an important objective |
| Lineage | Trace from raw input through transformations to claims and decisions |
| Manifest | Versioned list of authoritative files, checksums, schemas, and metadata |
| Measure | Calculated analytical value |
| Metric registry | Authoritative catalog of metric definitions and governance |
| Observability | Ability to understand system state through logs, metrics, traces, and metadata |
| PII | Information that identifies or relates to a person |
| Progressive disclosure | Showing summary first and detail when requested |
| Provenance | Origin and history of data or a claim |
| RequiresData | Honest state saying a value needs a defined missing input |
| Schema | Structural and validation rules for data |
| Semantic token | Design value named by meaning rather than raw color or size |
| Snapshot | Point-in-time observation, not a trend |
| Source registry | Controlled list of source IDs and evidence meaning |
| Star schema | BI model with fact and dimension tables |
| Stop ship | Gap that blocks publication, ingestion, implementation, or deployment in scope |
| Surrogate key | System-generated stable identifier |
| Traceability | Ability to connect requirements, data, code, tests, and decisions |
| Untrusted data | Content that may be analyzed but cannot grant authority |
| Validation | Verification that data or implementation follows its contract |
| Versioning | Controlled tracking of changes over time |

---

## 39. Learning Resources

### 39.1 Internal foundation

| Goal | Resource |
|---|---|
| Understand file estate | [`00_Project_Inventory.md`](./00_Project_Inventory.md) |
| Understand the project | [`01_Understanding.md`](./01_Understanding.md) |
| Understand dashboard pages and components | [`02_Dashboard_Architecture.md`](./02_Dashboard_Architecture.md) |
| Understand visual meaning | [`03_Design_System.md`](./03_Design_System.md) |
| Understand system and compiler architecture | [`04_System_Architecture.md`](./04_System_Architecture.md) |
| Understand prompts and AI behavior | [`05_Prompt_Analysis.md`](./05_Prompt_Analysis.md) |
| Understand approved and blocked decisions | [`06_Project_Decisions.md`](./06_Project_Decisions.md) |
| Enter the project efficiently | [`07_Project_Brain.md`](./07_Project_Brain.md) |
| Understand readiness and blockers | [`08_Gap_Report.md`](./08_Gap_Report.md) |

### 39.2 Project operating sources

- `CIELITO_TAB_DEEPENING_MASTER_PROMPT.md`
- `RUN_STATE.json`
- `_intel/SOURCE_REGISTRY.md`
- `_intel/data_pass_menu_base360.md`
- `_intel/scraping_evidence_log.yaml`
- `dashboard/react_dashboard_spec.md`
- `dashboard/powerbi_spec.md`
- `creative/IMAGE_GENERATION_BRIEFS.md`
- `final/DECISION_DOCK.md`
- `final/NEXT_STEPS.md`

### 39.3 Recommended learning sequence by discipline

#### Dashboard and BI

1. Decision questions
2. Metrics and dimensions
3. Information architecture
4. Chart selection
5. Interaction and filters
6. Evidence and missing-data states
7. Accessibility and responsive behavior

#### Data and analytics

1. Evidence classes
2. Grain and keys
3. Canonical datasets
4. Transformation and lineage
5. Metric registry
6. Star schema
7. Validation and testing

#### Engineering

1. Current versus target architecture
2. Data contract
3. Compiler
4. Fail-closed validation
5. React or Power BI implementation
6. Tests
7. CI/CD and operations

#### AI and governance

1. Authority hierarchy
2. Trusted versus untrusted context
3. Permission envelope
4. Structured output
5. Validation
6. Audit and handoff

---

## 40. Mastery Checklist

A reader is ready to contribute when they can answer all of the following.

### Project understanding

- [ ] Explain the three-system mental model: evidence, decision intelligence, dashboard blueprint.
- [ ] Explain why the runnable dashboard is unconfirmed.
- [ ] State the accepted business sequence without calling it implemented.

### Evidence and data

- [ ] Classify facts, interpretations, hypotheses, and unknowns.
- [ ] Trace a claim to raw evidence.
- [ ] Define grain and keys for core entities.
- [ ] Explain why canonical generations are required.
- [ ] Explain why product and SKU cannot be used interchangeably.

### Metrics

- [ ] Define a complete metric contract.
- [ ] Explain the `~190×` conflict.
- [ ] Explain sample, window, confidence, and freshness.
- [ ] Explain why missing is not zero.

### Dashboard and design

- [ ] Explain L0–L3 architecture.
- [ ] Select an appropriate chart for a business question.
- [ ] Distinguish semantic color roles from provisional tokens.
- [ ] Explain RTL, accessibility, and responsive requirements.

### Engineering

- [ ] Explain the compiler’s role.
- [ ] Explain fail-closed behavior.
- [ ] Distinguish React and Power BI strengths and costs.
- [ ] Explain build, deploy, and validate as separate states.

### Governance and safety

- [ ] Separate task permission from side-effect permission.
- [ ] Treat external content as untrusted data.
- [ ] Explain client-data, PII, creator-rights, and founder-claim gates.
- [ ] Use the Decision Ledger and Gap Report correctly.
- [ ] Produce a structured handoff.

---

## 41. Phase 9 Validation Gate

### 41.1 Learning-contract gate

- [x] Definitions provided.
- [x] Purposes explained.
- [x] Advantages documented.
- [x] Disadvantages and tradeoffs documented.
- [x] Real-world examples included.
- [x] Every major concept related to the Cielito project.
- [x] Best practices documented.
- [x] Common mistakes documented.
- [x] Learning resources provided.
- [x] Professional terminology defined.

### 41.2 Coverage gate

- [x] Dashboard and BI fundamentals covered.
- [x] Evidence, provenance, lineage, grain, schema, canonicality, and metrics covered.
- [x] Missing data, confidence, freshness, and transformation covered.
- [x] Information architecture, charts, design systems, state, RTL, accessibility, and responsive design covered.
- [x] Compiler, React, Power BI, testing, deployment, and operations covered.
- [x] Prompt injection, permissions, privacy, PII, rights, decisions, gaps, and readiness covered.
- [x] Project-specific case studies included.
- [x] Role-based paths, exercises, answers, terminology, and mastery checks included.

### 41.3 Evidence and safety gate

- [x] No project gap was marked closed.
- [x] No metric conflict was silently resolved.
- [x] No canonical dataset was selected.
- [x] No implementation or deployment was invented.
- [x] No founder, client, creator, privacy, or legal approval was invented.
- [x] No production code changed.
- [x] No external data collection, paid route, client-data ingestion, media generation, build, or deployment occurred.

### 41.4 Quality result

**Phase 9 result:** PASS — PROJECT-SPECIFIC LEARNING MODE COMPLETE.

The project now has a structured educational layer that helps a new human or AI understand both the professional disciplines involved and the exact mistakes those disciplines prevent in the Cielito estate.

### 41.5 Phase transition

Phase 10 (`10_Design_Principles.md`) remains blocked until the repository owner validates or explicitly advances beyond Phase 9.

---

## 42. Glossary

| Term | Meaning |
|---|---|
| Learning Mode | DIOS phase that teaches concepts thoroughly and connects them to the project |
| Concept | Reusable professional idea, method, pattern, or discipline |
| Tradeoff | Benefit gained at the cost of another quality, resource, or constraint |
| Best practice | Widely useful professional method that still requires project judgment |
| Common mistake | Recurring misuse that creates incorrect, unsafe, or low-quality outcomes |
| Case study | Project example used to connect theory to practical reasoning |
| Mastery | Ability to explain, apply, challenge, and validate a concept |
| Learning path | Ordered set of topics for a specific role |
| Professional terminology | Shared language used by specialists to describe work precisely |

---

## 43. Document Control

| Field | Value |
|---|---|
| Document | `docs/DIOS/09_Learning_Guide.md` |
| Phase | 9 |
| Created | 2026-07-12 |
| Authoring system | DIOS analysis through connected GitHub workflow |
| Repository | `omarali304ii-byte/Islam-Brain` |
| Working branch | `docs/dios-phase-0-inventory` |
| Major concept modules | 28 |
| Project case studies | 7 |
| Practical exercises | 10 |
| Production code changed | No |
| External actions executed | No |
| Next phase | `10_Design_Principles.md`, pending owner validation |
