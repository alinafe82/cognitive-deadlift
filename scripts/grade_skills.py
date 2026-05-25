#!/usr/bin/env python3
"""Grade Cognitive Deadlift skills against a compact skill-quality rubric."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
DATE_RE = re.compile(r"\b20\d{2}-\d{2}-\d{2}\b")


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


def has_table_after(text: str, heading: str) -> bool:
    section_start = text.find(f"\n## {heading}\n")
    if section_start == -1:
        return False
    next_heading = text.find("\n## ", section_start + 1)
    section = text[section_start: next_heading if next_heading != -1 else len(text)]
    return "| --- |" in section


def grade_description(frontmatter: dict[str, str]) -> AxisGrade:
    description = frontmatter.get("description", "")
    words = description.split()
    has_use = "Use when" in description
    has_not = "NOT for" in description
    has_name = bool(frontmatter.get("name"))

    if has_name and has_use and has_not and 25 <= len(words) <= 70:
        return AxisGrade("Description Quality", 95, "Specific trigger, exclusions, and compact length.")
    if has_name and has_use and has_not:
        return AxisGrade("Description Quality", 88, "Good trigger and exclusions; length could be tighter.")
    if description:
        return AxisGrade("Description Quality", 74, "Description exists but lacks trigger or exclusion precision.")
    return AxisGrade("Description Quality", 0, "Description is missing.")


def grade_scope(text: str) -> AxisGrade:
    if has_heading(text, "When To Use") and has_heading(text, "Do Not Use For"):
        return AxisGrade("Scope Discipline", 95, "Explicit use and non-use boundaries.")
    if has_heading(text, "When To Use") or has_heading(text, "Do Not Use For"):
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
    return AxisGrade("Progressive Disclosure", 60, f"Too long for a primary skill file ({lines} lines).")


def grade_anti_patterns(text: str) -> AxisGrade:
    if has_heading(text, "Anti-Patterns") and has_table_after(text, "Anti-Patterns"):
        return AxisGrade("Anti-Pattern Coverage", 94, "Anti-pattern table maps novice moves to expert moves.")
    if has_heading(text, "Anti-Patterns"):
        return AxisGrade("Anti-Pattern Coverage", 82, "Anti-patterns exist but are not table-structured.")
    return AxisGrade("Anti-Pattern Coverage", 62, "No anti-pattern section.")


def grade_tools(text: str) -> AxisGrade:
    if has_heading(text, "Tooling"):
        return AxisGrade("Self-Contained Tools", 93, "Tool expectations are explicit.")
    return AxisGrade("Self-Contained Tools", 72, "Tool expectations are implicit.")


def grade_activation(frontmatter: dict[str, str], text: str) -> AxisGrade:
    description = frontmatter.get("description", "")
    if "Use when" in description and "NOT for" in description and has_heading(text, "When To Use"):
        return AxisGrade("Activation Precision", 94, "Activation and false-positive boundaries are explicit.")
    if "Use when" in description:
        return AxisGrade("Activation Precision", 82, "Activation exists but false-positive boundaries are weak.")
    return AxisGrade("Activation Precision", 65, "Activation depends on vague wording.")


def grade_visuals(text: str) -> AxisGrade:
    has_mermaid = "```mermaid" in text
    has_tables = "| --- |" in text
    if has_mermaid and has_tables:
        return AxisGrade("Visual Artifacts", 95, "Includes decision flow and comparison table.")
    if has_mermaid or has_tables:
        return AxisGrade("Visual Artifacts", 84, "Includes one visual structure.")
    return AxisGrade("Visual Artifacts", 65, "No diagrams or tables.")


def grade_output(text: str) -> AxisGrade:
    if has_heading(text, "Output Contract") and "```md" in text:
        return AxisGrade("Output Contracts", 95, "Structured markdown output contract is explicit.")
    if has_heading(text, "Output Contract"):
        return AxisGrade("Output Contracts", 84, "Output contract exists but lacks a fenced template.")
    return AxisGrade("Output Contracts", 62, "No explicit output contract.")


def grade_temporal(text: str) -> AxisGrade:
    if has_heading(text, "Temporal Note") and DATE_RE.search(text):
        return AxisGrade("Temporal Awareness", 92, "Temporal status is explicit and dated.")
    if has_heading(text, "Temporal Note"):
        return AxisGrade("Temporal Awareness", 84, "Temporal status exists but is not dated.")
    return AxisGrade("Temporal Awareness", 65, "No temporal status.")


def grade_docs(text: str) -> AxisGrade:
    required = ["When To Use", "Do Not Use For", "Process", "Output Contract"]
    present = sum(has_heading(text, heading) for heading in required)
    repo_docs = all((ROOT / path).exists() for path in ["README.md", "CATALOG.md", "CHANGELOG.md"])
    if present == len(required) and repo_docs:
        return AxisGrade("Documentation Quality", 92, "Skill is self-contained and repo-level docs exist.")
    if present >= 3:
        return AxisGrade("Documentation Quality", 84, "Most expected sections are present.")
    return AxisGrade("Documentation Quality", 70, "Skill documentation structure is incomplete.")


def grade_skill(path: Path) -> SkillGrade:
    text = path.read_text(encoding="utf-8")
    frontmatter = parse_frontmatter(text)
    axes = [
        grade_description(frontmatter),
        grade_scope(text),
        grade_progressive(text),
        grade_anti_patterns(text),
        grade_tools(text),
        grade_activation(frontmatter, text),
        grade_visuals(text),
        grade_output(text),
        grade_temporal(text),
        grade_docs(text),
    ]
    weighted_total = (
        axes[0].score * 2
        + axes[1].score * 2
        + sum(axis.score for axis in axes[2:])
    )
    score = weighted_total / 12
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
