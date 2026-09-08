---
name: alternatives-before-code
description: "Compare viable approaches when an unresolved design decision has meaningful cost or reversibility tradeoffs."
---

# Alternatives Before Code

Prevent the first plausible implementation from becoming the decision by default.

## Scope

Use for the task in the description. For example: Compare a queue with scheduled retries for failed billing sync. Do not activate for: Rename this variable to match the existing convention.

## Workflow

1. Name the decision in one sentence.
2. Compare only viable options, including a minimal or no-change path when useful; do not invent options to fill a quota.
3. Compare cost, reversibility, blast radius, testability, and cognitive load.
4. Recommend one option.
5. State what evidence would change the recommendation.

## Evidence

Decision to be made. Constraints that affect reversibility, blast radius, cost, or testability. Existing architecture notes or code boundaries if available. Report the outcome with relevant decision, option a - minimal, option b - structural, option c - conservative/no-build. Adapt the format to the task; omit empty fields. Never claim checks ran without observed results.

## Boundaries

Do not include private vendor details, customer names, or confidential architecture diagrams. Use generic labels when examples need sensitive context. Continue authorized read-only and reversible local work through the requested outcome. If evidence is missing, inspect available sources before asking; report limits honestly.

## References

For worked examples, open [simple](examples/simple.md) or [edge case](examples/edge-case.md) only when useful. [Routing cases](tests/routing.json) record positive and negative activation examples for review; they are not a model benchmark.
