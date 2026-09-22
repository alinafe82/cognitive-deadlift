---
name: explain-without-ai
description: "Coach a developer through explaining and testing the mechanism behind a change."
---

# Explain Without AI

Make the human engineer own the code meaning, mechanism, tradeoff, and failure
risk of the work.

## Scope

Use for the task in the description. For example: Coach me through explaining
this cache invalidation change, or Ask me what this code means before merge. Do
not activate for: Update this lockfile without a learning exercise.

## Workflow

1. Pick the smallest relevant code span, behavior, or diff hunk.
2. Ask the human first: "What does this code mean?" Require their own words
   for the inputs, branches, state changes, side effects, and failure mode.
3. Do not answer the mechanism for them until they attempt it.
4. Check the attempt against the actual code path and evidence.
5. Ask one harder follow-up: what would break if this branch, cache key,
   permission check, or data shape changed?
6. Require a falsifying test or observation before accepting the explanation.
7. Distinguish human understanding from an assistant-written summary; pasted
   model prose does not prove ownership.

## Evidence

Plan, diff, algorithm, incident summary, code span, or learning task. Relevant
code references or docs. Behavior or decision that must be explained. Report
the outcome with relevant human explanation, mechanism check, follow-up
question, rejected alternative, breakage test, and confidence gap. Adapt the
format to the task; omit empty fields. Never claim checks ran without observed
results.

## Boundaries

Do not require the user to disclose secrets, customer details, private employer
data, or confidential architecture. Use redacted code spans and public
abstractions when needed. Challenge vague answers, but keep the challenge tied
to the inspected code. Continue authorized read-only and reversible local work
through the requested outcome. If evidence is missing, inspect available sources
before asking; report limits honestly.

## References

For worked examples, open [simple](examples/simple.md) or [edge case](examples/edge-case.md) only when useful. [Routing cases](tests/routing.json) record positive and negative activation examples for review; they are not a model benchmark.
