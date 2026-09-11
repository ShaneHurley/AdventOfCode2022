"""Tests for shared helpers and the CLI."""

from __future__ import annotations

import io
import unittest
from contextlib import redirect_stderr, redirect_stdout

from aoc2022 import DAYS, get_day
from aoc2022.__main__ import main
from aoc2022.day02 import PAPER, ROCK, SCISSORS, _round_score
from aoc2022.day03 import priority


def _run_cli(argv: list[str]) -> tuple[int, str, str]:
    stdout, stderr = io.StringIO(), io.StringIO()
    with redirect_stdout(stdout), redirect_stderr(stderr):
        code = main(argv)
    return code, stdout.getvalue(), stderr.getvalue()


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
        code, stdout, stderr = _run_cli(["--example", "2"])
        self.assertEqual(code, 0)
        self.assertIn("Part 1: 15", stdout)
        self.assertIn("Part 2: 12", stdout)
        self.assertEqual(stderr, "")

    def test_cli_all_personal_days_skips_missing_input(self) -> None:
        code, stdout, _stderr = _run_cli([])
        self.assertEqual(code, 0)
        self.assertIn("Day 01", stdout)
        self.assertIn("Day 04: skipped", stdout)

    def test_cli_unknown_day(self) -> None:
        code, _stdout, stderr = _run_cli(["25"])
        self.assertEqual(code, 1)
        self.assertIn("not implemented", stderr)


if __name__ == "__main__":
    unittest.main()
