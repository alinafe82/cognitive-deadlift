# Cognitive Deadlift V2 Modernization

## Current repo inventory

- Public docs: `README.md`, `CONTEXT.md`, `ARCHITECTURE.md`, `CATALOG.md`,
  `repo-audit.md`, `productionization-report.md`, and supporting files under `docs/`.
- Runtime adapters: `.codex-plugin/plugin.json`, `.claude-plugin/plugin.json`,
  `gemini-extension.json`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, and `.gemini/README.md`.
- Skills: ten shared skills under `skills/<name>/SKILL.md`, each with `examples/`,
  `fixtures/`, and `tests/`.
- Existing skills: `problem-framing`, `assumption-audit`, `alternatives-before-code`,
  `failing-test-first`, `trace-the-code`, `read-the-docs-first`,
  `explain-without-ai`, `diff-interrogation`, `debugging-lab-notebook`, and
  `complexity-budget`.
- Hooks: `hooks/pre-commit` calls `scripts/cognitive_deadlift_check.py`.
- Scripts: repo validation, skill validation, skill grading, security scanning, and
  thinking-ledger checking under `scripts/`.
- Tests: pytest coverage for repo validation and skill validation under `tests/`.
- CI: GitHub Actions for validation, CI, security hygiene, CodeQL, and dependency review.
- Build and check surface: `Makefile`, `pyproject.toml`, `uv.lock`, and Python 3.11+
  tooling.

## Current strengths

- The repo already has a clear anti-autopilot thesis.
- The ten skills map to real engineering abilities, not generic prompting.
- Skill structure is consistent and validated.
- Runtime adapters use shared skill bodies instead of duplicated runtime copies.
- The validation harness is deterministic and standard-library first.
- CI exists and is fast.
- The repo already rejects filler language, placeholder text, obvious secret patterns,
  broken internal links, and tracked generated artifacts.

## Current problems

- The repo still reads like a skill and prompt package more than a practical
  skill-retention harness.
- The README gives the skills but does not explain the retention model clearly enough.
- Risk-based thinking is implicit. There is no visible low / medium / high budget.
- There are no harness fixtures that teach reviewers how agent failure modes look.
- There are no context packs that show what evidence an agent should receive for common
  workflows.
- Skill atrophy and AI slop are described indirectly instead of as practical review
  taxonomies.
- `AGENTS.md` still frames the repo as a portfolio artifact. That is not the right gate
  for a general developer tool.
- Existing validators do not yet cover harnesses, context packs, the thinking budget, or
  doctor readiness.

## Repo thesis

AI can move faster than judgment. Cognitive Deadlift keeps the judgment in the loop.

Cognitive Deadlift helps developers use AI without losing the engineering skills that
make them useful: defining problems, reading code, debugging, designing tests,
understanding tradeoffs, reviewing diffs, and explaining changes in plain English.

## What the repo is

- A skill-retention harness for AI-assisted development.
- A set of reusable skills that preserve specific developer abilities.
- A risk-based thinking budget for choosing the right amount of evidence.
- A small collection of context packs for common AI-assisted workflows.
- A set of harness fixtures for reviewing agent failure modes.
- A deterministic validation harness for repo structure, skills, docs, policies, and
  fixtures.

## What the repo is not

- It is not anti-AI.
- It is not a prompt dump.
- It is not an agent framework.
- It is not a chat UI.
- It is not a benchmark suite.
- It is not a replacement for human code review.
- It is not a process checklist for every small edit.
- It is not a claim that skills always make agents behave correctly.

## Target users

- Individual developers using AI coding assistants for bugs, refactors, tests, docs, and
  code review.
- Teams that want lightweight AI-assisted development gates without a heavy process.
- Maintainers who review AI-heavy diffs and need better evidence than fluent summaries.
- Engineering leads who want risk-based guidance for when AI-assisted work needs more
  human judgment.

The repo should stay vendor-neutral. Codex, Claude, Gemini, and similar tools are
runtime targets, not the identity of the project.

## Skill-retention model

Passive AI use can erode these developer skills:

- Problem definition.
- Code reading.
- Debugging.
- Test design.
- Systems thinking.
- Tradeoff analysis.
- Diff review.
- Error interpretation.
- Operational judgment.
- Ability to explain the mechanism.

Cognitive Deadlift protects those skills by making each risky workflow produce evidence:

- `problem-framing` protects problem definition.
- `trace-the-code` protects code reading.
- `failing-test-first` protects behavioral proof and test design.
- `debugging-lab-notebook` protects systematic debugging and error interpretation.
- `alternatives-before-code` protects tradeoff analysis.
- `complexity-budget` protects systems thinking and operational judgment.
- `diff-interrogation` protects review judgment.
- `explain-without-ai` protects ownership of the mechanism.
- `assumption-audit` protects judgment around unverified claims.
- `read-the-docs-first` protects source-based reasoning.

The model should not add the same burden to every task. The amount of thinking evidence
should match the risk.

## Risk-based thinking budget

- Low risk: mechanical or reversible work. Require intent and a basic check.
- Medium risk: normal behavior changes. Require code-path evidence, behavioral proof, and
  diff review.
- High risk: security, data, public API, permissions, destructive behavior, migrations, or
  production configuration. Require problem framing, assumption audit, alternatives,
  rollback thinking, human approval, and final mechanism explanation.

The budget should be documented in `policies/thinking-budget.yaml` and validated by a
small script. It should remain human-readable. No policy engine is needed.

## Proposed file layout

