#!/usr/bin/env python3
"""Exact certificates for the cyclic cases of orders 5 through 10.

All cut computations and dual-certificate checks use exact integers,
``Fraction`` objects, or symbolic expressions in Q(sqrt(5)).  The four cases
requiring negative-type information use explicit Fourier identities.
"""

from fractions import Fraction
from math import gcd

import sympy as sp


def orbit_representatives(n):
    candidates = []
    for mask in range(1 << (n - 1)):
        subset = frozenset(
            x for x in range(1, n) if mask >> (x - 1) & 1
        )
        if (
            subset == frozenset((-x) % n for x in subset)
            and gcd(n, *subset) == 1
        ):
            candidates.append(subset)
    units = [u for u in range(1, n) if gcd(u, n) == 1]
    unseen = set(candidates)
    representatives = []
    while unseen:
        representative = min(
            unseen, key=lambda subset: (len(subset), tuple(sorted(subset)))
        )
        unseen -= {
            frozenset((u * x) % n for x in representative) for u in units
        }
        representatives.append(representative)
    return representatives


def exact_cut_optimum(n, generators):
    """Return (value, one minimizing set, boundary size), all exactly."""
    best = None
    # Every cut/complement pair has a unique representative avoiding n-1.
    for mask in range(1, 1 << (n - 1)):
        subset = {x for x in range(n - 1) if mask >> x & 1}
        size = len(subset)
        boundary = sum(
            (x + s) % n not in subset for x in subset for s in generators
        )
        value = Fraction(
            n * boundary, len(generators) * size * (n - size)
        )
        candidate = (value, tuple(sorted(subset)), boundary)
        if best is None or candidate < best:
            best = candidate
    return best


def distance_index(n, residue):
    residue %= n
    if residue == 0:
        return None
    return min(residue, n - residue) - 1


def metric_lp_data(n, generators):
    """Rational data for symmetric translation-invariant semimetrics."""
    dimension = n // 2
    rows = []
    labels = []
    for a in range(1, n):
        for b in range(a, n):
            row = [0] * dimension
            for coefficient, residue in ((1, a), (1, b), (-1, a + b)):
                index = distance_index(n, residue)
                if index is not None:
                    row[index] += coefficient
            if any(row):
                rows.append(row)
                labels.append((a, b))

    objective = [Fraction(0) for _ in range(dimension)]
    denominator = [Fraction(0) for _ in range(dimension)]
    for s in generators:
        objective[distance_index(n, s)] += Fraction(1, len(generators))
    for residue in range(1, n):
        denominator[distance_index(n, residue)] += Fraction(1, n)
    return rows, labels, objective, denominator


def rational_metric_certificate(n, generators, target):
    """Load a serialized dual certificate and validate its identity exactly.

    If R_ab is the row for f(a)+f(b)-f(a+b) >= 0, this verifies

        objective - target*denominator = sum lambda_ab R_ab + sum mu_i e_i

    with all lambda_ab and mu_i nonnegative rational numbers.
    """
    rows, labels, objective, denominator = metric_lp_data(n, generators)
    key = (n, tuple(sorted(generators)))
    if key not in RATIONAL_CERTIFICATES:
        return None
    raw_lambdas, raw_mus = RATIONAL_CERTIFICATES[key]
    lambdas = [(label, Fraction(*value)) for label, value in raw_lambdas]
    mus = [Fraction(*value) for value in raw_mus]
    assert all(value >= 0 for _, value in lambdas)
    assert all(value >= 0 for value in mus)

    right = mus[:]
    row_by_label = dict(zip(labels, rows))
    for label, multiplier in lambdas:
        for index, entry in enumerate(row_by_label[label]):
            right[index] += multiplier * entry
    left = [
        objective[index] - target * denominator[index]
        for index in range(len(objective))
    ]
    assert left == right
    return lambdas, mus


SQRT5 = sp.sqrt(5)


