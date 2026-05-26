# Skill Standard

A skill is a reusable engineering instruction artifact. It is not a prompt dump.

## Required Files

```text
skills/<skill-name>/
├── SKILL.md
├── examples/
├── tests/
└── fixtures/
```

`examples/`, `tests/`, and `fixtures/` may contain short markdown notes, but the directories must exist so every skill has a consistent review surface.

## Required `SKILL.md` Sections

Each skill must include:

1. `Purpose`
2. `When To Use`
3. `When Not To Use`
4. `Inputs Expected`
5. `Output Expected`
6. `Process`
7. `Quality Bar`
8. `Examples`
9. `Failure Modes`
10. `Safety And Privacy`
11. `Anti-Slop Rules`

## Metadata

Frontmatter must include:

- `name`
- `description`

The `description` must explain:

- what the skill does
- when it should activate
- when it should not activate

Use this pattern:

```yaml
description: "Do X for Y. Use when ... NOT for ..."
```

## Good Skill Requirements

A good skill has:

- a clear name
- a real developer problem
- clear trigger conditions
- clear non-trigger conditions
- explicit inputs
- explicit outputs
- constraints and boundaries
- simple and complex examples
- failure-mode behavior
- safety and privacy notes
- no hidden assumptions
- no unsupported claims
- no generic filler
- no confusing overlap with another skill

## Examples

Every skill must include at least two examples:

- simple case
- complex case or edge case

Examples should show realistic input and expected output shape. They do not need to be long.

## Failure Modes

Every skill must say what to do when:

- required files are missing
- context is ambiguous
- permissions are missing
- tests fail
- the user asks for unsafe behavior
- the assistant cannot verify a claim

## Safety And Privacy

Every skill must explicitly protect:

- secrets
- tokens
- private keys
- private employer details
- customer names
- personal data
- legal, medical, and financial high-stakes claims
- destructive operations

## Anti-Slop Rules

Every skill must forbid:

- generic summaries
- fake certainty
- unsupported claims
- unnecessary verbosity
- boilerplate
- pretending a check was run when it was not
- vague praise
- buzzword stuffing

## Banned Filler

Do not use inflated marketing language or vague praise in skill instructions. The exact banned phrase list is enforced in `scripts/validate_skills.py` so it can be tested without duplicating policy text across docs and code.

## Review Standard

If a skill cannot explain what problem it solves, when it triggers, what output it produces, and how it fails safely, do not merge it.
