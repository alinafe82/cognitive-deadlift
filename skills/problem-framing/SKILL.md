---
name: problem-framing
description: "Resolve an ambiguous engineering request into an observable problem and completion criteria."
---

# Problem Framing

Make the assistant define the real problem before it designs or writes code.

## Scope

Use for the task in the description. For example: Add retries; I do not know which failures or duplicates we are seeing. Do not activate for: Apply the change specified by this precise failing test.

## Workflow

1. Restate the request as a problem, not a solution.
2. Identify actor, workflow, boundary, and observable symptom.
3. Separate facts from interpretation.
4. Name assumptions that still need checking.
5. Define success as a test, command, user-visible outcome, or reviewable signal.
6. Inspect available evidence first; ask only when a missing fact prevents safe progress.

## Evidence

User request or symptom. Current evidence, or an explicit note that evidence is missing. Constraints, non-goals, or success signal if known. Report the outcome with relevant problem, current evidence, assumptions, non-goals. Adapt the format to the task; omit empty fields. Never claim checks ran without observed results.

## Boundaries

Do not ask for secrets, customer records, private employer details, or production credentials. If examples contain private data, request redacted logs or synthetic identifiers. Continue authorized read-only and reversible local work through the requested outcome. If evidence is missing, inspect available sources before asking; report limits honestly.

## References

For worked examples, open [simple](examples/simple.md) or [edge case](examples/edge-case.md) only when useful. [Routing cases](tests/routing.json) record positive and negative activation examples for review; they are not a model benchmark.
