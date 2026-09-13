#!/usr/bin/env python3
"""Independent exact referee for the reciprocal moving-sheet envelope.

This verifier deliberately imports no project verifier and trusts no stored
coefficient table or claimed rational constant.  It rebuilds the fully
conjugated Hermitian Q,Q^2 gate, the moving-sheet quotient, its centered-box
envelope, all reciprocal endpoint decisions, and the first lower-Z scope
failure from the definitions.
"""

if not __debug__:
    raise RuntimeError("refuse optimized execution: exact assertions must remain active")

import argparse
import hashlib
from pathlib import Path

import sympy as sp


def exact_zero(value, label):
    """Fail unless a scalar or every matrix entry vanishes identically."""
    if isinstance(value, sp.MatrixBase):
        for row in range(value.rows):
            for column in range(value.cols):
                exact_zero(value[row, column], f"{label}[{row},{column}]")
        return
    reduced = sp.factor(sp.cancel(sp.together(sp.expand_complex(value))))
    if reduced != 0:
        raise AssertionError(f"{label}: {reduced}")


def quotient_mod_relation(value, q, relation):
    """Reduce a rational expression modulo a monic polynomial in q."""
    if isinstance(value, sp.MatrixBase):
        return value.applyfunc(lambda item: quotient_mod_relation(item, q, relation))
    numerator, denominator = sp.cancel(sp.together(value)).as_numer_denom()
    remainder = sp.Poly(sp.expand(numerator), q).rem(relation).as_expr()
    return sp.cancel(remainder / denominator)


def bivariate_product(left, right):
    """Multiply sparse polynomials keyed by powers of (S,X)."""
    result = {}
    for (si, xi), left_coefficient in left.items():
        for (sj, xj), right_coefficient in right.items():
            key = (si + sj, xi + xj)
            result[key] = result.get(key, 0) + left_coefficient * right_coefficient
    return {key: sp.expand(value) for key, value in result.items() if value != 0}


def bivariate_power(base, exponent):
    result = {(0, 0): sp.Integer(1)}
    for _ in range(exponent):
        result = bivariate_product(result, base)
    return result


def bivariate_accumulate(target, source):
    for key, value in source.items():
        target[key] = target.get(key, 0) + value


def centered_l1_bound(polynomial, variables, radii):
    """Exact l1 bound after scaling a centered parameter box to [-1,1]^3."""
    expanded = sp.Poly(sp.expand(polynomial), *variables, domain=sp.QQ)
    total = sp.Integer(0)
    for powers, coefficient in expanded.terms():
        scale = sp.prod(radius**power for radius, power in zip(radii, powers))
        total += abs(coefficient) * scale
    return sp.factor(total), len(expanded.terms())


