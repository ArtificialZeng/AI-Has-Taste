#!/usr/bin/env python3
"""Exact checks for the round-2 infinite odd-obstruction construction.

The proof of infinitude uses Dirichlet's theorem and is given in
proof/round2_structural_attack.md.  This script checks the CRT data, the
structural identities, and one small explicit prime instance using only the
Python standard library.
"""

from __future__ import annotations

import math
from dataclasses import dataclass


def v2(n: int) -> int:
    if n == 0:
        raise ValueError("v2(0) is not used")
    return (n & -n).bit_length() - 1


def is_prime_trial(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for divisor in range(3, math.isqrt(n) + 1, 2):
        if n % divisor == 0:
            return False
    return True


def crt_pairwise(residues: list[int], moduli: list[int]) -> tuple[int, int]:
    """Solve pairwise-coprime CRT congruences, returning 0 <= x < modulus."""
    if len(residues) != len(moduli):
        raise ValueError("residue/modulus length mismatch")
    x = 0
    modulus = 1
    for residue, new_modulus in zip(residues, moduli):
        if math.gcd(modulus, new_modulus) != 1:
            raise ValueError("moduli are not pairwise coprime")
        step = ((residue - x) * pow(modulus, -1, new_modulus)) % new_modulus
        x += modulus * step
        modulus *= new_modulus
        x %= modulus
    return x, modulus


@dataclass(frozen=True)
class Progression:
    base: tuple[int, ...]
    obstruction_prime: int
    base_n: int
    base_phi: int
    v2_base_phi: int
    v2_base_n_minus_one: int
    residue: int
    modulus: int


def obstruction_progression(base: tuple[int, ...], ell: int) -> Progression:
    assert base == tuple(sorted(base))
    assert all(is_prime_trial(p) and p % 2 for p in base)
    assert is_prime_trial(ell) and ell % 2
    assert ell not in base
    assert all(
        (base[j] - 1) % base[i] != 0
        for i in range(len(base))
        for j in range(i + 1, len(base))
    )

    m = math.prod(base)
    phi = math.prod(p - 1 for p in base)
    assert m > 2 * phi
    assert (m - 1) % ell != 0
    assert phi % ell != 0  # the appended prime creates a new odd LCM factor

    a = v2(m - 1)
    big_v = v2(phi)
    exponent = big_v + a
    two_modulus = 1 << exponent
    moduli = [two_modulus, *base, ell]
    residues = [pow(m, -1, two_modulus), *([2] * len(base)), 1]
    residue, modulus = crt_pairwise(residues, moduli)

    assert math.gcd(residue, modulus) == 1
    assert m * residue % two_modulus == 1
    assert v2(residue - 1) == a
    assert all((residue - 1) % p != 0 for p in base)
    assert (residue - 1) % ell == 0

    return Progression(
        base=base,
        obstruction_prime=ell,
        base_n=m,
        base_phi=phi,
        v2_base_phi=big_v,
        v2_base_n_minus_one=a,
        residue=residue,
        modulus=modulus,
    )


def check_appended_prime(progression: Progression, q: int) -> None:
    assert q % progression.modulus == progression.residue
    assert is_prime_trial(q)
    assert q > progression.base[-1]

    primes = (*progression.base, q)
    n = math.prod(primes)
    phi = math.prod(p - 1 for p in primes)
    two_part = phi & -phi
    modulus = math.lcm(*(p - 1 for p in primes))

    assert all(
        (primes[j] - 1) % primes[i] != 0
        for i in range(len(primes))
        for j in range(i + 1, len(primes))
    )
    assert n > 2 * phi
    assert (n - 1) % two_part == 0
    assert (q - 1) % progression.obstruction_prime == 0
    assert (n - 1) % progression.obstruction_prime != 0
    assert (n - 1) % modulus != 0

    print("explicit prime tuple:", primes)
    print("n:", n)
    print("phi:", phi)
    print("v2(phi):", v2(phi))
    print("(n-1) mod lcm(p-1):", (n - 1) % modulus)


def main() -> None:
    small = obstruction_progression((3, 5, 17, 23), 7)
    assert small.residue == 45412697
    assert small.modulus == 84080640
    explicit_q = small.residue + small.modulus
    assert explicit_q == 129493337
    check_appended_prime(small, explicit_q)

    frontier_base = (3, 5, 17, 23, 29, 53, 83, 89, 113, 149, 173, 197, 257, 263)
    frontier = obstruction_progression(frontier_base, 19)
    assert frontier.base_n == 2582711497985129172242745
    assert frontier.base_phi == 1108909394958557175087104
    assert frontier.v2_base_phi == 35
    assert frontier.v2_base_n_minus_one == 3
    assert frontier.residue == 8102964695365714789790474720630705417
    assert frontier.modulus == 13488676285320748421967659149893304320

    print("frontier base cardinality:", len(frontier_base))
    print("frontier CRT residue:", frontier.residue)
    print("frontier CRT modulus:", frontier.modulus)

    universe = tuple(p for p in range(3, 348, 2) if is_prime_trial(p))
    universe_n = math.prod(universe)
    universe_phi = math.prod(p - 1 for p in universe)
    assert len(universe) == 68 and universe[-1] == 347
    assert 5 * universe_phi < universe_n < 6 * universe_phi
    assert universe_n.bit_length() == 458
    assert universe_phi.bit_length() == 455
    assert (5 * universe_phi + 1).bit_length() == 457
    print("cap-347 quotient range: k in {2,3,4,5}")
    print("cap-347 bit widths: N=458, Phi=455, 5*Phi+1=457")
    print("PASS: exact CRT and obstruction checks")


if __name__ == "__main__":
    main()
