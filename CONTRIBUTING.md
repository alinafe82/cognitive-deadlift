# Contributing

Contributions should strengthen developer reasoning, not just add more prompts.

## Add Or Change A Skill

1. Define the reasoning failure the skill prevents.
2. Keep `SKILL.md` concise and operational.
3. Add supporting files only when they reduce repeated instructions.
4. Update `.claude-plugin/plugin.json` if a skill directory is added or removed.
5. Run `make validate`.

## Pull Request Standard

Every non-trivial change should answer:

- What developer autopilot behavior does this prevent?
- What reasoning evidence does it require?
- Which runtime adapters are affected: Codex, Claude, Gemini?
- What was verified locally?

## Avoid

- Generic productivity prompts.
- Duplicated skill bodies for each runtime.
- Hooks that block work without explaining the missing reasoning evidence.
- CI or package-manager complexity that does not support the repo.
