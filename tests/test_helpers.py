"""Tests for shared helpers and the CLI."""

from __future__ import annotations

import unittest

from aoc2022 import DAYS, get_day
from aoc2022.__main__ import main
from aoc2022.day02 import _round_score, PAPER, ROCK, SCISSORS
from aoc2022.day03 import priority


class HelperTests(unittest.TestCase):
    def test_available_days(self) -> None:
        self.assertEqual(DAYS, (1, 2, 3, 4))
        self.assertTrue(hasattr(get_day(4), "part1"))
        with self.assertRaises(ValueError):
            get_day(5)

    def test_rock_paper_scissors_scoring(self) -> None:
        self.assertEqual(_round_score(ROCK, ROCK), 4)  # draw
        self.assertEqual(_round_score(PAPER, ROCK), 8)  # win
        self.assertEqual(_round_score(SCISSORS, ROCK), 3)  # loss

    def test_item_priorities(self) -> None:
        self.assertEqual(priority("a"), 1)
        self.assertEqual(priority("z"), 26)
        self.assertEqual(priority("A"), 27)
        self.assertEqual(priority("Z"), 52)

    def test_cli_example_day_two(self) -> None:
        self.assertEqual(main(["--example", "2"]), 0)

    def test_cli_unknown_day(self) -> None:
        self.assertEqual(main(["25"]), 1)


if __name__ == "__main__":
    unittest.main()
