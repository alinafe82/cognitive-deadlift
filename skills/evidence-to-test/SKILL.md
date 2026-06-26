---
name: evidence-to-test
description: "Convert qualitative repo gaps or repeated failures into deterministic tests, fixtures, validators, or checks. Use when a gap, false confidence pattern, validator miss, or repeated review failure should become executable evidence. NOT for writing implementation code before the observable failure is defined or for broad test-suite expansion without a specific gap."
---

# Evidence To Test

## Purpose

Turn review concerns into repeatable proof instead of recurring discussion.

## Preserves

Test design and validation judgment.

## Required Evidence

- Gap or repeated failure described in concrete terms.
- Observable bad behavior or missing invariant.
- Existing test or validator surface.
- Expected failing signal before the fix.

## Failure Signs

- A test is added because coverage is low, not because a gap is defined.
- The proposed check only asserts implementation details.
- The fix is written before the failing signal is named.

## When To Use

- A repo review finds a validator gap.
- A repeated agent failure should be captured in a harness fixture.
- A qualitative claim needs executable proof.
- A bug or docs drift should become a regression check.

## When Not To Use

- The request already has a precise failing test.
- The task is exploratory debugging; use debugging-lab-notebook.
- The desired behavior is not yet understood enough to test.

## Inputs Expected

- Gap description or failure example.
- Relevant code, docs, validator, or harness files.
- Existing tests and commands.
- Acceptance criteria for the new check.

## Output Expected

```md
Gap:
Observable failure:
Best test surface:
Fixture needed:
Expected red signal:
Passing proof:
Scope limits:
```

## Process

1. Restate the gap as an invariant that can fail.
2. Choose the narrowest test surface: unit test, validator fixture, harness case, slop scan, or command check.
3. Define the red signal before proposing the fix.
4. Name fixture data needed to prove the behavior without private data.
5. Keep the check deterministic, fast, and aligned with the repo contract.

## Quality Bar

A good result gives another engineer enough detail to write the failing check before changing behavior.

## Examples

Simple case: A validator misses stale PR template wording. The skill should define a fake PR template fixture with the stale command.

Complex case: Agent transcripts often claim tests passed without command output. The skill should choose a harness fixture or transcript-review rubric rather than a unit test.

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
