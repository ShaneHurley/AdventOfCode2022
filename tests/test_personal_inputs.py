"""Regression tests against the original Colab notebook answers.

These use the personal puzzle inputs in inputs/. Day 4 is skipped until
that input file is added.
"""

from __future__ import annotations

import unittest

from aoc2022 import day01, day02, day03, day04
from aoc2022.util import puzzle_path, read_text


class PersonalInputTests(unittest.TestCase):
    def test_day01_matches_original_notebook(self) -> None:
        puzzle = read_text(1)
        self.assertEqual(day01.part1(puzzle), 68802)
        self.assertEqual(day01.part2(puzzle), 205370)

    def test_day02_matches_original_notebook(self) -> None:
        puzzle = read_text(2)
        self.assertEqual(day02.part1(puzzle), 14375)
        self.assertEqual(day02.part2(puzzle), 10274)

    def test_day03_matches_original_notebook(self) -> None:
        puzzle = read_text(3)
        self.assertEqual(day03.part1(puzzle), 7967)
        self.assertEqual(day03.part2(puzzle), 2716)

    def test_day04_personal_input_if_present(self) -> None:
        path = puzzle_path(4)
        if not path.exists():
            self.skipTest("Add inputs/day04.txt from adventofcode.com/2022/day/4")
        puzzle = path.read_text(encoding="utf-8")
        contained = day04.part1(puzzle)
        overlap = day04.part2(puzzle)
        self.assertGreater(contained, 0)
        self.assertGreaterEqual(overlap, contained)


if __name__ == "__main__":
    unittest.main()
