#!/usr/bin/env python3
"""Generate a rigorous Arb certificate for the two hardest source grid cells.

The certified cells have radius 1/16 about the two smallest-|q| abscissae
printed in Mao--Wu, Table 1.  Every endpoint is stored as an exact rational.
For each leaf X, this script uses the functional equation

    F(x) = p F(x/2) + p^2 exp(-pi*i*x) F(x/4)

with directed Arb balls.  At recursion depth D the terminal boxes use the
proved support estimate

    |F(t)-1| <= (4*pi/3) |t|.

It first proves 0 is not in F(X/2), then forms q(X)=F(X)/F(X/2), and accepts
the leaf only when either Re q(X) or Im q(X) excludes zero.  Consequently
F(x) is nonzero for every real x in every accepted leaf.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path

import flint
from flint import acb, arb, ctx, fmpq


PRECISION_BITS = 256
RECURSION_DEPTH = 120
MAX_BISECTION_DEPTH = 60
CENTERS = ("6580077.19160276", "5065070.60771886")
CELL_RADIUS = Fraction(1, 16)

ctx.prec = PRECISION_BITS
P = (arb(5).sqrt() - 1) / 2
P2 = P * P
PI = arb.pi()
LIPSCHITZ = 4 * PI / 3
TWO = arb(2)


def as_fmpq(value: Fraction) -> fmpq:
    return fmpq(value.numerator, value.denominator)


def rational_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def interval_ball(left: Fraction, right: Fraction) -> arb:
    """Return an Arb ball containing the exact rational interval [left,right]."""
    assert left < right
    midpoint = (left + right) / 2
    radius = (right - left) / 2
    # Arb stores the second argument as an outward-rounded magnitude, so this
    # contains both exact rational endpoints (usually with tiny extra padding).
    return arb(as_fmpq(midpoint), as_fmpq(radius))


def serialized_ball(value: arb) -> str:
    """Emit a decimal Arb enclosure that is safe to parse back."""
    result = value.str(90, radius=True, more=True)
    parsed = arb(result)
    assert parsed.contains(value)
    return result


def enclose_f_pair(x: arb) -> tuple[acb, acb]:
    """Enclose F(X) and F(X/2) by downward terminal bounds and upward recursion."""
    terminal_radius = LIPSCHITZ * abs(x) / (TWO**RECURSION_DEPTH)
    f_next = acb(
        arb(1, terminal_radius),
        arb(0, terminal_radius),
    )
    f_next2 = acb(
        arb(1, terminal_radius / 2),
        arb(0, terminal_radius / 2),
    )

    for k in range(RECURSION_DEPTH - 1, -1, -1):
        scaled_x = x / (TWO**k)
        phase = acb(0, -PI * scaled_x).exp()
        f_here = P * f_next + P2 * phase * f_next2
        f_next2, f_next = f_next, f_here

    return f_next, f_next2


def try_leaf(left: Fraction, right: Fraction, depth: int) -> dict | None:
    x = interval_ball(left, right)
    f_x, f_half = enclose_f_pair(x)
    if f_half.contains(0):
        return None

    q_x = f_x / f_half
    denominator_re = serialized_ball(f_half.real)
    denominator_im = serialized_ball(f_half.imag)
    q_re = serialized_ball(q_x.real)
    q_im = serialized_ball(q_x.imag)

    stored_denominator = acb(arb(denominator_re), arb(denominator_im))
    stored_q_re = arb(q_re)
    stored_q_im = arb(q_im)
    if stored_denominator.contains(0):
        return None

    re_ok = not stored_q_re.contains(0)
    im_ok = not stored_q_im.contains(0)
    if not (re_ok or im_ok):
        return None
    witness = "re" if re_ok else "im"

    return {
        "left": rational_text(left),
        "right": rational_text(right),
        "bisect_depth": depth,
        "denominator_re": denominator_re,
        "denominator_im": denominator_im,
        "q_re": q_re,
        "q_im": q_im,
        "witness_component": witness,
    }


def certify_cell(center_text: str) -> dict:
    center = Fraction(center_text)
    cell_left = center - CELL_RADIUS
    cell_right = center + CELL_RADIUS
    stack = [(cell_left, cell_right, 0)]
    leaves: list[dict] = []
    attempted_nodes = 0

    while stack:
        left, right, depth = stack.pop()
        attempted_nodes += 1
        leaf = try_leaf(left, right, depth)
        if leaf is not None:
            leaves.append(leaf)
            continue
        if depth >= MAX_BISECTION_DEPTH:
            raise RuntimeError(
                f"uncertified interval at depth {depth}: "
                f"[{rational_text(left)}, {rational_text(right)}]"
            )
        midpoint = (left + right) / 2
        # Push right first so the output is monotonically left-to-right.
        stack.append((midpoint, right, depth + 1))
        stack.append((left, midpoint, depth + 1))

    assert leaves
    assert leaves[0]["left"] == rational_text(cell_left)
    assert leaves[-1]["right"] == rational_text(cell_right)
    for previous, following in zip(leaves, leaves[1:]):
        assert previous["right"] == following["left"]

    return {
        "center_printed_decimal": center_text,
        "left": rational_text(cell_left),
        "right": rational_text(cell_right),
        "leaf_count": len(leaves),
        "attempted_nodes": attempted_nodes,
        "maximum_leaf_bisect_depth": max(x["bisect_depth"] for x in leaves),
        "leaves": leaves,
    }


def build_certificate() -> dict:
    cells = [certify_cell(center) for center in CENTERS]
    return {
        "schema": "win-00070-p02-valley-cells-v1",
        "provenance_job_id": "win-00070-p02-research-857391805db7",
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
            "terminal_bound": "|F(t)-1| <= (4*pi/3)*|t|",
            "support_bound": "supp(mu) subset [0,2/3]",
            "parameter": "p=(sqrt(5)-1)/2 and 1-p=p^2",
        },
        "cell_radius": rational_text(CELL_RADIUS),
        "total_leaf_count": sum(cell["leaf_count"] for cell in cells),
        "cells": cells,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("evidence/research_valley_cells_certificate.json"),
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
            f"{cell['leaf_count']} leaves, max depth "
            f"{cell['maximum_leaf_bisect_depth']}"
        )
    print(f"wrote {args.output} ({certificate['total_leaf_count']} total leaves)")


if __name__ == "__main__":
    main()
