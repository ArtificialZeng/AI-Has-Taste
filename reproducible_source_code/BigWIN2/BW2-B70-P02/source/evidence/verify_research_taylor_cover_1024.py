#!/usr/bin/env python3
"""Audit and independently replay the [27/25,1024] Taylor cover.

The first pass checks the complete exact-rational partition and every stored
256-bit witness.  The second pass uses the independently written Taylor-
coefficient recurrence from ``verify_research_taylor_stencils.py`` at 320 bits
and recursion depth 128, recomputing every accepted leaf.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from fractions import Fraction
from math import factorial
from pathlib import Path

import flint
from flint import arb, ctx

import verify_research_taylor_stencils as fresh


EXPECTED_SCHEMA = "win-00070-p02-taylor-cover-1024-v1"
EXPECTED_JOB = "win-00070-p02-research-5ae3369c8f92"
LEFT = Fraction(27, 25)
RIGHT = Fraction(1024)
INITIAL_WIDTH = Fraction(1, 8)
EXPECTED_INITIAL_CELL_COUNT = 8184


def validate_stored(certificate: dict) -> tuple[int, int]:
    assert certificate["schema"] == EXPECTED_SCHEMA
    assert certificate["provenance_job_id"] == EXPECTED_JOB
    assert fresh.parse_rational(certificate["domain_left"]) == LEFT
    assert fresh.parse_rational(certificate["domain_right"]) == RIGHT
    assert (
        fresh.parse_rational(certificate["initial_width_upper_bound"])
        == INITIAL_WIDTH
    )
    assert certificate["initial_cell_count"] == EXPECTED_INITIAL_CELL_COUNT
    arithmetic = certificate["arithmetic"]
    assert arithmetic["library"] == "python-flint"
    assert arithmetic["library_version"] == flint.__version__
    assert arithmetic["precision_bits"] == 256
    assert arithmetic["recursion_depth"] == 120

    ctx.prec = 256
    cells = certificate["cells"]
    assert len(cells) == EXPECTED_INITIAL_CELL_COUNT
    next_cell_left = LEFT
    total_leaves = 0
    total_attempted = 0
    total_segments = 0
    maximum_taylor_depth = 0
    maximum_cover_depth = 0
    taylor_depth_histogram: Counter[int] = Counter()
    cover_depth_histogram: Counter[int] = Counter()

    for index, cell in enumerate(cells):
        left = fresh.parse_rational(cell["left"])
        right = fresh.parse_rational(cell["right"])
        assert cell["index"] == index
        assert left == next_cell_left
        assert right == min(left + INITIAL_WIDTH, RIGHT)
        assert left < right and right - left <= INITIAL_WIDTH
        leaves = cell["leaves"]
        assert leaves and len(leaves) == cell["leaf_count"]
        assert cell["attempted_taylor_nodes"] == 2 * len(leaves) - 1
        next_leaf_left = left
        cell_maximum_depth = 0
        for leaf in leaves:
            leaf_left = fresh.parse_rational(leaf["left"])
            leaf_right = fresh.parse_rational(leaf["right"])
            depth = int(leaf["taylor_bisect_depth"])
            assert leaf_left == next_leaf_left
            assert leaf_left < leaf_right <= right
            assert leaf_right - leaf_left == (right - left) / (2**depth)
            alignment = (leaf_left - left) / (leaf_right - leaf_left)
            assert alignment.denominator == 1
            expected_nodes = (leaf_left, (leaf_left + leaf_right) / 2, leaf_right)
            assert tuple(
                fresh.parse_rational(value) for value in leaf["node_arguments"]
            ) == expected_nodes
            for denominator in leaf["node_denominator"]:
                assert not fresh.parse_complex(denominator).contains(0)
            assert not fresh.parse_complex(leaf["interval_denominator"]).contains(0)
            assert arb(leaf["quadratic_distance_lower"]) > arb(
                leaf["remainder_norm_upper"]
            )
            fresh.check_segment_witnesses(leaf)

            segment_count = int(leaf["polynomial_cover_segment_count"])
            cover_depth = int(leaf["maximum_polynomial_cover_depth"])
            total_segments += segment_count
            maximum_cover_depth = max(maximum_cover_depth, cover_depth)
            maximum_taylor_depth = max(maximum_taylor_depth, depth)
            cell_maximum_depth = max(cell_maximum_depth, depth)
            taylor_depth_histogram[depth] += 1
            cover_depth_histogram[cover_depth] += 1
            next_leaf_left = leaf_right
        assert next_leaf_left == right
        assert cell["maximum_taylor_bisect_depth"] == cell_maximum_depth
        total_leaves += len(leaves)
        total_attempted += cell["attempted_taylor_nodes"]
        next_cell_left = right

    assert next_cell_left == RIGHT
    assert total_leaves == certificate["total_taylor_leaf_count"]
    assert total_attempted == certificate["total_attempted_taylor_nodes"]
    assert total_segments == certificate["total_polynomial_cover_segment_count"]
    assert maximum_taylor_depth == certificate["maximum_taylor_bisect_depth"]
    assert maximum_cover_depth == certificate["maximum_polynomial_cover_depth"]
    assert {
        str(key): taylor_depth_histogram[key]
        for key in sorted(taylor_depth_histogram)
    } == certificate["taylor_leaf_depth_histogram"]
    assert {
        str(key): cover_depth_histogram[key]
        for key in sorted(cover_depth_histogram)
    } == certificate["leaf_maximum_polynomial_cover_depth_histogram"]
    print(
        f"VERIFIED stored gap-free partition: {len(cells)} initial cells, "
        f"{total_leaves} Taylor leaves, {total_segments} polynomial segments, "
        f"max Taylor depth {maximum_taylor_depth}",
        flush=True,
    )
    return total_leaves, total_segments


def replay_fresh(certificate: dict, total_leaves: int) -> tuple[int, int]:
    ctx.prec = fresh.VERIFY_PRECISION
    replayed = 0
    fresh_segments = 0
    fresh_maximum_cover_depth = 0
    for cell_index, cell in enumerate(certificate["cells"]):
        for leaf in cell["leaves"]:
            left = fresh.parse_rational(leaf["left"])
            right = fresh.parse_rational(leaf["right"])
            midpoint = (left + right) / 2
            node_values = []
            for index, argument in enumerate((left, midpoint, right)):
                coefficients, denominator = fresh.fresh_quotient(
                    fresh.exact_ball(argument)
                )
                assert fresh.parse_complex(leaf["node_q"][index]).contains(
                    coefficients[0]
                )
                assert fresh.parse_complex(
                    leaf["node_denominator"][index]
                ).contains(denominator)
                node_values.append(coefficients[0])

            interval_coefficients, interval_denominator = fresh.fresh_quotient(
                fresh.interval_ball(left, right)
            )
            stored_interval_denominator = fresh.parse_complex(
                leaf["interval_denominator"]
            )
            stored_third = fresh.parse_complex(leaf["q_third_derivative"])
            fresh_third = factorial(3) * interval_coefficients[3]
            assert stored_interval_denominator.contains(interval_denominator)
            assert stored_third.contains(fresh_third)

            halfwidth = (right - left) / 2
            scale = fresh.exact_ball(halfwidth**3) / (9 * arb(3).sqrt())
            error_re = fresh_third.real.abs_upper() * scale
            error_im = fresh_third.imag.abs_upper() * scale
            error = (error_re**2 + error_im**2).sqrt()
            quadratic = (
                node_values[1],
                (node_values[2] - node_values[0]) / 2,
                (node_values[2] + node_values[0]) / 2 - node_values[1],
            )
            segment_count, cover_depth = fresh.fresh_distance_proof(
                quadratic, error
            )
            fresh_segments += segment_count
            fresh_maximum_cover_depth = max(
                fresh_maximum_cover_depth, cover_depth
            )
            replayed += 1

        if (cell_index + 1) % 1024 == 0 or cell_index + 1 == len(
            certificate["cells"]
        ):
            print(
                f"fresh replay checkpoint {cell_index + 1}/"
                f"{len(certificate['cells'])}: {replayed}/{total_leaves} leaves",
                flush=True,
            )

    assert replayed == total_leaves
    print(
        f"VERIFIED fresh 320-bit/depth-128 replay: {replayed} leaves, "
        f"{fresh_segments} polynomial segments, max cover depth "
        f"{fresh_maximum_cover_depth}",
        flush=True,
    )
    return fresh_segments, fresh_maximum_cover_depth


def verify(path: Path) -> None:
    raw = path.read_bytes()
    certificate = json.loads(raw)
    total_leaves, _ = validate_stored(certificate)
    replay_fresh(certificate, total_leaves)
    digest = hashlib.sha256(raw).hexdigest()
    print(f"certificate_sha256={digest}")
    print(
        "CONCLUSION: F(x) != 0 for every real x in [27/25,1024]; "
        "the exact-rational cover is gap-free and every accepted leaf passed "
        "the independent higher-precision replay."
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "certificate",
        nargs="?",
        type=Path,
        default=Path("evidence/research_taylor_cover_1024_certificate.json"),
    )
    args = parser.parse_args()
    verify(args.certificate)


if __name__ == "__main__":
    main()
