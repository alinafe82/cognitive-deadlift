# Thinking Ledger

## Problem

The repo had a contract gap: AGENTS/CLAUDE/GEMINI named a "repo contract" that wasn't enforced anywhere, `skills_index.json` could silently drift from `skills/`, doc files could lose their declared sections without anyone noticing, and `cognitive_deadlift.egg-info/` style artifacts could get tracked. The Makefile also didn't expose the targets the user contract names: `prod-gate`, `docs-check`, `skills-check`, `slop-scan`.

## Current Evidence

- `git ls-files` confirmed no generated artifacts are currently tracked; the gap was the absence of an enforcing check, not a live failure.
- `scripts/validate_repo.py` only checked file presence and the Claude manifest — no index match, no doc contract, no artifact policing.
- `scripts/validate_skills.py` already does the slop scan but had no entry point for "slop only," so `make slop-scan` had nowhere to land.
- `make check` was passing on the existing tree, so the work was about closing contract gaps without regressing what already worked.
- `ARCHITECTURE.md` was a one-line redirect to `docs/architecture.md` — two files claiming the same job, exactly the duplication `repo-audit.md` is supposed to catch.

## Assumptions

- The harness must validate structure, not behavior. Agents passing the gate can still ignore skills at runtime.
- `skills_index.json` stays hand-maintained until the skill count justifies generation.
- The slop scanner must allow docs to *name* banned phrases as examples — listing what to avoid is part of the contract.
- `prod-gate` is the single command for CI and PR reviewers; everything meaningful chains into it.

## Alternatives

- **Generate `skills_index.json` from `skills/`.** Rejected. At 10 skills, the hand-written file is reviewable and the validator catches drift. Revisit at ~30 skills.
- **Add a separate `slop-scan.py` script.** Rejected. The slop logic already lives in `validate_skills.py`; a flag is cheaper than a new file.
- **Make the slop scanner ignore filenames named `*-banned-list.md`.** Rejected. Brittle naming convention. The right behavior is to ignore code spans and fenced blocks — that's how every linter handles this.
- **Trim AGENTS.md to a five-bullet contract.** Rejected. The existing engineering-style content is useful; the contract bullets land at the top and the rest stays.
- **Delete `docs/architecture.md` and consolidate into `ARCHITECTURE.md`.** Rejected. Two different jobs: top-level structure (root) vs deeper rationale and alternatives (docs/). Both have audiences.

## Chosen Approach

- Expand `validate_repo.py` with three new checks: `skills_index`, `doc_contract`, `generated_artifacts`. Keep failures as findings printed to stderr instead of bailing on the first one.
- Add `--slop-only` to `validate_skills.py` and a `strip_code` helper so code spans/fenced blocks don't count.
- Add Makefile targets `prod-gate`, `repo-check`, `skills-check`, `docs-check`, `slop-scan`, plus a `help` target. Keep `check`, `validate`, `grade` for back-compat with CI.
- Rewrite CONTEXT.md (added mission/principles/anti-slop/validation/assumptions, kept glossary), ARCHITECTURE.md (canonical structural doc), CATALOG.md (added Scripts section), AGENTS.md (added repo-contract section), CLAUDE.md/GEMINI.md (slimmed to per-agent layer).
- Rewrite `repo-audit.md` as a standing audit with the source-of-truth contract table.
- Rewrite `productionization-report.md` with current checks, commands, results, risks.
- Add `tests/test_validate_repo.py` and extend `tests/test_validate_skills.py` to lock the new checks and the code-block-skipping slop behavior.

## Verification

`make prod-gate` exits 0 with:

- `validate_repo: ok`
- `validate_skills: ok`
- `slop_scan: ok`
- 10 skills graded A (94.7) above the 90 floor
- `ruff check .` clean
- `security_scan: ok`
- 13 pytest tests passing (4 new repo-contract tests, 3 new slop-scanner tests)

## Residual Risk

- The harness validates structure, not behavior. Skills can still be ignored by a runtime.
- External link liveness is unchecked.
- Skill grading is heuristic — gameable by line/bullet counts.
- The pre-commit hook can't tell whether a thinking ledger is real (including this one).
- Future runtime adapter format changes (Claude, Codex, Gemini) will need ongoing maintenance.
