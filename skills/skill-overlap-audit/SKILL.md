---
name: skill-overlap-audit
description: "Compare overlapping skill triggers and workflows to resolve ambiguous selection."
---

# Skill Overlap Audit

Prevent the skill set from becoming a set of near-duplicate prompts.

## Scope

Use for the task in the description. For example: Compare the triggers of resume writing and resume tailoring skills. Do not activate for: Correct spelling in a single example.

## Workflow

1. List the existing skills that could fire on the same request.
2. Compare preserved ability, required evidence, process, and output shape.
3. Classify overlap as acceptable sequence, confusing duplicate, missing boundary, or true distinct skill.
4. Recommend merge, rename, split, reject, or proceed.
5. Write the exact description or body edits needed to make the boundary clear.

## Evidence

Proposed skill name, description, and body if available. List of existing nearby skills and their descriptions. Concrete trigger examples and non-trigger examples. Report the outcome with relevant candidate skill, nearby skills, shared surface, distinct job. Adapt the format to the task; omit empty fields. Never claim checks ran without observed results.

## Boundaries

Keep secrets and private records out of shared artifacts. Use redacted or synthetic evidence. External sends, publication, destructive operations and permission widening need explicit authorization; reuse authorization already given for the action. Continue authorized read-only and reversible local work through the requested outcome. If evidence is missing, inspect available sources before asking; report limits honestly.

## References

For worked examples, open [simple](examples/simple.md) or [edge case](examples/edge-case.md) only when useful. [Routing cases](tests/routing.json) record positive and negative activation examples for review; they are not a model benchmark.
