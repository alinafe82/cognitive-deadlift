# Branch Protection

Last reviewed: 2026-08-23.

Recommended `main` branch settings:

- Require a pull request before merging.
- Require at least one approving review.
- Require review from code owners.
- Dismiss stale approvals when new commits are pushed.
- Require status checks to pass.
- Require branches to be up to date before merging.
- Require conversation resolution.
- Require linear history.
- Do not allow force pushes.
- Do not allow deletions.

Required checks should include:

- `validate`
- `security-hygiene`
- `check`
- `Python 3.13 compatibility`
- `Analyze Python`
- `dependency-review`
- `gitleaks`

These settings are repository configuration, not source files. They must be applied in GitHub after workflows exist.
