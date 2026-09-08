---
name: transcript-review
description: "Audit a real agent transcript for unsupported claims, missed evidence, and instruction failures."
---

# Transcript Review

Turn real agent sessions into evidence about whether skills work in practice.

## Scope

Use for the task in the description. For example: Audit this actual agent transcript for claimed checks without output. Do not activate for: Review a hypothetical skill draft without a transcript.

## Workflow

1. Identify the user request, risk level, and expected skill triggers.
2. Compare the agent response to each expected output contract.
3. Mark every claimed check as supported, unsupported, or unverifiable from the transcript.
4. Separate agent failure from skill wording failure.
5. Recommend concrete changes to skill body, examples, harness rubric, or validation process.

## Evidence

Transcript or session excerpt. Skill or skills expected to apply. Task context and any tool outputs the agent claimed to use. Known outcome if available. Report the outcome with relevant session, expected skill behavior, evidence followed, evidence skipped. Adapt the format to the task; omit empty fields. Never claim checks ran without observed results.

## Boundaries

Keep secrets and private records out of shared artifacts. Use redacted or synthetic evidence. External sends, publication, destructive operations and permission widening need explicit authorization; reuse authorization already given for the action. Continue authorized read-only and reversible local work through the requested outcome. If evidence is missing, inspect available sources before asking; report limits honestly.

## References

For worked examples, open [simple](examples/simple.md) or [edge case](examples/edge-case.md) only when useful. [Routing cases](tests/routing.json) record positive and negative activation examples for review; they are not a model benchmark.
