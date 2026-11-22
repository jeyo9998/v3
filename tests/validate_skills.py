#!/usr/bin/env python3
"""Validate the basic structure and frontmatter of local Agent Skills."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is missing. Run: python -m pip install -r requirements-dev.txt")
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MAX_NAME_LENGTH = 64
MAX_DESCRIPTION_LENGTH = 1024
MAX_SKILL_LINES = 500


def parse_frontmatter(skill_file: Path) -> tuple[dict[str, Any] | None, str | None]:
    """Return parsed YAML frontmatter or a readable validation error."""
    try:
        content = skill_file.read_text(encoding="utf-8")
    except OSError as exc:
        return None, f"cannot read file: {exc}"

    lines = content.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, "file must start with YAML frontmatter opened by ---"

    try:
        closing_index = lines.index("---", 1)
    except ValueError:
        return None, "YAML frontmatter is missing its closing ---"

    raw_yaml = "\n".join(lines[1:closing_index])
    try:
        metadata = yaml.safe_load(raw_yaml)
    except yaml.YAMLError as exc:
        return None, f"invalid YAML frontmatter: {exc}"

    if not isinstance(metadata, dict):
        return None, "frontmatter must be a YAML mapping"

    return metadata, None


def validate_skill(skill_dir: Path) -> list[str]:
    """Return validation errors for one skill directory."""
    errors: list[str] = []
    skill_file = skill_dir / "SKILL.md"

    if not skill_file.is_file():
        return [f"{skill_dir.relative_to(ROOT)}: missing SKILL.md"]

    metadata, parse_error = parse_frontmatter(skill_file)
    if parse_error:
        return [f"{skill_file.relative_to(ROOT)}: {parse_error}"]

    assert metadata is not None
    name = metadata.get("name")
    description = metadata.get("description")

    if not isinstance(name, str) or not name.strip():
        errors.append("frontmatter field 'name' must be a non-empty string")
    else:
        if len(name) > MAX_NAME_LENGTH:
            errors.append(f"name exceeds {MAX_NAME_LENGTH} characters")
        if not NAME_PATTERN.fullmatch(name):
            errors.append("name must use lowercase letters, digits, and single hyphens")
        if name != skill_dir.name:
            errors.append(f"name '{name}' must match directory '{skill_dir.name}'")

    if not isinstance(description, str) or not description.strip():
        errors.append("frontmatter field 'description' must be a non-empty string")
    elif len(description) > MAX_DESCRIPTION_LENGTH:
        errors.append(f"description exceeds {MAX_DESCRIPTION_LENGTH} characters")

    try:
        line_count = len(skill_file.read_text(encoding="utf-8").splitlines())
        if line_count >= MAX_SKILL_LINES:
            errors.append(f"SKILL.md has {line_count} lines; keep it below {MAX_SKILL_LINES}")
    except OSError as exc:
        errors.append(f"cannot count lines: {exc}")

    if errors:
        return [f"{skill_file.relative_to(ROOT)}: {error}" for error in errors]
    return []


def main() -> int:
    if not SKILLS_DIR.is_dir():
        print("ERROR: skills/ directory not found.")
        return 2

    skill_dirs = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir())
    if not skill_dirs:
        print("ERROR: no skill directories found under skills/.")
        return 2

    all_errors: list[str] = []
    for skill_dir in skill_dirs:
        all_errors.extend(validate_skill(skill_dir))

    if all_errors:
        print("Skill validation FAILED:\n")
        for error in all_errors:
            print(f"- {error}")
        return 1

    print(f"Skill validation PASSED: {len(skill_dirs)} skill(s) checked.")
    for skill_dir in skill_dirs:
        print(f"- {skill_dir.name}/SKILL.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
