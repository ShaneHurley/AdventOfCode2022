"""Advent of Code 2022 solutions."""

from importlib import import_module

__all__ = ["DAYS"]

DAYS = (1, 2, 3, 4)


def get_day(day: int):
    """Return the module for a puzzle day."""
    if day not in DAYS:
        raise ValueError(f"Day {day} is not implemented yet. Available: {list(DAYS)}")
    return import_module(f"aoc2022.day{day:02d}")
