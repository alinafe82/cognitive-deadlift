# Claude Instructions

Cognitive Deadlift uses Claude skills as the primary portable skill format.

## Claude Adapter

Claude should load skills from `skills/*/SKILL.md` through `.claude-plugin/plugin.json`.

When a request touches implementation, review, debugging, architecture, or learning, prefer the relevant Cognitive Deadlift skill before generating code:

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

## Claude-Specific Rule

Claude can be persuasive even when wrong. Require reasoning evidence before accepting fluent explanations.
