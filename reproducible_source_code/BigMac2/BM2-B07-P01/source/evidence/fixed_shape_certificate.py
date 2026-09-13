#!/usr/bin/env python3
"""Exact checks for the two non-admissible residue families.

The mathematical proof that the displayed word formulae hold for every k is
in ``evidence/fixed_shape_proof.md``.  This script independently checks the
mex recurrence, the universal signature tables, and agreement with a direct
recurrence computation for any finite range requested by the auditor.  It is
supporting exact computation, not by itself an all-k proof.
"""

from __future__ import annotations

import argparse


Word = tuple[int, ...]
Signature = tuple[int | None, int | None, int | None, int]

B: Word = tuple(map(int, "0011021"))
E: Word = tuple(map(int, "0011223"))
A: Word = tuple(map(int, "0210210"))
C: Word = tuple(map(int, "0110210"))
D: Word = tuple(map(int, "011021"))

F: Word = tuple(map(int, "32203103"))
H: Word = tuple(map(int, "1001102"))
I: Word = tuple(map(int, "1021021"))
J: Word = tuple(map(int, "02"))


SIG4: set[Signature] = {
    (None, None, None, 0),
    (0, None, None, 1),
    (0, 0, None, 1),
    (0, 0, 0, 1),
    (0, 0, 2, 1),
    (0, 2, None, 1),
    (0, 2, 2, 1),
    (1, None, None, 0),
    (1, 0, None, 2),
    (1, 0, 0, 2),
    (1, 1, None, 0),
    (1, 1, 0, 2),
    (1, 1, 1, 0),
    (1, 1, 3, 0),
    (1, 3, 0, 2),
    (2, 0, 1, 3),
    (2, 1, None, 0),
    (2, 1, 1, 0),
    (2, 2, 1, 0),
    (3, 1, 0, 2),
}

SIG0: set[Signature] = {
    (None, None, None, 0),
    (0, None, None, 1),
    (0, 0, None, 1),
    (0, 0, 0, 1),
    (0, 0, 2, 1),
    (0, 0, 3, 1),
    (0, 2, None, 1),
    (0, 2, 2, 1),
    (0, 3, 2, 1),
    (1, None, None, 0),
    (1, 0, None, 2),
    (1, 0, 0, 2),
    (1, 0, 3, 2),
    (1, 1, None, 0),
    (1, 1, 0, 2),
    (1, 1, 1, 0),
    (1, 2, 0, 3),
    (2, 1, None, 0),
    (2, 1, 0, 3),
    (2, 1, 1, 0),
    (2, 1, 2, 0),
    (2, 2, 1, 0),
    (3, 0, 1, 2),
    (3, 2, 1, 0),
    (3, 3, 1, 0),
}


def mex(values: set[int]) -> int:
    ans = 0
    while ans in values:
        ans += 1
    return ans


def words(residue: int, k: int) -> tuple[int, int, Word, Word]:
    """Return c, q, preperiod word U, and eventual period word W."""
    if residue == 4:
        if k < 1:
            raise ValueError("c=7k+4 requires k>=1")
        c = 7 * k + 4
        q = c + 3
        return c, q, B * k + E, A + C * (k - 1) + D
    if residue == 0:
        if k < 2:
            raise ValueError("c=7k requires k>=2 in the problem domain")
        c = 7 * k
        q = c + 8
        return c, q, B * k + F, H * (k - 1) + I + J
    raise ValueError("residue must be 0 or 4")


def formula_value(residue: int, k: int, n: int) -> int:
    c, q, prefix, period = words(residue, k)
    assert len(prefix) == q and len(period) == c + 2
    if n < q:
        return prefix[n]
    return period[(n - q) % len(period)]


def value_getter(residue: int, k: int):
    """Build the finite words once and return their O(1) value lookup."""
    c, q, prefix, period = words(residue, k)

    def value(n: int) -> int:
        return prefix[n] if n < q else period[(n - q) % len(period)]

    return c, q, prefix, period, value


def formula_signatures(residue: int, k: int) -> set[Signature]:
    c, q, _, period, value = value_getter(residue, k)
    # Before q+c all c-predecessors have not both entered the tail.  From
    # q+c onward every entry in a signature is in the tail, so one period
    # covers every remaining signature.
    stop = q + c + len(period)
    signatures: set[Signature] = set()
    for n in range(stop):
        predecessors: list[int | None] = []
        for move in (2, 5, c):
            predecessors.append(
                value(n - move) if n >= move else None
            )
        signatures.add((*predecessors, value(n)))
    return signatures


def direct_values(c: int, stop: int) -> list[int]:
    values: list[int] = []
    for n in range(stop):
        options = {values[n - move] for move in (2, 5, c) if n >= move}
        values.append(mex(options))
    return values


def verify_case(residue: int, k: int) -> None:
    c, q, _, period, value = value_getter(residue, k)
    stop = q + c + len(period)
    expected_signatures = SIG4 if residue == 4 else SIG0
    actual_signatures = formula_signatures(residue, k)
    assert actual_signatures == expected_signatures

    for before_2, before_5, before_c, claimed in actual_signatures:
        options = {x for x in (before_2, before_5, before_c) if x is not None}
        assert claimed == mex(options)

    direct = direct_values(c, stop)
    formula = [value(n) for n in range(stop)]
    assert formula == direct
    assert value(q) == value(q + c + 2)
    assert value(0) == 0
    assert value(c + 2) == (3 if residue == 4 else 2)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-k", type=int, default=200)
    args = parser.parse_args()
    if args.max_k < 2:
        raise SystemExit("--max-k must be at least 2")

    cases = 0
    for k in range(1, args.max_k + 1):
        verify_case(4, k)
        cases += 1
    for k in range(2, args.max_k + 1):
        verify_case(0, k)
        cases += 1

    print(f"verified {cases} exact parameter instances through k={args.max_k}")
    print(f"rho=4 universal signature count: {len(SIG4)}")
    print(f"rho=0 universal signature count: {len(SIG0)}")
    print("all formula, recurrence, signature, and mismatch checks passed")


if __name__ == "__main__":
    main()
