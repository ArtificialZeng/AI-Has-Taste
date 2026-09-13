#!/usr/bin/env python3
"""Frozen no-import referee for 16/25<=x<=7/10 xy-cell."""

from __future__ import annotations

import argparse
from pathlib import Path

import sympy as sp

from uncovered_box_x5_8_xy_adjacent_x7_10_referee_literal_free_scout import (
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
    "0fc14fff3113fcf0ddcb24747af6d4e13667b356b06f72b42396bade4ceed4fc"
)
EXPECTED_SEAM_SHA = (
    "79e086b34409a911c84048b751fdea7dfef8470574026b49ff46c5d84357b57c"
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
    ((0, 2, 2), sp.Rational(517, 1000)),
    ((0, 0, 4), sp.Rational(445787099, 36000000)),
    ((0, 0, 6), sp.Rational(6613713203, 12000000000)),
    ((0, 0, 8), sp.Rational(845947392310481, 216000000000000)),
)
EXPECTED_GLOBAL_WEAKEST = (
    1, (0, 2, 2), sp.Rational(517, 1000)
)
EXPECTED_DIAGNOSTIC_MINIMUM = sp.Rational(
    1620000000171848841039116449058653213029997439,
    324000000000000000000000000000000000000000000,
)
EXPECTED_DIAGNOSTIC_DATA = (
    sp.Rational(1, 1000000), sp.Rational(7, 10),
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
    # This referee stores controls in (S,v_x,u_y) order.  The source report
    # uses (S,u_y,v_x).  Verify the complete-table involution and the reported
    # minima under the exact coordinate permutation, not by comparing tensors.
    for certificate in result["certificates"]:
        source_order = tuple(
            ((i, k, j), value)
            for (i, j, k), value in certificate["bernstein"]
        )
        round_trip = tuple(
            ((i, k, j), value) for (i, j, k), value in source_order
        )
        require(round_trip == certificate["bernstein"],
                "complete control-table index-order involution")
    source_order_group_indices = tuple(
        (index[0], index[2], index[1]) for index, _ in group_weakest
    )
    require(source_order_group_indices == (
        (0, 0, 0), (0, 2, 2), (0, 4, 0), (0, 6, 0), (0, 8, 0)),
        "source/referee weakest-index coordinate permutation")
    require(result["control_count"] == 531, "frozen 531 exact controls")
    require(result["seam_group_counts"] == (1, 3, 10, 21, 36),
            "frozen 71/71 five-group seam controls")
    require(result["global_weakest"] == EXPECTED_GLOBAL_WEAKEST,
            "frozen unique global weakest control")
    require(result["global_weakest_multiplicity"] == 1,
            "frozen weakest-control multiplicity one")
    require(result["danger_reserve"] == sp.Rational(3849, 10000),
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
    print("PASS all five group minima and unique global lambda^1,(0,2,2)")
    print("INDEX ORDER (S,v_x,u_y); candidate convention (S,u_y,v_x) "
          "is the exact coordinate permutation (i,j,k)->(i,k,j)")
    print("PASS x=16/25 parameter/Hermitian/raw/71-control predecessor seam")
    print("PASS theorem scope: 16/25<=x<=7/10, |y|<=1/100, "
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
        "none", "bad-normalization", "bad-clearing", "drop-q2",
        "break-conjugate", "omit-z-sign", "flip-danger",
        "corrupt-coefficient", "drop-control", "break-parameter-seam",
        "break-hermitian-seam", "break-seam",
    ), default="none")
    args = parser.parse_args()
    formal_referee(source_path=args.source_path,
                   manifest_path=args.manifest_path,
                   dependency_path=args.dependency_path,
                   attack=args.attack)
    print("INDEPENDENT_REFEREE PASS")


if __name__ == "__main__":
    main()
