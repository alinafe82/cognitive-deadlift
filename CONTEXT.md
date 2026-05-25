# Cognitive Deadlift

Cognitive Deadlift is a developer-tooling context for AI-assisted engineering that preserves human reasoning. It treats AI as useful equipment, not a substitute for problem framing, debugging, design judgment, and review.

## Language

**Cognitive Deadlift**:
A deliberate reasoning exercise that makes a developer carry the intellectual weight of the task before accepting AI output.
_Avoid_: AI detox, anti-AI repo, productivity hack

**Autopilot**:
The failure mode where a developer accepts AI-generated plans or code without enough independent understanding to debug, review, or defend it.
_Avoid_: Vibe coding, laziness, AI use

**Thinking Ledger**:
A small written record of the problem, assumptions, alternatives, evidence, and trade-offs behind a non-trivial change.
_Avoid_: Status update, journal, documentation

**Friction**:
A constraint that slows action until the developer supplies missing reasoning evidence.
_Avoid_: Blocker, punishment, bureaucracy

**Skill**:
An agent instruction package that changes how Codex approaches a class of work.
_Avoid_: Prompt, script, checklist

**Hook**:
A local automation gate that checks whether a developer has produced reasoning evidence before a risky action.
_Avoid_: Plugin, CI job

**Plugin**:
The distributable repo shape that bundles skills, hooks, scripts, and metadata into one installable package.
_Avoid_: Skill collection, extension, addon

**Runtime Adapter**:
A small manifest or instruction file that lets one shared skill library work in a specific agent harness such as Codex, Claude, or Gemini.
_Avoid_: Fork, duplicate skill, compatibility hack

**Reasoning Evidence**:
Concrete traces that the developer understood the work: hypotheses, code paths, tests, alternatives, constraints, or review notes.
_Avoid_: Explanation, confidence, vibes

**Security Posture**:
The repo's layered controls for preventing malicious changes, secret exposure, unsafe automation, and supply-chain drift.
_Avoid_: Enterprise security claim, checkbox security

**Security Gate**:
A CI, review, branch, or local validation control that blocks risky changes until the missing security evidence is supplied.
_Avoid_: Test artifact, audit report

## Flagged Ambiguities

**"Against AI"**:
The repo is not against AI use. The canonical stance is against autopilot: using AI in ways that remove human understanding from engineering decisions.

**"Force developers to think"**:
The repo should force reasoning evidence at decision points, not add performative friction to every action.

**"Codex, Gemini, and Claude skills"**:
The shared skill source is `skills/*/SKILL.md`. Codex, Claude, and Gemini each get a runtime adapter instead of separate duplicated skill bodies.

**"CrowdStrike level security"**:
The repo cannot honestly claim commercial EDR or enterprise SOC capability. The canonical interpretation is enterprise-style repository security: least privilege, supply-chain checks, secret scanning, threat modeling, protected branches, and auditable security gates.

## Example Dialogue

Developer: "AI wrote the fix. Can I merge it?"

Reviewer: "Show the thinking ledger first. What bug did you reproduce, which code path did you trace, what alternatives did you reject, and what test proves the behavior?"

Developer: "The ledger says the failure is in token refresh, not login. I traced the retry path, rejected a global timeout increase, and added a failing integration test around expired refresh tokens."

Reviewer: "That is reasoning evidence. Now interrogate the diff."
