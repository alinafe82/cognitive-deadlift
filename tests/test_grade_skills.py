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
