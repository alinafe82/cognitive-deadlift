---
name: docs-claim-audit
description: "Verify changed public documentation claims against implementation and recorded checks."
---

# Docs Claim Audit

Keep public documentation factual, bounded, and backed by repo evidence.

## Scope

Use for the task in the description. For example: Check the README claim that all three runtime adapters were tested. Do not activate for: Correct a spelling mistake in the README title.

## Workflow

1. Extract each factual claim from the changed text.
2. Trace each claim to a repo artifact or command output.
3. Mark claims as supported, unsupported, overstated, or explicitly limited.
4. Replace unsupported claims with factual wording or limitation language.
5. Run the relevant doc or slop checks when changing public docs.

## Evidence

Changed docs or claim text. Files, tests, scripts, examples, or commands that support each claim. Known limitations or unsupported surfaces. Target audience if relevant. Report the outcome with relevant claim, evidence found, unsupported part, required edit. Adapt the format to the task; omit empty fields. Never claim checks ran without observed results.

## Boundaries

Keep secrets and private records out of shared artifacts. Use redacted or synthetic evidence. External sends, publication, destructive operations and permission widening need explicit authorization; reuse authorization already given for the action. Continue authorized read-only and reversible local work through the requested outcome. If evidence is missing, inspect available sources before asking; report limits honestly.

## References

For worked examples, open [simple](examples/simple.md) or [edge case](examples/edge-case.md) only when useful. [Routing cases](tests/routing.json) record positive and negative activation examples for review; they are not a model benchmark.