FOURIER_CASES = {
    # The first three are precisely the non-exact order-ten presentations.
    (10, (1, 3, 7, 9)): {
        "cut": sp.Rational(4, 5),
        "gl": sp.Rational(3, 4),
        "b": ((5 - SQRT5) / 10, 0, (5 + SQRT5) / 10, 0, 0),
        "triangles": (),
        "mu": (0, sp.Rational(1, 2), 0, sp.Rational(1, 2), sp.Rational(5, 4)),
    },
    (10, (1, 4, 6, 9)): {
        "cut": sp.Rational(4, 5),
        "gl": (15 + SQRT5) / 22,
        "b": (
            sp.Rational(4, 11) - 6 * SQRT5 / 55,
            sp.Rational(1, 11) + 3 * SQRT5 / 11,
            sp.Rational(4, 11) - 6 * SQRT5 / 55,
            0,
            sp.Rational(2, 11) - 3 * SQRT5 / 55,
        ),
        "triangles": (
            ((1, 1), (7 - SQRT5) / 88),
            ((1, 6), (7 - SQRT5) / 44),
            ((4, 4), (7 - SQRT5) / 88),
        ),
        "mu": (0, 0, 0, (15 + SQRT5) / 44, 0),
    },
    (10, (1, 2, 5, 8, 9)): {
        "cut": sp.Rational(5, 6),
        "gl": (10 + SQRT5) / 15,
        "b": (
            SQRT5 / 3,
            (3 - SQRT5) / 6,
            0,
            (3 - SQRT5) / 6,
            0,
        ),
        "triangles": (
            ((1, 2), (5 - SQRT5) / 25),
            ((2, 2), (5 - SQRT5) / 75),
        ),
        "mu": (0, 0, sp.Rational(2, 5), 0, (8 - SQRT5) / 15),
    },
    # This order-ten case is exact but needs negative type, not just triangles.
    (10, (1, 2, 3, 5, 7, 8, 9)): {
        "cut": sp.Rational(20, 21),
        "gl": sp.Rational(20, 21),
        "b": (sp.Rational(1, 3), 0, (3 - SQRT5) / 6, (1 + SQRT5) / 6, 0),
        "triangles": (((2, 2), sp.Rational(2, 21)),),
        "mu": (0, 0, 0, 0, sp.Rational(10, 21)),
    },
}


MULTIPARTITE_CASES = {
    (6, (1, 3, 5)): (2, 3),
    (8, (1, 3, 5, 7)): (2, 4),
    (9, (1, 2, 4, 5, 7, 8)): (3, 3),
    (10, (1, 3, 5, 7, 9)): (2, 5),
}


