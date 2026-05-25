# Contributing

Contributions should make AI-assisted engineering more understandable, safer, or easier to review. Do not add prompts because they sound useful. Add skills only when they solve a repeated developer workflow problem.

## Local Setup

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -e ".[test,lint]"
make check
```

The repo intentionally keeps dependencies small. Do not add a dependency unless it removes real maintenance burden or enables meaningful validation.

## Add Or Change A Skill

1. Define the developer problem the skill solves.
2. Check [docs/skill-standard.md](docs/skill-standard.md).
3. Keep one skill focused on one reasoning workflow.
4. Add or update `SKILL.md`.
5. Add at least two examples under `examples/`.
6. Add fixtures or notes under `fixtures/` or `tests/` when practical.
7. Update `CATALOG.md`, `skills_index.json`, and `.claude-plugin/plugin.json` when a skill is added or renamed.
8. Run `make check`.

## Pull Request Standard

Every non-trivial change should answer:

- What developer problem does this solve?
- What reasoning evidence does it require?
- Which runtime adapters are affected: Codex, Claude, Gemini?
- What was verified locally?
- What are the remaining risks?

Use [docs/review-checklist.md](docs/review-checklist.md) before asking for review.

## Licensing

By contributing, you agree that your contribution is licensed under this repo's split license:

- Code, scripts, hooks, workflows, and plugin manifests: MIT.
- Skills, docs, prompts, catalogs, and written methodology: CC BY-NC-SA 4.0.

## Do Not Commit

- Generated test artifacts.
- Coverage output.
- Caches.
- Logs.
- Local grading reports.
- Secrets or credentials.
- Private employer, customer, or infrastructure details.
- Unverified claims about third-party tools.

## Avoid

- Generic productivity prompts.
- Duplicated skills with different names.
- Skills that only restate common sense.
- Runtime-specific copies of the same skill body.
- Hooks that block work without explaining the missing evidence.
- CI that depends on private services, secrets, or local-only state.
