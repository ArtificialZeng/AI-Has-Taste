#!/usr/bin/env python3
"""Exact Fourier-block certificate for the frozen (m,n)=(4,2) problem.

The calculation is independent of evidence/triage_exact_check.py.  It starts
from the two explicit state-transition rules, constructs both integer
adjacency matrices, and checks the claimed Fourier intertwiners over the
Gaussian integers before multiplying the 2-by-2 block determinants.
"""

import sympy as sp


I = sp.I
X = sp.symbols("x")
D = (2, 0, -2, 0)  # i^j+i^(-j), j=0,1,2,3


def cayley_certificate():
    # t=0 means label order (1,2), t=1 means (2,1); a,b are positional colors.
    states = [(t, a, b) for t in range(2) for a in range(4) for b in range(4)]
    index = {state: j for j, state in enumerate(states)}
    adjacency = sp.zeros(32)
    for row, (t, a, b) in enumerate(states):
        for eps in (-1, 1):
            adjacency[row, index[(t, (a + eps) % 4, b)]] += 1
            adjacency[row, index[(1 - t, (b + eps) % 4, (a + eps) % 4)]] += 1

    # For each ordered (k,l), columns are F_{0,k,l} and F_{1,l,k}.
    fourier = sp.zeros(32)
    blocks = []
    factors = []
    column = 0
    for k in range(4):
        for ell in range(4):
            c = D[(k + ell) % 4]
            block = sp.Matrix([[D[k], c], [c, D[ell]]])
            blocks.append(block)
            factors.append(sp.factor((X - D[k]) * (X - D[ell]) - c**2))
            for row, (t, a, b) in enumerate(states):
                if t == 0:
                    fourier[row, column] = I ** ((k * a + ell * b) % 4)
                else:
                    fourier[row, column + 1] = I ** ((ell * a + k * b) % 4)
            column += 2

    block_diagonal = sp.diag(*blocks)
    assert adjacency == adjacency.T
    assert all(sum(adjacency.row(j)) == 4 for j in range(32))
    assert fourier.conjugate().T * fourier == 16 * sp.eye(32)
    assert adjacency * fourier == fourier * block_diagonal

    product = sp.factor(sp.prod(factors))
    expected = X**10 * (X - 4) * (X - 2)**8 * (X + 2)**8 * (X + 4) * (X**2 - 8)**2
    assert sp.expand(product - expected) == 0
    assert sp.expand(adjacency.charpoly(X).as_expr() - expected) == 0
    return states, adjacency, factors, product


def schreier_certificate():
    states = [(a, p) for a in range(4) for p in (1, 2)]
    index = {state: j for j, state in enumerate(states)}
    adjacency = sp.zeros(8)
    for row, (a, p) in enumerate(states):
        for eps in (-1, 1):
            # length one
            image = ((a + eps) % 4, 1) if p == 1 else (a, 2)
            adjacency[row, index[image]] += 1
            # length two
            adjacency[row, index[((a + eps) % 4, 3 - p)]] += 1

    # For each k, columns are the Fourier functions supported at p=1 and p=2.
    fourier = sp.zeros(8)
    blocks = []
    factors = []
    column = 0
    for k in range(4):
        d = D[k]
        block = sp.Matrix([[d, d], [d, 2]])
        blocks.append(block)
        factors.append(sp.factor((X - d) * (X - 2) - d**2))
        for row, (a, p) in enumerate(states):
            fourier[row, column + p - 1] = I ** ((k * a) % 4)
        column += 2

    block_diagonal = sp.diag(*blocks)
    assert adjacency == adjacency.T
    assert all(sum(adjacency.row(j)) == 4 for j in range(8))
    assert fourier.conjugate().T * fourier == 4 * sp.eye(8)
    assert adjacency * fourier == fourier * block_diagonal

    product = sp.factor(sp.prod(factors))
    expected = X**3 * (X - 4) * (X - 2)**2 * (X**2 - 8)
    assert sp.expand(product - expected) == 0
    assert sp.expand(adjacency.charpoly(X).as_expr() - expected) == 0
    return states, adjacency, factors, product


def main():
    cay_states, cay, cay_factors, cay_product = cayley_certificate()
    sch_states, sch, sch_factors, sch_product = schreier_certificate()
    print("Cayley state order:", cay_states)
    print("Cayley 2x2 determinant factors by rows k=0,1,2,3:")
    for k in range(4):
        print(k, cay_factors[4 * k : 4 * k + 4])
    print("Cayley characteristic polynomial:", cay_product)
    print("Schreier state order:", sch_states)
    print("Schreier matrix:")
    print(sch)
    print("Schreier block determinant factors:", sch_factors)
    print("Schreier characteristic polynomial:", sch_product)
    print("Both second adjacency eigenvalues are 2*sqrt(2).")
    print("Both unnormalized adjacency gaps are 4-2*sqrt(2).")


if __name__ == "__main__":
    main()
