# Cognitive Deadlift Context

This is the operating context for the repo. Every agent and contributor reads this before editing.

## Mission

Package reusable skills, runtime adapters, hooks, and validation that keep AI-assisted developers thinking. The repo treats AI as useful equipment, not a substitute for problem framing, debugging, design judgment, and review.

## Operating principles

- One source of truth per question. If two files answer the same question, fix it in `repo-audit.md` and pick a single owner.
- Smallest safe change. Prefer a five-line patch over a refactor.
- Reasoning evidence beats fluency. A confident explanation is not a check.
- The harness validates structure, not behavior. Human review still ships the change.
- Portable across macOS and Linux. No tools required beyond Python 3.11 and standard build chain.

## Anti-slop rules

- No placeholder content (`TODO`, `TBD`, `coming soon`, `lorem ipsum`).
- No marketing filler (`seamlessly`, `revolutionary`, `cutting-edge`, `world-class`, `enterprise-grade`, `best-in-class`).
- No fake examples, fake tests, or fake checks.
- No new dependencies unless they remove a real problem.
- No new abstractions until three real call sites exist.
- No new top-level docs without updating `repo-audit.md` to say what job they own.

## Validation philosophy

- Structural over semantic. The validator catches missing sections, broken links, banned phrases, secret patterns, index drift, and tracked build artifacts. It cannot judge whether a skill is good.
- Deterministic and fast. Every check finishes in under a second on this repo.
- Standard library only where possible. The supply chain stays small.
- Fail loudly. A real problem makes `make prod-gate` exit nonzero.
- One command. `make prod-gate` runs every meaningful check.

## Current assumptions

- Skills live in `skills/<name>/` with `SKILL.md`, `examples/`, `tests/`, `fixtures/`. Folder-per-skill is intentional.
- `skills/*/SKILL.md` is the shared body, and runtime adapters reference it without duplicating it.
- Hooks are optional local automation. The repo does not assume any hook is installed in a consumer repo.
- The pre-commit hook only checks that a thinking ledger is staged. It cannot verify the ledger is real.
- The repo is portable and self-contained, with no private hostnames, no customer data, and no internal infrastructure references.

## What agents must read before editing

1. This file.
2. `repo-audit.md` for the standing list of duplications, gaps, and risks.
3. `ARCHITECTURE.md` for the current structure.
4. `AGENTS.md` for generic agent behavior, then the agent-specific file (`CLAUDE.md` or `GEMINI.md`).
5. The relevant `skills/<name>/SKILL.md` if the change touches that skill.

## Language

**Cognitive Deadlift**
A deliberate reasoning exercise that makes a developer carry the intellectual weight of the task before accepting AI output.
_Avoid_: AI detox, anti-AI repo, productivity hack.

**Autopilot**
The failure mode where a developer accepts AI-generated plans or code without enough independent understanding to debug, review, or defend it.
_Avoid_: Vibe coding, laziness, AI use.

**Thinking Ledger**
A small written record of the problem, assumptions, alternatives, evidence, and trade-offs behind a non-trivial change.
_Avoid_: Status update, journal, documentation.

**Friction**
A constraint that slows action until the developer supplies missing reasoning evidence.
_Avoid_: Blocker, punishment, bureaucracy.

**Skill**
An agent instruction package that changes how an assistant approaches a class of work.
_Avoid_: Prompt, script, checklist.

**Hook**
A local automation gate that checks whether a developer has produced reasoning evidence before a risky action.
_Avoid_: Plugin, CI job.

**Plugin**
The distributable repo shape that bundles skills, hooks, scripts, and metadata into one installable package.
_Avoid_: Skill collection, extension, addon.

**Runtime Adapter**
A small manifest or instruction file that lets one shared skill library work in a specific agent harness such as Codex, Claude, or Gemini.
_Avoid_: Fork, duplicate skill, compatibility hack.

**Reasoning Evidence**
Concrete traces that the developer understood the work, such as hypotheses, code paths, tests, alternatives, constraints, or review notes.
_Avoid_: Explanation, confidence, vibes.

**Workflow Audit**
A fixed-scope commercial review of how a developer or team uses AI-assisted coding tools, focused on finding missing reasoning evidence and recommending Cognitive Deadlift skills, hooks, or review gates.
_Avoid_: Security audit, productivity survey, generic AI enablement.

**Security Posture**
The repo's layered controls for preventing malicious changes, secret exposure, unsafe automation, and supply-chain drift.
_Avoid_: Enterprise security claim, checkbox security.

**Security Gate**
A CI, review, branch, or local validation control that blocks risky changes until the missing security evidence is supplied.
_Avoid_: Test artifact, audit report.

## Flagged ambiguities

**"Against AI"**
The repo is not against AI use. The canonical stance is against autopilot, which means using AI in ways that remove human understanding from engineering decisions.

**"Force developers to think"**
The repo should force reasoning evidence at decision points, not add performative friction to every action.

**"Codex, Gemini, and Claude skills"**
The shared skill source is `skills/*/SKILL.md`. Codex, Claude, and Gemini each get a runtime adapter instead of separate duplicated skill bodies.

**"CrowdStrike level security"**
The repo cannot claim commercial EDR or enterprise SOC capability. The canonical interpretation is enterprise-style repository security covering least privilege, supply-chain checks, secret scanning, threat modeling, protected branches, and auditable security gates.
