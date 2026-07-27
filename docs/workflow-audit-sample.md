# Workflow Audit Sample

This sample shows the shape of a Cognitive Deadlift Workflow Audit without using
private client material.

It is illustrative. A paid audit is based on the team's actual pull requests,
tickets, change writeups, or agent instruction files.

## Sample Inputs

- Three recent pull requests where an AI assistant wrote or changed code.
- One bugfix ticket that moved through review without a failing test first.
- Current agent instructions, review checklist, and CI gate summary.
- A short note from the team lead naming the workflow they want to improve.

Do not send secrets, production credentials, customer data, or private incident
details in first contact.

## Sample Findings

| Area | Signal | Risk |
| --- | --- | --- |
| Problem framing | Two PRs started from implementation requests without a named user symptom. | The assistant can solve the wrong problem quickly. |
| Code tracing | One change edited a nearby helper without proving it was on the runtime path. | Reviewers have to infer whether the patch reaches production behavior. |
| Test evidence | The bugfix PR added a passing test after the implementation but no failing signal. | Regressions can be masked by broad happy-path coverage. |
| Diff review | Generated docs were accepted without a claim audit against source files. | Public claims can drift beyond what the repo actually supports. |

## Recommended Workflow

Use a light gate for normal feature work:

1. `problem-framing` before implementation when the actor or symptom is unclear.
2. `trace-the-code` before editing shared behavior.
3. `failing-test-first` for bugfixes and behavior changes.
4. `diff-interrogation` before merge.
5. `explain-without-ai` for handoff when the mechanism is not obvious.

Use the high-risk thinking budget for security, permissions, data, public API,
destructive behavior, migrations, and production config changes.

## First Three Adoption Steps

1. Add a pull request checklist item requiring the agent to name the observed
   failure, touched code path, and verification command.
2. Require one failing signal before bugfix implementation unless the lead
   explicitly records why that is impractical.
3. Add a weekly review of two AI-assisted PRs using `docs-claim-audit` and
   `diff-interrogation` to calibrate reviewer expectations.

## Out Of Scope

- Security penetration testing.
- Incident response.
- Rewriting the team's development process.
- Guaranteeing that an AI assistant will follow every instruction.
- Commercial licensing of Cognitive Deadlift content.
