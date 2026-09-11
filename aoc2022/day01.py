"""Day 1: Calorie Counting.

Elves are carrying snacks separated by blank lines. Part 1 asks for the
most calories carried by one elf. Part 2 asks for the top three combined.
"""

from __future__ import annotations


def calorie_totals(puzzle_input: str) -> list[int]:
    """Return each elf's calorie total, highest first."""
    totals = []
    for group in puzzle_input.strip().split("\n\n"):
        meals = [int(line) for line in group.splitlines() if line.strip()]
        totals.append(sum(meals))
    totals.sort(reverse=True)
    return totals


def part1(puzzle_input: str) -> int:
    return calorie_totals(puzzle_input)[0]


def part2(puzzle_input: str) -> int:
    return sum(calorie_totals(puzzle_input)[:3])
