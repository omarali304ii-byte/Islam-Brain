# 11 — Best Practices

> **System:** Dashboard Intelligence Operating System (DIOS)  
> **Repository:** `omarali304ii-byte/Islam-Brain`  
> **Repository baseline:** `44cea987cd42f077cc0f6e448bcdc69f2683ecb1`  
> **DIOS working branch:** `docs/dios-phase-0-inventory`  
> **Best-practices date:** 2026-07-12  
> **Phase status:** Phase 11 — Complete, awaiting validation  
> **Previous artifacts:** [`00_Project_Inventory.md`](./00_Project_Inventory.md) · [`01_Understanding.md`](./01_Understanding.md) · [`02_Dashboard_Architecture.md`](./02_Dashboard_Architecture.md) · [`03_Design_System.md`](./03_Design_System.md) · [`04_System_Architecture.md`](./04_System_Architecture.md) · [`05_Prompt_Analysis.md`](./05_Prompt_Analysis.md) · [`06_Project_Decisions.md`](./06_Project_Decisions.md) · [`07_Project_Brain.md`](./07_Project_Brain.md) · [`08_Gap_Report.md`](./08_Gap_Report.md) · [`09_Learning_Guide.md`](./09_Learning_Guide.md) · [`10_Design_Principles.md`](./10_Design_Principles.md)  
> **Next phase:** Blocked until this document passes its quality gate

---

## Table of Contents