```text
context-packs/
  README.md
  bugfix.yaml
  refactor.yaml
  repo-review.yaml
  risky-change.yaml
docs/
  ai-slop-taxonomy.md
  roadmap.md
  skill-atrophy-taxonomy.md
harnesses/
  README.md
  ambiguous-request/
    task.md
    expected-behavior.md
    rubric.yaml
  fake-test-pass/
    task.md
    expected-behavior.md
    rubric.yaml
  overeager-refactor/
    task.md
    expected-behavior.md
    rubric.yaml
  unsafe-tool-use/
    task.md
    expected-behavior.md
    rubric.yaml
policies/
  thinking-budget.yaml
scripts/
  doctor.py
  validate_context_packs.py
  validate_harnesses.py
  validate_policies.py
```

## Required changes

- Rewrite `README.md` around skill retention, thinking budget, context packs, harnesses,
  workflows, validation commands, and honest limits.
- Update `AGENTS.md` with a skill-retention behavior contract for coding agents.
- Keep `CLAUDE.md` and `GEMINI.md` aligned with shared skill routing and the risk budget.
- Update `CONTEXT.md` so mission, principles, assumptions, and language reflect skill
  retention rather than prompt packaging.
- Update `ARCHITECTURE.md`, `docs/architecture.md`, `CATALOG.md`, `repo-audit.md`, and
  `productionization-report.md` for the new directories, scripts, and checks.
- Add `policies/thinking-budget.yaml`.
- Add `docs/skill-atrophy-taxonomy.md`.
- Add `docs/ai-slop-taxonomy.md`.
- Add `docs/roadmap.md`.
- Add `harnesses/` fixtures and a lightweight validator.
- Add `context-packs/` files and a lightweight validator.
- Add `scripts/doctor.py`.
- Add Makefile targets: `harness-check`, `context-check`, `policy-check`, and `doctor`.
- Keep existing targets working: `check`, `prod-gate`, `skills-check`, `docs-check`,
  `slop-scan`, `test`, and `lint`.
- Update CI to run the expanded check surface.
- Add tests for policy, harness, context-pack, doctor, and contract artifacts.
- Run anti-slop cleanup and remove unsupported personal or portfolio positioning.

## Deferred changes

- No full benchmark runner.
- No scoring engine for agent transcripts.
- No YAML schema dependency.
- No new package dependency.
- No chat UI.
- No hosted service.
- No vendor-specific install automation beyond existing adapters.
- No automatic enforcement of the thinking budget inside downstream repositories.

These can be reconsidered only after the lightweight harness is useful in review.

## Acceptance criteria

- The README communicates this thesis in the first screen: Cognitive Deadlift helps
  developers use AI without losing the engineering skills that make them useful.
- The repo is framed for any developer or team using AI coding assistants.
- Personal work history, employer history, resume positioning, and portfolio positioning
  are not used as the repo gate or audience.
- Risk-based thinking is explicit and backed by `policies/thinking-budget.yaml`.
- Skill atrophy and AI slop are documented as practical review taxonomies.
- Harness fixtures exist and are validated.
- Context packs exist and are validated.
- The doctor command reports readiness deterministically.
- Makefile targets listed in the README work.
- CI runs meaningful checks.
- Tests cover the new validators and doctor command.
- Existing skills remain concise and continue to pass `skills-check`.
- Final validation commands pass or any remaining failure is documented with cause.

## Commands run

Inspection commands run before this spec:

- `git branch --show-current`
- `git status --short`
- `git checkout -b modernize-skill-retention-harness`
- `sed` reads of `README.md`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `CATALOG.md`,
  `CONTEXT.md`, `ARCHITECTURE.md`, `repo-audit.md`, `Makefile`, `pyproject.toml`,
  `docs/skill-standard.md`, `docs/review-checklist.md`, runtime adapter manifests,
  workflow files, current skill files, scripts, hooks, tests, and local `.specs/`
  context.
- `find` inventory of `skills/`, `hooks/`, `scripts/`, `tests/`, `docs/`, workflows,
  and root files.

Validation commands to run after implementation:

- `python3 scripts/validate_policies.py`: pass.
- `python3 scripts/validate_context_packs.py`: pass.
- `python3 scripts/validate_harnesses.py`: pass.
- `python3 scripts/doctor.py`: ready.
- `python3 scripts/validate_repo.py`: pass.
- `python3 scripts/validate_skills.py`: pass.
- `python3 scripts/validate_skills.py --slop-only`: pass.
- `python3 scripts/security_scan.py`: pass.
- `python3 -m pytest`: 19 passed, with one sandbox cache warning.
- `python3 -m ruff check .`: initially failed on unused import, passed after fix.
- `make check`: pass.
- `make prod-gate`: pass.
- `make skills-check`: pass.
- `make harness-check`: pass.
- `make context-check`: pass.
- `make docs-check`: pass.
- `make slop-scan`: pass.
- `make doctor`: ready.
- `make test`: 19 passed, with one sandbox cache warning.
- `make lint`: pass.
- `make policy-check`: pass.

## Test results

- Added `tests/test_contract_artifacts.py`.
- Pytest now runs 19 tests.
- Contract artifact tests cover simple YAML parsing, thinking budget validation,
  context pack validation, harness validation, doctor readiness, and doctor JSON output.
- Existing repo and skill validator tests still pass.
- Pytest warning: local sandbox blocked writing `.pytest_cache`; this did not affect test
  results.

## Manual follow-up

- Decide whether the paid offer page still belongs in the public README after the v2
  repositioning. The page can remain as a supporting doc, but it should not distract from
  the skill-retention thesis.
- Periodically review real agent sessions to see whether the harness fixtures catch the
  right failure modes. The repo can validate structure, but human review still judges
  behavior.
- Consider whether `docs/paid-offer.md` should be revised or removed in a later PR so it
  does not distract from the vendor-neutral harness story.
