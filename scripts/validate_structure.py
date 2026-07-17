#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "AGENTS.md",
    "README.md",
    "ARCHITECTURE.md",
    "docs/index.md",
    "docs/PROJECT_STATUS.md",
    "docs/00_MASTER_DESIGN.md",
    "docs/01_INPUT_CONTRACT.md",
    "docs/02_SYSTEM_INSTRUCTIONS.md",
    "docs/03_KNOWLEDGE_BASE_INDEX.md",
    "docs/04_SCRIPT_OUTPUT_SCHEMA.md",
    "docs/05_EVALUATION_RUBRIC.md",
    "docs/06_KNOWLEDGE_SKILLS_ARCHITECTURE_AND_FEEDBACK_LOOP.md",
    "docs/07_REPOSITORY_OPERATING_MODEL.md",
    "templates/SCRIPT_INPUT_PACK.yaml",
    "templates/SCRIPT_OUTPUT_TEMPLATE.md",
]

REQUIRED_SKILLS = [
    "tsd-input-fact-validation",
    "tsd-concept-strategy-design",
    "tsd-shooting-script-generation",
    "tsd-script-quality-review",
    "repo-source-digest",
    "repo-exec-plan-maintenance",
]

FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)

def error(message: str) -> None:
    print(f"ERROR: {message}")

def main() -> int:
    failures = 0

    for rel in REQUIRED_FILES:
        path = ROOT / rel
        if not path.is_file():
            error(f"missing required file: {rel}")
            failures += 1

    for skill in REQUIRED_SKILLS:
        skill_file = ROOT / ".agents" / "skills" / skill / "SKILL.md"
        if not skill_file.is_file():
            error(f"missing skill: {skill_file.relative_to(ROOT)}")
            failures += 1
            continue

        text = skill_file.read_text(encoding="utf-8")
        match = FRONTMATTER_RE.match(text)
        if not match:
            error(f"missing YAML frontmatter: {skill_file.relative_to(ROOT)}")
            failures += 1
            continue

        frontmatter = match.group(1)
        for key in ("name:", "description:"):
            if key not in frontmatter:
                error(f"missing {key[:-1]} in {skill_file.relative_to(ROOT)}")
                failures += 1

    if failures:
        print(f"\nValidation failed with {failures} issue(s).")
        return 1

    print("Repository structure validation passed.")
    print(f"Root: {ROOT}")
    print(f"Skills checked: {len(REQUIRED_SKILLS)}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
