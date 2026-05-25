# Security Policy

Cognitive Deadlift is installable developer tooling. Treat every skill, hook, script, workflow, and runtime adapter as supply-chain surface.

## Supported Versions

Only the current `main` branch is supported before the first stable release.

## Reporting A Vulnerability

Use GitHub private vulnerability reporting or a private security advisory if available. If that is unavailable, contact the maintainer through the GitHub profile listed in the plugin manifest.

Do not open a public issue for secrets, exploit details, or bypasses until a maintainer has coordinated disclosure.

## Security Model

Primary risks:

- Malicious skill instructions that cause unsafe agent behavior.
- Hook or script changes that execute unexpected commands.
- GitHub Actions supply-chain compromise.
- Secret exposure through committed files, logs, or generated artifacts.
- Runtime adapter drift between Codex, Claude, and Gemini.

Required controls:

- All workflows use least-privilege `permissions`.
- Security-sensitive paths are owned in `CODEOWNERS`.
- CI runs repository validation, skill grading, and security hygiene checks.
- GitHub secret scanning and push protection should remain enabled.
- Branch protection should require pull requests, code-owner review, and passing checks.
- Generated test artifacts, coverage, caches, logs, and reports must not be committed.

## Skill Safety

Skills must not instruct agents to:

- Exfiltrate secrets or credentials.
- Disable security tools without explicit user approval.
- Run destructive commands without clear confirmation.
- Fetch or execute remote code as part of normal use.
- Hide bypasses or weaken review evidence.

## Hook And Script Safety

Hooks and scripts should be small, deterministic, and local-repository scoped. They should prefer read-only inspection and fail closed when security assumptions are not met.

Any bypass must be explicit, searchable, and documented. Silent bypasses are security bugs.

## Maintainer Response

Security reports should receive an initial response within 7 days. Critical issues should be triaged as soon as practical and fixed before public disclosure when possible.
