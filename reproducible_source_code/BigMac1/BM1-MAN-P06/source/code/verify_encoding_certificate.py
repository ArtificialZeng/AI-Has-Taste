#!/usr/bin/env python3
"""Recompute the serialized formula counts without trusting stored totals."""

from __future__ import annotations

import json
import math
from pathlib import Path

from compact_sat import counts


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    certificate = json.loads((ROOT / "certificates/encoding_counts.json").read_text())
    assert certificate["global_claim_solved"] is False
    assert certificate["terminal_status"] == "partial theorem"

    current = counts(33, 7, ax5_mode="signotope")
    expected = certificate["compressed_formula"]
    assert current["variables"] == expected["variables"]
    assert current["clauses"] == expected["clauses"]
    assert current["literal_occurrences"] == expected["literal_occurrences"]
    assert current["triple_variables"] == expected["triple_variables"]
    assert current["four_set_indicators"] == expected["four_set_indicators"]
    assert current["consistency_clauses"] == expected["signotope_clauses"]
    assert current["parity_clauses"] == expected["parity_guard_clauses"]
    assert current["exclusion_clauses"] == expected["seven_set_clauses"]
    assert math.comb(7, 4) == expected["seven_set_clause_width"]

    direct = counts(33, 7, ax5_mode="signotope-direct")
    direct_expected = certificate["direct_forbidden_pattern_variant"]
    assert direct["variables"] == direct_expected["variables"]
    assert direct["clauses"] == direct_expected["clauses"]
    assert direct["literal_occurrences"] == direct_expected["literal_occurrences"]
    assert direct["consistency_clauses"] == direct_expected["signotope_clauses"]
    assert direct["parity_clauses"] == direct_expected["parity_guard_clauses"]
    assert direct["exclusion_clauses"] == direct_expected["seven_set_clauses"]

    anchored = counts(33, 7, ax5_mode="reduced")
    anchored_expected = certificate["anchor_compatible_parity_formula"]
    assert anchored["variables"] == anchored_expected["variables"]
    assert anchored["clauses"] == anchored_expected["clauses"]
    assert anchored["literal_occurrences"] == anchored_expected["literal_occurrences"]
    assert anchored["consistency_clauses"] == anchored_expected["reduced_ax5_clauses"]
    assert anchored["parity_clauses"] == anchored_expected["parity_guard_clauses"]
    assert anchored["exclusion_clauses"] == anchored_expected["seven_set_clauses"]

    baseline = certificate["audited_2025_baseline"]
    assert baseline["variables"] == math.comb(33, 3) + 14 * math.comb(33, 4)
    assert baseline["clauses"] == (
        math.prod(range(29, 34)) // 3
        + 71 * math.comb(33, 4)
        + math.comb(33, 7)
    )
    assert baseline["literal_occurrences"] == (
        6 * (math.prod(range(29, 34)) // 3)
        + 196 * math.comb(33, 4)
        + 280 * math.comb(33, 7)
    )

    public = certificate["subercaseaux_public_fixed_order"]
    quadruples = math.comb(33, 4)
    seven_sets = math.comb(33, 7)
    assert public["variables"] == math.comb(33, 3) + quadruples
    assert public["signotope_clauses"] == 4 * quadruples
    assert public["full_reification_clauses"] == 16 * quadruples
    assert public["seven_set_clauses"] == seven_sets
    assert public["full_reification_clause_width"] == 5
    assert public["clauses"] == 20 * quadruples + seven_sets
    assert public["literal_occurrences"] == (
        3 * 4 * quadruples + 5 * 16 * quadruples + 35 * seven_sets
    )

    reductions = certificate["reduction_vs_subercaseaux_public_fixed_order_percent"]
    for field in ("variables", "clauses", "literal_occurrences"):
        expected_reduction = 100 * (public[field] - expected[field]) / public[field]
        assert reductions[field] == f"{expected_reduction:.4f}"
    factored_full = certificate["factored_full_reification_fixed_order"]
    generated_factored_full = counts(
        33, 7, ax5_mode="signotope", parity_mode="equivalence-factored"
    )
    for field in (
        "variables",
        "clauses",
        "literal_occurrences",
        "consistency_clauses",
        "parity_clauses",
        "exclusion_clauses",
    ):
        certificate_field = {
            "consistency_clauses": "signotope_clauses",
            "parity_clauses": "full_reification_clauses",
            "exclusion_clauses": "seven_set_clauses",
        }.get(field, field)
        assert generated_factored_full[field] == factored_full[certificate_field]
    factored_reductions = certificate["reduction_vs_factored_full_reification_percent"]
    for field in ("variables", "clauses", "literal_occurrences"):
        expected_reduction = 100 * (factored_full[field] - expected[field]) / factored_full[field]
        assert factored_reductions[field] == f"{expected_reduction:.4f}"
    print("verified_serialized_33_point_encoding_counts")
    print("verified_subercaseaux_public_fixed_order_certificate")
    print("verified_factored_full_reification_control")
    print("verified_global_claim_remains_unresolved")


if __name__ == "__main__":
    main()
