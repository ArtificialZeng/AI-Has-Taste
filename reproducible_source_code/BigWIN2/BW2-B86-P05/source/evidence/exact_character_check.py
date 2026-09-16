#!/usr/bin/env python3
"""Exact triage check for SDS(9,8,1,C_3^2).

All arithmetic in character values is performed in Z[w], where
w^2 + w + 1 = 0 and N(a+bw)=a^2-ab+b^2.
"""

from itertools import combinations, product


POINTS = tuple(product(range(3), repeat=2))
NONZERO = tuple(x for x in POINTS if x != (0, 0))
CHARACTERS = NONZERO


def add(z, t):
    return (z[0] + t[0], z[1] + t[1])


def omega_power(exponent):
    """Return w**exponent as the coefficient pair (a,b) for a+bw."""
    return ((1, 0), (0, 1), (-1, -1))[exponent % 3]


def eisenstein_norm(z):
    a, b = z
    return a * a - a * b + b * b


def character_sum(negative_pair, character):
    """Compute chi(D), with zero at 0 and signs -1 on negative_pair."""
    total = (0, 0)
    for x in NONZERO:
        coefficient = -1 if x in negative_pair else 1
        exponent = (character[0] * x[0] + character[1] * x[1]) % 3
        value = omega_power(exponent)
        total = add(total, (coefficient * value[0], coefficient * value[1]))
    return total


def coefficient(negative_pair, x):
    if x == (0, 0):
        return 0
    return -1 if x in negative_pair else 1


def autocorrelation(negative_pair, shift):
    """Coefficient of shift in D D^(-1), computed directly in Z[G]."""
    return sum(
        coefficient(negative_pair, x)
        * coefficient(
            negative_pair,
            ((x[0] - shift[0]) % 3, (x[1] - shift[1]) % 3),
        )
        for x in POINTS
    )


def matrices_gl23():
    matrices = []
    for entries in product(range(3), repeat=4):
        a, b, c, d = entries
        if (a * d - b * c) % 3:
            matrices.append(((a, b), (c, d)))
    return tuple(matrices)


def act(matrix, x):
    return (
        (matrix[0][0] * x[0] + matrix[0][1] * x[1]) % 3,
        (matrix[1][0] * x[0] + matrix[1][1] * x[1]) % 3,
    )


def canonical_pair(x, y):
    return tuple(sorted((x, y)))


def orbit(pair, matrices):
    return {
        canonical_pair(act(matrix, pair[0]), act(matrix, pair[1]))
        for matrix in matrices
    }


def pair_type(pair):
    x, y = pair
    return "opposite" if y == ((-x[0]) % 3, (-x[1]) % 3) else "independent"


def main():
    pairs = tuple(combinations(NONZERO, 2))
    matrices = matrices_gl23()
    assert len(pairs) == 28
    assert len(matrices) == 48

    remaining = set(pairs)
    orbits = []
    while remaining:
        representative = min(remaining)
        current_orbit = orbit(representative, matrices)
        assert current_orbit <= set(pairs)
        orbits.append((representative, current_orbit))
        remaining -= current_orbit

    assert sorted(len(current_orbit) for _, current_orbit in orbits) == [4, 24]
    assert len({pair_type(representative) for representative, _ in orbits}) == 2

    print("ring=Z[w]/(w^2+w+1); norm(a+bw)=a^2-a*b+b^2")
    print(f"points={len(POINTS)} nonzero_points={len(NONZERO)}")
    print(f"GL(2,3)_matrices={len(matrices)} unordered_negative_pairs={len(pairs)}")
    print(
        "orbits="
        + ", ".join(
            f"{pair_type(representative)}:representative={representative}:size={len(current_orbit)}"
            for representative, current_orbit in sorted(orbits)
        )
    )
    print("character_order=" + repr(CHARACTERS))

    passing_pairs = []
    direct_passing_pairs = []
    for pair in pairs:
        values = tuple(character_sum(pair, character) for character in CHARACTERS)
        norms = tuple(eisenstein_norm(value) for value in values)
        if all(norm == 7 for norm in norms):
            passing_pairs.append(pair)
        correlations = tuple(autocorrelation(pair, shift) for shift in NONZERO)
        if all(value == 1 for value in correlations):
            direct_passing_pairs.append(pair)
        exact = ",".join(
            f"{character}:{value[0]}+{value[1]}w:N={norm}"
            for character, value, norm in zip(CHARACTERS, values, norms)
        )
        print(
            f"pair={pair} type={pair_type(pair)} "
            f"correlations={correlations} exact=[{exact}]"
        )

    print(f"pairs_with_all_nonprincipal_norms_7={len(passing_pairs)}")
    print(f"pairs_with_all_nonzero_correlations_1={len(direct_passing_pairs)}")
    assert passing_pairs == direct_passing_pairs
    assert not passing_pairs
    print("RESULT=PASS: every normalized sign assignment has an exact character obstruction")


if __name__ == "__main__":
    main()
