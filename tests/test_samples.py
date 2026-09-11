"""Tests against the official Advent of Code 2022 example inputs."""

from __future__ import annotations

import unittest

from aoc2022 import day01, day02, day03, day04
from aoc2022.util import read_text


class SampleTests(unittest.TestCase):
    def test_day01_example(self) -> None:
        puzzle = read_text(1, example=True)
        self.assertEqual(day01.part1(puzzle), 24000)
        self.assertEqual(day01.part2(puzzle), 45000)

    def test_day02_example(self) -> None:
        puzzle = read_text(2, example=True)
        self.assertEqual(day02.part1(puzzle), 15)
        self.assertEqual(day02.part2(puzzle), 12)

    def test_day03_example(self) -> None:
        puzzle = read_text(3, example=True)
        self.assertEqual(day03.part1(puzzle), 157)
        self.assertEqual(day03.part2(puzzle), 70)

    def test_day04_example(self) -> None:
        puzzle = read_text(4, example=True)
        self.assertEqual(day04.part1(puzzle), 2)
        self.assertEqual(day04.part2(puzzle), 4)


if __name__ == "__main__":
    unittest.main()
