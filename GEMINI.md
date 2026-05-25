# Gemini Instructions

Cognitive Deadlift exposes the same shared skills to Gemini through this context file and `gemini-extension.json`.

Gemini may not treat `SKILL.md` directories exactly like Codex or Claude in every environment. Use this file as the Gemini entry point, then read the relevant `skills/*/SKILL.md` file before acting.

## Skill Routing

- For unclear requests, read `skills/problem-framing/SKILL.md`.
- For plans or assumptions, read `skills/assumption-audit/SKILL.md`.
- For design choices, read `skills/alternatives-before-code/SKILL.md` and `skills/complexity-budget/SKILL.md`.
- For fixes, read `skills/failing-test-first/SKILL.md`.
- For unfamiliar code, read `skills/trace-the-code/SKILL.md`.
- For external behavior, read `skills/read-the-docs-first/SKILL.md`.
- For generated diffs, read `skills/diff-interrogation/SKILL.md`.
- For hard bugs, read `skills/debugging-lab-notebook/SKILL.md`.
- Before merge or handoff, read `skills/explain-without-ai/SKILL.md`.

## Gemini-Specific Rule

When Gemini is used for broad synthesis, force it back to local evidence: files, docs, tests, logs, traces, and explicit assumptions.
