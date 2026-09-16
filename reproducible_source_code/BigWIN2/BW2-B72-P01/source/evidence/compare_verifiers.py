#!/usr/bin/env python3
"""Fail-closed comparison of the enumeration and bounded-SMT reports."""

from __future__ import annotations

from hashlib import sha256
import json
from math import comb
from pathlib import Path
import sys


SCRIPT_PATH = Path(__file__).resolve()
EVIDENCE_DIR = SCRIPT_PATH.parent
PROJECT_DIR = EVIDENCE_DIR.parent
ENUMERATION_PATH = EVIDENCE_DIR / "signature_join_61.json"
SMT_PATH = EVIDENCE_DIR / "z3_bv_verification_61.json"
OUTPUT_PATH = EVIDENCE_DIR / "independent_verifier_comparison.json"


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def match_key(match: dict[str, object]) -> tuple[tuple[int, ...], ...]:
    return (tuple(match["b"]), tuple(match["a"]), tuple(match["signature"]))


def orbit_key(match: dict[str, object]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    b = tuple(match["b"])
    a = tuple(match["a"])
    b_images = (b, (b[3], b[2], b[1], b[0]))
    a_images = (a, (a[0], a[2], a[1], a[3]))
    return min((bb, aa) for bb in b_images for aa in a_images)


def main() -> int:
    enumeration = load(ENUMERATION_PATH)
    smt = load(SMT_PATH)
    layers = enumeration["layers"]
    smt_query = smt["at_most_61_query"]
    expected_layers = list(range(4, 62))
    expected_total = comb(61, 4)

    enumeration_matches = sorted(match_key(match) for match in enumeration["matches"])
    smt_matches = sorted(match_key(match) for match in smt_query["models"])
    layer_numbers = [layer["s"] for layer in layers]
    layer_coverage_ok = all(
        layer["a"]["domain_count"] == comb(layer["s"] - 1, 3)
        and layer["b"]["domain_count"] == comb(layer["s"] - 1, 3)
        for layer in layers
    )
    no_enumeration_hit_below_61 = all(
        layer["match_count"] == 0 for layer in layers if layer["s"] < 61
    )
    orbit_keys = sorted({orbit_key(match) for match in enumeration["matches"]})

    checks = {
        "enumeration_status_complete": enumeration["status"] == "complete",
        "enumeration_has_no_anomalies": enumeration["anomalies"] == [],
        "enumeration_layers_are_exactly_4_through_61": layer_numbers == expected_layers,
        "enumeration_per_layer_domain_counts_are_compositions": layer_coverage_ok,
        "enumeration_aggregate_a_count": enumeration["aggregate"]["a_domain_count"] == expected_total,
        "enumeration_aggregate_b_count": enumeration["aggregate"]["b_domain_count"] == expected_total,
        "smt_status_complete": smt["status"] == "complete",
        "smt_domain_count_each_side": smt["domain"]["domain_count_each_side"] == expected_total,
        "same_source_sha256": enumeration["source_sha256"] == smt["source_sha256"],
        "enumeration_no_hit_below_61": no_enumeration_hit_below_61,
        "smt_sub_61_unsat": smt["sub_61_query"]["result"] == "unsat",
        "enumeration_first_matching_layer_61": enumeration["first_matching_layer"] == 61,
        "smt_first_matching_layer_61": smt_query["first_matching_layer"] == 61,
        "smt_terminal_result_unsat_after_blocking_models": smt_query["terminal_result"] == "unsat",
        "same_complete_ordered_match_set": enumeration_matches == smt_matches,
        "same_match_count": enumeration["aggregate"]["match_count"] == smt_query["model_count"],
        "one_orbit_under_only_allowed_involutions": len(orbit_keys) == 1,
    }
    passed = all(checks.values())
    report = {
        "schema": "p4-paw-independent-verifier-comparison-v1",
        "status": "pass" if passed else "fail",
        "inputs": {
            "enumeration_report": str(ENUMERATION_PATH.relative_to(PROJECT_DIR)),
            "enumeration_report_sha256": digest(ENUMERATION_PATH),
            "smt_report": str(SMT_PATH.relative_to(PROJECT_DIR)),
            "smt_report_sha256": digest(SMT_PATH),
        },
        "coverage": {
            "common_sum_range": [4, 61],
            "positive_ordered_quadruples_each_side": expected_total,
        },
        "checks": checks,
        "agreed_first_matching_layer": 61 if passed else None,
        "agreed_ordered_matches": [
            {"b": list(b), "a": list(a), "signature": list(signature)}
            for b, a, signature in enumeration_matches
        ] if passed else [],
        "allowed_orbit_count": len(orbit_keys) if passed else None,
        "allowed_orbit_representatives": [
            {"b": list(b), "a": list(a)} for b, a in orbit_keys
        ] if passed else [],
    }
    temporary = OUTPUT_PATH.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    temporary.replace(OUTPUT_PATH)
    return 0 if passed else 2


if __name__ == "__main__":
    sys.exit(main())
