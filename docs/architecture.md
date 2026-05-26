# Architecture

## Repo Layout

```text
.
├── skills/
│   └── skill-name/
│       ├── SKILL.md
│       ├── examples/
│       ├── tests/
│       └── fixtures/
├── docs/
├── scripts/
├── hooks/
├── .codex-plugin/
├── .claude-plugin/
├── .gemini/
├── AGENTS.md
├── CLAUDE.md
└── GEMINI.md
```

## Skill Loading Model

The shared skill body lives in `skills/<skill-name>/SKILL.md`.

Runtime adapters point at or describe those shared skills:

- Codex: `.codex-plugin/plugin.json` and `AGENTS.md`
- Claude: `.claude-plugin/plugin.json` and `CLAUDE.md`
- Gemini: `gemini-extension.json` and `GEMINI.md`

The repo does not duplicate skill bodies per runtime. If a runtime needs special routing, put that in the adapter file, not in a forked copy of the skill.

## Naming Conventions

- Skill folders use lowercase hyphen-case.
- `name` in `SKILL.md` must match the folder name.
- Skill names should describe the action: `trace-the-code`, `assumption-audit`, `diff-interrogation`.
- Avoid vague names such as `better-coding`, `ai-helper`, or `productivity-mode`.

## Metadata Conventions

Each `SKILL.md` starts with YAML frontmatter:

```yaml
---
name: skill-name
description: "What it does. Use when ... NOT for ..."
---
```

Descriptions must include trigger conditions and false-positive boundaries. They are part of runtime discovery, not marketing copy.

## Validation Approach

Validation is intentionally simple:

- `scripts/validate_repo.py` checks repo-level required files and manifest consistency.
- `scripts/validate_skills.py` checks skill structure and content standards.
- `scripts/grade_skills.py` scores skills against a compact quality rubric.
- `scripts/security_scan.py` checks obvious secrets, dangerous script patterns, workflow permissions, and CODEOWNERS coverage.

These scripts use the Python standard library where possible to keep the supply chain small.

## Testing Strategy

Tests cover the validators and discovery logic, not AI model behavior. The repo cannot guarantee that a model follows a skill perfectly.

Minimum test coverage:

- skill discovery
- metadata parsing
- validation failures
- good and bad skill fixtures
- required examples
- banned filler phrases
- broken internal links

## Safety Model

Skills can influence agent behavior, so they are treated like code:

- every skill has `When To Use` and `When Not To Use`
- every skill has safety/privacy notes
- destructive operations require explicit confirmation
- no skill may claim a check was performed unless it was performed
- no skill may ask an agent to expose secrets or private data

Hooks and scripts should be deterministic, small, and local-repo scoped.

## Why This Structure

Folder-per-skill keeps instructions, examples, and fixtures together. It makes review easier because a reviewer can inspect one skill as one unit.

The tradeoff is extra directories for small skills. That is acceptable because consistency matters more than saving a few folders.

## Alternatives Considered

- Single large prompt file: rejected because it is hard to review, test, and route.
- Separate Codex/Claude/Gemini copies: rejected because duplicated skill bodies drift.
- Full plugin framework: rejected because this repo does not need runtime extensibility.
- Dependency-heavy validator: rejected because simple structural checks do not need a larger supply chain.

## What Would Change At Larger Scale

At 50+ skills, this repo may need:

- generated catalogs
- a schema file for skill metadata
- stronger link checking
- semantic duplicate detection
- release automation
- compatibility tests against specific runtimes
