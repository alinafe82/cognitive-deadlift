---
name: release-readiness
description: "Check release readiness before tagging, publishing, or distributing a skills repo or plugin. Use when preparing a release, version bump, public package update, adapter publication, or handoff that depends on consistent versioning, changelog, adapters, licenses, docs, and make prod-gate. NOT for ordinary feature branches or local-only validation changes."
---

# Release Readiness

## Purpose

Prevent publishing a skills repo with inconsistent metadata, stale docs, or unverified adapters.

## Preserves

Operational release judgment.

## Required Evidence

- Release target and version.
- Changed files since last release or tag.
- Adapter manifests, license files, changelog, and README.
- Gate results and known limitations.

## Failure Signs

- Version appears in one manifest but not another.
- Release notes claim behavior not backed by files or checks.
- Publishing is recommended without adapter or license review.

## When To Use

- A tag, package, plugin, or public release is planned.
- Runtime adapter metadata changed.
- License, changelog, README, or install instructions changed.
- A release candidate needs a final readiness decision.

## When Not To Use

- No publish, tag, or distribution action is planned.
- The task is only checking a single PR; use diff-interrogation.
- The task is adding a skill; use skill-authoring-gate first.

## Inputs Expected

- Target version and release scope.
- Diff or commit range.
- Manifest, license, changelog, README, and adapter files.
- Results from prod-gate and optional scans.

## Output Expected

```md
Release target:
Version surfaces:
Public docs:
Adapters:
License and notices:
Checks:
Blockers:
Release decision:
```

## Process

1. Identify every version and distribution metadata surface.
2. Check changelog, README, catalog, license, and notice files for accurate release claims.
3. Verify adapter manifests route to shared skill bodies.
4. Run or require prod-gate and any release-specific smoke checks.
5. List blockers separately from follow-up work before recommending release.

## Quality Bar

A good readiness review lets a maintainer decide whether to tag or publish without rediscovering metadata, adapter, and licensing risks.

## Examples

Simple case: Prepare a patch release after adding one skill. The skill should check skill index, catalog, adapter manifests, changelog need, and prod-gate result.

Complex case: Prepare a public plugin release after changing licenses and runtime manifests. The skill should check license and notice consistency.

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
