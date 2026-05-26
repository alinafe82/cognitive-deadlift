#!/usr/bin/env python3
"""Validate Cognitive Deadlift repository structure."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_ROOT_FILES = [
    "README.md",
    "LICENSE",
    "CONTEXT.md",
    "AGENTS.md",
    "CLAUDE.md",
    "GEMINI.md",
    ".codex-plugin/plugin.json",
    ".claude-plugin/plugin.json",
    "gemini-extension.json",
    "SECURITY.md",
    "docs/security/threat-model.md",
    "docs/security/supply-chain.md",
    "docs/security/branch-protection.md",
    "docs/security/incident-response.md",
    "scripts/security_scan.py",
    "scripts/validate_skills.py",
    "docs/architecture.md",
    "docs/skill-standard.md",
    "docs/review-checklist.md",
]


def fail(message: str) -> int:
    print(f"validate_repo: {message}", file=sys.stderr)
    return 1


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def skill_dirs() -> list[Path]:
    return sorted(path for path in (ROOT / "skills").iterdir() if path.is_dir())


def validate_required_files() -> int:
    for relative in REQUIRED_ROOT_FILES:
        if not (ROOT / relative).exists():
            return fail(f"missing required file: {relative}")
    return 0


def validate_skills() -> int:
    dirs = skill_dirs()
    if not dirs:
        return fail("skills directory has no skills")

    for directory in dirs:
        skill_file = directory / "SKILL.md"
        if not skill_file.exists():
            return fail(f"missing SKILL.md in {directory.relative_to(ROOT)}")
        text = skill_file.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            return fail(f"missing YAML frontmatter in {skill_file.relative_to(ROOT)}")
        if "name:" not in text.split("---", 2)[1]:
            return fail(f"missing frontmatter name in {skill_file.relative_to(ROOT)}")
        if "description:" not in text.split("---", 2)[1]:
            return fail(f"missing frontmatter description in {skill_file.relative_to(ROOT)}")
    return 0


def validate_claude_manifest() -> int:
    manifest = load_json(ROOT / ".claude-plugin" / "plugin.json")
    listed = sorted(Path(item).as_posix().removeprefix("./") for item in manifest.get("skills", []))
    actual = sorted(path.relative_to(ROOT).as_posix() for path in skill_dirs())
    if listed != actual:
        return fail(".claude-plugin/plugin.json skills list does not match skills/")
    return 0


def validate_codex_manifest() -> int:
    manifest = load_json(ROOT / ".codex-plugin" / "plugin.json")
    if manifest.get("skills") != "./skills/":
        return fail(".codex-plugin/plugin.json must point skills to ./skills/")
    return 0


def validate_gemini_manifest() -> int:
    manifest = load_json(ROOT / "gemini-extension.json")
    if manifest.get("contextFileName") != "GEMINI.md":
        return fail("gemini-extension.json must use GEMINI.md as contextFileName")
    return 0


def main() -> int:
    checks = [
        validate_required_files,
        validate_skills,
        validate_claude_manifest,
        validate_codex_manifest,
        validate_gemini_manifest,
    ]

    for check in checks:
        result = check()
        if result != 0:
            return result

    print("validate_repo: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
