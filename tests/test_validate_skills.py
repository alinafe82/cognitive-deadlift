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


def test_markdown_links_accept_optional_titles(tmp_path: Path) -> None:
    readme = tmp_path / "README.md"
    target = tmp_path / "CONTRIBUTING.md"
    target.write_text("# Contributing\n", encoding="utf-8")
    readme.write_text(
        '[Guide](CONTRIBUTING.md "Contrib guide")\n'
        "[Angle guide](<CONTRIBUTING.md> 'Contrib guide')\n",
        encoding="utf-8",
    )
    errors: list[str] = []

    validate_skills.validate_links(readme, readme.read_text(encoding="utf-8"), tmp_path, errors)

    assert errors == []


def test_real_skills_have_examples() -> None:
    for skill in validate_skills.skill_dirs():
        examples = list((skill / "examples").glob("*.md"))
        assert len(examples) >= 2, skill


def test_slop_scanner_ignores_backticked_banned_phrases(tmp_path: Path) -> None:
    """Banned phrases inside backticks (as examples of what to avoid) must not trip the scanner."""
    md = tmp_path / "doc.md"
    md.write_text(
        "Do not use words like `seamlessly`, `revolutionary`, or `world-class`.\n",
        encoding="utf-8",
    )
    errors: list[str] = []

    validate_skills.validate_no_bad_text(md, md.read_text(encoding="utf-8"), tmp_path, errors)

    assert errors == []


def test_slop_scanner_catches_banned_phrase_in_prose(tmp_path: Path) -> None:
    md = tmp_path / "doc.md"
    md.write_text("Our seamlessly integrated platform is world-class.\n", encoding="utf-8")
    errors: list[str] = []

    validate_skills.validate_no_bad_text(md, md.read_text(encoding="utf-8"), tmp_path, errors)

    assert any("seamlessly" in e for e in errors)
    assert any("world-class" in e for e in errors)


def test_slop_scan_checks_yaml_and_json_files(tmp_path: Path) -> None:
    yaml_file = tmp_path / "context.yaml"
    json_file = tmp_path / "plugin.json"
    yaml_file.write_text("description: seamlessly connected checks\n", encoding="utf-8")
    json_file.write_text('{"description": "world-class adapter"}\n', encoding="utf-8")

    result = validate_skills.slop_scan(tmp_path)

    assert any("context.yaml" in error and "seamlessly" in error for error in result.errors)
    assert any("plugin.json" in error and "world-class" in error for error in result.errors)


def test_slop_scanner_ignores_fenced_code_block(tmp_path: Path) -> None:
    md = tmp_path / "doc.md"
    md.write_text(
        "Example of bad copy:\n\n```\nTODO: fix this revolutionary thing\n```\n",
        encoding="utf-8",
    )
    errors: list[str] = []

    validate_skills.validate_no_bad_text(md, md.read_text(encoding="utf-8"), tmp_path, errors)

    assert errors == []
