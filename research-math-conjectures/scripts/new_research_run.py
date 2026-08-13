#!/usr/bin/env python3
"""Create a dated, non-overwriting mathematics-research output directory."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import shutil


SKILL_ROOT = Path(__file__).resolve().parent.parent
ASSET_ROOT = SKILL_ROOT / "assets"
TEMPLATES = {
    "DAILY_REPORT_TEMPLATE.md": "DAILY_REPORT.md",
    "LITERATURE_SEARCH_TEMPLATE.md": "LITERATURE_SEARCH.md",
    "CRUX_SUBMISSION_TEMPLATE.md": "CRUX_SUBMISSION_DRAFT.md",
}


def safe_date(value: str) -> str:
    try:
        return date.fromisoformat(value).isoformat()
    except ValueError as exc:
        raise argparse.ArgumentTypeError("date must use YYYY-MM-DD") from exc


def choose_directory(root: Path, run_date: str) -> Path:
    first = root / run_date
    if not first.exists():
        return first
    index = 2
    while True:
        candidate = root / f"{run_date}-run-{index:02d}"
        if not candidate.exists():
            return candidate
        index += 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-root", required=True, type=Path)
    parser.add_argument("--date", default=date.today().isoformat(), type=safe_date)
    args = parser.parse_args()

    output_root = args.output_root.expanduser().resolve()
    if output_root.exists() and not output_root.is_dir():
        parser.error(f"output root is not a directory: {output_root}")
    output_root.mkdir(parents=True, exist_ok=True)

    destination = choose_directory(output_root, args.date)
    destination.mkdir()
    for source_name, target_name in TEMPLATES.items():
        source = ASSET_ROOT / source_name
        if not source.is_file():
            raise FileNotFoundError(f"missing template: {source}")
        shutil.copyfile(source, destination / target_name)

    print(destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
