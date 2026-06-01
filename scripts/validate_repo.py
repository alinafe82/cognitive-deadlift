#!/usr/bin/env python3
"""Validate the Cognitive Deadlift repo contract.

Checks:
- required files exist
- runtime adapter manifests are consistent
- skills_index.json matches the skills/ directory
- top-level docs each own their declared job (doc contract)
- generated artifacts stay untracked
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_ROOT_FILES = [
    "README.md",
    "LICENSE",
    "CONTEXT.md",
    "ARCHITECTURE.md",
    "CATALOG.md",
    "AGENTS.md",
    "CLAUDE.md",
    "GEMINI.md",
    "Makefile",
    "pyproject.toml",
    "skills_index.json",
    "repo-audit.md",
    "productionization-report.md",
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
    "scripts/validate_policies.py",
    "scripts/validate_harnesses.py",
    "scripts/validate_context_packs.py",
    "scripts/doctor.py",
    "docs/architecture.md",
    "docs/skill-standard.md",
    "docs/review-checklist.md",
    "docs/skill-atrophy-taxonomy.md",
    "docs/ai-slop-taxonomy.md",
    "docs/roadmap.md",
    "policies/thinking-budget.yaml",
    "harnesses/README.md",
    "context-packs/README.md",
]

# Each entry: (file, list of required section headings).
# Headings are matched against `## <heading>` markers.
DOC_CONTRACT: list[tuple[str, list[str]]] = [
    (
        "CONTEXT.md",
        [
            "Mission",
            "Operating principles",
            "Anti-slop rules",
            "Validation philosophy",
            "Current assumptions",
            "What agents must read before editing",
        ],
    ),
    (
        "ARCHITECTURE.md",
        [
            "Top-level layout",
            "Skill lifecycle",
            "Hook lifecycle",
            "Policy lifecycle",
            "Context pack lifecycle",
            "Review harness lifecycle",
            "Validation lifecycle",
        ],
    ),
    (
        "CATALOG.md",
        ["Skills", "Hooks", "Scripts", "Runtime adapters"],
    ),
    (
        "AGENTS.md",
        ["Repo contract", "Engineering style", "Final response format"],
    ),
    (
        "repo-audit.md",
        ["Source-of-truth contract", "Findings"],
    ),
    (
        "productionization-report.md",
        ["Summary", "Checks available", "Commands run", "Remaining risks"],
    ),
]

# Glob patterns for generated artifacts that must not be tracked.
FORBIDDEN_TRACKED_PATTERNS: list[re.Pattern[str]] = [
    re.compile(r"(^|/)\.pytest_cache(/|$)"),
    re.compile(r"(^|/)\.ruff_cache(/|$)"),
    re.compile(r"(^|/)\.mypy_cache(/|$)"),
    re.compile(r"(^|/)__pycache__(/|$)"),
    re.compile(r"\.egg-info(/|$)"),
    re.compile(r"(^|/)dist(/|$)"),
    re.compile(r"(^|/)build(/|$)"),
    re.compile(r"(^|/)htmlcov(/|$)"),
    re.compile(r"(^|/)\.venv(/|$)"),
    re.compile(r"(^|/)node_modules(/|$)"),
]


def fail(message: str, findings: list[str]) -> None:
    findings.append(message)


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def skill_dirs() -> list[Path]:
    return sorted(path for path in (ROOT / "skills").iterdir() if path.is_dir())


def validate_required_files(findings: list[str]) -> None:
    for relative in REQUIRED_ROOT_FILES:
        if not (ROOT / relative).exists():
            fail(f"missing required file: {relative}", findings)


def validate_skill_dirs(findings: list[str]) -> None:
    dirs = skill_dirs()
    if not dirs:
        fail("skills/ has no skills", findings)
        return

    for directory in dirs:
        skill_file = directory / "SKILL.md"
        if not skill_file.exists():
            fail(f"missing SKILL.md in {directory.relative_to(ROOT)}", findings)
            continue
        text = skill_file.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            fail(f"missing YAML frontmatter in {skill_file.relative_to(ROOT)}", findings)
            continue
        try:
            frontmatter = text.split("---", 2)[1]
        except IndexError:
            fail(f"unterminated frontmatter in {skill_file.relative_to(ROOT)}", findings)
            continue
        if "name:" not in frontmatter:
            fail(f"missing frontmatter name in {skill_file.relative_to(ROOT)}", findings)
        if "description:" not in frontmatter:
            fail(f"missing frontmatter description in {skill_file.relative_to(ROOT)}", findings)


def validate_claude_manifest(findings: list[str]) -> None:
    manifest = load_json(ROOT / ".claude-plugin" / "plugin.json")
    listed = sorted(Path(item).as_posix().removeprefix("./") for item in manifest.get("skills", []))
    actual = sorted(path.relative_to(ROOT).as_posix() for path in skill_dirs())
    if listed != actual:
        fail(".claude-plugin/plugin.json skills list does not match skills/", findings)


def validate_codex_manifest(findings: list[str]) -> None:
    manifest = load_json(ROOT / ".codex-plugin" / "plugin.json")
    if manifest.get("skills") != "./skills/":
        fail(".codex-plugin/plugin.json must point skills to ./skills/", findings)


def validate_gemini_manifest(findings: list[str]) -> None:
    manifest = load_json(ROOT / "gemini-extension.json")
    if manifest.get("contextFileName") != "GEMINI.md":
        fail("gemini-extension.json must use GEMINI.md as contextFileName", findings)


def validate_skills_index(findings: list[str]) -> None:
    index_path = ROOT / "skills_index.json"
    index = load_json(index_path)
    entries = index.get("skills")
    if not isinstance(entries, list):
        fail("skills_index.json: missing or non-list 'skills' field", findings)
        return

    indexed_names: list[str] = []
    for i, entry in enumerate(entries):
        if not isinstance(entry, dict):
            fail(f"skills_index.json: entry {i} is not an object", findings)
            continue
        for field in ("name", "path", "purpose"):
            if not entry.get(field):
                fail(f"skills_index.json: entry {i} missing '{field}'", findings)
        name = entry.get("name", "")
        path = entry.get("path", "")
        indexed_names.append(name)
        if name and path:
            expected_path = f"skills/{name}/SKILL.md"
            if path != expected_path:
                fail(
                    f"skills_index.json: entry '{name}' path is {path!r}, "
                    f"expected {expected_path!r}",
                    findings,
                )
            if not (ROOT / path).exists():
                fail(f"skills_index.json: entry '{name}' path does not exist on disk", findings)

    on_disk = sorted(path.name for path in skill_dirs())
    indexed_sorted = sorted(indexed_names)
    if indexed_sorted != on_disk:
        missing = sorted(set(on_disk) - set(indexed_sorted))
        extra = sorted(set(indexed_sorted) - set(on_disk))
        if missing:
            fail(f"skills_index.json: missing entries for {missing}", findings)
        if extra:
            fail(f"skills_index.json: lists skills not on disk: {extra}", findings)


def validate_doc_contract(findings: list[str]) -> None:
    for relative, headings in DOC_CONTRACT:
        path = ROOT / relative
        if not path.exists():
            fail(f"doc contract: {relative} missing", findings)
            continue
        text = path.read_text(encoding="utf-8")
        for heading in headings:
            marker = f"\n## {heading}\n"
            if marker not in text and not text.startswith(f"## {heading}\n"):
                fail(f"doc contract: {relative} missing '## {heading}' section", findings)


def git_tracked_files() -> list[str]:
    result = subprocess.run(
        ["git", "ls-files"],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )
    return [line for line in result.stdout.splitlines() if line.strip()]


def validate_generated_artifacts(findings: list[str]) -> None:
    try:
        tracked = git_tracked_files()
    except (subprocess.CalledProcessError, FileNotFoundError):
        fail("generated artifacts: git ls-files failed; cannot check tracking", findings)
        return

    for path in tracked:
        for pattern in FORBIDDEN_TRACKED_PATTERNS:
            if pattern.search(path):
                fail(f"generated artifact is tracked: {path}", findings)
                break


def main() -> int:
    findings: list[str] = []

    validate_required_files(findings)
    validate_skill_dirs(findings)
    validate_claude_manifest(findings)
    validate_codex_manifest(findings)
    validate_gemini_manifest(findings)
    validate_skills_index(findings)
    validate_doc_contract(findings)
    validate_generated_artifacts(findings)

    if findings:
        print("validate_repo: failed", file=sys.stderr)
        for finding in findings:
            print(f"- {finding}", file=sys.stderr)
        return 1

    print("validate_repo: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
