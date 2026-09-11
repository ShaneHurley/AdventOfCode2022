"""Command-line runner: ``python3 -m aoc2022 1`` or ``python3 -m aoc2022 --example 4``."""

from __future__ import annotations

import argparse
import sys

from aoc2022 import DAYS, get_day
from aoc2022.util import read_text


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Run Advent of Code 2022 solutions.",
    )
    parser.add_argument(
        "day",
        nargs="?",
        type=int,
        help="Puzzle day to run (default: all implemented days).",
    )
    parser.add_argument(
        "--example",
        action="store_true",
        help="Use the official example input instead of inputs/dayXX.txt.",
    )
    args = parser.parse_args(argv)

    requested = args.day is not None
    days = [args.day] if requested else list(DAYS)
    ran = 0

    for day in days:
        try:
            module = get_day(day)
            puzzle_input = read_text(day, example=args.example)
        except ValueError as exc:
            print(exc, file=sys.stderr)
            return 1
        except FileNotFoundError as exc:
            if requested:
                print(exc, file=sys.stderr)
                return 1
            print(f"Day {day:02d}: skipped (no input file yet)")
            continue

        label = "example" if args.example else "input"
        print(f"Day {day:02d} ({label})")
        print(f"  Part 1: {module.part1(puzzle_input)}")
        print(f"  Part 2: {module.part2(puzzle_input)}")
        ran += 1

    if ran == 0:
        print("No days were run.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
