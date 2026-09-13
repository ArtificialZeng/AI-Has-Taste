#!/usr/bin/env python3
"""Independent exact referee for the adjacent-X positive-Z moving sheet.

This program is intentionally standalone.  It imports neither a discovery
script nor any source-verifier coefficient table.  It reconstructs the
Hermitian Q,Q^2 gate, performs the rational moving-sheet substitution, and
derives all coefficient bounds again from the resulting polynomial.
"""

if not __debug__:
    raise RuntimeError("referee verifier must not be run with python -O")

import argparse
from hashlib import sha256
from pathlib import Path

import sympy as sp


EXPECTED_STATEMENT_SHA256 = (
    "95028dc46a177a8e856200eaba3f954086d6b4335aef34efac6be09783e39e92"
)


def parse_arguments():
    workspace = Path(__file__).resolve().parents[1]
    default_statement = workspace / (
        "tmp/research/common_metric_ranktwo_transverse_compact_ball_"
        "positive_z_moving_sheet_adjacent_x_layer.md"
    )
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--statement",
        type=Path,
        default=default_statement,
        help="the exact theorem note bound to this audit",
    )
    return parser.parse_args()


def require(condition, label):
    if not condition:
        raise RuntimeError(label)


def exact_zero(expression, label):
    if isinstance(expression, sp.MatrixBase):
        for row in range(expression.rows):
            for column in range(expression.cols):
                exact_zero(expression[row, column], f"{label}[{row},{column}]")
        return
    value = sp.factor(sp.cancel(sp.together(sp.expand_complex(expression))))
    if value != 0:
        raise RuntimeError(f"{label}: {value}")


def reduce_mod_kernel(expression, q, kernel_relation):
    """Reduce a rational expression modulo q^2=1-h^2 exactly."""
    if isinstance(expression, sp.MatrixBase):
        return expression.applyfunc(
            lambda entry: reduce_mod_kernel(entry, q, kernel_relation)
        )
    numerator, denominator = sp.cancel(sp.together(expression)).as_numer_denom()
    remainder = sp.Poly(sp.expand(numerator), q).rem(kernel_relation).as_expr()
    return sp.factor(remainder / denominator)


