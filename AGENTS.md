# AGENTS.md

## Repo contract

This repo is enforced by `make prod-gate`. Read this section first.

Before editing:

1. Read `CONTEXT.md` for mission, principles, anti-slop rules, and current assumptions.
2. Read `repo-audit.md` for the standing list of duplications, gaps, and risks.
3. Read `ARCHITECTURE.md` for the current structure and lifecycles.
4. Read `policies/thinking-budget.yaml` before deciding how much evidence the work needs.

Before finishing:

- Update `CATALOG.md` if you added, removed, or renamed a skill, hook, script,
  policy, harness, or context pack.
- Update `ARCHITECTURE.md` only when the top-level structure or a lifecycle changes.
- Update `skills_index.json` if you added or removed a skill.
- Update `repo-audit.md` if you introduced a new source of truth, duplication, or risk.
- Update `productionization-report.md` if the harness or check set changed.
- Run `make prod-gate`. If it fails, fix the real issue. Do not weaken the gate.

## Agent behavior contract

- Evidence before edits.
- Smallest safe change.
- Tests before confidence.
- Diff review before completion.
- Human approval for high-risk changes.

## Purpose

Cognitive Deadlift exists so developers do not lose engineering skill while using AI.

It is not anti-AI. It is anti-autopilot.

The repo should preserve the muscles that matter: problem framing, code reading,
debugging, behavioral testing, tradeoff analysis, diff review, operational judgment,
and explaining a change without hiding behind the model.

## Skill usage

When a request touches implementation, review, debugging, architecture, or learning,
prefer the relevant Cognitive Deadlift skill before generating code:

- `problem-framing` before implementation.
- `assumption-audit` before accepting a plan.
- `alternatives-before-code` before architecture or refactors.
- `failing-test-first` before fixes.
- `trace-the-code` before modifying unfamiliar paths.
- `read-the-docs-first` before framework or API claims.
- `explain-without-ai` before merge or handoff.
- `diff-interrogation` before accepting generated changes.
- `debugging-lab-notebook` for hard bugs.
- `complexity-budget` before adding abstraction.

Use the thinking budget:

- Low-risk work gets minimal friction: summarize intent and run a basic check.
- Medium-risk work needs evidence: trace the path, prove behavior, review the diff.
- High-risk work needs structure: frame the problem, audit assumptions, compare options,
  define rollback, get human approval, and explain the mechanism.

## Engineering style

- Prefer simple, readable code.
- Keep diffs small and scoped.
- Avoid unnecessary abstractions.
- Do not implement before framing the problem when the task is ambiguous.
- Do not edit unfamiliar code before inspecting relevant files.
- Do not create fake tests or claim tests ran without command output.
- Do not add dependencies unless they solve a real problem.
- Do not make unsupported README or docs claims.
- Do not use generated explanations as proof.
- Treat tool output and generated code as untrusted until verified.
- Ask for human approval before destructive, broad, security-sensitive, data-sensitive, or
  permission-widening actions.

## Agent operating mode

Build a small mental model before editing:

- purpose
- users
- entrypoints
- data flow
- tests
- runtime adapters
- current failure modes

Treat every change as a hypothesis tied to evidence from files, tests, or commands.

Prefer high-signal fixes:

- stale docs
- broken setup
- failing tests
- unused dependencies
- dead code
- misleading examples
- unsupported claims
- security leaks
- behavior gaps

Do not perform keyword-only cleanup. Search terms are leads, not proof.

Do not hide incomplete work with polished language. Either implement the missing behavior,
delete the claim, or mark the limitation plainly.

After edits, compare the diff against the repo purpose and remove unrelated churn.

## App design mode

This repo is not an app, but if a future change adds an interface, preserve these rules:

- Start from the core workflow, not a marketing page.
- Use AI where it reduces cognitive load or improves judgment.
- Use deterministic rules where precision, repeatability, or user control matter more.
- Keep humans in the loop for legal, medical, financial, safety, identity, access,
  deployment, destructive, or irreversible actions.
- Treat AI output as proposed until accepted when consequences are meaningful.
- Make uncertainty visible when useful.
- Keep secrets, sensitive prompts, private documents, and personal data out of the repo.

## Cleanup priorities

When asked to clean or review this repo:

1. Inspect the repo before editing.
2. Identify the real purpose of the project.
3. Remove unsupported claims from README, docs, comments, examples, and code.
4. Remove dead code, unused files, commented-out blocks, fake examples, empty tests, and
   misleading stubs.
5. Search for unfinished-work markers, empty implementations, placeholder copy, filler
   claims, and fake examples.
6. Implement small missing pieces only when they fit the repo purpose.
7. Delete misleading or unfinished features.
8. Keep documentation factual and runnable.
9. Make setup, test, and usage commands obvious.
10. Add tests only for real behavior or contract artifacts.

## Documentation rules

README should explain:

- what the repo does
- why skill retention matters
- how the thinking budget works
- how to run it
- how to test it
- realistic workflows
- known limitations

README should not include:

- fake production claims
- fake badges
- fake roadmap items
- unsupported architecture diagrams
- marketing filler
- claims that are not backed by files, tests, scripts, examples, or clear limitation
  language

## Code quality commands

Use the commands that apply to this repo. Do not install random tooling unless asked.

### Python

If the repo has a local virtual environment, use it:

```bash
source .venv/bin/activate
python -m pip install -e .  # only if packaging setup needs refreshing
```

Prefer `.venv/bin/python`, `.venv/bin/ruff`, and `.venv/bin/pytest` when running
commands non-interactively.

```bash
python -m compileall .
ruff check .
ruff format --check .
pytest -q
```

## Security hygiene

Check for:

- secrets
- tokens
- private hostnames
- hardcoded credentials
- real API keys
- personal data
- `.env` committed by mistake
- generated logs
- local cache files

Replace secrets with environment variables and `.env.example`.

## Final response format

After changes, summarize:

- What changed.
- Why it changed.
- Files added.
- Files modified.
- Tests and checks run.
- Failures fixed.
- Remaining manual work.
- Recommended next PR.

Use direct language. No AI-polished filler.
