---
name: skill-deprecation-review
description: "Assess whether an existing skill should be retained, merged, renamed, or retired, including migration impacts."
---

# Skill Deprecation Review

Keep the skill set small, memorable, and aligned with real repeated work.

## Scope

Use for the task in the description. For example: Assess retiring an unused skill and migrating its adapter references. Do not activate for: Propose a new skill with no retirement decision.

## Workflow

1. Identify the skill's current preserved ability and trigger surface.
2. Check usage evidence, examples, and current fit with repo purpose.
3. Compare with nearby skills for merge or rename options.
4. Evaluate risks of keeping versus removing.
5. If deprecating, list required updates to catalog, index, adapters, docs, and tests.

## Evidence

Skill path and current description. Usage evidence or absence of usage evidence. Nearby skills and overlap notes. Risks of keeping, changing, or removing the skill. Report the outcome with relevant skill, current job, usage evidence, overlap or staleness. Adapt the format to the task; omit empty fields. Never claim checks ran without observed results.

## Boundaries

Keep secrets and private records out of shared artifacts. Use redacted or synthetic evidence. External sends, publication, destructive operations and permission widening need explicit authorization; reuse authorization already given for the action. Continue authorized read-only and reversible local work through the requested outcome. If evidence is missing, inspect available sources before asking; report limits honestly.

## References

For worked examples, open [simple](examples/simple.md) or [edge case](examples/edge-case.md) only when useful. [Routing cases](tests/routing.json) record positive and negative activation examples for review; they are not a model benchmark.
