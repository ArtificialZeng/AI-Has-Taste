#!/usr/bin/env python3
"""Frozen no-import referee for 313/500<=x<=627/1000 xy-cell."""

from __future__ import annotations

import argparse
from pathlib import Path

import sympy as sp

from uncovered_box_x5_8_xy_adjacent_x627_1000_referee_literal_free_scout import (
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
    "f5b16ceedf15a37870ab0373f6bfba67fd47acccaa1b0c10f2258e070305f4ea"
)
EXPECTED_SEAM_SHA = (
    "47f305c5c5e756916f4cf61f6e5552e6a629b763baa6fd92842fd67fd8d4ec2b"
)
EXPECTED_CERTIFICATE_SHAPES = (
    (0, (0, 0, 0), 1),
    (1, (0, 2, 2), 9),
    (1, (1, 4, 4), 50),
    (1, (2, 6, 6), 147),
    (1, (3, 8, 8), 324),
)
EXPECTED_GROUP_WEAKEST = (
    ((0, 0, 0), sp.Rational(5)),
    ((0, 2, 2), sp.Rational(204229, 300000)),
    ((0, 0, 4), sp.Rational(153893289799, 12656250000)),
    ((0, 0, 6), sp.Rational(130268743001281, 237304687500000)),
    ((0, 0, 8), sp.Rational(
        99445552715982526441, 26696777343750000000)),
)
EXPECTED_GLOBAL_WEAKEST = (
    3, (0, 0, 6), sp.Rational(130268743001281, 237304687500000)
)
EXPECTED_DIAGNOSTIC_MINIMUM = sp.Rational(
    328050000045463739293969815616575420309937417703711,
    65610000000000000000000000000000000000000000000000,
)
EXPECTED_DIAGNOSTIC_DATA = (
    sp.Rational(1, 1000000), sp.Rational(627, 1000),
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
    require(result["seam_sha"] == EXPECTED_SEAM_SHA,
            "frozen independently derived predecessor seam")
    certificate_shapes = tuple(
        (certificate["order"], certificate["degrees"],
         len(certificate["bernstein"]))
        for certificate in result["certificates"]
    )
    require(certificate_shapes == EXPECTED_CERTIFICATE_SHAPES,
            "frozen certificate shapes 1/9/50/147/324")
    group_weakest = tuple(
        (certificate["weakest_index"], certificate["weakest_value"])
        for certificate in result["certificates"]
    )
    require(group_weakest == EXPECTED_GROUP_WEAKEST,
            "all five exact group minima")
    require(result["control_count"] == 531, "frozen 531 exact controls")
    require(result["seam_group_counts"] == (1, 3, 10, 21, 36),
            "frozen 71/71 five-group seam controls")
    require(result["global_weakest"] == EXPECTED_GLOBAL_WEAKEST,
            "frozen unique global weakest control")
    require(result["global_weakest_multiplicity"] == 1,
            "frozen weakest-control multiplicity one")
    require(result["danger_reserve"] == sp.Rational(481771, 1000000),
            "frozen strict danger reserve")
    require(result["det_ratio"] == sp.Rational(5, 72),
            "frozen det(C)/S")
    require(result["diagnostic_count"] == 81,
            "frozen 81 exact diagnostic nodes")
    require(result["diagnostic_minimum"] == EXPECTED_DIAGNOSTIC_MINIMUM,
            "frozen exact diagnostic minimum")
    require(result["diagnostic_data"] == EXPECTED_DIAGNOSTIC_DATA,
            "frozen exact diagnostic minimizer")
    print("PASS frozen coefficient/control/seam hashes")
    print("PASS 531/531 strict controls in groups 1/9/50/147/324")
    print("PASS all five group minima and unique global lambda^3,(0,0,6)")
    print("PASS x=313/500 parameter/raw-gate/71-control predecessor seam")
    print("PASS theorem scope: 313/500<=x<=627/1000, |y|<=1/100, "
          "Z=1/8, 0<S<=1, lambda>0, both signed-z lifts")
    print("PASS 81 nodes retained as falsification diagnostics only")
    print("FATAL 0 MAJOR 0 MINOR 0")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-path", type=Path, default=SOURCE)
    parser.add_argument("--manifest-path", type=Path,
                        default=SOURCE_MANIFEST)
    parser.add_argument("--dependency-path", type=Path,
                        default=PREV_REFEREE)
    parser.add_argument("--attack", choices=(
        "none", "bad-normalization", "drop-q2", "flip-danger",
        "corrupt-coefficient", "drop-control", "break-seam",
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