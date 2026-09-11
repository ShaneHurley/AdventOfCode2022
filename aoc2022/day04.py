"""Day 4: Camp Cleanup.

Each line is a pair of inclusive section ranges, like ``2-4,6-8``.

Part 1: count pairs where one range fully contains the other.
Part 2: count pairs where the ranges overlap at all.
"""

from __future__ import annotations

from aoc2022.util import non_empty_lines


def _parse_range(text: str) -> tuple[int, int]:
    start, end = text.split("-")
    return int(start), int(end)


def _parse_pairs(puzzle_input: str) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    pairs = []
    for line in non_empty_lines(puzzle_input):
        left, right = line.split(",")
        pairs.append((_parse_range(left), _parse_range(right)))
    return pairs


def _fully_contains(a: tuple[int, int], b: tuple[int, int]) -> bool:
    return (a[0] <= b[0] and a[1] >= b[1]) or (b[0] <= a[0] and b[1] >= a[1])


def _overlaps(a: tuple[int, int], b: tuple[int, int]) -> bool:
    return a[0] <= b[1] and b[0] <= a[1]


def part1(puzzle_input: str) -> int:
    return sum(1 for left, right in _parse_pairs(puzzle_input) if _fully_contains(left, right))


def part2(puzzle_input: str) -> int:
    return sum(1 for left, right in _parse_pairs(puzzle_input) if _overlaps(left, right))