1. [Phase Entry Decision](#1-phase-entry-decision)
2. [Purpose and Scope](#2-purpose-and-scope)
3. [How to Use Best Practices](#3-how-to-use-best-practices)
4. [Practice Strength Levels](#4-practice-strength-levels)
5. [The Golden Path](#5-the-golden-path)
6. [Repository Entry and Task Scoping](#6-repository-entry-and-task-scoping)
7. [Research and Evidence Capture](#7-research-and-evidence-capture)
8. [Source Registry and Provenance](#8-source-registry-and-provenance)
9. [Canonical Data and Dataset Promotion](#9-canonical-data-and-dataset-promotion)
10. [Data Modeling and Schema Design](#10-data-modeling-and-schema-design)
11. [Metric Definition and KPI Governance](#11-metric-definition-and-kpi-governance)
12. [Analysis and Interpretation](#12-analysis-and-interpretation)
13. [Decision Governance](#13-decision-governance)
14. [Product Scope and Acceptance Criteria](#14-product-scope-and-acceptance-criteria)
15. [Dashboard Information Architecture](#15-dashboard-information-architecture)
16. [Chart and Card Design](#16-chart-and-card-design)
17. [Design-System Practice](#17-design-system-practice)
18. [Accessibility, RTL, and Responsive Practice](#18-accessibility-rtl-and-responsive-practice)
19. [Media and Creative Practice](#19-media-and-creative-practice)
20. [Compiler and Data-Contract Practice](#20-compiler-and-data-contract-practice)
21. [React Implementation Practice](#21-react-implementation-practice)
22. [Power BI Implementation Practice](#22-power-bi-implementation-practice)
23. [Testing and Quality Assurance](#23-testing-and-quality-assurance)
24. [Prompt and AI-Agent Practice](#24-prompt-and-ai-agent-practice)
25. [Permission and External-Collection Practice](#25-permission-and-external-collection-practice)
26. [Security, Privacy, PII, and Rights Practice](#26-security-privacy-pii-and-rights-practice)
27. [Git, Pull Request, and Documentation Practice](#27-git-pull-request-and-documentation-practice)
28. [Deployment and Release Practice](#28-deployment-and-release-practice)
29. [Observability and Incident Practice](#29-observability-and-incident-practice)
30. [Project Brain, Handoff, and Memory Practice](#30-project-brain-handoff-and-memory-practice)
31. [Definition of Ready](#31-definition-of-ready)
32. [Definition of Done](#32-definition-of-done)
33. [Stage Checklists](#33-stage-checklists)
34. [Review Checklists by Role](#34-review-checklists-by-role)
35. [Practice Templates](#35-practice-templates)
36. [Common Failure Patterns](#36-common-failure-patterns)
37. [Exception and Deviation Practice](#37-exception-and-deviation-practice)
38. [Maturity Model](#38-maturity-model)
39. [Principle and Gap Traceability](#39-principle-and-gap-traceability)
40. [Phase 11 Validation Gate](#40-phase-11-validation-gate)
41. [Glossary](#41-glossary)
42. [Document Control](#42-document-control)

---

## 1. Phase Entry Decision

The owner requested Phase 11 before Phase 10 existed. Phase 10 was therefore completed first as the mandatory DIOS prerequisite.

Phase 10 passed its quality gate and established the governing design principles. This authorizes Phase 11.

This phase records:

- **Phase 10 acceptance for progression:** The principles are accepted as the basis for best-practice procedures, while remaining unimplemented unless evidence proves otherwise.
- **Authorized work:** Convert principles, lessons, decisions, and gaps into repeatable working methods and checklists.
- **Forbidden work:** Do not implement production code, select canonical data, approve unresolved metrics, collect external data, ingest client data, generate media, deploy, or close gaps without proof.

> [!IMPORTANT]
> A best practice is guidance for performing future work. Its presence in this file does not prove the repository currently follows it.

---

## 2. Purpose and Scope

The principles explain **what must remain true**. Best practices explain **how teams should work** to preserve those truths.

This document provides:

- Repeatable procedures
- Entry and exit checks
- Review rules
- Required records
- Evidence standards
- Role-specific responsibilities
- Definition of Ready and Definition of Done
- Templates for recurring project work
- Failure patterns and corrective actions

It covers the full lifecycle:

```text
Request
→ Scope
→ Authority
→ Evidence
→ Definitions
→ Decision
→ Product contract
→ Data contract
→ Implementation
→ Validation
→ Review
→ Release
→ Observation
→ Memory update
```

---

## 3. How to Use Best Practices

### 3.1 Before starting work

1. Read the Project Brain.
2. Classify the task.
3. Identify the maximum authorized permission.
4. Load the minimum context pack.
5. Check related decisions, gaps, and principles.
6. Define the output contract.
7. Confirm the Definition of Ready.

### 3.2 During work

- Preserve raw evidence.
- Record assumptions.
- Keep side effects within scope.
- Validate incrementally.
- Surface blockers immediately.
- Update affected records when state changes.

### 3.3 Before declaring completion

- Test the exact acceptance criteria.
- Produce implementation or closure proof.
- Update downstream artifacts.
- Create a structured handoff.
- Do not use “done” when the state is only specified, coded, or previewed.

---

## 4. Practice Strength Levels

| Level | Meaning | Deviation rule |
|---|---|---|
| **MUST** | Required for evidence, safety, privacy, rights, governed metrics, or release integrity | Explicit approved deviation required; some cannot be waived |
| **SHOULD** | Strong default with broad professional benefit | May deviate with documented rationale and validation |
| **MAY** | Useful contextual option | Team may choose based on scope and constraints |
| **MUST NOT** | Prohibited behavior | Cannot proceed without changing the task or receiving lawful/authorized resolution |

### 4.1 Non-waivable areas

The following cannot be bypassed by convenience:

- Fabricated data or claims
- Unauthorized client-data ingestion
- Unauthorized paid collection
- Secret exposure
- Creator/media use without appropriate rights
- Founder or sustainability claims without confirmation
- Production deployment without approval
- Treating untrusted content as authority

---

## 5. The Golden Path

### BP-000 — Use the project golden path

Every governed task SHOULD follow this sequence:

1. **Orient:** Read Brain snapshot, branch, phase, PR, blockers.
2. **Classify:** Research, analysis, decision, design, code, collection, data handling, creative, or deployment.
3. **Authorize:** Resolve permission and approver.
4. **Define:** State deliverable, path, inputs, exclusions, and acceptance criteria.
5. **Ground:** Identify authoritative evidence and freshness.
6. **Model:** Define grain, schema, identities, metrics, and states where applicable.
7. **Execute:** Perform only bounded work.
8. **Validate:** Test semantics, safety, quality, and parity.
9. **Propagate:** Update decisions, source records, gaps, Brain, and dependent targets.
10. **Handoff:** Record exact state and next action.

Skipping a step requires an explicit reason. Skipping authorization, evidence grounding, or validation is not allowed for governed output.

---

## 6. Repository Entry and Task Scoping

### BP-ENT-001 — Start with the Project Brain

**MUST:** Read `07_Project_Brain.md` before broad project work.

**Why:** It prevents full-repository rediscovery and exposes known contradictions and blocked states.

**Evidence:** Files read list in the handoff.

---

### BP-ENT-002 — Use the minimum context pack

**SHOULD:** Read only the specialist artifacts required for the task before expanding scope.

**Examples:**

- Metric task: Brain → Decisions → relevant raw/derived data → source registry → evidence log.
- UI task: Brain → Dashboard Architecture → Design System → System Architecture → compiled contract.
- Prompt task: Brain → Prompt Analysis → target prompt → output validator.

**Avoid:** Scanning the full repository “just in case.”

---

### BP-ENT-003 — Write the task contract first

Every task MUST define:

```yaml
task: ""
deliverable: ""
path_or_target: ""
authorized_permission: ""
inputs: []
outputs: []
excluded_actions: []
acceptance_criteria: []
known_blockers: []
```

A vague request such as “finish the dashboard” is not ready.

---

### BP-ENT-004 — Resolve branch and PR truth

Before repository writes, MUST confirm:

- Repository
- Branch
- Current head SHA
- Open PR state
- Base branch
- Whether previous work was merged
- Whether the requested file already exists

This prevents duplicate PRs, accidental default-branch writes, and false history.

---

### BP-ENT-005 — Separate discovery from mutation

**SHOULD:** Perform read-only investigation before the first write.

**MUST:** Obtain explicit authorization before production mutation, data collection, private-data use, media generation, or deployment.

---

## 7. Research and Evidence Capture

### BP-RES-001 — Define the research question

Before collecting, MUST record:

- Decision supported
- Exact question
- Population
- Target source
- Required fields
- Time window
- Expected limitations
- Permission and cost
- Stop condition

Collection without a decision question creates data volume, not intelligence.

---

### BP-RES-002 — Prefer primary sources

**SHOULD:** Use first-party storefronts, platform records, client exports, and direct captures before summaries.

**MUST:** Label secondary and inferred evidence.

---

### BP-RES-003 — Preserve raw captures

Raw evidence MUST be immutable and accompanied by:

- Capture timestamp
- Source URL or system
- Route/tool
- Parameters
- Response status
- File checksum
- Collector/version
- Permission record
- Cost where applicable

Transformations create new artifacts.

---

### BP-RES-004 — Record blocked and partial routes

When collection fails or is incomplete, MUST record:

- Target
- Attempt time
- Error/status
- Data obtained
- Data missing
- Cost incurred
- Retry permission
- Current state: blocked, partial, deferred, or dropped

MUST NOT translate failure into “none found.”

---

### BP-RES-005 — Bound retries

Retries MUST have:

- Maximum attempts
- Backoff
- Cost ceiling
- Idempotency strategy
- Stop condition
- Approval scope

A later explicit dropped decision overrides earlier retry suggestions.

---

### BP-RES-006 — Minimize collection

Collect only fields needed for the decision. Public personal data SHOULD be minimized, and client-private data MUST follow approved governance.

---

### BP-RES-007 — Validate the captured population

Before analysis, SHOULD compare:

- Expected versus received count
- Date range
- Duplicates
- Missing fields
- Platform/account identity
- Pagination completeness
- Media manifest alignment

---

## 8. Source Registry and Provenance

### BP-EVD-001 — Assign stable source IDs

Every governed source MUST have a unique stable ID independent of filename.

Recommended fields:

```yaml
source_id: ""
type: "public | client | survey | model | instrument | derived"
owner: ""
captured_at: ""
window: ""
location: ""
checksum: ""
grade: ""
rights_or_permission: ""
retention: ""
```

---

### BP-EVD-002 — Register exact generations

A source ID SHOULD identify the exact version/generation, not only a conceptual source such as “Instagram.”

Example:

- Weak: `instagram_posts`
- Strong: `instagram_owned_posts_2026-07-09_run-03`

---

### BP-EVD-003 — Link claims to sources and transformations

Every executive claim or governed metric MUST link to:

- Source IDs
- Dataset version
- Transformation version
- Metric ID
- Capture window
- Sample size
- Confidence/caveat

---

### BP-EVD-004 — Preserve correction history

When evidence is corrected, SHOULD supersede the previous version rather than erase it silently.

The correction record should identify:

- Old value/version
- New value/version
- Reason
- Affected claims
- Downstream updates

---

### BP-EVD-005 — Review freshness before reuse

Before using existing evidence in a “current” claim, MUST check its freshness policy and capture date.

---

## 9. Canonical Data and Dataset Promotion

### BP-CAN-001 — Use a canonical manifest

Governed builds MUST begin from a versioned manifest.

```yaml
manifest_id: ""
version: ""
approved_by: ""
created_at: ""
inputs:
  - dataset_id: ""
    path: ""
    checksum: ""
    schema_version: ""
    grain: ""
    window: ""
    status: canonical
```

---

### BP-CAN-002 — Do not select by convenience

MUST NOT choose canonical input solely because it is:

- Newest
- Largest
- Most polished
- Used by the final report
- Easiest to parse

Selection needs decision relevance, completeness, method quality, and approval.

---

### BP-CAN-003 — Preserve non-canonical generations

Older or alternate generations SHOULD remain available for audit, migration, and comparison, clearly marked non-canonical.

---

### BP-CAN-004 — Promote only after validation

Dataset promotion MUST require:

- Schema pass
- Grain/identity pass
- Duplicate pass
- Window/population check
- Transformation report
- Rights/privacy check
- Owner approval
- Downstream compatibility check

---

### BP-CAN-005 — Record supersession

The manifest MUST identify what the new canonical generation supersedes and why.

---

### BP-CAN-006 — Reconcile counts before executive use

Conflicting social, voice, creator, catalog, media, and spend counts MUST be reconciled or visibly scoped before publication.

---

## 10. Data Modeling and Schema Design

### BP-MOD-001 — Define one-row meaning

Every table or collection MUST state:

> One row/object represents ______.

If the sentence contains “or,” the grain is probably mixed.

---

### BP-MOD-002 — Model product, variant, and SKU separately

For catalog work, SHOULD define:

- Product identity
- Variant identity
- SKU identity
- Option type and value
- Parent-child relationships
- Availability and price grain

MUST NOT assume `option1` is size.

---

### BP-MOD-003 — Use stable identities

Keys SHOULD survive sorting, reprocessing, and title changes.

Avoid display names, array positions, ranks, and mutable URLs as sole identifiers.

---

### BP-MOD-004 — Validate relationships

MUST test:

- Uniqueness
- Required fields
- Referential integrity
- Cardinality
- Orphans
- Duplicate relationships

---

### BP-MOD-005 — Version schemas

Schema changes MUST declare:

- Version
- Compatibility
- Migration
- Consumer impact
- Validation changes
- Rollback

---

### BP-MOD-006 — Separate raw, normalized, and presentation models

**Raw:** source-preserving.

**Normalized:** controlled entities and classifications.

**Presentation:** card/page-ready structures.

MUST NOT use presentation convenience to mutate raw meaning.

---

### BP-MOD-007 — Define locale contracts

The model SHOULD define:

- Timezone
- Currency
- Number format
- Language
- Text direction
- Date format
- Unit conventions

For this project, Africa/Cairo and EGP-related behavior must be explicit when implementation begins.

---

## 11. Metric Definition and KPI Governance

### BP-MET-001 — Create the metric record before code

Every governed metric MUST exist in a registry before TypeScript, Python, or DAX implementation.

Required fields:

```yaml
metric_id: ""
name: ""
question: ""
formula: ""
numerator: ""
denominator: ""
aggregation: ""
grain: ""
population: ""
filters: []
unit: ""
source_ids: []
minimum_sample: null
window: ""
target: null
thresholds: []
confidence_rule: ""
owner: ""
caveat: ""
```

---

### BP-MET-002 — Name aggregation explicitly

MUST identify mean, median, sum, count, maximum, percentile, rate, or ratio.

MUST NOT describe peak-to-median as median-to-median.

---

### BP-MET-003 — Normalize platform vocabulary

Views, plays, reach, impressions, likes, comments, saves, shares, followers, and interactions MUST retain their platform-specific definitions or be explicitly normalized.

---

### BP-MET-004 — Define targets before gauges

A gauge or red/amber/green state MUST have an approved target and threshold logic.

No target means no governed gauge.

---

### BP-MET-005 — Use fixtures

Every metric SHOULD have a small test dataset with expected output and edge cases:

- Empty
- Zero
- Null
- Duplicate
- Small sample
- Extreme outlier
- Mixed platform
- Stale window

---

### BP-MET-006 — Keep `n`, window, and confidence close

Important KPI cards SHOULD disclose sample, capture window, and confidence without requiring repository access.

---

### BP-MET-007 — Establish parity

React and Power BI MUST pass equivalent metric fixtures before governed release.

---

### BP-MET-008 — Review metric changes as product changes

Changing a formula requires decision review, versioning, migration, updated copy, updated targets, and downstream propagation.

---

## 12. Analysis and Interpretation

### BP-ANA-001 — Separate observation from explanation

Analysis SHOULD use this pattern:

```text
Observed evidence
→ Derived measure
→ Interpretation
→ Alternative explanations
→ Decision implication
→ Confidence and limitation
```

---

### BP-ANA-002 — Test alternative explanations

For claims such as Arabic outperforming English, SHOULD consider:

- Platform
- Format
- Post age
- Creator versus owned
- Paid versus organic
- Product category
- Season
- Sample size

---

### BP-ANA-003 — Avoid causal language from observational data

Use “associated with,” “coincides with,” or “suggests” unless the design supports causation.

---

### BP-ANA-004 — Keep qualitative methods qualitative

Verbatims and theme coding SHOULD not be presented as population percentages without appropriate sampling and coding reliability.

---

### BP-ANA-005 — Validate models on project-relevant samples

Sentiment and intent methods SHOULD be evaluated using Cielito/Egyptian Arabic examples, not unrelated brand contexts.

---

### BP-ANA-006 — Report fallback behavior

If a model falls back to rules, keywords, or another engine, the output MUST expose the engine and confidence.

---

### BP-ANA-007 — Preserve disconfirming evidence

Analysis SHOULD include evidence that weakens the preferred narrative.

---

## 13. Decision Governance

### BP-DEC-001 — Use decision records

Binding choices MUST record:

- ID
- Date
- Owner
- Approver
- Status
- Statement
- Evidence
- Alternatives
- Rationale
- Consequences
- Dependencies
- Implementation proof
- Review/reopen condition

---

### BP-DEC-002 — Separate decision status from implementation

Use controlled states such as:

- Accepted
- Specified
- Pending approval
- Client required
- Founder gated
- Deferred
- Dropped
- Superseded
- Implemented
- Validated

---

### BP-DEC-003 — Record supersession

A later decision MUST link to the previous record it replaces.

Example: Noon retry recommendation → later dropped instruction.

---

### BP-DEC-004 — Give persistent decisions review triggers

Review when:

- New client data arrives
- Founder confirms identity/material claims
- Canonical metric changes
- Season/campaign ends
- Implementation contradicts specification
- Evidence becomes stale

---

### BP-DEC-005 — Do not infer owner approval

A polished final strategy does not prove client or founder acceptance.

---

### BP-DEC-006 — Link decisions to monitoring

Every operational decision SHOULD identify the metric or evidence used to evaluate it.

---

## 14. Product Scope and Acceptance Criteria

### BP-PRD-001 — Write an approved product brief

Before implementation, MUST decide:

- Launch target: React, Power BI, both, export-only, or another bounded form
- Primary and secondary users
- Release type: public, client-only, agency-internal
- MVP pages
- Excluded pages/features
- Read-only versus editable behavior
- Authentication
- Refresh model
- Export behavior
- Evidence behavior
- Acceptance criteria

---

### BP-PRD-002 — Prioritize user decisions

Every MVP feature SHOULD map to a user decision or evidence requirement.

---

### BP-PRD-003 — Define intentional boundaries

A read-only MVP, manual refresh, no database, or limited pages MAY be acceptable if approved and documented.

---

### BP-PRD-004 — Define non-goals

Explicit non-goals prevent every repository idea from becoming MVP scope.

---

### BP-PRD-005 — Define success before build

Acceptance criteria SHOULD cover:

- Business usefulness
- Metric correctness
- Evidence access
- Missing-data behavior
- Accessibility
- RTL/responsiveness
- Performance
- Privacy/security
- Deployment/recovery

---

### BP-PRD-006 — Validate with real tasks

User review SHOULD test tasks such as:

- Identify the three priority decisions
- Explain a KPI’s source and caveat
- Find a high-performing post
- Inspect catalog hygiene
- Identify what data is required for revenue

---

## 15. Dashboard Information Architecture

### BP-IA-001 — Preserve the L0–L3 hierarchy

Unless approved otherwise:

- L0: persistent orientation
- L1: executive story
- L2: diagnostic rooms
- L3: evidence

---

### BP-IA-002 — Use progressive disclosure

Summary cards SHOULD not contain every formula and row. Evidence MUST remain reachable.

---

### BP-IA-003 — Give each page one purpose

Each page MUST state:

- Primary user
- Decision/question
- Required data
- Key actions
- Evidence route
- Empty/error behavior

---

### BP-IA-004 — Keep navigation terms client-safe

Internal protocol labels SHOULD be translated or contained in evidence/admin views.

---

### BP-IA-005 — Make active context visible

Users SHOULD see active platform, date, language, population, and comparison state.

---

### BP-IA-006 — Design evidence paths explicitly

A KPI, chart, or claim SHOULD link to the relevant source records and methodology in no more than two intentional interactions.

---

### BP-IA-007 — Review persistent content for staleness

Decision Dock and executive narrative MUST carry version/review state.

---

## 16. Chart and Card Design

### BP-CHT-001 — Start with the question

Write the business question before selecting chart type.

---

### BP-CHT-002 — Select encoding by task

- Comparison: bar/dot
- Trend: line
- Distribution: histogram/box plot
- Relationship: scatter
- Composition: stacked bars when comparison remains readable
- Detailed inspection: table
- Geographic: map only when location is decision-relevant

---

### BP-CHT-003 — Use one primary message

A chart SHOULD have one insight-led title and one “So what?” statement.

---

### BP-CHT-004 — Label unusual scales

Logarithmic, indexed, normalized, or broken axes MUST be obvious and explained.

---

### BP-CHT-005 — Show sources and caveats

Card footer SHOULD include source, `n`, window, confidence, and snapshot/trend state.

---

### BP-CHT-006 — Use semantic colors

MUST preserve ownership, sentiment, and missing-state meaning across targets and exports.

---

### BP-CHT-007 — Provide non-visual alternatives

Important charts SHOULD have summaries and accessible tables where practical.

---

### BP-CHT-008 — Do not optimize for card count

A card without decision or evidence value SHOULD be removed, even if the tab target is not reached.

---

### BP-CHT-009 — Design all data states

Cards MUST handle:

- Valid value
- Zero
- Unknown
- Not applicable
- RequiresData
- Blocked
- Stale
- Partial
- Validation error
- System error

---

## 17. Design-System Practice

### BP-DES-001 — Separate primitive and semantic tokens

Examples:

- Primitive: `terracotta-600`
- Semantic: `data-earned-primary`

---

### BP-DES-002 — Approve tokens against real brand assets

MUST NOT convert provisional creative language into canonical tokens without design/brand approval.

---

### BP-DES-003 — Define component anatomy and states

Every component SHOULD specify:

- Purpose
- Content slots
- Variants
- States
- Responsive behavior
- RTL behavior
- Accessibility behavior
- Source/evidence behavior

---

### BP-DES-004 — Version the design system

Token and component changes SHOULD have versions, owners, change notes, and migration impact.

---

### BP-DES-005 — Maintain cross-target semantic mapping

React theme, Power BI theme, PDFs, and presentations SHOULD share semantic meanings even when exact implementation differs.

---

### BP-DES-006 — Use non-color cues

Sentiment, ownership, confidence, and missing states MUST also use labels, icons, patterns, or line styles.

---

## 18. Accessibility, RTL, and Responsive Practice

### BP-ACC-001 — Choose a standard

The product MUST select an accessibility acceptance standard before release.

---

### BP-ACC-002 — Test keyboard and focus behavior

All controls, modals, drawers, tables, evidence links, and filters MUST be keyboard accessible with visible focus.

---

### BP-ACC-003 — Test chart comprehension

Charts SHOULD provide text summaries and meaningful accessible names. Critical insights MUST not depend only on hover.

---

### BP-RTL-001 — Use logical layout properties

Use start/end rather than hardcoded left/right where possible.

---

### BP-RTL-002 — Test mixed-direction content

Test Arabic and English with:

- Numbers
- Currency
- Percentages
- Handles
- URLs
- Product codes
- Dates
- Parentheses

---

### BP-RSP-001 — Define breakpoints by task

Breakpoints SHOULD reflect when layouts stop supporting user tasks, not arbitrary device labels alone.

---

### BP-RSP-002 — Create mobile alternatives

Wide tables, comparison charts, and persistent docks MAY require cards, horizontal scrolling, summaries, or collapsible structures.

---

### BP-RSP-003 — Test real content extremes

Test long Arabic labels, missing thumbnails, large values, many filters, and empty states.

---

## 19. Media and Creative Practice

### BP-MED-001 — Use real factual media

Real product/founder/creator media SHOULD be used when the visual represents current reality.

---

### BP-MED-002 — Store provenance and rights

Every asset MUST have:

- Asset ID
- Origin
- Creator/owner
- Permission/license
- Attribution
- Intended use
- Duration/territory
- Modification rights
- Synthetic status
- Review/expiry

---

### BP-MED-003 — Preserve synthetic disclosure

Synthetic labels MUST survive dashboard, PDF, presentation, export, and client handoff.

---

### BP-MED-004 — Avoid unverified visual claims

Generated workshop, founder, material, sustainability, or product imagery MUST NOT imply confirmed facts.

---

### BP-MED-005 — Use local approved assets

Presentation systems SHOULD consume validated local assets or approved asset storage, not fragile hotlinks.

---

## 20. Compiler and Data-Contract Practice

### BP-CMP-001 — Build the compiler after truth contracts

Compiler implementation MUST wait for:

- Canonical manifest
- Entity/grain definitions
- Schema registry
- Metric registry
- Rights/privacy rules
- Product output contract
- Acceptance criteria

---

### BP-CMP-002 — Define inputs explicitly

Compiler input config SHOULD list required, optional, and forbidden sources.

---

### BP-CMP-003 — Validate before transform and after emit

Stages SHOULD include:

1. Input existence/checksum
2. Schema validation
3. Identity/grain validation
4. Transformation
5. Metric generation
6. Claim/media/vocabulary validation
7. Output schema validation
8. Build report
9. Atomic promotion

---

### BP-CMP-004 — Separate errors and warnings

Stop-ship errors block output. Warnings remain visible in the build report and dashboard state where relevant.

---

### BP-CMP-005 — Emit version metadata

Compiled output MUST identify:

- Build ID
- Compiler version
- Manifest version
- Metric-registry version
- Design-contract version where relevant
- Created time
- Validation status

---

### BP-CMP-006 — Preserve last known good

Invalid new input MUST NOT overwrite the previous valid contract.

---

### BP-CMP-007 — Produce actionable diagnostics

Errors SHOULD name file, record, field, rule, severity, and suggested resolution.

---

### BP-CMP-008 — Test deterministic output

Repeated compilation of the same inputs SHOULD produce equivalent hashes except declared timestamps.

---

## 21. React Implementation Practice

### BP-REA-001 — Consume only the compiled contract

MUST NOT import heterogeneous research files into presentation components.

---

### BP-REA-002 — Organize by business feature

Prefer feature modules such as:

- Command
- Social
- Catalog
- Website
- Competitive
- Audience
- Content
- Strategy
- Evidence

---

### BP-REA-003 — Centralize semantic components

Create reusable components for:

- KPI cards
- Chart cards
- RequiresData
- Source footer
- Evidence drawer
- Confidence badge
- Stale state
- Error/blocked state

---

### BP-REA-004 — Keep metrics out of UI components

Components SHOULD receive governed values and metadata rather than calculate business metrics independently.

---

### BP-REA-005 — Model state intentionally

Separate:

- Server/compiled data
- Global filters
- Route state
- Component state
- Modal/drawer state
- Language/direction

---

### BP-REA-006 — Use shareable state where valuable

Filters and selected evidence MAY be represented in URLs when privacy permits.

---

### BP-REA-007 — Test all states

Every component MUST be tested with real, empty, zero, missing, stale, blocked, partial, and error fixtures.

---

### BP-REA-008 — Optimize after correctness

Performance work SHOULD preserve evidence, accessibility, and semantic behavior.

---

## 22. Power BI Implementation Practice

### BP-PBI-001 — Confirm fact grain first

Do not write DAX until fact-table grain and relationships are approved.

---

### BP-PBI-002 — Use a controlled semantic model

Dimensions SHOULD include date, platform, source, evidence/confidence, and approved business categories.

---

### BP-PBI-003 — Centralize measures

Measures MUST map to metric-registry IDs and include descriptions.

---

### BP-PBI-004 — Avoid ambiguous relationships

Prefer single-direction, one-to-many relationships unless a documented case requires otherwise.

---

### BP-PBI-005 — Define refresh and workspace governance

Before release, MUST define:

- Workspace
- License
- Dataset owner
- Gateway if needed
- Refresh cadence
- Failure alert
- RLS/access
- Export policy

---

### BP-PBI-006 — Validate RequiresData behavior

Unavailable metrics MUST remain labeled and must not become blanks or zeros through DAX.

---

### BP-PBI-007 — Test React parity

Where both targets exist, equivalent filters and fixtures MUST produce equivalent governed values.

---

### BP-PBI-008 — Document visual interactions

Cross-filtering, drill-through, tooltip, and slicer behavior SHOULD be documented and tested.

---

## 23. Testing and Quality Assurance

### BP-QA-001 — Build a layered test strategy

The project SHOULD include:

- Source/manifest tests
- Schema tests
- Grain and identity tests
- Transformation tests
- Metric fixtures
- Compiler negative tests
- Component tests
- Interaction tests
- React/PBI parity tests
- Accessibility tests
- RTL/responsive tests
- Security/permission tests
- Deployment smoke tests

---

### BP-QA-002 — Map tests to acceptance criteria

Every acceptance criterion MUST have one or more validation methods.

---

### BP-QA-003 — Use representative fixtures

Fixtures SHOULD include Egyptian Arabic, mixed direction, extreme values, missing media, conflicting data, and small samples.

---

### BP-QA-004 — Test failure paths

MUST test what happens when:

- Source is missing
- Schema changes
- Metric unresolved
- Permission absent
- Media lacks rights
- Data stale
- Compiler interrupted
- Deployment fails

---

### BP-QA-005 — Require review of semantic changes

Formula, grain, category, confidence, and source-grade changes require data/product review even when code tests pass.

---

### BP-QA-006 — Preserve test evidence

Release records SHOULD link to test run, commit, fixture/version, result, reviewer, and exceptions.

---

### BP-QA-007 — Do not call narrow audits comprehensive

A specific security or performance check MUST be described by its tested scope.

---

## 24. Prompt and AI-Agent Practice

### BP-AI-001 — Use modular prompt layers

Recommended order:

```text
Authority
→ Permission
→ Task
→ Trusted context
→ Untrusted evidence
→ Output schema
→ Validation
→ Execution
→ Audit
```

---

### BP-AI-002 — Version prompts and models

Governed AI output MUST record prompt ID/version, model/runtime, parameters where available, tools, inputs, and output validator.

---

### BP-AI-003 — Treat evidence as untrusted content

Webpages, comments, transcripts, product text, metadata, and images MUST NOT override instructions or grant tool authority.

---

### BP-AI-004 — Require structured outputs

Machine-consumed outputs SHOULD use schemas and enumerated statuses.

---

### BP-AI-005 — Validate before use

AI output SHOULD be checked for:

- Required fields
- Source support
- Evidence class
- Hallucinated claims
- PII
- Rights
- Banned/internal vocabulary
- Permission violations

---

### BP-AI-006 — Log fallback and uncertainty

Model fallbacks and low-confidence classifications MUST remain visible.

---

### BP-AI-007 — Use bounded context

Load the minimum context pack and avoid mixing unrelated task authority.

---

### BP-AI-008 — Prefer blocked reports to invention

When missing authority or data prevents completion, complete safe parts and name exact blockers.

---

### BP-AI-009 — Keep generated creative factuality-safe

Creative prompts MUST separate concept from current product/founder/manufacturing truth.

---

## 25. Permission and External-Collection Practice

### BP-PER-001 — Assign a permission level

Every task SHOULD declare one maximum level:

1. Read
2. Local analysis/derive
3. Documentation write
4. Code write
5. Free external call
6. Paid external call
7. Client-data handling
8. Creative generation
9. Preview deployment
10. Production deployment
11. Decision mutation

---

### BP-PER-002 — Use route-specific approval

Paid/free collection approval MUST identify:

- Route ID
- Target
- Purpose
- Estimated and maximum cost
- Data categories
- PII level
- Retention
- Approver
- One-time/recurring
- Retry policy

---

### BP-PER-003 — Recheck stale approvals

Approval SHOULD expire when target, cost, data category, or time window changes materially.

---

### BP-PER-004 — Separate preview and production

A preview deployment approval MUST NOT authorize production.

---

### BP-PER-005 — Record actual spend

External calls SHOULD update a canonical spend ledger with estimated versus actual cost.

---

### BP-PER-006 — Do not revive dropped work

A dropped route requires a new explicit decision before retry.

---

## 26. Security, Privacy, PII, and Rights Practice

### BP-SEC-001 — Use least privilege

Users, services, agents, and environments SHOULD receive only the access required for the task.

---

### BP-SEC-002 — Keep secrets in secret storage

MUST NOT place secrets in:

- URLs
- Source files
- Prompts
- Logs
- Screenshots
- Generated reports
- PR descriptions

Use runtime injection and rotation.

---

### BP-SEC-003 — Complete private-data governance first

Before client-data ingestion, MUST approve and implement:

- Purpose limitation
- Access control
- Storage
- Encryption
- Retention
- Deletion
- Tenant/client isolation
- Export control
- Audit logging
- Incident response

---

### BP-SEC-004 — Do not overstate anonymization

Handles, verbatims, URLs, and contextual identifiers are not fully anonymized merely because names are absent.

---

### BP-SEC-005 — Minimize public personal data

Store and display only what is required. Consider aggregation or pseudonymization for client-facing views.

---

### BP-SEC-006 — Maintain rights records

Creator/founder/media use MUST link to permission, attribution, scope, duration, territory, modification, and revocation.

---

### BP-SEC-007 — Gate public claims

Founder, material, manufacturing, sustainability, financial, legal, and security claims MUST have appropriate authority and evidence.

---

### BP-SEC-008 — Design deletion and correction

Evidence systems SHOULD support correction, suppression, and deletion requests without destroying audit history beyond lawful retention needs.

---

## 27. Git, Pull Request, and Documentation Practice

### BP-GIT-001 — One bounded concern per commit

Documentation phases SHOULD use clear commits naming the artifact and phase.

---

### BP-GIT-002 — Verify writes by ref

After creating or updating a file, MUST fetch it from the intended branch and inspect header, status, structure, and critical sections.

---

### BP-GIT-003 — Keep PR history truthful

PR title/body MUST match actual changed phases and current validation state.

---

### BP-GIT-004 — Do not claim merged work is open

Refresh PR state before reporting or updating. If a PR was merged, create a truthful new PR for later work.

---

### BP-GIT-005 — Update descriptions as phases progress

When multiple documentation phases share one open PR, update title/body to include new artifacts and acceptance states.

---

### BP-GIT-006 — Protect production code boundaries

Documentation-only phases MUST NOT include production code changes.

---

### BP-DOC-001 — Link authority, do not duplicate everything

The Project Brain should summarize and route. Specialist docs should contain domain detail. Raw evidence should remain separate.

---

### BP-DOC-002 — Preserve exact status language

Use:

- Confirmed
- Unconfirmed
- Specified
- Accepted
- Implemented
- Deployed
- Validated
- Blocked

Avoid vague “ready,” “done,” or “working” without proof.

---

## 28. Deployment and Release Practice

### BP-REL-001 — Define environments

At minimum, SHOULD distinguish local/development, preview/staging, and production where applicable.

---

### BP-REL-002 — Create a release record

A release MUST identify:

```yaml
environment: ""
url: ""
commit: ""
build_artifact: ""
data_manifest: ""
compiler_version: ""
metric_registry_version: ""
validation_result: ""
approver: ""
deployed_at: ""
rollback_target: ""
```

---

### BP-REL-003 — Deploy immutable artifacts

Production SHOULD deploy the exact validated build artifact, not rebuild from moving inputs.

---

### BP-REL-004 — Require release gates

Production release MUST pass:

- Tests
- Data/metric validation
- Accessibility
- Security/access
- Privacy/rights
- Performance target
- Monitoring readiness
- Rollback readiness
- Explicit approval

---

### BP-REL-005 — Smoke test after deploy

Verify route, access, data version, key metrics, evidence links, language/RTL, media, and monitoring.

---

### BP-REL-006 — Roll back on truth failure

A semantically wrong metric or data generation is a valid rollback reason even when the app is technically online.

---

## 29. Observability and Incident Practice

### BP-OBS-001 — Monitor five health layers

1. Application availability
2. Build/compiler health
3. Data freshness and validation
4. Metric parity and anomalies
5. Permission/privacy/rights state

---

### BP-OBS-002 — Alert on stale truth

Alerts SHOULD cover overdue captures, failed compilation, unresolved source references, parity failures, and expired decisions/rights.

---

### BP-OBS-003 — Separate user-safe and operator detail

Users see clear states; operators receive technical context without leaking secrets or PII.

---

### BP-OBS-004 — Record incidents

Incident records SHOULD include:

- Start/end
- Impact
- Detection
- Root cause
- Data/metric versions
- Permission/privacy impact
- Resolution
- Rollback
- Prevention actions

---

### BP-OBS-005 — Correct downstream claims

If an incident affects a published claim, update dashboards, exports, decisions, and client communication as appropriate.

---

## 30. Project Brain, Handoff, and Memory Practice

### BP-MEM-001 — Update Brain on material state changes

Triggers include:

- Phase acceptance
- PR merge/replacement
- Canonical dataset selection
- Metric change
- Client data arrival
- Founder decision
- Route approval/completion/drop
- Build/deployment
- Major risk/gap change

---

### BP-MEM-002 — Keep Brain concise and linked

Summarize current state; link to specialist authority rather than copying all details.

---

### BP-MEM-003 — Use structured handoffs

Every handoff MUST include:

```yaml
project: Cielito 360
repository: omarali304ii-byte/Islam-Brain
branch: ""
commit: ""
pr: ""
phase: ""
task: ""
permission: ""
files_read: []
files_changed: []
decisions_used: []
evidence_used: []
contradictions: []
completed: []
blocked: []
validation: []
next_exact_action: ""
```

---

### BP-MEM-004 — State exact blockers

Do not say “waiting on data.” Name the data, owner, schema, permission, and decision it blocks.

---

### BP-MEM-005 — Record no-change outcomes

A valid task may conclude that no safe change should be made. Record the analysis and reason.

---

## 31. Definition of Ready

A task is ready only when applicable items pass.

### 31.1 Universal readiness

- [ ] Task and deliverable are explicit.
- [ ] Repository/branch/PR state confirmed.
- [ ] Permission level resolved.
- [ ] Inputs and authority identified.
- [ ] Relevant decisions and gaps reviewed.
- [ ] Excluded actions named.
- [ ] Acceptance criteria defined.

### 31.2 Data/metric readiness

- [ ] Canonical input selected.
- [ ] Grain and keys defined.
- [ ] Schema available.
- [ ] Metric contract approved.
- [ ] Sample/window/freshness known.
- [ ] Rights/privacy state acceptable.

### 31.3 UI readiness

- [ ] Product target and MVP approved.
- [ ] Compiled contract available.
- [ ] Design tokens/components approved or explicitly temporary.
- [ ] States defined.
- [ ] Accessibility/RTL/responsive criteria defined.

### 31.4 Collection readiness

- [ ] Research question defined.
- [ ] Route and target approved.
- [ ] Cost ceiling set.
- [ ] Data categories and PII level known.
- [ ] Retention and retry rules set.

### 31.5 Deployment readiness

- [ ] Build validated.
- [ ] Environment/access defined.
- [ ] Monitoring and rollback ready.
- [ ] Production approver explicit.

If a required item fails, the task is not ready; produce a blocked report or bounded preparatory work.

---

## 32. Definition of Done

A task is done only when applicable items pass.

### 32.1 Universal completion

- [ ] Deliverable exists at the intended target.
- [ ] Scope and exclusions respected.
- [ ] Acceptance criteria tested.
- [ ] No unsupported claims introduced.
- [ ] Validation evidence recorded.
- [ ] Downstream records updated.
- [ ] Handoff completed.

### 32.2 Data/metric completion

- [ ] Transformation reproducible.
- [ ] Manifest/schema/metric versions recorded.
- [ ] Edge cases tested.
- [ ] Source/sample/window/confidence exposed.
- [ ] React/PBI parity tested where applicable.

### 32.3 UI completion

- [ ] All data states implemented.
- [ ] Keyboard/accessibility tested.
- [ ] RTL/mixed direction tested.
- [ ] Responsive tasks tested.
- [ ] Evidence route tested.
- [ ] Performance acceptance passed.

### 32.4 Deployment completion

- [ ] Exact artifact deployed.
- [ ] Release record created.
- [ ] Smoke test passed.
- [ ] Monitoring active.
- [ ] Rollback target verified.
- [ ] Brain status updated.

“Code merged” is not equivalent to “product done.”

---

## 33. Stage Checklists

### 33.1 Before research

- Decision question
- Source and population
- Permission
- Cost/retention
- Required fields
- Stop/retry conditions
- Raw-capture plan

### 33.2 Before analysis

- Canonical generation or scoped dataset
- Grain and population
- Transformation audit
- Missingness and duplicates
- Model/fallback version
- Alternative explanations

### 33.3 Before metric publication

- Registry record
- Formula fixture
- Aggregation/population
- Source and window
- Target if visualized as gauge
- Confidence and caveat
- Cross-target parity

### 33.4 Before UI implementation

- Approved MVP
- Validated contract
- Design/system states
- Accessibility/RTL/responsive criteria
- Media rights
- Test plan

### 33.5 Before merge

- Correct branch
- Tests passed
- No secrets/PII
- Scope respected
- Documentation and contracts updated
- PR description truthful
- Review complete

### 33.6 Before preview deployment

- Preview approval
- Environment config
- Test artifact
- Access controls
- Data version
- Monitoring/smoke plan

### 33.7 Before production deployment

- Explicit production approval
- Release gates passed
- Immutable artifact
- Rollback target
- Monitoring/incident owner
- Release record ready

### 33.8 After deployment

- Smoke tests
- Data/metric version verification
- Evidence links
- Accessibility/RTL spot checks
- Monitoring confirmation
- Brain/handoff update

---

## 34. Review Checklists by Role

### Product reviewer

- Does every feature serve a named user decision?
- Are non-goals explicit?
- Are RequiresData states honest?
- Are acceptance criteria testable?
- Is the Decision Dock current?

### Data reviewer

- Are grain, keys, schema, manifest, and metric registry valid?
- Can every KPI be reproduced?
- Are generations and windows explicit?
- Are transformations audited?

### Design reviewer

- Is hierarchy decision-first?
- Is semantic meaning consistent?
- Are all states designed?
- Are accessibility, RTL, and mobile tasks addressed?
- Are media facts and rights safe?

### Engineering reviewer

- Does presentation consume only validated contracts?
- Are failures safe and actionable?
- Are dependencies/configuration controlled?
- Are reruns atomic/idempotent?
- Are tests meaningful?

### Privacy/security reviewer

- Is personal/client data minimized and governed?
- Are secrets protected?
- Is access least-privilege?
- Are rights and retention documented?
- Could output make an unapproved claim?

### Executive reviewer

- Is the verdict supported?
- Are decisions approved and current?
- Are caveats understandable?
- Are financial claims honest?
- Is the next action owned?

---

## 35. Practice Templates

### 35.1 Research route record

```yaml
route_id: ""
question: ""
decision_supported: ""
target: ""
source_class: ""
permission: ""
estimated_cost: 0
maximum_cost: 0
data_categories: []
pii_level: ""
retention: ""
retry_policy: ""
owner: ""
approver: ""
status: "proposed | approved | running | complete | partial | blocked | deferred | dropped"
```

### 35.2 Canonical promotion record

```yaml
dataset_id: ""
version: ""
grain: ""
window: ""
schema: ""
checksum: ""
quality_results: []
supersedes: []
rationale: ""
owner: ""
approver: ""
promoted_at: ""
```

### 35.3 Metric record

Use the structure from BP-MET-001.

### 35.4 Implementation proof

```yaml
requirement_or_decision: ""
implementation:
  commit: ""
  files: []
  environment: ""
validation:
  tests: []
  result: ""
reviewer: ""
limitations: []
```

### 35.5 Gap closure record

```yaml
gap_id: ""
closed_at: ""
owner: ""
approver: ""
resolution: ""
evidence: []
downstream_updates: []
remaining_limitations: []
review_or_expiry: null
```

### 35.6 Principle deviation

```yaml
principle_id: ""
scope: ""
reason: ""
evidence: []
benefit: ""
risk: ""
mitigation: ""
owner: ""
approver: ""
expires_at: ""
validation: ""
```

---

## 36. Common Failure Patterns

### Failure 1 — UI-first implementation

**Symptom:** Components are built directly from `_intel` files.

**Consequence:** Data generations, metrics, and identities become hardcoded inconsistently.

**Correction:** Stop production implementation; establish manifest, schemas, registry, and compiler.

---

### Failure 2 — Dramatic metric optimization

**Symptom:** The most persuasive comparison becomes the headline without a stable formula.

**Consequence:** Executive narrative becomes materially misleading.

**Correction:** Freeze/caveat, define formula, reproduce, test, and propagate.

---

### Failure 3 — Specification inflation

**Symptom:** Detailed docs are reported as working software.

**Consequence:** Planning and stakeholder trust fail.

**Correction:** Require implementation/deployment/validation proof.

---

### Failure 4 — Silent canonical selection

**Symptom:** One of several datasets is used without a manifest.

**Consequence:** Different contributors produce different “official” results.

**Correction:** Preserve generations and run approval-based promotion.

---

### Failure 5 — Unknown-to-zero conversion

**Symptom:** Missing financial or demographic values render as zero.

**Consequence:** Absence is misread as measured poor performance.

**Correction:** Model state separately and use RequiresData.

---

### Failure 6 — Public-data overconfidence

**Symptom:** Handles, comments, and creator media are reused freely.

**Consequence:** Privacy, platform, rights, and reputation exposure.

**Correction:** Minimize, govern retention, and obtain rights.

---

### Failure 7 — Permission collapse

**Symptom:** One short command includes collection, spending, code writes, and deployment.

**Consequence:** Unauthorized side effects.

**Correction:** Separate task and permission layers with route-specific approval.

---

### Failure 8 — Accessibility afterthought

**Symptom:** Accessibility review begins after visual completion.

**Consequence:** Components and charts require expensive redesign.

**Correction:** Include criteria and test fixtures from product/design start.

---

### Failure 9 — Stale persistent strategy

**Symptom:** Decision Dock remains unchanged after new evidence.

**Consequence:** Dashboard confidently recommends outdated actions.

**Correction:** Version decisions and review on evidence events.

---

### Failure 10 — Vague handoff

**Symptom:** “Continue the dashboard with latest data.”

**Consequence:** Rediscovery, wrong generation, and permission ambiguity.

**Correction:** Use structured handoff with exact branch, files, versions, and blocker.

---

## 37. Exception and Deviation Practice

### 37.1 When deviation may be reasonable

Examples:

- Manual refresh for a bounded pitch MVP
- No database for a compile-time snapshot
- One presentation target before the other
- Temporary tokens for an internal prototype
- Partial output with explicit RequiresData states

### 37.2 Required deviation record

Any deviation from a MUST/SHOULD practice should include the template in Section 35.6.

### 37.3 Expiry

Temporary deviations SHOULD have an expiry or reopen condition.

### 37.4 No deviation by silence

A practice is not waived because nobody mentioned it during implementation.

---

## 38. Maturity Model

### Level 0 — Ad hoc

- Files and claims exist without controlled contracts.
- Manual knowledge drives work.
- No reliable readiness proof.

### Level 1 — Documented

- Principles, decisions, gaps, and architecture are written.
- Current Cielito DIOS documentation is largely at this level.

### Level 2 — Controlled

- Owners assigned.
- Canonical manifest, schemas, metric registry, permissions, and product brief exist.
- Required P0 gaps are closed with proof.

### Level 3 — Implemented

- Compiler and selected presentation target exist.
- Tests, accessibility, RTL, security, and parity controls operate.

### Level 4 — Operational

- CI/CD, monitoring, rollback, freshness, incident response, and client-data controls function.

### Level 5 — Learning system

- Evidence, decisions, metrics, and practices are reviewed continuously.
- Change propagation is automated or reliably governed.
- The Project Brain stays current without rediscovery.

### 38.1 Current truthful placement

The repository has strong **documented** maturity and partial evidence practices, but remains blocked from controlled/implemented product maturity by P0 gaps.

---

## 39. Principle and Gap Traceability

| Practice domain | Main Phase 10 principles | Main Phase 8 gaps |
|---|---|---|
| Entry/scoping | DP-OPS-005, DP-SEC-001 | Governance/permission gaps |
| Evidence | DP-TRU-001 to 008 | `GAP-EVD-*` |
| Canonical data | DP-DAT-001, 002, 005, 006 | `GAP-DAT-*` |
| Metrics | DP-DAT-003, 004, 007 | `GAP-MET-*` |
| Product/decisions | DP-DEC-001 to 006 | `GAP-BIZ-*`, `GAP-GOV-*`, `GAP-PRD-*` |
| Dashboard/design | DP-IA-*, DP-VIS-* | `GAP-PRD-*`, `GAP-DES-*` |
| Compiler/engineering | DP-ENG-* | `GAP-ENG-*` |
| AI/prompts | DP-AI-* | Prompt debt, `GAP-OPS-001/002` |
| Security/rights | DP-SEC-* | `GAP-SEC-*`, `GAP-CNV-003` |
| Release/operations | DP-OPS-* | `GAP-OPS-*` |

### 39.1 High-leverage practice bundles

One artifact or workflow may close multiple gaps:

- **Canonical manifest bundle:** dataset generation, lineage, freshness, spend, promotion.
- **Metric registry bundle:** formulas, targets, parity, chart labels, fixtures.
- **Product brief bundle:** target, MVP, access, editability, acceptance criteria.
- **Privacy/rights bundle:** client data, PII, creator media, retention, deletion.
- **Compiler bundle:** schemas, validation, deterministic output, last known good.
- **Release bundle:** CI/CD, environments, monitoring, rollback, approval.

---

## 40. Phase 11 Validation Gate

### 40.1 Completeness

- [x] Best practices cover project entry, research, evidence, provenance, canonical data, modeling, metrics, analysis, decisions, product, IA, charts, design, accessibility, RTL, responsive behavior, media, compiler, React, Power BI, testing, AI, permissions, security, privacy, rights, Git, deployment, observability, and memory.
- [x] Definition of Ready and Definition of Done are documented.
- [x] Stage and role checklists are documented.
- [x] Templates are included.
- [x] Failure patterns and deviation practice are documented.
- [x] Maturity model and traceability are documented.

### 40.2 Principle alignment

- [x] Practices operationalize Phase 10 principles.
- [x] Practices preserve the Phase 8 stop-ship boundary.
- [x] Practices retain Phase 6 decision statuses and Phase 7 authority model.
- [x] Practices use the Phase 9 learning concepts correctly.

### 40.3 Evidence and safety

- [x] No best practice is represented as currently implemented without proof.
- [x] No gap was marked closed.
- [x] No canonical dataset, metric formula, target, owner, launch choice, right, or approval was invented.
- [x] No production code changed.
- [x] No external collection, client-data ingestion, media generation, build, or deployment occurred.

### 40.4 Quality result

**Phase 11 result:** PASS — PROJECT BEST-PRACTICE OPERATING STANDARD ESTABLISHED.

The repository now contains both the durable principles and the repeatable procedures required to guide later Dashboard Bible, Master Prompt, and Roadmap work.

### 40.5 Phase transition

Phase 12 (`12_Dashboard_Bible.md`) remains blocked until the repository owner validates or explicitly advances beyond Phase 11.

---

## 41. Glossary

| Term | Meaning |
|---|---|
| Best practice | Repeatable method that usually produces safer, clearer, or more reliable outcomes |
| Golden path | Preferred end-to-end workflow for governed tasks |
| Definition of Ready | Conditions required before work should begin |
| Definition of Done | Evidence required before work may be called complete |
| Practice strength | MUST, SHOULD, MAY, or MUST NOT classification |
| Practice bundle | Related practices/artifacts that close several gaps together |
| Semantic review | Review of meaning and business correctness, beyond code syntax |
| Release gate | Validation and approval required before deployment |
| Maturity level | Degree to which documented practices are controlled, implemented, and operational |

---

## 42. Document Control

| Field | Value |
|---|---|
| Document | `docs/DIOS/11_Best_Practices.md` |
| Phase | 11 |
| Created | 2026-07-12 |
| Authoring system | DIOS analysis through connected GitHub workflow |
| Repository | `omarali304ii-byte/Islam-Brain` |
| Working branch | `docs/dios-phase-0-inventory` |
| Production code changed | No |
| External actions executed | No |
| Next phase | `12_Dashboard_Bible.md`, pending owner validation |
