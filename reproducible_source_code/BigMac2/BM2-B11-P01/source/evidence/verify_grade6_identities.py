#!/usr/bin/env python3
"""Exact-rational checks of the grade-six identities used in the proof dossier.

This is a finite algebra check, not a proof of asymptotic convergence.  It
recomputes four restart-4 blocks from rational spectral data and verifies the
annihilator, polynomial-division, energy, drift, and sign-transport identities.
"""

from fractions import Fraction as F


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(p, q):
    n = max(len(p), len(q))
    return trim([(p[i] if i < len(p) else F(0)) +
                 (q[i] if i < len(q) else F(0)) for i in range(n)])


def scale(p, c):
    return trim([c * x for x in p])


def sub(p, q):
    return add(p, scale(q, -1))


def mul(p, q):
    out = [F(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i + j] += x * y
    return trim(out)


def evaluate(p, x):
    out = F(0)
    for c in reversed(p):
        out = out * x + c
    return out


def divmod_poly(p, q):
    p = trim(p)
    q = trim(q)
    if q == [F(0)]:
        raise ZeroDivisionError
    if len(p) < len(q):
        return [F(0)], p
    quotient = [F(0)] * (len(p) - len(q) + 1)
    remainder = p[:]
    while len(remainder) >= len(q) and remainder != [F(0)]:
        shift = len(remainder) - len(q)
        coeff = remainder[-1] / q[-1]
        quotient[shift] = coeff
        subtractor = [F(0)] * shift + scale(q, coeff)
        remainder = sub(remainder, subtractor)
    return trim(quotient), trim(remainder)


def solve(matrix, rhs):
    a = [list(row) + [rhs[i]] for i, row in enumerate(matrix)]
    n = len(a)
    for col in range(n):
        pivot = next(row for row in range(col, n) if a[row][col] != 0)
        a[col], a[pivot] = a[pivot], a[col]
        d = a[col][col]
        a[col] = [x / d for x in a[col]]
        for row in range(n):
            if row == col:
                continue
            d = a[row][col]
            if d:
                a[row] = [a[row][j] - d * a[col][j]
                          for j in range(n + 1)]
    return [a[i][-1] for i in range(n)]


def monic_orthogonal_degree_four(nodes, weights):
    moments = [sum(weights[i] * nodes[i] ** j for i in range(6))
               for j in range(9)]
    matrix = [[moments[i + j] for i in range(4)] for j in range(4)]
    rhs = [-moments[j + 4] for j in range(4)]
    p = solve(matrix, rhs) + [F(1)]
    assert all(sum(weights[i] * evaluate(p, nodes[i]) * nodes[i] ** j
                   for i in range(6)) == 0 for j in range(4))
    h = sum(weights[i] * evaluate(p, nodes[i]) ** 2 for i in range(6))
    assert h > 0
    return p, h


def node_polynomial(nodes):
    delta = [F(1)]
    for x in nodes:
        delta = mul(delta, [-x, F(1)])
    return delta


def barycentric_denominators(nodes):
    return [evaluate(mul_all([[-nodes[j], F(1)]
                              for j in range(6) if j != i]), nodes[i])
            for i in range(6)]


def mul_all(polynomials):
    out = [F(1)]
    for p in polynomials:
        out = mul(out, p)
    return out


def annihilator_root(nodes, weights, p, h, denominators):
    candidates = [nodes[i] - weights[i] * evaluate(p, nodes[i]) *
                  denominators[i] / h for i in range(6)]
    assert len(set(candidates)) == 1
    return candidates[0]


def restart(nodes, weights):
    p, h = monic_orthogonal_degree_four(nodes, weights)
    values = [evaluate(p, x) for x in nodes]
    next_weights = [weights[i] * values[i] ** 2 / h for i in range(6)]
    assert sum(next_weights) == 1
    return p, h, next_weights


def completion_functional(delta, p):
    """Return J and f -> [t^3](J f mod p), with deg(J Delta mod p)<=1."""
    basis = []
    for factor in ([F(0), F(0), F(1)], [F(0), F(1)], [F(1)]):
        _, remainder = divmod_poly(mul(factor, delta), p)
        remainder += [F(0)] * (4 - len(remainder))
        basis.append(remainder)
    # Unknown order is (j0,j1), whereas basis order is (t^2,t,1).
    matrix = [[basis[col][degree] for col in (2, 1)] for degree in (2, 3)]
    rhs = [-basis[0][degree] for degree in (2, 3)]
    j0, j1 = solve(matrix, rhs)
    j = [j0, j1, F(1)]
    _, remainder = divmod_poly(mul(j, delta), p)
    assert len(remainder) <= 2

    def functional(f):
        _, r = divmod_poly(mul(j, f), p)
        return r[3] if len(r) > 3 else F(0)

    return j, functional


def main():
    nodes = list(map(F, [1, 2, 4, 7, 11, 16]))
    raw_weights = list(map(F, [2, 3, 5, 7, 11, 13]))
    total = sum(raw_weights)
    weights = [[x / total for x in raw_weights]]
    polynomials = []
    energies = []
    for _ in range(5):
        p, h, next_weights = restart(nodes, weights[-1])
        polynomials.append(p)
        energies.append(h)
        weights.append(next_weights)

    delta = node_polynomial(nodes)
    denominators = barycentric_denominators(nodes)
    roots = [annihilator_root(nodes, weights[k], polynomials[k],
                              energies[k], denominators) for k in range(5)]

    defects = []
    kernels = []
    for k in range(4):
        s = [-roots[k], F(1)]
        s_next = [-roots[k + 1], F(1)]
        numerator = sub(mul(s, mul(polynomials[k], polynomials[k + 1])),
                        scale(s_next, energies[k + 1]))
        b, remainder = divmod_poly(numerator, delta)
        assert remainder == [F(0)] and len(b) == 4 and b[-1] == 1
        ell, u_remainder = divmod_poly(b, s)
        assert len(ell) == 3 and ell[-1] == 1 and len(u_remainder) == 1
        u = u_remainder[0]
        defects.append(u)
        delta_minus_value = sub(delta, [evaluate(delta, roots[k])])
        kernel, remainder = divmod_poly(delta_minus_value, s)
        assert remainder == [F(0)]
        kernels.append(kernel)

        q = mul(polynomials[k], polynomials[k + 1])
        asserted_q = add([energies[k + 1]],
                         add(mul(delta, ell), scale(kernel, u)))
        assert q == asserted_q
        assert roots[k + 1] - roots[k] == evaluate(delta, roots[k]) * u / energies[k + 1]
        energy_rhs = u * u / energies[k + 1] * sum(
            weights[k][i] * evaluate(kernel, nodes[i]) ** 2 for i in range(6))
        assert energies[k + 1] - energies[k] == energy_rhs

    for k in range(3):
        _, functional = completion_functional(delta, polynomials[k + 1])
        assert functional([F(1)]) == 0
        assert functional(delta) == 0
        assert functional(mul([F(0), F(1)], delta)) == 0
        assert defects[k + 1] * functional(kernels[k + 1]) == \
               defects[k] * functional(kernels[k])

    # Check the limiting identity L_P(K_a)=Q(a) on an exact rational
    # factorization P Q = h + Delta L.  Real-root hypotheses are needed for
    # the convergence proof, but not for this polynomial identity.
    p_fixed = list(map(F, [7, 5, 3, 2, 1]))
    ell_fixed = list(map(F, [1, 1, 1]))
    h_fixed = F(3)
    q_base = list(map(F, [0, 0, 2, -1, 1]))
    remainder_columns = []
    for basis_q in ([F(1)], [F(0), F(1)], q_base):
        _, remainder = divmod_poly(mul(p_fixed, basis_q), ell_fixed)
        remainder += [F(0)] * (2 - len(remainder))
        remainder_columns.append(remainder)
    matrix = [[remainder_columns[col][degree] for col in (0, 1)]
              for degree in (0, 1)]
    rhs = [(h_fixed if degree == 0 else F(0)) -
           remainder_columns[2][degree] for degree in (0, 1)]
    q0, q1 = solve(matrix, rhs)
    q_fixed = add(q_base, [q0, q1])
    delta_fixed, remainder = divmod_poly(
        sub(mul(p_fixed, q_fixed), [h_fixed]), ell_fixed)
    assert remainder == [F(0)] and len(delta_fixed) == 7
    j_fixed, functional = completion_functional(delta_fixed, p_fixed)
    assert j_fixed == ell_fixed
    for a in map(F, [-2, 0, 1, 3]):
        kernel, remainder = divmod_poly(
            sub(delta_fixed, [evaluate(delta_fixed, a)]), [-a, F(1)])
        assert remainder == [F(0)]
        assert functional(kernel) == evaluate(q_fixed, a)

    max_bits = max(max(abs(x.numerator).bit_length() + x.denominator.bit_length()
                       for x in p) for p in polynomials)
    print("PASS: 5 blocks; 4 division/drift/energy checks; "
          "3 exact sign-transport checks; 4 limiting-functional checks")
    print("nodes=1,2,4,7,11,16; initial_weights=2,3,5,7,11,13 / 41")
    print(f"largest polynomial-coefficient numerator+denominator bit length: {max_bits}")


if __name__ == "__main__":
    main()
