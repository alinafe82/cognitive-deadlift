# Architecture

Current top-level structure of the repo. Deeper rationale, alternatives considered, and scaling notes live in `docs/architecture.md`.

## Top-level layout

```text
.
├── skills/                    # One folder per shared skill (source of truth)
│   └── <skill-name>/
│       ├── SKILL.md
│       ├── examples/
│       ├── tests/
│       └── fixtures/
├── scripts/                   # Validation, grading, security scanning, ledger check
├── hooks/                     # Optional pre-commit hook
├── tests/                     # Pytest tests for the harness
├── docs/                      # Deeper supporting docs, ADRs, security
├── specs/                     # Planning and review documents for repo-level changes
├── policies/                  # Risk-based thinking budget
├── context-packs/             # Evidence contracts for common workflows
├── harnesses/                 # Review fixtures for agent failure modes
├── .codex-plugin/             # Codex runtime adapter manifest
├── .claude-plugin/            # Claude runtime adapter manifest
├── .gemini/                   # Gemini runtime adapter note
├── .github/                   # CI, CODEOWNERS, issue templates
├── AGENTS.md                  # Generic agent rules
├── CLAUDE.md                  # Claude-specific rules
├── GEMINI.md                  # Gemini-specific rules
├── CONTEXT.md                 # Mission, principles, anti-slop rules, glossary
├── README.md                  # Public quickstart
├── CATALOG.md                 # Index of skills, hooks, scripts, adapters
├── ARCHITECTURE.md            # This file
├── repo-audit.md              # Standing audit
├── productionization-report.md # Standing prod-readiness status
├── skills_index.json          # Machine-readable index of skills/
├── Makefile                   # Validation and gate targets
└── pyproject.toml             # Python packaging + ruff config
```

## What belongs where

- **`scripts/`** holds Python checkers and harness logic. New deterministic checks land here.
- **`hooks/`** holds local automation invoked by git. The repo does not assume hooks are installed in consumer repos.
- **`skills/`** holds reusable skill bodies and is the single source of truth for any skill. Runtime adapters reference these and never copy them.
- **`docs/`** holds deeper documentation like architecture rationale, ADRs, the security model, the skill standard, the review checklist, and the workflow audit note. It is not the contract surface.
- **`specs/`** holds planning and review documents for repo-level changes.
- **`policies/`** holds risk-based evidence policy. `thinking-budget.yaml` is the source of truth for low / medium / high gates.
- **`context-packs/`** holds workflow-specific context contracts for bug fixes, refactors, repo review, and risky changes.
- **`harnesses/`** holds review fixtures that teach how to catch AI-assisted development failure modes. These are not benchmark claims.
- **`tests/`** holds pytest tests that lock harness behavior (validators, doc contract, slop scanner). These are not behavior tests for the AI.

## Skill lifecycle

1. Author creates `skills/<name>/` with `SKILL.md` and the three required subdirectories.
2. `SKILL.md` follows the format defined in `docs/skill-standard.md`: frontmatter (`name`, `description` with `Use when ... NOT for ...`), then the eleven required sections.
3. Author adds at least two markdown examples (`examples/simple.md`, `examples/edge-case.md`), a fixture, and a tests README.
4. Author updates `skills_index.json` and `CATALOG.md` to add the skill.
5. Author updates `.claude-plugin/plugin.json` if the skill should be exposed to Claude.
6. `make prod-gate` must pass before review.

## Hook lifecycle

1. Hook scripts live in `hooks/` and are symlinked into a consumer repo's `.git/hooks/` by the user.
2. The only hook today is `hooks/pre-commit`, which calls `scripts/cognitive_deadlift_check.py`.
3. The hook blocks staged source changes unless a `docs/thinking/*.md` ledger is also staged. `COGNITIVE_DEADLIFT_BYPASS=1` skips the check.
4. Adding a new hook requires updating `CATALOG.md` and `hooks/pre-commit` documentation.

## Policy lifecycle

1. Policy files live in `policies/`.
2. `policies/thinking-budget.yaml` defines the low / medium / high evidence gates.
3. `scripts/validate_policies.py` checks required levels and required fields.
4. Changing policy shape requires updating `README.md`, `CATALOG.md`, tests, and this file.

## Context pack lifecycle

1. Context packs live in `context-packs/*.yaml`.
2. Each pack defines purpose, required evidence, optional evidence, forbidden context, freshness rules, output contract, and recommended skills.
3. `scripts/validate_context_packs.py` checks required fields and recommended skill names.
4. Adding or removing a pack requires updating `CATALOG.md` and tests.

## Review harness lifecycle

1. Harness fixtures live in `harnesses/<name>/`.
2. Each harness has `task.md`, `expected-behavior.md`, and `rubric.yaml`.
3. Harnesses are review fixtures, not benchmark suites or claims about model quality.
4. `scripts/validate_harnesses.py` checks required files and rubric shape.
5. Adding or removing a harness requires updating `CATALOG.md` and tests.

## Validation lifecycle

```text
make prod-gate
  ├── make repo-check     -> scripts/validate_repo.py
  │                          (required files, manifests, skills_index, doc contract, no tracked build artifacts)
  ├── make skills-check   -> scripts/validate_skills.py
  │                          (skill structure, frontmatter, sections, examples, links)
  ├── make policy-check   -> scripts/validate_policies.py
  │                          (thinking budget levels and required fields)
  ├── make harness-check  -> scripts/validate_harnesses.py
  │                          (review fixture files and rubrics)
  ├── make context-check  -> scripts/validate_context_packs.py
  │                          (context pack fields and skill references)
  ├── make slop-scan      -> scripts/validate_skills.py --slop-only
  │                          (banned filler, placeholders, secret patterns across all markdown)
  ├── make grade          -> scripts/grade_skills.py --min-score 90
  ├── make lint           -> ruff check
  ├── make security       -> scripts/security_scan.py
  ├── make doctor         -> scripts/doctor.py
  │                          (readiness check for contract artifacts)
  └── make test           -> pytest
```

Each check exits nonzero on real failure. `make prod-gate` chains them and propagates the first failure.

## Skills index

`skills_index.json` is hand-maintained, not generated. The repo prefers a small artifact under review over a generator. `scripts/validate_repo.py` enforces that the index lists exactly the directories under `skills/`, each with `name`, `path`, and `purpose`.

If skill count grows beyond ~30, switch to generation. The threshold for that decision lives in `docs/architecture.md`.

## Runtime adapter contract

Adapters route discovery to the shared skills, and they never carry a skill body.

| Runtime | Manifest | Context file |
| --- | --- | --- |
| Claude | `.claude-plugin/plugin.json` | `CLAUDE.md` |
| Codex | `.codex-plugin/plugin.json` | `AGENTS.md` |
| Gemini | `gemini-extension.json` | `GEMINI.md` |

The validator checks that each manifest points at `skills/` correctly and that Claude's explicit skill list matches the directory.

## Source-control hygiene

Generated artifacts (`*.egg-info/`, `.pytest_cache/`, `.ruff_cache/`, `__pycache__/`, `.venv/`, `dist/`, `build/`, `htmlcov/`, `coverage.xml`) are gitignored and validated as untracked by `scripts/validate_repo.py`. If any of them appears in `git ls-files`, the gate fails.