# Exact rational dual certificates.  A pair ``((a,b),(p,q))`` means the
# triangle f(a)+f(b)-f(a+b) has multiplier p/q.  The second tuple gives the
# nonnegative multipliers of f(1),...,f(floor(n/2)).
RATIONAL_CERTIFICATES = {
    (5, (1, 4)): (((((4, 4), (1, 3))),), ((0, 1), (0, 1))),
    (5, (1, 2, 3, 4)): ((), ((0, 1), (0, 1))),
    (6, (1, 5)): (
        (((1, 1), (1, 3)), ((4, 5), (1, 9))),
        ((0, 1), (0, 1), (0, 1)),
    ),
    (6, (2, 3, 4)): (
        (((2, 3), (2, 9)),),
        ((0, 1), (2, 9), (0, 1)),
    ),
    (6, (1, 2, 4, 5)): (
        (((4, 5), (1, 6)),),
        ((0, 1), (0, 1), (0, 1)),
    ),
    (6, (1, 2, 3, 4, 5)): ((), ((0, 1), (0, 1), (0, 1))),
    (7, (1, 6)): (
        (((1, 1), (1, 3)), ((5, 6), (1, 6))),
        ((0, 1), (0, 1), (0, 1)),
    ),
    (7, (1, 2, 5, 6)): (
        (((5, 6), (1, 4)),),
        ((0, 1), (0, 1), (0, 1)),
    ),
    (7, (1, 2, 3, 4, 5, 6)): ((), ((0, 1), (0, 1), (0, 1))),
    (8, (1, 7)): (
        (((1, 1), (5, 16)), ((1, 2), (3, 16)), ((1, 3), (1, 16))),
        ((0, 1), (0, 1), (0, 1), (0, 1)),
    ),
    (8, (1, 4, 7)): (
        (((1, 1), (1, 6)), ((1, 4), (1, 6))),
        ((0, 1), (0, 1), (0, 1), (1, 12)),
    ),
    (8, (1, 2, 6, 7)): (
        (((1, 1), (1, 16)), ((1, 2), (3, 16)), ((2, 2), (3, 32))),
        ((0, 1), (0, 1), (0, 1), (0, 1)),
    ),
    (8, (1, 2, 4, 6, 7)): (
        (((1, 2), (1, 5)),),
        ((0, 1), (0, 1), (0, 1), (1, 10)),
    ),
    (8, (1, 3, 4, 5, 7)): (
        (((1, 5), (1, 5)),),
        ((0, 1), (0, 1), (0, 1), (1, 10)),
    ),
    (8, (1, 2, 3, 5, 6, 7)): (
        (((1, 3), (1, 12)), ((2, 2), (1, 24))),
        ((0, 1), (0, 1), (0, 1), (0, 1)),
    ),
    (8, (1, 2, 3, 4, 5, 6, 7)): (
        (),
        ((0, 1), (0, 1), (0, 1), (0, 1)),
    ),
    (9, (1, 8)): (
        (((1, 1), (2, 5)), ((1, 2), (1, 10)), ((2, 2), (1, 10))),
        ((0, 1), (0, 1), (0, 1), (0, 1)),
    ),
    (9, (1, 2, 7, 8)): (
        (((1, 1), (1, 10)), ((1, 2), (3, 20)), ((2, 2), (3, 20))),
        ((0, 1), (0, 1), (0, 1), (0, 1)),
    ),
    (9, (1, 3, 6, 8)): (
        (((1, 3), (1, 6)), ((1, 6), (1, 6))),
        ((0, 1), (0, 1), (0, 1), (0, 1)),
    ),
    (9, (1, 2, 3, 6, 7, 8)): (
        (((1, 3), (2, 15)), ((2, 2), (1, 15))),
        ((0, 1), (0, 1), (0, 1), (0, 1)),
    ),
    (9, (1, 2, 3, 4, 5, 6, 7, 8)): (
        (),
        ((0, 1), (0, 1), (0, 1), (0, 1)),
    ),
    (10, (1, 9)): (
        (
            ((1, 1), (7, 25)),
            ((1, 2), (1, 5)),
            ((1, 3), (3, 25)),
            ((1, 4), (1, 25)),
        ),
        ((0, 1), (0, 1), (0, 1), (0, 1), (0, 1)),
    ),
    (10, (1, 5, 9)): (
        (((1, 1), (1, 9)), ((1, 5), (2, 9)), ((1, 6), (1, 9))),
        ((0, 1), (0, 1), (0, 1), (0, 1), (1, 18)),
    ),
    (10, (2, 5, 8)): (
        (((2, 2), (2, 9)), ((2, 5), (1, 9)), ((4, 5), (1, 9))),
        ((0, 1), (0, 1), (0, 1), (0, 1), (1, 18)),
    ),
    (10, (1, 2, 8, 9)): (
        (
            ((1, 1), (1, 10)),
            ((1, 2), (9, 50)),
            ((2, 2), (3, 25)),
            ((2, 3), (3, 50)),
        ),
        ((0, 1), (0, 1), (0, 1), (0, 1), (0, 1)),
    ),
    (10, (1, 4, 5, 6, 9)): (
        (((1, 1), (1, 15)), ((1, 6), (2, 15)), ((4, 4), (1, 15))),
        ((0, 1), (0, 1), (0, 1), (0, 1), (2, 15)),
    ),
    (10, (2, 4, 5, 6, 8)): (
        (((1, 6), (2, 25)), ((2, 2), (4, 25)), ((4, 5), (4, 25))),
        ((0, 1), (0, 1), (0, 1), (6, 25), (0, 1)),
    ),
    (10, (1, 2, 3, 7, 8, 9)): (
        (
            ((1, 3), (2, 15)),
            ((1, 4), (1, 25)),
            ((2, 2), (1, 15)),
            ((2, 3), (1, 25)),
        ),
        ((0, 1), (0, 1), (0, 1), (0, 1), (0, 1)),
    ),
    (10, (1, 2, 4, 6, 8, 9)): (
        (((1, 6), (1, 5)), ((2, 2), (1, 15)), ((2, 3), (1, 15))),
        ((0, 1), (0, 1), (0, 1), (1, 15), (0, 1)),
    ),
    (10, (1, 2, 4, 5, 6, 8, 9)): (
        (
            ((1, 6), (2, 15)),
            ((2, 2), (4, 105)),
            ((2, 5), (4, 105)),
            ((4, 5), (2, 105)),
        ),
        ((0, 1), (0, 1), (0, 1), (0, 1), (0, 1)),
    ),
    (10, (1, 2, 3, 4, 6, 7, 8, 9)): (
        (((1, 4), (1, 20)), ((2, 3), (1, 20))),
        ((0, 1), (0, 1), (0, 1), (0, 1), (0, 1)),
    ),
    (10, (1, 2, 3, 4, 5, 6, 7, 8, 9)): (
        (),
        ((0, 1), (0, 1), (0, 1), (0, 1), (0, 1)),
    ),
}


