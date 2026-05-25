# Repository Audit

Date: 2026-05-25
Branch: `skill-repo-productionization`

## Repo Purpose

Cognitive Deadlift is a reusable skill library for AI-assisted engineering. Its purpose is to keep developers from accepting AI output on autopilot by forcing problem framing, assumption checks, code tracing, test evidence, tradeoff analysis, and review discipline.

The repo is not an agent runtime, hosted service, benchmark suite, or generic prompt collection.

## Current Structure

```text
.
├── .codex-plugin/             # Codex plugin manifest
├── .claude-plugin/            # Claude plugin manifest
├── .gemini/                   # Gemini adapter note
├── .github/                   # Issue templates, CI, security workflows, CODEOWNERS
├── docs/                      # ADRs, security docs, research, licensing, quality notes
├── hooks/                     # Optional pre-commit hook
├── scripts/                   # Validation, grading, security scanning
├── skills/                    # One folder per shared skill
├── AGENTS.md                  # Codex-facing instructions
├── CLAUDE.md                  # Claude-facing instructions
├── GEMINI.md                  # Gemini-facing instructions
├── README.md                  # Project overview and usage
└── skills_index.json          # Machine-readable catalog
```

## Overall Findings

- The repo has a clear thesis: anti-autopilot AI-assisted engineering.
- The ten skills are coherent and mostly non-overlapping.
- The current skill bodies have useful boundaries, anti-patterns, process steps, and output contracts.
- The repo already has CI, security scanning, plugin manifests, and a grading script.
- The repo is not yet interview-ready because skills lack local examples and tests, the validator does not check enough of the promised standard, and documentation is split across older top-level files and newer `docs/` files.
- No skill should be removed. All should be kept but improved.

## Skill Inventory

| Skill | Appears To Do | Useful? | Duplicate? | Too Vague? | Clear Inputs/Outputs? | Examples? | Tests/Validation? | Safety Risks | Classification | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `problem-framing` | Forces a request into a concrete problem statement before implementation. | Yes | No | No | Output contract exists; inputs are implied. | No | Graded structurally only. | Low; could slow urgent work if overused. | B | Add inputs, examples, failure modes, safety notes, tests. |
| `assumption-audit` | Extracts and classifies assumptions before acting on a plan. | Yes | Partial overlap with `problem-framing`, but distinct. | No | Output contract exists; inputs are implied. | No | Graded structurally only. | Low; could become performative if every tiny claim is challenged. | B | Add examples and clearer missing-information behavior. |
| `alternatives-before-code` | Requires multiple solution paths before architecture or implementation. | Yes | Partial overlap with `complexity-budget`, but distinct. | No | Output contract exists; inputs are implied. | No | Graded structurally only. | Medium; can delay emergency work if misapplied. | B | Add examples, emergency boundary, and test fixtures. |
| `failing-test-first` | Requires a failing signal before bug fixes and behavior changes. | Yes | Partial overlap with `debugging-lab-notebook`, but narrower. | No | Output contract exists; inputs are implied. | No | Graded structurally only. | Low; must not block emergency hotfixes. | B | Add examples, fallback when test framework is absent, and fixtures. |
| `trace-the-code` | Forces code-path tracing before modifying unfamiliar behavior. | Yes | No | No | Output contract exists; inputs are implied. | No | Graded structurally only. | Low; file/line references must avoid exposing private data. | B | Add examples and edge cases for missing files or generated code. |
| `read-the-docs-first` | Requires checking local docs, ADRs, schemas, and primary sources before guessing. | Yes | No | No | Output contract exists; inputs are implied. | No | Graded structurally only. | Medium; web lookup can drift or cite stale/current-sensitive docs incorrectly. | B | Add examples, source hierarchy, and privacy note for external browsing. |
| `explain-without-ai` | Forces mechanism-level explanation before merge or handoff. | Yes | No | No | Output contract exists; inputs are implied. | No | Graded structurally only. | Low; should not demand private/confidential details. | B | Add examples, failure modes, and privacy boundaries. |
| `diff-interrogation` | Reviews diffs as untrusted claims before accepting changes. | Yes | No | No | Output contract exists; inputs are implied. | No | Graded structurally only. | Medium; should avoid overclaiming without running tests. | B | Add examples, finding format, and reviewer constraints. |
| `debugging-lab-notebook` | Structures hard debugging around reproduction, hypotheses, experiments, and regression proof. | Yes | Partial overlap with `failing-test-first`, but broader. | No | Output contract exists; inputs are implied. | No | Graded structurally only. | Medium; instrumentation can expose sensitive logs if not constrained. | B | Add examples, privacy notes, and test fixtures. |
| `complexity-budget` | Challenges abstractions, dependencies, and indirection before adding complexity. | Yes | Partial overlap with `alternatives-before-code`, but focused on cost. | No | Output contract exists; inputs are implied. | No | Graded structurally only. | Low; can bias against justified platform work if applied dogmatically. | B | Add examples, scaling caveat, and tests. |

Classification legend:

- A. Keep as-is
- B. Keep but improve
- C. Merge with another skill
- D. Rewrite
- E. Remove
- F. Move to examples/archive

## Duplication Review

No skills are strict duplicates.

- `problem-framing` and `assumption-audit` are adjacent but solve different stages: defining the problem versus testing claims in a plan.
- `alternatives-before-code` and `complexity-budget` overlap in design review but differ in output: option comparison versus cost accounting for new moving parts.
- `failing-test-first` and `debugging-lab-notebook` overlap in debugging but differ in scope: simple red-green behavior proof versus hard-bug investigation.

Keep all ten, but make their boundaries explicit in the standard and examples.

## Structural Gaps

- Skills do not yet have `examples/`, `tests/`, or `fixtures/` directories.
- Existing validation checks required files and manifests but not the full skill standard.
- Existing grading checks are useful but rubric-oriented, not enough to catch missing examples or broken internal links.
- There is no pytest suite for validator behavior.
- `ARCHITECTURE.md` exists at repo root, but the requested canonical architecture document should live at `docs/architecture.md`.
- The README is clear but not yet reviewer-oriented enough for installation, usage examples, limitations, and contribution workflow.
- There is no `docs/review-checklist.md`, `docs/skill-standard.md`, `docs/security-notes.md`, or `docs/interview-notes.md`.

## Security And Privacy Gaps

- Security scanning exists, but a dedicated security-notes audit file is missing.
- No obvious secrets were observed during inventory, but a formal grep-based audit should be run and recorded.
- Skills should explicitly forbid unsupported claims, fake checks, secret exposure, and destructive action without confirmation.

## Recommended Plan

1. Keep all ten skills.
2. Add a standard `examples/`, `tests/`, and `fixtures/` directory under each skill.
3. Rewrite each `SKILL.md` to the same production format: purpose, triggers, inputs, outputs, process, quality bar, examples, failure modes, safety/privacy, and anti-slop rules.
4. Replace or extend validation with `scripts/validate_skills.py`.
5. Add pytest tests for discovery, metadata parsing, validation failures, examples, and banned phrases.
6. Make README and docs reviewer-oriented.
7. Add ADRs for folder-per-skill layout and validation.
8. Add security-notes and interview-notes.
9. Keep the repo small; do not add a runtime framework or dependency-heavy tooling.
