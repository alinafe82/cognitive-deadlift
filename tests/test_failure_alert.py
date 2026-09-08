"""Execute the workflow's actual Bash body with an isolated GitHub CLI double."""
from __future__ import annotations

import json
import os
import subprocess
import sys
import textwrap
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize(
    ("conclusion", "existing", "expected"),
    [
        ("success", False, []),
        ("success", True, ["comment", "close"]),
        ("failure", False, ["create"]),
        ("failure", True, ["comment"]),
    ],
)
def test_alert_reconciles_json(tmp_path, conclusion, existing, expected):
    workflow = (ROOT / ".github/workflows/failure-alert.yml").read_text()
    script = textwrap.dedent(workflow.split("        run: |\n", 1)[1])
    cli = tmp_path / "gh"
    cli.write_text(
        f"#!{sys.executable}\n"
        + textwrap.dedent('''\
        import json, os, sys
        args = sys.argv[1:]
        if args[0] == "api":
            endpoint = next(a for a in args if a.startswith("repos/"))
            if endpoint.endswith("/runs"):
                print(json.dumps([{"workflow_runs": [{
                    "id": 123, "run_attempt": 1, "name": "CI",
                    "event": "push", "conclusion": os.environ["RESULT"],
                    "html_url": "https://example.test/run/123", "head_sha": "abc"
                }]}]))
            elif endpoint.endswith("/comments"):
                print("")
            elif endpoint.endswith("/issues"):
                issues = ([{"number": 7, "body": "<!-- ci-failure-alert:99 -->"}]
                          if os.environ["EXISTING"] == "1" else [])
                print(json.dumps([issues]))
            else:
                print("main")
        elif args[:2] == ["issue", "view"]:
            print("<!-- ci-failure-alert:99 -->")
        elif args[0] == "issue":
            with open(os.environ["CALLS"], "a") as stream:
                stream.write(json.dumps(args) + "\\n")
        elif args[:2] != ["label", "create"]:
            sys.exit("Unexpected call: " + repr(args))
        ''')
    )
    cli.chmod(0o755)
    calls = tmp_path / "calls.jsonl"
    result = subprocess.run(
        ["bash", "-c", script],
        env={
            **os.environ,
            "PATH": f"{tmp_path}:{os.environ['PATH']}",
            "REPOSITORY": "owner/repo",
            "REPOSITORY_OWNER": "owner",
            "REPOSITORY_OWNER_TYPE": "User",
            "WORKFLOW_ID": "99",
            "ALERT_LABEL": "ci-failure-alert",
            "RESULT": conclusion,
            "EXISTING": str(int(existing)),
            "CALLS": str(calls),
        },
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    recorded = (
        [json.loads(line) for line in calls.read_text().splitlines()] if calls.exists() else []
    )
    assert [args[1] for args in recorded] == expected
    if conclusion == "failure":
        assert "<!-- ci-failure-alert:99:123:1 -->" in recorded[0][recorded[0].index("--body") + 1]
