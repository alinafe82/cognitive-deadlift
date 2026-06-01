---
name: trace-the-code
description: "Trace existing execution paths before changing unfamiliar behavior. Use when editing unknown code, debugging, reviewing AI-generated changes, or when a plan depends on current state, side effects, or error flow. NOT for greenfield files, pure docs, or already-traced isolated changes."
---

# Trace The Code

## Purpose

Force the assistant to read the real implementation path before inventing behavior.

## Preserves

Code reading.

## Required Evidence

- Entry point, command, route, component, function, stack trace, or workflow.
- Relevant files found by search or supplied by the user.
- Behavior to understand or change.

## Failure Signs

- Architecture is described from memory while code is available.
- Error flow, state, or side effects are skipped.
- Edits are proposed before the call path is summarized.

## When To Use

- The code path is unfamiliar.
- The change crosses module boundaries.
- Current state, data shape, error handling, or side effects matter.
- AI suggests an implementation without showing how the current code works.

## When Not To Use

- Greenfield files with no existing callers.
- Pure documentation edits.
- Work where a recent trace already exists in the issue, PR, or thinking ledger.

## Inputs Expected

- Entry point, command, route, component, function, stack trace, or user workflow.
- Relevant repository files if known.
- The behavior to understand or change.

## Output Expected

```md
Entry point:
Call path:
Data shape:
State/external effects:
Error path:
Unknowns:
```

## Process

1. Find the public entry point.
2. Follow calls to the state change or external effect.
3. Track the data shape at boundaries.
4. Track where errors are swallowed, transformed, retried, or surfaced.
5. Summarize the path with file references before proposing edits.

## Quality Bar

A good trace gives enough file and line references that another engineer can verify the path without redoing the search from scratch.

## Examples

Simple case: a CLI flag is ignored. The skill should trace from argument parsing to config construction to the branch that should consume the flag.

Complex case: a webhook is acknowledged but not persisted. The skill should trace request handling, validation, persistence, retries, and error logging.

See `examples/simple.md` and `examples/edge-case.md`.

## Failure Modes

- Entry point unknown: search for user-visible strings, routes, commands, or tests.
- Generated code involved: trace to the generated boundary and identify the source of generation.
- Files unavailable: state that the trace is incomplete and ask for the smallest missing file.
- Multiple possible paths: list them and prioritize the path with the reported symptom.

## Safety And Privacy

Do not paste private source code, secrets, logs, customer identifiers, or internal hostnames into the final output. Use file references and redacted snippets.

## Anti-Slop Rules

- Do not describe architecture from memory when code is available.
- Do not skip the error path.
- Do not invent callers or data shapes.
- Do not propose edits before summarizing the trace.
