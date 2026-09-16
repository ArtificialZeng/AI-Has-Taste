#!/usr/bin/env python3
"""Exact certificates for the three small-prime counterexamples over F_5.

No nonstandard packages are used.  The script enumerates all affine points,
checks nonsingularity, computes Frobenius traces/polynomials, and verifies the
claimed rational canonical form data modulo 2, 3, and 7.
"""

P = 5

CURVES = {
    "E_minus4": (3, 0),  # y^2 = x^3 + 3x
    "E_0": (0, 1),       # y^2 = x^3 + 1
    "E_1": (3, 2),       # y^2 = x^3 + 3x + 2
    "E_minus2": (4, 0),  # y^2 = x^3 + 4x
    "E_3": (4, 2),       # y^2 = x^3 + 4x + 2
}


def affine_fibers(a, b):
    return [
        (x, (x**3 + a*x + b) % P,
         [y for y in range(P) if y*y % P == (x**3 + a*x + b) % P])
        for x in range(P)
    ]


def poly_eval(coeffs, x, ell):
    value = 0
    for coefficient in coeffs:
        value = (value*x + coefficient) % ell
    return value


records = {}
for name, (a, b) in CURVES.items():
    fibers = affine_fibers(a, b)
    count = 1 + sum(len(ys) for _, _, ys in fibers)  # point at infinity
    trace = P + 1 - count
    discriminant_factor = (4*a**3 + 27*b**2) % P
    roots = [x for x in range(P) if (x**3 + a*x + b) % P == 0]
    assert discriminant_factor != 0
    assert -4 <= trace <= 4
    records[name] = {
        "a": a,
        "b": b,
        "fibers": fibers,
        "count": count,
        "trace": trace,
        "disc_factor": discriminant_factor,
        "roots": roots,
    }

expected = {
    "E_minus4": (10, -4, [0]),
    "E_0": (6, 0, [4]),
    "E_1": (5, 1, []),
    "E_minus2": (8, -2, [0, 1, 4]),
    "E_3": (3, 3, []),
}
for name, (count, trace, roots) in expected.items():
    record = records[name]
    assert (record["count"], record["trace"], record["roots"]) == (count, trace, roots)

# Pair entries are (ell, first curve, second curve, common polynomial [1,c1,c0],
# companion matrix in row-major order).
pairs = [
    (2, "E_minus4", "E_0", [1, 0, 1], [[0, 1], [1, 0]]),
    (3, "E_1", "E_minus2", [1, 2, 2], [[0, 1], [1, 1]]),
    (7, "E_minus4", "E_3", [1, 4, 5], [[0, 2], [1, 3]]),
]

for ell, first, second, polynomial, companion in pairs:
    r1, r2 = records[first], records[second]
    reduced1 = [1, (-r1["trace"]) % ell, P % ell]
    reduced2 = [1, (-r2["trace"]) % ell, P % ell]
    assert reduced1 == reduced2 == polynomial
    # det(TI-C) = T^2 - tr(C)T + det(C).
    matrix_poly = [
        1,
        (-(companion[0][0] + companion[1][1])) % ell,
        (companion[0][0]*companion[1][1] - companion[0][1]*companion[1][0]) % ell,
    ]
    assert matrix_poly == polynomial
    if ell in (3, 7):
        # No root in the base field: the common quadratic is irreducible, so
        # every operator having it as characteristic polynomial is cyclic.
        assert all(poly_eval(polynomial, x, ell) != 0 for x in range(ell))
    else:
        # Exactly one rational root of each defining cubic means exactly two
        # rational 2-torsion points (including O), so ker(Frob-I) has dimension
        # one.  Thus Frob is not I and its minimal polynomial is (T+1)^2.
        assert len(r1["roots"]) == len(r2["roots"]) == 1

for name, record in records.items():
    print(f"{name}: y^2=x^3+{record['a']}x+{record['b']}")
    print(f"  4a^3+27b^2 mod 5 = {record['disc_factor']} (nonsingular)")
    print("  fibers (x,rhs,ys) = " + repr(record["fibers"]))
    print(f"  #E(F_5)={record['count']}, trace={record['trace']}, "
          f"P(T)=T^2-({record['trace']})T+5, cubic roots={record['roots']}")

for ell, first, second, polynomial, companion in pairs:
    print(f"ell={ell}, pair=({first},{second})")
    print(f"  common reduced characteristic polynomial coefficients={polynomial}")
    print(f"  common rational canonical matrix={companion}")
    if ell in (3, 7):
        print("  certificate: polynomial has no root, hence is irreducible and minimal")
    else:
        print("  certificate: each fixed 2-torsion subspace has dimension 1, "
              "hence minimal polynomial=(T+1)^2")

print("ALL EXACT CERTIFICATE CHECKS PASSED")
