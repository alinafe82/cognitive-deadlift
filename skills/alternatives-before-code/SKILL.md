---
name: alternatives-before-code
description: "Compare viable solution paths before implementation. Use when architecture, refactors, data model changes, workflow changes, tool choices, or irreversible decisions make the first idea too sticky. NOT for one-line fixes, constrained chores, or changes with only one safe path."
---

# Alternatives Before Code

## Purpose

Prevent the first plausible implementation from becoming the decision by default.

## When To Use

- The change affects architecture, data shape, workflow, dependencies, or public behavior.
- Multiple implementation strategies are plausible.
- Reversibility, blast radius, or testability matters.
- The user has already anchored on one solution.

## When Not To Use

- One-line fixes with obvious verification.
- Formatting, renames, generated files, or lockfile-only work.
- Emergency mitigation where delay would increase impact.

## Inputs Expected

- Decision to be made.
- Constraints such as time, compatibility, migration risk, ownership, and test surface.
- Existing architecture notes, ADRs, or code boundaries if available.

## Output Expected

```md
Decision:
Option A - Minimal:
Option B - Structural:
Option C - Conservative/no-build:
Recommendation:
Change-my-mind evidence:
```

## Process

1. Name the decision in one sentence.
2. Produce a minimal option, a structural option, and a conservative/no-build option.
3. Compare cost, reversibility, blast radius, testability, and cognitive load.
4. Recommend one option.
5. State what evidence would change the recommendation.

## Quality Bar

A good alternatives pass makes the tradeoff obvious enough that a reviewer can disagree with the recommendation without first reconstructing the decision.

## Examples

Simple case: "Should we add a config flag or hardcode this timeout?" The skill should compare local constant, config flag, and no-change options.

Complex case: "Should failed billing sync move to a queue?" The skill should compare synchronous retry, scheduled retry, queue-based retry, and no-build operational mitigation.

See `examples/simple.md` and `examples/edge-case.md`.

## Failure Modes

- Only one option appears viable: explain which constraints eliminated the others.
- Missing architecture context: inspect ADRs or code before recommending.
- Emergency request: recommend immediate mitigation and defer deeper alternatives.
- The boring option looks worse: explain the specific cost it fails to handle.

## Safety And Privacy

Do not include private vendor details, customer names, or confidential architecture diagrams. Use generic labels when examples need sensitive context.

## Anti-Slop Rules

- Do not create fake options just to fill a template.
- Do not hide the no-build option.
- Do not recommend a complex option without naming the complexity it buys.
- Do not use vague tradeoff words without specifics.

