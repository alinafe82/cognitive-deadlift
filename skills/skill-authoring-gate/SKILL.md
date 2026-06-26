---
name: skill-authoring-gate
description: "Gate new or changed skills before review. Use when adding, rewriting, or materially expanding a skill and the author needs to prove the skill has a real repeated problem, clear trigger, non-trigger, evidence contract, failure modes, and examples. NOT for typo-only skill edits or mechanical catalog/index updates."
---

# Skill Authoring Gate

## Purpose

Make every new or changed skill prove it belongs before it enters the skill set.

## Preserves

Skill design judgment and trigger discipline.

## Required Evidence

- Proposed skill name and body or draft.
- Problem the skill solves and evidence that it repeats.
- Nearby skills, examples, expected output, and failure handling.

## Failure Signs

- The skill reads like a prompt collection entry instead of a reusable workflow.
- The trigger is broad enough to fire on unrelated requests.
- Examples show only happy paths or omit expected output shape.

## When To Use

- A new skill is being added.
- An existing skill is being materially rewritten or expanded.
- A reviewer cannot tell whether the skill has a distinct job.
- A skill lacks examples, evidence requirements, or failure-mode behavior.

## When Not To Use

- Typo-only edits that do not change scope or behavior.
- Mechanical catalog, manifest, or index updates with no skill body change.
- Deleting a skill; use skill-deprecation-review instead.

## Inputs Expected

- Skill draft or path to the skill folder.
- Intended user request examples.
- Existing nearby skills and repo skill standard.
- Validation output if available.

## Output Expected

```md
Skill:
Repeated problem:
Trigger:
Non-trigger:
Required evidence:
Examples checked:
Failure handling:
Recommendation:
```

## Process

1. Name the repeated developer problem the skill preserves judgment around.
2. Check that the description contains specific trigger and non-trigger language.
3. Compare required evidence to the work the skill claims to gate.
4. Inspect simple and edge-case examples for realistic input and output shape.
5. Confirm failure modes cover missing files, ambiguity, permissions, failed checks, unsafe requests, and unverifiable claims.
6. Recommend accept, revise, merge with another skill, or reject.

## Quality Bar

A good gate decision explains why the skill should exist, when it should activate, and what proof would catch a weak implementation.

## Examples

Simple case: Review a proposed skill named api-docs-check before adding it. The skill should identify the repeated problem the skill solves.

Complex case: Review a broad skill named better-coding that overlaps with problem-framing, trace-the-code, and diff-interrogation. The skill should reject the broad name and scope.

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