def replace_even_h(expression, h, S):
    """Replace h^(2k) by S^k, failing if an odd power survives."""
    polynomial = sp.Poly(sp.expand(expression), h, domain=sp.EX)
    result = sp.Integer(0)
    for (degree,), coefficient in polynomial.terms():
        require(degree % 2 == 0, f"odd h power survived: {degree}")
        result += coefficient * S ** (degree // 2)
    return sp.expand(result)


def centered_lower(expression, variables, radii):
    """Exact monomial L1 lower bound on a centered rational box."""
    polynomial = sp.Poly(sp.expand(expression), *variables, domain=sp.QQ)
    zero_power = (0,) * len(variables)
    center = polynomial.coeff_monomial(zero_power)
    variation = sp.Integer(0)
    for powers, coefficient in polynomial.terms():
        if powers == zero_power:
            continue
        variation += abs(coefficient) * sp.prod(
            radius**power for radius, power in zip(radii, powers)
        )
    return sp.factor(center - variation), len(polynomial.terms())


def centered_absolute(expression, variables, radii):
    """Exact monomial L1 absolute bound on a centered rational box."""
    polynomial = sp.Poly(sp.expand(expression), *variables, domain=sp.QQ)
    bound = sp.Integer(0)
    for powers, coefficient in polynomial.terms():
        bound += abs(coefficient) * sp.prod(
            radius**power for radius, power in zip(radii, powers)
        )
    return sp.factor(bound), len(polynomial.terms())


def bipoly_add(left, right):
    """Add sparse polynomials keyed by powers of (S,X)."""
    result = dict(left)
    for power, coefficient in right.items():
        result[power] = result.get(power, 0) + coefficient
    return {power: sp.expand(coefficient)
            for power, coefficient in result.items() if coefficient != 0}


def bipoly_multiply(left, right):
    """Multiply sparse (S,X)-polynomials exactly."""
    result = {}
    for (si, xi), left_coefficient in left.items():
        for (sj, xj), right_coefficient in right.items():
            power = (si + sj, xi + xj)
            result[power] = (
                result.get(power, 0) + left_coefficient * right_coefficient
            )
    return {power: sp.expand(coefficient)
            for power, coefficient in result.items() if coefficient != 0}


def bipoly_power(base, exponent):
    result = {(0, 0): sp.Integer(1)}
    for _ in range(exponent):
        result = bipoly_multiply(result, base)
    return result


def main():
    arguments = parse_arguments()
    require(arguments.statement.is_file(), "theorem statement is missing")
    statement_digest = sha256(arguments.statement.read_bytes()).hexdigest()
    require(
        statement_digest == EXPECTED_STATEMENT_SHA256,
        f"theorem statement hash mismatch: {statement_digest}",
    )

    R = sp.Rational
    I = sp.I

    # ------------------------------------------------------------------
    # 1. Reconstruct the original Hermitian Q,Q^2 gate.
    # ------------------------------------------------------------------
    h, q, lam = sp.symbols("h q lambda", real=True)
    S, Z, x, y = sp.symbols("S Z x y", real=True)
    X, M, omega, nu = sp.symbols("X M omega nu", real=True)

    a = 1 / sp.sqrt(6)
    c = sp.sqrt(R(5, 6))
    zeta = R(4, 5) + I * R(3, 5)
    p = sp.Matrix([a, 0, c])
    rvec = sp.Matrix([-a, 0, c * zeta])
    fvec = sp.Matrix([-c * h, q, -a * h * zeta])
    nvec = sp.Matrix([c * q, h, a * q * zeta])
    U = sp.Matrix.hstack(rvec, fvec)
    relation = sp.Poly(q**2 - (1 - h**2), q)

    exact_zero(reduce_mod_kernel(U.conjugate().T * U - sp.eye(2), q, relation),
               "transverse orthonormal frame")
    exact_zero(reduce_mod_kernel(U.conjugate().T * nvec, q, relation),
               "kernel orthogonality")
    exact_zero(reduce_mod_kernel((nvec.conjugate().T * nvec)[0] - 1,
                                 q, relation), "kernel normalization")

    j = (1 + 5 * x) / (3 * sp.sqrt(5))
    kappa = (-3 + 5 * y) / (3 * sp.sqrt(5))
    compression = sp.Matrix([
        [h**2, h * (j + I * kappa)],
        [h * (j - I * kappa), j**2 + kappa**2 + R(5, 9) * Z],
    ])
    exact_zero(compression - compression.conjugate().T,
               "Hermitian compression")
    exact_zero(compression.det() - R(5, 9) * h**2 * Z,
               "compression determinant")

    H = sp.expand(U * compression * U.conjugate().T)
    exact_zero(reduce_mod_kernel(H * nvec, q, relation), "H kernel")
    Q = sp.expand(lam * H)
    Qp = sp.expand(Q * p)
    Q2 = sp.expand(Q * Q)

    first = c * sp.conjugate(Qp[0]) + a * Qp[2] + I * (
        a * c - Q2[2, 0]
    )
    leakage = c * sp.conjugate(Qp[1]) - I * Q2[2, 1]
    raw_gate = sp.expand_complex(
        4 * a**2 * Qp[1] * sp.conjugate(Qp[1])
        + first * sp.conjugate(first)
        + leakage * sp.conjugate(leakage)
        - 32 * a**2 * sp.re(Qp[0])**2
    )
    raw_gate = reduce_mod_kernel(raw_gate, q, relation)
    gate36 = replace_even_h(36 * raw_gate, h, S)
    require(not gate36.has(h, q), "kernel variables survived raw-gate reduction")
    gate_polynomial = sp.Poly(gate36, lam)
    require(gate_polynomial.degree() == 4, "raw gate is not quartic in lambda")
    require(gate_polynomial.nth(0) == 5, "wrong raw-gate constant")

    # An independent vector-quartic reconstruction cross-checks the indexing
    # of both Q^2 entries in the original gate.
    H_image = sp.expand(H * p)
    constant = sp.Matrix([0, I * a * c, 0])
    linear = sp.Matrix([
        2 * a * H_image[1],
        c * sp.conjugate(H_image[0]) + a * H_image[2],
        c * sp.conjugate(H_image[1]),
    ])
    H2 = sp.expand(H * H)
    quadratic = sp.Matrix([0, -I * H2[2, 0], -I * H2[2, 1]])
    vector_gate = sp.expand_complex(
        ((constant + lam * linear + lam**2 * quadratic).conjugate().T
         * (constant + lam * linear + lam**2 * quadratic))[0]
        - 32 * a**2 * lam**2 * sp.re(H_image[0])**2
    )
    exact_zero(reduce_mod_kernel(raw_gate - vector_gate, q, relation),
               "raw gate/vector quartic cross-check")

    # ------------------------------------------------------------------
    # 2. Apply the exact moving-sheet map directly, without cached tables.
    # ------------------------------------------------------------------
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

    # A direct all-at-once substitution creates an enormous transient
    # expression in SymPy.  Instead, enumerate every term of the freshly
    # reconstructed raw polynomial and compose two exact sparse bivariate
    # polynomials.  This is an algebraic reconstruction, not a loaded table.
    mu, Yaux = sp.symbols("mu Yaux", real=True)
    rescaled = sp.cancel(gate36.subs(lam, mu / S))
    numerator_before_map = sp.expand((S**3 * rescaled).subs({
        x: xmap,
        y: R(3, 5) + Yaux,
        mu: A,
    }))
    raw_polynomial = sp.Poly(numerator_before_map, S, Z, X, Yaux)

    y0_sparse = (12 + 25 * A * nu) / (25 * A)
    w0_sparse = (45 * M + 18 + 25 * A * omega) / (25 * A)
    sparse_Y = {(1, 0): y0_sparse}
    sparse_Z = {
        (0, 1): R(3),
        (0, 2): -R(1),
        (1, 0): w0_sparse,
        (1, 1): -R(3, 5),
        (2, 0): -y0_sparse**2,
    }
    mapped_numerator = {}
    for (sdegree, zdegree, xdegree, ydegree), coefficient \
            in raw_polynomial.terms():
        term = {(sdegree, xdegree): coefficient}
        term = bipoly_multiply(term, bipoly_power(sparse_Z, zdegree))
        term = bipoly_multiply(term, bipoly_power(sparse_Y, ydegree))
        mapped_numerator = bipoly_add(mapped_numerator, term)

    clearing = (25 * A) ** 8
    cleared = {}
    for power, coefficient in mapped_numerator.items():
        value = sp.cancel(clearing * coefficient)
        if value == 0:
            continue
        numerator, denominator = value.as_numer_denom()
        require(not denominator.free_symbols,
                f"symbolic denominator survived at {power}: {denominator}")
        cleared[power] = sp.expand(value)
    require(all(sdegree >= 2 for sdegree, _ in cleared),
            "claimed S^2 factor is absent")
    qhat = sp.expand(sum(
        coefficient * S**(sdegree - 2) * X**xdegree
        for (sdegree, xdegree), coefficient in cleared.items()
    ))
    require(sp.Poly(qhat, S, X, M, omega, nu).domain == sp.QQ,
            "cleared quotient is not rational")

    sx_polynomial = sp.Poly(qhat, S, X, domain=sp.EX)
    coefficients = {powers: sp.expand(coefficient)
                    for powers, coefficient in sx_polynomial.terms()}
    require(len(coefficients) == 20, "unexpected (S,X) support size")
    require(max(i for i, _ in coefficients) == 5, "unexpected S degree")
    require(max(jj for _, jj in coefficients) == 4, "unexpected X degree")

    # The isolated degree-one layer is manifestly nonnegative on the box.
    h1 = coefficients.pop((1, 0), None)
    require(h1 is not None, "missing degree-one layer")
    positive_factor = sp.factor(
        sp.cancel(h1 / (M**2 * A**8 * (5 * M**2 + 14 * M + 14)))
    )
    require(positive_factor.is_Rational and positive_factor > 0,
            f"bad H1 factor: {positive_factor}")
    exact_zero(5 * M**2 + 14 * M + 14
               - (5 * (M + R(7, 5))**2 + R(21, 5)),
               "H1 positive completion")
    require(all(i + jj >= 2 for i, jj in coefficients),
            "unaccounted layer below total degree two")

    # Recompute all coefficient-box estimates from the newly expanded qhat.
    parameter_variables = (M, omega, nu)
    parameter_radii = (R(1, 1000), R(1, 100), R(1, 100))
    quadratic_indices = ((2, 0), (1, 1), (0, 2))
    quadratic_lowers = {}
    for index in quadratic_indices:
        lower, _ = centered_lower(
            coefficients[index], parameter_variables, parameter_radii
        )
        quadratic_lowers[index] = lower
        require(lower > 0, f"nonpositive quadratic lower at {index}: {lower}")
    reserve = min(quadratic_lowers.values())

    layer_bounds = {}
    parameter_term_count = 0
    for (sdegree, xdegree), coefficient in coefficients.items():
        total_degree = sdegree + xdegree
        if total_degree == 2:
            continue
        bound, count = centered_absolute(
            coefficient, parameter_variables, parameter_radii
        )
        excess_degree = total_degree - 2
        layer_bounds[excess_degree] = (
            layer_bounds.get(excess_degree, 0) + bound
        )
        parameter_term_count += count
    layer_bounds = {degree: sp.factor(bound)
                    for degree, bound in layer_bounds.items()}
    require(set(layer_bounds) == {1, 2, 3, 4, 5},
            f"unexpected remainder degrees: {sorted(layer_bounds)}")

    def margin(radius):
        return sp.factor(reserve - sum(
            bound * radius**degree
            for degree, bound in layer_bounds.items()
        ))

    old_S_margin = margin(R(1, 10000))
    old_X_margin = margin(R(3, 10000))
    adjacent_margin = margin(R(1, 31))
    failed_bound_at_thirtieth = margin(R(1, 30))
    require(old_S_margin > 0, "predecessor C0 margin is not positive")
    require(old_X_margin > 0, "predecessor C1 margin is not positive")
    require(adjacent_margin > 0, "adjacent C1 margin is not positive")
    require(failed_bound_at_thirtieth < 0,
            "expected inherited sufficient bound to fail at X=1/30")

    # ------------------------------------------------------------------
    # 3. Independently prove every legality and endpoint condition.
    # ------------------------------------------------------------------
    Smax = R(1, 10000)
    stitch = R(3, 10000)
    Xmax = R(1, 31)
    Mradius, omega_radius, nu_radius = parameter_radii
    Amin = 1 - Mradius
    Amax = 1 + Mradius
    require(Amin > 0, "A is not uniformly positive")

    y0min = R(12, 25) / Amax - nu_radius
    y0max = R(12, 25) / Amin + nu_radius
    require(y0min > 0, "y0 can vanish")

    # wc+omega = (45M+18)/(25(1+M)) - 3X/5 + omega.
    w_at_minus = (18 - 45 * Mradius) / (25 * Amin)
    w_at_plus = (18 + 45 * Mradius) / (25 * Amax)
    wlower = w_at_minus - R(3, 5) * Xmax - omega_radius
    wupper = w_at_plus + omega_radius
    exact_zero(
        wc + omega
        - ((45 * M + 18) / (25 * A) - R(3, 5) * X + omega),
        "wc monotonic form",
    )
    require(wlower > 0, "wc+omega can vanish")

    zslope = sp.factor(wlower - Smax * y0max**2)
    zupper = sp.factor(3 * Xmax + Smax * wupper)
    danger_reserve = sp.factor(
        R(3, 5) - R(13, 5) * Xmax
        - R(6, 5) * Smax * y0max - Smax * wupper
    )
    require(zslope > 0, "positive-Z slope is not positive")
    require(zupper < R(1, 8), "Z upper bound does not imply Z<1/8")
    require(danger_reserve > R(1, 2),
            "strict-danger reserve is not greater than one half")

    # At every actual point, Z >= 3X-X^2+S*zslope>0; also
    # det(C)=(5/9)SZ>0.  S>0 is part of the theorem and X<=1/31<3.
    require(0 < Smax < stitch < Xmax < 3, "bad domain ordering")

    # Exact audit of the displayed rational reserves in the theorem note.
    displayed_claims = {
        "wlower": (wlower, R(79093, 114700)),
        "zslope": (zslope, R(237033451226441, 343755900000000)),
        "zupper": (zupper, R(3005268611, 31031000000)),
        "danger": (danger_reserve,
                   R(8886607262249, 17222205000000)),
        "adjacent_margin": (
            adjacent_margin,
            R(42950357876463827039627477692165648038556445276911579,
              984800872161607680000000000000000000000000),
        ),
        "bound_failure_only": (
            failed_bound_at_thirtieth,
            -R(3902147921357110886357029674143626227976364394263,
               171992678400000000000000000000000000000),
        ),
    }
    for label, (derived, displayed) in displayed_claims.items():
        exact_zero(derived - displayed, f"displayed claim {label}")

    # Quantifier/endpoint audit, expressed as logical coverage checks.
    # Predecessor cell: for 0<=X<=stitch, either X<=S (C0, including X=0)
    # or S<=X (C1, where X>0 because S>0).  Adjacent cell: stitch<=X<=Xmax,
    # and S<=Smax<stitch<=X, so C1 is lossless and X^2>0.
    require(stitch <= stitch, "closed-cell overlap missing")
    require(Smax < stitch, "adjacent C1 ordering failed")
    require(stitch > 0, "adjacent chart divides by zero X")
    require(Smax > 0, "predecessor C0 divides by zero S")
    # S=0 is deliberately not added: lambda=A/S is undefined there.

    digest = sha256(Path(__file__).read_bytes()).hexdigest()
    print("PASS standalone reconstruction of original Hermitian Q,Q^2 gate")
    print("PASS independent vector-quartic cross-check and lossless clearing")
    print("PASS continuous centered-box remainder certificate")
    print("PARAMETER_MONOMIALS_RECOMPUTED", parameter_term_count)
    print("QUADRATIC_RESERVE", reserve)
    print("PREDECESSOR_C0_MARGIN", old_S_margin)
    print("PREDECESSOR_C1_MARGIN", old_X_margin)
    print("ADJACENT_C1_MARGIN", adjacent_margin)
    print("PASS merged 0<=X<=1/31 with closed stitch at X=3/10000")
    print("PASS lambda>0, 0<Z<1/8, danger reserve>1/2, rank-two PSD")
    print("PASS X=0 belongs only to predecessor C0; S=0 is not in domain")
    print("BOUND_FAILURE_ONLY_AT_X=1/30", failed_bound_at_thirtieth)
    print("RESULT=PASS exact strict raw 36Gamma on the stated merged family")
    print("SCOPE=partial moving-sheet theorem; no full compact-ball claim")
    print("STATEMENT_SHA256", statement_digest)
    print("CODE_SHA256", digest)


if __name__ == "__main__":
    main()
