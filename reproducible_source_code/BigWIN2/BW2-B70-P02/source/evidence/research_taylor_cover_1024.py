#!/usr/bin/env python3
"""Generate a rigorous adaptive Taylor cover of [27/25, 1024].

The analytic evaluator and leaf certificate are imported from
``research_taylor_stencils.py``.  Initial exact-rational cells have width
1/8, except for the shorter final cell.  A failed cell is bisected exactly
until its order-3 quadratic Taylor stencil succeeds.  Progress is checkpointed
after every 256 initial cells.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

import flint

import research_taylor_stencils as core


LEFT = Fraction(27, 25)
RIGHT = Fraction(1024)
INITIAL_WIDTH = Fraction(1, 8)
MAX_TAYLOR_DEPTH = 30
PROVENANCE_JOB = "win-00070-p02-research-5ae3369c8f92"
SCHEMA = "win-00070-p02-taylor-cover-1024-v1"


def rational_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def initial_cells() -> list[tuple[Fraction, Fraction]]:
    cells: list[tuple[Fraction, Fraction]] = []
    left = LEFT
    while left < RIGHT:
        right = min(left + INITIAL_WIDTH, RIGHT)
        cells.append((left, right))
        left = right
    assert cells[0][0] == LEFT and cells[-1][1] == RIGHT
    assert all(a < b and b - a <= INITIAL_WIDTH for a, b in cells)
    return cells


def certify_initial_cell(index: int, left: Fraction, right: Fraction) -> dict:
    stack = [(left, right, 0)]
    leaves: list[dict] = []
    attempted = 0
    while stack:
        leaf_left, leaf_right, depth = stack.pop()
        attempted += 1
        leaf = core.try_taylor_leaf(leaf_left, leaf_right, depth)
        if leaf is not None:
            leaves.append(leaf)
            continue
        if depth >= MAX_TAYLOR_DEPTH:
            raise RuntimeError(
                "Taylor certification failed at maximum depth on "
                f"[{rational_text(leaf_left)}, {rational_text(leaf_right)}]"
            )
        midpoint = (leaf_left + leaf_right) / 2
        stack.append((midpoint, leaf_right, depth + 1))
        stack.append((leaf_left, midpoint, depth + 1))

    assert leaves[0]["left"] == rational_text(left)
    assert leaves[-1]["right"] == rational_text(right)
    assert all(
        previous["right"] == following["left"]
        for previous, following in zip(leaves, leaves[1:])
    )
    return {
        "index": index,
        "left": rational_text(left),
        "right": rational_text(right),
        "attempted_taylor_nodes": attempted,
        "leaf_count": len(leaves),
        "maximum_taylor_bisect_depth": max(
            leaf["taylor_bisect_depth"] for leaf in leaves
        ),
        "leaves": leaves,
    }


def write_progress(path: Path, completed: int, total: int, cells: list[dict]) -> None:
    leaf_count = sum(cell["leaf_count"] for cell in cells)
    record = {
        "schema": "win-00070-p02-taylor-cover-1024-progress-v1",
        "provenance_job_id": PROVENANCE_JOB,
        "completed_initial_cells": completed,
        "total_initial_cells": total,
        "certified_through": cells[-1]["right"] if cells else rational_text(LEFT),
        "current_taylor_leaf_count": leaf_count,
        "maximum_taylor_bisect_depth": max(
            (cell["maximum_taylor_bisect_depth"] for cell in cells),
            default=0,
        ),
    }
    path.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")


def build_certificate(progress_path: Path) -> dict:
    partition = initial_cells()
    cells: list[dict] = []
    for index, (left, right) in enumerate(partition):
        cells.append(certify_initial_cell(index, left, right))
        completed = index + 1
        if completed % 256 == 0 or completed == len(partition):
            write_progress(progress_path, completed, len(partition), cells)
            print(
                f"checkpoint {completed}/{len(partition)} through "
                f"{cells[-1]['right']}: "
                f"{sum(cell['leaf_count'] for cell in cells)} leaves",
                flush=True,
            )

    depth_histogram = Counter(
        leaf["taylor_bisect_depth"]
        for cell in cells
        for leaf in cell["leaves"]
    )
    cover_depth_histogram = Counter(
        leaf["maximum_polynomial_cover_depth"]
        for cell in cells
        for leaf in cell["leaves"]
    )
    return {
        "schema": SCHEMA,
        "provenance_job_id": PROVENANCE_JOB,
        "claim_scope": "F(x) is nonzero for every real x in [27/25,1024]",
        "proof_reduction": (
            "each leaf certifies q(x)=F(x)/F(x/2) is defined and nonzero; "
            "hence F(x) is nonzero"
        ),
        "arithmetic": {
            "library": "python-flint",
            "library_version": flint.__version__,
            "precision_bits": core.PRECISION_BITS,
            "rounding": "Arb outward ball arithmetic",
            "recursion_depth": core.RECURSION_DEPTH,
            "terminal_value_bound": "|F(t)-1| <= (4*pi/3)*|t|",
            "terminal_derivative_bound": (
                "|F^(n)(t)| <= (4*pi/3)^n, n=1,2,3"
            ),
            "support_bound": "supp(mu) subset [0,2/3]",
            "interpolation_remainder": (
                "componentwise |q-P2| <= "
                "sup|component(q''')|*h^3/(9*sqrt(3))"
            ),
        },
        "domain_left": rational_text(LEFT),
        "domain_right": rational_text(RIGHT),
        "initial_width_upper_bound": rational_text(INITIAL_WIDTH),
        "initial_cell_count": len(cells),
        "total_taylor_leaf_count": sum(cell["leaf_count"] for cell in cells),
        "total_attempted_taylor_nodes": sum(
            cell["attempted_taylor_nodes"] for cell in cells
        ),
        "total_polynomial_cover_segment_count": sum(
            leaf["polynomial_cover_segment_count"]
            for cell in cells
            for leaf in cell["leaves"]
        ),
        "maximum_taylor_bisect_depth": max(
            cell["maximum_taylor_bisect_depth"] for cell in cells
        ),
        "maximum_polynomial_cover_depth": max(
            leaf["maximum_polynomial_cover_depth"]
            for cell in cells
            for leaf in cell["leaves"]
        ),
        "taylor_leaf_depth_histogram": {
            str(key): depth_histogram[key] for key in sorted(depth_histogram)
        },
        "leaf_maximum_polynomial_cover_depth_histogram": {
            str(key): cover_depth_histogram[key]
            for key in sorted(cover_depth_histogram)
        },
        "cells": cells,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("evidence/research_taylor_cover_1024_certificate.json"),
    )
    parser.add_argument(
        "--progress",
        type=Path,
        default=Path("evidence/research_taylor_cover_1024_progress.json"),
    )
    args = parser.parse_args()
    certificate = build_certificate(args.progress)
    args.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        f"wrote {args.output}: {certificate['total_taylor_leaf_count']} leaves, "
        f"max Taylor depth {certificate['maximum_taylor_bisect_depth']}, "
        f"{certificate['total_polynomial_cover_segment_count']} polynomial "
        "segments",
        flush=True,
    )


if __name__ == "__main__":
    main()
