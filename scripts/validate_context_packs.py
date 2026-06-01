#!/usr/bin/env python3
"""Validate context pack contract files."""

from __future__ import annotations

import json
from pathlib import Path

try:
    from contract_yaml import read_contract_yaml
except ImportError:  # pragma: no cover - exercised when imported as a package in tests.
    from scripts.contract_yaml import read_contract_yaml

ROOT = Path(__file__).resolve().parents[1]
PACKS_DIR = ROOT / "context-packs"
SKILLS_INDEX = ROOT / "skills_index.json"

REQUIRED_PACKS = ["bugfix", "refactor", "repo-review", "risky-change"]
REQUIRED_FIELDS = [
    "purpose",
    "required_evidence",
    "optional_evidence",
    "forbidden_context",
    "freshness_rules",
    "output_contract",
    "recommended_skills",
]


def known_skills() -> set[str]:
    data = json.loads(SKILLS_INDEX.read_text(encoding="utf-8"))
    return {entry["name"] for entry in data.get("skills", [])}


def validate_pack(path: Path, skills: set[str]) -> list[str]:
    findings: list[str] = []
    data = read_contract_yaml(path)
    relative = path.relative_to(ROOT)

    for field in REQUIRED_FIELDS:
        if field not in data:
            findings.append(f"{relative} missing field: {field}")
            continue
        value = data[field]
        if field == "purpose" and not str(value).strip():
            findings.append(f"{relative} purpose is empty")
        if field != "purpose" and (not isinstance(value, list) or not value):
            findings.append(f"{relative} {field} must be a non-empty list")

    recommended = data.get("recommended_skills", [])
    if isinstance(recommended, list):
        unknown = sorted(set(recommended) - skills)
        if unknown:
            findings.append(f"{relative} recommends unknown skills: {unknown}")

    return findings


def validate_context_packs(root: Path = ROOT) -> list[str]:
    findings: list[str] = []
    packs_dir = root / "context-packs"
    if not (packs_dir / "README.md").exists():
        findings.append("context-packs/README.md is missing")

    skills = known_skills()
    for pack in REQUIRED_PACKS:
        path = packs_dir / f"{pack}.yaml"
        if not path.exists():
            findings.append(f"missing context pack: context-packs/{pack}.yaml")
            continue
        findings.extend(validate_pack(path, skills))

    return findings


def main() -> int:
    findings = validate_context_packs()
    if findings:
        print("validate_context_packs: failed")
        for finding in findings:
            print(f"- {finding}")
        return 1
    print("validate_context_packs: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
