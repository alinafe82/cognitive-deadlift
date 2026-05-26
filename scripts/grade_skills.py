#!/usr/bin/env python3
"""Grade Cognitive Deadlift skills against a compact skill-quality rubric."""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
REQUIRED_SECTIONS = [
    "Purpose",
    "When To Use",
    "When Not To Use",
    "Inputs Expected",
    "Output Expected",
    "Process",
    "Quality Bar",
    "Examples",
    "Failure Modes",
    "Safety And Privacy",
    "Anti-Slop Rules",
]


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


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    try:
        frontmatter = text.split("---", 2)[1]
    except IndexError:
        return {}

    result: dict[str, str] = {}
    for line in frontmatter.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip('"').strip("'")
    return result


def has_heading(text: str, heading: str) -> bool:
    return f"\n## {heading}\n" in text


def section_text(text: str, heading: str) -> str:
    section_start = text.find(f"\n## {heading}\n")
    if section_start == -1:
        return ""
    next_heading = text.find("\n## ", section_start + 1)
    return text[section_start: next_heading if next_heading != -1 else len(text)]


def bullet_count(section: str) -> int:
    return sum(1 for line in section.splitlines() if line.startswith("- "))


def numbered_step_count(section: str) -> int:
    count = 0
    for line in section.splitlines():
        prefix, separator, _ = line.lstrip().partition(". ")
        if separator and prefix.isdigit():
            count += 1
    return count


def grade_description(frontmatter: dict[str, str]) -> AxisGrade:
    description = frontmatter.get("description", "")
    words = description.split()
    has_use = "Use when" in description
    has_not = "NOT for" in description
    has_name = bool(frontmatter.get("name"))

    if has_name and has_use and has_not and 25 <= len(words) <= 70:
        return AxisGrade(
            "Description Quality",
            95,
            "Specific trigger, exclusions, and compact length.",
        )
    if has_name and has_use and has_not:
        return AxisGrade(
            "Description Quality",
            88,
            "Good trigger and exclusions; length could be tighter.",
        )
    if description:
        return AxisGrade(
            "Description Quality",
            74,
            "Description exists but lacks trigger or exclusion precision.",
        )
    return AxisGrade("Description Quality", 0, "Description is missing.")


def grade_scope(text: str) -> AxisGrade:
    has_negative_boundary = has_heading(text, "Do Not Use For") or has_heading(
        text,
        "When Not To Use",
    )
    if has_heading(text, "When To Use") and has_negative_boundary:
        return AxisGrade("Scope Discipline", 95, "Explicit use and non-use boundaries.")
    if has_heading(text, "When To Use") or has_negative_boundary:
        return AxisGrade("Scope Discipline", 82, "Only one scope boundary section is present.")
    return AxisGrade("Scope Discipline", 60, "No explicit scope boundaries.")


def grade_progressive(text: str) -> AxisGrade:
    lines = len(text.splitlines())
    if lines <= 160:
        return AxisGrade("Progressive Disclosure", 94, f"Compact SKILL.md ({lines} lines).")
    if lines <= 300:
        return AxisGrade("Progressive Disclosure", 88, f"Readable SKILL.md ({lines} lines).")
    if lines <= 500:
        return AxisGrade("Progressive Disclosure", 76, f"Long SKILL.md ({lines} lines).")
    return AxisGrade(
        "Progressive Disclosure",
        60,
        f"Too long for a primary skill file ({lines} lines).",
    )


def grade_activation(frontmatter: dict[str, str], text: str) -> AxisGrade:
    description = frontmatter.get("description", "")
    if "Use when" in description and "NOT for" in description and has_heading(text, "When To Use"):
        return AxisGrade(
            "Activation Precision",
            94,
            "Activation and false-positive boundaries are explicit.",
        )
    if "Use when" in description:
        return AxisGrade(
            "Activation Precision",
            82,
            "Activation exists but false-positive boundaries are weak.",
        )
    return AxisGrade("Activation Precision", 65, "Activation depends on vague wording.")


def grade_io(text: str) -> AxisGrade:
    has_inputs = has_heading(text, "Inputs Expected")
    has_outputs = has_heading(text, "Output Expected")
    output = section_text(text, "Output Expected")
    if has_inputs and has_outputs and "```md" in output:
        return AxisGrade(
            "Input/Output Contract",
            95,
            "Inputs and fenced output shape are explicit.",
        )
    if has_inputs and has_outputs:
        return AxisGrade(
            "Input/Output Contract",
            84,
            "Inputs and outputs exist but output shape is loose.",
        )
    return AxisGrade("Input/Output Contract", 62, "Input or output contract is missing.")


