#!/usr/bin/env python3
"""Independent exact check of the positive (n,k)=(4,3) certificate.

This implementation does not construct or multiply the 20-by-20 rho matrices
used by the triage verifier.  Instead, SymPy differentiates polynomials
directly, the three Lie algebra factors are applied one at a time in operator
order, and SymPy's exact integer determinant routine checks the resulting
coefficient matrices.
"""

from itertools import product

from sympy import Matrix, Poly, diff, expand, symbols


X1 = Matrix(
    [
        [2, 0, 0, -1],
        [1, 0, 0, -2],
        [1, -1, 1, 0],
        [-1, -1, 1, -3],
    ]
)
X2 = Matrix(
    [
        [2, 1, 2, 2],
        [0, -2, 2, -1],
        [-2, -1, 2, -1],
        [2, 1, -2, -2],
    ]
)
X3 = Matrix(
    [
        [1, 1, 0, 0],
        [1, 1, 0, 1],
        [2, 1, -2, 1],
        [-2, -2, -1, 0],
    ]
)

z = symbols("e1 e2 e3 e4")

# The explicit sort makes the convention independent of product's iteration
# details.  It agrees with the frozen lexicographic exponent basis.
BASIS = sorted(t for t in product(range(4), repeat=4) if sum(t) == 3)
U_BASIS = [t for t in BASIS if t[3] == 0]
QUOTIENT_BASIS = [t for t in BASIS if t[3] > 0]


def monomial(exponent):
    """Return e1^a e2^b e3^c e4^d for an exponent tuple."""
    out = 1
    for variable, power in zip(z, exponent):
        out *= variable**power
    return out


def derived_action(x, polynomial):
    """Apply sum_ij x_ij e_i (partial/partial e_j) directly."""
    return expand(
        sum(
            x[i, j] * z[i] * diff(polynomial, z[j])
            for i in range(4)
            for j in range(4)
        )
    )


def m2_image(polynomial):
    """Apply rho(X1)rho(X2)rho(X3): X3 is the first acting factor."""
    for factor in (X3, X2, X1):
        polynomial = derived_action(factor, polynomial)
    return polynomial


def coefficient_column(polynomial, row_basis):
    """Exact coefficient column of a homogeneous cubic."""
    polynomial = Poly(polynomial, *z, domain="ZZ")
    return [polynomial.coeff_monomial(monomial(t)) for t in row_basis]


def main():
    traces = [x.trace() for x in (X1, X2, X3)]
    assert traces == [0, 0, 0]
    assert len(BASIS) == 20
    assert len(U_BASIS) == len(QUOTIENT_BASIS) == 10

    images = [m2_image(monomial(t)) for t in U_BASIS]

    # Projection V -> V/U.  If these ten projected images are independent,
    # then U + m2(U) = V.  This is a smaller exact certificate than the full
    # spanning determinant.
    quotient_columns = [coefficient_column(p, QUOTIENT_BASIS) for p in images]
    quotient_matrix = Matrix.hstack(*(Matrix(c) for c in quotient_columns))
    quotient_determinant = quotient_matrix.det(method="domain-ge")

    u_columns = [coefficient_column(monomial(t), BASIS) for t in U_BASIS]
    image_columns = [coefficient_column(p, BASIS) for p in images]
    spanning_matrix = Matrix.hstack(
        *(Matrix(c) for c in u_columns + image_columns)
    )
    spanning_determinant = spanning_matrix.det(method="domain-ge")

    print("implementation = direct symbolic differentiation (SymPy)")
    print("basis =", BASIS)
    print("U basis =", U_BASIS)
    print("V/U row basis =", QUOTIENT_BASIS)
    print("traces =", traces)
    print("operator order = X3 first, then X2, then X1")
    print("projected m2(U) coefficient matrix =")
    print(quotient_matrix.tolist())
    print("10x10 quotient determinant =", quotient_determinant)
    print("20x20 spanning determinant =", spanning_determinant)

    assert quotient_determinant != 0
    assert spanning_determinant == 8412259151430144
    print("independent_certificate_verified = true")


if __name__ == "__main__":
    main()
