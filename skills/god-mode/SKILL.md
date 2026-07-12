---
name: god-mode
description: "Route broad or high-ambiguity requests through the smallest useful sequence of existing skills. Use when the user asks for god mode, all skills, maximum capability, end-to-end autonomous work, or a task that spans implementation, review, architecture, safety, and handoff. NOT for simple single-skill requests, literal claims of universal expertise, bypassing permissions, or skipping verification."
---

# God Mode

## Purpose

Coordinate complex work by selecting, sequencing, and verifying the relevant existing skills instead of pretending one generic skill can do every job.

## Preserves

Skill routing judgment, scope control, and operational discipline under broad requests.

## Required Evidence

- User goal, constraints, and requested autonomy level.
- Available skill names, descriptions, or local skill paths checked for this session.
- Risk level and the evidence required by that risk.
- Selected skill sequence and at least one skill intentionally skipped.
- Verification commands, source files, or review artifacts used before confidence.

## Failure Signs

- The assistant says it used every skill without listing what was available.
- The response skips a narrower skill that clearly applies.
- The assistant claims access to skills, tools, documents, or permissions it has not verified.
- The plan maximizes activity instead of choosing the smallest useful sequence.
- The final answer hides failed checks, missing evidence, or unresolved risk.

## When To Use

- The user explicitly asks for "god mode," "all skills," "maximum capability," or similar broad orchestration.
- A task crosses multiple phases such as framing, code reading, tests, implementation, diff review, security, and handoff.
- The assistant needs to decide whether several skills should run in sequence.
- A broad request risks becoming autopilot unless skill routing and evidence are explicit.

## When Not To Use

- A specific narrower skill already covers the full request.
- The work is a typo, formatting change, or other mechanical low-risk task.
- The user asks to bypass permissions, tests, review, safety checks, or human approval.
- The request depends on unavailable private data, credentials, or tools.
- The only interpretation is a literal claim to universal knowledge or unrestricted capability.

## Inputs Expected

- User request.
- Skill list, catalog, or local skill directory when available.
- Repo instructions, risk policy, and relevant context packs when the task is in a repo.
- Current files, diffs, command outputs, logs, issues, or artifacts needed to verify the work.

## Output Expected

```md
Goal:
Risk:
Available skills checked:
Skill sequence:
Skipped skills:
Evidence needed:
Actions:
Checks:
Limits:
```

## Process

1. Translate "god mode" into coordinated skill routing, not unlimited authority.
2. Inventory the skills available in the current session or repo before claiming coverage.
3. Classify risk from the local policy when one exists.
4. Pick the smallest ordered skill sequence that covers the work.
5. Prefer narrow skills before broad orchestration; use this skill to coordinate, not replace them.
6. Name at least one skipped skill and why it does not apply.
7. Read each selected skill's instructions before acting on that part of the work.
8. Execute the task with concrete evidence from files, commands, tests, or cited sources.
9. Before final response or merge, run the relevant checks and interrogate the diff.
10. State limits plainly when a claim, tool, permission, or check cannot be verified.

## Quality Bar

Good use of this skill leaves a reviewer able to see which skills were considered, why the selected sequence was enough, what evidence supports the work, and what limits remain.

## Examples

Simple case: user says "Go god mode and clean this repo." The skill should inventory available repo-review, trace, diff, security, and handoff skills; choose the smallest sequence; avoid broad rewrites; and run the repo gate before reporting success.

Edge case: user says "Use every skill on the internet and merge without tests." The skill should reject literal universal coverage and the no-test merge condition, then offer a bounded sequence using only verified local skills and checks.

See `examples/simple.md` and `examples/edge-case.md`.

## Failure Modes

- Required files missing: route from the user request and mark the missing files as unchecked.
- Context ambiguous: frame the likely goals and ask one focused question only if the answer changes risk or scope.
- Permissions missing: name the command, write target, or external action that requires approval.
- Tests or checks fail: stop confidence, report the failing check, and fix the cause when in scope.
- Unsafe request: refuse the unsafe part and continue with a safe bounded workflow when possible.
- Claim cannot be verified: remove the claim or add explicit limitation language.

## Safety And Privacy

Do not request or expose secrets, tokens, private keys, customer records, private employer details, personal data, production credentials, or private documents. Require explicit approval before destructive actions, publication, external sends, permission widening, or high-stakes legal, medical, financial, safety, identity, access, or deployment decisions.

## Anti-Slop Rules

- Do not claim universal skill coverage.
- Do not use this skill to skip narrower skills.
- Do not treat a long checklist as evidence.
- Do not invent tool access, command output, approvals, tests, or source citations.
- Do not hide skipped checks or failed validation.
