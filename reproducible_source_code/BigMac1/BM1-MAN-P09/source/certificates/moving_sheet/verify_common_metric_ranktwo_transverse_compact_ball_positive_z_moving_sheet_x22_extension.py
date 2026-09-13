#!/usr/bin/env python3
"""Fail-closed exact verifier for the moving-sheet extension through X=1/22.

No predecessor verifier, discovery program, cached quartic, or serialized
coefficient table is imported.  The fully conjugated Hermitian Q,Q^2 gate,
an independent Gram-vector gate, the sparse quotient, all 947 centered
parameter monomials, legality, endpoints, and exact falsification nodes are
reconstructed from definitions.
"""

if not __debug__:
    raise RuntimeError("fail closed: optimized Python disables verification")

import argparse
import hashlib
import os
from itertools import product
from pathlib import Path

import sympy as sp


EXPECTED_STATEMENT_SHA256 = (
    "5189571fc3913b3ff41dde268d2ce47cd89b18568748d76378007a1e0667d06d"
)
EXPECTED_PREDECESSOR_SHA256 = (
    "c6d3ee1900d6274e7651d28ab8cdf89fdffe999c1f8a544bf22d4b368e5c7395"
)


def require(condition, label):
    if not condition:
        raise RuntimeError(f"verification failed: {label}")


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def arguments():
    root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(
        description="Exact definition-level verifier for the x22 moving-sheet cell"
    )
    parser.add_argument(
        "--statement",
        type=Path,
        default=root / (
            "tmp/research/common_metric_ranktwo_transverse_compact_ball_"
            "positive_z_moving_sheet_x22_extension.md"
        ),
    )
    parser.add_argument(
        "--predecessor",
        type=Path,
        default=root / (
            "tmp/research/common_metric_ranktwo_transverse_compact_ball_"
            "positive_z_moving_sheet_cross_z_cap_stitch.md"
        ),
    )
    return parser.parse_args()


