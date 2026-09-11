# Roadmap

Two tracks: finish Advent of Code 2022 in this repo, then give [BasketballElo](https://github.com/ShaneHurley/BasketballElo) the same cleanup.

## This repo — Advent of Code 2022

Posted on GitHub in November 2023 as Colab notebooks. Only days 1–3 were solved. In May 2026 a basketball notebook was accidentally pushed here from Colab. That file did not belong in this repository.

### Done

- Days 1–3 rewritten as Python modules, with the original answers preserved
- Day 4 (Camp Cleanup) implemented against the official sample
- Tests, CLI, README, and a layout that can take one new `dayXX.py` at a time

### Next days (suggested order)

| Day | Puzzle | Why it is a good next step |
| --- | --- | --- |
| 5 | Supply Stacks | Parsing + stacks. Natural follow-up to day 4. |
| 6 | Tuning Trouble | Sliding window / unique characters. Short. |
| 7 | No Space Left On Device | Directory tree walk. First “real” data structure day. |
| 8 | Treetop Tree House | 2D grid, visibility. |
| 9 | Rope Bridge | Simulate a rope on a grid. |
| 10 | Cathode-Ray Tube | Instruction clock + drawing pixels. |

Days 11–25 get heavier (monkeys, pathfinding, parsing, simulations). Tackle them after 5–10 so the package pattern is familiar: `part1` / `part2`, an example file, and a unittest.

### How to add a day

1. Save the puzzle input as `inputs/dayNN.txt`.
2. Put the official sample in `examples/dayNN.txt`.
3. Add `aoc2022/dayNN.py` with `part1` and `part2`.
4. Append the day number to `DAYS` in `aoc2022/__init__.py`.
5. Add a sample test (and a personal-input regression once you have an answer).

## Next GitHub project — BasketballElo

[BasketballElo](https://github.com/ShaneHurley/BasketballElo) is the side project that was already posted. It is much further along than the notebook that landed in this Advent of Code repo.

### What is already on GitHub

| When | What |
| --- | --- |
| 2023-10-27 | First upload. Note that most of the work lived in Colab. |
| 2026-05-19 | Same `basketballevaluatorPASTYEARS.ipynb` that was also committed here |
| 2026-05-20 | Claimed ~57% ATS; flagged as maybe overfit to that season |
| 2026-06-18 | Warning that pre-2026 data may leak |
| 2026-06-23 | Unified Colab pipeline: “no leaks, consistent 2–4% edge” |

The current main artifact is `nba_unified_pipeline_colab.ipynb`: one notebook with ~50 inlined modules (ratings, HAPM, market, calibration, staking, backtest, daily predict). Plots live in `analysis_plots/`. Older notebooks are under `old code/`, including the past-years evaluator.

There is no README. `allData.zip` is about 92 MB.

The past-years notebook in this repo (2013–2017 holdout) reported:

- 1,230 games
- spread MAE 11.69 (Elo) / 10.90 (XGBoost blend)
- 62.28% winner accuracy

That is an older, leak-prone version. The June 2026 pipeline is the one to keep.

### What to fix first in BasketballElo

1. **README** — what the model is, how to run it, what the ATS numbers mean, and the leak warnings from the commit history.
2. **Split the mega-notebook** into a real package (`ratings.py`, `backtest.py`, …) plus a thin Colab/script entry point. The notebook already labels modules; they just need to become files.
3. **Stop committing data dumps** — gitignore `allData.zip` and Drive paths; document how to place PBP / odds files locally.
4. **Lock evaluation** — one walk-forward script, no training on the test season, and a short note on the 2026-06-18 leak.
5. **Tests on tiny fixtures** — a handful of stints and a fake odds row so the pipeline can run without 92 MB of NBA history.

Do that work in the BasketballElo repo, not here.
