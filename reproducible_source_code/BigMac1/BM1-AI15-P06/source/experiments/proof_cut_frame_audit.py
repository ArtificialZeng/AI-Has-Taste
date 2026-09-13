#!/usr/bin/env python3
"""Fail-closed exact audit for finite calculations in builder_notes.md.

This is an audit aid, not a proof of the full Kusner n=5 instance.  It uses
only the standard library.  Every decisive condition is an explicit branch
and remains active under ``python -O``.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import NoReturn


M = 11
LABELS = tuple(range(M))


class AuditError(Exception):
    """A failed exact-arithmetic audit condition."""


def fail(message: str) -> NoReturn:
    raise AuditError(message)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def centered_inner(s: frozenset[int], t: frozenset[int]) -> Fraction:
    return Fraction(M * len(s & t) - len(s) * len(t), M)


def cut_entry(s: frozenset[int], r: int, u: int) -> int:
    return int((r in s) != (u in s))


def all_canonical_cuts() -> list[frozenset[int]]:
    """One representative per unordered cut, chosen to omit label 10."""
    return [
        frozenset(i for i in range(M - 1) if mask & (1 << i))
        for mask in range(1, 1 << (M - 1))
    ]


def check_double_centering(cuts: list[frozenset[int]]) -> None:
    for s in cuts:
        size = len(s)
        row_means = [Fraction(size if r not in s else M - size, M) for r in LABELS]
        grand_mean = Fraction(2 * size * (M - size), M * M)
        v = [Fraction(int(r in s), 1) - Fraction(size, M) for r in LABELS]
        for r in LABELS:
            for u in LABELS:
                lhs = (
                    Fraction(cut_entry(s, r, u), 1)
                    - row_means[r]
                    - row_means[u]
                    + grand_mean
                )
                rhs = -2 * v[r] * v[u]
                require(lhs == rhs, f"double-centering failure: S={sorted(s)}, r={r}, u={u}")


def check_nonorthogonality(cuts: list[frozenset[int]]) -> int:
    checked = 0
    for i, s in enumerate(cuts):
        for t in cuts[i:]:
            require(centered_inner(s, t) != 0, f"orthogonal cuts: {sorted(s)}, {sorted(t)}")
            checked += 1
    return checked


def check_nested_positivity() -> int:
    checked = 0
    for s_size in range(1, M - 1):
        for t_size in range(s_size + 1, M):
            value = Fraction(s_size * (M - t_size), M)
            require(value > 0, f"nested inner product not positive: {s_size}, {t_size}")
            checked += 1
    return checked


def verify_uniform_decomposition(blocks: list[frozenset[int]], weight: Fraction) -> None:
    for pair_index, (r, u) in enumerate(itertools.combinations(LABELS, 2)):
        distance = sum(
            (weight * cut_entry(block, r, u) for block in blocks),
            Fraction(0, 1),
        )
        require(distance == 1, f"uniform-decomposition failure at pair {pair_index}: {distance}")


def check_explicit_decompositions() -> None:
    singletons = [frozenset({r}) for r in LABELS]
    verify_uniform_decomposition(singletons, Fraction(1, 2))

    residues = frozenset({1, 3, 4, 5, 9})
    blocks = [frozenset((x + shift) % M for x in residues) for shift in LABELS]
    require(len(set(blocks)) == M, "quadratic-residue blocks are not distinct")
    for r in LABELS:
        require(sum(r in block for block in blocks) == 5, f"wrong QR replication for label {r}")
    for r, u in itertools.combinations(LABELS, 2):
        require(
            sum(r in block and u in block for block in blocks) == 2,
            f"wrong QR pair incidence for labels {r},{u}",
        )
    verify_uniform_decomposition(blocks, Fraction(1, 6))


def check_private_direction_diagnostic() -> None:
    table = (
        (0, 1, 0, 0),
        (2, 0, 1, 1),
        (2, 1, 1, 1),
        (0, 1, 0, 0),
    )
    left = (Fraction(3), Fraction(1), Fraction(-1), Fraction(-2))
    right = (Fraction(1), Fraction(0), Fraction(-1, 2), Fraction(-3, 2))
    require(all(left[i] > left[i + 1] for i in range(3)), "left direction is not decreasing")
    require(all(right[i] > right[i + 1] for i in range(3)), "right direction is not decreasing")
    require(
        all(sum(table[i][j] * left[i] for i in range(4)) == 0 for j in range(4)),
        "left direction does not give zero column sums",
    )
    require(
        all(sum(table[i][j] * right[j] for j in range(4)) == 0 for i in range(4)),
        "right direction does not give zero row sums",
    )
    require(all(sum(row) > 0 for row in table), "empty row block")
    require(all(sum(table[i][j] for i in range(4)) > 0 for j in range(4)), "empty column block")
    require(sum(map(sum, table)) == M, "contingency-table mass mismatch")

    row_sizes = tuple(sum(row) for row in table)
    prefix_sums = []
    running = Fraction(0)
    for size, value in zip(row_sizes, left):
        running += size * value
        prefix_sums.append(running)
    require(prefix_sums[-1] == 0, "private direction has nonzero total")
    require(all(value != 0 for value in prefix_sums[:-1]), "zero denominator in recovered gaps")
    gaps = tuple((left[i] - left[i + 1]) / (2 * prefix_sums[i]) for i in range(3))
    require(gaps == (Fraction(1, 3), Fraction(1, 7), Fraction(1, 4)), "recovered gaps mismatch")
    require(all(gap > 0 for gap in gaps), "recovered gap is not positive")


def matmul(
    a: tuple[tuple[Fraction, ...], ...],
    b: tuple[tuple[Fraction, ...], ...],
) -> tuple[tuple[Fraction, ...], ...]:
    return tuple(
        tuple(
            sum((a[i][k] * b[k][j] for k in range(len(b))), Fraction(0))
            for j in range(len(b[0]))
        )
        for i in range(len(a))
    )


def check_markov_inverse_and_deficit_bounds() -> None:
    # Exact check of equation (29) on nontrivial rational parameters.
    rs = (Fraction(1, 3), Fraction(2, 5), Fraction(3, 7), Fraction(4, 9))
    n = len(rs) + 1
    corr = []
    for i in range(n):
        row = []
        for j in range(n):
            lo, hi = sorted((i, j))
            value = Fraction(1)
            for k in range(lo, hi):
                value *= rs[k]
            row.append(value)
        corr.append(tuple(row))

    precision = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    precision[0][0] += 1
    for i, r in enumerate(rs):
        den = 1 - r * r
        precision[i][i] += r * r / den
        precision[i][i + 1] -= r / den
        precision[i + 1][i] -= r / den
        precision[i + 1][i + 1] += 1 / den
    product = matmul(tuple(corr), tuple(tuple(row) for row in precision))
    identity = tuple(
        tuple(Fraction(int(i == j)) for j in range(n)) for i in range(n)
    )
    require(product == identity, "Markov correlation inverse formula failed")

    endpoint_checks = 0
    for first in range(1, M - 1):
        for last in range(first + 1, M):
            correlation_squared = Fraction(first * (M - last), last * (M - first))
            require(
                correlation_squared >= Fraction(1, (M - 1) ** 2),
                f"endpoint-correlation bound failed: {first},{last}",
            )
            endpoint_checks += 1
    require(endpoint_checks == 45, "endpoint-correlation check count mismatch")

    require(19**2 > 10 * 6**2, "square-root comparison failed")
    require(41**3 > 10 * 19**3, "cube-root comparison failed")
    require(41**4 > 10 * 23**4, "fourth-root comparison failed")
    require(307**5 > 10 * 193**5, "fifth-root comparison failed")

    c = (
        Fraction(0),
        Fraction(0),
        Fraction(2, 11),
        Fraction(24, 25),
        Fraction(19, 10),
        Fraction(23, 8),
        Fraction(193, 50),
    )
    increments = tuple(c[i] - c[i - 1] for i in range(1, len(c)))
    require(
        all(increments[i] < increments[i + 1] for i in range(len(increments) - 1)),
        "rational deficit lower bounds are not discretely convex",
    )
    require(2 * c[3] + 3 * c[2] == Fraction(678, 275) > 2, "t=12 budget failed")
    require(3 * c[3] + 2 * c[2] == Fraction(892, 275) > 3, "t=13 budget failed")
    require(4 * c[3] + c[2] == Fraction(1106, 275) > 4, "t=14 budget failed")
    require(5 * c[3] == Fraction(24, 5) < 5, "balanced t=15 diagnostic failed")
    require(c[4] + 3 * c[3] + c[2] == Fraction(2729, 550) < 5, "second t=15 diagnostic failed")
    require(2 * c[4] + c[3] + 2 * c[2] == Fraction(2818, 550) > 5, "t=15 cutoff failed")


def audit() -> dict[str, object]:
    require(M == 11, f"audit is bound to m=11, got {M}")
    require(LABELS == tuple(range(11)), "label universe mismatch")
    cuts = all_canonical_cuts()
    require(len(cuts) == 2 ** (M - 1) - 1 == 1023, "canonical cut count mismatch")
    check_double_centering(cuts)
    pair_count = check_nonorthogonality(cuts)
    nested_count = check_nested_positivity()
    check_explicit_decompositions()
    check_private_direction_diagnostic()
    check_markov_inverse_and_deficit_bounds()
    script_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return {
        "status": "PASS",
        "scope": "finite arithmetic audit; not a machine proof of the human frame implications",
        "m": M,
        "canonical_cuts": len(cuts),
        "nonorthogonal_pairs_with_repetition": pair_count,
        "nested_cardinality_pairs": nested_count,
        "explicit_decompositions": ["singleton:1/2", "QR(11,5,2):1/6"],
        "private_direction_diagnostic": "table21,gaps:1/3,1/7,1/4",
        "spectral_deficit_audit": "markov_inverse,endpoint45,power_bounds,budgets12-15",
        "script_sha256": script_hash,
    }


def main() -> int:
    try:
        result = audit()
    except Exception as exc:
        print(
            json.dumps({"status": "FAIL", "error": f"{type(exc).__name__}: {exc}"}, sort_keys=True),
            file=sys.stderr,
        )
        return 1
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
