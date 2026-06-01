---
name: assumption-audit
description: "Find and challenge hidden assumptions in a plan, prompt, bug report, design, or AI-generated answer. Use when claims are unverified, something is called obvious or safe, or a plan depends on external behavior. NOT for confirmed requirements or tiny mechanical edits."
---

# Assumption Audit

## Purpose

Make unverified claims visible before they become implementation decisions.

## Preserves

Evidence-based judgment.

## Required Evidence

- Proposed plan, answer, or design.
- Claims the plan depends on.
- Available code, docs, logs, tests, metrics, or constraints.

## Failure Signs

- Confidence is treated as proof.
- The riskiest assumption is buried.
- Locally checkable claims are sent back to the user instead of verified.

## When To Use

- A plan depends on behavior that has not been checked.
- The user or assistant says "obviously", "just", "safe", or "simple".
- A design depends on API, framework, runtime, user, or operational assumptions.
- AI produced a fluent answer without evidence.

## When Not To Use

- Requirements already verified by tests, docs, or code references.
- Cosmetic changes with no behavioral or operational effect.
- Early brainstorming where evaluation is explicitly deferred.

## Inputs Expected

- Proposed plan, answer, or design.
- Any available code, docs, logs, tests, metrics, or constraints.
- The decision that depends on the assumptions.

## Output Expected

```md
Verified:
Likely but unproven:
Risky:
Unknown:
Recommended next check:
```

## Process

1. Extract concrete assumptions from the plan.
2. Classify each as factual, technical, product, operational, or social.
3. Check locally verifiable assumptions in code or docs before asking the user.
4. Mark each assumption as verified, likely, risky, or unknown.
5. Recommend the next check that would most change the decision.

## Quality Bar

A good audit changes behavior: it either verifies the plan, narrows it, or exposes a risk that must be resolved before implementation.

## Examples

Simple case: "This endpoint is idempotent, so retries are safe." The skill should verify idempotency in code or mark the retry plan as risky.

Complex case: "We can cache permission checks because role changes are rare." The skill should identify assumptions about role update frequency, cache invalidation, stale access risk, and audit requirements.

See `examples/simple.md` and `examples/edge-case.md`.

## Failure Modes

- No code access: mark technical claims as unverified and ask for the smallest source needed.
- Too many assumptions: rank by blast radius and reversibility.
- User refuses delay: document the unverified assumption and recommend the smallest reversible step.
- External docs may be stale: cite access date when browsing is used.

## Safety And Privacy

Do not request raw secrets, customer data, private contracts, or internal incident details. Ask for redacted evidence or aggregate behavior.

## Anti-Slop Rules

- Do not list generic assumptions that do not affect the decision.
- Do not treat confidence as proof.
- Do not ask the user for facts the repo can answer.
- Do not bury the highest-risk assumption.
