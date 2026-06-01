# Productionization Report

Date: 2026-06-01

## Summary

Cognitive Deadlift is a portable skill-retention harness. This report tracks readiness status, the checks the harness enforces, the commands run to verify them, and the risks the harness cannot cover.

## Checks available

The validation harness runs structural checks only. It does not evaluate agent behavior or skill quality beyond a heuristic rubric.

| Check | Script | What it enforces |
| --- | --- | --- |
| Repo contract | `scripts/validate_repo.py` | Required files exist, runtime adapter manifests are consistent, `skills_index.json` matches `skills/`, top-level docs each cover their declared sections, no generated artifacts are tracked. |
| Skill structure | `scripts/validate_skills.py` | Each skill has the required folders, frontmatter, sections, examples, and no broken internal links. |
| Thinking budget | `scripts/validate_policies.py` | Low / medium / high policy levels exist with required evidence and examples. |
| Harness fixtures | `scripts/validate_harnesses.py` | Each review fixture has a task, expected behavior, and rubric. |
| Context packs | `scripts/validate_context_packs.py` | Each workflow pack has required fields and known recommended skills. |
| Slop scan | `scripts/validate_skills.py --slop-only` | No banned filler phrases, no placeholder text (`TODO`, `TBD`, `coming soon`, `lorem ipsum`), no obvious secret patterns in any markdown file. |
| Skill grading | `scripts/grade_skills.py --min-score 90` | Skills score above a rubric threshold. Heuristic, not a substitute for review. |
| Lint | `ruff check .` | Python style and common bug patterns. |
| Security hygiene | `scripts/security_scan.py` | Secret patterns, dangerous shell, GitHub Actions permissions, action pinning, CODEOWNERS coverage. |
| Doctor | `scripts/doctor.py` | Readiness check for contract artifacts needed for AI-assisted work. |
| Tests | `pytest` | Locks harness behavior (validators, doc contract, slop scanner, repo contract). |

All checks run via `make prod-gate`.

## Commands run

```bash
uv sync --all-extras
.venv/bin/python scripts/validate_repo.py
.venv/bin/python scripts/validate_skills.py
.venv/bin/python scripts/validate_policies.py
.venv/bin/python scripts/validate_harnesses.py
.venv/bin/python scripts/validate_context_packs.py
.venv/bin/python scripts/validate_skills.py --slop-only
.venv/bin/python scripts/grade_skills.py --min-score 90
.venv/bin/python -m ruff check .
.venv/bin/python scripts/security_scan.py
.venv/bin/python scripts/doctor.py
.venv/bin/python -m pytest
make PYTHON=.venv/bin/python prod-gate
```

Final result: `make prod-gate` passes locally on the v2 modernization branch.

## Test results

- repo contract: ok (files, manifests, skills_index, doc contract, artifacts)
- skill validation: ok (10 skills)
- thinking budget: ok
- harness fixtures: ok
- context packs: ok
- slop scan: ok
- skill grading: 10 skills at 94.7 average
- ruff: clean
- security hygiene: ok
- doctor: ready
- pytest: 19 passed

Pytest reported one local cache warning because the sandbox blocked writing
`.pytest_cache`; tests still passed.

## Remaining risks

- The harness validates structure, not behavior. A skill can pass every check and still be ignored by a runtime.
- Harness fixtures are review aids, not model benchmarks.
- Context packs cannot prove the supplied context is complete or true.
- External link liveness is not checked; only internal link targets.
- Grade is heuristic. Line counts and bullet counts can be gamed without improving substance. Human review remains required for new skills.
- The pre-commit hook only verifies that a thinking ledger is staged; it cannot tell whether the ledger is real.
- Runtime compatibility with future Claude / Codex / Gemini formats may need updates as their adapter conventions evolve.

## Recommended next steps

- Keep `make prod-gate` green on every PR.
- When a new skill is added, update `skills_index.json` and `CATALOG.md` in the same PR; the repo contract check enforces both.
- If skill count grows beyond ~30, switch `skills_index.json` to generated and add a check that the generator output is up to date.
- Review skill behavior in real Claude, Codex, and Gemini sessions periodically. The harness cannot do this for you.
