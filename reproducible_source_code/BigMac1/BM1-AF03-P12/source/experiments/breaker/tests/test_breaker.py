#!/usr/bin/env python3

from __future__ import annotations

import itertools
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VERIFY = ROOT / "verify_counterexample.py"
VERIFY_FINITE = ROOT / "verify_finite.py"
DISCOVERY = ROOT / "discovery"
SEAL = ROOT / "seal_run.py"


def row_tableau(word: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    rows: list[list[int]] = []
    for value in word:
        carry = value
        for row in rows:
            position = next((j for j, x in enumerate(row) if x > carry), len(row))
            if position == len(row):
                row.append(carry)
                break
            row[position], carry = carry, row[position]
        else:
            rows.append([carry])
    return tuple(tuple(row) for row in rows)


def column_tableau_of_reverse(word: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    rows: list[list[int]] = []
    for value in reversed(word):
        carry = value
        column = 0
        while True:
            hit = None
            for row_index, row in enumerate(rows):
                if column >= len(row):
                    break
                if row[column] >= carry:
                    hit = row_index
                    break
            if hit is None:
                row_index = 0
                while row_index < len(rows) and column < len(rows[row_index]):
                    row_index += 1
                if row_index == len(rows):
                    rows.append([carry])
                else:
                    rows[row_index].append(carry)
                break
            rows[hit][column], carry = carry, rows[hit][column]
            column += 1
    return tuple(tuple(row) for row in rows)


class RSKTests(unittest.TestCase):
    def test_hand_tableau(self) -> None:
        expected = ((1, 2), (3,))
        self.assertEqual(row_tableau((1, 3, 2)), expected)
        self.assertEqual(row_tableau((3, 1, 2)), expected)

    def test_knuth_relations_with_repetitions(self) -> None:
        self.assertEqual(row_tableau((1, 2, 1)), row_tableau((2, 1, 1)))
        self.assertEqual(row_tableau((2, 1, 2)), row_tableau((2, 2, 1)))
        self.assertEqual(row_tableau((2, 1, 3)), row_tableau((2, 3, 1)))

    def test_independent_orientations_agree_exhaustively(self) -> None:
        for length in range(7):
            for word in itertools.product(range(1, 4), repeat=length):
                self.assertEqual(row_tableau(word), column_tableau_of_reverse(word), word)


class RejectTamperingTests(unittest.TestCase):
    def run_verify(self, data: object) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "certificate.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            return subprocess.run(
                [sys.executable, str(VERIFY), str(path)],
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                check=False,
            )

    def base(self) -> dict[str, object]:
        return {
            "schema_version": 1,
            "claim": "membership_changes",
            "u": [1, 2, 3],
            "w": [],
            "k_a": 3,
            "k_b": 4,
            "membership_a": True,
            "membership_b": False,
        }

    def test_rejects_tampered_membership(self) -> None:
        result = self.run_verify(self.base())
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("VERIFY_REJECTED", result.stdout)

    def test_rejects_missing_field(self) -> None:
        data = self.base()
        del data["k_b"]
        self.assertNotEqual(self.run_verify(data).returncode, 0)

    def test_rejects_nonpacked_u(self) -> None:
        data = self.base()
        data["u"] = [1, 2, 2]
        self.assertNotEqual(self.run_verify(data).returncode, 0)

    def test_rejects_bool_disguised_as_integer(self) -> None:
        data = self.base()
        data["k_a"] = True
        self.assertNotEqual(self.run_verify(data).returncode, 0)

    def test_rejects_unexpected_trusted_tableau(self) -> None:
        data = self.base()
        data["left_tableau"] = [[1, 2, 3]]
        self.assertNotEqual(self.run_verify(data).returncode, 0)


class FiniteCertificateTests(unittest.TestCase):
    def make_small_run(self, directory: Path) -> Path:
        raw = directory / "result.raw.json"
        result = directory / "result.json"
        trace = directory / "trace.bin"
        subprocess.run(
            [
                str(DISCOVERY),
                "--u-min-length", "3",
                "--u-max-length", "3",
                "--w-alphabet", "3",
                "--w-max-length", "2",
                "--k-first", "3",
                "--k-last", "4",
                "--trace", str(trace),
                "--result", str(raw),
            ],
            check=True,
            stdout=subprocess.PIPE,
            text=True,
        )
        subprocess.run(
            [
                sys.executable, str(SEAL),
                "--raw", str(raw),
                "--trace", str(trace),
                "--discovery-source", str(ROOT / "discovery.cpp"),
                "--output", str(result),
            ],
            check=True,
            stdout=subprocess.PIPE,
            text=True,
        )
        return result

    def test_independent_finite_verifier_accepts_small_run(self) -> None:
        with tempfile.TemporaryDirectory() as directory_name:
            directory = Path(directory_name)
            result = self.make_small_run(directory)
            # The sealed result expects its trace beside it and source files in ROOT.
            verification = subprocess.run(
                [sys.executable, str(VERIFY_FINITE), str(result), "--source-dir", str(ROOT)],
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                check=False,
            )
            self.assertEqual(verification.returncode, 0, verification.stdout)
            self.assertIn("FINITE_VERIFY_OK", verification.stdout)

    def test_finite_verifier_rejects_tampered_digest(self) -> None:
        with tempfile.TemporaryDirectory() as directory_name:
            directory = Path(directory_name)
            result = self.make_small_run(directory)
            data = json.loads(result.read_text(encoding="utf-8"))
            data["artifacts"]["trace_sha256"] = "0" * 64
            result.write_text(json.dumps(data), encoding="utf-8")
            verification = subprocess.run(
                [sys.executable, str(VERIFY_FINITE), str(result), "--source-dir", str(ROOT)],
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                check=False,
            )
            self.assertNotEqual(verification.returncode, 0)
            self.assertIn("FINITE_VERIFY_REJECTED", verification.stdout)

    def test_finite_verifier_rejects_unknown_top_level_field(self) -> None:
        with tempfile.TemporaryDirectory() as directory_name:
            directory = Path(directory_name)
            result = self.make_small_run(directory)
            data = json.loads(result.read_text(encoding="utf-8"))
            data["trusted_answer"] = "no changes"
            result.write_text(json.dumps(data), encoding="utf-8")
            verification = subprocess.run(
                [sys.executable, str(VERIFY_FINITE), str(result), "--source-dir", str(ROOT)],
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                check=False,
            )
            self.assertNotEqual(verification.returncode, 0)
            self.assertIn("FINITE_VERIFY_REJECTED", verification.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
