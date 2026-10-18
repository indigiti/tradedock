#!/usr/bin/env python3
"""Non-trading validation of the English documentation and UI-only source edits.

Run from repository root:
    python3 tools/check_english_translation.py

The comparison intentionally uses origin/main. CI must checkout full git history.
It verifies UI source changes are exactly the reviewed literal substitutions,
not edits to order routing, event handlers, expressions, or logic.
"""
from __future__ import annotations

import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
MAPPING = json.loads((ROOT / "tools/english-ui-glossary.json").read_text(encoding="utf-8"))
LINK_RE = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^)]+)\)")


def git(*args: str) -> str:
    proc = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, check=False)
    if proc.returncode:
        raise RuntimeError(f"git {' '.join(args)}: {proc.stderr.strip()}")
    return proc.stdout


def validate_source_edits() -> int:
    changed = git("diff", "--name-only", "origin/main...HEAD").splitlines()
    sources = [p for p in changed if p.startswith("src/") and p.endswith(".cs")]
    errors = []
    for file in sources:
        before = git("show", f"origin/main:{file}")
        after = (ROOT / file).read_text(encoding="utf-8")
        before_lines = before.splitlines(keepends=True)
        after_lines = after.splitlines(keepends=True)
        if len(before_lines) != len(after_lines):
            errors.append(file + ": line count changed")
            continue
        for line_number, (original_line, translated_line) in enumerate(zip(before_lines, after_lines), start=1):
            if original_line == translated_line:
                continue
            expected_line = original_line
            for source, target in MAPPING.items():
                source_token = '"' + source + '"'
                target_token = '"' + target + '"'
                # Only require changes that actually appear on this line.
                # New glossary entries must not force every UI view to be translated
                # at once, but any change must still be a reviewed literal.
                if source_token in expected_line and target_token in translated_line:
                    expected_line = expected_line.replace(source_token, target_token)
            if expected_line != translated_line:
                errors.append(f"{file}:{line_number}")
    print(f"UI source files changed: {len(sources)}")
    print(f"UI literal-only changes: {'PASS' if not errors else 'FAIL'}")
    if errors:
        print("Unreviewed or inconsistent source changes:")
        for item in errors:
            print("  -", item)
    return len(errors)


def validate_english_links() -> int:
    files = [ROOT / "README.md", ROOT / "docs/README.md", *sorted((ROOT / "docs/en").glob("*.md"))]
    broken = []
    for file in files:
        content = file.read_text(encoding="utf-8")
        for raw in LINK_RE.findall(content):
            href = raw.strip().split(" ", 1)[0].strip("<>")
            if not href or href.startswith(("https://", "http://", "mailto:", "#")):
                continue
            relative = unquote(href.split("#", 1)[0].split("?", 1)[0])
            if relative and not (file.parent / relative).exists():
                broken.append((str(file.relative_to(ROOT)), href))
    print(f"English documentation files checked: {len(files)}")
    print(f"English documentation links: {'PASS' if not broken else 'FAIL'}")
    for page, link in broken:
        print(f"  - {page} -> {link}")
    return len(broken)


def report_remaining_localization() -> None:
    translated_files = list((ROOT / "src/TradingHub.App").rglob("*.cs"))
    # Heuristic only: includes developer comments and Spanish strings that are not UI.
    count = 0
    for file in translated_files:
        count += len(re.findall(r'(?<!\\)"[^"\n]*[áéíóúñ¿¡][^"\n]*"', file.read_text(encoding="utf-8")))
    print(f"Remaining accented source-string candidates (includes non-UI): {count}")
    print("Localization coverage: INCOMPLETE until manual UI review resolves remaining strings.")


if __name__ == "__main__":
    try:
        problems = validate_source_edits() + validate_english_links()
        report_remaining_localization()
        sys.exit(1 if problems else 0)
    except (OSError, RuntimeError) as exc:
        print(f"Validation unavailable: {exc}", file=sys.stderr)
        sys.exit(2)
