import json
from pathlib import Path

from scripts import validate_skills


def compact_skill(tmp_path: Path) -> Path:
    skill = tmp_path / "skills" / "repair-parser"
    (skill / "examples").mkdir(parents=True)
    (skill / "tests").mkdir()
    (skill / "SKILL.md").write_text("""---
name: repair-parser
description: Diagnose a parser regression from a failing input.
---

## Scope
Use for parser regressions; skip unrelated copy edits.

## Workflow
Reproduce the failing input, inspect the parser, fix the cause and rerun the regression.

## Evidence
Use a failing input and expected output; report the changed behavior and actual check results.

## Boundaries
Use synthetic records and do not expose private input. Report missing evidence honestly.

## References
[Simple](examples/simple.md) and [Edge](examples/edge-case.md).
""")
    for name in ["simple", "edge-case"]:
        (skill / "examples" / f"{name}.md").write_text(
            f"# {name}\n\nInput and expected parser result.\n"
        )
    (skill / "tests/routing.json").write_text(
        json.dumps(
            {
                "use": [
                    {
                        "request": "Fix parsing of an empty record.",
                        "reason": "An observable parser failure.",
                    }
                ],
                "skip": [
                    {"request": "Correct a README typo.", "reason": "No parser behavior changes."}
                ],
            }
        )
    )
    return skill


def test_compact_skill_without_magic_description_words_or_fourteen_sections(tmp_path):
    skill = compact_skill(tmp_path)
    assert validate_skills.validate_skill(skill, tmp_path) == []


def test_compact_skill_rejects_missing_evidence(tmp_path):
    skill = compact_skill(tmp_path)
    path = skill / "SKILL.md"
    path.write_text(path.read_text().replace("## Evidence", "## Unrelated"))
    assert any("Evidence" in x for x in validate_skills.validate_skill(skill, tmp_path))


def test_compact_skill_rejects_broken_reference(tmp_path):
    skill = compact_skill(tmp_path)
    (skill / "examples/simple.md").unlink()
    assert any("broken internal link" in x for x in validate_skills.validate_skill(skill, tmp_path))


def test_compact_skill_rejects_missing_negative_routing_case(tmp_path):
    skill = compact_skill(tmp_path)
    path = skill / "tests/routing.json"
    data = json.loads(path.read_text())
    del data["skip"]
    path.write_text(json.dumps(data))
    assert any("skip" in x for x in validate_skills.validate_skill(skill, tmp_path))


def test_compact_skill_rejects_contradictory_routing_examples(tmp_path):
    skill = compact_skill(tmp_path)
    path = skill / "tests/routing.json"
    data = json.loads(path.read_text())
    data["skip"] = data["use"]
    path.write_text(json.dumps(data))
    assert any("both" in x for x in validate_skills.validate_skill(skill, tmp_path))


def test_compact_grader_does_not_reward_padding(tmp_path):
    from scripts.grade_skills import grade_skill

    skill = compact_skill(tmp_path)
    assert grade_skill(skill / "SKILL.md").score == 100
    path = skill / "tests/routing.json"
    path.write_text("{}")
    assert grade_skill(skill / "SKILL.md").score < 100
