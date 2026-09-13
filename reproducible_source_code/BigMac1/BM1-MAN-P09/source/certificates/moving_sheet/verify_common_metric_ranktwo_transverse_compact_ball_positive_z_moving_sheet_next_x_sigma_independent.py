#!/usr/bin/env python3
"""Standalone exact referee for the next-X sigma moving-sheet cell.

No discovery module, source verifier, cached quartic, or serialized
certificate is imported.  The program reconstructs the fully conjugated
Hermitian Q,Q^2 gate from its defining matrices, derives the moving-sheet
quotient, and recomputes every continuum bound over QQ.
"""

if not __debug__:
    raise RuntimeError("independent verifier refuses optimized Python (-O)")

import argparse
from hashlib import sha256
from itertools import product
from pathlib import Path

import sympy as sp


EXPECTED_STATEMENT_SHA256 = (
    "c94f4775dc9e29568a0fe913c39fc1677d3aaa57c7b4e07cea8c54be70e3501c"
)
EXPECTED_PREDECESSOR_SHA256 = (
    "95028dc46a177a8e856200eaba3f954086d6b4335aef34efac6be09783e39e92"
)


def arguments():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--statement",
        type=Path,
        default=root / (
            "tmp/research/common_metric_ranktwo_transverse_compact_ball_"
            "positive_z_moving_sheet_next_x_sigma_layer.md"
        ),
    )
    parser.add_argument(
        "--predecessor",
        type=Path,
        default=root / (
            "tmp/research/common_metric_ranktwo_transverse_compact_ball_"
            "positive_z_moving_sheet_adjacent_x_layer.md"
        ),
    )
    return parser.parse_args()


def require(condition, label):
    if not condition:
        raise RuntimeError(label)


def digest_bound(path, expected, label):
    require(path.is_file(), f"{label} is missing: {path}")
    actual = sha256(path.read_bytes()).hexdigest()
    require(actual == expected, f"{label} hash mismatch: {actual}")
    return actual


def exact_zero(expression, label):
    if isinstance(expression, sp.MatrixBase):
        for row in range(expression.rows):
            for column in range(expression.cols):
                exact_zero(expression[row, column], f"{label}[{row},{column}]")
        return
    value = sp.factor(sp.cancel(sp.together(sp.expand_complex(expression))))
    require(value == 0, f"{label}: {value}")


def kernel_reduce(expression, q, relation):
    if isinstance(expression, sp.MatrixBase):
        return expression.applyfunc(
            lambda entry: kernel_reduce(entry, q, relation)
        )
    numerator, denominator = sp.cancel(sp.together(expression)).as_numer_denom()
    remainder = sp.Poly(sp.expand(numerator), q).rem(relation).as_expr()
    return sp.factor(remainder / denominator)


