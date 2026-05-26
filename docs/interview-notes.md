# Interview Notes

## 60-Second Explanation

Cognitive Deadlift is a small skill library for developers who use AI coding assistants but still want a disciplined engineering workflow. The skills force problem framing, assumption checks, code tracing, failing tests, alternatives, and diff interrogation before implementation or merge. The repo treats those skills like engineering artifacts: each one has structure, examples, validation, tests, safety notes, and CI.

## Problem It Solves

AI tools can make repeated engineering steps optional. That is risky in code review, debugging, and design because the assistant may produce confident output without evidence. This repo standardizes reusable reasoning workflows so a developer can ask for a specific skill and get a predictable review surface.

## Why It Matters

This maps directly to Engineering Productivity:

- standardizes repeated work
- reduces prompt sprawl
- improves review quality
- adds quality gates around reusable instructions
- keeps validation local and cheap
- documents tradeoffs and limitations

## Design Choices I Can Defend

- Folder-per-skill layout keeps instructions, examples, and fixtures together.
- One shared skill body avoids Codex, Claude, and Gemini copies drifting apart.
- Python validators use the standard library to keep the supply chain small.
- Pytest is used only where it adds real regression coverage.
- Security scanning is local, deterministic, and does not require secrets.
- Docs explain limitations instead of claiming model behavior can be guaranteed.

## Tradeoffs

- Structural validation cannot prove model compliance.
- Small skills carry extra directories, but consistency makes review easier.
- The repo avoids runtime-specific skill forks, so adapters may need thin compatibility notes.
- The quality bar is strict enough to reject weak prompts, but human review is still required.

## Intentionally Kept Simple

- No plugin runtime framework.
- No model-evaluation harness.
- No external validation service.
- No private company workflow assumptions.
- No dependency-heavy markdown toolchain.

## What I Would Improve Next

- Generate `CATALOG.md` from skill metadata.
- Add schema validation for richer metadata if the skill count grows.
- Add sampled runtime compatibility checks for Codex, Claude, and Gemini.
- Add semantic duplicate detection once there are enough skills to justify it.
- Add release notes and versioned skill bundles when consumers depend on stable versions.

## Likely Questions And Answers

### Why is this more than a prompt repo?

Because every skill has a standard shape, examples, failure modes, safety notes, validation, tests, and review criteria. The repo is designed for maintenance, not just inspiration.

### Why not build a full plugin framework?

The current problem is quality and reuse of instructions, not runtime dispatch. A framework would add complexity before there is evidence that it is needed.

### How do you know the skills work?

The repo validates structure and examples deterministically. It does not claim to prove model behavior. Human review and runtime trials are still required for behavioral confidence.

### How does this reduce repeated work?

Instead of rewriting the same review prompt for every bug, design, or diff, developers can invoke a named skill with a known output shape and quality bar.

### What makes this relevant to Google Engineering Productivity?

It focuses on repeatable developer workflows, quality gates, maintainability, local tooling, reviewability, and reducing accidental complexity.
