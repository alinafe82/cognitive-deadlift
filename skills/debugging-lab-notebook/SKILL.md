---
name: debugging-lab-notebook
description: "Investigate hard or intermittent failures by tracking hypotheses, experiments, and regression evidence."
---

# Debugging Lab Notebook

Turn hard debugging into a recorded experiment loop instead of a sequence of guesses.

## Scope

Use for the task in the description. For example: Investigate a worker that intermittently drops messages under concurrency. Do not activate for: Fix this parser assertion with an already-isolated deterministic regression.

## Workflow

1. Build the smallest available reproduction or observation signal.
2. Write competing hypotheses.
3. Add instrumentation that distinguishes between hypotheses.
4. Run one experiment at a time.
5. Record negative findings.
6. Add regression proof after the fix.

## Evidence

Symptom and reproduction attempt. Logs, traces, metrics, failing command, or user report if available. Code area or workflow likely involved. Report the outcome with relevant reproduction, hypotheses, experiment, result. Adapt the format to the task; omit empty fields. Never claim checks ran without observed results.

## Boundaries

Do not expose raw production logs, tokens, customer data, internal hostnames, or private incident details. Remove exploratory instrumentation unless it is intentionally kept. Continue authorized read-only and reversible local work through the requested outcome. If evidence is missing, inspect available sources before asking; report limits honestly.

## References

For worked examples, open [simple](examples/simple.md) or [edge case](examples/edge-case.md) only when useful. [Routing cases](tests/routing.json) record positive and negative activation examples for review; they are not a model benchmark.
