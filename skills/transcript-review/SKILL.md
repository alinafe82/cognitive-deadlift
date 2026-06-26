---
name: transcript-review
description: "Review real agent transcripts against expected skill behavior. Use when a Codex, Claude, Gemini, or other agent session needs review to see whether the assistant followed the named skill, skipped evidence, overclaimed checks, or exposed a rubric gap. NOT for reviewing source diffs directly or for hypothetical skill design without a transcript."
---

# Transcript Review

## Purpose

Turn real agent sessions into evidence about whether skills work in practice.

## Preserves

Review judgment and skill-behavior calibration.

## Required Evidence

- Transcript or session excerpt.
- Skill or skills expected to apply.
- Task context and any tool outputs the agent claimed to use.
- Known outcome if available.

## Failure Signs

- The review judges tone instead of evidence behavior.
- The assistant's claimed checks are accepted without tool output or artifacts.
- Rubric improvements are not tied to a concrete missed behavior.

## When To Use

- A real agent session is available for review.
- A skill may not have activated when it should have.
- A harness or rubric missed a behavior gap.
- A team wants to improve skills from actual usage.

## When Not To Use

- No transcript or concrete session evidence is available.
- The request is a normal code review; use diff-interrogation.
- The task is designing a new skill from scratch; use skill-authoring-gate.

## Inputs Expected

- Transcript text or exported session.
- Expected skill names and their SKILL.md files if available.
- Commands, files, or outputs referenced by the agent.
- Reviewer question or failure hypothesis.

## Output Expected

```md
Session:
Expected skill behavior:
Evidence followed:
Evidence skipped:
Unsupported claims:
Rubric misses:
Recommended skill or harness edits:
```

## Process

1. Identify the user request, risk level, and expected skill triggers.
2. Compare the agent response to each expected output contract.
3. Mark every claimed check as supported, unsupported, or unverifiable from the transcript.
4. Separate agent failure from skill wording failure.
5. Recommend concrete changes to skill body, examples, harness rubric, or validation process.

## Quality Bar

A good transcript review produces evidence-backed findings and at least one concrete improvement when the session exposes a repeatable miss.

## Examples

Simple case: Review a transcript where the agent used diff-interrogation before merging a small validator change. The skill should check whether behavior change, risk lines, missing proof, and recommendation were covered.

Complex case: Review a long session where the agent used problem-framing but still implemented before tracing code. The skill should separate problem-framing compliance from trace-the-code failure.

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