def fourier_vectors(n, generators):
    frequencies = range(1, n // 2 + 1)
    values = [
        [1 - sp.cos(2 * sp.pi * k * residue / n) for k in frequencies]
        for residue in range(n)
    ]
    objective = [
        sp.simplify(sum(values[s][k - 1] for s in generators) / len(generators))
        for k in frequencies
    ]
    return values, objective


def exact_nonnegative(expression):
    """Decide the signs needed here without trusting a decimal approximation."""
    expression = sp.radsimp(sp.simplify(expression))
    polynomial = sp.Poly(expression, SQRT5)
    if polynomial.degree() <= 0:
        return polynomial.nth(0) >= 0
    a = polynomial.nth(0)
    b = polynomial.nth(1)
    if b >= 0:
        return a >= 0 or (a < 0 and 5 * b * b >= a * a)
    return a >= 0 and a * a >= 5 * b * b


def verify_fourier_case(n, generators, data):
    values, objective = fourier_vectors(n, generators)
    b = tuple(map(sp.sympify, data["b"]))
    target = sp.sympify(data["gl"])
    assert sp.simplify(sum(b) - 1) == 0
    assert all(exact_nonnegative(value) for value in b)

    # Exact primal: the stated Fourier metric satisfies every triangle and has
    # objective target under D=sum b=1.
    for a in range(n):
        for c in range(n):
            slack = sum(
                b[k - 1]
                * (values[a][k - 1] + values[c][k - 1] - values[(a + c) % n][k - 1])
                for k in range(1, n // 2 + 1)
            )
            assert exact_nonnegative(slack)
    assert sp.simplify(sum(objective[k] * b[k] for k in range(len(b))) - target) == 0

    # Exact dual identity in Fourier-weight coordinates.
    right = list(map(sp.sympify, data["mu"]))
    for (a, c), multiplier in data["triangles"]:
        multiplier = sp.sympify(multiplier)
        assert exact_nonnegative(multiplier)
        for k in range(len(right)):
            right[k] += multiplier * (
                values[a][k] + values[c][k] - values[(a + c) % n][k]
            )
    left = [sp.simplify(value - target) for value in objective]
    assert all(exact_nonnegative(value) for value in data["mu"])
    assert all(sp.simplify(x - y) == 0 for x, y in zip(left, right))


def characteristic_polynomial(n, generators):
    adjacency = sp.zeros(n)
    for x in range(n):
        for s in generators:
            adjacency[x, (x + s) % n] = 1
    return tuple(adjacency.charpoly().all_coeffs())


def main():
    rows = []
    counts = {}
    for n in range(5, 11):
        representatives = orbit_representatives(n)
        counts[n] = len(representatives)
        for generators in representatives:
            key = (n, tuple(sorted(generators)))
            cut, subset, boundary = exact_cut_optimum(n, generators)
            if key in FOURIER_CASES:
                data = FOURIER_CASES[key]
                assert sp.Rational(cut.numerator, cut.denominator) == data["cut"]
                verify_fourier_case(n, generators, data)
                gl_value = str(data["gl"])
                method = "Fourier-Q(sqrt(5))"
            elif key in MULTIPARTITE_CASES:
                parts, part_size = MULTIPARTITE_CASES[key]
                assert n == parts * part_size
                assert cut == 1
                # Differences outside the index-parts subgroup are exactly S.
                subgroup = {parts * j % n for j in range(part_size)}
                assert generators == frozenset(set(range(n)) - subgroup)
                gl_value = "1"
                method = f"K_{{{parts}x{part_size}}}-centroid"
            else:
                certificate = rational_metric_certificate(n, generators, cut)
                assert certificate is not None
                gl_value = str(cut)
                method = "rational-metric-dual"
            rows.append(
                (n, tuple(sorted(generators)), str(cut), gl_value, subset, boundary, method)
            )

    assert counts == {5: 2, 6: 5, 7: 3, 8: 8, 9: 6, 10: 16}

    # Distinct characteristic polynomials prove that all 16 order-ten
    # presentation-orbit representatives are pairwise nonisomorphic as graphs.
    order_ten = orbit_representatives(10)
    polynomials = [characteristic_polynomial(10, s) for s in order_ten]
    assert len(set(polynomials)) == 16

    nonexact = []
    for n, generators, cut, gl_value, subset, boundary, method in rows:
        print(
            f"n={n} S={list(generators)} cut={cut} GL={gl_value} "
            f"cut_witness={list(subset)} boundary={boundary} method={method}"
        )
        if (n, generators) in FOURIER_CASES:
            data = FOURIER_CASES[(n, generators)]
            if sp.simplify(data["cut"] - data["gl"]) > 0:
                nonexact.append((generators, data["cut"], data["gl"]))
    assert len(nonexact) == 3
    print("order-10 characteristic polynomials: 16/16 distinct")
    print("non-exact order-10 presentation orbits:")
    for generators, cut, gl_value in nonexact:
        print(f"  S={list(generators)} cut={cut} GL={gl_value}")


if __name__ == "__main__":
    main()
