#!/usr/bin/env python3
"""Independent verifier for audit_output.json; imports no discovery code."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def ok_pair(a: int, b: int) -> bool:
    for r in range(4):
        if not ((a >> r) & 1):
            continue
        for s in range(4):
            if ((b >> s) & 1) and abs(r - s) <= 1:
                return False
    return True


LEGAL = [x for x in range(16) if all(not ((x >> r) & 3) == 3 for r in range(3))]


def independent_set_count(width: int, wanted: int, seam_test=None) -> int:
    table = {(0, 0): 1}
    for _ in range(width):
        new = {}
        for (previous, size), multiplicity in table.items():
            for current in LEGAL:
                if not ok_pair(previous, current):
                    continue
                new_size = size + current.bit_count()
                if new_size <= wanted:
                    key = (current, new_size)
                    new[key] = new.get(key, 0) + multiplicity
        table = new
    return sum(
        multiplicity
        for (last, size), multiplicity in table.items()
        if size == wanted and (seam_test is None or seam_test(last))
    )


def flip_rows(mask: int) -> int:
    answer = 0
    for r in range(4):
        if (mask >> r) & 1:
            answer |= 1 << (3 - r)
    return answer


def recompute(n: int) -> dict[str, int]:
    if n == 0:
        return {"identity": 1, "horizontal": 1, "vertical": 1, "half_turn": 1}
    return {
        "identity": independent_set_count(2 * n, 2 * n),
        "horizontal": n + 1,
        "vertical": independent_set_count(n - 1, n) if n % 2 == 0 else 0,
        "half_turn": independent_set_count(
            n, n, seam_test=lambda m: ok_pair(m, flip_rows(m))
        ),
    }


def exhaustive_square() -> dict[str, int]:
    maps = {
        "identity": lambda r, c: (r, c),
        "horizontal": lambda r, c: (3 - r, c),
        "vertical": lambda r, c: (r, 3 - c),
        "half_turn": lambda r, c: (3 - r, 3 - c),
        "quarter_turn": lambda r, c: (c, 3 - r),
        "three_quarter_turn": lambda r, c: (3 - c, r),
        "main_diagonal": lambda r, c: (c, r),
        "anti_diagonal": lambda r, c: (3 - c, 3 - r),
    }
    answer = dict.fromkeys(maps, 0)

    # Directly inspect all C(16,4)=1820 four-cell subsets.  This is independent
    # of the column-path generator in exact_audit.py.
    for bits in range(1 << 16):
        if bits.bit_count() != 4:
            continue
        cells = {(i // 4, i % 4) for i in range(16) if (bits >> i) & 1}
        if any(
            (r, c) != (s, d) and max(abs(r - s), abs(c - d)) <= 1
            for r, c in cells
            for s, d in cells
        ):
            continue
        for name, mapping in maps.items():
            answer[name] += {mapping(r, c) for r, c in cells} == cells
    return answer


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    data = json.loads(args.input.read_text())
    assert data["metadata"]["integer_arithmetic"] is True
    rows = data["rows"]
    assert [x["n"] for x in rows] == list(range(len(rows)))

    for row in rows:
        expected = recompute(row["n"])
        stored = {name: row[name] for name in expected}
        assert expected == stored, (row["n"], expected, stored)
        numerator = sum(expected.values())
        assert numerator == row["burnside_numerator"]
        assert numerator % 4 == 0 and numerator // 4 == row["a"]

    coefficients = data["recurrence"]["coefficients"]
    values = [row["a"] for row in rows]
    for n in range(10, len(values)):
        right = sum(coefficients[j - 1] * values[n - j] for j in range(1, 11))
        assert values[n] == right, (n, values[n], right)

    denominator = [1] + [-x for x in coefficients]
    numerator = [
        sum(denominator[j] * values[k - j] for j in range(k + 1))
        for k in range(9)
    ]
    assert numerator == data["recurrence"]["gf_numerator_coefficients_low_to_high"]

    d4 = exhaustive_square()
    assert d4 == data["square_n_2"]["D4_fixed"]
    assert sum(d4.values()) == 8 * data["square_n_2"]["D4_free"]
    full_group_values = values.copy()
    full_group_values[2] = sum(d4.values()) // 8
    variant = data["semantic_variant_full_board_automorphism_group"]
    recomputed_variant_residuals = []
    for n in range(10, len(values)):
        right = sum(coefficients[j - 1] * full_group_values[n - j] for j in range(1, 11))
        recomputed_variant_residuals.append({"n": n, "residual": full_group_values[n] - right})
    assert recomputed_variant_residuals == variant["recurrence_residuals"]
    assert next(x for x in recomputed_variant_residuals if x["residual"] != 0) == variant["first_failure"]
    print(f"VERIFIED rows=0..{len(rows)-1}")
    print("VERIFIED recurrence range=n=10..%d" % (len(rows) - 1))
    print("VERIFIED n=2 D2_free=%d D4_free=%d" % (
        data["square_n_2"]["D2_free"], data["square_n_2"]["D4_free"]
    ))


if __name__ == "__main__":
    main()
