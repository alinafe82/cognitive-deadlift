# ADR 0002: Skill Validation

## Status

Accepted.

## Context

Skills are written instructions, but they still need quality gates. Without validation, the repo can accumulate missing examples, broken links, placeholder sections, duplicate names, and vague prompt text.

The repo is small and mostly markdown. A complex parser or service-backed validator would add maintenance cost without improving the current checks.

## Decision

Use a lightweight Python validator in `scripts/validate_skills.py`.

The validator checks:

- required skill files and directories
- frontmatter metadata
- folder/name consistency
- required sections
- examples
- duplicate names
- placeholder text
- banned filler
- obvious secret patterns
- broken internal links

Pytest covers parser behavior, skill discovery, good fixtures, bad fixtures, examples, and banned filler detection.

## Alternatives Considered

- Markdown lint only: rejected because it does not understand skill-specific structure.
- JSON schema only: rejected because the repo does not store full skill metadata in JSON.
- Runtime model evaluation: rejected because it is expensive, nondeterministic, and not needed for structural quality gates.
- A third-party validation framework: rejected because standard-library Python is enough here.

## Why This Choice

I chose simple deterministic validation because it catches the failures most likely to make this repo look careless: missing sections, weak examples, placeholders, broken links, and accidental secrets.

## Tradeoffs

- The validator cannot prove that a skill works well with every AI assistant.
- Banned phrase detection is lexical, so it may need rare exemptions.
- Link checking is local-only and does not validate external URLs.
- Structural tests do not replace human review.

## Consequences

- Contributors get fast local feedback through `make check`.
- CI can run without secrets or network-dependent services.
- Reviewers have an objective baseline before judging skill quality.

## What Would Change At Larger Scale

At larger scale, validation should add metadata schemas, generated catalogs, semantic duplicate detection, and sampled runtime evaluation. Those should be added only when the repo has enough skills to justify them.
