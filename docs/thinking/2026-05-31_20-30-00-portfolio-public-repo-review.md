# Thinking Ledger

## Problem

The public-facing portfolio of 11 repos reads as "ten variations on one AI-generated template" to a senior platform reviewer. The user wants the portfolio to be sharper, not bigger: pin a differentiated set, fix slop in GitHub descriptions, fix real security findings (exception leakage), and document everything else as planned follow-up.

## Current Evidence

- `gh repo list` confirmed all 11 named public repos exist.
- A structural pass across all 10 non-cognitive-deadlift repos found suspiciously identical scaffolding: identical `repowave.toml` (170 bytes), identical pre-commit-config.yaml (728 bytes for agent repos, 438 for infra), identical Dockerfile (371 bytes in ticket-triage-agent and compliance-copilot).
- Five repos share the same docs/ subtree: `architecture.md`, `runbook.md`, `security-notes.md`, `production-readiness.md`. This is the "generated sameness" signature.
- Reading READMEs, the prose itself is mostly grounded. The main slop sources are the GitHub repo descriptions (one-line sales pitches on the profile page) and the repeated section headings.
- grep across `src/`, `app/` directories of the four FastAPI repos found `str(e)` or `str(exc)` returned in client response bodies in three of them.

## Assumptions

- A full per-repo rewrite cannot ship in one session. The most leveraged thing is the source-of-truth review doc plus the low-effort high-impact fixes.
- The user's pinning recommendation is sound. Confirming it against actual repo state did not change my recommendation.
- `gh repo edit --description` is the right tool for fixing one-line descriptions without needing a PR per repo.
- The `str(e)` leakage is a real finding, not a style preference. Three separate fix PRs are the right shape.
- The slop scanner I added in cognitive-deadlift's PR #7 should catch slop in my own spec doc. It did. Backticking the quoted slop is the right escape.

## Alternatives

- **Do nothing except write the spec.** Rejected. The exception leakage is a real bug and the GitHub descriptions cost nothing to fix.
- **Open one mega-PR across all repos.** Rejected. Per-repo PRs are reviewable; a cross-repo blob is not.
- **Rewrite every README in one shot.** Rejected. Each README needs careful per-repo voice. Mass-editing READMEs would reintroduce the "generated sameness" problem from a different angle.
- **Use gh repo edit to also pin/unpin/archive.** Rejected. Pinning and archiving are user decisions, not auto-applicable.

## Chosen Approach

- Survey all 11 repos, document the inventory and decisions in `specs/public-portfolio-repo-review.md`.
- Fix 11 GitHub repo descriptions via `gh repo edit`.
- Open three separate security PRs for the `str(e)` leaks (mlops-factory, ticket-triage-agent, compliance-copilot).
- Document all remaining per-repo work in the spec doc as planned follow-up, not as work pretending to be done.

## Verification

- `make prod-gate`: pass (13 tests).
- `gh repo list alinafe82` shows all 11 descriptions updated to grounded, mechanism-specific one-liners.
- Three PRs opened:
  - mlops-factory PR #29: `/infer` no longer returns `str(e)`. New test passes.
  - ticket-triage-agent PR #6: `/triage` 500 path no longer returns `str(e)`.
  - compliance-copilot PR #16: three response-bound `str(exc)` leaks closed in LLM, timeout, and ValueError handlers.

## Residual Risk

- I did not run `gitleaks` or `trufflehog` on any repo. Recommended next pass.
- I did not run each repo's full test suite. Three of the four FastAPI repos likely have heavier dependency sets that need a per-repo venv.
- I did not verify CORS defaults across the FastAPI repos.
- The Dockerfiles in ticket-triage-agent and compliance-copilot have identical byte counts. I did not diff them or verify the non-root-user pattern.
- The orbital-factory-mlops archive decision needs user confirmation before action.
- The compliance-copilot rename decision (to `pr-risk-scorer` or similar) needs user confirmation before action.
- READMEs still share repeated section headings. Per-repo PRs to differentiate them are listed in the spec.
