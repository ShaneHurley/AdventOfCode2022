"""Day 3: Rucksack Reorganization.

Each rucksack is a string of item types. The first half and second half
are the two compartments.

Part 1: priority of the item that appears in both compartments.
Part 2: priority of the badge shared by each group of three elves.
"""

from __future__ import annotations

from aoc2022.util import non_empty_lines

PRIORITIES = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def priority(item: str) -> int:
    return PRIORITIES.index(item) + 1


def part1(puzzle_input: str) -> int:
    total = 0
    for sack in non_empty_lines(puzzle_input):
        mid = len(sack) // 2
        shared = set(sack[:mid]) & set(sack[mid:])
        total += priority(next(iter(shared)))
    return total


def part2(puzzle_input: str) -> int:
    sacks = non_empty_lines(puzzle_input)
    total = 0
    for i in range(0, len(sacks), 3):
        first, second, third = sacks[i : i + 3]
        badge = set(first) & set(second) & set(third)
        total += priority(next(iter(badge)))
    return total
