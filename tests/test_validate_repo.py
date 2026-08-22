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


def test_validator_detects_duplicate_skill_names(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from scripts import validate_repo

    real_index = json.loads((REPO_ROOT / "skills_index.json").read_text(encoding="utf-8"))
    duplicate_index = {"skills": [*real_index["skills"], real_index["skills"][0]]}
    monkeypatch.setattr(validate_repo, "ROOT", REPO_ROOT)
    monkeypatch.setattr(validate_repo, "load_json", lambda _path: duplicate_index)

    findings: list[str] = []
    validate_repo.validate_skills_index(findings)

    assert any("duplicate skill name" in finding for finding in findings)


def test_validator_rejects_non_string_skill_metadata(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from scripts import validate_repo

    invalid_index = json.loads(
        (REPO_ROOT / "skills_index.json").read_text(encoding="utf-8")
    )
    invalid_index["skills"][0]["purpose"] = ["not", "text"]
    monkeypatch.setattr(validate_repo, "ROOT", REPO_ROOT)
    monkeypatch.setattr(validate_repo, "load_json", lambda _path: invalid_index)

    findings: list[str] = []
    validate_repo.validate_skills_index(findings)

    assert any("purpose must be a non-empty string" in finding for finding in findings)


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


def test_validator_requires_prod_gate_in_pr_template(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    from scripts import validate_repo

    fake_root = tmp_path
    pr_template = fake_root / ".github" / "PULL_REQUEST_TEMPLATE.md"
    pr_template.parent.mkdir()
    pr_template.write_text("- [ ] `make validate` passes\n", encoding="utf-8")
    monkeypatch.setattr(validate_repo, "ROOT", fake_root)

    findings: list[str] = []
    validate_repo.validate_pr_template(findings)

    assert any("make prod-gate" in finding for finding in findings)


def test_validator_detects_runtime_adapter_version_drift(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    from scripts import validate_repo

    fake_root = tmp_path
    (fake_root / ".codex-plugin").mkdir()
    (fake_root / ".claude-plugin").mkdir()
    (fake_root / "pyproject.toml").write_text(
        '[project]\nname = "cognitive-deadlift"\nversion = "0.1.0"\n',
        encoding="utf-8",
    )
    (fake_root / ".codex-plugin" / "plugin.json").write_text(
        '{"name": "cognitive-deadlift", "version": "0.1.0", "description": "x", '
        '"skills": "./skills/", "interface": {"displayName": "Cognitive Deadlift", '
        '"shortDescription": "x", "longDescription": "x", "developerName": "x", '
        '"category": "Productivity", "capabilities": ["Read"], "defaultPrompt": ["x"]}}\n',
        encoding="utf-8",
    )
    (fake_root / ".claude-plugin" / "plugin.json").write_text(
        '{"name": "cognitive-deadlift", "version": "9.9.9", "description": "x", '
        '"skills": []}\n',
        encoding="utf-8",
    )
    (fake_root / "gemini-extension.json").write_text(
        '{"name": "cognitive-deadlift", "version": "0.1.0", "description": "x", '
        '"contextFileName": "GEMINI.md"}\n',
        encoding="utf-8",
    )
    monkeypatch.setattr(validate_repo, "ROOT", fake_root)

    findings: list[str] = []
    validate_repo.validate_runtime_adapter_metadata(findings)

    assert any(".claude-plugin/plugin.json version" in finding for finding in findings)


def test_validator_detects_runtime_context_skill_routing_drift(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    from scripts import validate_repo

    fake_root = tmp_path
    for skill in ("problem-framing", "runtime-adapter-smoke"):
        (fake_root / "skills" / skill).mkdir(parents=True)

    (fake_root / "AGENTS.md").write_text(
        "- `problem-framing` before implementation.\n",
        encoding="utf-8",
    )
    (fake_root / "CLAUDE.md").write_text(
        "- `problem-framing` before implementation.\n",
        encoding="utf-8",
    )
    (fake_root / "GEMINI.md").write_text(
        "- `skills/problem-framing/SKILL.md` before implementation.\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(validate_repo, "ROOT", fake_root)

    findings: list[str] = []
    validate_repo.validate_runtime_context_skill_routing(findings)

    assert any(
        "AGENTS.md" in finding and "runtime-adapter-smoke" in finding
        for finding in findings
    )
    assert any(
        "CLAUDE.md" in finding and "runtime-adapter-smoke" in finding
        for finding in findings
    )
    assert any(
        "GEMINI.md" in finding and "runtime-adapter-smoke" in finding
        for finding in findings
    )
