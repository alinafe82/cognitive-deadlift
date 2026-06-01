"""Tests for the repo contract validator.

These tests run the real validator against the real repo to lock in:
- the contract checks all pass on the live tree
- each individual check returns nonzero when its invariant is broken
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "scripts" / "validate_repo.py"


def run_validator(cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=cwd,
        text=True,
        capture_output=True,
        check=False,
    )


def test_validator_passes_on_real_repo() -> None:
    result = run_validator(REPO_ROOT)
    assert result.returncode == 0, result.stderr


def test_validator_detects_skills_index_drift(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """If skills_index.json claims a skill that's not on disk, validate_repo must fail."""
    from scripts import validate_repo

    monkeypatch.setattr(validate_repo, "ROOT", REPO_ROOT)
    # Build an index with a phantom skill on top of the real ones.
    real_index = json.loads((REPO_ROOT / "skills_index.json").read_text(encoding="utf-8"))
    real_index["skills"].append(
        {
            "name": "ghost-skill",
            "path": "skills/ghost-skill/SKILL.md",
            "purpose": "Should not exist.",
        }
    )
    bad_index = tmp_path / "skills_index.json"
    bad_index.write_text(json.dumps(real_index), encoding="utf-8")

    # Patch the index path resolution by overriding load_json for this test.
    findings: list[str] = []
    original_load = validate_repo.load_json

    def fake_load(path: Path) -> dict:
        if path.name == "skills_index.json":
            return real_index
        return original_load(path)

    monkeypatch.setattr(validate_repo, "load_json", fake_load)
    validate_repo.validate_skills_index(findings)
    assert any("ghost-skill" in f for f in findings)


def test_validator_detects_missing_doc_section(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """If a required doc section is missing, validate_repo must report it."""
    from scripts import validate_repo

    fake_root = tmp_path
    (fake_root / "CONTEXT.md").write_text("# CONTEXT\n\n## Mission\n\nText.\n", encoding="utf-8")
    monkeypatch.setattr(validate_repo, "ROOT", fake_root)

    findings: list[str] = []
    validate_repo.validate_doc_contract(findings)
    # CONTEXT.md is missing five of the six required sections, plus other docs.
    assert any("Operating principles" in f for f in findings)
    assert any("Anti-slop rules" in f for f in findings)


def test_validator_detects_tracked_artifact(monkeypatch: pytest.MonkeyPatch) -> None:
    """If git ls-files reports a forbidden artifact, validate_repo must flag it."""
    from scripts import validate_repo

    monkeypatch.setattr(
        validate_repo,
        "git_tracked_files",
        lambda: ["scripts/__pycache__/foo.pyc", "src/main.py"],
    )
    findings: list[str] = []
    validate_repo.validate_generated_artifacts(findings)
    assert any("__pycache__" in f for f in findings)
    assert not any("main.py" in f for f in findings)
