# Claude Instructions

Claude-specific rules. Read `AGENTS.md` first, and treat the rules below as additions to that file rather than replacements for it.

## Claude adapter

Claude loads skills from `skills/*/SKILL.md` through `.claude-plugin/plugin.json`. The shared body is the only body, and you should not generate Claude-specific copies of any skill.

## Skill routing

When a request touches implementation, review, debugging, architecture, or learning, route to a skill before generating code:

- `problem-framing` before implementation.
- `assumption-audit` before accepting a plan.
- `alternatives-before-code` before architecture or refactors.
- `failing-test-first` before fixes.
- `trace-the-code` before modifying unfamiliar paths.
- `read-the-docs-first` before framework or API claims.
- `explain-without-ai` before merge or handoff.
- `diff-interrogation` before accepting generated changes.
- `debugging-lab-notebook` for hard bugs.
- `complexity-budget` before adding abstraction.

Use `policies/thinking-budget.yaml` to choose friction by risk. Low-risk work needs
intent and a basic check. Medium-risk work needs trace, behavior proof, and diff
review. High-risk work needs framing, assumption audit, alternatives, rollback,
human approval, and final mechanism explanation.

## Model choice

- Use Opus for repo audit, architecture decisions, doc contract changes, and security-sensitive work.
- Use Sonnet for skill edits, harness checks, and routine implementation when the architecture is settled.
- Do not switch models mid-task unless the user asks.

## Claude-specific rule

Claude can be persuasive even when wrong. Require reasoning evidence like file paths, line numbers, command output, and test results before accepting a fluent explanation. Treat your own draft answers the same way before sending them.

## Before finishing

Run `make prod-gate`. If it fails, fix the real issue. Do not weaken the gate.
