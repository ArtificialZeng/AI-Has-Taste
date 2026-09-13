#!/usr/bin/env python3
"""Frozen independent referee for the x=5/8, Z=1/8 y-strip.

The underlying reconstruction lives in the literal-free scout.  It starts
from the original signed Hermitian frame and treats the candidate source,
source note, and source manifest as opaque hash-bound byte strings only.
This wrapper freezes only outputs independently derived by that scout.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import sympy as sp

from uncovered_ray_x5_8_ystrip_referee_literal_free_scout import (
    PREV_REFEREE,
    SOURCE,
    SOURCE_MANIFEST,
    reconstruct,
    require,
)


EXPECTED_COEFFICIENT_SHA = (
    "b0ceebda4f845cb5d4d988c2f2b6f4384d0143859a48c5b9779f1f73ac7b3855"
)
EXPECTED_CONTROL_SHA = (
    "2a57209ee9fe5745b0ae7bf366534808ec0862e83903036cff95229594bae226"
)
EXPECTED_CERTIFICATE_SHAPES = (
    (0, 0, 0, 1),
    (1, 0, 2, 3),
    (1, 1, 4, 10),
    (1, 2, 6, 21),
    (1, 3, 8, 36),
)
EXPECTED_DIAGNOSTIC_MINIMUM = sp.Rational(
    6480000000904470954193509231569982095853980231,
    1296000000000000000000000000000000000000000000,
)
EXPECTED_DIAGNOSTIC_DATA = (
    sp.Rational(1, 1000000), sp.Rational(1, 100), sp.Rational(1, 1000)
)


def formal_referee(*, source_path: Path = SOURCE,
                   manifest_path: Path = SOURCE_MANIFEST,
                   dependency_path: Path = PREV_REFEREE,
                   attack: str = "none") -> None:
    result = reconstruct(
        source_path=source_path,
        manifest_path=manifest_path,
        dependency_path=dependency_path,
        attack=attack,
    )
    require(result["lambda_degree"] == 4, "frozen lambda degree four")
    require(len(result["coefficients"]) == 5, "frozen five coefficients")
    require(result["coefficient_sha"] == EXPECTED_COEFFICIENT_SHA,
            "frozen independently derived coefficient tuple")
    require(result["control_sha"] == EXPECTED_CONTROL_SHA,
            "frozen independently derived complete control table")
    certificate_shapes = tuple(
        (certificate["order"], certificate["degree_s"],
         certificate["degree_u"], len(certificate["bernstein"]))
        for certificate in result["certificates"]
    )
    require(certificate_shapes == EXPECTED_CERTIFICATE_SHAPES,
            "frozen certificate shapes 1/3/10/21/36")
    require(result["control_count"] == 71, "frozen 71 exact controls")
    require(result["danger_reserve"] == sp.Rational(19371, 40000),
            "frozen strict danger reserve")
    require(result["det_ratio"] == sp.Rational(5, 72),
            "frozen det(C)/S")
    require(result["diagnostic_count"] == 27,
            "frozen 27 exact diagnostic nodes")
    require(result["diagnostic_minimum"] == EXPECTED_DIAGNOSTIC_MINIMUM,
            "frozen exact diagnostic minimum")
    require(result["diagnostic_data"] == EXPECTED_DIAGNOSTIC_DATA,
            "frozen exact diagnostic minimizer")
    print("PASS frozen coefficient/control hashes and certificate shapes")
    print("PASS 71/71 strict exact controls (1+3+10+21+36)")
    print("PASS theorem scope: x=5/8, Z=1/8, |y|<=1/100, "
          "0<S<=1, lambda>0, both signed-z lifts")
    print("PASS 27 nodes retained as diagnostics only")
    print("FATAL 0 MAJOR 0 MINOR 0")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-path", type=Path, default=SOURCE)
    parser.add_argument("--manifest-path", type=Path, default=SOURCE_MANIFEST)
    parser.add_argument("--dependency-path", type=Path, default=PREV_REFEREE)
    parser.add_argument("--attack", choices=(
        "none", "drop-q2", "flip-danger", "corrupt-coefficient", "drop-control"
    ), default="none")
    args = parser.parse_args()
    formal_referee(
        source_path=args.source_path,
        manifest_path=args.manifest_path,
        dependency_path=args.dependency_path,
        attack=args.attack,
    )
    print("INDEPENDENT_REFEREE PASS")


if __name__ == "__main__":
    main()
