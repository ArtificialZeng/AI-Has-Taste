#!/usr/bin/env python3
"""Focused exact tests for survivor-obstruction analysis."""

from __future__ import annotations

import unittest

from analyze_survivor_obstructions import (
    PROJECT_ROOT,
    analyze_prime_set,
    build_report,
    factor_integer,
)


class ObstructionAnalysisTests(unittest.TestCase):
    def test_factorization(self) -> None:
        self.assertEqual(
            factor_integer(2**4 * 7**2 * 11 * 17),
            {2: 4, 7: 2, 11: 1, 17: 1},
        )

    def test_lift_only_counterexample(self) -> None:
        result = analyze_prime_set([7, 19])
        self.assertTrue(result["compatible"])
        self.assertTrue(result["two_adic_component_passes"])
        self.assertTrue(result["odd_radical_divides_n_minus_one"])
        self.assertFalse(result["L_divides_n_minus_one"])
        witness = result["minimum_odd_prime_power_witness"]
        self.assertEqual(witness["prime"], 3)
        self.assertEqual(witness["first_failing_power"], "9")

    def test_full_l_counterexample(self) -> None:
        result = analyze_prime_set([7, 13, 19])
        self.assertTrue(result["compatible"])
        self.assertTrue(result["two_adic_component_passes"])
        self.assertTrue(result["L_divides_n_minus_one"])
        self.assertIsNone(result["minimum_odd_prime_power_witness"])

    def test_frozen_survivor_summary(self) -> None:
        report = build_report(
            PROJECT_ROOT / "results/agent_hunter_cap347.json",
            counterexample_cap=50,
        )
        summary = report["summary"]
        self.assertEqual(summary["records_certified"], 38)
        self.assertEqual(summary["odd_radical_reject_count"], 38)
        self.assertEqual(summary["minimum_witness_is_prime_count"], 38)
        self.assertEqual(
            summary["minimum_witness_value_frequency"],
            {"7": 19, "11": 13, "13": 1, "17": 1, "23": 2, "37": 1, "41": 1},
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
