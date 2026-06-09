# Linting and Testing Standards

These standards define the checks expected before a pull request is marked ready. Run the sections for the
languages touched by the change.

## Required Gates

- Start from the default branch and keep the PR focused on one reviewable change.
- Run `git diff --check` and `git diff --cached --check` before committing.
- Run `repowave scan .` when `repowave.toml` is present.
- Run every applicable language command below. If a command needs credentials, a live service, or unavailable
  platform tooling, state that in the PR and run the closest local gate.
- Add or update tests for behavior changes. Documentation-only changes still need the diff and repository gates.

## Python

- Use `uv` with the checked-in lockfile for reproducible local and CI runs.
- Run Ruff for linting before every PR.
- Run Pytest for behavior changes, including edge cases around prompt and policy evaluation.
- Keep fixtures small and explicit; do not depend on private local files or network calls in unit tests.

## Current Command Map

- Install: `uv sync --extra test --extra lint`.
- Lint: `make lint`.
- Tests: `make test`.
- Focused repository validation: `make validate`.
- Full local gate: `make check`.
- Production gate when relevant: `make prod-gate`.
