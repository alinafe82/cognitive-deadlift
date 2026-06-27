---
name: runtime-adapter-smoke
description: "Smoke-test runtime adapter changes for shared skills. Use when publishing or merging changes to Codex, Claude, Gemini, or other adapter manifests, context files, skill paths, or runtime metadata. NOT for skill body edits that do not affect adapter discovery or for unrelated CI changes."
---

# Runtime Adapter Smoke

## Purpose

Verify adapter changes still route runtime discovery to the shared skill bodies.

## Preserves

Operational judgment around distribution and runtime compatibility.

## Required Evidence

- Changed adapter files or manifest diff.
- Expected skill paths and context files.
- Configured validation command or manual smoke path.
- Result of discovery/load check when available.

## Failure Signs

- The adapter manifest points at copied skill bodies instead of shared skills.
- A runtime can list metadata but cannot load the referenced skill body.
- Publishing is recommended without naming which runtime was checked.

## When To Use

- Adapter manifests change.
- A skill is added, removed, renamed, or moved.
- Runtime context files such as AGENTS.md, CLAUDE.md, or GEMINI.md change.
- A release depends on runtime discovery working.

## When Not To Use

- Skill body changes do not affect discovery paths.
- Only internal docs unrelated to adapters changed.
- The task is a security review of tool permissions; use agent-security-boundary.

## Inputs Expected

- Adapter manifest paths and diff.
- Skill directory or index changes.
- Runtime context file changes.
- Validation command output or manual check notes.

## Output Expected

```md
Adapter touched:
Discovery path:
Shared body path:
Smoke check:
Result:
Risk:
Publish decision:
```

## Process

1. Identify each runtime surface affected by the diff.
2. Trace the manifest path to the shared skill directory or context file.
3. Check that skill additions/removals are reflected in explicit adapter lists.
4. Run deterministic validators first; add manual runtime notes only when available.
5. Block publish if any adapter cannot discover or load the expected shared skill body.

## Quality Bar

A good smoke result proves metadata, discovery path, and shared body routing for each affected runtime or states which runtime remains unchecked.

## Examples

Simple case: A new skill was added and .claude-plugin/plugin.json was updated. The skill should check the Claude list includes the new skill path.

Complex case: A release changes AGENTS.md, GEMINI.md, and skills_index.json but not the Gemini extension manifest. The skill should trace each runtime context file.

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
