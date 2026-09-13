#!/usr/bin/env python3
"""Compare every record from the two independent exact enumerators."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 16), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("lp_json", type=Path)
    parser.add_argument("facet_json", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--source", type=Path, default=Path("source.md"))
    parser.add_argument("--problem", type=Path, default=Path("problem.md"))
    args = parser.parse_args()

    lp = json.loads(args.lp_json.read_text(encoding="utf-8"))
    facet = json.loads(args.facet_json.read_text(encoding="utf-8"))
    assert lp["records"] == facet["records"]
    assert lp["labeled_ideal_count"] == facet["labeled_ideal_count"] == 517
    assert lp["three_generator_count"] == facet["three_generator_count"] == 64
    assert lp["four_generator_count"] == facet["four_generator_count"] == 453
    assert lp["violating_count"] == facet["violating_count"] == 0
    assert (
        lp["v_closure_minus_v_I_distribution"]
        == facet["v_closure_minus_v_I_distribution"]
    )
    assert lp["degree_five_positive_control"] == facet["degree_five_positive_control"]
    assert (
        lp["degree_five_positive_control"]["v_I"],
        lp["degree_five_positive_control"]["v_closure"],
    ) == (2, 3)

    canonical_records = json.dumps(
        lp["records"], ensure_ascii=False, separators=(",", ":"), sort_keys=True
    ).encode("utf-8")
    payload = {
        "result": "exact agreement",
        "first_method": lp["method"],
        "second_method": facet["method"],
        "labeled_ideal_count": 517,
        "three_generator_count": 64,
        "four_generator_count": 453,
        "expanded_grid_point_count_per_method": lp["expanded_grid_point_count"],
        "standard_box_point_count_per_method": lp["standard_box_point_count"],
        "membership_decisions_per_method": 2 * lp["expanded_grid_point_count"],
        "cross_method_membership_bit_equalities": 2
        * lp["expanded_grid_point_count"],
        "serialized_membership_bits_across_both_methods": 4
        * lp["expanded_grid_point_count"],
        "v_closure_minus_v_I_distribution": lp[
            "v_closure_minus_v_I_distribution"
        ],
        "violating_count": 0,
        "degree_five_positive_control": {
            "generators": lp["degree_five_positive_control"]["generators"],
            "v_I": 2,
            "v_closure": 3,
        },
        "canonical_records_sha256": hashlib.sha256(canonical_records).hexdigest(),
        "lp_output_sha256": file_sha256(args.lp_json),
        "facet_output_sha256": file_sha256(args.facet_json),
        "source_sha256": file_sha256(args.source),
        "problem_sha256": file_sha256(args.problem),
    }
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(payload, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
