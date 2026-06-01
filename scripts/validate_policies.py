#!/usr/bin/env python3
"""Validate policy contract files."""

from __future__ import annotations

from pathlib import Path

try:
    from contract_yaml import read_contract_yaml
except ImportError:  # pragma: no cover - exercised when imported as a package in tests.
    from scripts.contract_yaml import read_contract_yaml

ROOT = Path(__file__).resolve().parents[1]
POLICY = ROOT / "policies" / "thinking-budget.yaml"

REQUIRED_LEVELS = ["low", "medium", "high"]
REQUIRED_FIELDS = ["description", "required", "examples"]


def validate_thinking_budget(path: Path = POLICY) -> list[str]:
    findings: list[str] = []
    if not path.exists():
        return [f"missing policy: {path.relative_to(ROOT)}"]

    data = read_contract_yaml(path)
    for level in REQUIRED_LEVELS:
        value = data.get(level)
        if not isinstance(value, dict):
            findings.append(f"thinking budget missing level: {level}")
            continue
        for field in REQUIRED_FIELDS:
            if field not in value:
                findings.append(f"{level} missing field: {field}")
        if not value.get("description"):
            findings.append(f"{level} description is empty")
        for list_field in ("required", "examples"):
            if not isinstance(value.get(list_field), list) or not value[list_field]:
                findings.append(f"{level} {list_field} must be a non-empty list")

    high = data.get("high", {})
    if isinstance(high, dict):
        required = high.get("required", [])
        if isinstance(required, list):
            for item in ("human-approval", "rollback-plan"):
                if item not in required:
                    findings.append(f"high required list must include {item}")

    return findings


def main() -> int:
    findings = validate_thinking_budget()
    if findings:
        print("validate_policies: failed")
        for finding in findings:
            print(f"- {finding}")
        return 1
    print("validate_policies: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
