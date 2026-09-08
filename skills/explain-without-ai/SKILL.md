---
name: explain-without-ai
description: "Coach a developer through explaining and testing the mechanism behind a change."
---

# Explain Without Ai

Make the developer own the mechanism, tradeoff, and failure risk of the work.

## Scope

Use for the task in the description. For example: Coach me through explaining this cache invalidation change. Do not activate for: Update this lockfile without a learning exercise.

## Workflow

1. Ask the developer for a short mechanism explanation when coaching is requested.
2. Check it against the relevant code path and evidence.
3. Use one focused question or counterexample to expose a gap.
4. Distinguish the developer’s explanation from an assistant-written explanation; the latter does not prove understanding.
5. Identify the test or observation that would falsify the explanation.

## Evidence

Plan, diff, algorithm, incident summary, or learning task. Relevant code references or docs. Behavior or decision that must be explained. Report the outcome with relevant plain explanation, mechanism, rejected alternative, breakage test. Adapt the format to the task; omit empty fields. Never claim checks ran without observed results.

## Boundaries

Do not require the user to disclose secrets, customer details, private employer data, or confidential architecture. Ask for redacted mechanisms and public abstractions. Continue authorized read-only and reversible local work through the requested outcome. If evidence is missing, inspect available sources before asking; report limits honestly.

## References

For worked examples, open [simple](examples/simple.md) or [edge case](examples/edge-case.md) only when useful. [Routing cases](tests/routing.json) record positive and negative activation examples for review; they are not a model benchmark.
