# Skill Quality

Cognitive Deadlift uses a local grading script inspired by public Claude skill-grader patterns and the local skill-creator guidance.

## Constraint

Do not vendor third-party skill-grader content unless the license is clear. The public grader inspected during setup had restricted or unknown licensing metadata, so this repo owns a compact local rubric instead.

## Local Rubric

Run:

```bash
make grade
```

The grader checks ten axes:

- Description quality
- Scope discipline
- Progressive disclosure
- Anti-pattern coverage
- Self-contained tooling expectations
- Activation precision
- Visual artifacts
- Output contracts
- Temporal awareness
- Documentation quality

The default minimum score is 90. CI runs the same check.

## Current Standard

As of 2026-05-25, all ten initial skills grade `A` with a score of `94.1`.
