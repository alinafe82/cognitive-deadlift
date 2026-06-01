# Repository Audit

Date: 2026-06-01
Branch: `modernize-skill-retention-harness`

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
| `skills_index.json` | Machine-readable index of `skills/`. Must match `skills/`. |

Each file should answer questions only in its column. If two files answer the same question, the audit must say so here.

## Findings

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
- `skills_index.json` matches the ten directories under `skills/`.
- `.claude-plugin/plugin.json` skill list matches `skills/` (existing check).
- Each skill has `SKILL.md`, two examples, fixtures, and tests/README per the skill standard.

## Skill inventory

Ten skills, all classification B (keep but iterate) from the prior audit; structural validators are passing and the grade rubric reports 94.7 across the board. Concrete boundaries are documented in each `SKILL.md` and `docs/skill-standard.md`.

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

## Next refresh triggers

Update this audit when any of the following happens:

- A skill is added, removed, or its scope shifts.
- A doc swaps roles or a new top-level file appears.
- A harness check is added, removed, or weakened.
- A duplicated source of truth appears.
- A generated artifact starts getting tracked.
