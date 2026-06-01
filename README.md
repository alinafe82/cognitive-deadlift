# Cognitive Deadlift

Cognitive Deadlift is a skill-retention harness for developers using AI coding
assistants.

AI can write code quickly. That does not mean the developer understood the
problem, read the existing path, proved the behavior, or reviewed the diff
carefully.

This repo keeps those muscles in the loop.

It gives teams reusable skills, context packs, harness fixtures, and lightweight
gates for AI-assisted development. The goal is not to slow developers down. The
goal is to make sure the right thinking happens at the right risk level.

Use it when AI is helping with:

- bug fixes
- refactors
- tests
- code review
- risky changes
- tool-using agents
- documentation updates that must stay true to code

Do not use it as:

- a prompt dump
- an agent framework
- a chat UI
- a replacement for code review
- a process checklist for every tiny change

## Why Skill Retention Matters

AI can move faster than judgment. Cognitive Deadlift keeps the judgment in the
loop.

Passive AI use can weaken the skills that make a developer useful:

- defining the real problem
- reading the current code path
- debugging from evidence
- designing tests that prove behavior
- comparing implementation tradeoffs
- reviewing diffs as untrusted proposals
- interpreting errors instead of pasting them back into a model
- explaining the mechanism of a change without hiding behind the assistant

Cognitive Deadlift protects those abilities by requiring evidence at the points
where judgment usually gets skipped.

## Thinking Budget

Not every task deserves the same amount of friction.

| Risk | Use For | Required Evidence |
| --- | --- | --- |
| Low | Mechanical or reversible work | Intent summary and a basic check |
| Medium | Normal behavior changes | Code-path trace, failing signal, and diff review |
| High | Security, data, public API, permissions, destructive behavior, migrations, or production config | Problem frame, assumption audit, alternatives, rollback plan, human approval, and final explanation |

The policy lives in [policies/thinking-budget.yaml](policies/thinking-budget.yaml).

## Quickstart

Clone and set up:

```bash
git clone https://github.com/alinafe82/cognitive-deadlift.git
cd cognitive-deadlift
uv sync --all-extras   # or: python3 -m pip install -e ".[test,lint]"
```

Run the full gate:

```bash
make check
```

Check readiness for AI-assisted work:

```bash
make doctor
```

Run focused checks:

```bash
make skills-check
make harness-check
make context-check
make docs-check
make slop-scan
make test
make lint
```

## Core Skills

| Skill | Preserves |
| --- | --- |
| `problem-framing` | Problem definition |
| `assumption-audit` | Evidence-based judgment |
| `alternatives-before-code` | Tradeoff analysis |
| `failing-test-first` | Behavioral proof |
| `trace-the-code` | Code reading |
| `read-the-docs-first` | Source-based reasoning |
| `explain-without-ai` | Ownership of the mechanism |
| `diff-interrogation` | Review judgment |
| `debugging-lab-notebook` | Systematic debugging |
| `complexity-budget` | Systems thinking and operational judgment |

See [CATALOG.md](CATALOG.md) for the full catalog.

## Use A Skill

Use the skill name in your assistant prompt, then provide the task context.

Installing a skill makes it available to the runtime. It does not mean the full
`SKILL.md` body is loaded into every conversation at session start. Most agent
runtimes first discover skill metadata, then load the full skill body when the
user names the skill or the request matches its trigger conditions.

Example:

```text
Use problem-framing before coding:
"Add retries to the webhook worker."
```

Expected behavior: the assistant identifies the actual failure, current evidence,
assumptions, non-goals, success condition, and first verification step before it
proposes code.

## Harnesses

Harnesses are review fixtures, not a full benchmark suite. They teach reviewers
how to catch common agent failure modes:

- ambiguous requests
- fake test passes
- overeager refactors
- unsafe tool use

Each harness includes a task, expected behavior, and rubric. Validate them with:

```bash
make harness-check
```

See [harnesses/README.md](harnesses/README.md).

## Context Packs

Context packs describe the evidence an agent should receive for a workflow. They
keep prompts grounded without building a prompt framework.

Included packs:

- `bugfix`
- `refactor`
- `repo-review`
- `risky-change`

Validate them with:

```bash
make context-check
```

See [context-packs/README.md](context-packs/README.md).

## Example Workflows

Bug fix:

1. Use `problem-framing` if the symptom is unclear.
2. Use `trace-the-code` to read the path before editing.
3. Use `failing-test-first` to prove the behavior.
4. Use `diff-interrogation` before accepting the change.
5. Use `explain-without-ai` before handoff if the mechanism is not obvious.

Risky change:

1. Classify the work as high risk in the thinking budget.
2. Use `problem-framing` and `assumption-audit`.
3. Compare options with `alternatives-before-code`.
4. Write down rollback and approval requirements.
5. Review the diff as untrusted.
6. Explain the final mechanism in plain English.

Repo review:

1. Use `read-the-docs-first` to check local docs and ADRs.
2. Use `diff-interrogation` for generated or unfamiliar changes.
3. Use `complexity-budget` before adding a new layer, dependency, or workflow.

## Validation

The repo validates structure and review artifacts. It does not judge whether a
model behaved well.

```bash
make check          # full local gate
make prod-gate      # same full gate, used before merge
make skills-check   # skill structure and content
make policy-check   # thinking budget policy
make harness-check  # harness fixtures
make context-check  # context packs
make docs-check     # repo contract
make slop-scan      # filler, placeholders, and obvious secret patterns
make doctor         # readiness check
make test           # pytest
make lint           # ruff
```

CI runs the same meaningful checks.

## Runtime Adapters

The shared source of truth is `skills/*/SKILL.md`. Runtime adapters route to
those files and should not duplicate them.

- Codex: `.codex-plugin/plugin.json` and `AGENTS.md`
- Claude: `.claude-plugin/plugin.json` and `CLAUDE.md`
- Gemini: `gemini-extension.json` and `GEMINI.md`

## Support

Cognitive Deadlift is free to use. If it helps your team keep better judgment in
AI-assisted development, voluntary support is available through GitHub Sponsors.

Sponsorship does not change the repo's purpose, license, or vendor-neutral
stance. Teams that want help applying the workflow can read
[docs/workflow-audit.md](docs/workflow-audit.md).

## What This Repo Deliberately Does Not Do

- No generic prompt dump.
- No full agent framework.
- No chat UI.
- No vendor lock-in.
- No replacing human code review.
- No claims that agents will follow skills perfectly.
- No fake reports, screenshots, adoption metrics, or integrations.
- No heavy policy engine for small teams.

## Design Notes

- [specs/cognitive-deadlift-v2-modernization.md](specs/cognitive-deadlift-v2-modernization.md)
- [docs/architecture.md](docs/architecture.md)
- [docs/skill-atrophy-taxonomy.md](docs/skill-atrophy-taxonomy.md)
- [docs/ai-slop-taxonomy.md](docs/ai-slop-taxonomy.md)
- [docs/skill-standard.md](docs/skill-standard.md)
- [docs/review-checklist.md](docs/review-checklist.md)
- [docs/roadmap.md](docs/roadmap.md)

## License

Cognitive Deadlift uses a split license:

- Code, scripts, hooks, workflows, and plugin manifests: [MIT](LICENSE)
- Skills, docs, prompts, catalogs, and written methodology:
  [CC BY-NC-SA 4.0](LICENSE-CONTENT)

See [NOTICE](NOTICE) for the file-scope policy.
