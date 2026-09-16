#!/usr/bin/env python3
"""Extended exact factor-cycle and terminal-run tests for H=F^3.

The terminal-run patterns were formulated from i<=6 and then tested without
revision at the new held-out values i=7,8.  This remains finite evidence for
the all-length single-cycle assertion.
"""

from functools import cache

from research_block_transducer import local_rule
from research_three_step_factors import path_counts, valid_left, valid_right


@cache
def cached_rule(window):
    return local_rule(window)


def image(word):
    padded = (0, 0) + tuple(word) + (0, 0)
    return tuple(cached_rule(padded[j:j + 5]) for j in range(len(word)))


def circular_runs(values):
    runs = []
    for value in values:
        if runs and runs[-1][0] == value:
            runs[-1] = value, runs[-1][1] + 1
        else:
            runs.append((value, 1))
    if len(runs) > 1 and runs[0][0] == runs[-1][0]:
        runs[0] = runs[0][0], runs[0][1] + runs[-1][1]
        runs.pop()
    return tuple(runs)


def expected_runs(previous_count, side):
    offset = -1 if side == "left" else 1
    runs = (
        (1, previous_count),
        (9, previous_count + offset),
        (13, 1),
        (14, 1),
        (6, previous_count + offset),
        (2, previous_count),
        (15, 1),
    )
    return tuple(run for run in runs if run[1])


def check_factor(i, side):
    a, b = path_counts(i)
    if side == "left":
        initial, period, validator = (1,) * i, a, valid_left
    else:
        initial, period, validator = (3,) + (1,) * i, b, valid_right

    state = initial
    terminal_values = []
    for q in range(period):
        assert validator(state)
        if q:
            assert state != initial
        if i:
            terminal_values.append(state[-1])
        state = image(state)
    assert state == initial

    if i:
        previous = path_counts(i - 1)[0 if side == "left" else 1]
        runs = circular_runs(terminal_values)
        assert runs == expected_runs(previous, side)
    else:
        runs = ()
    return period, runs


if __name__ == "__main__":
    for i in range(9):
        left_period, left_runs = check_factor(i, "left")
        right_period, right_runs = check_factor(i, "right")
        print(
            f"i={i} left_period={left_period} right_period={right_period} "
            f"left_runs={left_runs} right_runs={right_runs}"
        )
    print(f"cached_local_windows={cached_rule.cache_info().currsize}")
    print("certificate=PASS scope=exact_factor_cycles_i_0_through_8")
