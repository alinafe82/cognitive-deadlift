# Architecture

Cognitive Deadlift has one shared skill library and several runtime adapters.

```text
skills/*/SKILL.md
  -> .codex-plugin/plugin.json + AGENTS.md
  -> .claude-plugin/plugin.json + CLAUDE.md
  -> gemini-extension.json + GEMINI.md
```

## Shared Core

The `skills/` directory is the source of truth. A skill should not be copied into a runtime-specific directory unless that runtime requires a different file format.

## Runtime Adapters

Runtime adapters describe how a harness discovers or routes to the shared skills:

- Codex uses `.codex-plugin/plugin.json`.
- Claude uses `.claude-plugin/plugin.json`.
- Gemini uses `gemini-extension.json` and `GEMINI.md`.

## Enforcement

Hooks and scripts do not replace the skills. They enforce that risky changes include reasoning evidence, usually through `docs/thinking/*.md`.
