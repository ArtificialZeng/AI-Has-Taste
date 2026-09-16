#!/usr/bin/env python3
"""Independent coverage and Arb replay for research_valley_cells_certificate.json.

Unlike the generator, this verifier evaluates F(X) and F(X/2) in two separate
functional-equation recursions.  It also reconstructs every exact rational
leaf, checks that the leaves form gap-free closed covers of the stated cells,
and checks both the serialized witnesses and freshly computed witnesses.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

import flint
from flint import acb, arb, ctx, fmpq


EXPECTED_SCHEMA = "win-00070-p02-valley-cells-v1"
EXPECTED_JOB = "win-00070-p02-research-857391805db7"
EXPECTED_CENTERS = ("6580077.19160276", "5065070.60771886")
EXPECTED_RADIUS = Fraction(1, 16)
EXPECTED_PRECISION = 256
EXPECTED_RECURSION_DEPTH = 120


def parse_rational(text: str) -> Fraction:
    if "/" in text:
        numerator, denominator = text.split("/", 1)
        return Fraction(int(numerator), int(denominator))
    return Fraction(int(text), 1)


def as_fmpq(value: Fraction) -> fmpq:
    return fmpq(value.numerator, value.denominator)


def interval_ball(left: Fraction, right: Fraction) -> arb:
    midpoint = (left + right) / 2
    radius = (right - left) / 2
    return arb(as_fmpq(midpoint), as_fmpq(radius))


def verifier_fourier_enclosure(argument: arb) -> acb:
    """Enclose F(argument), independently returning only one recursion output."""
    p = (arb(5).sqrt() - 1) / 2
    pi = arb.pi()
    two = arb(2)
    tail_lipschitz = 4 * pi / 3
    tail_radius = (
        tail_lipschitz * abs(argument) / (two**EXPECTED_RECURSION_DEPTH)
    )
    higher = acb(arb(1, tail_radius), arb(0, tail_radius))
    still_higher = acb(arb(1, tail_radius / 2), arb(0, tail_radius / 2))

    exponent_scale = two ** (EXPECTED_RECURSION_DEPTH - 1)
    for _ in range(EXPECTED_RECURSION_DEPTH):
        phase = acb(0, -pi * argument / exponent_scale).exp()
        current = p * higher + p * p * phase * still_higher
        still_higher, higher = higher, current
        exponent_scale /= 2
    return higher


def verify(certificate_path: Path) -> None:
    raw = certificate_path.read_bytes()
    certificate = json.loads(raw)
    assert certificate["schema"] == EXPECTED_SCHEMA
    assert certificate["provenance_job_id"] == EXPECTED_JOB
    assert parse_rational(certificate["cell_radius"]) == EXPECTED_RADIUS
    arithmetic = certificate["arithmetic"]
    assert arithmetic["precision_bits"] == EXPECTED_PRECISION
    assert arithmetic["recursion_depth"] == EXPECTED_RECURSION_DEPTH
    assert arithmetic["library"] == "python-flint"
    assert arithmetic["library_version"] == flint.__version__

    ctx.prec = EXPECTED_PRECISION
    cells = certificate["cells"]
    assert len(cells) == len(EXPECTED_CENTERS)
    total_leaves = 0
    stored_re_witnesses = 0
    stored_im_witnesses = 0
    replay_re_witnesses = 0
    replay_im_witnesses = 0

    for cell, center_text in zip(cells, EXPECTED_CENTERS):
        assert cell["center_printed_decimal"] == center_text
        center = Fraction(center_text)
        cell_left = center - EXPECTED_RADIUS
        cell_right = center + EXPECTED_RADIUS
        assert parse_rational(cell["left"]) == cell_left
        assert parse_rational(cell["right"]) == cell_right

        leaves = cell["leaves"]
        assert cell["leaf_count"] == len(leaves)
        assert leaves
        next_left = cell_left
        maximum_depth = 0

        for leaf in leaves:
            left = parse_rational(leaf["left"])
            right = parse_rational(leaf["right"])
            depth = int(leaf["bisect_depth"])
            assert left == next_left
            assert left < right <= cell_right
            assert right - left == (cell_right - cell_left) / (2**depth)
            alignment = (left - cell_left) / (right - left)
            assert alignment.denominator == 1
            maximum_depth = max(maximum_depth, depth)

            stored_denominator = acb(
                arb(leaf["denominator_re"]), arb(leaf["denominator_im"])
            )
            assert not stored_denominator.contains(0)
            stored_q_re = arb(leaf["q_re"])
            stored_q_im = arb(leaf["q_im"])
            if leaf["witness_component"] == "re":
                assert not stored_q_re.contains(0)
                stored_re_witnesses += 1
            elif leaf["witness_component"] == "im":
                assert not stored_q_im.contains(0)
                stored_im_witnesses += 1
            else:
                raise AssertionError("unknown serialized witness component")

            x = interval_ball(left, right)
            numerator = verifier_fourier_enclosure(x)
            denominator = verifier_fourier_enclosure(x / 2)
            assert not denominator.contains(0)
            quotient = numerator / denominator
            if not quotient.real.contains(0):
                replay_re_witnesses += 1
            elif not quotient.imag.contains(0):
                replay_im_witnesses += 1
            else:
                raise AssertionError(
                    f"fresh replay did not separate q on [{left}, {right}]"
                )

            next_left = right

        assert next_left == cell_right
        assert maximum_depth == cell["maximum_leaf_bisect_depth"]
        total_leaves += len(leaves)
        print(
            f"VERIFIED cell [{cell['left']}, {cell['right']}]: "
            f"{len(leaves)} exact rational leaves, max depth {maximum_depth}"
        )

    assert total_leaves == certificate["total_leaf_count"]
    print(f"VERIFIED gap-free union: {total_leaves} leaves in {len(cells)} cells")
    print(
        "VERIFIED serialized witnesses: "
        f"Re={stored_re_witnesses}, Im={stored_im_witnesses}"
    )
    print(
        "VERIFIED fresh separate-recursion witnesses: "
        f"Re={replay_re_witnesses}, Im={replay_im_witnesses}"
    )
    print(f"certificate_sha256={hashlib.sha256(raw).hexdigest()}")
    print(
        "CONCLUSION: F(x) != 0 throughout both closed radius-1/16 cells "
        "(conditional only on the stated functional equation and proved "
        "support/tail bound)."
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "certificate",
        nargs="?",
        type=Path,
        default=Path("evidence/research_valley_cells_certificate.json"),
    )
    args = parser.parse_args()
    verify(args.certificate)


if __name__ == "__main__":
    main()
