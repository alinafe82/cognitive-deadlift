#!/usr/bin/env python3
"""Validate Cognitive Deadlift skill structure and content."""

from __future__ import annotations

import argparse
import re
import shlex
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"

REQUIRED_SECTIONS = [
    "Purpose",
    "When To Use",
    "When Not To Use",
    "Inputs Expected",
    "Output Expected",
    "Process",
    "Quality Bar",
    "Examples",
    "Failure Modes",
    "Safety And Privacy",
    "Anti-Slop Rules",
]

BANNED_PHRASES = [
    "seamlessly",
    "revolutionary",
    "cutting-edge",
    "unlock potential",
    "transform workflows",
    "enterprise-grade",
    "best-in-class",
    "world-class",
]

PLACEHOLDER_PATTERNS = [
    re.compile(r"\bTODO\b", re.IGNORECASE),
    re.compile(r"\bTBD\b", re.IGNORECASE),
    re.compile(r"coming soon", re.IGNORECASE),
    re.compile(r"lorem ipsum", re.IGNORECASE),
]

SECRET_PATTERNS = [
    re.compile(r"-----BEGIN (?:RSA |DSA |EC |OPENSSH |PGP )?PRIVATE KEY-----"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{36,}\b"),
    re.compile(r"(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*['\"][^'\"\s]{16,}['\"]"),
]

LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")

FENCED_CODE_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`\n]+`")


def strip_code(text: str) -> str:
    """Remove fenced code blocks and inline code spans for slop scanning.

    Banned phrases inside backticks are intentional (e.g., listing what NOT
    to write), so they should not count as violations.
    """
    without_fences = FENCED_CODE_RE.sub("", text)
    return INLINE_CODE_RE.sub("", without_fences)


@dataclass(frozen=True)
class ValidationResult:
    errors: list[str]

    @property
    def ok(self) -> bool:
        return not self.errors


def parse_frontmatter(text: str) -> tuple[dict[str, str], list[str]]:
    errors: list[str] = []
    if not text.startswith("---\n"):
        return {}, ["missing YAML frontmatter"]

    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, ["unterminated YAML frontmatter"]

    values: dict[str, str] = {}
    for line in parts[1].splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            errors.append(f"invalid frontmatter line: {line}")
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")

    return values, errors


def skill_dirs(root: Path = ROOT) -> list[Path]:
    skills_root = root / "skills"
    if not skills_root.exists():
        return []
    return sorted(path for path in skills_root.iterdir() if path.is_dir())


def markdown_files(root: Path) -> list[Path]:
    return sorted(path for path in root.rglob("*.md") if path.is_file())


def is_excluded_markdown(path: Path, root: Path) -> bool:
    try:
        parts = path.relative_to(root).parts
    except ValueError:
        return False

    excluded_prefixes = [
        (".git",),
        (".venv",),
        ("tests", "fixtures"),
    ]
    return any(parts[: len(prefix)] == prefix for prefix in excluded_prefixes)


def has_heading(text: str, heading: str) -> bool:
    return f"\n## {heading}\n" in text or text.startswith(f"## {heading}\n")


def relative(path: Path, root: Path = ROOT) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def validate_no_bad_text(path: Path, text: str, root: Path, errors: list[str]) -> None:
    scannable = strip_code(text)
    lower = scannable.lower()
    for phrase in BANNED_PHRASES:
        if phrase in lower:
            errors.append(f"{relative(path, root)} contains banned filler phrase: {phrase}")

    for pattern in PLACEHOLDER_PATTERNS:
        if pattern.search(scannable):
            errors.append(f"{relative(path, root)} contains placeholder text: {pattern.pattern}")

    # Secret patterns still scan the raw text — secrets in code blocks are still secrets.
    for pattern in SECRET_PATTERNS:
        if pattern.search(text):
            errors.append(f"{relative(path, root)} contains possible secret material")


def parse_markdown_link_target(raw_target: str) -> str:
    """Return the link destination, ignoring an optional Markdown title."""
    target = raw_target.strip()
    try:
        parts = shlex.split(target)
    except ValueError:
        parts = target.split(maxsplit=1)

    if parts:
        target = parts[0]

    if target.startswith("<") and target.endswith(">"):
        return target[1:-1].strip()
    return target


def validate_links(path: Path, text: str, root: Path, errors: list[str]) -> None:
    for match in LINK_RE.finditer(text):
        target = parse_markdown_link_target(match.group(1))
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target_path = (path.parent / target.split("#", 1)[0]).resolve()
        if target_path == path.parent.resolve():
            continue
        if not target_path.exists():
            errors.append(f"{relative(path, root)} has broken internal link: {target}")


def validate_skill(skill_dir: Path, root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    skill_file = skill_dir / "SKILL.md"
    name = skill_dir.name

    if not skill_file.exists():
        return [f"{relative(skill_dir, root)} missing SKILL.md"]

    text = skill_file.read_text(encoding="utf-8")
    metadata, metadata_errors = parse_frontmatter(text)
    errors.extend(f"{relative(skill_file, root)} {error}" for error in metadata_errors)

    if metadata.get("name") != name:
        errors.append(f"{relative(skill_file, root)} frontmatter name must match folder name")

    description = metadata.get("description", "")
    if not description:
        errors.append(f"{relative(skill_file, root)} missing description")
    if "Use when" not in description:
        errors.append(f"{relative(skill_file, root)} description must include 'Use when'")
    if "NOT for" not in description:
        errors.append(f"{relative(skill_file, root)} description must include 'NOT for'")

    for section in REQUIRED_SECTIONS:
        if not has_heading(text, section):
            errors.append(f"{relative(skill_file, root)} missing section: {section}")

    for directory in ["examples", "tests", "fixtures"]:
        child = skill_dir / directory
        if not child.is_dir():
            errors.append(f"{relative(skill_dir, root)} missing {directory}/")
        elif not any(child.iterdir()):
            errors.append(f"{relative(child, root)} is empty")

    examples_dir = skill_dir / "examples"
    examples = sorted(examples_dir.glob("*.md")) if examples_dir.exists() else []
    if len(examples) < 2:
        errors.append(f"{relative(skill_dir, root)} must include at least two markdown examples")

    for md_file in markdown_files(skill_dir):
        content = md_file.read_text(encoding="utf-8")
        if not content.strip():
            errors.append(f"{relative(md_file, root)} is empty")
        validate_no_bad_text(md_file, content, root, errors)
        validate_links(md_file, content, root, errors)

    return errors


def validate_all(root: Path = ROOT) -> ValidationResult:
    errors: list[str] = []
    dirs = skill_dirs(root)
    if not dirs:
        errors.append("skills/ has no skill directories")

    seen_names: set[str] = set()
    for directory in dirs:
        skill_file = directory / "SKILL.md"
        metadata, _ = (
            parse_frontmatter(skill_file.read_text(encoding="utf-8"))
            if skill_file.exists()
            else ({}, [])
        )
        name = metadata.get("name", directory.name)
        if name in seen_names:
            errors.append(f"duplicate skill name: {name}")
        seen_names.add(name)
        errors.extend(validate_skill(directory, root))

    for md_file in markdown_files(root):
        if is_excluded_markdown(md_file, root):
            continue
        content = md_file.read_text(encoding="utf-8")
        validate_no_bad_text(md_file, content, root, errors)
        validate_links(md_file, content, root, errors)

    return ValidationResult(errors)


def slop_scan(root: Path = ROOT) -> ValidationResult:
    """Scan all repo markdown for banned filler, placeholders, and secret patterns."""
    errors: list[str] = []
    for md_file in markdown_files(root):
        if is_excluded_markdown(md_file, root):
            continue
        content = md_file.read_text(encoding="utf-8")
        validate_no_bad_text(md_file, content, root, errors)
    return ValidationResult(errors)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument(
        "--slop-only",
        action="store_true",
        help="Only run the banned-phrase / placeholder / secret scan.",
    )
    args = parser.parse_args()

    root = args.root.resolve()
    if args.slop_only:
        result = slop_scan(root)
        label = "slop_scan"
    else:
        result = validate_all(root)
        label = "validate_skills"

    if not result.ok:
        print(f"{label}: failed")
        for error in result.errors:
            print(f"- {error}")
        return 1

    print(f"{label}: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
