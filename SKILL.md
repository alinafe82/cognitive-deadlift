---
name: cognitive-deadlift
description: "Use when a developer asks to apply Cognitive Deadlift, frame a coding problem, audit assumptions, prove a bug with a failing test, trace code, or review a diff while retaining human engineering judgment. Route to the relevant bundled workflow."
---

# Cognitive Deadlift

A skill-retention harness for AI-assisted software development by Alinafe Matenda.
Copyright (c) 2026 Alinafe Matenda.
This entry point routes to the existing bundled skills; it is not a new agent framework.

## Workflow

1. Identify the user's concrete engineering task, current evidence and authorized scope. Read local project instructions before making changes.
2. Read [the skill index](skills_index.json) and select only the workflow matching that task. Use the corresponding `skills/<name>/SKILL.md` as the source of instructions, then follow its workflow and evidence requirements. Load linked examples only when useful. Do not activate every skill for an ordinary small task.
3. Use [the thinking budget](policies/thinking-budget.yaml) to scale evidence to risk. Low-risk mechanical work needs intent and a basic check. Normal behavior changes need a path trace, failing signal and diff review. High-risk changes need problem framing, assumptions, alternatives, rollback and an authorization check.
4. For a bug fix, use `trace-the-code`, `failing-test-first` and `diff-interrogation` as relevant. Use `problem-framing` when the symptom is unclear. Use `explain-without-ai` for a human explanation exercise, not a fabricated claim of human understanding.
5. For release checks on this package, read `skills/release-readiness/SKILL.md`; validate the actual source with `make doctor` and `make prod-gate` only when a shell and installed development dependencies are available. Report commands actually observed, their exit results and remaining limitations.
6. Return the concrete outcome, supporting evidence, changed files or review findings, checks run and unresolved limits. Keep observed results separate from assumptions. Never invent successful tests, approvals, benchmarks, integrations or human explanations.

## Boundaries and requirements

Use only tools and repository access the user has authorized. Reuse authorization already given for the requested action; pause for missing essential authorization, destructive actions, secrets or private records. Do not request credentials or expose private data in outputs. This package does not grant permissions or bypass runtime safeguards.

The agent must be able to read bundled support files and relevant project files. If bundled references are unavailable in the current runtime, state that limit and request access rather than pretending to have loaded them. Python 3.11+ and the optional development dependencies in `pyproject.toml` are needed only for repository validation commands. Those dependencies are not installed automatically by this skill. No external account or API key is required for its own local validators; tasks may separately require authorized tools or documentation access.

The repository includes Codex, Claude and Gemini adapter metadata and structural fixtures. These do not prove a full live behavior matrix across all agents or guarantee that a model follows every instruction. Human code review remains necessary.

## Source and license

Cognitive Deadlift 0.1.0 source:
https://github.com/alinafe82/cognitive-deadlift

This entry routes to the shared workflow bodies instead of duplicating them. Code/scripts/manifests are MIT; skills, docs and written methodology (including this entry) are CC BY-NC-SA 4.0. Preserve attribution and share-alike terms; commercial use of the content requires separate permission. Read [LICENSE](LICENSE), [LICENSE-CONTENT](LICENSE-CONTENT) and [NOTICE](NOTICE).
