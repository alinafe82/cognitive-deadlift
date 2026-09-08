---
name: release-readiness
description: "Check versioning, distribution metadata, licenses, and validation evidence for a planned skills release."
---

# Release Readiness

Prevent publishing a skills repo with inconsistent metadata, stale docs, or unverified adapters.

## Scope

Use for the task in the description. For example: Check metadata, licenses and validation before this plugin release. Do not activate for: Fix an internal helper on a branch with no release planned.

## Workflow

1. Identify every version and distribution metadata surface.
2. Check changelog, README, catalog, license, and notice files for accurate release claims.
3. Verify adapter manifests route to shared skill bodies.
4. Run or require prod-gate and any release-specific smoke checks.
5. List blockers separately from follow-up work before recommending release.

## Evidence

Release target and version. Changed files since last release or tag. Adapter manifests, license files, changelog, and README. Gate results and known limitations. Report the outcome with relevant release target, version surfaces, public docs, adapters. Adapt the format to the task; omit empty fields. Never claim checks ran without observed results.

## Boundaries

Keep secrets and private records out of shared artifacts. Use redacted or synthetic evidence. External sends, publication, destructive operations and permission widening need explicit authorization; reuse authorization already given for the action. Continue authorized read-only and reversible local work through the requested outcome. If evidence is missing, inspect available sources before asking; report limits honestly.

## References

For worked examples, open [simple](examples/simple.md) or [edge case](examples/edge-case.md) only when useful. [Routing cases](tests/routing.json) record positive and negative activation examples for review; they are not a model benchmark.
