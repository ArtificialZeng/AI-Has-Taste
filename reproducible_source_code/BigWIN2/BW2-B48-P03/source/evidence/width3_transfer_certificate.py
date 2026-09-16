#!/usr/bin/env python3
"""Machine-checkable certificate for the width-three transfer proof.

Polynomials are tuples of exact integer coefficients in ascending order.  The
two states record whether the top and bottom colors of the last column agree
(A) or whether all three colors are distinct (B).
"""

from chromatic_fk_transfer import chromatic_polynomial, eval_poly


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return tuple(p)


def add(p, q):
    n = max(len(p), len(q))
    return trim(tuple((p[i] if i < len(p) else 0) +
                      (q[i] if i < len(q) else 0) for i in range(n)))


def mul(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return trim(out)


def peval(p, q):
    return eval_poly(p, q)


# M[old_type][new_type].
a = (3, -3, 1)            # q^2 - 3q + 3
b = (5, -4, 1)            # q^2 - 4q + 5
c = mul((-2, 1), b)       # (q-2)(q^2 - 4q + 5)
d = (-13, 14, -6, 1)      # q^3 - 6q^2 + 14q - 13
M = ((a, c), (b, d))

# v_1=(q(q-1),q(q-1)(q-2)).
v = ((0, -1, 1), (0, 2, -3, 1))


def step(v):
    return tuple(add(mul(v[0], M[0][j]), mul(v[1], M[1][j]))
                 for j in range(2))


def classify_count(q, old_type, new_type):
    old = (0, 1, 0) if old_type == 0 else (0, 1, 2)
    ans = 0
    for x in range(q):
        for y in range(q):
            for z in range(q):
                if x == y or y == z:
                    continue
                if x == old[0] or y == old[1] or z == old[2]:
                    continue
                if (x == z) == (new_type == 0):
                    ans += 1
    return ans


def main():
    print("transition_polynomials_low_to_high=" + repr(M))
    for q in range(3, 13):
        observed = tuple(tuple(classify_count(q, i, j) for j in range(2))
                         for i in range(2))
        predicted = tuple(tuple(peval(M[i][j], q) for j in range(2))
                          for i in range(2))
        assert observed == predicted
    print("direct_transition_enumeration_check=q=3..12: PASS")

    current = v
    for m in range(1, 10):
        transfer_poly = add(*current)
        fk_poly, _, _ = chromatic_polynomial(3, m)
        assert trim(fk_poly) == transfer_poly
        chi_minus_one = peval(transfer_poly, -1)
        ao = (-1) ** (3 * m) * chi_minus_one
        print(f"m={m} chi(-1)={chi_minus_one} "
              f"acyclic_orientations={ao} residue={ao % 4}")
        current = step(current)
    print("full_FK_polynomial_crosscheck=m=1..9: PASS")

    matrix_at_minus_one = tuple(tuple(peval(x, -1) for x in row) for row in M)
    initial_at_minus_one = tuple(peval(x, -1) for x in v)
    initial_mod4 = tuple(x % 4 for x in initial_at_minus_one)
    second_mod4 = tuple(sum(initial_mod4[i] * matrix_at_minus_one[i][j]
                            for i in range(2)) % 4 for j in range(2))
    fixed_image = tuple(sum(second_mod4[i] * matrix_at_minus_one[i][j]
                            for i in range(2)) % 4 for j in range(2))
    print("M(-1)=" + repr(matrix_at_minus_one))
    print("M(-1)_mod4=" + repr(tuple(tuple(x % 4 for x in row)
                                      for row in matrix_at_minus_one)))
    print("v1(-1)=" + repr(initial_at_minus_one))
    print("v1(-1)_mod4=" + repr(initial_mod4))
    print("v2(-1)_mod4=" + repr(second_mod4))
    print("v2_times_M(-1)_mod4=" + repr(fixed_image))
    assert second_mod4 == (2, 0) == fixed_image
    print("mod4_fixed_orbit_certificate: PASS")


if __name__ == "__main__":
    main()
