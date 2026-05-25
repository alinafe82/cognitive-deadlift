# Threat Model

Last reviewed: 2026-05-25.

## Scope

Cognitive Deadlift is a public repository containing agent skills, plugin manifests, runtime adapter instructions, Git hooks, Python validation scripts, and GitHub Actions workflows.

It is not a hosted application. It has no database, network service, user accounts, or production runtime.

## Assets

- Maintainer GitHub permissions.
- Repository integrity and release history.
- Skill instructions consumed by Codex, Claude, Gemini, and similar agents.
- Hook and script behavior executed in downstream repositories.
- GitHub Actions workflow tokens.
- Contributor trust in the published repo.

## Trust Boundaries

- Pull requests from forks enter through GitHub Actions.
- Skills are read by agents and may influence tool use.
- Hooks and scripts execute on contributor machines when installed.
- Runtime adapters route shared skills into different agent harnesses.
- GitHub-hosted runners receive repository content and workflow tokens.

## Threats And Controls

| Threat | Impact | Controls |
| --- | --- | --- |
| Malicious skill prompt injection | Agents may perform unsafe actions in downstream repos | CODEOWNERS, PR review, skill grading, security scan, explicit skill safety policy |
| Dangerous hook/script edit | Local developer machines may execute unexpected commands | CODEOWNERS for `hooks/` and `scripts/`, security scan for shell risks, small deterministic scripts |
| Workflow token abuse | Compromised CI could write to repo or expose data | Least-privilege workflow permissions, no `pull_request_target`, dependency review |
| Secret leakage | Credentials may enter git history or logs | GitHub secret scanning, push protection, local secret-pattern scan |
| Runtime adapter drift | One harness may load weaker or stale instructions | Manifest validation and shared `skills/*/SKILL.md` source of truth |
| Supply-chain drift | Third-party actions or dependencies may change behavior | Dependabot, dependency review, action hygiene scan |

## Non-Goals

- Endpoint detection and response.
- Malware sandboxing.
- Enterprise SOC monitoring.
- Runtime isolation for every downstream user environment.

## Required Security Gates

- `make check`
- `python3 scripts/security_scan.py`
- GitHub Actions validation
- Code-owner review before protected-branch merge
