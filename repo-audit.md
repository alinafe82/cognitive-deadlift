# Repository Audit

Date: 2026-07-12
Branch: `main`

This is the standing audit. Refresh it in place rather than starting a new file.

## Purpose

Cognitive Deadlift is a portable skill-retention harness for AI-assisted engineering. It packages reusable skills, a thinking budget policy, context packs, review harness fixtures, runtime adapter manifests for Claude / Codex / Gemini, hooks, and deterministic validation.

It is not a runtime, not a hosted service, not a benchmark, not a generic prompt collection.

## Source-of-truth contract

| File | One job |
| --- | --- |
| `CONTEXT.md` | Repo mission, operating principles, anti-slop rules, validation philosophy, assumptions, glossary. |
| `ARCHITECTURE.md` | Current top-level structure and lifecycles (skill, hook, harness, index). |
| `CATALOG.md` | Index of skills, hooks, scripts, runtime adapters. |
| `README.md` | Public quickstart: install, run checks, use with each agent. |
| `AGENTS.md` | Generic rules for any coding agent working in this repo. |
| `CLAUDE.md` | Claude-specific rules layered on AGENTS.md. |
| `GEMINI.md` | Gemini-specific rules layered on AGENTS.md. |
| `docs/` | Deeper supporting docs (architecture rationale, ADRs, security, skill standard). |
| `policies/` | Risk-based thinking budget. |
| `context-packs/` | Evidence contracts for common AI-assisted workflows. |
| `harnesses/` | Review fixtures for agent failure modes. |
| `repo-audit.md` | This file. Standing audit of duplication, gaps, risks. |
| `productionization-report.md` | Standing prod-readiness status, checks available, commands run, risks. |
| `specs/` | Planning and review documents for repo-level changes. |
| `docs/workflow-audit.md` | Paid workflow audit offer, price, scope, deliverables, and contact path. |
| `docs/workflow-audit-sample.md` | Illustrative buyer-facing sample of the paid audit output shape. |
| `skills_index.json` | Machine-readable index of `skills/`. Must match `skills/`. |

Each file should answer questions only in its column. If two files answer the same question, the audit must say so here.

## Findings

### Resolved in this pass (2026-08-24, local gate entrypoint)

- `make prod-gate` now uses `.venv/bin/python` when the documented `uv sync
  --all-extras` setup has created it, while retaining `python3` for CI and
  system installs. This keeps Ruff and pytest on the same project environment
  as the other validation scripts.

### Resolved in this pass (2026-07-12, all-skills request harness)

- Added `harnesses/all-skills-request` to test whether broad god-mode or
  all-skills requests stay bounded, preserve user work, reject unverifiable
  universal-skill claims, and require configured checks before merge.

### Resolved in this pass (2026-07-21, workflow audit sample)

- Added `docs/workflow-audit-sample.md` as an illustrative deliverable preview for
  teams evaluating the fixed-scope Workflow Audit.
- `docs/workflow-audit.md` now links to the sample and uses a distinct fixed-scope
  section instead of repeating the `Paid Offer` heading.

### Resolved in this pass (2026-07-12, god-mode orchestration skill)

- Added `god-mode` as a bounded orchestration skill for broad requests that need
  explicit skill routing, evidence selection, and verification.
- The skill rejects literal universal-coverage claims and routes work through
  verified local skills instead of replacing the existing catalog.

### Resolved in this pass (2026-08-23, CI/CD productionization)

- CI runs the full gate on the declared Python 3.11 minimum and a compatibility
  test job on Python 3.13, both with lockfile-keyed package caches and a manual
  dispatch path for incident reproduction.
- Every workflow now declares bounded concurrency and immutable action pins.
- Dependabot now covers Python dependencies as well as GitHub Actions.
- Default-branch CI failures reconcile against the latest authoritative run,
  create an automation-labeled owner-assigned issue, and close only after the
  affected workflow recovers. GitHub account notifications remain the email
  delivery channel for failed workflow runs.

### Resolved in this pass (2026-06-24, revenue CTA)

- `docs/workflow-audit.md` now owns the fixed-scope paid Workflow Audit terms.
- `README.md` routes interested teams to that page without duplicating the price or
  scope, keeping the offer terms in one public source of truth.

### Resolved in this pass (2026-06-19, validator hardening)

- Added ten repository-lifecycle skills: `skill-authoring-gate`,
  `skill-overlap-audit`, `runtime-adapter-smoke`, `transcript-review`,
  `thinking-ledger-review`, `evidence-to-test`, `release-readiness`,
  `skill-deprecation-review`, `agent-security-boundary`, and
  `docs-claim-audit`.
- `.github/PULL_REQUEST_TEMPLATE.md` now points reviewers at `make prod-gate`
  instead of the narrower compatibility target.
- `scripts/validate_repo.py` now checks PR template drift and runtime adapter
  name/version metadata against `pyproject.toml`, plus runtime context routing
  for every shared skill.
- `scripts/validate_context_packs.py` and `scripts/validate_harnesses.py` now
  validate custom roots cleanly, which makes negative fixture tests meaningful.
- `scripts/validate_skills.py --slop-only` now scans Markdown, YAML, TOML, and
  JSON contract files instead of Markdown only.
- `.serena/` is ignored as local agent tooling state.
- Validator tests now cover negative cases for policies, context packs, harnesses,
  doctor readiness, runtime adapter drift, PR template drift, and non-Markdown
  slop scanning.

### Resolved in this pass (2026-06-01, skill-retention modernization)

