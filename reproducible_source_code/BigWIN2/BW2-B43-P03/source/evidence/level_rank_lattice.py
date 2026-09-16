#!/usr/bin/env python3
"""Exact level-rank lattice model for the two unresolved e=6 series.

This is an exact finite checker for the derivation in level-rank-lattice.md.
It does not turn finite coefficient or congruence tests into an all-orders
positivity proof.
"""

from __future__ import annotations

import argparse
import itertools
import math
from pathlib import Path

from exact_coefficients import is_six_core_bipartition


def inverse_cutoffs(t: tuple[int, ...]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Return residue cutoffs M_{j,r} for LR^{-1}(|empty,t>)."""
    first = tuple((x - 2) // 2 for x in t)
    second = tuple((x - 1) // 2 for x in t)
    return first, second


def row_charge(cutoffs: tuple[int, ...]) -> int:
    """Charge of {6m+r: m<=M_r, 1<=r<=6}."""
    return sum(m + 1 for m in cutoffs)


def cutoff_energy(cutoffs: tuple[int, ...]) -> int:
    """Regularized beta-set energy relative to charge zero."""
    return sum((m + 1) * (3 * m + r)
               for r, m in enumerate(cutoffs, start=1))


def multipartition_size(t: tuple[int, ...]) -> int:
    """Size obtained from the two inverse-LR beta sets."""
    rows = inverse_cutoffs(t)
    charges = tuple(row_charge(row) for row in rows)
    return (sum(cutoff_energy(row) for row in rows)
            - sum(s * (s + 1) // 2 for s in charges))


def q_form(u: tuple[int, ...], eps: tuple[int, ...], a: int) -> int:
    """The inhomogeneous A_5-coset form Q_a(u,eps)."""
    assert len(u) == len(eps) == 6
    assert sum(u) == 0 and sum(eps) == a
    return (sum(6 * x * x + 2 * (r - 3) * x
                + bit * (6 * x + r)
                for r, (x, bit) in enumerate(zip(u, eps), start=1))
            - a * (a + 1) // 2)


def partition_from_cutoffs(cutoffs: tuple[int, ...], charge: int) -> tuple[int, ...]:
    """Recover a partition from a six-residue beta set."""
    low_m = min(cutoffs) - 12
    beads = sorted((6 * m + r
                    for r, top in enumerate(cutoffs, start=1)
                    for m in range(low_m, top + 1)), reverse=True)
    parts = [beta + i - 1 - charge for i, beta in enumerate(beads, start=1)]
    if any(x < 0 for x in parts) or any(parts[i] < parts[i + 1]
                                       for i in range(len(parts) - 1)):
        raise AssertionError("cutoffs did not produce a partition")
    if any(parts[-12:]):
        raise AssertionError("beta-set truncation was not deep enough")
    return tuple(x for x in parts if x)


def ceil_div(n: int, d: int) -> int:
    return -((-n) // d)


def coefficients(limit: int, a: int) -> tuple[list[int], list[tuple[tuple[int, ...], tuple[int, ...]] | None]]:
    """Enumerate Q_a exactly through q^limit using the square-form bound."""
    if a not in (1, 3):
        raise ValueError("a must be 1 or 3")
    constant = 16 if a == 1 else 28
    x_bound = math.isqrt(6 * limit + constant)
    counts = [0] * (limit + 1)
    witnesses: list[tuple[tuple[int, ...], tuple[int, ...]] | None] = [None] * (limit + 1)

    for odd_positions in itertools.combinations(range(6), a):
        eps = tuple(int(i in odd_positions) for i in range(6))
        allowed: list[range] = []
        for r, bit in enumerate(eps, start=1):
            offset = 3 * bit + r - 3
            lo = ceil_div(-x_bound - offset, 6)
            hi = (x_bound - offset) // 6
            allowed.append(range(lo, hi + 1))

        for first_five in itertools.product(*allowed[:5]):
            last = -sum(first_five)
            if last not in allowed[5]:
                continue
            u = tuple(first_five) + (last,)
            n = q_form(u, eps, a)
            if not 0 <= n <= limit:
                continue

            t = tuple(2 * x + bit for x, bit in zip(u, eps))
            rows = inverse_cutoffs(t)
            charges = tuple(row_charge(row) for row in rows)
            if charges != (0, a):
                raise AssertionError((t, charges))
            if multipartition_size(t) != n:
                raise AssertionError((t, n, multipartition_size(t)))
            x = tuple(3 * tr + r - 3 for r, tr in enumerate(t, start=1))
            if sum(x) != 3 * (a + 1) or sum(y * y for y in x) != 6 * n + constant:
                raise AssertionError("six-square identity failed")
            lam1 = partition_from_cutoffs(rows[0], 0)
            lam2 = partition_from_cutoffs(rows[1], a)
            if sum(lam1) + sum(lam2) != n:
                raise AssertionError("reconstructed size failed")
            if not is_six_core_bipartition(lam1, lam2, a):
                raise AssertionError("reconstructed object failed nestedness")

            counts[n] += 1
            if witnesses[n] is None:
                witnesses[n] = (u, eps)
    return counts, witnesses


def load_previous_coefficients(path: Path, a: int) -> list[int]:
    prefix = f"c_6,(0,{a}):"
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith(prefix):
            return [int(x) for x in line[len(prefix):].split()]
    raise ValueError(f"missing {prefix!r} in {path}")


def represented_residues(a: int, modulus: int) -> set[int]:
    """Exact Q_a residues, using u_i modulo modulus and sum(u_i)=0."""
    states = {(0, 0, 0)}  # (number of odd coordinates, sum(u), Q before constant)
    for r in range(1, 7):
        nxt: set[tuple[int, int, int]] = set()
        values = [(u,
                   (6 * u * u + 2 * (r - 3) * u) % modulus,
                   (6 * u + r) % modulus)
                  for u in range(modulus)]
        for odd_count, u_sum, value in states:
            for u, even_term, odd_delta in values:
                nxt.add((odd_count,
                         (u_sum + u) % modulus,
                         (value + even_term) % modulus))
                if odd_count < a:
                    nxt.add((odd_count + 1,
                             (u_sum + u) % modulus,
                             (value + even_term + odd_delta) % modulus))
        states = nxt
    shift = a * (a + 1) // 2
    return {(value - shift) % modulus
            for odd_count, u_sum, value in states
            if odd_count == a and u_sum == 0}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=100)
    parser.add_argument("--max-modulus", type=int, default=24)
    parser.add_argument(
        "--compare",
        type=Path,
        default=Path(__file__).with_name("exact-coefficients-n40.txt"),
    )
    args = parser.parse_args()
    if args.limit < 0 or args.max_modulus < 2:
        parser.error("limit must be nonnegative and max-modulus at least 2")

    print("parameterization: t_r=2u_r+eps_r, sum(u_r)=0, sum(eps_r)=a")
    print("Q_a=sum_r[6u_r^2+2(r-3)u_r+eps_r(6u_r+r)]-a(a+1)/2")
    for a in (1, 3):
        counts, witnesses = coefficients(args.limit, a)
        previous = load_previous_coefficients(args.compare, a)
        overlap = min(len(previous), len(counts))
        if counts[:overlap] != previous[:overlap]:
            bad = next(i for i in range(overlap) if counts[i] != previous[i])
            raise AssertionError(
                f"coefficient mismatch for a={a}, n={bad}: "
                f"lattice={counts[bad]}, nested={previous[bad]}"
            )
        zeros = [n for n, value in enumerate(counts) if value == 0]
        missing_moduli = []
        for modulus in range(2, args.max_modulus + 1):
            residues = represented_residues(a, modulus)
            if len(residues) != modulus:
                missing_moduli.append(
                    (modulus, sorted(set(range(modulus)) - residues))
                )
        if any(witness is None for witness in witnesses):
            raise AssertionError("zero coefficient unexpectedly has no witness")
        print(f"a={a}: exact coefficients 0<=n<={args.limit}: "
              + " ".join(map(str, counts)))
        print(f"a={a}: zero coefficients on 0<=n<={args.limit}: {zeros}")
        print(f"a={a}: agrees with nested-beta enumeration on 0<=n<{overlap}")
        print(f"a={a}: missing residue classes for 2<=m<={args.max_modulus}: "
              f"{missing_moduli}")


if __name__ == "__main__":
    main()
