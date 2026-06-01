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

- **`scripts/`** holds Python checkers and harness logic. New checks land here.
- **`hooks/`** holds local automation invoked by git. The repo does not assume hooks are installed in consumer repos.
- **`skills/`** holds reusable skill bodies and is the single source of truth for any skill. Runtime adapters reference these and never copy them.
- **`docs/`** holds deeper documentation like architecture rationale, ADRs, the security model, the skill standard, the review checklist, and the paid offer. It is not the contract surface.
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

## Harness lifecycle

```text
make prod-gate
  ├── make repo-check     -> scripts/validate_repo.py
  │                          (required files, manifests, skills_index, doc contract, no tracked build artifacts)
  ├── make skills-check   -> scripts/validate_skills.py
  │                          (skill structure, frontmatter, sections, examples, links)
  ├── make slop-scan      -> scripts/validate_skills.py --slop-only
  │                          (banned filler, placeholders, secret patterns across all markdown)
  ├── make grade          -> scripts/grade_skills.py --min-score 90
  ├── make lint           -> ruff check
  ├── make security       -> scripts/security_scan.py
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
