#!/usr/bin/env python3
"""Adversarial direct-evaluator search; never used as a proof of an upper bound."""

from __future__ import annotations

import argparse
import itertools
import json
import random
from fractions import Fraction
from pathlib import Path


def variation(values: tuple[Fraction, ...] | list[Fraction]) -> Fraction:
    return sum(
        (abs(values[index + 1] - values[index]) for index in range(len(values) - 1)),
        Fraction(0),
    )


def maximal(values: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    n = len(values)
    absolute = tuple(abs(value) for value in values)
    output = []
    for vertex in range(n):
        best: Fraction | None = None
        for radius in range(max(vertex, n - 1 - vertex) + 1):
            left = max(0, vertex - radius)
            right = min(n - 1, vertex + radius)
            average = sum(absolute[left : right + 1], Fraction(0)) / (
                right - left + 1
            )
            if best is None or average > best:
                best = average
        assert best is not None
        output.append(best)
    return tuple(output)


def ratio(values: tuple[Fraction, ...]) -> Fraction | None:
    denominator = variation(values)
    if denominator == 0:
        return None
    return variation(maximal(values)) / denominator


def search(n: int, levels: int, random_trials: int, seed: int) -> dict[str, object]:
    target = Fraction(n - 1, n)
    best = Fraction(-1)
    witness: tuple[Fraction, ...] | None = None
    checked = 0
    over_target = []

    def consider(values: tuple[Fraction, ...], family: str) -> None:
        nonlocal best, witness, checked
        value = ratio(values)
        if value is None:
            return
        checked += 1
        if value > best:
            best = value
            witness = values
        if value > target and len(over_target) < 10:
            over_target.append({
                "family": family,
                "input": [str(item) for item in values],
                "ratio": str(value),
            })

    for raw in itertools.product(range(levels), repeat=n):
        consider(tuple(Fraction(value) for value in raw), f"grid_{levels}")

    for left in range(n):
        for right in range(left, n):
            values = tuple(
                Fraction(1 if left <= index <= right else 0) for index in range(n)
            )
            consider(values, "interval_indicator")
    for first in range(n):
        for second in range(first + 1, n):
            for first_height, second_height in ((1, 2), (2, 1), (1, 3), (3, 1)):
                values = [Fraction(0) for _ in range(n)]
                values[first] = Fraction(first_height)
                values[second] = Fraction(second_height)
                consider(tuple(values), "two_spike")

    rng = random.Random(seed)
    for _ in range(random_trials):
        denominator = rng.randint(1, 19)
        values = tuple(
            Fraction(rng.randint(0, 37), denominator) for _ in range(n)
        )
        consider(values, "seeded_random_rational")

    endpoint = tuple(Fraction(1 if index == 0 else 0) for index in range(n))
    endpoint_ratio = ratio(endpoint)
    return {
        "n": n,
        "target": str(target),
        "levels": levels,
        "random_trials": random_trials,
        "seed": seed,
        "nonconstant_inputs_checked": checked,
        "largest_ratio": str(best),
        "first_largest_witness": None if witness is None else [str(x) for x in witness],
        "endpoint_point_mass_ratio": str(endpoint_ratio),
        "strict_over_target_count_retained": len(over_target),
        "strict_over_target_candidates": over_target,
        "interpretation": "counterexample search only; absence is not an upper-bound proof",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--levels", type=int, default=2)
    parser.add_argument("--random-trials", type=int, default=20000)
    parser.add_argument("--seed", type=int, default=20260830)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    rendered = json.dumps(
        search(args.n, args.levels, args.random_trials, args.seed), indent=2
    ) + "\n"
    if args.output is not None:
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
