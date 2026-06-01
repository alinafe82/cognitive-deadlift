# Gemini Instructions

Gemini-specific rules. Read `AGENTS.md` first — these are additions, not replacements.

## Gemini adapter

Gemini reads the shared skills through `gemini-extension.json` and uses this file as the context entry point. The shared body in `skills/*/SKILL.md` is the only body; do not generate Gemini-specific copies.

Gemini may not treat `SKILL.md` directories exactly like Codex or Claude in every environment. When in doubt, read the relevant `skills/<name>/SKILL.md` directly before acting.

## Skill routing

- For unclear requests, read `skills/problem-framing/SKILL.md`.
- For plans or assumptions, read `skills/assumption-audit/SKILL.md`.
- For design choices, read `skills/alternatives-before-code/SKILL.md` and `skills/complexity-budget/SKILL.md`.
- For fixes, read `skills/failing-test-first/SKILL.md`.
- For unfamiliar code, read `skills/trace-the-code/SKILL.md`.
- For external behavior, read `skills/read-the-docs-first/SKILL.md`.
- For generated diffs, read `skills/diff-interrogation/SKILL.md`.
- For hard bugs, read `skills/debugging-lab-notebook/SKILL.md`.
- Before merge or handoff, read `skills/explain-without-ai/SKILL.md`.

## Gemini-specific rule

When Gemini is used for broad synthesis, force it back to local evidence: files, docs, tests, logs, traces, and explicit assumptions. A synthesis without file paths or commands is a draft, not an answer.

## Before finishing

Run `make prod-gate`. If it fails, fix the real issue. Do not weaken the gate.
