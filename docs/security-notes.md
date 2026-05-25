# Security Notes

Last reviewed: 2026-05-25.

## Scope Checked

This pass checked the current working tree and reachable git history for obvious secrets and private references. It also ran the repo security scanner.

Commands run:

```bash
git grep -n -E 'AKIA|SECRET|TOKEN|PASSWORD|PRIVATE_KEY|BEGIN RSA|BEGIN OPENSSH|api_key|client_secret|passwd|pwd'
find . -name '.env*' -o -name '*secret*' -o -name '*key*'
python3 scripts/security_scan.py
git grep -n -E 'AKIA|SECRET|TOKEN|PASSWORD|PRIVATE_KEY|BEGIN RSA|BEGIN OPENSSH|api_key|client_secret|passwd|pwd' $(git rev-list --all)
```

## Findings

No committed credential files, `.env` files, private keys, API keys, or token-looking values were found.

The grep checks produced false positives in:

- `README.md`, from an example command using `$(pwd)`.
- `hooks/pre-commit`, from shell path setup.
- `scripts/security_scan.py`, from the scanner's own secret-pattern definitions.

`scripts/security_scan.py` passed.

## Risks Fixed

- Skill validation now checks required structure, examples, banned filler, broken internal links, duplicate skill names, and obvious secret patterns.
- CI has a no-secret path: validation, grading, tests, and security scanning run without private systems or repository secrets.
- The repo keeps a split license so code and written methodology have explicit terms.

## Manual Review Still Needed

- GitHub secret scanning and push protection should remain enabled in repository settings.
- Any future imported skill or example should be reviewed for private employer details, customer names, internal URLs, and non-public operational processes.
- If a real secret is ever committed, deleting it from the working tree is not enough. Rotate the credential and clean git history before publishing or tagging.

## Never Commit

- API keys, tokens, passwords, SSH keys, private keys, cookies, or session values.
- `.env` files or local configuration with credentials.
- Private employer details, customer data, internal URLs, incident details, or non-public infrastructure names.
- Legal, medical, or financial case data.
- Generated test artifacts, coverage directories, caches, or local grading output.
