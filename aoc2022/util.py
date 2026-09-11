"""Shared helpers for reading puzzle input."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INPUTS_DIR = ROOT / "inputs"
EXAMPLES_DIR = ROOT / "examples"


def puzzle_path(day: int, *, example: bool = False) -> Path:
    folder = EXAMPLES_DIR if example else INPUTS_DIR
    return folder / f"day{day:02d}.txt"


def read_text(day: int, *, example: bool = False) -> str:
    path = puzzle_path(day, example=example)
    if not path.exists():
        kind = "example" if example else "personal"
        raise FileNotFoundError(
            f"Missing {kind} input for day {day}: {path}\n"
            "Download your puzzle input from https://adventofcode.com/2022 "
            f"and save it as {path.name} in the {path.parent.name}/ folder."
        )
    return path.read_text(encoding="utf-8")


def non_empty_lines(text: str) -> list[str]:
    return [line.strip() for line in text.splitlines() if line.strip()]