def grade_process(text: str) -> AxisGrade:
    process = section_text(text, "Process")
    steps = numbered_step_count(process)
    if steps >= 5:
        return AxisGrade("Process Specificity", 95, f"Process has {steps} concrete steps.")
    if steps >= 3:
        return AxisGrade("Process Specificity", 84, f"Process has {steps} steps.")
    return AxisGrade("Process Specificity", 65, "Process is missing or too thin.")


def grade_examples(path: Path, text: str) -> AxisGrade:
    examples = section_text(text, "Examples")
    example_files = sorted((path.parent / "examples").glob("*.md"))
    has_simple = "Simple case:" in examples
    has_complex = "Complex case:" in examples or "edge case" in examples.lower()
    if len(example_files) >= 2 and has_simple and has_complex:
        return AxisGrade("Example Coverage", 95, "Simple and complex examples are present.")
    if len(example_files) >= 2:
        return AxisGrade(
            "Example Coverage",
            84,
            "Example files exist but SKILL.md examples are thin.",
        )
    return AxisGrade("Example Coverage", 62, "Skill needs at least two examples.")


def grade_failure_modes(text: str) -> AxisGrade:
    failure_modes = section_text(text, "Failure Modes")
    bullets = bullet_count(failure_modes)
    if bullets >= 4:
        return AxisGrade(
            "Failure Handling",
            94,
            "Failure modes cover common missing-context cases.",
        )
    if bullets >= 2:
        return AxisGrade("Failure Handling", 84, "Failure modes exist but could cover more cases.")
    return AxisGrade("Failure Handling", 62, "Failure modes are missing or too thin.")


def grade_safety(text: str) -> AxisGrade:
    safety = section_text(text, "Safety And Privacy").lower()
    markers = ["secret", "private", "credential", "customer", "production", "destructive"]
    hits = sum(marker in safety for marker in markers)
    if hits >= 2:
        return AxisGrade(
            "Safety and Privacy",
            94,
            "Safety notes name concrete data or action risks.",
        )
    if safety.strip():
        return AxisGrade("Safety and Privacy", 82, "Safety section exists but risks are broad.")
    return AxisGrade("Safety and Privacy", 60, "Safety section is missing.")


def grade_anti_slop(text: str) -> AxisGrade:
    anti_slop = section_text(text, "Anti-Slop Rules")
    do_not_rules = sum(1 for line in anti_slop.splitlines() if line.startswith("- Do not "))
    if do_not_rules >= 3:
        return AxisGrade("Anti-Slop Rules", 94, "Concrete anti-slop rules are present.")
    if anti_slop.strip():
        return AxisGrade("Anti-Slop Rules", 82, "Anti-slop section exists but is thin.")
    return AxisGrade("Anti-Slop Rules", 60, "Anti-slop section is missing.")


def grade_docs(text: str) -> AxisGrade:
    present = sum(has_heading(text, heading) for heading in REQUIRED_SECTIONS)
    repo_docs = all(
        (ROOT / path).exists()
        for path in [
            "README.md",
            "CONTRIBUTING.md",
            "docs/architecture.md",
            "docs/skill-standard.md",
            "docs/review-checklist.md",
        ]
    )
    if present == len(REQUIRED_SECTIONS) and repo_docs:
        return AxisGrade(
            "Documentation Quality",
            96,
            "Skill standard sections and repo docs exist.",
        )
    if present >= len(REQUIRED_SECTIONS) - 2:
        return AxisGrade("Documentation Quality", 84, "Most expected sections are present.")
    return AxisGrade("Documentation Quality", 70, "Skill documentation structure is incomplete.")


def grade_skill(path: Path) -> SkillGrade:
    text = path.read_text(encoding="utf-8")
    frontmatter = parse_frontmatter(text)
    axes = [
        grade_description(frontmatter),
        grade_scope(text),
        grade_progressive(text),
        grade_activation(frontmatter, text),
        grade_io(text),
        grade_process(text),
        grade_examples(path, text),
        grade_failure_modes(text),
        grade_safety(text),
        grade_anti_slop(text),
        grade_docs(text),
    ]
    weighted_total = (
        axes[0].score * 2
        + axes[1].score * 2
        + sum(axis.score for axis in axes[2:])
    )
    score = weighted_total / (len(axes) + 2)
    return SkillGrade(frontmatter.get("name", path.parent.name), score, axes)


def render_report(grades: list[SkillGrade]) -> str:
    lines = [
        "# Skill Grade Report",
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
    args = parser.parse_args()

    grades = [grade_skill(path) for path in skill_files()]
    print(render_report(grades))

    failures = [grade for grade in grades if grade.score < args.min_score]
    if failures:
        names = ", ".join(f"{grade.name} ({grade.score:.1f})" for grade in failures)
        print(f"\nSkills below minimum score {args.min_score:.1f}: {names}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
