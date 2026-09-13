#!/usr/bin/env python3
"""Destructive-input tests for the fail-closed certificate verifier."""

from __future__ import annotations

import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
VERIFIER = ROOT / "certificates" / "verify_certificate.py"
VALID = ROOT / "certificates" / "n3_input.json"


class VerifierTamperTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = json.loads(VALID.read_text(encoding="utf-8"))

    def run_payload(self, payload):
        with tempfile.TemporaryDirectory(prefix="lentfer-tamper-") as directory:
            path = Path(directory) / "input.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            return subprocess.run(
                [sys.executable, str(VERIFIER), str(path)],
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                timeout=60,
                check=False,
            )

    def test_valid_baseline_is_accepted(self):
        completed = subprocess.run(
            [sys.executable, str(VERIFIER), str(VALID)],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=60,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout)
        self.assertIn("VERIFIED n=3", completed.stdout)

    def test_missing_key_is_rejected(self):
        payload = copy.deepcopy(self.payload)
        del payload["field"]
        completed = self.run_payload(payload)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("REJECTED", completed.stdout)

    def test_duplicate_candidate_is_rejected(self):
        payload = copy.deepcopy(self.payload)
        payload["monomials"][-1] = payload["monomials"][0]
        completed = self.run_payload(payload)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("duplicate candidate", completed.stdout)

    def test_generator_coefficient_tamper_is_rejected(self):
        payload = copy.deepcopy(self.payload)
        payload["invariant_generators"][0]["terms"][0]["coefficient"] = 2
        completed = self.run_payload(payload)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("generators differ", completed.stdout)

    def test_block_count_tamper_is_rejected(self):
        payload = copy.deepcopy(self.payload)
        first = next(iter(payload["block_counts"]))
        payload["block_counts"][first] += 1
        completed = self.run_payload(payload)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("block count mismatch", completed.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
