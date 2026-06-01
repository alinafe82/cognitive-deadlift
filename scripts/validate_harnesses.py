#!/usr/bin/env python3
"""Validate harness fixture contract files."""

from __future__ import annotations

from pathlib import Path

try:
    from contract_yaml import read_contract_yaml
except ImportError:  # pragma: no cover - exercised when imported as a package in tests.
    from scripts.contract_yaml import read_contract_yaml

ROOT = Path(__file__).resolve().parents[1]
HARNESSES_DIR = ROOT / "harnesses"

REQUIRED_HARNESSES = [
    "ambiguous-request",
    "fake-test-pass",
    "overeager-refactor",
    "unsafe-tool-use",
]
REQUIRED_FILES = ["task.md", "expected-behavior.md", "rubric.yaml"]
REQUIRED_RUBRIC_FIELDS = ["name", "focus", "required_checks", "failure_modes", "pass_conditions"]


def validate_harness(path: Path) -> list[str]:
    findings: list[str] = []
    for filename in REQUIRED_FILES:
        file_path = path / filename
        relative = file_path.relative_to(ROOT)
        if not file_path.exists():
            findings.append(f"missing harness file: {relative}")
            continue
        if not file_path.read_text(encoding="utf-8").strip():
            findings.append(f"harness file is empty: {relative}")

    rubric_path = path / "rubric.yaml"
    if not rubric_path.exists():
        return findings

    rubric = read_contract_yaml(rubric_path)
    relative = rubric_path.relative_to(ROOT)
    if rubric.get("name") != path.name:
        findings.append(f"{relative} name must match directory")
    for field in REQUIRED_RUBRIC_FIELDS:
        if field not in rubric:
            findings.append(f"{relative} missing field: {field}")
            continue
        value = rubric[field]
        if field in {"name", "focus"} and not str(value).strip():
            findings.append(f"{relative} {field} is empty")
        if field not in {"name", "focus"} and (not isinstance(value, list) or not value):
            findings.append(f"{relative} {field} must be a non-empty list")

    return findings


def validate_harnesses(root: Path = ROOT) -> list[str]:
    findings: list[str] = []
    harnesses_dir = root / "harnesses"
    if not (harnesses_dir / "README.md").exists():
        findings.append("harnesses/README.md is missing")
    for harness in REQUIRED_HARNESSES:
        path = harnesses_dir / harness
        if not path.is_dir():
            findings.append(f"missing harness directory: harnesses/{harness}")
            continue
        findings.extend(validate_harness(path))
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
