# Cognitive Deadlift Catalog

Index of skills, hooks, scripts, and runtime adapters. Keep this concise — purpose only.

Search phrases this repo is intended to answer:

- Codex / Claude / Gemini skills for software engineering
- AI coding hooks
- agent skills for critical thinking
- AI-assisted development guardrails
- anti-vibe-coding developer tools

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

## Scripts

| Script | Purpose |
| --- | --- |
| `scripts/validate_repo.py` | Repo contract: required files, manifests, skills index, doc contract, untracked artifacts. |
| `scripts/validate_skills.py` | Skill format + slop scanner: structure, frontmatter, sections, examples, links, banned filler, secrets. |
| `scripts/grade_skills.py` | Heuristic rubric grading skills against the skill standard. |
| `scripts/security_scan.py` | Security hygiene: secret patterns, dangerous shell, workflow permissions, CODEOWNERS coverage. |
| `scripts/cognitive_deadlift_check.py` | Pre-commit ledger check. Used by `hooks/pre-commit`. |

## Runtime adapters

| Runtime | Manifest | Context file |
| --- | --- | --- |
| Codex | `.codex-plugin/plugin.json` | `AGENTS.md` |
| Claude | `.claude-plugin/plugin.json` | `CLAUDE.md` |
| Gemini | `gemini-extension.json` | `GEMINI.md` |
