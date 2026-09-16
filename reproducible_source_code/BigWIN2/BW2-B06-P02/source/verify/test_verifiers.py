#!/usr/bin/env python3
"""Regression and fail-closed tests for both exact checkers."""

from __future__ import annotations

import importlib.util
import itertools
import json
import pathlib
import random
import subprocess
import sys
import tempfile


ROOT = pathlib.Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "lyndon8_optimum.json"
PRIMARY = ROOT / "verify" / "verify_certificate.py"
INDEPENDENT = ROOT / "verify" / "independent_checker.py"


def run(checker: pathlib.Path, certificate: pathlib.Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(checker), str(certificate)],
        check=False,
        capture_output=True,
        text=True,
    )


def load_independent_module():
    spec = importlib.util.spec_from_file_location("independent_checker", INDEPENDENT)
    if spec is None or spec.loader is None:
        raise AssertionError("cannot import independent checker")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_hungarian_against_permutations() -> int:
    module = load_independent_module()
    rng = random.Random(20260830)
    cases = 0
    for size in range(1, 7):
        for _ in range(12):
            matrix = [[rng.randrange(-9, 10) for _ in range(size)] for _ in range(size)]
            expected = min(
                sum(matrix[row][perm[row]] for row in range(size))
                for perm in itertools.permutations(range(size))
            )
            observed, assignment = module.hungarian_min(matrix)
            assert observed == expected
            assert sorted(assignment) == list(range(size))
            cases += 1
    return cases


def main() -> None:
    baseline_primary = run(PRIMARY, CERT)
    baseline_independent = run(INDEPENDENT, CERT)
    assert baseline_primary.returncode == 0, baseline_primary.stdout + baseline_primary.stderr
    assert baseline_independent.returncode == 0, baseline_independent.stdout + baseline_independent.stderr

    original = json.loads(CERT.read_text(encoding="utf-8"))
    with tempfile.TemporaryDirectory(prefix="lyndon8-verifier-tests-") as directory:
        temp = pathlib.Path(directory)

        bad_word = json.loads(json.dumps(original))
        bad_word["witness"] = bad_word["witness"][:-1]
        bad_word_path = temp / "bad_word.json"
        bad_word_path.write_text(json.dumps(bad_word), encoding="utf-8")
        assert run(PRIMARY, bad_word_path).returncode != 0
        assert run(INDEPENDENT, bad_word_path).returncode != 0

        bad_dual = json.loads(json.dumps(original))
        bad_dual["overlap_assignment_dual"]["u"][0] -= 1
        bad_dual_path = temp / "bad_dual.json"
        bad_dual_path.write_text(json.dumps(bad_dual), encoding="utf-8")
        assert run(PRIMARY, bad_dual_path).returncode != 0
        # The second checker deliberately recomputes and ignores stored duals.
        assert run(INDEPENDENT, bad_dual_path).returncode == 0

        bad_order = json.loads(json.dumps(original))
        bad_order["target_order"][1] = bad_order["target_order"][0]
        bad_order_path = temp / "bad_order.json"
        bad_order_path.write_text(json.dumps(bad_order), encoding="utf-8")
        assert run(PRIMARY, bad_order_path).returncode != 0
        # The second checker deliberately ignores the discovery path order.
        assert run(INDEPENDENT, bad_order_path).returncode == 0

        missing_field = json.loads(json.dumps(original))
        del missing_field["alphabet_order"]
        missing_field_path = temp / "missing_field.json"
        missing_field_path.write_text(json.dumps(missing_field), encoding="utf-8")
        assert run(PRIMARY, missing_field_path).returncode != 0

    hungarian_cases = test_hungarian_against_permutations()
    print(
        "OK verifier_tests baselines=2 malformed_cases=7 "
        f"hungarian_bruteforce_cases={hungarian_cases} seed=20260830"
    )


if __name__ == "__main__":
    main()
