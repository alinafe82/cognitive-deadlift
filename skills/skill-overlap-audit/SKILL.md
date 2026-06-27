---
name: skill-overlap-audit
description: "Audit overlap between proposed or existing skills. Use when adding a skill near an existing skill, renaming a skill, splitting a skill, or reviewing a skill set that may be drifting into duplicate prompts. NOT for standalone skill edits with no nearby skill or for catalog formatting changes."
---

# Skill Overlap Audit

## Purpose

Prevent the skill set from becoming a set of near-duplicate prompts.

## Preserves

Conceptual boundaries and retrieval precision.

## Required Evidence

- Proposed skill name, description, and body if available.
- List of existing nearby skills and their descriptions.
- Concrete trigger examples and non-trigger examples.

## Failure Signs

- Two skills would activate for the same request without a clear order.
- The proposed skill differs only by wording, not workflow or evidence.
- The audit recommends adding a skill without naming what existing skill cannot cover.

## When To Use

- A new skill resembles an existing one.
- A reviewer suspects duplicate scope.
- A broad skill may need splitting into smaller gates.
- A skill name or description is changing enough to affect routing.

## When Not To Use

- The change is a typo or formatting edit.
- The skill has no plausible neighbors.
- The task is deciding whether to delete a stale skill; use skill-deprecation-review.

## Inputs Expected

- Candidate skill metadata and body.
- Current skill index or catalog.
- Examples of requests that should and should not trigger the skill.
- Any known confusion from real usage.

## Output Expected

```md
Candidate skill:
Nearby skills:
Shared surface:
Distinct job:
Trigger boundary:
Recommendation:
Required edits:
```

## Process

1. List the existing skills that could fire on the same request.
2. Compare preserved ability, required evidence, process, and output shape.
3. Classify overlap as acceptable sequence, confusing duplicate, missing boundary, or true distinct skill.
4. Recommend merge, rename, split, reject, or proceed.
5. Write the exact description or body edits needed to make the boundary clear.

## Quality Bar

A good audit leaves a future router or reviewer able to pick exactly one skill, or a deliberate sequence of skills, for a realistic request.

## Examples

Simple case: Compare a proposed docs-claim-audit skill against read-the-docs-first. The skill should show that read-the-docs-first gathers sources before claims.

Complex case: Compare a proposed plan-check skill against problem-framing, assumption-audit, and alternatives-before-code. The skill should identify overlapping plan validation behavior.

See `examples/simple.md` and `examples/edge-case.md`.

## Failure Modes

- Required files missing: state what could not be checked and ask for the smallest missing artifact.
- Context ambiguous: list the plausible interpretations and pick the one that affects the decision most.
- Permissions missing: name the command, file, or approval needed without inventing results.
- Tests or checks fail: report the failure and do not recommend acceptance until the failure is understood.
- Unsafe request: refuse the unsafe step and offer a safe review or evidence-gathering path.
- Claim cannot be verified: mark it as unsupported and require evidence or limitation language.

## Safety And Privacy

Do not request or expose secrets, tokens, private keys, customer records, private employer details, personal data, or production credentials. Use redacted examples and require approval before destructive, external-send, permission-widening, or publication actions.

## Anti-Slop Rules

- Do not approve a skill, claim, release, or workflow on confident wording alone.
- Do not treat file presence as evidence of substance.
- Do not invent command results, runtime behavior, usage evidence, or reviewer approval.
- Do not broaden scope to make the recommendation sound more useful.
- Do not hide missing evidence in a generic summary.
