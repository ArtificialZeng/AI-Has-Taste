#!/usr/bin/env python3
"""Exact counterexample search using telescoped almost-Golomb run lengths.

This is discovery implementation A.  It constructs Golomb's sequence by
self-describing run expansion and constructs each almost-Golomb sequence from
L_m = a(m+1)-a(m+1-r).  No floating-point arithmetic is used.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
from pathlib import Path


def golomb_by_runs(limit: int) -> list[int]:
    if limit < 1:
        return [0]
    if limit == 1:
        return [0, 1]
    # Complete runs of 1 and 2; thereafter G(value) is already available.
    values = [0, 1, 2, 2]
    value = 3
    while len(values) - 1 < limit:
        values.extend([value] * values[value])
        value += 1
    return values[: limit + 1]


def almost_by_run_lengths(order: int, limit: int) -> list[int]:
    if order < 3:
        raise ValueError("the locked problem has order >= 3")
    if limit < 1:
        return [0]
    values = [0, 1, 2, 2, 2]
    if limit <= 4:
        return values[: limit + 1]

    next_position = 5
    value = 3
    while len(values) - 1 < limit:
        if len(values) != next_position:
            raise AssertionError("run does not start at the first undefined position")
        left_index = value + 1 - order
        left_value = values[left_index] if left_index > 0 else 0
        run_length = values[value + 1] - left_value
        if not 1 <= run_length <= order:
            raise AssertionError((order, value, run_length))
        values.extend([value] * run_length)
        next_position += run_length
        value += 1
    return values[: limit + 1]


def search(max_order: int) -> dict[str, object]:
    if max_order < 3:
        raise ValueError("max_order must be at least 3")
    golomb = golomb_by_runs(max_order)
    checked_pairs = 0
    for order in range(3, max_order + 1):
        almost = almost_by_run_lengths(order, order)
        for n in range(3, order + 1):
            checked_pairs += 1
            if almost[n] != golomb[n - 1]:
                return {
                    "status": "counterexample",
                    "order": order,
                    "n": n,
                    "almost": almost[n],
                    "golomb_shift": golomb[n - 1],
                    "checked_pairs_before_failure": checked_pairs - 1,
                }
    code_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return {
        "status": "no_counterexample_in_finite_range",
        "implementation": "telescoped_run_lengths_plus_Golomb_run_expansion",
        "orders": [3, max_order],
        "checked_pairs": checked_pairs,
        "python": platform.python_version(),
        "code_sha256": code_hash,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-order", type=int, default=2000)
    args = parser.parse_args()
    print(json.dumps(search(args.max_order), sort_keys=True))


if __name__ == "__main__":
    main()
