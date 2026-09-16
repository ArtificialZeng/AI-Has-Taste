#!/usr/bin/env python3
"""Generate a rigorous adaptive quadratic-stencil certificate on two valleys.

For each exact rational leaf [a,b], the script evaluates q=F(x)/F(x/2)
at a,(a+b)/2,b, encloses q''' throughout [a,b], and applies the quadratic
Lagrange remainder separately to the real and imaginary parts.  The distance
of the resulting complex quadratic from zero is certified by an exact-rational
cover of the normalized variable s in [-1,1].  Each cover segment is accepted
either by direct complex-ball separation or by proving monotonicity of |P(s)|^2
and checking its minimizing endpoint.

All evaluations use 256-bit Arb arithmetic, the exact functional equation,
and terminal derivative bounds following from supp(mu) subset [0,2/3].
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import comb, factorial
from pathlib import Path

import flint
from flint import acb, arb, ctx, fmpq


PRECISION_BITS = 256
RECURSION_DEPTH = 120
MAX_TAYLOR_DEPTH = 30
MAX_POLY_COVER_DEPTH = 80
CENTERS = ("6580077.19160276", "5065070.60771886")
CELL_RADIUS = Fraction(1, 16)
PROVENANCE_JOB = "win-00070-p02-research-7788cb2527f4"

ctx.prec = PRECISION_BITS
P = (arb(5).sqrt() - 1) / 2
P2 = P * P
PI = arb.pi()
TWO = arb(2)
FOUR = arb(4)
A = 4 * PI / 3
MINUS_PI_I = acb(0, -PI)


def as_fmpq(value: Fraction) -> fmpq:
    return fmpq(value.numerator, value.denominator)


def exact_ball(value: Fraction) -> arb:
    return arb(as_fmpq(value))


def interval_ball(left: Fraction, right: Fraction) -> arb:
    midpoint = (left + right) / 2
    radius = (right - left) / 2
    return arb(as_fmpq(midpoint), as_fmpq(radius))


def rational_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def serialized_ball(value: arb) -> str:
    text = value.str(90, radius=True, more=True)
    assert arb(text).contains(value)
    return text


def serialized_complex(value: acb) -> dict[str, str]:
    return {"re": serialized_ball(value.real), "im": serialized_ball(value.imag)}


def terminal_jet(t: arb) -> list[acb]:
    """Enclose F and its first three derivatives at every point in t."""
    value_radius = A * abs(t)
    result = [acb(arb(1, value_radius), arb(0, value_radius))]
    # F^(n)(t)=int(-2*pi*i*y)^n exp(-2*pi*i*t*y)dmu and 0<=y<=2/3.
    for n in range(1, 4):
        derivative_radius = A**n
        result.append(
            acb(arb(0, derivative_radius), arb(0, derivative_radius))
        )
    return result


def fourier_jets(x: arb) -> tuple[list[acb], list[acb]]:
    """Enclose F^(0..3)(X) and F^(0..3)(X/2)."""
    next_jet = terminal_jet(x / (TWO**RECURSION_DEPTH))
    next2_jet = terminal_jet(x / (TWO ** (RECURSION_DEPTH + 1)))

    for k in range(RECURSION_DEPTH - 1, -1, -1):
        y = x / (TWO**k)
        phase = (MINUS_PI_I * y).exp()
        current: list[acb] = []
        for n in range(4):
            first = P * next_jet[n] / (TWO**n)
            second_sum = acb(0)
            for j in range(n + 1):
                second_sum += (
                    comb(n, j)
                    * (MINUS_PI_I ** (n - j))
                    * next2_jet[j]
                    / (FOUR**j)
                )
            current.append(first + P2 * phase * second_sum)
        next2_jet, next_jet = next_jet, current

    return next_jet, next2_jet


def quotient_jets(x: arb) -> tuple[list[acb], acb]:
    """Enclose q^(0..3)(X), q(x)=F(x)/F(x/2), by series division."""
    numerator, half_argument_jet = fourier_jets(x)
    denominator = [half_argument_jet[n] / (TWO**n) for n in range(4)]
    if denominator[0].contains(0):
        raise ValueError("quotient denominator enclosure contains zero")

    numerator_coeff = [numerator[n] / factorial(n) for n in range(4)]
    denominator_coeff = [denominator[n] / factorial(n) for n in range(4)]
    quotient_coeff: list[acb] = []
    for n in range(4):
        residual = numerator_coeff[n]
        for j in range(1, n + 1):
            residual -= denominator_coeff[j] * quotient_coeff[n - j]
        quotient_coeff.append(residual / denominator_coeff[0])
    return (
        [quotient_coeff[n] * factorial(n) for n in range(4)],
        denominator[0],
    )


def polynomial_value(coefficients: tuple[acb, acb, acb], s: arb) -> acb:
    constant, linear, quadratic = coefficients
    return constant + s * (linear + s * quadratic)


def squared_norm_derivative(
    coefficients: tuple[acb, acb, acb], s: arb
) -> arb:
    constant, linear, quadratic = coefficients
    value = constant + s * (linear + s * quadratic)
    derivative = linear + 2 * s * quadratic
    return 2 * (
        value.real * derivative.real + value.imag * derivative.imag
    )


def prove_quadratic_distance(
    coefficients: tuple[acb, acb, acb], error_norm: arb
) -> tuple[list[dict], arb] | None:
    """Prove |P(s)|>error_norm on [-1,1] by a rational segment cover."""
    stack = [(Fraction(-1), Fraction(1), 0)]
    accepted: list[dict] = []
    global_lower: arb | None = None

    while stack:
        left, right, depth = stack.pop()
        s_interval = interval_ball(left, right)
        value = polynomial_value(coefficients, s_interval)
        direct_lower = value.abs_lower()
        method = None
        witness_lower = direct_lower

        if direct_lower > error_norm:
            method = "direct"
        else:
            derivative = squared_norm_derivative(coefficients, s_interval)
            if derivative > 0:
                endpoint_value = polynomial_value(coefficients, exact_ball(left))
                witness_lower = endpoint_value.abs_lower()
                if witness_lower > error_norm:
                    method = "increasing_squared_norm"
            elif derivative < 0:
                endpoint_value = polynomial_value(coefficients, exact_ball(right))
                witness_lower = endpoint_value.abs_lower()
                if witness_lower > error_norm:
                    method = "decreasing_squared_norm"

        if method is not None:
            accepted.append(
                {
                    "left": rational_text(left),
                    "right": rational_text(right),
                    "cover_depth": depth,
                    "method": method,
                    "distance_lower": serialized_ball(witness_lower),
                }
            )
            if global_lower is None or witness_lower < global_lower:
                global_lower = witness_lower
            continue

        if depth >= MAX_POLY_COVER_DEPTH:
            return None
        midpoint = (left + right) / 2
        stack.append((midpoint, right, depth + 1))
        stack.append((left, midpoint, depth + 1))

    assert accepted and global_lower is not None
    assert accepted[0]["left"] == "-1"
    assert accepted[-1]["right"] == "1"
    for previous, following in zip(accepted, accepted[1:]):
        assert previous["right"] == following["left"]
    return accepted, global_lower


def try_taylor_leaf(left: Fraction, right: Fraction, depth: int) -> dict | None:
    midpoint = (left + right) / 2
    halfwidth = (right - left) / 2
    node_arguments = (left, midpoint, right)
    node_values: list[acb] = []
    node_denominators: list[acb] = []
    try:
        for argument in node_arguments:
            jets, denominator = quotient_jets(exact_ball(argument))
            node_values.append(jets[0])
            node_denominators.append(denominator)
        interval_jets, interval_denominator = quotient_jets(
            interval_ball(left, right)
        )
    except ValueError:
        return None

    left_value, middle_value, right_value = node_values
    coefficients = (
        middle_value,
        (right_value - left_value) / 2,
        (right_value + left_value) / 2 - middle_value,
    )
    third = interval_jets[3]
    max_product_over_s_div_6 = arb(1) / (9 * arb(3).sqrt())
    scale = exact_ball(halfwidth**3) * max_product_over_s_div_6
    error_re = third.real.abs_upper() * scale
    error_im = third.imag.abs_upper() * scale
    error_norm = (error_re**2 + error_im**2).sqrt()

    distance_proof = prove_quadratic_distance(coefficients, error_norm)
    if distance_proof is None:
        return None
    cover, distance_lower = distance_proof

    return {
        "left": rational_text(left),
        "right": rational_text(right),
        "taylor_bisect_depth": depth,
        "node_arguments": [rational_text(x) for x in node_arguments],
        "node_q": [serialized_complex(x) for x in node_values],
        "node_denominator": [serialized_complex(x) for x in node_denominators],
        "interval_denominator": serialized_complex(interval_denominator),
        "q_third_derivative": serialized_complex(third),
        "remainder_re_abs_upper": serialized_ball(error_re),
        "remainder_im_abs_upper": serialized_ball(error_im),
        "remainder_norm_upper": serialized_ball(error_norm),
        "quadratic_coefficients": [serialized_complex(x) for x in coefficients],
        "quadratic_distance_lower": serialized_ball(distance_lower),
        "polynomial_cover_segment_count": len(cover),
        "maximum_polynomial_cover_depth": max(x["cover_depth"] for x in cover),
        "polynomial_cover": cover,
    }


def whole_cell_diagnostic(left: Fraction, right: Fraction) -> dict:
    """Record why one quadratic stencil on the full cell is insufficient."""
    midpoint = (left + right) / 2
    halfwidth = (right - left) / 2
    node_values = [
        quotient_jets(exact_ball(argument))[0][0]
        for argument in (left, midpoint, right)
    ]
    interval_jets, interval_denominator = quotient_jets(
        interval_ball(left, right)
    )
    third = interval_jets[3]
    scale = exact_ball(halfwidth**3) / (9 * arb(3).sqrt())
    error_re = third.real.abs_upper() * scale
    error_im = third.imag.abs_upper() * scale
    error_norm = (error_re**2 + error_im**2).sqrt()
    middle_value = node_values[1]
    center_tube_overlaps_zero = (
        not (middle_value.real.abs_lower() > error_re)
        and not (middle_value.imag.abs_lower() > error_im)
    )
    assert center_tube_overlaps_zero
    return {
        "q_third_derivative": serialized_complex(third),
        "interval_denominator": serialized_complex(interval_denominator),
        "remainder_re_abs_upper": serialized_ball(error_re),
        "remainder_im_abs_upper": serialized_ball(error_im),
        "remainder_norm_upper": serialized_ball(error_norm),
        "center_q": serialized_complex(middle_value),
        "componentwise_remainder_tube_at_center_overlaps_zero": True,
        "diagnosis": (
            "one full-cell quadratic stencil is inconclusive under this "
            "uniform third-derivative enclosure"
        ),
    }


def certify_cell(center_text: str) -> dict:
    center = Fraction(center_text)
    cell_left = center - CELL_RADIUS
    cell_right = center + CELL_RADIUS
    stack = [(cell_left, cell_right, 0)]
    leaves: list[dict] = []
    attempted = 0

    while stack:
        left, right, depth = stack.pop()
        attempted += 1
        leaf = try_taylor_leaf(left, right, depth)
        if leaf is not None:
            leaves.append(leaf)
            continue
        if depth >= MAX_TAYLOR_DEPTH:
            raise RuntimeError(
                f"Taylor certification failed at depth {depth} on "
                f"[{rational_text(left)}, {rational_text(right)}]"
            )
        midpoint = (left + right) / 2
        stack.append((midpoint, right, depth + 1))
        stack.append((left, midpoint, depth + 1))

    assert leaves[0]["left"] == rational_text(cell_left)
    assert leaves[-1]["right"] == rational_text(cell_right)
    for previous, following in zip(leaves, leaves[1:]):
        assert previous["right"] == following["left"]
    return {
        "center_printed_decimal": center_text,
        "left": rational_text(cell_left),
        "right": rational_text(cell_right),
        "leaf_count": len(leaves),
        "attempted_taylor_nodes": attempted,
        "maximum_taylor_bisect_depth": max(
            x["taylor_bisect_depth"] for x in leaves
        ),
        "whole_cell_stencil_diagnostic": whole_cell_diagnostic(
            cell_left, cell_right
        ),
        "leaves": leaves,
    }


def build_certificate() -> dict:
    cells = [certify_cell(center) for center in CENTERS]
    return {
        "schema": "win-00070-p02-taylor-stencils-v1",
        "provenance_job_id": PROVENANCE_JOB,
        "claim_scope": (
            "F(x) is nonzero on each closed radius-1/16 cell centered at "
            "the two listed exact printed decimals"
        ),
        "arithmetic": {
            "library": "python-flint",
            "library_version": flint.__version__,
            "precision_bits": PRECISION_BITS,
            "rounding": "Arb outward ball arithmetic",
            "recursion_depth": RECURSION_DEPTH,
            "terminal_value_bound": "|F(t)-1| <= (4*pi/3)*|t|",
            "terminal_derivative_bound": "|F^(n)(t)| <= (4*pi/3)^n, n=1,2,3",
            "support_bound": "supp(mu) subset [0,2/3]",
            "interpolation_remainder": (
                "componentwise |q-P2| <= sup|component(q''')|*h^3/(9*sqrt(3))"
            ),
        },
        "cell_radius": rational_text(CELL_RADIUS),
        "total_taylor_leaf_count": sum(x["leaf_count"] for x in cells),
        "total_polynomial_cover_segment_count": sum(
            leaf["polynomial_cover_segment_count"]
            for cell in cells
            for leaf in cell["leaves"]
        ),
        "cells": cells,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("evidence/research_taylor_stencils_certificate.json"),
    )
    args = parser.parse_args()
    certificate = build_certificate()
    args.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    for cell in certificate["cells"]:
        print(
            f"cell {cell['left']} .. {cell['right']}: "
            f"{cell['leaf_count']} Taylor leaves, max depth "
            f"{cell['maximum_taylor_bisect_depth']}"
        )
    print(
        f"wrote {args.output}: {certificate['total_taylor_leaf_count']} Taylor "
        f"leaves and {certificate['total_polynomial_cover_segment_count']} "
        "polynomial-cover segments"
    )


if __name__ == "__main__":
    main()
