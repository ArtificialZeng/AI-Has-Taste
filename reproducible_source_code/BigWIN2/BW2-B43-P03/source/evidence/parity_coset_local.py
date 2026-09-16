#!/usr/bin/env python3
"""Exact checks for parity-coset symmetries and local coverage.

The proofs of the all-prime statements are in parity-coset-local.md.  This
script checks the finite orbit bookkeeping and the stated residue/lifting
patterns; it is not an integral local-to-global theorem.
"""

from __future__ import annotations

import itertools


def eps_vector(positions: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(int(r in positions) for r in range(1, 7))


def constant_parity(a: int, eps: tuple[int, ...]) -> int:
    return (sum(r * eps[r - 1] for r in range(1, 7))
            - a * (a + 1) // 2) % 2


def half_gradient_mod_2(eps: tuple[int, ...]) -> tuple[int, ...]:
    """Gradient of (Q-C)/2 after u_6=-sum_{i<=5}u_i, modulo 2."""
    return tuple((i + eps[i - 1] + eps[5]) % 2 for i in range(1, 6))


def q_value(a: int, eps: tuple[int, ...], first_five: tuple[int, ...]) -> int:
    u = first_five + (-sum(first_five),)
    return (sum(6 * z * z + 2 * (r - 3) * z + eps[r - 1] * (6 * z + r)
                for r, z in enumerate(u, start=1))
            - a * (a + 1) // 2)


def residue_values(a: int, eps: tuple[int, ...], modulus: int) -> set[int]:
    """Values of Q modulo modulus, exhaustively but with coordinate DP."""
    # State is (sum of chosen u_i, partial Q without the constant).
    states = {(0, 0)}
    for r in range(1, 7):
        nxt = set()
        for old_sum, old_q in states:
            for u in range(modulus):
                term = (6 * u * u + 2 * (r - 3) * u
                        + eps[r - 1] * (6 * u + r))
                nxt.add(((old_sum + u) % modulus,
                         (old_q + term) % modulus))
        states = nxt
    shift = a * (a + 1) // 2
    return {(value - shift) % modulus for total, value in states if total == 0}


def orbit_key(a: int, eps: tuple[int, ...]) -> tuple[int, ...]:
    """Key under Aut(A5)=+-S6 for the affine norm cosets."""
    residues = tuple(sorted(((r - 3) + 3 * eps[r - 1]) % 6
                            for r in range(1, 7)))
    reflected = tuple(sorted((a + 1 - z) % 6 for z in residues))
    return min(residues, reflected)


def orbit_rows(a: int) -> list[tuple[tuple[int, ...], tuple[tuple[int, ...], ...]]]:
    groups: dict[tuple[int, ...], list[tuple[int, ...]]] = {}
    for positions in itertools.combinations(range(1, 7), a):
        groups.setdefault(orbit_key(a, eps_vector(positions)), []).append(positions)
    return [(key, tuple(members)) for key, members in sorted(groups.items())]


def main() -> None:
    for a in (1, 3):
        rows = orbit_rows(a)
        print(f"a={a}: full affine-isometry orbits={len(rows)}")
        for index, (key, members) in enumerate(rows, start=1):
            annotated = [
                (member, constant_parity(a, eps_vector(member)))
                for member in members
            ]
            print(f"  orbit {index}: residue-key={key}; "
                  f"members-and-Q-parity={annotated}")

        nonsingular_by_parity: dict[int, list[tuple[int, ...]]] = {0: [], 1: []}
        singular = []
        for positions in itertools.combinations(range(1, 7), a):
            eps = eps_vector(positions)
            parity = constant_parity(a, eps)
            gradient = half_gradient_mod_2(eps)
            (nonsingular_by_parity[parity] if any(gradient) else singular).append(positions)
        print(f"a={a}: 2-adically nonsingular cosets by Q parity="
              f"{nonsingular_by_parity}")
        print(f"a={a}: singular after halving at 2={singular}")

        # Exhaustive finite shadows of the lifting proofs.
        for positions in (nonsingular_by_parity[0][0],
                          nonsingular_by_parity[1][0]):
            eps = eps_vector(positions)
            parity = constant_parity(a, eps)
            values_32 = residue_values(a, eps, 32)
            expected_32 = set(range(parity, 32, 2))
            assert values_32 == expected_32
            values_27 = residue_values(a, eps, 27)
            assert values_27 == set(range(27))
            print(f"a={a}, eps={positions}: Q mod 32 is every residue "
                  f"of parity {parity}; Q mod 27 is all residues")

    # Spot-check the direct polynomial evaluator against its parity formula.
    for a in (1, 3):
        for positions in itertools.combinations(range(1, 7), a):
            eps = eps_vector(positions)
            parity = constant_parity(a, eps)
            for first_five in itertools.product(range(-2, 3), repeat=5):
                assert q_value(a, eps, first_five) % 2 == parity
    print("direct parity identity checked for every coset and u_1,...,u_5 in [-2,2]")


if __name__ == "__main__":
    main()
