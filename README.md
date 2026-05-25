# Cognitive Deadlift

Codex skills, Claude skills, Gemini instructions, AI coding hooks, and agent plugins for developers who use AI without outsourcing their thinking.

AI can write code faster than you can type. That is not the same as engineering.

Cognitive Deadlift is a public multi-agent skills repo for developers who use AI without letting it dissolve their judgment. It ships Codex skills, Claude skills, Gemini-compatible instructions, hooks, and scripts that force the developer to frame problems, challenge assumptions, read the code, form hypotheses, write failing tests, compare alternatives, and interrogate diffs.

The position is not anti-AI. It is anti-autopilot.

## Why This Exists

The risk is not that AI writes code. The risk is that developers stop practicing the mental work that makes code review, debugging, design, and incident response possible.

Recent research points at the shape of the problem:

- Microsoft Research found that higher confidence in GenAI is associated with less critical thinking effort, while higher self-confidence is associated with more critical thinking.
- METR found that, in one randomized controlled trial, experienced open-source developers took 19% longer with early-2025 AI tools while still believing AI had sped them up.
- Anthropic found that AI-assisted developers scored lower on immediate mastery of a new Python library, while the strongest learners used AI for explanation and conceptual inquiry instead of delegation.
- A GitHub Copilot brownfield-task study found students were faster with Copilot but reported concern about not understanding how or why suggestions worked.
- The MIT Media Lab-led "Your Brain on ChatGPT" preprint argues that LLM-assisted writing can produce cognitive costs and lower ownership, while acknowledging the need for deeper study.

Those findings do not prove that AI is bad for software engineering. They do support a stricter operating model: AI should accelerate known mechanics, not replace the developer's thinking loop.

## What Is Inside

Runtime adapters:

- Codex: `.codex-plugin/plugin.json` and `AGENTS.md`.
- Claude: `.claude-plugin/plugin.json` and `CLAUDE.md`.
- Gemini: `gemini-extension.json` and `GEMINI.md`.

Initial skills:

- `problem-framing` - turn a request into a clear problem statement before implementation.
- `assumption-audit` - list and challenge the assumptions hidden in a plan or prompt.
- `alternatives-before-code` - compare at least three solution paths before choosing one.
- `failing-test-first` - prove the bug or missing behavior before writing the fix.
- `trace-the-code` - follow the current execution path before asking AI to invent one.
- `read-the-docs-first` - inspect source docs, ADRs, interfaces, and contracts before guessing.
- `explain-without-ai` - make the developer explain the approach without model help.
- `diff-interrogation` - review a generated or human diff as if it came from an untrusted contributor.
- `debugging-lab-notebook` - run a disciplined reproduce, hypothesize, instrument, verify loop.
- `complexity-budget` - reject cleverness unless the extra moving parts pay for themselves.

See [CATALOG.md](CATALOG.md) for the searchable skill catalog.

Hook and script foundation:

- `scripts/cognitive_deadlift_check.py` - checks whether a staged code change includes a thinking ledger.
- `hooks/pre-commit` - optional Git pre-commit hook that runs the check.
- `docs/thinking/TEMPLATE.md` - lightweight evidence of human reasoning for non-trivial changes.

## Install As A Codex Plugin

Clone the repo, then add it as a local plugin from the repo root:

```bash
codex plugin add .
```

## Use The Optional Hook

From this repo, copy or symlink the hook into another repo that should enforce a thinking ledger:

```bash
ln -s "$(pwd)/hooks/pre-commit" /path/to/target-repo/.git/hooks/pre-commit
```

The hook requires a staged `docs/thinking/*.md` file for staged source changes. Bypass only for truly mechanical work:

```bash
COGNITIVE_DEADLIFT_BYPASS=1 git commit
```

## Research Notes

See [docs/research-brief.md](docs/research-brief.md) for the source-grounded argument behind the repo.

## Quality Checks

Run the local validation and skill grading checks:

```bash
make check
```

The grader requires each skill to keep clear activation boundaries, anti-pattern coverage, a decision flow, explicit tooling expectations, and a structured output contract.

## License

MIT
