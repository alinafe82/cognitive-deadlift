from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from scripts import doctor, validate_context_packs, validate_harnesses, validate_policies
from scripts.contract_yaml import read_contract_yaml

REPO_ROOT = Path(__file__).resolve().parents[1]


def test_contract_yaml_reads_top_level_and_nested_lists() -> None:
    data = read_contract_yaml(REPO_ROOT / "policies" / "thinking-budget.yaml")

    assert data["low"]["required"] == ["summarize-intent", "run-basic-check"]
    assert "human-approval" in data["high"]["required"]


def test_thinking_budget_policy_passes() -> None:
    assert validate_policies.validate_thinking_budget() == []


def write_context_pack(path: Path, *, omit: str | None = None) -> None:
    fields = {
        "purpose": "Exercise the context pack validator.",
        "required_evidence": ["current behavior"],
        "optional_evidence": ["related docs"],
        "forbidden_context": ["secrets"],
        "freshness_rules": ["use current files"],
        "output_contract": ["summarize evidence"],
        "recommended_skills": ["problem-framing"],
    }
    if omit:
        fields.pop(omit)

    lines: list[str] = []
    for key, value in fields.items():
        if isinstance(value, list):
            lines.append(f"{key}:")
            lines.extend(f"  - {item}" for item in value)
        else:
            lines.append(f"{key}: {value}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_harness(path: Path, *, omit_rubric_field: str | None = None) -> None:
    path.mkdir(parents=True)
    (path / "task.md").write_text("# Task\n\nReview the change.\n", encoding="utf-8")
    (path / "expected-behavior.md").write_text(
        "# Expected Behavior\n\nRequire evidence before approval.\n",
        encoding="utf-8",
    )
    fields = {
        "name": path.name,
        "focus": "Evidence quality.",
        "required_checks": ["problem framed"],
        "failure_modes": ["unsupported confidence"],
        "pass_conditions": ["missing evidence is rejected"],
    }
    if omit_rubric_field:
        fields.pop(omit_rubric_field)

    lines: list[str] = []
    for key, value in fields.items():
        if isinstance(value, list):
            lines.append(f"{key}:")
            lines.extend(f"  - {item}" for item in value)
        else:
            lines.append(f"{key}: {value}")
    (path / "rubric.yaml").write_text("\n".join(lines) + "\n", encoding="utf-8")


def test_thinking_budget_policy_reports_missing_field(tmp_path: Path) -> None:
    policy = tmp_path / "thinking-budget.yaml"
    policy.write_text(
        """
low:
  description: Low risk.
  required:
    - summarize-intent
  examples:
    - typo fixes
medium:
  description: Medium risk.
  required:
    - trace-the-code
  examples:
    - bug fix
high:
  description: High risk.
  required:
    - rollback-plan
    - human-approval
""".strip()
        + "\n",
        encoding="utf-8",
    )

    findings = validate_policies.validate_thinking_budget(policy)

    assert "high missing field: examples" in findings


def test_context_packs_pass() -> None:
    assert validate_context_packs.validate_context_packs() == []


def test_context_pack_validator_reports_missing_field_with_custom_root(tmp_path: Path) -> None:
    packs_dir = tmp_path / "context-packs"
    packs_dir.mkdir()
    (packs_dir / "README.md").write_text("# Context Packs\n", encoding="utf-8")
    (tmp_path / "skills_index.json").write_text(
        '{"skills": [{"name": "problem-framing"}]}\n',
        encoding="utf-8",
    )
    for pack in validate_context_packs.REQUIRED_PACKS:
        write_context_pack(
            packs_dir / f"{pack}.yaml",
            omit="output_contract" if pack == "bugfix" else None,
        )

    findings = validate_context_packs.validate_context_packs(tmp_path)

    assert "context-packs/bugfix.yaml missing field: output_contract" in findings


def test_harnesses_pass() -> None:
    assert validate_harnesses.validate_harnesses() == []


def test_harness_validator_reports_missing_rubric_field_with_custom_root(tmp_path: Path) -> None:
    harnesses_dir = tmp_path / "harnesses"
    harnesses_dir.mkdir()
    (harnesses_dir / "README.md").write_text("# Harnesses\n", encoding="utf-8")
    for harness in validate_harnesses.REQUIRED_HARNESSES:
        write_harness(
            harnesses_dir / harness,
            omit_rubric_field="pass_conditions" if harness == "fake-test-pass" else None,
        )

    findings = validate_harnesses.validate_harnesses(tmp_path)

    assert "harnesses/fake-test-pass/rubric.yaml missing field: pass_conditions" in findings


def test_doctor_readiness_passes() -> None:
    rows = doctor.readiness()

    assert all(row["ok"] for row in rows)


def test_doctor_readiness_reports_missing_contract_artifacts(tmp_path: Path) -> None:
    rows = doctor.readiness(tmp_path)

    assert not all(row["ok"] for row in rows)
    assert any(row["name"] == "README" and not row["ok"] for row in rows)


def test_doctor_json_command_passes() -> None:
    result = subprocess.run(
        [sys.executable, "scripts/doctor.py", "--json"],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0, result.stdout + result.stderr
    assert '"ok": true' in result.stdout
