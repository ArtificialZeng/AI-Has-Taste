#!/usr/bin/env python3
"""Independent structural and 320-bit replay of the Taylor-stencil certificate.

The fresh evaluator stores exponential Taylor coefficients rather than raw
derivatives and uses recursion depth 128 instead of the generator's 120.  It
checks the serialized rational covers, every stored denominator and polynomial
witness, then recomputes every node value, uniform third derivative, remainder,
and quadratic separation at 320-bit precision.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from math import factorial
from pathlib import Path

import flint
from flint import acb, arb, ctx, fmpq


EXPECTED_SCHEMA = "win-00070-p02-taylor-stencils-v1"
EXPECTED_JOB = "win-00070-p02-research-7788cb2527f4"
EXPECTED_CENTERS = ("6580077.19160276", "5065070.60771886")
EXPECTED_RADIUS = Fraction(1, 16)
VERIFY_PRECISION = 320
VERIFY_DEPTH = 128
MAX_COVER_DEPTH = 90


def parse_rational(text: str) -> Fraction:
    if "/" in text:
        numerator, denominator = text.split("/", 1)
        return Fraction(int(numerator), int(denominator))
    return Fraction(int(text), 1)


def exact_ball(value: Fraction) -> arb:
    return arb(fmpq(value.numerator, value.denominator))


def interval_ball(left: Fraction, right: Fraction) -> arb:
    midpoint = (left + right) / 2
    radius = (right - left) / 2
    return arb(
        fmpq(midpoint.numerator, midpoint.denominator),
        fmpq(radius.numerator, radius.denominator),
    )


def parse_complex(record: dict[str, str]) -> acb:
    return acb(arb(record["re"]), arb(record["im"]))


def fresh_terminal_coefficients(t: arb, analytic_bound: arb) -> list[acb]:
    value_radius = analytic_bound * abs(t)
    result = [acb(arb(1, value_radius), arb(0, value_radius))]
    for n in range(1, 4):
        radius = analytic_bound**n / factorial(n)
        result.append(acb(arb(0, radius), arb(0, radius)))
    return result


def fresh_fourier_coefficients(x: arb) -> tuple[list[acb], list[acb]]:
    """Return Taylor coefficients F^(n)/n! at X and X/2."""
    p = (arb(5).sqrt() - 1) / 2
    pi = arb.pi()
    two = arb(2)
    four = arb(4)
    analytic_bound = 4 * pi / 3
    minus_pi_i = acb(0, -pi)

    at_half = fresh_terminal_coefficients(
        x / (two**VERIFY_DEPTH), analytic_bound
    )
    at_quarter = fresh_terminal_coefficients(
        x / (two ** (VERIFY_DEPTH + 1)), analytic_bound
    )
    for level in range(VERIFY_DEPTH - 1, -1, -1):
        argument = x / (two**level)
        phase = (minus_pi_i * argument).exp()
        current: list[acb] = []
        for n in range(4):
            first = p * at_half[n] / (two**n)
            convolution = acb(0)
            for j in range(n + 1):
                phase_coefficient = (
                    minus_pi_i ** (n - j) / factorial(n - j)
                )
                convolution += (
                    phase_coefficient * at_quarter[j] / (four**j)
                )
            current.append(first + p * p * phase * convolution)
        at_quarter, at_half = at_half, current
    return at_half, at_quarter


def fresh_quotient(x: arb) -> tuple[list[acb], acb]:
    numerator, half_coefficients = fresh_fourier_coefficients(x)
    denominator = [
        half_coefficients[n] / (arb(2) ** n) for n in range(4)
    ]
    assert not denominator[0].contains(0)
    quotient: list[acb] = []
    for n in range(4):
        residual = numerator[n]
        for j in range(1, n + 1):
            residual -= denominator[j] * quotient[n - j]
        quotient.append(residual / denominator[0])
    return quotient, denominator[0]


def polynomial_value(coefficients: tuple[acb, acb, acb], s: arb) -> acb:
    return coefficients[0] + s * (coefficients[1] + s * coefficients[2])


def squared_norm_derivative(
    coefficients: tuple[acb, acb, acb], s: arb
) -> arb:
    value = polynomial_value(coefficients, s)
    derivative = coefficients[1] + 2 * s * coefficients[2]
    return 2 * (
        value.real * derivative.real + value.imag * derivative.imag
    )


def check_segment_witnesses(leaf: dict) -> None:
    coefficients = tuple(
        parse_complex(x) for x in leaf["quadratic_coefficients"]
    )
    assert len(coefficients) == 3
    error = arb(leaf["remainder_norm_upper"])
    cover = leaf["polynomial_cover"]
    assert cover
    assert len(cover) == leaf["polynomial_cover_segment_count"]
    next_left = Fraction(-1)
    maximum_depth = 0
    for segment in cover:
        left = parse_rational(segment["left"])
        right = parse_rational(segment["right"])
        depth = int(segment["cover_depth"])
        assert left == next_left
        assert left < right <= 1
        assert right - left == Fraction(2, 2**depth)
        alignment = (left + 1) / (right - left)
        assert alignment.denominator == 1
        maximum_depth = max(maximum_depth, depth)
        interval = interval_ball(left, right)
        method = segment["method"]
        if method == "direct":
            lower = polynomial_value(coefficients, interval).abs_lower()
        elif method == "increasing_squared_norm":
            assert squared_norm_derivative(coefficients, interval) > 0
            lower = polynomial_value(coefficients, exact_ball(left)).abs_lower()
        elif method == "decreasing_squared_norm":
            assert squared_norm_derivative(coefficients, interval) < 0
            lower = polynomial_value(coefficients, exact_ball(right)).abs_lower()
        else:
            raise AssertionError("unknown polynomial-cover method")
        assert lower > error
        next_left = right
    assert next_left == 1
    assert maximum_depth == leaf["maximum_polynomial_cover_depth"]


def fresh_distance_proof(
    coefficients: tuple[acb, acb, acb], error: arb
) -> tuple[int, int]:
    stack = [(Fraction(-1), Fraction(1), 0)]
    accepted = 0
    maximum_depth = 0
    while stack:
        left, right, depth = stack.pop()
        interval = interval_ball(left, right)
        value = polynomial_value(coefficients, interval)
        success = value.abs_lower() > error
        if not success:
            derivative = squared_norm_derivative(coefficients, interval)
            if derivative > 0:
                success = (
                    polynomial_value(coefficients, exact_ball(left)).abs_lower()
                    > error
                )
            elif derivative < 0:
                success = (
                    polynomial_value(coefficients, exact_ball(right)).abs_lower()
                    > error
                )
        if success:
            accepted += 1
            maximum_depth = max(maximum_depth, depth)
            continue
        assert depth < MAX_COVER_DEPTH
        midpoint = (left + right) / 2
        stack.append((midpoint, right, depth + 1))
        stack.append((left, midpoint, depth + 1))
    return accepted, maximum_depth


def verify(path: Path) -> None:
    raw = path.read_bytes()
    certificate = json.loads(raw)
    assert certificate["schema"] == EXPECTED_SCHEMA
    assert certificate["provenance_job_id"] == EXPECTED_JOB
    assert parse_rational(certificate["cell_radius"]) == EXPECTED_RADIUS
    arithmetic = certificate["arithmetic"]
    assert arithmetic["library"] == "python-flint"
    assert arithmetic["library_version"] == flint.__version__
    assert arithmetic["precision_bits"] == 256
    assert arithmetic["recursion_depth"] == 120

    # First audit the frozen serialized proof at its stated precision.
    ctx.prec = 256
    total_leaves = 0
    total_stored_segments = 0
    cells = certificate["cells"]
    assert len(cells) == 2
    for cell, center_text in zip(cells, EXPECTED_CENTERS):
        center = Fraction(center_text)
        cell_left = center - EXPECTED_RADIUS
        cell_right = center + EXPECTED_RADIUS
        assert cell["center_printed_decimal"] == center_text
        assert parse_rational(cell["left"]) == cell_left
        assert parse_rational(cell["right"]) == cell_right
        diagnostic = cell["whole_cell_stencil_diagnostic"]
        assert not parse_complex(diagnostic["interval_denominator"]).contains(0)
        diagnostic_center = parse_complex(diagnostic["center_q"])
        diagnostic_error_re = arb(diagnostic["remainder_re_abs_upper"])
        diagnostic_error_im = arb(diagnostic["remainder_im_abs_upper"])
        assert not (diagnostic_center.real.abs_lower() > diagnostic_error_re)
        assert not (diagnostic_center.imag.abs_lower() > diagnostic_error_im)
        assert diagnostic[
            "componentwise_remainder_tube_at_center_overlaps_zero"
        ] is True
        leaves = cell["leaves"]
        assert len(leaves) == cell["leaf_count"]
        next_left = cell_left
        maximum_depth = 0
        for leaf in leaves:
            left = parse_rational(leaf["left"])
            right = parse_rational(leaf["right"])
            depth = int(leaf["taylor_bisect_depth"])
            assert left == next_left
            assert left < right <= cell_right
            assert right - left == (cell_right - cell_left) / (2**depth)
            alignment = (left - cell_left) / (right - left)
            assert alignment.denominator == 1
            maximum_depth = max(maximum_depth, depth)
            assert parse_rational(leaf["node_arguments"][0]) == left
            assert parse_rational(leaf["node_arguments"][1]) == (left + right) / 2
            assert parse_rational(leaf["node_arguments"][2]) == right
            for denominator in leaf["node_denominator"]:
                assert not parse_complex(denominator).contains(0)
            assert not parse_complex(leaf["interval_denominator"]).contains(0)
            assert arb(leaf["quadratic_distance_lower"]) > arb(
                leaf["remainder_norm_upper"]
            )
            check_segment_witnesses(leaf)
            total_stored_segments += leaf["polynomial_cover_segment_count"]
            next_left = right
        assert next_left == cell_right
        assert maximum_depth == cell["maximum_taylor_bisect_depth"]
        total_leaves += len(leaves)
        print(
            f"VERIFIED stored cell {center_text}: {len(leaves)} gap-free "
            f"Taylor leaves, max depth {maximum_depth}"
        )
    assert total_leaves == certificate["total_taylor_leaf_count"]
    assert total_stored_segments == certificate[
        "total_polynomial_cover_segment_count"
    ]

    # Recompute all analytic enclosures with a distinct depth and precision.
    ctx.prec = VERIFY_PRECISION
    fresh_segments = 0
    fresh_max_cover_depth = 0
    for cell in cells:
        cell_left = parse_rational(cell["left"])
        cell_right = parse_rational(cell["right"])
        diagnostic = cell["whole_cell_stencil_diagnostic"]
        fresh_whole, fresh_whole_denominator = fresh_quotient(
            interval_ball(cell_left, cell_right)
        )
        fresh_center, _ = fresh_quotient(
            exact_ball((cell_left + cell_right) / 2)
        )
        assert parse_complex(diagnostic["interval_denominator"]).contains(
            fresh_whole_denominator
        )
        assert parse_complex(diagnostic["q_third_derivative"]).contains(
            6 * fresh_whole[3]
        )
        assert parse_complex(diagnostic["center_q"]).contains(fresh_center[0])
        for leaf in cell["leaves"]:
            left = parse_rational(leaf["left"])
            right = parse_rational(leaf["right"])
            midpoint = (left + right) / 2
            node_values: list[acb] = []
            for index, argument in enumerate((left, midpoint, right)):
                coefficients, denominator = fresh_quotient(exact_ball(argument))
                stored_q = parse_complex(leaf["node_q"][index])
                stored_denominator = parse_complex(
                    leaf["node_denominator"][index]
                )
                assert stored_q.contains(coefficients[0])
                assert stored_denominator.contains(denominator)
                node_values.append(coefficients[0])

            interval_coefficients, interval_denominator = fresh_quotient(
                interval_ball(left, right)
            )
            stored_interval_denominator = parse_complex(
                leaf["interval_denominator"]
            )
            stored_third = parse_complex(leaf["q_third_derivative"])
            fresh_third = 6 * interval_coefficients[3]
            assert stored_interval_denominator.contains(interval_denominator)
            assert stored_third.contains(fresh_third)

            halfwidth = (right - left) / 2
            scale = exact_ball(halfwidth**3) / (9 * arb(3).sqrt())
            error_re = fresh_third.real.abs_upper() * scale
            error_im = fresh_third.imag.abs_upper() * scale
            error = (error_re**2 + error_im**2).sqrt()
            coefficients = (
                node_values[1],
                (node_values[2] - node_values[0]) / 2,
                (node_values[2] + node_values[0]) / 2 - node_values[1],
            )
            count, depth = fresh_distance_proof(coefficients, error)
            fresh_segments += count
            fresh_max_cover_depth = max(fresh_max_cover_depth, depth)

    print(
        f"VERIFIED fresh 320-bit/depth-128 replay: {total_leaves} Taylor "
        f"leaves, {fresh_segments} polynomial-cover segments, max cover "
        f"depth {fresh_max_cover_depth}"
    )
    print(f"certificate_sha256={hashlib.sha256(raw).hexdigest()}")
    print(
        "CONCLUSION: F(x) != 0 throughout both closed radius-1/16 cells; "
        "the adaptive Taylor proof uses 8 and 10 leaves instead of the "
        "previous direct recursion's 78 and 148 leaves."
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "certificate",
        nargs="?",
        type=Path,
        default=Path("evidence/research_taylor_stencils_certificate.json"),
    )
    args = parser.parse_args()
    verify(args.certificate)


if __name__ == "__main__":
    main()
