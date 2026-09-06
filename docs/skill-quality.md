# Skill Quality

Cognitive Deadlift uses a local grading script inspired by public Claude skill-grader patterns and the local skill-creator guidance.

## Constraint

Do not vendor third-party skill-grader content unless the license is clear. The public grader inspected during setup had restricted or unknown licensing metadata, so this repo owns a compact local rubric instead.

## Local Rubric

Run:

```bash
make grade
```

The grader checks eleven axes:

- Description quality
- Scope discipline
- Progressive disclosure
- Activation precision
- Input/output contract
- Process specificity
- Example coverage
- Failure handling
- Safety and privacy
- Anti-slop rules
- Documentation quality

A score of `100.0` means a skill hit the full-contract branch on every axis.
Lower scores identify the first missing or thin contract surfaces. The default
minimum score is 100. CI runs the same check.

## Current Standard

As of 2026-09-06, all twenty-one skills grade `A+` with a score of `100.0`.
