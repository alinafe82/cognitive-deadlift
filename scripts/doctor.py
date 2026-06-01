#!/usr/bin/env python3
"""Report whether the repo has the contract files needed for AI-assisted work."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CHECKS = [
    ("README", "README.md"),
    ("AGENTS", "AGENTS.md"),
    ("skills index", "skills_index.json"),
    ("skills directory", "skills"),
    ("tests directory", "tests"),
    ("Makefile", "Makefile"),
    ("CI workflow", ".github/workflows/ci.yml"),
    ("harnesses", "harnesses"),
    ("context packs", "context-packs"),
    ("thinking budget", "policies/thinking-budget.yaml"),
    ("skill atrophy taxonomy", "docs/skill-atrophy-taxonomy.md"),
    ("AI slop taxonomy", "docs/ai-slop-taxonomy.md"),
    ("harness validator", "scripts/validate_harnesses.py"),
    ("context pack validator", "scripts/validate_context_packs.py"),
    ("policy validator", "scripts/validate_policies.py"),
]


def readiness(root: Path = ROOT) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for label, relative in CHECKS:
        path = root / relative
        ok = path.exists()
        rows.append({"name": label, "path": relative, "ok": ok})
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true", help="Print JSON instead of text.")
    args = parser.parse_args()

    rows = readiness()
    ok = all(bool(row["ok"]) for row in rows)

    if args.json:
        print(json.dumps({"ok": ok, "checks": rows}, indent=2))
    else:
        print("Cognitive Deadlift doctor")
        print(f"Overall: {'ready' if ok else 'not ready'}")
        for row in rows:
            status = "ok" if row["ok"] else "missing"
            print(f"- {status}: {row['name']} ({row['path']})")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
