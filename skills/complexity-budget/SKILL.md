---
name: complexity-budget
description: "Review whether proposed abstractions or infrastructure justify their maintenance and operational cost."
---

# Complexity Budget

Make the future maintenance cost of new moving parts explicit before they are added.

## Scope

Use for the task in the description. For example: Review whether one caller justifies adding a new service and queue. Do not activate for: Remove this unused helper with no replacement abstraction.

## Workflow

1. List new concepts, dependencies, states, and failure modes.
2. Separate essential complexity from optional complexity.
3. Compare with the boring alternative.
4. Define how the abstraction could be deleted later.
5. Recommend proceed, simplify, defer, or reject.

## Evidence

Proposed design or implementation plan. New components, dependencies, states, or failure modes. Expected benefit, expected lifetime, and deletion path. Report the outcome with relevant new moving parts, essential complexity, optional complexity, boring alternative. Adapt the format to the task; omit empty fields. Never claim checks ran without observed results.

## Boundaries

Do not include confidential architecture diagrams, private vendor contracts, or customer-specific operational details. Use abstract component names when needed. Continue authorized read-only and reversible local work through the requested outcome. If evidence is missing, inspect available sources before asking; report limits honestly.

## References

For worked examples, open [simple](examples/simple.md) or [edge case](examples/edge-case.md) only when useful. [Routing cases](tests/routing.json) record positive and negative activation examples for review; they are not a model benchmark.
