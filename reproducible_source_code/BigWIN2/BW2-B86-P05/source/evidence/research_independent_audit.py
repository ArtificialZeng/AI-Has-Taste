#!/usr/bin/env python3
"""Independent exact audit of the proposed SDS(9,8,1,C_3^2) proof.

This implementation does not import either triage checker.  It verifies the
normalization map on all 2304 raw coefficient assignments, the two GL(2,3)
orbits, and the character selected by the proof for every normalized pair.
Eisenstein integers are stored as (r,s) = r+s*w with w^2+w+1=0.
"""

from collections import Counter
from itertools import combinations, product


F3 = range(3)
G = tuple(product(F3, repeat=2))
ZERO = (0, 0)
G_STAR = tuple(x for x in G if x != ZERO)


def vadd(x, y):
    return ((x[0] + y[0]) % 3, (x[1] + y[1]) % 3)


def vneg(x):
    return ((-x[0]) % 3, (-x[1]) % 3)


def dot(x, y):
    return (x[0] * y[0] + x[1] * y[1]) % 3


def correlations(coeff):
    """Coefficients of D D^(-1), indexed by the additive shift t."""
    return tuple(
        sum(coeff[x] * coeff[vadd(x, vneg(t))] for x in G)
        for t in G
    )


def translate_to_zero(coeff, old_zero):
    """Coefficients of [-old_zero]D, whose zero is at the identity."""
    return {x: coeff[vadd(x, old_zero)] for x in G}


def canonical_negative_pair(coeff, old_zero):
    """Normalize translation and global sign for any principal-sum candidate."""
    assert abs(sum(coeff.values())) == 4
    normalized = translate_to_zero(coeff, old_zero)
    if sum(normalized.values()) == -4:
        normalized = {x: -value for x, value in normalized.items()}
    assert normalized[ZERO] == 0
    negatives = tuple(sorted(x for x in G_STAR if normalized[x] == -1))
    assert len(negatives) == 2
    return negatives, normalized


def omega_power(j):
    return ((1, 0), (0, 1), (-1, -1))[j % 3]


def zadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def zscale(c, x):
    return (c * x[0], c * x[1])


def enorm(x):
    r, s = x
    return r * r - r * s + s * s


def normalized_coeff(pair):
    return {x: 0 if x == ZERO else (-1 if x in pair else 1) for x in G}


def character_value(pair, u):
    coeff = normalized_coeff(pair)
    value = (0, 0)
    for x in G:
        value = zadd(value, zscale(coeff[x], omega_power(dot(u, x))))
    return value


def matrices_gl23():
    answer = []
    for a, b, c, d in product(F3, repeat=4):
        if (a * d - b * c) % 3 != 0:
            answer.append(((a, b), (c, d)))
    return tuple(answer)


def mact(matrix, x):
    return (
        (matrix[0][0] * x[0] + matrix[0][1] * x[1]) % 3,
        (matrix[1][0] * x[0] + matrix[1][1] * x[1]) % 3,
    )


def unordered_pair(x, y):
    return tuple(sorted((x, y)))


def main():
    # Raw coverage: the principal equation forces sum(D)^2=16.  Verify that
    # normalization of every such raw assignment lands on exactly one of the
    # 28 pairs, with the expected 9 translations and 2 global signs.
    raw_count = 0
    principal_eligible = 0
    normalized_multiplicity = Counter()
    raw_solutions = 0
    target = (8,) + (1,) * 8  # G is lexicographically ordered, with 0 first.
    for old_zero in G:
        support = tuple(x for x in G if x != old_zero)
        for signs in product((-1, 1), repeat=8):
            raw_count += 1
            coeff = dict(zip(support, signs))
            coeff[old_zero] = 0
            corr = correlations(coeff)
            raw_solutions += corr == target
            if abs(sum(coeff.values())) != 4:
                continue
            principal_eligible += 1
            pair, normalized = canonical_negative_pair(coeff, old_zero)
            normalized_multiplicity[pair] += 1
            assert correlations(normalized) == corr  # translation/global sign

    all_pairs = tuple(combinations(G_STAR, 2))
    assert raw_count == 9 * 2**8 == 2304
    assert principal_eligible == 9 * 2 * len(all_pairs) == 504
    assert set(normalized_multiplicity) == set(all_pairs)
    assert set(normalized_multiplicity.values()) == {18}
    assert raw_solutions == 0

    # Symmetry audit, independent of the character obstruction.
    gl = matrices_gl23()
    assert len(gl) == 48
    unvisited = set(all_pairs)
    orbit_data = []
    while unvisited:
        representative = min(unvisited)
        orbit = {
            unordered_pair(mact(matrix, representative[0]),
                           mact(matrix, representative[1]))
            for matrix in gl
        }
        kind = "opposite" if representative[1] == vneg(representative[0]) else "independent"
        assert all(
            (pair[1] == vneg(pair[0])) == (kind == "opposite")
            for pair in orbit
        )
        orbit_data.append((kind, representative, len(orbit)))
        unvisited -= orbit
    assert sorted(size for _, _, size in orbit_data) == [4, 24]
    assert {kind for kind, _, _ in orbit_data} == {"opposite", "independent"}

    # Proof audit: construct the advertised nonprincipal character separately
    # for every pair and check its exact value and norm.
    obstruction_counts = Counter()
    certificates = []
    for a, b in all_pairs:
        if b == vneg(a):
            witnesses = tuple(u for u in G_STAR if dot(u, a) == 0)
            assert len(witnesses) == 2
            u = min(witnesses)
            assert dot(u, b) == 0
            value = character_value((a, b), u)
            assert value == (-5, 0)
            expected_norm = 25
            kind = "opposite"
        else:
            # Distinct dependent nonzero vectors in F_3^2 are opposites, so
            # this is precisely the independent case.  The two affine-linear
            # equations have one solution u, necessarily nonzero.
            witnesses = tuple(
                u for u in G if dot(u, a) == 1 and dot(u, b) == 1
            )
            assert len(witnesses) == 1 and witnesses[0] != ZERO
            u = witnesses[0]
            value = character_value((a, b), u)
            assert value == (-1, -4)
            expected_norm = 13
            kind = "independent"
        norm = enorm(value)
        assert norm == expected_norm and norm != 7
        obstruction_counts[kind] += 1
        certificates.append((a, b, u, value, norm))

    assert obstruction_counts == {"opposite": 4, "independent": 24}
    assert len(certificates) == 28

    print("raw_assignments=2304")
    print("principal_sum_eligible=504")
    print("normalized_pairs=28 multiplicity_each=18")
    print("GL(2,3)=48")
    print("orbits=" + repr(sorted(orbit_data)))
    print("character_certificates=opposite:4:norm25,independent:24:norm13")
    print("raw_solutions=0")
    print("RESULT=PASS: normalization, orbit exhaustion, and all exact character obstructions verified")


if __name__ == "__main__":
    main()
