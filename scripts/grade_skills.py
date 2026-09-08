#!/usr/bin/env python3
"""Grade Cognitive Deadlift skills against a compact skill-quality rubric."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
try:
    from validate_skills import (
        missing_contract_sections,
        validate_routing_cases,
        validate_skill,
    )
    from validate_skills import (
        parse_frontmatter as read_frontmatter,
    )
except ImportError:
    from scripts.validate_skills import (
        missing_contract_sections,
        validate_routing_cases,
        validate_skill,
    )
    from scripts.validate_skills import (
        parse_frontmatter as read_frontmatter,
    )


@dataclass(frozen=True)
class AxisGrade:
    axis: str
    score: int
    finding: str

    @property
    def letter(self) -> str:
        return letter_grade(self.score)


@dataclass(frozen=True)
class SkillGrade:
    name: str
    score: float
    axes: list[AxisGrade]

    @property
    def letter(self) -> str:
        return letter_grade(round(self.score))


def letter_grade(score: int | float) -> str:
    score = round(score)
    if score >= 97:
        return "A+"
    if score >= 93:
        return "A"
    if score >= 90:
        return "A-"
    if score >= 87:
        return "B+"
    if score >= 83:
        return "B"
    if score >= 80:
        return "B-"
    if score >= 77:
        return "C+"
    if score >= 73:
        return "C"
    if score >= 70:
        return "C-"
    if score >= 67:
        return "D+"
    if score >= 63:
        return "D"
    if score >= 60:
        return "D-"
    return "F"


def skill_files() -> list[Path]:
    return sorted(SKILLS.glob("*/SKILL.md"))


def grade_skill(path: Path) -> SkillGrade:
    """Score static packaging checks; this is not a model-quality measurement."""
    text = path.read_text(encoding="utf-8")
    metadata, metadata_errors = read_frontmatter(text)
    description = metadata.get("description", "")
    contract_errors = missing_contract_sections(text)
    errors = validate_skill(path.parent, path.parent.parent.parent)
    routing_errors = validate_routing_cases(path.parent / "tests" / "routing.json")
    checks = [
        (
            "Metadata",
            not metadata_errors
            and metadata.get("name") == path.parent.name
            and bool(description.strip())
            and len(description) <= 240,
            "Named skill with a concise description (at most 240 characters).",
        ),
        (
            "Evidence contract",
            not contract_errors,
            "Scope, workflow, evidence and action/data boundaries contain guidance.",
        ),
        (
            "Package integrity",
            not errors,
            "Metadata, examples, local links and content checks pass.",
        ),
        (
            "Routing review cases",
            not routing_errors,
            "Distinct positive and negative requests with reasons are present.",
        ),
        (
            "Context cost",
            len(text.split()) <= 450,
            "Root stays within the 450-word review budget; details can load on demand.",
        ),
    ]
    axes = [
        AxisGrade(name, 100 if passed else 0, detail if passed else "Missing contract: " + detail)
        for name, passed, detail in checks
    ]
    return SkillGrade(
        metadata.get("name", path.parent.name), sum(axis.score for axis in axes) / len(axes), axes
    )


def render_report(grades: list[SkillGrade]) -> str:
    lines = [
        "# Skill Contract Report",
        "",
        "Static packaging checks only; scores do not measure agent performance.",
        "",
        "| Skill | Overall | Score | Lowest Axis | Finding |",
        "| --- | --- | ---: | --- | --- |",
    ]

    for grade in grades:
        lowest = min(grade.axes, key=lambda axis: axis.score)
        lines.append(
            f"| `{grade.name}` | {grade.letter} | {grade.score:.1f} | "
            f"{lowest.axis} ({lowest.letter}) | {lowest.finding} |"
        )

    lines.extend(["", "## Detailed Axis Scores", ""])
    for grade in grades:
        lines.extend(
            [
                f"### {grade.name}",
                "",
                "| Axis | Grade | Score | Finding |",
                "| --- | --- | ---: | --- |",
            ]
        )
        for axis in grade.axes:
            lines.append(f"| {axis.axis} | {axis.letter} | {axis.score} | {axis.finding} |")
        lines.append("")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--min-score", type=float, default=90.0)
    parser.add_argument("--skill", action="append", default=[], help="Grade only this skill")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    args = parser.parse_args()

    paths = skill_files()
    if args.skill:
        requested = set(args.skill)
        paths = [path for path in paths if path.parent.name in requested]
        missing = sorted(requested - {path.parent.name for path in paths})
        if missing:
            parser.error(f"unknown skill(s): {', '.join(missing)}")

    grades = [grade_skill(path) for path in paths]
    if args.json:
        print(
            json.dumps(
                [
                    {
                        "name": grade.name,
                        "score": round(grade.score, 1),
                        "letter": grade.letter,
                        "axes": [
                            {
                                "axis": axis.axis,
                                "score": axis.score,
                                "letter": axis.letter,
                                "finding": axis.finding,
                            }
                            for axis in grade.axes
                        ],
                    }
                    for grade in grades
                ],
                indent=2,
            )
        )
    else:
        print(render_report(grades))

    failures = [grade for grade in grades if grade.score < args.min_score]
    if failures:
        names = ", ".join(f"{grade.name} ({grade.score:.1f})" for grade in failures)
        print(f"\nSkills below minimum score {args.min_score:.1f}: {names}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