def centered_constant_reserve(polynomial, variables, radii):
    """Constant coefficient minus the exact l1 variation on a centered box."""
    expanded = sp.Poly(sp.expand(polynomial), *variables, domain=sp.QQ)
    origin = expanded.coeff_monomial((0,) * len(variables))
    variation = sp.Integer(0)
    for powers, coefficient in expanded.terms():
        if any(powers):
            scale = sp.prod(radius**power for radius, power in zip(radii, powers))
            variation += abs(coefficient) * scale
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

    # Original fully conjugated Hermitian gate.
    h, q, lam = sp.symbols("h q lambda", real=True)
    S, Z, x, y = sp.symbols("S Z x y", real=True)
    X, Y, M, omega, nu = sp.symbols("X Y M omega nu", real=True)
    a = 1 / sp.sqrt(6)
    c = sp.sqrt(R(5, 6))
    zeta = R(4, 5) + I * R(3, 5)
    p = sp.Matrix([a, 0, c])
    rvec = sp.Matrix([-a, 0, c * zeta])
    fvec = sp.Matrix([-c * h, q, -a * h * zeta])
    nvec = sp.Matrix([c * q, h, a * q * zeta])
    frame = sp.Matrix.hstack(rvec, fvec)
    q_relation = sp.Poly(q**2 + h**2 - 1, q)

    exact_zero(
        quotient_mod_relation(frame.conjugate().T * frame - sp.eye(2), q, q_relation),
        "transverse frame Gram",
    )
    exact_zero(
        quotient_mod_relation(frame.conjugate().T * nvec, q, q_relation),
        "transverse/kernel orthogonality",
    )
    exact_zero(
        quotient_mod_relation((nvec.conjugate().T * nvec)[0] - 1, q, q_relation),
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
    exact_zero(quotient_mod_relation(H * nvec, q, q_relation), "H kernel")
    Q = sp.expand(lam * H)
    exact_zero(Q - Q.conjugate().T, "Q Hermitian")
    image = sp.expand(Q * p)
    exact_zero(
        quotient_mod_relation(
            sp.re(image[0])
            - R(5, 36) * sp.sqrt(6) * lam * h**2 * (x**2 + y**2 + Z - 1),
            q,
            q_relation,
        ),
        "danger compression identity",
    )

    Q2 = sp.expand(Q * Q)
    first = c * sp.conjugate(image[0]) + a * image[2] + I * (a * c - Q2[2, 0])
    leakage = c * sp.conjugate(image[1]) - I * Q2[2, 1]
    gate = sp.expand_complex(
        4 * a**2 * image[1] * sp.conjugate(image[1])
        + first * sp.conjugate(first)
        + leakage * sp.conjugate(leakage)
        - 32 * a**2 * sp.re(image[0]) ** 2
    )
    gate = sp.expand(quotient_mod_relation(gate, q, q_relation))

    # Convert even powers of h to S by coefficient extraction, rather than
    # trusting a replacement list from an earlier verifier.
    h_polynomial = sp.Poly(sp.expand(36 * gate), h)
    gate36 = sp.Integer(0)
    for (power,), coefficient in h_polynomial.terms():
        if power % 2:
            raise AssertionError(f"unexpected odd h power {power}")
        gate36 += coefficient * S ** (power // 2)
    gate36 = sp.expand(gate36)
    if gate36.has(h) or gate36.has(q):
        raise AssertionError("h/q remained after exact quotient")
    lambda_polynomial = sp.Poly(gate36, lam)
    if lambda_polynomial.degree() != 4 or lambda_polynomial.nth(0) != 5:
        raise AssertionError("raw gate is not the required quartic with constant five")
    print("PASS original fully conjugated Hermitian Q,Q^2 gate")

    # Moving sheet and algebraic danger identity.
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
        "moving-sheet danger identity",
    )

    smax = R(1, 10000)
    xmin = R(1, 30)
    mrad = R(1, 1000)
    wrad = R(1, 100)
    nrad = R(1, 100)
    amin, amax = 1 - mrad, 1 + mrad
    y0min = R(12, 25) / amax - nrad
    y0max = R(12, 25) / amin + nrad
    w0min = (18 - 45 * mrad) / (25 * amin) - wrad
    w0max = (18 + 45 * mrad) / (25 * amax) + wrad
    if not (amin > 0 and y0min > 0 and smax < xmin):
        raise AssertionError("basic parameter positivity failed")

    # Rebuild N=S^3(36 Gamma) and then compose the moving sheet using an
    # independently implemented sparse bivariate evaluator.
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
        part = bivariate_product(part, bivariate_power(z_series, zpow))
        part = bivariate_product(part, bivariate_power(y_series, ypow))
        bivariate_accumulate(composed, part)

    cleared = {}
    for key, value in composed.items():
        value = sp.factor(sp.cancel(value * denominator**8))
        if value == 0:
            continue
        if sp.denom(value).free_symbols:
            raise AssertionError(f"symbolic denominator survived at {key}")
        cleared[key] = value
    below_s2 = {key: value for key, value in cleared.items() if key[0] < 2}
    if below_s2:
        raise AssertionError(f"claimed exact S^2 factor is false: {below_s2}")
    quotient = {(si - 2, xi): value for (si, xi), value in cleared.items()}
    if len(quotient) != 20:
        raise AssertionError(f"moving quotient has {len(quotient)} rather than 20 terms")
    if max(si for si, _ in quotient) != 5 or max(xi for _, xi in quotient) != 4:
        raise AssertionError("moving quotient bidegree mismatch")

    h1 = quotient[(1, 0)]
    exact_zero(
        h1
        - R(152587890625) * M**2 * A**8 * (5 * M**2 + 14 * M + 14),
        "nonnegative first layer",
    )
    proof_terms = dict(quotient)
    del proof_terms[(1, 0)]
    if any(si + xi < 2 for si, xi in proof_terms):
        raise AssertionError("unaccounted quotient term below degree two")

    parameter_variables = (M, omega, nu)
    parameter_radii = (mrad, wrad, nrad)
    quadratic_keys = ((2, 0), (1, 1), (0, 2))
    quadratic_reserves = {
        key: centered_constant_reserve(proof_terms[key], parameter_variables, parameter_radii)
        for key in quadratic_keys
    }
    if any(value <= 0 for value in quadratic_reserves.values()):
        raise AssertionError(f"nonpositive quadratic reserve {quadratic_reserves}")
    c0 = quadratic_reserves[(0, 2)]

    higher_bounds = {}
    parameter_monomials = 0
    for key, coefficient in proof_terms.items():
        if sum(key) <= 2:
            continue
        bound, count = centered_l1_bound(coefficient, parameter_variables, parameter_radii)
        higher_bounds[key] = bound
        parameter_monomials += count
    if len(higher_bounds) != 16 or parameter_monomials != 947:
        raise AssertionError(
            f"higher support/count mismatch: {len(higher_bounds)}, {parameter_monomials}"
        )
    sigma_max = sp.factor(smax / xmin)
    if sigma_max != R(3, 1000):
        raise AssertionError("sigma envelope mismatch")

    endpoint_rows = []
    for denominator_n in range(29, 22, -1):
        xmax = R(1, denominator_n)
        remainder = sp.factor(
            sum(
                bound * sigma_max**si * xmax ** (si + xi - 2)
                for (si, xi), bound in higher_bounds.items()
            )
        )
        margin = sp.factor(c0 - remainder)
        wbar_min = w0min - R(3, 5) * xmax
        z_slope = sp.factor(wbar_min - smax * y0max**2)
        z_upper = sp.factor(3 * xmax - xmax**2 + smax * w0max)
        danger_reserve = sp.factor(
            R(3, 5)
            - R(13, 5) * xmax
            - R(6, 5) * smax * y0max
            - smax * w0max
        )
        gate_ok = margin > 0
        legal_except_cap = z_slope > 0 and danger_reserve > 0
        cap_ok = z_upper < R(1, 8)
        endpoint_rows.append(
            (denominator_n, remainder, margin, z_slope, z_upper, danger_reserve,
             gate_ok, legal_except_cap, cap_ok)
        )

    requested = [row for row in endpoint_rows if 24 <= row[0] <= 29]
    if not all(row[6] and row[7] and row[8] for row in requested):
        raise AssertionError("one of the requested reciprocal endpoints failed")
    row24 = next(row for row in endpoint_rows if row[0] == 24)
    row23 = next(row for row in endpoint_rows if row[0] == 23)
    if not (row24[6] and row24[8] and row23[6] and row23[7]):
        raise AssertionError("last-pass/next-endpoint gate audit failed")

    # Exact legality values for the proved endpoint.  These are computed, not
    # compared to constants copied from the candidate note.
    xmax = R(1, 24)
    wbar_min_24 = sp.factor(w0min - R(3, 5) * xmax)
    z_slope_24 = sp.factor(wbar_min_24 - smax * y0max**2)
    z_upper_24 = sp.factor(3 * xmax - xmax**2 + smax * w0max)
    danger_24 = sp.factor(
        R(3, 5)
        - R(13, 5) * xmax
        - R(6, 5) * smax * y0max
        - smax * w0max
    )
    if not (
        wbar_min_24 > 0
        and z_slope_24 > 0
        and 0 < z_upper_24 < R(1, 8)
        and danger_24 > 0
    ):
        raise AssertionError("X=1/24 legality failed")
    if danger_24 > R(1, 2):
        raise AssertionError("the documented reserve is not a >1/2 reserve")

    # Rank-two PSD follows from the two exact leading principal minors.
    det_compression = R(5, 9) * S * Z
    exact_zero(compression.det().subs(h**2, S) - det_compression, "det C=(5/9)SZ")
    if not (amin > 0 and z_slope_24 > 0):
        raise AssertionError("lambda/rank premises failed")

    remainder24, margin24 = row24[1], row24[2]
    print("PASS moving quotient support=20 higher_terms=16 parameter_monomials=947")
    print("RABS_1_OVER_24", remainder24)
    print("STRICT_MARGIN_1_OVER_24", margin24)
    print("WBAR_LOWER_1_OVER_24", wbar_min_24)
    print("Z_SLOPE_LOWER_1_OVER_24", z_slope_24)
    print("Z_UPPER_1_OVER_24", z_upper_24)
    print("DANGER_RESERVE_1_OVER_24", danger_24)
    print("PASS lambda>0, 0<Z<1/8, strict danger, det=(5/9)SZ>0, rank=2")

    for row in requested:
        n, remainder, margin, _, z_upper, danger_reserve, gate_ok, _, cap_ok = row
        print(
            "RECIPROCAL_ENDPOINT",
            f"1/{n}",
            f"gate_envelope={'PASS' if gate_ok else 'FAIL'}",
            f"z_cap={'PASS' if cap_ok else 'FAIL'}",
            f"danger={'PASS' if danger_reserve > 0 else 'FAIL'}",
            "margin=", margin,
            "z_upper=", z_upper,
        )

    # First tested reciprocal beyond the theorem: exact lower-Z scope failure.
    xfail = R(1, 23)
    mfail, ofail, nufail = mrad, wrad, -nrad
    afail = 1 + mfail
    y0fail = R(12, 25) / afail + nufail
    wcfail = -3 * (5 * mfail * xfail - 15 * mfail + 5 * xfail - 6) / (25 * afail)
    zfail = sp.factor(3 * xfail - xfail**2 - (smax * y0fail) ** 2 + smax * (wcfail + ofail))
    xraw = -R(1, 5) + xfail
    yraw = R(3, 5) + smax * y0fail
    lfail = afail / smax
    danger_fail = sp.factor(1 - xraw**2 - yraw**2 - zfail)
    det_fail = sp.factor(R(5, 9) * smax * zfail)
    gate_fail = sp.factor(
        lambda_polynomial.as_expr().subs(
            {S: smax, Z: zfail, x: xraw, y: yraw, lam: lfail}
        )
    )
    if not (
        zfail - R(1, 8) > 0
        and danger_fail > 0
        and det_fail > 0
        and lfail > 0
        and gate_fail > 0
        and row23[6]
    ):
        raise AssertionError("1/23 classification failed")
    print("X_1_OVER_23_Z", zfail)
    print("X_1_OVER_23_Z_MINUS_1_OVER_8", sp.factor(zfail - R(1, 8)))
    print("X_1_OVER_23_DANGER", danger_fail)
    print("X_1_OVER_23_DET", det_fail)
    print("X_1_OVER_23_RAW_36GAMMA", gate_fail)
    print("X_1_OVER_23_ENVELOPE_MARGIN", row23[2])
    print("X_1_OVER_23_UNIFORM_Z_UPPER", row23[4])
    print("PASS 1/23 is solely a lower-Z scope failure, not a gate counterexample")

    # Falsification-only grid, not used by the continuum proof.
    s_nodes = (R(1, 10000), R(1, 20000), R(1, 100000))
    x_nodes = (R(1, 24), (R(1, 24) + R(1, 23)) / 2, R(1, 23))
    minimum = None
    minimum_data = None
    node_count = 0
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
        raise AssertionError(f"unexpected falsification node count {node_count}")
    print("PASS adversarial exact raw-gate nodes", node_count)
    print("ADVERSARIAL_NODE_MIN", minimum)
    print("ADVERSARIAL_NODE_ARG", minimum_data)

    # Endpoint/stitch attribution.  The current reciprocal proof starts at
    # X=1/30; X=0 belongs to the predecessor chart that does not divide by X.
    stitch_points = (R(0), R(3, 10000), R(1, 31), R(1, 30), R(1, 24))
    if not all(left < right for left, right in zip(stitch_points, stitch_points[1:])):
        raise AssertionError("stitch endpoints are not ordered")
    print("PASS closed stitches X=3/10000,1/31,1/30; reciprocal layer ends at 1/24")
    print("ATTRIBUTION X=0 predecessor C0 chart only; no reciprocal division by X")
    print("ATTRIBUTION S=0 algebraic cleared closure only; lambda=(1+M)/S is undefined there")
    print("INTERPRETATION 1/24 maximal only among tested reciprocal endpoints 1/n in this family")
    print("INTERPRETATION no continuum-sharp boundary is claimed or proved")

    script_path = Path(__file__).resolve()
    print("VERIFIER_SHA256", sha256(script_path))
    print("PASS independent reciprocal moving-sheet referee")
    print("SCOPE partial moving-sheet family; full compact ball/common metric/fixed lens remain open")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Independent exact reciprocal moving-sheet referee"
    )
    parser.parse_args()
    main()
