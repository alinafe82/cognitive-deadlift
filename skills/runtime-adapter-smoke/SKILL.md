---
name: runtime-adapter-smoke
description: "Validate skill discovery and loading after runtime adapter or manifest changes."
---

# Runtime Adapter Smoke

Verify adapter changes still route runtime discovery to the shared skill bodies.

## Scope

Use for the task in the description. For example: Verify discovery after moving the shared skill directory. Do not activate for: Rewrite an example without changing any discovery paths.

## Workflow

1. Identify each runtime surface affected by the diff.
2. Trace the manifest path to the shared skill directory or context file.
3. Check that skill additions/removals are reflected in explicit adapter lists.
4. Run deterministic validators first; add manual runtime notes only when available.
5. Block publish if any adapter cannot discover or load the expected shared skill body.

## Evidence

Changed adapter files or manifest diff. Expected skill paths and context files. Configured validation command or manual smoke path. Result of discovery/load check when available. Report the outcome with relevant adapter touched, discovery path, shared body path, smoke check. Adapt the format to the task; omit empty fields. Never claim checks ran without observed results.

## Boundaries

Keep secrets and private records out of shared artifacts. Use redacted or synthetic evidence. External sends, publication, destructive operations and permission widening need explicit authorization; reuse authorization already given for the action. Continue authorized read-only and reversible local work through the requested outcome. If evidence is missing, inspect available sources before asking; report limits honestly.

## References

For worked examples, open [simple](examples/simple.md) or [edge case](examples/edge-case.md) only when useful. [Routing cases](tests/routing.json) record positive and negative activation examples for review; they are not a model benchmark.
