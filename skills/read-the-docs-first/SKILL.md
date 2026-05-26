---
name: read-the-docs-first
description: "Check local docs, ADRs, interfaces, schemas, and primary upstream sources before guessing. Use when work depends on APIs, frameworks, repo conventions, architecture decisions, or policy. NOT for purely local refactors or cases where code is the only source of truth."
---

# Read The Docs First

## Purpose

Prevent unsupported claims about tools, APIs, frameworks, and repo decisions.

## When To Use

- The task depends on external API, framework, CLI, or runtime behavior.
- The repo may already document a decision in `CONTEXT.md`, ADRs, schemas, or interfaces.
- The user states a rule or convention that could be outdated.
- AI proposes behavior without citing a primary source.

## When Not To Use

- Purely local refactors whose behavior is fully determined by code.
- Cases where the user supplied the authoritative source in the prompt.
- Cases where no docs exist and code is explicitly the source of truth.

## Inputs Expected

- Claim, plan, or task that depends on documented behavior.
- Relevant repo files, docs, ADRs, package names, API names, or version constraints.
- Whether external browsing is allowed when upstream docs are needed.

## Output Expected

```md
Sources checked:
Relevant constraints:
Inference:
Docs gap:
Next action:
```

## Process

1. Check local `CONTEXT.md`, `CONTEXT-MAP.md`, `docs/adr/`, README files, schemas, and interface definitions.
2. Check primary upstream docs when external behavior matters.
3. Record what each source actually constrains.
4. Separate documented facts from inference.
5. Flag contradictions before changing code.

## Quality Bar

A good result makes it clear what was checked, what was learned, and which claims remain inference.

## Examples

Simple case: "This GitHub Action supports Node 24." The skill should check the action docs or release notes before changing workflow versions.

Complex case: "Gemini uses skills the same way Claude does." The skill should distinguish shared skill bodies from Gemini's context-file extension model and document the adapter boundary.

See `examples/simple.md` and `examples/edge-case.md`.

## Failure Modes

- Network unavailable: state that upstream docs were not checked and use local sources only.
- Docs conflict with code: explain both and recommend the smallest verification step.
- Docs are versioned: match the repo's version before applying guidance.
- Source is missing: record the docs gap instead of guessing.

## Safety And Privacy

Do not send private code, customer data, internal URLs, or confidential employer details to external sites. Use official public docs when browsing is required.

## Anti-Slop Rules

- Do not cite memory as documentation.
- Do not claim a source was checked unless it was opened or inspected.
- Do not treat inference as fact.
- Do not use broad recommendations when a version-specific source is required.

