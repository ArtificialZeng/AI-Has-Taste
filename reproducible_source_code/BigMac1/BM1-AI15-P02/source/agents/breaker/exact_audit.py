#!/usr/bin/env python3
"""Exact adversarial audit for OEIS A321614.

All arithmetic is integer arithmetic.  The primary implementation is a
column-mask transfer computation.  For small n a deliberately simpler
enumerator materializes every maximum placement and applies the geometric
maps cell by cell.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import sys
from pathlib import Path


ROWS = 4
MASKS = tuple(m for m in range(1 << ROWS) if not (m & (m << 1)))
POPCOUNT = {m: m.bit_count() for m in MASKS}


def compatible(left: int, right: int) -> bool:
    """No horizontal or diagonal king attack between adjacent columns."""
    danger = left | (left << 1) | (left >> 1)
    return (danger & right) == 0


COMPAT = {m: tuple(q for q in MASKS if compatible(m, q)) for m in MASKS}


def reverse4(mask: int) -> int:
    return sum(((mask >> r) & 1) << (ROWS - 1 - r) for r in range(ROWS))


def count_columns(width: int, target: int, accept_last=None) -> int:
    """Count labeled independent sets of the requested size on 4 x width."""
    if width < 0 or target < 0:
        return 0
    if width == 0:
        return int(target == 0 and (accept_last is None or accept_last(0)))
    dp = {(0, 0): 1}  # (last mask, number of kings) after zero columns
    for _ in range(width):
        nxt = {}
        for (last, used), count in dp.items():
            for mask in COMPAT[last]:
                total = used + POPCOUNT[mask]
                if total <= target:
                    nxt[(mask, total)] = nxt.get((mask, total), 0) + count
        dp = nxt
    return sum(
        count
        for (last, used), count in dp.items()
        if used == target and (accept_last is None or accept_last(last))
    )


def d2_fixed_counts(n: int) -> dict[str, int]:
    """Fixed maximum placements for id, row flip, column flip, half-turn."""
    if n < 0:
        raise ValueError("n must be nonnegative")
    identity = count_columns(2 * n, 2 * n)
    if n == 0:
        return {"identity": 1, "horizontal": 1, "vertical": 1, "half_turn": 1}

    # Row reflection: only row-pairs {0,3} are internally nonattacking;
    # choose n nonconsecutive columns from 2n.
    horizontal = n + 1

    # Column reflection: the last column of the left half must be empty.
    # Removing it leaves a 4 x (n-1) half-board carrying n kings.
    vertical = count_columns(n - 1, n) if n % 2 == 0 else 0

    # Half-turn: choose the left half and rotate it into the right half.
    # The sole new condition is compatibility across the central seam.
    half_turn = count_columns(
        n, n, accept_last=lambda m: compatible(m, reverse4(m))
    )
    return {
        "identity": identity,
        "horizontal": horizontal,
        "vertical": vertical,
        "half_turn": half_turn,
    }


def d2_free(n: int) -> int:
    fixed = d2_fixed_counts(n)
    numerator = sum(fixed.values())
    assert numerator % 4 == 0
    return numerator // 4


def placement_cells(columns: tuple[int, ...]) -> frozenset[tuple[int, int]]:
    return frozenset(
        (r, c)
        for c, mask in enumerate(columns)
        for r in range(ROWS)
        if (mask >> r) & 1
    )


def enumerate_columns(width: int, target: int):
    """Materialize paths for the independent small-n cross-check only."""
    columns = []

    def visit(last: int, used: int):
        col = len(columns)
        if col == width:
            if used == target:
                yield tuple(columns)
            return
        # Each remaining column contains at most two kings.
        remaining_after = width - col - 1
        for mask in COMPAT[last]:
            now = used + POPCOUNT[mask]
            if now > target or now + 2 * remaining_after < target:
                continue
            columns.append(mask)
            yield from visit(mask, now)
            columns.pop()

    yield from visit(0, 0)


def transform(cells: frozenset[tuple[int, int]], width: int, name: str):
    if name == "identity":
        f = lambda r, c: (r, c)
    elif name == "horizontal":
        f = lambda r, c: (ROWS - 1 - r, c)
    elif name == "vertical":
        f = lambda r, c: (r, width - 1 - c)
    elif name == "half_turn":
        f = lambda r, c: (ROWS - 1 - r, width - 1 - c)
    elif name == "quarter_turn":
        assert width == ROWS
        f = lambda r, c: (c, ROWS - 1 - r)
    elif name == "three_quarter_turn":
        assert width == ROWS
        f = lambda r, c: (ROWS - 1 - c, r)
    elif name == "main_diagonal":
        assert width == ROWS
        f = lambda r, c: (c, r)
    elif name == "anti_diagonal":
        assert width == ROWS
        f = lambda r, c: (ROWS - 1 - c, ROWS - 1 - r)
    else:
        raise ValueError(name)
    return frozenset(f(r, c) for r, c in cells)


def brute_fixed_counts(n: int, square_group: bool = False) -> dict[str, int]:
    width = 2 * n
    names = ["identity", "horizontal", "vertical", "half_turn"]
    if square_group:
        if width != ROWS:
            raise ValueError("the D4 square group only applies to n=2")
        names.extend(
            [
                "quarter_turn",
                "three_quarter_turn",
                "main_diagonal",
                "anti_diagonal",
            ]
        )
    fixed = dict.fromkeys(names, 0)
    for columns in enumerate_columns(width, 2 * n):
        cells = placement_cells(columns)
        for name in names:
            fixed[name] += transform(cells, width, name) == cells
    return fixed


COEFFICIENTS = (12, -54, 98, 17, -346, 505, -210, -120, 126, -27)
OEIS_PREFIX = (
    1,
    4,
    23,
    106,
    473,
    1939,
    7618,
    28703,
    105112,
    375597,
    1316944,
    4544124,
    15474559,
    52108212,
    173799309,
    574908646,
    1888125243,
    6162032375,
    19998659760,
    64584817367,
    207655073310,
    665017743665,
)


def recurrence_residual(values: list[int], n: int) -> int:
    return values[n] - sum(COEFFICIENTS[j - 1] * values[n - j] for j in range(1, 11))


def multiply_polynomials(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def barker_denominator_from_factors() -> list[int]:
    factors = [
        [1, -1],
        [1, -1],
        [1, -3],
        [1, -3],
        [1, -3, 1],
        [1, -1, -1],
        [1, 0, -3],
    ]
    product = [1]
    for factor in factors:
        product = multiply_polynomials(product, factor)
    return product


def run(limit: int, brute_limit: int) -> dict:
    rows = []
    values = []
    for n in range(limit + 1):
        fixed = d2_fixed_counts(n)
        value = sum(fixed.values()) // 4
        values.append(value)
        rows.append({"n": n, **fixed, "burnside_numerator": sum(fixed.values()), "a": value})

    brute = []
    for n in range(min(brute_limit, limit) + 1):
        fixed = brute_fixed_counts(n)
        assert fixed == d2_fixed_counts(n), (n, fixed, d2_fixed_counts(n))
        brute.append({"n": n, **fixed})

    d4 = brute_fixed_counts(2, square_group=True)
    d4_free = sum(d4.values()) // 8
    d2_at_square = d2_free(2)

    expected_denominator = [1] + [-c for c in COEFFICIENTS]
    factored_denominator = barker_denominator_from_factors()
    assert expected_denominator == factored_denominator

    # Q(x) A(x) from the computed prefix.  Barker's displayed numerator is
    # (1-2x)(1-6x+17x^2-18x^3-2x^4+7x^5+6x^6-3x^7).
    gf_numerator = [
        sum(expected_denominator[j] * values[k - j] for j in range(k + 1))
        for k in range(10)
    ]
    displayed_numerator = multiply_polynomials(
        [1, -2], [1, -6, 17, -18, -2, 7, 6, -3]
    )
    assert gf_numerator == displayed_numerator + [0]

    residuals = [
        {"n": n, "residual": recurrence_residual(values, n)}
        for n in range(10, limit + 1)
    ]
    first_failure = next((x for x in residuals if x["residual"] != 0), None)

    # Adversarial semantic variant: at n=2 quotient by all eight geometric
    # symmetries of the square, not by the four-element rectangle group used
    # by OEIS.  All other n are nonsquare and unchanged.
    full_automorphism_values = values.copy()
    full_automorphism_values[2] = d4_free
    full_group_residuals = [
        {"n": n, "residual": recurrence_residual(full_automorphism_values, n)}
        for n in range(10, limit + 1)
    ]
    first_full_group_failure = next(
        (x for x in full_group_residuals if x["residual"] != 0), None
    )

    return {
        "metadata": {
            "python": sys.version,
            "platform": platform.platform(),
            "integer_arithmetic": True,
            "random_seed": None,
            "limit": limit,
            "brute_limit": brute_limit,
        },
        "column_masks": list(MASKS),
        "rows": rows,
        "oeis_prefix_matches": values[: len(OEIS_PREFIX)] == list(OEIS_PREFIX),
        "first_oeis_prefix_mismatch": next(
            (
                {"n": n, "computed": values[n], "oeis": OEIS_PREFIX[n]}
                for n in range(min(len(values), len(OEIS_PREFIX)))
                if values[n] != OEIS_PREFIX[n]
            ),
            None,
        ),
        "brute_crosscheck": brute,
        "square_n_2": {
            "D2_fixed": d2_fixed_counts(2),
            "D2_free": d2_at_square,
            "D4_fixed": d4,
            "D4_free": d4_free,
        },
        "recurrence": {
            "coefficients": list(COEFFICIENTS),
            "validity_claim": "n >= 10 (OEIS writes n > 9)",
            "denominator_coefficients_low_to_high": expected_denominator,
            "factor_product_coefficients_low_to_high": factored_denominator,
            "gf_numerator_coefficients_low_to_high": gf_numerator[:-1],
            "residuals": residuals,
            "first_failure": first_failure,
        },
        "semantic_variant_full_board_automorphism_group": {
            "changed_term": {"n": 2, "D2_value": d2_at_square, "D4_value": d4_free},
            "recurrence_residuals": full_group_residuals,
            "first_failure": first_full_group_failure,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=60)
    parser.add_argument("--brute-limit", type=int, default=6)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.limit < 21:
        parser.error("--limit must be at least 21 to audit the complete OEIS prefix")
    if not 0 <= args.brute_limit <= 8:
        parser.error("--brute-limit must be in 0..8")

    result = run(args.limit, args.brute_limit)
    encoded = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode()
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_bytes(encoded)
        digest = hashlib.sha256(encoded).hexdigest()
        print(f"wrote={args.output}")
        print(f"sha256={digest}")
    else:
        sys.stdout.buffer.write(encoded)

    sq = result["square_n_2"]
    print(f"oeis_prefix_matches={result['oeis_prefix_matches']}")
    print(f"recurrence_first_failure={result['recurrence']['first_failure']}")
    print(f"n=2_D2_free={sq['D2_free']} n=2_D4_free={sq['D4_free']}")


if __name__ == "__main__":
    main()
