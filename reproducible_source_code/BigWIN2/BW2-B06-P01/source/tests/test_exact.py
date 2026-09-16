#!/usr/bin/env python3
"""Fast cross-checks for exact arithmetic and fail-closed certificate parsing."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from discover_numpy import build_mul_table, words_through  # noqa: E402
from verify_certificate import (all_words_through, matrix_product,
                                validate_certificate)  # noqa: E402


class ExactCrossChecks(unittest.TestCase):
    def test_all_matrix_products_match(self) -> None:
        table = build_mul_table()
        for a in range(512):
            for b in range(512):
                self.assertEqual(int(table[a, b]), matrix_product(a, b))

    def test_word_orders_match(self) -> None:
        for degree in range(8):
            self.assertEqual(words_through(degree), all_words_through(degree))

    def test_parser_rejects_tampered_degree(self) -> None:
        data = json.loads((ROOT / "certificates" / "min_degree_7.json").read_text())
        data["identity"]["degree"] = 6
        with self.assertRaises(ValueError):
            validate_certificate(data)

    def test_parser_rejects_duplicate_minor_row(self) -> None:
        data = json.loads((ROOT / "certificates" / "min_degree_7.json").read_text())
        data["lower_bound"]["selected_minor_rows"][1] = dict(
            data["lower_bound"]["selected_minor_rows"][0])
        with self.assertRaises(ValueError):
            validate_certificate(data)


if __name__ == "__main__":
    unittest.main()
