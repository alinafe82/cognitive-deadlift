---
name: skill-deprecation-review
description: "Review whether a stale, overlapping, unused, or harmful skill should be kept, merged, renamed, archived, or deleted. Use when a skill overlaps with another, stops matching repo purpose, has weak usage evidence, or creates routing confusion. NOT for adding new skills or for minor edits that keep scope intact."
---

# Skill Deprecation Review

## Purpose

Keep the skill set small, memorable, and aligned with real repeated work.

## Preserves

Curation judgment and maintenance discipline.

## Required Evidence

- Skill path and current description.
- Usage evidence or absence of usage evidence.
- Nearby skills and overlap notes.
- Risks of keeping, changing, or removing the skill.

## Failure Signs

- A skill is kept because it sounds useful without usage or distinct scope.
- Deletion is recommended without checking adapter and index impacts.
- The review ignores migration guidance for users.

## When To Use

- A skill overlaps with another skill.
- A skill is stale, unused, or hard to trigger correctly.
- The skill set is being pruned.
- A skill no longer matches repo purpose or quality bar.

## When Not To Use

- A new skill is being proposed; use skill-authoring-gate.
- The issue is only trigger overlap for a proposed addition; use skill-overlap-audit.
- The task is a typo or example refresh.

## Inputs Expected

- Skill folder or SKILL.md text.
- Catalog and skill index entries.
- Usage notes, transcript evidence, or reviewer reports.
- Nearby skills and runtime adapter references.

## Output Expected

```md
Skill:
Current job:
Usage evidence:
Overlap or staleness:
Options:
Recommendation:
Migration and cleanup:
```

## Process

1. Identify the skill's current preserved ability and trigger surface.
2. Check usage evidence, examples, and current fit with repo purpose.
3. Compare with nearby skills for merge or rename options.
4. Evaluate risks of keeping versus removing.
5. If deprecating, list required updates to catalog, index, adapters, docs, and tests.

## Quality Bar

A good deprecation review protects users from churn while removing skills that dilute routing or quality.

## Examples

Simple case: Review whether to keep a skill that duplicates docs-claim-audit. The skill should compare distinct jobs and usage evidence.

Complex case: Review a popular but broad skill that overlaps with five narrower skills. The skill should consider migration path before deletion.

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
