---
name: good-skill
description: "Validate a well-formed fixture skill. Use when testing the validator happy path. NOT for production assistant behavior."
---

# Good Skill

## Purpose

Provide a valid fixture.

## When To Use

- During validator tests.

## When Not To Use

- During production assistant work.

## Inputs Expected

- Fixture repository path.

## Output Expected

```md
Result:
```

## Process

1. Read the fixture.
2. Return a result.

## Quality Bar

The fixture passes validation for structural reasons.

## Examples

See `examples/simple.md` and `examples/edge-case.md`.

## Failure Modes

- Missing fixture files should fail validation.

## Safety And Privacy

No private data is used.

## Anti-Slop Rules

- Do not add filler.
