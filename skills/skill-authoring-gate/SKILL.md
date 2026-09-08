---
name: skill-authoring-gate
description: "Review a new or materially changed skill for distinct purpose, useful routing, and executable guidance."
---

# Skill Authoring Gate

Make every new or changed skill prove it belongs before it enters the skill set.

## Scope

Use for the task in the description. For example: Review whether this new parser-debugging skill is useful and correctly scoped. Do not activate for: Fix a typo in a skill title.

## Workflow

1. Name the repeated developer problem the skill preserves judgment around.
2. Check that the description identifies a specific task and routing examples distinguish neighboring tasks.
3. Compare required evidence to the work the skill claims to gate.
4. Inspect simple and edge-case examples for realistic input and output shape.
5. Check handling of missing evidence and the data/action risks actually present in the workflow.
6. Recommend accept, revise, merge with another skill, or reject.

## Evidence

Proposed skill name and body or draft. Problem the skill solves and evidence that it repeats. Nearby skills, examples, expected output, and failure handling. Report the outcome with relevant skill, repeated problem, trigger, non-trigger. Adapt the format to the task; omit empty fields. Never claim checks ran without observed results.

## Boundaries

Keep secrets and private records out of shared artifacts. Use redacted or synthetic evidence. External sends, publication, destructive operations and permission widening need explicit authorization; reuse authorization already given for the action. Continue authorized read-only and reversible local work through the requested outcome. If evidence is missing, inspect available sources before asking; report limits honestly.

## References

For worked examples, open [simple](examples/simple.md) or [edge case](examples/edge-case.md) only when useful. [Routing cases](tests/routing.json) record positive and negative activation examples for review; they are not a model benchmark.
