# Advent of Code 2022

Python solutions for [Advent of Code 2022](https://adventofcode.com/2022). Started in Google Colab in 2023 (days 1–3), then cleaned up into a regular Python package so the repo is easy to clone, run, and keep going.

## Progress

| Day | Puzzle | Part 1 | Part 2 |
| --- | --- | --- | --- |
| 01 | [Calorie Counting](https://adventofcode.com/2022/day/1) | 68802 | 205370 |
| 02 | [Rock Paper Scissors](https://adventofcode.com/2022/day/2) | 14375 | 10274 |
| 03 | [Rucksack Reorganization](https://adventofcode.com/2022/day/3) | 7967 | 2716 |
| 04 | [Camp Cleanup](https://adventofcode.com/2022/day/4) | example: 2 | example: 4 |
| 05–25 | Not started | | |

Day 4 is implemented and checked against the official sample. Drop your personal input in `inputs/day04.txt` and run it the same way as the earlier days.

## Run

Python 3.10+ is enough. There are no extra packages. Use `python3` if `python` is not on your PATH.

```bash
# Official examples
python3 -m aoc2022 --example
python3 -m aoc2022 --example 4

# Personal inputs in inputs/dayXX.txt
python3 -m aoc2022
python3 -m aoc2022 1
```

## Test

```bash
python3 -m unittest discover -s tests -v
```

Tests cover the official samples, scoring helpers, and a regression against the original Colab answers for days 1–3.

## Layout

```
aoc2022/          # one module per day
examples/         # official sample inputs
inputs/           # personal puzzle inputs
tests/
ROADMAP.md        # remaining AoC days + next GitHub project
```

Each day exposes `part1(text)` and `part2(text)` so the runner and tests stay the same as new days get added.

## What changed from the Colab notebooks

The original files were cell-by-cell Colab scripts (`Day1.ipynb` … `Day3.ipynb`): files left open, `input` used as a variable name, magic ASCII offsets, and hardcoded lookup tables. Those solutions still produce the same answers; they are just regular functions now.

A basketball ELO notebook (`basketballevaluatorPASTYEARS.ipynb`) was committed here from Colab in May 2026. That work already lives in [BasketballElo](https://github.com/ShaneHurley/BasketballElo), so it was removed from this repo. See [ROADMAP.md](ROADMAP.md) for how far that project got and what to do next with it.

## Next

**This repo:** Day 5 (Supply Stacks). After that, days 6–10 are a good streak — parsing, stacks, sliding windows, trees, and a tiny CRT.

**The other project:** [BasketballElo](https://github.com/ShaneHurley/BasketballElo) is further along than this repo ever was, but it is still a Colab dump. Details and a cleanup plan are in [ROADMAP.md](ROADMAP.md).