def bind(path, expected, label):
    require(path.is_file(), f"missing {label}: {path}")
    actual = sha256(path)
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
    result = sp.Integer(0)
    for (degree,), coefficient in sp.Poly(sp.expand(expression), h).terms():
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
    statement_expected = EXPECTED_STATEMENT_SHA256
    if os.environ.get("X22_TEST_BAD_STATEMENT") == "1":
        statement_expected = "0" * 64
    statement_hash = bind(args.statement, statement_expected, "statement")
    predecessor_hash = bind(
        args.predecessor, EXPECTED_PREDECESSOR_SHA256, "predecessor"
    )

    R = sp.Rational
    I = sp.I
    h, q, lam = sp.symbols("h q lambda", real=True)
    S, Z, x, y = sp.symbols("S Z x y", real=True)
    X, M, omega, nu = sp.symbols("X M omega nu", real=True)

    # 1. Fully conjugated original Hermitian Q,Q^2 gate.
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
        "transverse frame Gram",
    )
    exact_zero(
        kernel_reduce(U.conjugate().T * nvec, q, relation),
        "frame/kernel orthogonality",
    )
    exact_zero(
        kernel_reduce((nvec.conjugate().T * nvec)[0] - 1, q, relation),
        "kernel normalization",
    )

    j = (1 + 5 * x) / (3 * sp.sqrt(5))
    kappa = (-3 + 5 * y) / (3 * sp.sqrt(5))
    C = sp.Matrix([
        [h**2, h * (j + I * kappa)],
        [h * (j - I * kappa), j**2 + kappa**2 + R(5, 9) * Z],
    ])
    exact_zero(C - C.conjugate().T, "compression Hermitian")
    exact_zero(C.det() - R(5, 9) * h**2 * Z, "compression determinant")
    H = sp.expand(U * C * U.conjugate().T)
    exact_zero(kernel_reduce(H * nvec, q, relation), "H kernel")
    Q = sp.expand(lam * H)
    exact_zero(Q - Q.conjugate().T, "Q Hermitian")
    image = sp.expand(Q * p)
    Q2 = sp.expand(Q * Q)
    danger_formula = (
        R(5, 36) * sp.sqrt(6) * lam * h**2
        * (x**2 + y**2 + Z - 1)
    )
    exact_zero(
        kernel_reduce(sp.re(image[0]) - danger_formula, q, relation),
        "danger identity",
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
    require(quartic.degree() == 4, "gate is not quartic in lambda")
    require(quartic.nth(0) == 5, "gate quartic constant is not five")

    # Independent Gram-vector expression catches Q^2 index/conjugation errors.
    Hp = sp.expand(H * p)
    B0 = sp.Matrix([0, I * a * c, 0])
    L = sp.Matrix([
        2 * a * Hp[1],
        c * sp.conjugate(Hp[0]) + a * Hp[2],
        c * sp.conjugate(Hp[1]),
    ])
    H2 = sp.expand(H * H)
    V2 = sp.Matrix([0, -I * H2[2, 0], -I * H2[2, 1]])
    vector_gate = sp.expand_complex(
        ((B0 + lam * L + lam**2 * V2).conjugate().T
         * (B0 + lam * L + lam**2 * V2))[0]
        - 32 * a**2 * lam**2 * sp.re(Hp[0]) ** 2
    )
    exact_zero(
        kernel_reduce(raw_gate - vector_gate, q, relation),
        "entrywise/Gram-vector gate",
    )
    print("PASS fully conjugated Hermitian Q,Q^2 gate and Gram-vector cross-check")

    # 2. Moving map and fresh sparse quotient.
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
        "moving danger identity",
    )

    mu, Yaux = sp.symbols("mu Yaux", real=True)
    rescaled = sp.cancel(gate36.subs(lam, mu / S))
    before_map = sp.expand((S**3 * rescaled).subs({
        x: -R(1, 5) + X,
        y: R(3, 5) + Yaux,
        mu: A,
    }))
    raw_polynomial = sp.Poly(before_map, S, Z, X, Yaux)
    require(len(raw_polynomial.terms()) == 134, "wrong pre-map support")

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
        _, residual_denominator = value.as_numer_denom()
        require(
            not residual_denominator.free_symbols,
            f"symbolic denominator survived at {key}",
        )
        cleared[key] = sp.expand(value)
    require(all(sd >= 2 for sd, _ in cleared), "exact S^2 factor missing")
    qhat = sp.expand(sum(
        coefficient * S ** (sd - 2) * X**xd
        for (sd, xd), coefficient in cleared.items()
    ))
    require(
        sp.Poly(qhat, S, X, M, omega, nu).domain == sp.QQ,
        "cleared quotient is not rational",
    )
    sx = sp.Poly(qhat, S, X, domain=sp.EX)
    coefficients = {
        powers: sp.expand(coefficient) for powers, coefficient in sx.terms()
    }
    require(len(coefficients) == 20, "quotient support is not 20")
    require(max(i for i, _ in coefficients) == 5, "wrong S degree")
    require(max(jj for _, jj in coefficients) == 4, "wrong X degree")
    h1 = coefficients.pop((1, 0), None)
    require(h1 is not None, "missing H1")
    h1_factor = sp.factor(sp.cancel(
        h1 / (M**2 * A**8 * (5 * M**2 + 14 * M + 14))
    ))
    require(h1_factor == R(152587890625), "wrong H1 factor")
    exact_zero(
        5 * M**2 + 14 * M + 14
        - (5 * (M + R(7, 5)) ** 2 + R(21, 5)),
        "H1 positive completion",
    )
    require(all(sd + xd >= 2 for sd, xd in coefficients), "lost low layer")

    variables = (M, omega, nu)
    radii = (R(1, 1000), R(1, 100), R(1, 100))
    quadratic = {}
    for index in ((2, 0), (1, 1), (0, 2)):
        lower, _ = centered_lower(coefficients[index], variables, radii)
        require(lower > 0, f"nonpositive H2 lower at {index}")
        quadratic[index] = lower
    quadratic_claims = {
        (2, 0): R(
            481040550200263282578648409035494777132062079,
            114661785600000000000000000000000,
        ),
        (1, 1): R(
            2301835302565365212028445402384697058519239,
            191102976000000000000000000000,
        ),
        (0, 2): R(
            2564950982194530478444050838857341987999,
            1274019840000000000000000000,
        ),
    }
    require(quadratic == quadratic_claims, "H2 exact bounds changed")

    # 3. Lossless S=sigma X chart on the whole x22 cell.
    Smax, Xmin, Xmax = R(1, 10000), R(1, 23), R(1, 22)
    sigmamax = sp.factor(Smax / Xmin)
    require(sigmamax == R(23, 10000), "wrong sigma maximum")
    if os.environ.get("X22_TEST_DROP_HIGHER") == "1":
        drop = next(index for index in coefficients if sum(index) > 2)
        coefficients.pop(drop)
    remainder = sp.Integer(0)
    higher_terms = parameter_monomials = 0
    for (sd, xd), coefficient in coefficients.items():
        if sd + xd <= 2:
            continue
        bound, terms = centered_absolute(coefficient, variables, radii)
        remainder += bound * sigmamax**sd * Xmax ** (sd + xd - 2)
        higher_terms += 1
        parameter_monomials += terms
    remainder = sp.factor(remainder)
    c0 = quadratic[(0, 2)]
    margin = sp.factor(c0 - remainder)
    require(higher_terms == 16, "higher term count is not 16")
    require(parameter_monomials == 947, "parameter monomial count is not 947")
    remainder_claim = R(
        45501595887352000690514390785303819932610237699051256372767272123253,
        16648891269120000000000000000000000000000000000000000000000,
    )
    margin_claim = R(
        33473277839430772291616341971402441279238321762300948743627232727876747,
        16648891269120000000000000000000000000000000000000000000000,
    )
    require(remainder == remainder_claim, "exact remainder mismatch")
    require(margin == margin_claim and margin > 0, "strict margin failed")
    print("PASS 20-term quotient, 16 higher terms, 947 monomials, strict margin")

    # 4. Legality, proved independently from the gate envelope.
    Mrad, wrad, nrad = radii
    Amin, Amax = 1 - Mrad, 1 + Mrad
    y0min = R(12, 25) / Amax - nrad
    y0max = R(12, 25) / Amin + nrad
    w0min = (18 - 45 * Mrad) / (25 * Amin) - wrad
    w0max = (18 + 45 * Mrad) / (25 * Amax) + wrad
    wlower = sp.factor(w0min - R(3, 5) * Xmax)
    zslope = sp.factor(wlower - Smax * y0max**2)
    zbase = sp.factor(3 * Xmin - Xmin**2)
    zupper = sp.factor(3 * Xmax - Xmax**2 + Smax * w0max)
    danger = sp.factor(
        R(3, 5) - R(13, 5) * Xmax
        - R(6, 5) * Smax * y0max - Smax * w0max
    )
    legality_claims = {
        "Amin": (Amin, R(999, 1000)),
        "y0min": (y0min, R(46999, 100100)),
        "wlower": (wlower, R(27743, 40700)),
        "zslope": (zslope, R(83142836564221, 121977900000000)),
        "zbase": (zbase, R(68, 529)),
        "zupper": (zupper, R(1479554991, 11011000000)),
        "danger": (danger, R(267603185879, 555555000000)),
    }
    for label, (value, claim) in legality_claims.items():
        exact_zero(value - claim, label)
    require(0 < Smax < Xmin < Xmax < 3, "invalid cell ordering")
    require(Amin > 0 and y0min > 0, "scale/y0 legality failed")
    require(zslope > 0 and zbase > R(1, 8), "strict positive-Z lower failed")
    require(zupper < R(1, 7), "Z upper is not below 1/7")
    require(danger > 0, "strict danger reserve failed")
    require(not qhat.has(sp.Symbol("T")), "cap coordinate entered quotient")
    print("PASS lambda>0, 68/529<Z<1/7, strict danger, det=(5/9)SZ>0")
    print("PASS no division by a cap coordinate")

    # 5. Endpoint witnesses and exact rational falsification route.
    sample_S = (R(1, 1000000), R(1, 20000), Smax)
    sample_X = (Xmin, sp.factor((Xmin + Xmax) / 2), Xmax)
    records = []
    for Sv, Xv, Mv, ov, nv in product(
        sample_S, sample_X, (-Mrad, Mrad), (-wrad, wrad), (-nrad, nrad)
    ):
        Av = 1 + Mv
        y0v = R(12, 25) / Av + nv
        wcv = -3 * (5 * Mv * Xv - 15 * Mv + 5 * Xv - 6) / (25 * Av)
        Yv = Sv * y0v
        Zv = sp.factor(3 * Xv - Xv**2 - Yv**2 + Sv * (wcv + ov))
        xrv = -R(1, 5) + Xv
        yrv = R(3, 5) + Yv
        lv = Av / Sv
        dv = sp.factor(1 - xrv**2 - yrv**2 - Zv)
        detv = sp.factor(R(5, 9) * Sv * Zv)
        value = sp.factor(gate36.subs({
            S: Sv, Z: Zv, x: xrv, y: yrv, lam: lv,
        }))
        require(lv > 0 and Zv > 0 and dv > 0 and detv > 0, "illegal node")
        require(value > 0, "exact rational node has negative gate")
        records.append(((Sv, Xv, Mv, ov, nv), value, Zv, dv, detv))
    require(len(records) == 72, "falsification node count is not 72")
    minimum = min(records, key=lambda item: item[1])
    minimum_claim = R(
        2851967535986553322459201051507517913149039,
        11193640000000000000000000000000000000000,
    )
    require(
        minimum[0] == (Smax, Xmin, -Mrad, -wrad, -nrad),
        "sample minimum moved",
    )
    require(minimum[1] == minimum_claim, "sample minimum value mismatch")
    left = next(item for item in records if item[0] == minimum[0])
    right_arg = (Smax, Xmax, -Mrad, -wrad, -nrad)
    right = next(item for item in records if item[0] == right_arg)
    right_claim = R(
        14817150110247071841775080222180418970749,
        53240000000000000000000000000000000000,
    )
    require(right[1] == right_claim, "right endpoint witness mismatch")
    require(Xmin == R(1, 23), "predecessor stitch endpoint mismatch")
    print("PASS both closed endpoints and exact stitch at X=1/23")
    print("PASS 72 exact legal falsification nodes; no negative gate")

    print("SIGMA_MAX", sigmamax)
    print("QUOTIENT_SX_TERMS", 20)
    print("HIGHER_SX_TERMS", higher_terms)
    print("PARAMETER_MONOMIALS_RECOMPUTED", parameter_monomials)
    print("REMAINDER_ABS", remainder)
    print("STRICT_MARGIN", margin)
    print("Z_UPPER", zupper)
    print("DANGER_RESERVE", danger)
    print("LEFT_ENDPOINT_RAW_36GAMMA", left[1])
    print("RIGHT_ENDPOINT_RAW_36GAMMA", right[1])
    print("FALSIFICATION_MIN", minimum[1])
    print("STATEMENT_SHA256", statement_hash)
    print("PREDECESSOR_SHA256", predecessor_hash)
    print("VERIFIER_SHA256", sha256(Path(__file__).resolve()))
    print("RESULT exact strict raw 36Gamma for 1/23<=X<=1/22")
    print("SCOPE moving-sheet partial theorem; compact ball/common metric/fixed lens open")


if __name__ == "__main__":
    main()
