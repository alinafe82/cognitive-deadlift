# ADR 0001: Skill Repo Structure

## Status

Accepted.

## Context

Cognitive Deadlift stores reusable skills for AI coding assistants. A reviewer needs to inspect a skill quickly and see its instructions, examples, and validation material in one place.

The repo supports Codex, Claude, and Gemini adapters, but the skill bodies should not drift across runtime-specific copies.

## Decision

Use a folder-per-skill layout:

```text
skills/<skill-name>/
├── SKILL.md
├── examples/
├── tests/
└── fixtures/
```

`SKILL.md` is the source of truth. Runtime adapters point to shared skills instead of duplicating skill bodies.

## Alternatives Considered

- One large prompt file: rejected because it is hard to review, test, and route.
- Separate skill copies per runtime: rejected because duplicated instructions drift.
- A plugin framework with runtime registration code: rejected because the repo does not need runtime extensibility yet.
- A flat `skills/*.md` layout: rejected because examples and fixtures become detached from the skill they validate.

## Why This Choice

I chose a folder-per-skill layout because it keeps instructions, examples, and tests together. That makes each skill reviewable as one engineering artifact.

The tradeoff is that small skills may look heavier, but the consistency makes review easier.

## Consequences

- New skills have a predictable shape.
- Reviewers can compare skills without learning a new layout each time.
- Validation can remain simple and path-based.
- Runtime adapters stay thin.

## What Would Change At Larger Scale

At larger scale, the repo may need generated catalogs, metadata schema validation, runtime compatibility tests, and release automation. It does not need those before the skill set grows beyond the current small library.