- `README.md` now leads with the skill-retention thesis instead of presenting the repo mainly as a skill package.
- `policies/thinking-budget.yaml` is the source of truth for low / medium / high evidence gates.
- `context-packs/` now defines evidence contracts for bugfix, refactor, repo-review, and risky-change workflows.
- `harnesses/` now contains four review fixtures for ambiguous requests, fake test confidence, overeager refactors, and unsafe tool use.
- `docs/skill-atrophy-taxonomy.md` and `docs/ai-slop-taxonomy.md` provide practical review vocabularies.
- `scripts/validate_policies.py`, `scripts/validate_context_packs.py`, `scripts/validate_harnesses.py`, and `scripts/doctor.py` add deterministic checks for the new contract surfaces.
- Existing skills now name the developer ability they preserve, required evidence, and failure signs.
- `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md` now route work through the thinking budget.

### Resolved in earlier pass (2026-06-01)

- New top-level `specs/` directory added to hold planning documents.

### Resolved in earlier pass (2026-05-31)

- `ARCHITECTURE.md` previously delegated everything to `docs/architecture.md`. It now carries the canonical top-level structure and lifecycles; `docs/architecture.md` keeps the deeper rationale and alternatives.
- `CONTEXT.md` previously held only a glossary. It now leads with mission, principles, anti-slop rules, validation philosophy, and assumptions; glossary remains at the end.
- `Makefile` did not expose the targets the contract names (`prod-gate`, `skills-check`, `docs-check`, `slop-scan`). They now exist and `prod-gate` chains the meaningful checks.
- `validate_repo.py` did not check that `skills_index.json` matches `skills/`, did not check the doc contract, and did not check that generated artifacts stay untracked. It now does.
- `AGENTS.md` did not name the repo contract (read CONTEXT first, update CATALOG when skills change, update ARCHITECTURE only when structure changes, run `make prod-gate` before final). It now does.
- `productionization-report.md` was dated 2026-05-25 and referenced old commands. Refreshed in place.

### Standing risks

- The harness validates structure, not agent behavior. A skill can pass every check and still be ignored by a runtime.
- Harness fixtures are review examples, not benchmark scores.
- Context packs can say what evidence should be present, but they cannot prove the supplied evidence is true.
- External link liveness is not checked; only internal link targets.
- Skill grading uses heuristic scoring. A skill author can game the rubric (lines, bullet counts) without improving substance. Human review remains required for new skills.
- The repo cannot tell whether a thinking ledger is real or fabricated. The pre-commit hook only checks that one is staged.
- `cognitive_deadlift.egg-info/`, `.pytest_cache/`, `.ruff_cache/`, `__pycache__/`, `.venv/` exist in the working tree as expected and are gitignored. The new generated-artifact check enforces that they stay untracked.

### Non-issues confirmed

- No secrets in tracked files (`scripts/security_scan.py` is clean).
- `skills_index.json` matches the twenty-one directories under `skills/`.
- `.claude-plugin/plugin.json` skill list matches `skills/` (existing check).
- `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md` route all twenty-one skills.
- Each skill has `SKILL.md`, two examples, fixtures, and tests/README per the skill standard.
- Local `.serena/` agent state is ignored and excluded from slop scanning.

## Skill inventory

Twenty-one skills are present. The original ten developer-practice skills, the
`god-mode` orchestration skill, and the ten repository-lifecycle skills are
structurally validated. Concrete boundaries are documented in each `SKILL.md`
and `docs/skill-standard.md`.

| Skill | Stage | Distinct from |
| --- | --- | --- |
| `problem-framing` | Before code | `assumption-audit` (this defines, that tests) |
| `assumption-audit` | Before plan acceptance | `problem-framing` (this tests, that defines) |
| `alternatives-before-code` | Before architecture | `complexity-budget` (this compares, that prices) |
| `failing-test-first` | Before fix | `debugging-lab-notebook` (this proves, that investigates) |
| `trace-the-code` | Before edit | (none) |
| `read-the-docs-first` | Before claim | (none) |
| `explain-without-ai` | Before merge | (none) |
| `diff-interrogation` | Before accept | (none) |
| `debugging-lab-notebook` | Hard bugs | `failing-test-first` (this investigates, that proves) |
| `complexity-budget` | Before abstraction | `alternatives-before-code` (this prices, that compares) |
| `god-mode` | Cross-skill orchestration | All narrower skills (this routes and sequences, those perform the work) |
| `skill-authoring-gate` | Before adding or changing a skill | `skill-overlap-audit` (this checks quality, that checks boundaries) |
| `skill-overlap-audit` | Before adding a nearby skill | `skill-authoring-gate` (this checks overlap, that checks readiness) |
| `runtime-adapter-smoke` | Before adapter publication | `release-readiness` (this checks runtime routing, that checks release state) |
| `transcript-review` | After real agent sessions | `diff-interrogation` (this reviews session behavior, that reviews code diffs) |
| `thinking-ledger-review` | Before accepting reasoning evidence | `cognitive_deadlift_check.py` hook (this checks substance, that checks presence) |
| `evidence-to-test` | After a repo gap or repeated failure | `failing-test-first` (this designs the check, that proves behavior before a fix) |
| `release-readiness` | Before tagging or publishing | `runtime-adapter-smoke` (this checks release state, that checks adapter routing) |
| `skill-deprecation-review` | Before removing or merging skills | `skill-overlap-audit` (this decides lifecycle, that maps overlap) |
| `agent-security-boundary` | Before tool-using agent changes | `diff-interrogation` (this checks agent security boundaries, that reviews diffs) |
| `docs-claim-audit` | Before public docs claims merge | `read-the-docs-first` (this audits claims, that gathers sources) |

## Next refresh triggers

Update this audit when any of the following happens:

- A skill is added, removed, or its scope shifts.
- A doc swaps roles or a new top-level file appears.
- A harness check is added, removed, or weakened.
- A duplicated source of truth appears.
- A generated artifact starts getting tracked.
