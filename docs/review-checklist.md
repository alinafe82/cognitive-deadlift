# Review Checklist

Use this checklist for every skill change.

## Problem Fit

- Does the skill solve a real repeated developer problem?
- Would an engineer actually use it during coding, review, debugging, or design?
- Is it more than a generic prompt?
- Is the skill narrow enough to be memorable?

## Activation

- Is the trigger condition clear?
- Is the `NOT for` boundary clear?
- Could it fire on unrelated requests?
- Does it overlap confusingly with another skill?

## Instructions

- Are the steps specific enough to execute?
- Are the inputs explicit?
- Are the outputs explicit?
- Are examples included?
- Are edge cases covered?
- Is the language direct and natural?

## Safety

- Could this leak secrets, private data, customer data, or employer details?
- Could it encourage destructive operations?
- Could it make legal, medical, or financial claims without appropriate caution?
- Does it require confirmation for risky actions?
- Does it avoid pretending that checks were run?

## Validation

- Does `python scripts/validate_skills.py` pass?
- Does `python -m pytest` pass?
- Does `make check` pass?
- Are examples present and readable?
- Are internal links valid?

## Maintainability

- Is the skill body concise?
- Are examples close to the skill?
- Are fixtures useful rather than decorative?
- Are runtime adapters still consistent?
- Are catalogs updated if the skill was added, renamed, or removed?

## Decision

Approve only if:

- the skill has a clear purpose
- the skill has clear activation boundaries
- examples are realistic
- validation passes
- no private or unsafe content is introduced
- the reviewer can explain why this belongs in the repo
