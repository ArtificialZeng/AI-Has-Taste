#!/usr/bin/env python3
"""Independent exact referee for the continuous moving-sheet Z-cap stitch.

No source verifier, discovery program, cached polynomial, or certificate
constant is imported.  The original fully conjugated Hermitian Q,Q^2 gate
and the complete continuum envelope are rebuilt from definitions.
"""

if not __debug__:
    raise RuntimeError("refuse optimized execution: assertions must remain enabled")

import argparse
import hashlib
from pathlib import Path

import sympy as sp


def exact_zero(value, label):
    if isinstance(value, sp.MatrixBase):
        for row in range(value.rows):
            for column in range(value.cols):
                exact_zero(value[row, column], f"{label}[{row},{column}]")
        return
    reduced = sp.factor(sp.cancel(sp.together(sp.expand_complex(value))))
    if reduced != 0:
        raise AssertionError(f"{label}: {reduced}")


def reduce_q(value, q, relation):
    if isinstance(value, sp.MatrixBase):
        return value.applyfunc(lambda item: reduce_q(item, q, relation))
    numerator, denominator = sp.cancel(sp.together(value)).as_numer_denom()
    remainder = sp.Poly(sp.expand(numerator), q).rem(relation).as_expr()
    return sp.cancel(remainder / denominator)


def sparse_product(left, right):
    result = {}
    for (si, xi), left_value in left.items():
        for (sj, xj), right_value in right.items():
            key = (si + sj, xi + xj)
            result[key] = result.get(key, 0) + left_value * right_value
    return {key: sp.expand(value) for key, value in result.items() if value != 0}


def sparse_power(base, exponent):
    result = {(0, 0): sp.Integer(1)}
    for _ in range(exponent):
        result = sparse_product(result, base)
    return result


def sparse_accumulate(target, source):
    for key, value in source.items():
        target[key] = target.get(key, 0) + value


def centered_absolute_bound(polynomial, variables, radii):
    expanded = sp.Poly(sp.expand(polynomial), *variables, domain=sp.QQ)
    total = sp.Integer(0)
    for powers, coefficient in expanded.terms():
        total += abs(coefficient) * sp.prod(
            radius**power for radius, power in zip(radii, powers)
        )
    return sp.factor(total), len(expanded.terms())


