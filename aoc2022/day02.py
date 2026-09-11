"""Day 2: Rock Paper Scissors.

Opponent plays A/B/C (rock/paper/scissors).

Part 1: X/Y/Z is the shape you play.
Part 2: X/Y/Z means lose/draw/win, and you choose the matching shape.

Score for a round is shape points (1/2/3) plus outcome (0/3/6).
"""

from __future__ import annotations

from aoc2022.util import non_empty_lines

ROCK, PAPER, SCISSORS = 0, 1, 2
SHAPE_POINTS = (1, 2, 3)
OPPONENT = {"A": ROCK, "B": PAPER, "C": SCISSORS}
YOUR_SHAPE = {"X": ROCK, "Y": PAPER, "Z": SCISSORS}
GOAL_OFFSET = {"X": -1, "Y": 0, "Z": 1}  # lose, draw, win


def _round_score(you: int, opponent: int) -> int:
    result = (you - opponent) % 3
    outcome_points = {0: 3, 1: 6, 2: 0}[result]
    return SHAPE_POINTS[you] + outcome_points


def _parse_rounds(puzzle_input: str) -> list[tuple[str, str]]:
    return [tuple(line.split()) for line in non_empty_lines(puzzle_input)]


def part1(puzzle_input: str) -> int:
    total = 0
    for opponent_move, your_move in _parse_rounds(puzzle_input):
        total += _round_score(YOUR_SHAPE[your_move], OPPONENT[opponent_move])
    return total


def part2(puzzle_input: str) -> int:
    total = 0
    for opponent_move, goal in _parse_rounds(puzzle_input):
        opponent = OPPONENT[opponent_move]
        you = (opponent + GOAL_OFFSET[goal]) % 3
        total += _round_score(you, opponent)
    return total
