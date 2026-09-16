#!/usr/bin/env python3
"""Exact normalized counterexample screen for the triage claim.

For fixed missing sums {0,2}, missingness forces U(B) into C=F_p\A.  The
program enumerates every B and every size-ell superset C of U(B), computes the
restricted sumset directly, and compares all resulting normalized pairs with
the proposed representatives.  This is finite evidence, not a universal proof.
"""

from itertools import combinations


PRIMES = (11, 13, 17, 19)


def restricted_sumset(p, A, B):
    return {(x + y) % p for x in A for y in B if x != y}


def proposed_pair(p, ell, a):
    b = ell - a
    B = {(-2 * j) % p for j in range(a)}
    B |= {(1 + 2 * j) % p for j in range(b)}
    C = {(2 + 2 * j) % p for j in range(a)}
    C |= {(-1 - 2 * j) % p for j in range(b)}
    return frozenset(B), frozenset(C)


def key(pair):
    B, C = pair
    return tuple(sorted(B)), tuple(sorted(C))


def reflect(p, pair):
    B, C = pair
    return frozenset((1 - x) % p for x in B), frozenset(
        (1 - x) % p for x in C
    )


def normalized_pairs(p, ell):
    field = set(range(p))
    actual = set()
    slack = 0
    for values in combinations(range(p), ell):
        B = set(values)
        U = {(-y) % p for y in B if y != 0}
        U |= {(2 - y) % p for y in B if y != 1}
        if len(U) > ell:
            continue
        if len(U) < ell:
            slack += 1
        for extra in combinations(sorted(field - U), ell - len(U)):
            C = U | set(extra)
            A = field - C
            sums = restricted_sumset(p, A, B)
            if field - sums == {0, 2}:
                actual.add((frozenset(B), frozenset(C)))
    return actual, slack


def orbit_count(p, pairs):
    unseen = set(pairs)
    count = 0
    while unseen:
        pair = unseen.pop()
        unseen.discard(reflect(p, pair))
        count += 1
    return count


def main():
    total_cases = 0
    for p in PRIMES:
        for ell in range(3, (p - 3) // 2 + 1):
            actual, slack = normalized_pairs(p, ell)
            expected = {proposed_pair(p, ell, a) for a in range(ell + 1)}
            assert actual == expected
            assert slack == 0
            orbits = orbit_count(p, actual)
            assert len(actual) == ell + 1
            assert orbits == ell // 2 + 1
            total_cases += 1
            print(
                f"p={p:2d} ell={ell}: normalized={len(actual)}, "
                f"slack_U={slack}, affine_orbits={orbits}, match=True"
            )
    print(f"PASS: {total_cases} parameter cases; exact exhaustive normalized search")


if __name__ == "__main__":
    main()