def centered_lower_bound(polynomial, variables, radii):
    expanded = sp.Poly(sp.expand(polynomial), *variables, domain=sp.QQ)
    origin = expanded.coeff_monomial((0,) * len(variables))
    variation = sp.Integer(0)
    for powers, coefficient in expanded.terms():
        if any(powers):
            variation += abs(coefficient) * sp.prod(
                radius**power for radius, power in zip(radii, powers)
            )
    return sp.factor(origin - variation)


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def main():
    R = sp.Rational
    I = sp.I
    h, q, lam = sp.symbols("h q lambda", real=True)
    S, Z, x, y = sp.symbols("S Z x y", real=True)
    X, Y, M, omega, nu, T = sp.symbols("X Y M omega nu T", real=True)

    # Definition-level reconstruction of the original Hermitian data.
    a = 1 / sp.sqrt(6)
    c = sp.sqrt(R(5, 6))
    zeta = R(4, 5) + I * R(3, 5)
    p = sp.Matrix([a, 0, c])
    rvec = sp.Matrix([-a, 0, c * zeta])
    fvec = sp.Matrix([-c * h, q, -a * h * zeta])
    nvec = sp.Matrix([c * q, h, a * q * zeta])
    frame = sp.Matrix.hstack(rvec, fvec)
    relation = sp.Poly(q**2 + h**2 - 1, q)
    exact_zero(
        reduce_q(frame.conjugate().T * frame - sp.eye(2), q, relation),
        "transverse frame Gram",
    )
    exact_zero(
        reduce_q(frame.conjugate().T * nvec, q, relation),
        "frame/kernel orthogonality",
    )
    exact_zero(
        reduce_q((nvec.conjugate().T * nvec)[0] - 1, q, relation),
        "kernel norm",
    )

    j = (1 + 5 * x) / (3 * sp.sqrt(5))
    kappa = (-3 + 5 * y) / (3 * sp.sqrt(5))
    v = j**2 + kappa**2 + R(5, 9) * Z
    compression = sp.Matrix(
        [[h**2, h * (j + I * kappa)], [h * (j - I * kappa), v]]
    )
    exact_zero(compression - compression.conjugate().T, "compression Hermitian")
    exact_zero(compression.det() - R(5, 9) * h**2 * Z, "compression determinant")
    H = sp.expand(frame * compression * frame.conjugate().T)
    exact_zero(reduce_q(H * nvec, q, relation), "H kernel")
    Q = sp.expand(lam * H)
    exact_zero(Q - Q.conjugate().T, "Q Hermitian")
    image = sp.expand(Q * p)
    exact_zero(
        reduce_q(
            sp.re(image[0])
            - R(5, 36) * sp.sqrt(6) * lam * h**2
            * (x**2 + y**2 + Z - 1),
            q,
            relation,
        ),
        "danger identity",
    )

    Q2 = sp.expand(Q * Q)
    first = c * sp.conjugate(image[0]) + a * image[2] + I * (a * c - Q2[2, 0])
    leakage = c * sp.conjugate(image[1]) - I * Q2[2, 1]
    raw_gate = sp.expand_complex(
        4 * a**2 * image[1] * sp.conjugate(image[1])
        + first * sp.conjugate(first)
        + leakage * sp.conjugate(leakage)
        - 32 * a**2 * sp.re(image[0]) ** 2
    )
    raw_gate = sp.expand(reduce_q(raw_gate, q, relation))

    # Map even h powers to S by coefficient extraction.
    gate36 = sp.Integer(0)
    for (power,), coefficient in sp.Poly(sp.expand(36 * raw_gate), h).terms():
        if power % 2:
            raise AssertionError(f"unexpected odd h power {power}")
        gate36 += coefficient * S ** (power // 2)
    gate36 = sp.expand(gate36)
    if gate36.has(h) or gate36.has(q):
        raise AssertionError("h/q remained after quotient")
    lambda_polynomial = sp.Poly(gate36, lam)
    if lambda_polynomial.degree() != 4 or lambda_polynomial.nth(0) != 5:
        raise AssertionError("raw gate is not the required quartic")

    # Recenter at the cap only to audit losslessness.  The expression remains
    # polynomial in T and the proof below never divides by T.
    recentered_gate = sp.cancel(gate36.subs(Z, T + R(1, 8)))
    numerator_t, denominator_t = sp.together(recentered_gate).as_numer_denom()
    if denominator_t.has(T) or denominator_t == 0:
        raise AssertionError("Z=1/8 recentering introduced a denominator")
    sp.Poly(sp.expand(numerator_t), T)
    print("PASS original fully conjugated Hermitian Q,Q^2 gate")
    print("PASS Z=1/8 recentering is polynomial; no division by T")

    # Moving-sheet map and exact outer-box gap.
    A = 1 + M
    y0 = R(12, 25) / A + nu
    wc = -3 * (5 * M * X - 15 * M + 5 * X - 6) / (25 * A)
    Ymap = S * y0
    Wmap = S * (wc + omega)
    Zmap = 3 * X - X**2 - Ymap**2 + Wmap
    xmap = -R(1, 5) + X
    ymap = R(3, 5) + Ymap
    exact_zero(
        xmap**2 + ymap**2 + Zmap
        - (R(2, 5) + R(13, 5) * X + R(6, 5) * Ymap + Wmap),
        "moving danger identity",
    )

    smax = R(1, 10000)
    xmin, xmax = R(1, 24), R(1, 23)
    mrad = R(1, 1000)
    wrad = nrad = R(1, 100)
    amin, amax = 1 - mrad, 1 + mrad
    y0min = R(12, 25) / amax - nrad
    y0max = R(12, 25) / amin + nrad
    w0min = (18 - 45 * mrad) / (25 * amin) - wrad
    w0max = (18 + 45 * mrad) / (25 * amax) + wrad
    x_lower = sp.factor(-R(1, 5) + xmin)
    x_upper = sp.factor(-R(1, 5) + xmax)
    y_gap_infimum = R(1, 10)
    y_gap_upper = sp.factor(R(1, 10) + smax * y0max)
    if not (
        x_lower == -R(19, 120)
        and x_upper == -R(18, 115)
        and -R(1, 4) < x_lower < x_upper < R(1, 2)
        and y0min > 0
        and y_gap_infimum > 0
    ):
        raise AssertionError("outer-box coordinate audit failed")
    # Every actual point has S>0 and hence y-1/2>1/10; 1/10 is only
    # the closure infimum as S tends to zero.
    print("OUTER_X_RANGE", x_lower, x_upper)
    print("OUTER_Y_GAP_INFIMUM_CLOSURE", y_gap_infimum)
    print("OUTER_Y_GAP_UPPER", y_gap_upper)
    print("PASS every actual moving-sheet point lies above y=1/2")

    # Full-band scale, Z, danger, and rank-two legality.
    wbar_min = sp.factor(w0min - R(3, 5) * xmax)
    z_slope = sp.factor(wbar_min - smax * y0max**2)
    z_upper = sp.factor(3 * xmax - xmax**2 + smax * w0max)
    danger_reserve = sp.factor(
        R(3, 5)
        - R(13, 5) * xmax
        - R(6, 5) * smax * y0max
        - smax * w0max
    )
    if not (
        0 < smax < xmin < xmax < 3
        and amin > 0
        and y0min > 0
        and wbar_min > 0
        and z_slope > 0
        and 0 < z_upper < R(1, 7)
        and danger_reserve > 0
    ):
        raise AssertionError("full cross-cap legality failed")
    exact_zero(
        compression.det().subs(h**2, S) - R(5, 9) * S * Z,
        "det C=(5/9)SZ",
    )
    print("WBAR_LOWER", wbar_min)
    print("Z_SLOPE_LOWER", z_slope)
    print("Z_UPPER", z_upper)
    print("DANGER_RESERVE", danger_reserve)
    print("PASS lambda>0, 0<Z<1/7, strict danger, det=(5/9)SZ>0, rank=2")

    # Independently construct the cleared moving-sheet quotient.
    N = sp.Integer(0)
    for power in range(5):
        N += lambda_polynomial.nth(power) * A**power * S ** (3 - power)
    N = sp.cancel(N)
    N = sp.expand(N.subs({x: xmap, y: R(3, 5) + Y}))
    raw_shape = sp.Poly(N, S, Z, X, Y)
    if len(raw_shape.terms()) != 134:
        raise AssertionError(f"unexpected precomposition support {len(raw_shape.terms())}")

    denominator = 25 * A
    y_numerator = 12 + 25 * A * nu
    w0_numerator = 18 + 45 * M + 25 * A * omega
    y_series = {(1, 0): y_numerator / denominator}
    z_series = {
        (0, 1): R(3),
        (0, 2): -R(1),
        (1, 0): w0_numerator / denominator,
        (1, 1): -R(3, 5),
        (2, 0): -(y_numerator / denominator) ** 2,
    }
    composed = {}
    for (spow, zpow, xpow, ypow), coefficient in raw_shape.terms():
        part = {(spow, xpow): coefficient}
        part = sparse_product(part, sparse_power(z_series, zpow))
        part = sparse_product(part, sparse_power(y_series, ypow))
        sparse_accumulate(composed, part)

    cleared = {}
    for key, value in composed.items():
        cleared_value = sp.factor(sp.cancel(value * denominator**8))
        if cleared_value == 0:
            continue
        if sp.denom(cleared_value).free_symbols:
            raise AssertionError(f"uncleared symbolic denominator at {key}")
        cleared[key] = cleared_value
    below_s2 = {key: value for key, value in cleared.items() if key[0] < 2}
    if below_s2:
        raise AssertionError(f"missing exact S^2 factor: {below_s2}")
    quotient = {(si - 2, xi): value for (si, xi), value in cleared.items()}
    if len(quotient) != 20:
        raise AssertionError(f"moving quotient has {len(quotient)} terms")
    if max(si for si, _ in quotient) != 5 or max(xi for _, xi in quotient) != 4:
        raise AssertionError("quotient bidegree mismatch")

    h1 = quotient[(1, 0)]
    exact_zero(
        h1 - R(152587890625) * M**2 * A**8 * (5 * M**2 + 14 * M + 14),
        "nonnegative first layer",
    )
    proof_terms = dict(quotient)
    del proof_terms[(1, 0)]
    if any(si + xi < 2 for si, xi in proof_terms):
        raise AssertionError("unaccounted term below quadratic degree")

    parameter_variables = (M, omega, nu)
    parameter_radii = (mrad, wrad, nrad)
    quadratic_keys = ((2, 0), (1, 1), (0, 2))
    quadratic_reserves = {
        key: centered_lower_bound(proof_terms[key], parameter_variables, parameter_radii)
        for key in quadratic_keys
    }
    if any(value <= 0 for value in quadratic_reserves.values()):
        raise AssertionError(f"quadratic reserve failed: {quadratic_reserves}")
    c0 = quadratic_reserves[(0, 2)]

    higher_bounds = {}
    parameter_monomials = 0
    for key, coefficient in proof_terms.items():
        if sum(key) <= 2:
            continue
        bound, count = centered_absolute_bound(
            coefficient, parameter_variables, parameter_radii
        )
        higher_bounds[key] = bound
        parameter_monomials += count
    if len(higher_bounds) != 16 or parameter_monomials != 947:
        raise AssertionError(
            f"support/count mismatch {len(higher_bounds)}, {parameter_monomials}"
        )

    sigma_max = sp.factor(smax / xmin)
    if sigma_max != R(3, 1250):
        raise AssertionError("sigma bound is not 3/1250")
    remainder = sp.factor(
        sum(
            bound * sigma_max**si * xmax ** (si + xi - 2)
            for (si, xi), bound in higher_bounds.items()
        )
    )
    margin = sp.factor(c0 - remainder)
    if margin <= 0:
        raise AssertionError("cross-cap continuum margin is not positive")
    print("PASS quotient_terms=20 higher_terms=16 parameter_monomials=947")
    print("SIGMA_MAX", sigma_max)
    print("C0", c0)
    print("CROSS_CAP_RABS", remainder)
    print("CROSS_CAP_STRICT_MARGIN", margin)
    print("PASS continuum gate envelope on every 1/24<=X<=1/23")

    # Exact witnesses on opposite sides of the cap, including raw gate.
    witness_specs = (
        ("below", xmin, -mrad, -wrad, nrad),
        ("above", xmax, mrad, wrad, -nrad),
    )
    signed_caps = {}
    for label, xvalue, mvalue, ovalue, nuvalue in witness_specs:
        avalue = 1 + mvalue
        y0value = R(12, 25) / avalue + nuvalue
        wcvalue = -3 * (
            5 * mvalue * xvalue - 15 * mvalue + 5 * xvalue - 6
        ) / (25 * avalue)
        zvalue = sp.factor(
            3 * xvalue - xvalue**2
            - (smax * y0value) ** 2
            + smax * (wcvalue + ovalue)
        )
        xraw = -R(1, 5) + xvalue
        yraw = R(3, 5) + smax * y0value
        lvalue = avalue / smax
        danger_value = sp.factor(1 - xraw**2 - yraw**2 - zvalue)
        determinant_value = sp.factor(R(5, 9) * smax * zvalue)
        gate_value = sp.factor(
            lambda_polynomial.as_expr().subs(
                {S: smax, Z: zvalue, x: xraw, y: yraw, lam: lvalue}
            )
        )
        signed_caps[label] = sp.factor(zvalue - R(1, 8))
        if not (
            lvalue > 0
            and zvalue > 0
            and danger_value > 0
            and determinant_value > 0
            and gate_value > 0
        ):
            raise AssertionError(f"illegal crossing witness {label}")
        print(f"WITNESS_{label.upper()}_Z", zvalue)
        print(f"WITNESS_{label.upper()}_T", signed_caps[label])
        print(f"WITNESS_{label.upper()}_DANGER", danger_value)
        print(f"WITNESS_{label.upper()}_DET", determinant_value)
        print(f"WITNESS_{label.upper()}_RAW_36GAMMA", gate_value)
    if not (signed_caps["below"] < 0 < signed_caps["above"]):
        raise AssertionError("the exact witnesses do not cross Z=1/8")

    # Falsification-only grid.  It is explicitly not used in the continuum
    # envelope proof above.
    s_nodes = (R(1, 10000), R(1, 20000), R(1, 100000))
    x_nodes = (xmin, (xmin + xmax) / 2, xmax)
    node_count = 0
    minimum = None
    minimum_data = None
    for snode in s_nodes:
        for xnode in x_nodes:
            for mnode in (-mrad, mrad):
                for onode in (-wrad, wrad):
                    for nunode in (-nrad, nrad):
                        anode = 1 + mnode
                        y0node = R(12, 25) / anode + nunode
                        wcnode = -3 * (
                            5 * mnode * xnode - 15 * mnode + 5 * xnode - 6
                        ) / (25 * anode)
                        znode = sp.factor(
                            3 * xnode - xnode**2
                            - (snode * y0node) ** 2
                            + snode * (wcnode + onode)
                        )
                        value = sp.factor(
                            lambda_polynomial.as_expr().subs(
                                {
                                    S: snode,
                                    Z: znode,
                                    x: -R(1, 5) + xnode,
                                    y: R(3, 5) + snode * y0node,
                                    lam: anode / snode,
                                }
                            )
                        )
                        node_count += 1
                        if value <= 0:
                            raise AssertionError(f"falsification node nonpositive: {value}")
                        if minimum is None or value < minimum:
                            minimum = value
                            minimum_data = (snode, xnode, mnode, onode, nunode)
    if node_count != 72:
        raise AssertionError(f"unexpected falsification count {node_count}")
    print("PASS adversarial exact raw-gate nodes", node_count)
    print("ADVERSARIAL_NODE_MIN", minimum)
    print("ADVERSARIAL_NODE_ARG", minimum_data)

    print("PASS opposite-sign cap witnesses lie inside one proved continuous band")
    print("INTERPRETATION genuine continuum cross-cap theorem, not point stitching")
    print("ATTRIBUTION S=0 is closure only; every original datum has S>0")
    script_path = Path(__file__).resolve()
    print("VERIFIER_SHA256", sha256(script_path))
    print("PASS independent continuous cross-Z-cap referee")
    print("SCOPE moving-sheet family only; full compact ball/common metric/fixed lens open")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Independent exact referee for the continuous cross-Z cap stitch"
    )
    parser.parse_args()
    main()
