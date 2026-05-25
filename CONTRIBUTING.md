# Contributing

Contributions should strengthen developer reasoning, not just add more prompts.

## Add Or Change A Skill

1. Define the reasoning failure the skill prevents.
2. Keep `SKILL.md` concise and operational.
3. Add supporting files only when they reduce repeated instructions.
4. Update `.claude-plugin/plugin.json` if a skill directory is added or removed.
5. Run `make validate`.

## Licensing

By contributing, you agree that your contribution is licensed under this repo's split license:

- Code, scripts, hooks, workflows, and plugin manifests: MIT.
- Skills, docs, prompts, catalogs, and written methodology: CC BY-NC-SA 4.0.

## Pull Request Standard

Every non-trivial change should answer:

- What developer autopilot behavior does this prevent?
- What reasoning evidence does it require?
- Which runtime adapters are affected: Codex, Claude, Gemini?
- What was verified locally?

Do not commit generated test artifacts, grading reports, coverage output, caches, logs, or temporary files. Commit source checks and scripts; keep their generated output local or in CI logs.

## Avoid

- Generic productivity prompts.
- Duplicated skill bodies for each runtime.
- Hooks that block work without explaining the missing reasoning evidence.
- CI or package-manager complexity that does not support the repo.
