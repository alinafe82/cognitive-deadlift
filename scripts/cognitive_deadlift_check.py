#!/usr/bin/env python3
"""Check staged changes for a Cognitive Deadlift thinking ledger."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

SOURCE_SUFFIXES = {
    ".c",
    ".cc",
    ".cpp",
    ".cs",
    ".css",
    ".go",
    ".h",
    ".hpp",
    ".html",
    ".java",
    ".js",
    ".jsx",
    ".kt",
    ".mjs",
    ".py",
    ".rb",
    ".rs",
    ".sh",
    ".sql",
    ".swift",
    ".ts",
    ".tsx",
    ".vue",
    ".yaml",
    ".yml",
}

IGNORED_PREFIXES = (
    "docs/thinking/",
    "vendor/",
    "node_modules/",
    "dist/",
    "build/",
)


def git(args: list[str]) -> str:
    result = subprocess.run(
        ["git", *args],
        check=True,
        text=True,
        capture_output=True,
    )
    return result.stdout


def staged_files() -> list[Path]:
    output = git(["diff", "--cached", "--name-only", "--diff-filter=ACMR"])
    return [Path(line) for line in output.splitlines() if line.strip()]


def is_source_change(path: Path) -> bool:
    posix = path.as_posix()
    if posix.startswith(IGNORED_PREFIXES):
        return False
    return path.suffix.lower() in SOURCE_SUFFIXES


def has_thinking_ledger(files: list[Path]) -> bool:
    return any(
        path.as_posix().startswith("docs/thinking/")
        and path.name != "TEMPLATE.md"
        and path.suffix.lower() == ".md"
        for path in files
    )


def main() -> int:
    if os.getenv("COGNITIVE_DEADLIFT_BYPASS") == "1":
        print("Cognitive Deadlift bypassed by COGNITIVE_DEADLIFT_BYPASS=1.")
        return 0

    try:
        files = staged_files()
    except subprocess.CalledProcessError as error:
        sys.stderr.write(error.stderr)
        return error.returncode

    source_changes = [path for path in files if is_source_change(path)]
    if not source_changes:
        return 0

    if has_thinking_ledger(files):
        return 0

    print("Cognitive Deadlift blocked this commit.")
    print("")
    print("Staged source changes need reasoning evidence.")
    print("Add a staged docs/thinking/<short-name>.md using docs/thinking/TEMPLATE.md.")
    print("")
    print("Source changes detected:")
    for path in source_changes[:20]:
        print(f"  - {path}")
    if len(source_changes) > 20:
        print(f"  - ... {len(source_changes) - 20} more")
    print("")
    print("For a truly mechanical change:")
    print("  COGNITIVE_DEADLIFT_BYPASS=1 git commit")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
