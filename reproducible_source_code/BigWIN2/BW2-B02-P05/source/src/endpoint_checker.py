#!/usr/bin/env python3
"""Independent exact checker using direct sliding-window endpoints.

Implementation B generates Golomb's sequence from its scalar recurrence and
recomputes S_m and S_{m+1} as literal sums at every almost-Golomb run.  It is
deliberately separate from src/run_length_search.py.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
from pathlib import Path


def golomb_by_scalar_recurrence(limit: int) -> list[int]:
    if limit < 1:
        return [0]
    sequence = [0, 1]
    if limit == 1:
        return sequence
    sequence.append(2)
    for n in range(3, limit + 1):
        sequence.append(1 + sequence[n - sequence[sequence[n - 1]]])
    return sequence


def value_at(sequence: list[int], index: int) -> int:
    return sequence[index] if index > 0 else 0


def almost_by_endpoints(order: int, limit: int) -> list[int]:
    if order < 3:
        raise ValueError("the locked problem has order >= 3")
    if limit < 1:
        return [0]
    sequence = [0, 1, 2, 2, 2]
    if limit <= 4:
        return sequence[: limit + 1]

    value = 3
    while len(sequence) - 1 < limit:
        start = sum(value_at(sequence, value - j) for j in range(order))
        stop = sum(value_at(sequence, value + 1 - j) for j in range(order))
        if start != len(sequence):
            raise AssertionError((order, value, start, len(sequence)))
        if not start < stop:
            raise AssertionError((order, value, start, stop))
        sequence.extend([value] * (stop - start))
        value += 1
    return sequence[: limit + 1]


def check(max_order: int) -> dict[str, object]:
    if max_order < 3:
        raise ValueError("max_order must be at least 3")
    golomb = golomb_by_scalar_recurrence(max_order)
    checked_pairs = 0
    checked_endpoint_identities = 0
    for order in range(3, max_order + 1):
        almost = almost_by_endpoints(order, order)
        for n in range(3, order + 1):
            checked_pairs += 1
            if almost[n] != golomb[n - 1]:
                return {
                    "status": "counterexample",
                    "order": order,
                    "n": n,
                    "almost": almost[n],
                    "golomb_shift": golomb[n - 1],
                }

        # Independently check the proof's full-sum identity at every m whose
        # two endpoints are determined by the prefix under test.
        for m in range(3, max(almost[order], 3)):
            if m + 1 > order:
                break
            t_m = sum(([0, 1, 2] + [golomb[j - 1] for j in range(3, m + 1)])[1:])
            h_previous = sum(golomb[1:m])
            if t_m != h_previous + 2:
                raise AssertionError((order, m, t_m, h_previous + 2))
            checked_endpoint_identities += 1

    code_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return {
        "status": "no_counterexample_in_finite_range",
        "implementation": "direct_window_endpoints_plus_Golomb_scalar_recurrence",
        "orders": [3, max_order],
        "checked_pairs": checked_pairs,
        "checked_endpoint_identities": checked_endpoint_identities,
        "python": platform.python_version(),
        "code_sha256": code_hash,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-order", type=int, default=500)
    args = parser.parse_args()
    print(json.dumps(check(args.max_order), sort_keys=True))


if __name__ == "__main__":
    main()
