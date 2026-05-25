# Cognitive Deadlift Skill Catalog

Search phrases this repo is intended to answer:

- Codex skills for software engineering
- Claude skills for developers
- Gemini CLI extension for coding
- AI coding hooks
- agent skills for critical thinking
- AI-assisted development guardrails
- anti-vibe-coding developer tools
- software engineering thinking skills

## Skills

| Skill | Works With | Purpose |
| --- | --- | --- |
| `problem-framing` | Codex, Claude, Gemini | Define the real problem before implementation. |
| `assumption-audit` | Codex, Claude, Gemini | Surface and challenge hidden assumptions. |
| `alternatives-before-code` | Codex, Claude, Gemini | Compare solution paths before writing code. |
| `failing-test-first` | Codex, Claude, Gemini | Prove the bug or behavior before fixing it. |
| `trace-the-code` | Codex, Claude, Gemini | Follow the existing execution path before changing it. |
| `read-the-docs-first` | Codex, Claude, Gemini | Check docs, ADRs, schemas, and source references before guessing. |
| `explain-without-ai` | Codex, Claude, Gemini | Require a plain-language explanation before merge or handoff. |
| `diff-interrogation` | Codex, Claude, Gemini | Review generated or human diffs as untrusted code. |
| `debugging-lab-notebook` | Codex, Claude, Gemini | Reproduce, hypothesize, instrument, and verify hard bugs. |
| `complexity-budget` | Codex, Claude, Gemini | Challenge unnecessary abstraction and dependency creep. |

## Hooks

| Hook | Purpose |
| --- | --- |
| `hooks/pre-commit` | Blocks staged source changes unless a thinking ledger is staged. |

## Runtime Adapters

| Runtime | Files |
| --- | --- |
| Codex | `.codex-plugin/plugin.json`, `AGENTS.md` |
| Claude | `.claude-plugin/plugin.json`, `CLAUDE.md` |
| Gemini | `gemini-extension.json`, `GEMINI.md` |
