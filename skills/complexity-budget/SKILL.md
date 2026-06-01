---
name: complexity-budget
description: "Challenge unnecessary abstraction, dependencies, and indirection before adding them. Use when a solution adds modules, frameworks, queues, caches, state machines, agents, configuration layers, or hard-to-delete architecture. NOT for small local changes, deletion-only refactors, or accepted ADRs."
---

# Complexity Budget

## Purpose

Make the future maintenance cost of new moving parts explicit before they are added.

## Preserves

Systems thinking and operational judgment.

## Required Evidence

- Proposed design or implementation plan.
- New components, dependencies, states, or failure modes.
- Expected benefit, expected lifetime, and deletion path.

## Failure Signs

- Abstraction is justified as cleaner without a concrete future requirement.
- Operational ownership is ignored.
- The boring alternative is not considered.

## When To Use

- A change adds a dependency, framework, queue, cache, state machine, agent, or abstraction.
- A plan makes code more generic than the current need.
- The solution is hard to delete later.
- Ownership, operations, or onboarding cost may increase.

## When Not To Use

- Small local changes with no new abstraction.
- Deletion-only refactors that reduce moving parts.
- Architecture already justified by a current ADR.

## Inputs Expected

- Proposed design or implementation plan.
- New components, dependencies, states, or failure modes.
- Existing ADRs or constraints if relevant.
- Expected benefit and expected lifetime of the added complexity.

## Output Expected

```md
New moving parts:
Essential complexity:
Optional complexity:
Boring alternative:
Deletion path:
Recommendation:
```

## Process

1. List new concepts, dependencies, states, and failure modes.
2. Separate essential complexity from optional complexity.
3. Compare with the boring alternative.
4. Define how the abstraction could be deleted later.
5. Recommend proceed, simplify, defer, or reject.

## Quality Bar

A good budget shows what future engineers will have to understand and why that cost is worth paying now.

## Examples

Simple case: adding a new helper class for one call site. The skill should ask whether a function is enough and what future variation justifies the class.

Complex case: adding a queue and retry worker. The skill should account for delivery semantics, observability, idempotency, ownership, and deletion path.

See `examples/simple.md` and `examples/edge-case.md`.

## Failure Modes

- Benefit is unclear: recommend the boring alternative or a reversible experiment.
- Existing ADR conflicts: follow the ADR or write a new decision record before changing direction.
- Scale is unknown: state the threshold that would justify the complexity.
- Urgent mitigation: defer structural complexity until the incident is contained.

## Safety And Privacy

Do not include confidential architecture diagrams, private vendor contracts, or customer-specific operational details. Use abstract component names when needed.

## Anti-Slop Rules

- Do not call complexity "future-proofing" without a concrete future requirement.
- Do not ignore deletion cost.
- Do not hide operational ownership.
- Do not recommend abstraction because it feels cleaner.
