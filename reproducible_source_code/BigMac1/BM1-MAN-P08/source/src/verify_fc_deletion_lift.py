#!/usr/bin/env python3
"""Independent exact verifier for the FC deletion-lift certificate."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


if not __debug__:
    raise SystemExit("verification requires assertions; do not run Python with -O")


EXPECTED_SEEDS = {4: (8, 11), 5: (7, 13), 6: (8, 25)}


def choose(n: int, r: int) -> int:
    if not (0 <= r <= n):
        return 0
    r = min(r, n - r)
    value = 1
    for j in range(1, r + 1):
        value = value * (n - r + j) // j
    return value


def require_int(value: object, label: str) -> int:
    if type(value) is not int:
        raise ValueError(f"{label} is not an integer")
    return value


def verify(path: Path) -> None:
    data = json.loads(path.read_text())
    if data.get("schema_version") != 1:
        raise ValueError("unsupported schema")
    rows_by_k = data.get("rows")
    if not isinstance(rows_by_k, dict) or set(rows_by_k) != {"4", "5", "6"}:
        raise ValueError("missing or extra k-sequences")

    strict_improvements: list[tuple[int, int, int, int]] = []
    headline_bounds: set[tuple[int, int, int]] = set()
    for k, (start, seed) in EXPECTED_SEEDS.items():
        rows = rows_by_k[str(k)]
        if not isinstance(rows, list) or not rows:
            raise ValueError(f"empty row list for k={k}")
        previous = None
        expected_n = start
        for index, row in enumerate(rows):
            if not isinstance(row, dict):
                raise ValueError("row is not an object")
            n = require_int(row.get("n"), "n")
            a = require_int(
                row.get("non_fc_edge_upper_bound"), "non_fc_edge_upper_bound"
            )
            threshold = require_int(
                row.get("fc_threshold_upper_bound"), "fc_threshold_upper_bound"
            )
            if n != expected_n:
                raise ValueError(f"nonconsecutive n for k={k}")
            if index == 0:
                if a != seed:
                    raise ValueError(f"wrong seed for k={k}")
            else:
                expected = (n * previous) // (n - k)
                if a != expected:
                    raise ValueError(f"recurrence mismatch for k={k}, n={n}")
                # The summed deletion inequalities are
                # (n-k)|H| <= n*a_{n-1}.
                if (n - k) * a > n * previous:
                    raise ValueError("rounded bound violates deletion inequality")
                if (n - k) * (a + 1) <= n * previous:
                    raise ValueError("rounded bound is not maximal")
            if threshold != a + 1:
                raise ValueError("threshold/off-by-one mismatch")
            if a > choose(n, k):
                raise ValueError("bound exceeds the entire k-uniform universe")

            direct_num = seed * choose(n, k)
            direct_den = choose(start, k)
            direct_floor_threshold = direct_num // direct_den + 1
            if row.get("direct_seed_floor_threshold") != direct_floor_threshold:
                raise ValueError("direct seed comparison mismatch")
            if threshold < direct_floor_threshold:
                strict_improvements.append(
                    (k, n, threshold, direct_floor_threshold)
                )
            headline_bounds.add((k, n, threshold))

            if k == 4:
                closed = (choose(n, 4) + n) // 7
                if a != closed or row.get("closed_form_non_fc_bound") != closed:
                    raise ValueError(f"closed form mismatch at n={n}")
            previous = a
            expected_n += 1

    required = {(4, 9, 20), (4, 10, 32), (5, 8, 35)}
    if not required <= headline_bounds:
        raise ValueError("expected headline improvements are absent")

    # Independent infinite closed-form audit for k=4.  This does not replace
    # the seven-residue proof, but catches transcription and boundary errors.
    a = 11
    for n in range(9, 10001):
        a = (n * a) // (n - 4)
        if a != (choose(n, 4) + n) // 7:
            raise ValueError(f"extended k=4 identity failed at n={n}")

    print("CERTIFICATE STRUCTURE: PASS")
    print("k=4 closed form through n=10000: PASS")
    for item in sorted(strict_improvements)[:12]:
        k, n, new, direct = item
        print(f"strict lift: k={k}, n={n}, new={new}, direct={direct}")
    print("FC DELETION-LIFT VERIFICATION: PASS")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args()
    verify(args.certificate)


if __name__ == "__main__":
    main()
