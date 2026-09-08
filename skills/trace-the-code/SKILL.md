---
name: trace-the-code
description: "Trace an unfamiliar execution path when a change depends on its state, side effects, or error handling."
---

# Trace The Code

Force the assistant to read the real implementation path before inventing behavior.

## Scope

Use for the task in the description. For example: Trace the webhook acknowledgment through persistence and retry handling. Do not activate for: Write a new isolated module with no existing callers.

## Workflow

1. Find the public entry point.
2. Follow calls to the state change or external effect.
3. Track the data shape at boundaries.
4. Track where errors are swallowed, transformed, retried, or surfaced.
5. Summarize the path with file references before proposing edits.

## Evidence

Entry point, command, route, component, function, stack trace, or workflow. Relevant files found by search or supplied by the user. Behavior to understand or change. Report the outcome with relevant entry point, call path, data shape, state/external effects. Adapt the format to the task; omit empty fields. Never claim checks ran without observed results.

## Boundaries

Do not paste private source code, secrets, logs, customer identifiers, or internal hostnames into the final output. Use file references and redacted snippets. Continue authorized read-only and reversible local work through the requested outcome. If evidence is missing, inspect available sources before asking; report limits honestly.

## References

For worked examples, open [simple](examples/simple.md) or [edge case](examples/edge-case.md) only when useful. [Routing cases](tests/routing.json) record positive and negative activation examples for review; they are not a model benchmark.
