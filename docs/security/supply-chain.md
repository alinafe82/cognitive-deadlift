# Supply Chain Security

Last reviewed: 2026-05-25.

## Policy

This repo should stay boring and auditable.

- Prefer standard-library Python for repository checks.
- Do not add runtime dependencies unless the security or usability benefit is clear.
- Keep GitHub Actions permissions least-privilege.
- Avoid `pull_request_target` unless an ADR explains the threat model.
- Do not fetch and execute remote scripts in hooks, skills, or CI.
- Do not commit generated test artifacts, logs, caches, or reports.

## GitHub Actions

Allowed action categories:

- First-party GitHub actions such as `actions/checkout`, `actions/setup-python`, and `github/codeql-action`.
- GitHub security actions such as `actions/dependency-review-action`.

Third-party actions require a maintainer review and an explicit reason in the pull request.

## Skills

Skills are instructions that can shape agent behavior. Treat them like code:

- Require clear `NOT for` boundaries.
- Include explicit safety limits for destructive actions.
- Keep output contracts auditable.
- Do not instruct agents to bypass security gates quietly.

## Hooks And Scripts

Hooks and scripts must:

- Operate on local repository state.
- Avoid network calls by default.
- Avoid shell interpolation where possible.
- Provide clear error messages.
- Support explicit, searchable bypasses only when justified.
