---
name: problem-framing
description: "Turn an unclear request into a concrete engineering problem statement before implementation. Use when the user jumps to code, proposes a solution without the underlying problem, or asks for a fix without reproduction. NOT for pure formatting, copy edits, or already-scoped mechanical changes."
---

# Problem Framing

## Purpose

Make the assistant define the real problem before it designs or writes code.

## When To Use

- The request starts with an implementation idea instead of a problem.
- A bug report lacks reproduction evidence.
- A feature request mixes goals, constraints, and solution guesses.
- Success is described as "make it work" rather than a verifiable outcome.

## When Not To Use

- Pure formatting, typo fixes, or copy edits.
- Mechanical dependency bumps with clear validation.
- Work already framed by a current issue, PRD, failing test, or incident note.

## Inputs Expected

- User request or issue summary.
- Any known symptom, affected workflow, user, logs, screenshots, or failing command.
- Relevant constraints, deadlines, or non-goals if known.

## Output Expected

```md
Problem:
Current evidence:
Assumptions:
Non-goals:
Success condition:
First verification step:
```

## Process

1. Restate the request as a problem, not a solution.
2. Identify actor, workflow, boundary, and observable symptom.
3. Separate facts from interpretation.
4. Name assumptions that still need checking.
5. Define success as a test, command, user-visible outcome, or reviewable signal.
6. If the problem cannot be framed, ask one focused question.

## Quality Bar

A good frame lets another engineer understand what is wrong, what is out of scope, and what proof would make the fix credible.

## Examples

Simple case: user says "Add retries to the webhook worker." The skill should ask what failure is being retried, where the failure is observed, and what success signal proves retries help.

Complex case: user says "Move billing sync to a queue because customers are missing invoices." The skill should separate the customer-visible invoice failure from the proposed queue solution and require evidence from logs, current sync behavior, and acceptance criteria.

See `examples/simple.md` and `examples/edge-case.md`.

## Failure Modes

- Missing evidence: state what is missing and ask one question.
- Files unavailable: frame only from the prompt and mark code evidence as unchecked.
- Ambiguous actor or workflow: list the plausible interpretations and recommend the one to verify first.
- Urgent incident: create the shortest useful frame and defer non-critical detail.

## Safety And Privacy

Do not ask for secrets, customer records, private employer details, or production credentials. If examples contain private data, request redacted logs or synthetic identifiers.

## Anti-Slop Rules

- Do not summarize the request as if it were already clear.
- Do not claim the problem is verified without evidence.
- Do not produce a solution plan until the output contract is filled.
- Do not use filler or motivational language.

