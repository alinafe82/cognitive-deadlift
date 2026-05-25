# Incident Response

Last reviewed: 2026-05-25.

## Severity

| Severity | Examples | Response |
| --- | --- | --- |
| Critical | Secret leak, malicious workflow, malicious hook/script | Disable affected path, rotate secrets, force a clean commit, publish advisory |
| High | Security gate bypass, unsafe skill instruction, CI token over-permission | Patch quickly, add regression check, document impact |
| Medium | Missing ownership, weak workflow permission, non-blocking scanner gap | Fix in normal security hardening |
| Low | Documentation ambiguity or stale security note | Fix in normal maintenance |

## Response Steps

1. Preserve evidence: commit hash, PR, workflow run, report, and timestamps.
2. Contain: disable or revert the affected hook, script, skill, or workflow.
3. Eradicate: remove malicious or unsafe content and add a regression check.
4. Recover: run `make check`, security scan, and GitHub Actions.
5. Communicate: update `SECURITY.md`, advisory, or release notes as appropriate.
6. Improve: add a new security gate when the incident revealed a missing control.

## Secret Exposure

If a secret is committed, assume it is compromised. Remove it from history only as part of a coordinated response, rotate it first, and document the timeline privately before public disclosure.
