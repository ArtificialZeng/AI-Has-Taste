#!/usr/bin/env python3
"""Fast exact cross-checks and hand-computable CRIM cases."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "code"))

import discovery_dp  # noqa: E402
import independent_verify  # noqa: E402


class CrimTests(unittest.TestCase):
    def test_conjugation(self) -> None:
        self.assertEqual(independent_verify.transpose((5, 3, 2, 2, 1, 1)), (6, 4, 2, 1, 1))
        self.assertEqual(independent_verify.transpose(()), ())

    def test_hand_options(self) -> None:
        expected = {(1,), (2,), (1, 1)}
        self.assertEqual(discovery_dp.direct_options((2, 1)), expected)
        self.assertEqual(independent_verify.conjugation_options((2, 1)), expected)

    def test_option_generators_agree_through_size_16(self) -> None:
        for size in range(17):
            for shape in discovery_dp.partitions_of(size):
                self.assertEqual(
                    discovery_dp.direct_options(shape),
                    independent_verify.conjugation_options(shape),
                    shape,
                )

    def test_sg_and_boolean_outcomes_agree_through_size_18(self) -> None:
        discovery, grundy = discovery_dp.run(18)
        verification = independent_verify.run(18)
        self.assertEqual(discovery["odd_rank_losing_count"], 0)
        self.assertEqual(discovery["losing_set_sha256"], verification["losing_set_sha256"])
        # A few source-paper examples and elementary positions.
        self.assertEqual(grundy[()], 0)
        self.assertNotEqual(grundy[(1,)], 0)
        self.assertEqual(grundy[(2, 1)], 0)
        self.assertEqual(grundy[(4, 1)], 0)
        self.assertNotEqual(grundy[(4, 4, 4, 1)], 0)


if __name__ == "__main__":
    unittest.main()
