#!/usr/bin/env python3
"""Exact Lemma 2.2 enumeration for the r=12 residual instances.

Every number in this computation is a fractions.Fraction.  The candidate
times are precisely the three families in Zhang's Lemma 2.2, restricted to
[0,1); hence taking the maximum over them computes LR(V) exactly.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


RESIDUAL_PAIRS = (
    tuple((46, w) for w in range(46, 51))
    + tuple((47, w) for w in range(47, 49))
    + tuple((48, w) for w in range(48, 51))
    + tuple((50, w) for w in range(50, 57))
    + tuple((51, w) for w in range(51, 54))
)
TEST_PAIRS = ((14, 24),) + RESIDUAL_PAIRS


def speeds(n: int, w: int) -> tuple[int, ...]:
    return tuple(v for v in range(1, n) if v != 12) + (w,)


def breakpoints(values: tuple[int, ...]) -> set[Fraction]:
    """Return exactly the finite set T(V) from Lemma 2.2."""
    points: set[Fraction] = set()
    ordered = tuple(sorted(values))

    # Peaks of a single distance-to-integer constraint.
    for v in ordered:
        points.update(Fraction(2 * a + 1, 2 * v) for a in range(v))

    # Crossings of two constraints: (v+w)t or (w-v)t is integral.
    for j, w in enumerate(ordered):
        for v in ordered[:j]:
            points.update(Fraction(b, v + w) for b in range(v + w))
            points.update(Fraction(b, w - v) for b in range(w - v))
    return points


def nearest_integer_distance(x: Fraction) -> Fraction:
    residue = x.numerator % x.denominator
    return Fraction(min(residue, x.denominator - residue), x.denominator)


def exact_lr(n: int, w: int) -> dict[str, object]:
    values = speeds(n, w)
    points = breakpoints(values)
    best_value = Fraction(-1)
    best_time = Fraction(0)
    active: tuple[int, ...] = ()

    for t in points:
        distances = tuple((nearest_integer_distance(v * t), v) for v in values)
        value = min(item[0] for item in distances)
        if value > best_value or (value == best_value and t < best_time):
            best_value = value
            best_time = t
            active = tuple(v for d, v in distances if d == value)

    return {
        "n": n,
        "w": w,
        "speed_count": len(values),
        "breakpoint_count": len(points),
        "lr": f"{best_value.numerator}/{best_value.denominator}",
        "attaining_time": f"{best_time.numerator}/{best_time.denominator}",
        "active_speeds": list(active),
        "one_over_n": f"1/{n}",
        "comparison_to_one_over_n": (
            "equal"
            if best_value == Fraction(1, n)
            else "greater"
            if best_value > Fraction(1, n)
            else "less"
        ),
    }


def main() -> None:
    results = [exact_lr(n, w) for n, w in TEST_PAIRS]
    payload = {
        "method": "Exact enumeration of all three breakpoint families in Lemma 2.2",
        "arithmetic": "Python fractions.Fraction only; no floating point",
        "pair_count": len(results),
        "positive_control": [14, 24],
        "residual_pairs": [list(pair) for pair in RESIDUAL_PAIRS],
        "results": results,
    }
    target = Path(__file__).with_name("lr_breakpoints_results.json")
    target.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
