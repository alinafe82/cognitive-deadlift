import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_grader_can_emit_json_for_one_skill():
    result = subprocess.run(
        [sys.executable, "scripts/grade_skills.py", "--skill", "problem-framing", "--json"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )

    payload = json.loads(result.stdout)
    assert [item["name"] for item in payload] == ["problem-framing"]
    assert payload[0]["axes"]


def test_current_skill_set_meets_100_point_gate():
    result = subprocess.run(
        [sys.executable, "scripts/grade_skills.py", "--min-score", "100", "--json"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )

    payload = json.loads(result.stdout)
    assert result.returncode == 0, result.stderr
    assert {item["score"] for item in payload} == {100.0}


def test_grader_rejects_unknown_skill():
    result = subprocess.run(
        [sys.executable, "scripts/grade_skills.py", "--skill", "not-a-real-skill"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 2
    assert "unknown skill(s): not-a-real-skill" in result.stderr


def test_thin_skill_does_not_receive_100(tmp_path):
    from scripts.grade_skills import grade_skill

    skill_dir = tmp_path / "thin-skill"
    (skill_dir / "examples").mkdir(parents=True)
    (skill_dir / "examples" / "simple.md").write_text("Simple example\n", encoding="utf-8")
    (skill_dir / "examples" / "edge-case.md").write_text("Edge example\n", encoding="utf-8")
    skill_path = skill_dir / "SKILL.md"
    skill_path.write_text(
        """---
name: thin-skill
description: Use when checking a deliberately thin skill. NOT for production use.
---

## Purpose
Thin fixture.

## When To Use
- Use it for tests.

## When Not To Use
- Do not use it for real work.

## Inputs Expected
- Input.

## Output Expected
Result.
""",
        encoding="utf-8",
    )

    grade = grade_skill(skill_path)

    assert grade.score < 100
