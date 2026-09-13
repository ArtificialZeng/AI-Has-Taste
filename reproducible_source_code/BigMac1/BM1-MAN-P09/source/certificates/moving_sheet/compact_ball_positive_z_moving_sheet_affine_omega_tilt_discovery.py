#!/usr/bin/env python3
"""Exact discovery for an affine omega-recentered moving sheet.

The slice keeps all three centered radii and tilts the physical omega center.
This provenance script reconstructs the compact quartic through the established
definition-level discovery interface, rebuilds the sparse moving-sheet
quotient, tests the lossless sigma=S/X envelope, and evaluates exact rational
raw-gate nodes.  It is discovery evidence only; the companion source verifier
reconstructs the fully conjugated Hermitian Q,Q^2 gate without importing this
file or any predecessor verifier.
"""

if not __debug__:
    raise RuntimeError("fail closed: do not run discovery with python -O")

import argparse
import hashlib
from itertools import product
from pathlib import Path

import sympy as sp

from compact_ball_adjacent_z_layers_discovery import reconstruct_quartic
from compact_ball_positive_z_moving_sheet_reciprocal_endpoint_envelope_discovery import (
    centered_box_abs,
    centered_box_lower,
    sparse_add,
    sparse_mul,
    sparse_pow,
)


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def bernstein_controls_2d(expression, first, second):
    """Convert an exact bivariate power polynomial to tensor Bernstein."""
    polynomial = sp.Poly(sp.expand(expression), first, second)
    degree_first = polynomial.degree(first)
    degree_second = polynomial.degree(second)
    power = {
        powers: coefficient for powers, coefficient in polynomial.terms()
    }
    controls = {}
    for i in range(degree_first + 1):
        for j in range(degree_second + 1):
            value = 0
            for k in range(i + 1):
                for ell in range(j + 1):
                    coefficient = power.get((k, ell), 0)
                    value += (
                        coefficient
                        * sp.Rational(sp.binomial(i, k),
                                      sp.binomial(degree_first, k))
                        * sp.Rational(sp.binomial(j, ell),
                                      sp.binomial(degree_second, ell))
                    )
            controls[(i, j)] = sp.factor(value)
    return (degree_first, degree_second), controls


