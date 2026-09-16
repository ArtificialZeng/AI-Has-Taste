#!/usr/bin/env python3
"""Independent exact interval-cover certificates for the saved LR values.

This script deliberately does not import, invoke, or read lr_breakpoints.py or
lr_breakpoints_results.json.  The cases to be certified are encoded below.
For q <= 1/2 and an integer speed v,

    {t in [0,1] : ||v t|| <= q}

is the union, for 0 <= k <= v, of the closed rational intervals
[(k-q)/v,(k+q)/v] intersected with [0,1].  A greedy chain of such intervals
covering [0,1] proves LR <= q.  Direct exact evaluation at the encoded time
proves LR >= q.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


# (n, w, asserted LR numerator, asserted LR denominator,
#  attaining-time numerator, attaining-time denominator)
# These constants are intentionally independent of the breakpoint program.
CASES = (
    (14, 24, 1, 14, 1, 14),
    (46, 46, 2, 59, 5, 59),
    (46, 47, 2, 61, 5, 61),
    (46, 48, 2, 59, 5, 59),
    (46, 49, 2, 59, 5, 59),
    (46, 50, 2, 59, 5, 59),
    (47, 47, 2, 61, 5, 61),
    (47, 48, 2, 59, 5, 59),
    (48, 48, 2, 61, 5, 61),
    (48, 49, 2, 65, 27, 65),
    (48, 50, 2, 61, 5, 61),
    (50, 50, 2, 65, 27, 65),
    (50, 51, 2, 65, 27, 65),
    (50, 52, 2, 65, 27, 65),
    (50, 53, 2, 67, 28, 67),
    (50, 54, 2, 65, 27, 65),
    (50, 55, 2, 65, 27, 65),
    (50, 56, 2, 65, 27, 65),
    (51, 51, 2, 65, 27, 65),
    (51, 52, 2, 65, 27, 65),
    (51, 53, 2, 67, 28, 67),
)


@dataclass(frozen=True)
class Interval:
    left: Fraction
    right: Fraction
    speed: int
    integer: int


def fraction_text(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}"


def speed_set(n: int, w: int) -> tuple[int, ...]:
    values = tuple(v for v in range(1, n) if v != 12) + (w,)
    assert len(values) == n - 1
    assert len(set(values)) == n - 1
    return values


def distance_to_integer(x: Fraction) -> Fraction:
    residue = x.numerator % x.denominator
    return Fraction(min(residue, x.denominator - residue), x.denominator)


def sublevel_intervals(values: tuple[int, ...], q: Fraction) -> list[Interval]:
    assert 0 <= q <= Fraction(1, 2)
    intervals: list[Interval] = []
    for v in values:
        for k in range(v + 1):
            left = max(Fraction(0), Fraction(k, v) - q / v)
            right = min(Fraction(1), Fraction(k, v) + q / v)
            if left <= right:
                intervals.append(Interval(left, right, v, k))
    return intervals


def greedy_cover(intervals: list[Interval]) -> list[Interval]:
    """Return a labeled exact chain covering [0,1], or raise on a gap."""
    ordered = sorted(intervals, key=lambda z: (z.left, -z.right, z.speed, z.integer))
    chain: list[Interval] = []
    frontier = Fraction(0)
    scan = 0

    while frontier < 1:
        best: Interval | None = None
        while scan < len(ordered) and ordered[scan].left <= frontier:
            candidate = ordered[scan]
            if best is None or (candidate.right, -candidate.speed, -candidate.integer) > (
                best.right,
                -best.speed,
                -best.integer,
            ):
                best = candidate
            scan += 1
        if best is None or best.right <= frontier:
            next_left = ordered[scan].left if scan < len(ordered) else None
            raise AssertionError(
                f"uncovered point after {fraction_text(frontier)}; next left is {next_left}"
            )
        chain.append(best)
        frontier = best.right

    assert chain[0].left == 0
    assert chain[-1].right == 1
    assert all(right.right >= left.left for right, left in zip(chain, chain[1:]))
    return chain


def interval_record(interval: Interval) -> dict[str, object]:
    return {
        "left": fraction_text(interval.left),
        "right": fraction_text(interval.right),
        "speed": interval.speed,
        "nearest_integer": interval.integer,
    }


def certify_case(case: tuple[int, int, int, int, int, int]) -> dict[str, object]:
    n, w, q_num, q_den, t_num, t_den = case
    q = Fraction(q_num, q_den)
    t = Fraction(t_num, t_den)
    values = speed_set(n, w)

    intervals = sublevel_intervals(values, q)
    chain = greedy_cover(intervals)

    distances = [(v, distance_to_integer(v * t)) for v in values]
    attained = min(d for _, d in distances)
    active = [v for v, d in distances if d == attained]

    assert attained == q
    comparison = "equal" if q == Fraction(1, n) else "greater" if q > Fraction(1, n) else "less"

    return {
        "n": n,
        "w": w,
        "q": fraction_text(q),
        "attaining_time": fraction_text(t),
        "one_over_n": fraction_text(Fraction(1, n)),
        "comparison_to_one_over_n": comparison,
        "upper_bound_certificate": {
            "sublevel_interval_count": len(intervals),
            "cover_chain_length": len(chain),
            "cover_chain": [interval_record(interval) for interval in chain],
            "verified_covers_closed_unit_interval": True,
        },
        "lower_bound_certificate": {
            "distances": [
                {"speed": v, "distance": fraction_text(distance)}
                for v, distance in distances
            ],
            "minimum": fraction_text(attained),
            "active_speeds": active,
            "verified_minimum_equals_q": True,
        },
        "conclusion": f"LR(V_{{{n},{w}}})={fraction_text(q)}",
    }


def main() -> None:
    records = [certify_case(case) for case in CASES]
    assert len(records) == 21
    assert records[0]["comparison_to_one_over_n"] == "equal"
    assert all(record["comparison_to_one_over_n"] == "greater" for record in records[1:])

    payload = {
        "method": "Exact closed rational interval covers plus direct exact lower witnesses",
        "independence": (
            "No import, call, or read of the breakpoint enumerator or its results; "
            "the 21 cases are encoded as constants in this file"
        ),
        "arithmetic": "Python fractions.Fraction only; no floating point",
        "logic": (
            "The cover chain proves for every t in [0,1] that some speed has "
            "distance at most q; the distance list at attaining_time has minimum q"
        ),
        "pair_count": len(records),
        "all_certificates_verified": True,
        "results": records,
    }
    target = Path(__file__).with_name("lr_interval_cover_results.json")
    target.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
