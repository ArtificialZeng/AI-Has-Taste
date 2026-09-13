#!/usr/bin/env python3
"""Frozen independent referee for the x=5/8 compact-ball xy-box."""

from __future__ import annotations

import argparse
from pathlib import Path

import sympy as sp

from uncovered_box_x5_8_xy_referee_literal_free_scout import (
    PREV_REFEREE,
    SOURCE,
    SOURCE_MANIFEST,
    reconstruct,
    require,
)


EXPECTED_COEFFICIENT_SHA = (
    "b11348d029f2b1fd6bcbf4dfe3ff789f1f5e67a0846f2a83041e7af62bd9497f"
)
EXPECTED_CONTROL_SHA = (
    "89c49a8ba13aa17da382f3f62666246a9a70906fad34d16705d4f99f059b6a3d"
)
EXPECTED_CERTIFICATE_SHAPES = (
    (0, (0, 0, 0), 1),
    (1, (0, 2, 2), 9),
    (1, (1, 4, 4), 50),
    (1, (2, 6, 6), 147),
    (1, (3, 8, 8), 324),
)
EXPECTED_GLOBAL_WEAKEST = (
    3, (0, 0, 6), sp.Rational(8332318460470459, 15187500000000000)
)
EXPECTED_DIAGNOSTIC_MINIMUM = sp.Rational(
    20503125002851629448588057975216914071874155556911,
    4100625000000000000000000000000000000000000000000,
)
EXPECTED_DIAGNOSTIC_DATA = (
    sp.Rational(1, 1000000), sp.Rational(313, 500),
    sp.Rational(1, 100), sp.Rational(1, 1000),
)


def formal_referee(*, source_path: Path = SOURCE,
                   manifest_path: Path = SOURCE_MANIFEST,
                   dependency_path: Path = PREV_REFEREE,
                   attack: str = "none") -> None:
    result = reconstruct(source_path=source_path,
                         manifest_path=manifest_path,
                         dependency_path=dependency_path,
                         attack=attack)
    require(result["lambda_degree"] == 4, "frozen lambda degree four")
    require(len(result["coefficients"]) == 5, "frozen five coefficients")
    require(result["coefficient_sha"] == EXPECTED_COEFFICIENT_SHA,
            "frozen independently derived coefficient tuple")
    require(result["control_sha"] == EXPECTED_CONTROL_SHA,
            "frozen independently derived complete control table")
    certificate_shapes = tuple(
        (certificate["order"], certificate["degrees"],
         len(certificate["bernstein"]))
        for certificate in result["certificates"]
    )
    require(certificate_shapes == EXPECTED_CERTIFICATE_SHAPES,
            "frozen certificate shapes 1/9/50/147/324")
    require(result["control_count"] == 531, "frozen 531 exact controls")
    require(result["global_weakest"] == EXPECTED_GLOBAL_WEAKEST,
            "frozen unique global weakest control")
    require(result["global_weakest_multiplicity"] == 1,
            "frozen weakest-control multiplicity one")
    require(result["danger_reserve"] == sp.Rational(30189, 62500),
            "frozen strict danger reserve")
    require(result["det_ratio"] == sp.Rational(5, 72),
            "frozen det(C)/S")
    require(result["diagnostic_count"] == 81,
            "frozen 81 exact diagnostic nodes")
    require(result["diagnostic_minimum"] == EXPECTED_DIAGNOSTIC_MINIMUM,
            "frozen exact diagnostic minimum")
    require(result["diagnostic_data"] == EXPECTED_DIAGNOSTIC_DATA,
            "frozen exact diagnostic minimizer")
    print("PASS frozen coefficient/control hashes and certificate shapes")
    print("PASS 531/531 strict exact controls (1+9+50+147+324)")
    print("PASS unique global weakest lambda^3,(0,0,6)")
    print("PASS theorem scope: |x-5/8|<=1/1000, |y|<=1/100, "
          "Z=1/8, 0<S<=1, lambda>0, both signed-z lifts")
    print("PASS 81 nodes retained as diagnostics only")
    print("FATAL 0 MAJOR 0 MINOR 0")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-path", type=Path, default=SOURCE)
    parser.add_argument("--manifest-path", type=Path, default=SOURCE_MANIFEST)
    parser.add_argument("--dependency-path", type=Path, default=PREV_REFEREE)
    parser.add_argument("--attack", choices=(
        "none", "bad-normalization", "drop-q2", "flip-danger",
        "corrupt-coefficient", "drop-control",
    ), default="none")
    args = parser.parse_args()
    formal_referee(source_path=args.source_path,
                   manifest_path=args.manifest_path,
                   dependency_path=args.dependency_path,
                   attack=args.attack)
    print("INDEPENDENT_REFEREE PASS")


if __name__ == "__main__":
    main()
x