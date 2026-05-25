#!/usr/bin/env python3
"""Security hygiene scan for Cognitive Deadlift."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github" / "workflows"
SENSITIVE_CODEOWNER_PATHS = [
    "/.github/",
    "/.codex-plugin/",
    "/.claude-plugin/",
    "/hooks/",
    "/scripts/",
    "/skills/",
    "/SECURITY.md",
]

SECRET_PATTERNS = [
    re.compile(r"-----BEGIN (?:RSA |DSA |EC |OPENSSH |PGP )?PRIVATE KEY-----"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{36,}\b"),
    re.compile(r"\bsk-[A-Za-z0-9]{32,}\b"),
    re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b"),
    re.compile(r"(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*['\"][^'\"\s]{16,}['\"]"),
]

DANGEROUS_TEXT_PATTERNS = [
    (re.compile(r"curl\b[^\n|]*\|\s*(?:sh|bash)"), "curl piped to shell"),
    (re.compile(r"wget\b[^\n|]*\|\s*(?:sh|bash)"), "wget piped to shell"),
    (re.compile(r"\beval\s+['\"]?\$\("), "eval of command substitution"),
    (re.compile(r"\bos\.system\s*\("), "os.system call"),
    (
        re.compile(r"subprocess\.(?:run|call|Popen)\([^)]*shell\s*=\s*True", re.DOTALL),
        "subprocess shell=True",
    ),
]

ALLOWED_UNPINNED_ACTION_OWNERS = {"actions", "github"}


def repo_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )
    files: list[Path] = []
    for line in result.stdout.splitlines():
        path = ROOT / line
        if line.strip() and path.exists():
            files.append(path)
    return files


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return ""


def fail(findings: list[str], message: str) -> None:
    findings.append(message)


def check_secrets(findings: list[str]) -> None:
    for path in repo_files():
        text = read_text(path)
        if not text:
            continue
        relative = path.relative_to(ROOT)
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                fail(findings, f"possible secret pattern in {relative}")


def check_dangerous_patterns(findings: list[str]) -> None:
    for path in repo_files():
        text = read_text(path)
        if not text:
            continue
        relative = path.relative_to(ROOT)
        for pattern, label in DANGEROUS_TEXT_PATTERNS:
            if pattern.search(text):
                fail(findings, f"{label} found in {relative}")


def check_codeowners(findings: list[str]) -> None:
    codeowners = ROOT / ".github" / "CODEOWNERS"
    if not codeowners.exists():
        fail(findings, ".github/CODEOWNERS is missing")
        return

    text = codeowners.read_text(encoding="utf-8")
    for path in SENSITIVE_CODEOWNER_PATHS:
        if path not in text:
            fail(findings, f"CODEOWNERS missing sensitive path: {path}")


def extract_uses(line: str) -> str | None:
    stripped = line.strip()
    if not stripped.startswith("uses:"):
        return None
    return stripped.split(":", 1)[1].strip().strip('"').strip("'")


def action_is_pinned_or_allowed(action: str) -> bool:
    if action.startswith("./") or action.startswith("docker://"):
        return True
    if "@" not in action:
        return False
    repo, ref = action.rsplit("@", 1)
    owner = repo.split("/", 1)[0]
    if re.fullmatch(r"[a-f0-9]{40}", ref):
        return True
    return owner in ALLOWED_UNPINNED_ACTION_OWNERS and re.fullmatch(r"v\d+(?:\.\d+){0,2}", ref)


def check_workflows(findings: list[str]) -> None:
    if not WORKFLOWS.exists():
        fail(findings, ".github/workflows is missing")
        return

    for workflow in sorted(WORKFLOWS.glob("*.yml")) + sorted(WORKFLOWS.glob("*.yaml")):
        text = workflow.read_text(encoding="utf-8")
        relative = workflow.relative_to(ROOT)
        if "\npermissions:" not in f"\n{text}":
            fail(findings, f"{relative} missing top-level permissions")
        if "write-all" in text:
            fail(findings, f"{relative} uses write-all permissions")
        if "pull_request_target" in text:
            fail(findings, f"{relative} uses pull_request_target")
        if "timeout-minutes:" not in text:
            fail(findings, f"{relative} missing timeout-minutes")

        for line_number, line in enumerate(text.splitlines(), start=1):
            action = extract_uses(line)
            if action and not action_is_pinned_or_allowed(action):
                message = (
                    f"{relative}:{line_number} action is not pinned or "
                    f"first-party semver: {action}"
                )
                fail(
                    findings,
                    message,
                )


def main() -> int:
    findings: list[str] = []
    check_secrets(findings)
    check_dangerous_patterns(findings)
    check_codeowners(findings)
    check_workflows(findings)

    if findings:
        print("security_scan: failed")
        for finding in findings:
            print(f"- {finding}")
        return 1

    print("security_scan: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
