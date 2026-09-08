---
name: god-mode
description: "Coordinate relevant workflows when the user explicitly requests god mode or multi-skill orchestration."
---

# God Mode

Coordinate complex work by selecting, sequencing, and verifying the relevant existing skills instead of pretending one generic skill can do every job.

## Scope

Explicit invocation only. Ordinary end-to-end implementation does not require this router.

## Workflow

1. Use this workflow only for an explicit god-mode or multi-skill orchestration request.
2. Check available skill descriptions and choose only those needed for the requested outcome.
3. Read selected bodies at the point of use; do not load the whole catalog.
4. Carry the authorized task through implementation and relevant verification, fixing in-scope failures.
5. Report outcomes, evidence and unresolved limits without claiming universal capability.

## Evidence

User goal, constraints, and requested autonomy level. Available skill names, descriptions, or local skill paths checked for this session. Risk level and the evidence required by that risk. Selected workflows and why they fit the task. Verification commands, source files, or review artifacts used before confidence. Report the outcome with relevant goal, risk, available skills checked, skill sequence. Adapt the format to the task; omit empty fields. Never claim checks ran without observed results.

## Boundaries

Keep secrets and private records out of shared artifacts. Use redacted or synthetic evidence. External sends, publication, destructive operations and permission widening need explicit authorization; reuse authorization already given for the action. Continue authorized read-only and reversible local work through the requested outcome. If evidence is missing, inspect available sources before asking; report limits honestly.

## References

For worked examples, open [simple](examples/simple.md) or [edge case](examples/edge-case.md) only when useful. [Routing cases](tests/routing.json) record positive and negative activation examples for review; they are not a model benchmark.
