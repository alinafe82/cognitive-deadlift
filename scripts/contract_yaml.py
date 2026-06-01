"""Tiny YAML reader for Cognitive Deadlift contract files.

This supports only the subset this repo owns:
- top-level mappings
- one nested mapping level
- scalar strings
- list values using "- item"

It is intentionally not a general YAML parser.
"""

from __future__ import annotations

from pathlib import Path


def read_contract_yaml(path: Path) -> dict[str, object]:
    """Read the repo's simple YAML contract files."""
    root: dict[str, object] = {}
    current_top: str | None = None
    current_field: str | None = None

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue

        indent = len(raw_line) - len(raw_line.lstrip(" "))
        line = raw_line.strip()

        if indent == 0:
            if not line.endswith(":"):
                key, value = split_scalar(line, path)
                root[key] = value
                current_top = None
                current_field = None
                continue
            current_top = line[:-1]
            root[current_top] = None
            current_field = None
            continue

        if current_top is None:
            raise ValueError(f"{path}: nested value without parent: {raw_line}")

        top_value = root[current_top]

        if indent == 2 and line.endswith(":"):
            if top_value is None:
                top_value = {}
                root[current_top] = top_value
            if not isinstance(top_value, dict):
                raise ValueError(f"{path}: cannot nest mapping under list key {current_top}")
            current_field = line[:-1]
            top_value[current_field] = []
            continue

        if indent == 2 and not line.startswith("- "):
            if top_value is None:
                top_value = {}
                root[current_top] = top_value
            if not isinstance(top_value, dict):
                raise ValueError(f"{path}: cannot nest scalar under list key {current_top}")
            key, value = split_scalar(line, path)
            top_value[key] = value
            current_field = key
            continue

        if indent == 2 and line.startswith("- "):
            if top_value is None:
                top_value = []
                root[current_top] = top_value
            root_list = top_value
            if not isinstance(root_list, list):
                raise ValueError(f"{path}: mixed mapping and list at {current_top}")
            root_list.append(line[2:].strip())
            continue

        if indent == 4 and line.startswith("- ") and current_field:
            if not isinstance(top_value, dict):
                raise ValueError(f"{path}: cannot nest list item under non-mapping {current_top}")
            field_value = top_value.setdefault(current_field, [])
            if not isinstance(field_value, list):
                raise ValueError(f"{path}: mixed scalar and list at {current_field}")
            field_value.append(line[2:].strip())
            continue

        raise ValueError(f"{path}: unsupported YAML shape: {raw_line}")

    return root


def split_scalar(line: str, path: Path) -> tuple[str, str]:
    if ":" not in line:
        raise ValueError(f"{path}: expected key: value line: {line}")
    key, value = line.split(":", 1)
    return key.strip(), value.strip()
