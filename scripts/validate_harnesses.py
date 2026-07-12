#!/usr/bin/env python3
"""Validate harness fixture contract files."""

from __future__ import annotations

from pathlib import Path

try:
    from contract_yaml import read_contract_yaml
except ImportError:  # pragma: no cover - exercised when imported as a package in tests.
    from scripts.contract_yaml import read_contract_yaml

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_HARNESSES = [
    "all-skills-request",
    "ambiguous-request",
    "fake-test-pass",
    "overeager-refactor",
    "unsafe-tool-use",
]
REQUIRED_FILES = ["task.md", "expected-behavior.md", "rubric.yaml"]
REQUIRED_RUBRIC_FIELDS = ["name", "focus", "required_checks", "failure_modes", "pass_conditions"]


def relative(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def validate_harness(path: Path, root: Path = ROOT) -> list[str]:
    findings: list[str] = []
    for filename in REQUIRED_FILES:
        file_path = path / filename
        file_path_label = relative(file_path, root)
        if not file_path.exists():
            findings.append(f"missing harness file: {file_path_label}")
            continue
        if not file_path.read_text(encoding="utf-8").strip():
            findings.append(f"harness file is empty: {file_path_label}")

    rubric_path = path / "rubric.yaml"
    if not rubric_path.exists():
        return findings

    rubric = read_contract_yaml(rubric_path)
    rubric_label = relative(rubric_path, root)
    if rubric.get("name") != path.name:
        findings.append(f"{rubric_label} name must match directory")
    for field in REQUIRED_RUBRIC_FIELDS:
        if field not in rubric:
            findings.append(f"{rubric_label} missing field: {field}")
            continue
        value = rubric[field]
        if field in {"name", "focus"} and not str(value).strip():
            findings.append(f"{rubric_label} {field} is empty")
        if field not in {"name", "focus"} and (not isinstance(value, list) or not value):
            findings.append(f"{rubric_label} {field} must be a non-empty list")

    return findings


def validate_harnesses(root: Path = ROOT) -> list[str]:
    root = root.resolve()
    findings: list[str] = []
    harnesses_dir = root / "harnesses"
    if not (harnesses_dir / "README.md").exists():
        findings.append("harnesses/README.md is missing")
    for harness in REQUIRED_HARNESSES:
        path = harnesses_dir / harness
        if not path.is_dir():
            findings.append(f"missing harness directory: harnesses/{harness}")
            continue
        findings.extend(validate_harness(path, root))
    return findings


def main() -> int:
    findings = validate_harnesses()
    if findings:
        print("validate_harnesses: failed")
        for finding in findings:
            print(f"- {finding}")
        return 1
    print("validate_harnesses: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
