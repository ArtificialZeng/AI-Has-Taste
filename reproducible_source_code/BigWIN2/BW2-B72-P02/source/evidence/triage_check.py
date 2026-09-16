#!/usr/bin/env python3
"""Exact intake checks for win-00072-p02; Python standard library only."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


N = 34
A_DIGITS = "2202202000022020222202000220200020"
B_DIGITS = "1133303133112311101113211331303331"
ROOTS = ((1, 0), (0, 1), (-1, 0), (0, -1))
UNITS = tuple(k for k in range(N) if math.gcd(k, N) == 1)


def add(z: tuple[int, int], w: tuple[int, int]) -> tuple[int, int]:
    return z[0] + w[0], z[1] + w[1]


def mul(z: tuple[int, int], w: tuple[int, int]) -> tuple[int, int]:
    return z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0]


def conj(z: tuple[int, int]) -> tuple[int, int]:
    return z[0], -z[1]


def decode_digits(word: str) -> tuple[tuple[int, int], ...]:
    assert len(word) == N and set(word) <= set("0123")
    return tuple(ROOTS[int(c)] for c in word)


def paf(word: tuple[tuple[int, int], ...], h: int) -> tuple[int, int]:
    total = (0, 0)
    for j in range(N):
        total = add(total, mul(word[j], conj(word[(j + h) % N])))
    return total


def gray(word: tuple[tuple[int, int], ...]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    # z=(p+q)/2+i(p-q)/2, hence p=Re(z)+Im(z), q=Re(z)-Im(z).
    p = tuple(a + b for a, b in word)
    q = tuple(a - b for a, b in word)
    assert set(p) <= {-1, 1} and set(q) <= {-1, 1}
    return p, q


def reversible(row: tuple[object, ...]) -> bool:
    return all(row[j] == row[-j % N] for j in range(N))


def transform(
    word: tuple[tuple[int, int], ...],
    phase: tuple[int, int],
    shift: int,
    decimation: int,
    conjugate: int,
) -> tuple[tuple[int, int], ...]:
    k_inv = pow(decimation, -1, N)
    base = tuple(conj(z) for z in word) if conjugate else word
    # c_shift d_decimation(word), exactly in the order frozen in source.md.
    return tuple(mul(phase, base[((j - shift) * k_inv) % N]) for j in range(N))


def least_failure(row: tuple[object, ...]) -> int | None:
    return next((j for j in range(N) if row[j] != row[-j % N]), None)


def main() -> None:
    project = Path(__file__).resolve().parents[1]
    source_hash = hashlib.sha256((project / "source.md").read_bytes()).hexdigest()
    A = decode_digits(A_DIGITS)
    B = decode_digits(B_DIGITS)

    qlp_sums = [add(paf(A, h), paf(B, h)) for h in range(1, N)]
    assert qlp_sums == [(-2, 0)] * (N - 1)

    individual_domain = len(ROOTS) * N * len(UNITS) * 2
    reversible_counts: dict[str, int] = {}
    for label, word in (("A", A), ("B", B)):
        count = 0
        for phase in ROOTS:
            for shift in range(N):
                for k in UNITS:
                    for epsilon in (0, 1):
                        rows = gray(transform(word, phase, shift, k, epsilon))
                        count += int(all(reversible(row) for row in rows))
        reversible_counts[label] = count

    # A short certificate for the decisive obstruction: for each possible shift
    # axis (decimation merely permutes these), give the least failed index.
    a_shift_witnesses = []
    for shift in range(N):
        shifted = transform(A, ROOTS[0], shift, 1, 0)
        failure = least_failure(shifted)
        assert failure is not None
        a_shift_witnesses.append(
            {
                "shift": shift,
                "least_failed_j": failure,
                "value_at_j": A_DIGITS[(failure - shift) % N],
                "value_at_minus_j": A_DIGITS[(-failure - shift) % N],
            }
        )

    # Directly identify every cyclic reflection axis u -> a-u, including the
    # odd-axis class not reachable from j -> -j by an integral cyclic shift.
    reflection_axes = {}
    for label, word in (("A", A), ("B", B)):
        reflection_axes[label] = [
            axis
            for axis in range(N)
            if all(word[u] == word[(axis - u) % N] for u in range(N))
        ]

    result = {
        "job_id": "win-00072-p02-triage-226ed42f9d60",
        "source_sha256": source_hash,
        "word_lengths": {"A": len(A_DIGITS), "B": len(B_DIGITS)},
        "units_mod_34": list(UNITS),
        "parameter_domain_before_deduplication": 2 * 16 * N * N * len(UNITS) * 2,
        "qlp_nonzero_lags_checked": N - 1,
        "qlp_all_sums": [-2, 0],
        "individual_transform_domain": individual_domain,
        "transforms_with_both_gray_rows_reversible": reversible_counts,
        "cyclic_reflection_axes_u_to_a_minus_u": reflection_axes,
        "A_shift_failure_witnesses": a_shift_witnesses,
    }
    assert individual_domain == 4352
    assert result["parameter_domain_before_deduplication"] == 1_183_744
    assert reversible_counts["A"] == 0
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
