---
name: explain-without-ai
description: "Require a plain-language mechanism explanation before shipping, handoff, or review. Use when changes are largely AI-generated, learning-focused, or the developer may not understand the code. NOT for trivial edits, generated artifacts, or explanations already captured in a thinking ledger."
---

# Explain Without AI

## Purpose

Make the developer own the mechanism, tradeoff, and failure risk of the work.

## When To Use

- A diff was mostly AI-generated.
- A developer is learning a new API, library, or code path.
- A change is large enough that review needs mechanism-level context.
- The developer can describe the outcome but not how it works.

## When Not To Use

- Trivial edits where the mechanism is obvious.
- Generated artifacts validated elsewhere.
- Work with a recent thinking ledger that already explains mechanism and tradeoffs.

## Inputs Expected

- Plan, diff, algorithm, incident summary, or learning task.
- Relevant code references or docs.
- The decision or behavior that must be explained.

## Output Expected

```md
Plain explanation:
Mechanism:
Rejected alternative:
Breakage test:
Confidence gap:
```

## Process

1. Explain the mechanism in plain language.
2. Name the relevant code path or decision boundary.
3. Explain why the selected approach beats the obvious alternative.
4. Define what would break if the explanation is wrong.
5. Identify any remaining confidence gap.

## Quality Bar

A good explanation is falsifiable. A reviewer should be able to point to the breakage test and decide whether the developer understands the change.

## Examples

Simple case: a developer changed date parsing. The skill should explain accepted input, rejected input, timezone behavior, and the test that would catch a mistaken explanation.

Complex case: a model wrote a caching layer. The skill should explain cache key choice, invalidation, stale-read risk, and the rejected no-cache alternative.

See `examples/simple.md` and `examples/edge-case.md`.

## Failure Modes

- Explanation is vague: ask one focused mechanism question.
- Code is unavailable: explain only from provided context and mark code evidence unchecked.
- User cannot explain a risky diff: recommend blocking merge until the mechanism is understood.
- High-stakes domain: avoid giving legal, medical, or financial conclusions without expert review.

## Safety And Privacy

Do not require the user to disclose secrets, customer details, private employer data, or confidential architecture. Ask for redacted mechanisms and public abstractions.

## Anti-Slop Rules

- Do not accept "AI generated it" as an explanation.
- Do not use buzzwords instead of mechanism.
- Do not describe only the happy path.
- Do not pretend confidence when the developer cannot explain the code.

