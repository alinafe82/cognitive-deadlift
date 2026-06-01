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


def test_context_packs_pass() -> None:
    assert validate_context_packs.validate_context_packs() == []


def test_harnesses_pass() -> None:
    assert validate_harnesses.validate_harnesses() == []


def test_doctor_readiness_passes() -> None:
    rows = doctor.readiness()

    assert all(row["ok"] for row in rows)


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
