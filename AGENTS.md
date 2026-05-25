# Agent Instructions

This repo is a Cognitive Deadlift plugin for AI-assisted developers who want to keep their own engineering judgment sharp.

## Codex Usage

When working in this repo:

- Read `CONTEXT.md` before changing terminology.
- Treat `skills/*/SKILL.md` as the shared source of truth.
- Keep `.codex-plugin/plugin.json` aligned with the actual skill directories.
- Use `scripts/validate_repo.py` before committing.
- For non-trivial source changes, add a thinking ledger under `docs/thinking/`.

## Operating Rule

Do not optimize for less friction. Optimize for useful friction: problem framing, assumptions, alternatives, code tracing, failing tests, and diff interrogation at the points where a developer could otherwise go on autopilot.

## File Boundaries

- Codex adapter: `.codex-plugin/plugin.json`, `AGENTS.md`
- Claude adapter: `.claude-plugin/plugin.json`, `CLAUDE.md`
- Gemini adapter: `gemini-extension.json`, `GEMINI.md`, `.gemini/`
- Shared skills: `skills/*/SKILL.md`
- Shared enforcement: `hooks/`, `scripts/`