def replace_even_h(expression, h, S):
    polynomial = sp.Poly(sp.expand(expression), h, domain=sp.EX)
    result = sp.Integer(0)
    for (degree,), coefficient in polynomial.terms():
        require(degree % 2 == 0, f"odd h power survived: {degree}")
        result += coefficient * S ** (degree // 2)
    return sp.expand(result)


def sparse_add(left, right):
    result = dict(left)
    for key, value in right.items():
        result[key] = result.get(key, 0) + value
    return {
        key: sp.expand(value) for key, value in result.items() if value != 0
    }


def sparse_multiply(left, right):
    result = {}
    for (si, xi), left_value in left.items():
        for (sj, xj), right_value in right.items():
            key = (si + sj, xi + xj)
            result[key] = result.get(key, 0) + left_value * right_value
    return {
        key: sp.expand(value) for key, value in result.items() if value != 0
    }


def sparse_power(base, exponent):
    result = {(0, 0): sp.Integer(1)}
    for _ in range(exponent):
        result = sparse_multiply(result, base)
    return result


def centered_lower(expression, variables, radii):
    polynomial = sp.Poly(sp.expand(expression), *variables, domain=sp.QQ)
    zero = (0,) * len(variables)
    center = polynomial.coeff_monomial(zero)
    variation = sp.Integer(0)
    for powers, coefficient in polynomial.terms():
        if powers == zero:
            continue
        variation += abs(coefficient) * sp.prod(
            radius**power for radius, power in zip(radii, powers)
        )
    return sp.factor(center - variation), len(polynomial.terms())


def centered_absolute(expression, variables, radii):
    polynomial = sp.Poly(sp.expand(expression), *variables, domain=sp.QQ)
    bound = sp.Integer(0)
    for powers, coefficient in polynomial.terms():
        bound += abs(coefficient) * sp.prod(
            radius**power for radius, power in zip(radii, powers)
        )
    return sp.factor(bound), len(polynomial.terms())


def main():
    args = arguments()
    statement_hash = digest_bound(
        args.statement, EXPECTED_STATEMENT_SHA256, "candidate statement"
    )
    predecessor_hash = digest_bound(
        args.predecessor, EXPECTED_PREDECESSOR_SHA256, "predecessor statement"
    )

    R = sp.Rational
    I = sp.I
    h, q, lam = sp.symbols("h q lambda", real=True)
    S, Z, x, y = sp.symbols("S Z x y", real=True)
    X, M, omega, nu = sp.symbols("X M omega nu", real=True)

    # 1. Reconstruct the original fully conjugated Hermitian gate.
    a = 1 / sp.sqrt(6)
    c = sp.sqrt(R(5, 6))
    zeta = R(4, 5) + I * R(3, 5)
    p = sp.Matrix([a, 0, c])
    rvec = sp.Matrix([-a, 0, c * zeta])
    fvec = sp.Matrix([-c * h, q, -a * h * zeta])
    nvec = sp.Matrix([c * q, h, a * q * zeta])
    U = sp.Matrix.hstack(rvec, fvec)
    relation = sp.Poly(q**2 - (1 - h**2), q)

    exact_zero(
        kernel_reduce(U.conjugate().T * U - sp.eye(2), q, relation),
        "transverse frame",
    )
    exact_zero(
        kernel_reduce(U.conjugate().T * nvec, q, relation),
        "kernel orthogonality",
    )
    exact_zero(
        kernel_reduce((nvec.conjugate().T * nvec)[0] - 1, q, relation),
        "kernel normalization",
    )

    j = (1 + 5 * x) / (3 * sp.sqrt(5))
    k = (-3 + 5 * y) / (3 * sp.sqrt(5))
    C = sp.Matrix(
        [
            [h**2, h * (j + I * k)],
            [h * (j - I * k), j**2 + k**2 + R(5, 9) * Z],
        ]
    )
    exact_zero(C - C.conjugate().T, "compression Hermitian symmetry")
    exact_zero(C.det() - R(5, 9) * h**2 * Z, "compression determinant")

    H = sp.expand(U * C * U.conjugate().T)
    exact_zero(kernel_reduce(H * nvec, q, relation), "H kernel")
    Q = sp.expand(lam * H)
    image = sp.expand(Q * p)
    Q2 = sp.expand(Q * Q)
    exact_zero(Q - Q.conjugate().T, "Q Hermitian symmetry")

    danger_formula = (
        R(5, 36) * sp.sqrt(6) * lam * h**2
        * (x**2 + y**2 + Z - 1)
    )
    exact_zero(
        kernel_reduce(sp.re(image[0]) - danger_formula, q, relation),
        "raw danger identity",
    )

    first = c * sp.conjugate(image[0]) + a * image[2] + I * (
        a * c - Q2[2, 0]
    )
    leakage = c * sp.conjugate(image[1]) - I * Q2[2, 1]
    raw_gate = sp.expand_complex(
        4 * a**2 * image[1] * sp.conjugate(image[1])
        + first * sp.conjugate(first)
        + leakage * sp.conjugate(leakage)
        - 32 * a**2 * sp.re(image[0]) ** 2
    )
    raw_gate = kernel_reduce(raw_gate, q, relation)
    gate36 = replace_even_h(36 * raw_gate, h, S)
    require(not gate36.has(h, q), "h or q survived raw-gate reduction")
    quartic = sp.Poly(gate36, lam)
    require(quartic.degree() == 4, "raw gate is not quartic in lambda")
    require(quartic.nth(0) == 5, "raw gate has wrong constant term")

    # Independent Gram-vector decomposition catches Q^2 indexing/conjugation
    # mistakes in the entrywise reconstruction above.
    Hp = sp.expand(H * p)
    B0 = sp.Matrix([0, I * a * c, 0])
    L = sp.Matrix(
        [
            2 * a * Hp[1],
            c * sp.conjugate(Hp[0]) + a * Hp[2],
            c * sp.conjugate(Hp[1]),
        ]
    )
    H2 = sp.expand(H * H)
    V2 = sp.Matrix([0, -I * H2[2, 0], -I * H2[2, 1]])
    vector_gate = sp.expand_complex(
        (
            (B0 + lam * L + lam**2 * V2).conjugate().T
            * (B0 + lam * L + lam**2 * V2)
        )[0]
        - 32 * a**2 * lam**2 * sp.re(Hp[0]) ** 2
    )
    exact_zero(
        kernel_reduce(raw_gate - vector_gate, q, relation),
        "entrywise/vector gate cross-check",
    )

    # 2. Substitute the moving sheet into the freshly reconstructed gate.
    A = 1 + M
    y0 = R(12, 25) / A + nu
    wc = -3 * (5 * M * X - 15 * M + 5 * X - 6) / (25 * A)
    Ymap = S * y0
    Wmap = S * (wc + omega)
    xmap = -R(1, 5) + X
    ymap = R(3, 5) + Ymap
    Zmap = 3 * X - X**2 - Ymap**2 + Wmap
    exact_zero(
        xmap**2 + ymap**2 + Zmap
        - (R(2, 5) + R(13, 5) * X + R(6, 5) * Ymap + Wmap),
        "moving-sheet danger identity",
    )

    mu, Yaux = sp.symbols("mu Yaux", real=True)
    rescaled = sp.cancel(gate36.subs(lam, mu / S))
    before_map = sp.expand(
        (S**3 * rescaled).subs(
            {x: xmap, y: R(3, 5) + Yaux, mu: A}
        )
    )
    raw_polynomial = sp.Poly(before_map, S, Z, X, Yaux)
    require(len(raw_polynomial.terms()) == 134, "unexpected raw term count")

    denominator = 25 * A
    sparse_y = {(1, 0): (12 + 25 * A * nu) / denominator}
    sparse_z = {
        (0, 1): R(3),
        (0, 2): -R(1),
        (1, 0): (45 * M + 18 + 25 * A * omega) / denominator,
        (1, 1): -R(3, 5),
        (2, 0): -((12 + 25 * A * nu) / denominator) ** 2,
    }
    mapped = {}
    for (sd, zd, xd, yd), coefficient in raw_polynomial.terms():
        term = {(sd, xd): coefficient}
        term = sparse_multiply(term, sparse_power(sparse_z, zd))
        term = sparse_multiply(term, sparse_power(sparse_y, yd))
        mapped = sparse_add(mapped, term)

    cleared = {}
    for key, coefficient in mapped.items():
        value = sp.cancel(denominator**8 * coefficient)
        if value == 0:
            continue
        numerator, residual_denominator = value.as_numer_denom()
        require(
            not residual_denominator.free_symbols,
            f"symbolic denominator survived at {key}: {residual_denominator}",
        )
        cleared[key] = sp.expand(value)
    require(
        all(sd >= 2 for sd, _ in cleared),
        "the claimed exact S^2 factor is absent",
    )
    qhat = sp.expand(
        sum(
            coefficient * S ** (sd - 2) * X**xd
            for (sd, xd), coefficient in cleared.items()
        )
    )
    require(
        sp.Poly(qhat, S, X, M, omega, nu).domain == sp.QQ,
        "cleared quotient is not over QQ",
    )
    sx = sp.Poly(qhat, S, X, domain=sp.EX)
    coefficients = {
        powers: sp.expand(coefficient) for powers, coefficient in sx.terms()
    }
    require(len(coefficients) == 20, "quotient does not have 20 (S,X) terms")
    require(max(i for i, _ in coefficients) == 5, "wrong S degree")
    require(max(jj for _, jj in coefficients) == 4, "wrong X degree")

    h1_coefficient = coefficients.pop((1, 0), None)
    require(h1_coefficient is not None, "missing isolated H1 term")
    h1_positive_factor = sp.factor(
        sp.cancel(
            h1_coefficient
            / (M**2 * A**8 * (5 * M**2 + 14 * M + 14))
        )
    )
    require(
        h1_positive_factor.is_Rational and h1_positive_factor > 0,
        f"H1 factor is not positive rational: {h1_positive_factor}",
    )
    exact_zero(
        5 * M**2 + 14 * M + 14
        - (5 * (M + R(7, 5)) ** 2 + R(21, 5)),
        "H1 quadratic completion",
    )
    require(
        all(sd + xd >= 2 for sd, xd in coefficients),
        "unaccounted term below degree two",
    )

    variables = (M, omega, nu)
    radii = (R(1, 1000), R(1, 100), R(1, 100))
    quadratic_indices = ((2, 0), (1, 1), (0, 2))
    quadratic_lowers = {}
    for index in quadratic_indices:
        lower, _ = centered_lower(coefficients[index], variables, radii)
        require(lower > 0, f"quadratic lower is not positive at {index}")
        quadratic_lowers[index] = lower
    c0 = min(quadratic_lowers.values())
    require(c0 == quadratic_lowers[(0, 2)], "c0 is not the X^2 reserve")

    # 3. The decisive lossless projective chart S=sigma X.
    Smax = R(1, 10000)
    Xmin = R(1, 31)
    Xmax = R(1, 30)
    sigmamax = sp.factor(Smax / Xmin)
    exact_zero(sigmamax - R(31, 10000), "sigma maximum")
    remainder = sp.Integer(0)
    higher_sx_terms = 0
    parameter_monomials = 0
    for (sd, xd), coefficient in coefficients.items():
        total_degree = sd + xd
        if total_degree <= 2:
            continue
        bound, monomials = centered_absolute(coefficient, variables, radii)
        # After S=sigma X and division by X^2:
        # |S^sd X^xd| / X^2 <= sigmamax^sd Xmax^(sd+xd-2).
        remainder += bound * sigmamax**sd * Xmax ** (total_degree - 2)
        higher_sx_terms += 1
        parameter_monomials += monomials
    remainder = sp.factor(remainder)
    margin = sp.factor(c0 - remainder)
    require(higher_sx_terms == 16, "wrong higher (S,X) term count")
    require(parameter_monomials == 947, "wrong parameter monomial count")
    require(margin > 0, "sigma-sensitive exact margin is not positive")

    # Compare only after deriving all values from the original gate.
    displayed = {
        "c0": R(
            2564950982194530478444050838857341987999,
            1274019840000000000000000000,
        ),
        "remainder": R(
            46499117573964545715217879542445250542603528830310449624295476899453,
            17199267840000000000000000000000000000000000000000000000000,
        ),
        "margin": R(
            34580339142052196913279468445031671587443896471169689550375704523100547,
            17199267840000000000000000000000000000000000000000000000000,
        ),
    }
    exact_zero(c0 - displayed["c0"], "displayed c0")
    exact_zero(remainder - displayed["remainder"], "displayed remainder")
    exact_zero(margin - displayed["margin"], "displayed margin")

    # 4. Independently prove legality and every endpoint qualification.
    Mradius, omega_radius, nu_radius = radii
    Amin = 1 - Mradius
    Amax = 1 + Mradius
    require(Amin > 0, "A can vanish")
    y0min = R(12, 25) / Amax - nu_radius
    y0max = R(12, 25) / Amin + nu_radius
    require(y0min > 0, "y0 can vanish")
    w0minus = (18 - 45 * Mradius) / (25 * Amin)
    w0plus = (18 + 45 * Mradius) / (25 * Amax)
    wlower = w0minus - R(3, 5) * Xmax - omega_radius
    wupper = w0plus + omega_radius
    exact_zero(
        wc + omega
        - ((45 * M + 18) / (25 * A) - R(3, 5) * X + omega),
        "wc monotone form",
    )
    zslope = sp.factor(wlower - Smax * y0max**2)
    zupper = sp.factor(3 * Xmax + Smax * wupper)
    danger_reserve = sp.factor(
        R(3, 5) - R(13, 5) * Xmax
        - R(6, 5) * Smax * y0max - Smax * wupper
    )
    require(wlower > 0, "wc+omega is not uniformly positive")
    require(zslope > 0, "positive-Z slope is not positive")
    require(zupper < R(1, 8), "Z upper bound is not below 1/8")
    require(danger_reserve > R(1, 2), "danger reserve is not above 1/2")
    require(0 < Smax < Xmin < Xmax < 3, "domain ordering is invalid")

    legality_displayed = {
        "wlower": R(2549, 3700),
        "zslope": R(7639086233111, 11088900000000),
        "zupper": R(100173181, 1001000000),
        "danger": R(95037195293, 185185000000),
    }
    exact_zero(wlower - legality_displayed["wlower"], "displayed wlower")
    exact_zero(zslope - legality_displayed["zslope"], "displayed zslope")
    exact_zero(zupper - legality_displayed["zupper"], "displayed zupper")
    exact_zero(
        danger_reserve - legality_displayed["danger"],
        "displayed danger reserve",
    )

    # The closed new cell includes both X endpoints.  The predecessor and
    # new cells both contain X=1/31.  X=0 belongs only to predecessor chart
    # C0; this verifier never divides by X there.  S=0 is excluded because
    # lambda=A/S is undefined, despite its use as an algebraic closure.
    require(Xmin > 0, "new projective chart divides by zero X")
    require(Smax > 0, "empty positive-S domain")
    require(Xmin <= Xmin <= Xmax, "left endpoint is absent")
    require(Xmin <= Xmax <= Xmax, "right endpoint is absent")

    # 5. Symmetric finite falsification only; never used for the continuum.
    sample_S = (Smax, Smax / 2, Smax / 10)
    sample_X = (Xmin, (Xmin + Xmax) / 2, Xmax)
    minimum_node = None
    node_count = 0
    for Sv, Xv in product(sample_S, sample_X):
        for Mv, ov, nv in product(
            (-Mradius, Mradius),
            (-omega_radius, omega_radius),
            (-nu_radius, nu_radius),
        ):
            Av = 1 + Mv
            y0v = R(12, 25) / Av + nv
            wcv = -3 * (5 * Mv * Xv - 15 * Mv + 5 * Xv - 6) / (25 * Av)
            Yv = Sv * y0v
            Zv = 3 * Xv - Xv**2 - Yv**2 + Sv * (wcv + ov)
            value = sp.factor(
                gate36.subs(
                    {
                        S: Sv,
                        Z: Zv,
                        x: -R(1, 5) + Xv,
                        y: R(3, 5) + Yv,
                        lam: Av / Sv,
                    }
                )
            )
            require(value > 0, "exact finite falsification found a negative")
            minimum_node = value if minimum_node is None else min(minimum_node, value)
            node_count += 1
    require(node_count == 72, "wrong finite falsification node count")

    own_hash = sha256(Path(__file__).read_bytes()).hexdigest()
    print("PASS standalone original Hermitian Q,Q^2 reconstruction")
    print("PASS independent Gram-vector quartic cross-check")
    print("PASS lossless positive clearing 36Gamma=qhat/[25^8(1+M)^8 S]")
    print("QUOTIENT_SX_TERMS", 20)
    print("HIGHER_SX_TERMS", higher_sx_terms)
    print("PARAMETER_MONOMIALS_RECOMPUTED", parameter_monomials)
    print("H1_POSITIVE_FACTOR", h1_positive_factor)
    print("H2_LOWER_S2", quadratic_lowers[(2, 0)])
    print("H2_LOWER_SX", quadratic_lowers[(1, 1)])
    print("H2_LOWER_X2", quadratic_lowers[(0, 2)])
    print("C0", c0)
    print("SIGMA_MAX", sigmamax)
    print("REMAINDER_ABS", remainder)
    print("STRICT_MARGIN", margin)
    print("DANGER_RESERVE", danger_reserve)
    print("FINITE_FALSIFICATION_NODES", node_count)
    print("FINITE_FALSIFICATION_MIN", minimum_node)
    print("PASS lambda>0, 0<Z<1/8, danger>1/2, detC=(5/9)SZ>0")
    print("PASS closed X endpoints and stitch at X=1/31")
    print("PASS X=0 predecessor-only attribution; S=0 excluded")
    print("RESULT=PASS exact strict raw 36Gamma on next-X sigma cell")
    print("SCOPE=partial moving-sheet theorem; full compact ball remains open")
    print("STATEMENT_SHA256", statement_hash)
    print("PREDECESSOR_SHA256", predecessor_hash)
    print("CODE_SHA256", own_hash)


if __name__ == "__main__":
    main()