def main():
    R = sp.Rational
    quartic, (S, Z, x, y), lam = reconstruct_quartic()
    mu, X, Y, M = sp.symbols("mu X Y M", real=True)
    omega, nu = sp.symbols("omega nu", real=True)
    A = 1 + M
    denominator = 25 * A
    y0 = (12 + 25 * A * nu) / denominator
    tilt = -R(10636, 275)
    omega_physical = omega + tilt * (X - R(1, 5))
    w0 = (
        45 * M + 18 + 25 * A * (omega - tilt * R(1, 5))
    ) / denominator

    smax = R(1, 10000)
    xmin, xmax = R(1, 5), R(3, 13)
    mrad = R(1, 1000)
    wrad = nrad = R(1, 100)
    amin, amax = 1 - mrad, 1 + mrad
    y0min = R(12, 25) / amax - nrad
    y0max = R(12, 25) / amin + nrad
    w0min = (18 - 45 * mrad) / (25 * amin) - wrad
    w0max = (18 + 45 * mrad) / (25 * amax) + wrad

    # Sparse quotient after the exact positive clearing 25^8(1+M)^8 S^2.
    rescaled = sp.cancel(quartic.as_expr().subs(lam, mu / S))
    numerator = sp.expand((S**3 * rescaled).subs({
        x: -R(1, 5) + X,
        y: R(3, 5) + Y,
        mu: A,
    }))
    ymap = {(1, 0): y0}
    zmap = {
        (0, 1): R(3),
        (0, 2): -R(1),
        (1, 0): w0,
        (1, 1): tilt - R(3, 5),
        (2, 0): -y0**2,
    }
    raw_terms = sp.Poly(numerator, S, Z, X, Y).terms()
    mapped = {}
    for (si, zi, xi, yi), coefficient in raw_terms:
        term = {(si, xi): coefficient}
        term = sparse_mul(term, sparse_pow(zmap, zi))
        term = sparse_mul(term, sparse_pow(ymap, yi))
        mapped = sparse_add(mapped, term)
    cleared = {
        key: sp.factor(sp.cancel(value * denominator**8))
        for key, value in mapped.items()
    }
    if any(value != 0 and key[0] < 2 for key, value in cleared.items()):
        raise AssertionError("missing exact S^2 factor")
    quotient = {
        (si - 2, xi): value
        for (si, xi), value in cleared.items() if value != 0
    }
    if len(raw_terms) != 134:
        raise AssertionError(len(raw_terms))
    h1 = quotient.pop((1, 0))
    expected_h1 = R(152587890625) * M**2 * A**8 * (
        5 * M**2 + 14 * M + 14
    )
    if sp.expand(h1 - expected_h1) != 0:
        raise AssertionError("H1 mismatch")

    variables = (M, omega, nu)
    radii = (mrad, wrad, nrad)
    h2_lowers = {
        key: centered_box_lower(quotient[key], variables, radii)
        for key in ((2, 0), (1, 1), (0, 2))
    }
    h2_status = all(value > 0 for value in h2_lowers.values())

    # Lossless on the whole cell: S=sigma*X and 0<sigma<=1/2000.
    sigmamax = sp.factor(smax / xmin)
    remainder = sp.Integer(0)
    bend = sp.symbols("bend", real=True)
    remainder_poly = sp.Integer(0)
    higher_terms = parameter_monomials = 0
    for (si, xi), coefficient in quotient.items():
        if si + xi <= 2:
            continue
        bound, terms = centered_box_abs(coefficient, variables, radii)
        remainder += bound * sigmamax**si * xmax**(si + xi - 2)
        remainder_poly += bound * sigmamax**si * bend**(si + xi - 2)
        higher_terms += 1
        parameter_monomials += terms
    remainder = sp.factor(remainder)
    remainder_poly = sp.factor(remainder_poly)
    margin = sp.factor(h2_lowers[(0, 2)] - remainder)
    margin_poly = sp.factor(h2_lowers[(0, 2)] - remainder_poly)
    if sigmamax != R(1, 2000):
        raise AssertionError(sigmamax)

    # Two-stage exact Bernstein test: preserve the nonnegative M^2 first
    # layer, recenter X affinely, scale sigma to tau in [0,1], convert the
    # remaining quotient to Bernstein in (tau,u), then bound only the three
    # centered parameters absolutely inside each control.
    tau, useam = sp.symbols("tau useam", real=True)
    Xaff = xmin + (xmax - xmin) * useam
    qcore = sp.expand(sum(
        coefficient * S**si * X**xi
        for (si, xi), coefficient in quotient.items()
    ))
    recentered = sp.expand(qcore.subs({
        S: sigmamax * tau * Xaff,
        X: Xaff,
    }))
    bernstein_degree, controls = bernstein_controls_2d(
        recentered, tau, useam
    )
    control_lowers = {
        key: centered_box_lower(value, variables, radii)
        for key, value in controls.items()
    }
    minimum_control = min(control_lowers.items(), key=lambda item: item[1])
    bernstein_status = minimum_control[1] > 0

    # Legality is separate from the gate envelope.  The physical omega is
    # omega+tilt*(X-xmin), with the same centered radius |omega|<=1/100.
    wbarmin = sp.factor(
        w0min + tilt * (xmax - xmin) - R(3, 5) * xmax
    )
    wbarmax = sp.factor(w0max - R(3, 5) * xmin)
    zlower = sp.factor(
        3 * xmin - xmin**2 + smax * wbarmin - smax**2 * y0max**2
    )
    zupper = sp.factor(3 * xmax - xmax**2 + smax * wbarmax)
    Tmax = sp.factor(
        R(9, 5) + wrad + R(6, 5) * nrad
        - R(63, 125) / amax - R(3, 5) * X
        + tilt * (X - xmin)
    )
    Tmax_right = sp.factor(Tmax.subs(X, xmax))
    danger_smax = sp.factor(
        R(3, 5) - R(13, 5) * X - smax * Tmax
    )
    danger_smax_right = sp.factor(danger_smax.subs(X, xmax))
    legality_ok = (
        0 < smax < xmin < xmax < 3
        and amin > 0 and y0min > 0
        and zlower > 0 and zupper < 1
        and Tmax_right == -R(1, 100)
        and danger_smax_right == R(1, 1000000)
        and sp.diff(danger_smax, X) < 0
    )

    print("RAW_PREMAP_TERMS", len(raw_terms))
    print("QUOTIENT_SX_TERMS", len(quotient) + 1)
    print("HIGHER_SX_TERMS", higher_terms)
    print("PARAMETER_MONOMIALS", parameter_monomials)
    print("QUOTIENT_SUPPORT", sorted([(1, 0)] + list(quotient)))
    print("SIGMA_MAX", sigmamax)
    print("H2_STATUS", "PASS" if h2_status else "BOUND_FAILURE_ONLY")
    print("H2_S2_RESERVE", h2_lowers[(2, 0)])
    print("H2_SX_RESERVE", h2_lowers[(1, 1)])
    print("H2_X2_RESERVE", h2_lowers[(0, 2)])
    print("REMAINDER_ABS", remainder)
    print("STRICT_MARGIN", margin)
    print("ENVELOPE_STATUS",
          "PASS" if h2_status and margin > 0 else "BOUND_FAILURE_ONLY")
    print("LEGALITY_STATUS", "PASS" if legality_ok else "FAIL")
    print("TILT_SLOPE", tilt)
    print("OMEGA_CENTER_RIGHT", tilt * (xmax - xmin))
    print("WBAR_LOWER", wbarmin)
    print("Z_LOWER", zlower)
    print("Z_UPPER", zupper)
    print("TMAX_RIGHT", Tmax_right)
    print("DANGER_SMAX_RIGHT", danger_smax_right)
    positive_roots = sorted(
        float(sp.re(root))
        for root in sp.nroots(sp.together(margin_poly).as_numer_denom()[0])
        if abs(float(sp.im(root))) < 1e-20 and float(sp.re(root)) > 0
    )
    print("ABS_MARGIN_FIRST_POSITIVE_ROOT_APPROX", positive_roots[0])
    for probe in (R(2, 9), R(9, 40), R(23, 100)):
        print("ABS_MARGIN_AT", probe,
              sp.factor(margin_poly.subs(bend, probe)))
    print("TWO_STAGE_BERNSTEIN_DEGREE", bernstein_degree)
    print("TWO_STAGE_BERNSTEIN_CONTROLS", len(controls))
    print("TWO_STAGE_BERNSTEIN_MIN_INDEX", minimum_control[0])
    print("TWO_STAGE_BERNSTEIN_MIN", minimum_control[1])
    print("TWO_STAGE_BERNSTEIN_STATUS",
          "PASS" if bernstein_status else "FAILURE_ONLY")

    # Exact endpoint and interior falsification nodes, evaluated in the raw
    # quartic.  This is not used to prove the continuum envelope.
    records = []
    xmid = sp.factor((xmin + xmax) / 2)
    for sv, xv, mv, ov, nv in product(
        (R(1, 1000000), R(1, 20000), smax),
        (xmin, xmid, xmax),
        (-mrad, mrad),
        (-wrad, wrad),
        (-nrad, nrad),
    ):
        av = 1 + mv
        y0v = R(12, 25) / av + nv
        omega_physical_v = ov + tilt * (xv - xmin)
        w0v = (
            45 * mv + 18 + 25 * av * omega_physical_v
        ) / (25 * av)
        zv = sp.factor(
            3 * xv - xv**2
            + sv * (w0v - R(3, 5) * xv) - sv**2 * y0v**2
        )
        xrv = -R(1, 5) + xv
        yrv = R(3, 5) + sv * y0v
        lv = av / sv
        dv = sp.factor(1 - xrv**2 - yrv**2 - zv)
        detv = sp.factor(R(5, 9) * sv * zv)
        gv = sp.factor(quartic.as_expr().subs({
            S: sv, Z: zv, x: xrv, y: yrv, lam: lv,
        }))
        if not (lv > 0 and zv > 0 and dv > 0 and detv > 0):
            raise AssertionError(("illegal node", sv, xv, mv, ov, nv))
        records.append(((sv, xv, mv, ov, nv), gv, zv, dv, detv))
    negatives = [record for record in records if record[1] < 0]
    minimum = min(records, key=lambda record: record[1])
    print("EXACT_FALSIFICATION_NODES", len(records))
    print("EXACT_NEGATIVE_NODES", len(negatives))
    print("EXACT_NODE_MIN_ARG", minimum[0])
    print("EXACT_NODE_MIN_GATE", minimum[1])
    print("EXACT_NODE_MIN_Z", minimum[2])
    print("EXACT_NODE_MIN_DANGER", minimum[3])
    print("EXACT_NODE_MIN_DET", minimum[4])
    endpoint_corner = (smax, -mrad, -wrad, -nrad)
    for label, endpoint in (("LEFT", xmin), ("RIGHT", xmax)):
        record = next(
            item for item in records
            if item[0] == (
                endpoint_corner[0], endpoint, endpoint_corner[1],
                endpoint_corner[2], endpoint_corner[3],
            )
        )
        print(label + "_WITNESS_ARG", record[0])
        print(label + "_WITNESS_GATE", record[1])
        print(label + "_WITNESS_Z", record[2])
        print(label + "_WITNESS_DANGER", record[3])
        print(label + "_WITNESS_DET", record[4])
    if negatives:
        raise AssertionError(("exact legal negative", negatives[0]))

    print("LEFT_ENDPOINT_STITCH", xmin)
    print("RIGHT_ENDPOINT", xmax)
    print("SCRIPT_SHA256", sha256(Path(__file__).resolve()))
    print("SCOPE discovery only; complete compact ball/common metric/fixed lens open")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Exact discovery for the affine omega tilt"
    )
    parser.parse_args()
    main()
