# Dashboard Prompt Framework

This directory contains the permanent prompt engineering system for dashboard work.

## Active entry point

```text
prompts/dashboard/DASHBOARD_MASTER_PROMPT_v3.md
```

The framework becomes formally active after owner approval of the pull request containing v3.

## Files

| File | Purpose |
|---|---|
| `manifest.yaml` | Active version, defaults, module registry, lifecycle, review triggers |
| `DASHBOARD_MASTER_PROMPT_v3.md` | Permanent kernel, loader, activation, execution, and project adapter |
| `PROMPT_MODULE_LIBRARY.md` | Reusable modules for product, data, metrics, UX, compiler, React, Power BI, QA, release, memory, and prompt evolution |
| `PROMPT_TEST_SUITE.md` | Adversarial and acceptance tests for prompt behavior |
| `DASHBOARD_MASTER_PROMPT_v2.md` | Transitional monolithic version used for comparison and historical review |
| `docs/DIOS/16_Prompt_Engineering_Review.md` | Complete reverse engineering, critique, philosophy, v2 self-review, v3 rationale, and comparison |

## Historical sources

- `CIELITO_TAB_DEEPENING_MASTER_PROMPT.md`
- `docs/DIOS/05_Prompt_Analysis.md`
- `docs/DIOS/13_Dashboard_Master_Prompt.md`

These remain evidence and history. They are not the permanent activation entry point after v3 approval.

## Quick start

### 1. Read the manifest

Confirm the active framework version and project profile.

### 2. Read v3

Load the kernel and required activation schema.

### 3. Create one activation

Example: prompt-system review only.

```yaml
activation:
  task_id: PROMPT-REVIEW-001
  framework_version: 3.0.0
  project_profile_id: CIELITO-DASHBOARD-PROFILE
  requested_by: Omar Ali
  repository: omarali304ii-byte/Islam-Brain
  branch: prompts/review-example
  base_commit: "<main SHA>"
  mode: PROMPT_ENGINEERING
  modules:
    - M00_AUTHORITY_TRUTH
    - M01_CLAIMS_EVIDENCE
    - M02_ACTIVATION_EFFECTS
    - M03_UNTRUSTED_DATA
    - M04_FAILURE_CONTROL
    - M10_CONTEXT_BOOTSTRAP
    - M19_QUALITY
    - M21_MEMORY_HANDOFF
    - M22_PROMPT_ENGINEERING
  objective: Review one proposed prompt change and update prompt tests.
  deliverables:
    - prompt diff
    - test updates
    - review report
  allowed_paths:
    - prompts/dashboard/**
    - docs/DIOS/**
  prohibited_paths:
    - dashboard implementation
    - raw evidence
    - deployment configuration
  capabilities:
    read_repository: true
    write_documentation: true
    write_code: false
    modify_tests: true
    external_network: false
    free_external_collection: false
    paid_external_collection: false
    client_data: false
    generate_media: false
    preview_deploy: false
    production_deploy: false
    modify_secrets: false
    run_migration: false
    force_push: false
    delete_branch: false
    mutate_decisions: false
  tools:
    - repository read
    - documentation write
  required_inputs:
    - prompts/dashboard/manifest.yaml
    - prompts/dashboard/DASHBOARD_MASTER_PROMPT_v3.md
    - prompts/dashboard/PROMPT_MODULE_LIBRARY.md
    - prompts/dashboard/PROMPT_TEST_SUITE.md
  excluded_actions:
    - dashboard code changes
    - external calls
    - deployment
  approval_gates:
    - owner review before activation
  acceptance_criteria:
    - affected rules identified
    - version impact classified
    - relevant tests updated
    - no permissions broadened silently
  cost_ceiling: 0
  record_ceiling: 0
  retry_ceiling: 0
  approver: Omar Ali
  approval_expiry: null
```

### 4. Load required modules only

Use the mode-to-module table in `PROMPT_MODULE_LIBRARY.md`.

A frontend task does not automatically receive external-network, private-data, preview, or production capabilities.

### 5. Run prompt tests

Use relevant scenarios from `PROMPT_TEST_SUITE.md` before promoting a framework version or using a new high-risk capability.

### 6. Stop at gates

The framework never chains roadmap, architecture, code, migration, preview, and production without explicit approvals.

## Core differences from the original prompt

- No card-count success target.
- `HAVE` replaced with precise lifecycle states.
- Project doctrine separated from universal policy.
- Mode separated from side-effect capabilities.
- External evidence explicitly untrusted.
- Prompt source has versions, rule IDs, tests, and lifecycle.
- No prompt self-modification during execution.
- No automatic phase continuation.
- Critical output requires independent validation.

## Change policy

Prompt changes require:

1. `PROMPT_ENGINEERING` activation.
2. A dedicated branch and PR.
3. Semantic version decision.
4. Rule-ID impact review.
5. Test changes.
6. Owner approval.
7. Manifest and supersession updates.

Do not edit v3 casually during a dashboard implementation task.
