# Cognitive Deadlift

Reusable skills, hooks, and validation checks for developers who use AI coding assistants but still want to do the engineering thinking themselves.

The repo is not anti-AI. It is anti-autopilot.

## Who This Is For

- Developers using Codex, Claude, Gemini, ChatGPT-style assistants, or agentic coding tools.
- Engineers who want reusable review and reasoning workflows instead of one-off prompts.
- Teams that want lightweight quality gates around AI-assisted changes.
- Hiring reviewers who want to see practical Engineering Productivity judgment: standardization, validation, safety, and maintainability.

## Problem It Solves

AI assistants make it easy to skip the thinking that makes code review and debugging possible:

- framing the real problem
- checking assumptions
- reading the existing code path
- proving behavior with tests
- comparing alternatives
- reviewing diffs as untrusted changes
- explaining the mechanism before shipping

Cognitive Deadlift turns those behaviors into reusable skills with validation and review standards.

## Paid Offer

Teams that want help applying this repo to their own AI-assisted engineering workflow can buy a fixed-scope [Cognitive Deadlift Workflow Audit](docs/paid-offer.md).

- Price: USD 2,500 fixed fee.
- Outcome: a reasoning evidence gap analysis, recommended skill workflow, adapted thinking ledger template, and 30-day adoption plan.
- Scope: workflow review and recommendations, not security penetration testing or private implementation work.

## Repo Layout

```text
skills/
  skill-name/
    SKILL.md
    examples/
    tests/
    fixtures/
docs/
scripts/
hooks/
```

Runtime adapters:

- Codex: `.codex-plugin/plugin.json` and `AGENTS.md`
- Claude: `.claude-plugin/plugin.json` and `CLAUDE.md`
- Gemini: `gemini-extension.json` and `GEMINI.md`

The shared source of truth is `skills/*/SKILL.md`. Runtime adapters should route to those files, not duplicate them.

## Skills

| Skill | Use It For |
| --- | --- |
| `problem-framing` | Turn an unclear request into a concrete problem statement. |
| `assumption-audit` | Identify and test assumptions in a plan or AI answer. |
| `alternatives-before-code` | Compare viable solution paths before committing to one. |
| `failing-test-first` | Require a failing signal before a bug fix or behavior change. |
| `trace-the-code` | Follow the existing execution path before editing. |
| `read-the-docs-first` | Check local docs, ADRs, schemas, and primary sources before guessing. |
| `explain-without-ai` | Require a mechanism-level explanation before merge or handoff. |
| `diff-interrogation` | Review a diff as an untrusted claim. |
| `debugging-lab-notebook` | Debug hard failures with reproduction, hypotheses, and experiments. |
| `complexity-budget` | Challenge unnecessary abstraction, dependencies, and indirection. |

See [CATALOG.md](CATALOG.md) for the searchable catalog.

## Quickstart

Clone and set up:

```bash
git clone https://github.com/alinafe82/cognitive-deadlift.git
cd cognitive-deadlift
uv sync --all-extras   # or: python3 -m pip install -e ".[test,lint]"
```

Run the full gate:

```bash
make prod-gate
```

Or run individual checks:

```bash
make skills-check   # skill structure, frontmatter, sections, examples, links
make docs-check     # doc contract (required files + one-job per doc)
make slop-scan      # banned filler, placeholders, secret patterns
make lint           # ruff
make test           # pytest
make security       # security hygiene scan
```

## Use A Skill

Use the skill name in your assistant prompt, then provide the task context.

Simple example:

```text
Use problem-framing on this request before coding:
"Add retries to the webhook worker."
```

Expected behavior: the assistant should identify the actual failure, current evidence, assumptions, non-goals, success condition, and first verification step before proposing code.

Complex example:

```text
Use alternatives-before-code and complexity-budget:
We are considering a queue, a scheduled batch job, or synchronous retry for failed billing syncs.
```

Expected behavior: the assistant should compare options, call out reversibility and operational cost, and recommend the smallest defensible approach.

## Optional Hook

The repo includes an optional pre-commit hook that blocks staged source changes unless a thinking ledger is also staged:

```bash
ln -s "$(pwd)/hooks/pre-commit" /path/to/target-repo/.git/hooks/pre-commit
```

Bypass only for mechanical work like dependency bumps or generated-file regeneration:

```bash
COGNITIVE_DEADLIFT_BYPASS=1 git commit
```

## Validation And Tests

Validation checks:

- required repo files and plugin manifests
- `skills_index.json` matches `skills/`
- skill folder structure, frontmatter, sections, examples, fixtures
- banned filler phrases, placeholder text, obvious secret patterns
- broken internal links
- generated artifacts stay untracked

Commands:

```bash
make prod-gate     # run every meaningful check
make skills-check  # only the skill validator
make docs-check    # only the doc contract
make slop-scan     # only the filler / placeholder / secret scan
```

CI runs validation, tests, security hygiene scanning, dependency review, and CodeQL.

## Add A New Skill

1. Create `skills/<skill-name>/`.
2. Add `SKILL.md` matching the format in [docs/skill-standard.md](docs/skill-standard.md).
3. Add at least two examples under `examples/`.
4. Add validation fixtures or test notes under `fixtures/` or `tests/`.
5. Update `.claude-plugin/plugin.json` if the skill should be exposed to Claude.
6. Update `skills_index.json` and `CATALOG.md`.
7. Run `make prod-gate`.

Use [docs/skill-standard.md](docs/skill-standard.md) and [docs/review-checklist.md](docs/review-checklist.md) before opening a PR.

## Limitations

- This repo does not execute skills. It packages instructions and validation around them.
- It does not guarantee that an AI assistant will follow a skill perfectly.
- It does not replace code review, tests, security review, or human judgment.
- It does not include private company workflows, customer data, or internal infrastructure references.
- It intentionally avoids a plugin framework or dependency-heavy tooling until the repo needs it.

## What This Repo Intentionally Does Not Do

- No generic prompt dumps.
- No hidden private process knowledge.
- No claims that cannot be validated from the repo.
- No generated test artifacts committed to git.
- No separate skill bodies per runtime unless a runtime requires a different format.
- No complex build system for a small documentation/tooling repo.

## Design Notes

- [docs/architecture.md](docs/architecture.md)
- [docs/skill-standard.md](docs/skill-standard.md)
- [docs/security-notes.md](docs/security-notes.md)
- [docs/interview-notes.md](docs/interview-notes.md)
- [repo-audit.md](repo-audit.md)

## License

Cognitive Deadlift uses a split license:

- Code, scripts, hooks, workflows, and plugin manifests: [MIT](LICENSE)
- Skills, docs, prompts, catalogs, and written methodology: [CC BY-NC-SA 4.0](LICENSE-CONTENT)

See [NOTICE](NOTICE) for the file-scope policy.
