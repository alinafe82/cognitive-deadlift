from __future__ import annotations

from pathlib import Path

from scripts import validate_skills

FIXTURES = Path(__file__).parent / "fixtures"


def test_discovers_real_skills() -> None:
    names = [path.name for path in validate_skills.skill_dirs()]

    assert "problem-framing" in names
    assert "diff-interrogation" in names


def test_parse_frontmatter() -> None:
    text = '---\nname: example\ndescription: "Use when X. NOT for Y."\n---\n# Body\n'

    metadata, errors = validate_skills.parse_frontmatter(text)

    assert errors == []
    assert metadata["name"] == "example"
    assert metadata["description"] == "Use when X. NOT for Y."


def test_good_skill_fixture_passes() -> None:
    result = validate_skills.validate_all(FIXTURES / "good-repo")

    assert result.errors == []


def test_bad_skill_fixture_fails() -> None:
    result = validate_skills.validate_all(FIXTURES / "bad-repo")

    assert any("missing section" in error for error in result.errors)
    assert any("banned filler phrase" in error for error in result.errors)
    assert any("must include at least two markdown examples" in error for error in result.errors)


def test_real_skills_have_examples() -> None:
    for skill in validate_skills.skill_dirs():
        examples = list((skill / "examples").glob("*.md"))
        assert len(examples) >= 2, skill
