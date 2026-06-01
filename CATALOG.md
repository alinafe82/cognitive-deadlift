# Cognitive Deadlift Catalog

Index of skills, policies, context packs, harnesses, hooks, scripts, and runtime adapters. Keep entries concise and state only the purpose of each item.

Search phrases this repo is intended to answer:

- Codex / Claude / Gemini skills for software engineering
- AI coding review harness
- agent skills for critical thinking
- skill-retention harness
- AI-assisted development guardrails
- AI-assisted development evidence gates

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

## Policies

| Policy | Purpose |
| --- | --- |
| `policies/thinking-budget.yaml` | Defines low / medium / high evidence gates for AI-assisted work. |

## Context packs

| Pack | Purpose |
| --- | --- |
| `context-packs/bugfix.yaml` | Evidence needed before AI-assisted bug fixing. |
| `context-packs/refactor.yaml` | Evidence needed before preserving behavior through a refactor. |
| `context-packs/repo-review.yaml` | Evidence needed for repo clarity and honesty review. |
| `context-packs/risky-change.yaml` | Evidence needed before high-risk changes. |

## Harnesses

| Harness | Purpose |
| --- | --- |
| `harnesses/ambiguous-request` | Checks whether missing problem evidence is handled before code. |
| `harnesses/fake-test-pass` | Checks whether unsupported test confidence is rejected. |
| `harnesses/overeager-refactor` | Checks whether abstraction is challenged before a rewrite. |
| `harnesses/unsafe-tool-use` | Checks whether destructive tool use waits for approval. |

## Scripts

| Script | Purpose |
| --- | --- |
| `scripts/validate_repo.py` | Repo contract: required files, manifests, skills index, doc contract, untracked artifacts. |
| `scripts/validate_skills.py` | Skill format + slop scanner: structure, frontmatter, sections, examples, links, banned filler, secrets. |
| `scripts/validate_policies.py` | Thinking budget validator. |
| `scripts/validate_context_packs.py` | Context pack validator. |
| `scripts/validate_harnesses.py` | Harness fixture validator. |
| `scripts/grade_skills.py` | Heuristic rubric grading skills against the skill standard. |
| `scripts/security_scan.py` | Security hygiene: secret patterns, dangerous shell, workflow permissions, CODEOWNERS coverage. |
| `scripts/cognitive_deadlift_check.py` | Pre-commit ledger check. Used by `hooks/pre-commit`. |
| `scripts/doctor.py` | Readiness check for AI-assisted work contract artifacts. |

## Runtime adapters

| Runtime | Manifest | Context file |
| --- | --- | --- |
| Codex | `.codex-plugin/plugin.json` | `AGENTS.md` |
| Claude | `.claude-plugin/plugin.json` | `CLAUDE.md` |
| Gemini | `gemini-extension.json` | `GEMINI.md` |
