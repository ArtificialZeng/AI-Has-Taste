#!/usr/bin/env python3
"""Destructive-input rejection tests for breaker_verify_counterexample.py."""

from __future__ import annotations

import copy
import json
import tempfile
from pathlib import Path

from breaker_verify_counterexample import verify


ROOT = Path(__file__).resolve().parents[1]
GOOD = ROOT / "experiments" / "breaker_counterexample_certificate.json"


def must_reject(label: str, payload: object) -> None:
    with tempfile.TemporaryDirectory(prefix="snake_breaker_reject_") as directory:
        path = Path(directory) / "bad.json"
        path.write_text(json.dumps(payload), encoding="utf-8")
        try:
            verify(path)
        except SystemExit as exc:
            if not str(exc).startswith("REJECT:"):
                raise AssertionError(f"{label}: non-fail-closed exception text: {exc}") from exc
        else:
            raise AssertionError(f"{label}: corrupted certificate was accepted")


def main() -> None:
    good = json.loads(GOOD.read_text(encoding="utf-8"))

    missing = copy.deepcopy(good)
    del missing["word"]
    must_reject("missing field", missing)

    extra = copy.deepcopy(good)
    extra["untrusted_hint"] = 1
    must_reject("extra field", extra)

    wrong_word = copy.deepcopy(good)
    wrong_word["word"] = "RLRLRLRLRL"
    must_reject("wrong pinned word", wrong_word)

    wrong_hstar = copy.deepcopy(good)
    wrong_hstar["hstar_coefficients_ascending"][5] += 1
    must_reject("corrupt hstar", wrong_hstar)

    wrong_quintic = copy.deepcopy(good)
    wrong_quintic["primitive_y_quintic_coefficients_ascending"][0] += 1
    must_reject("corrupt quintic", wrong_quintic)

    wrong_taylor = copy.deepcopy(good)
    wrong_taylor["taylor_coefficients"][0]["real"][0] += 1
    must_reject("corrupt Taylor coefficient", wrong_taylor)

    false_bound = copy.deepcopy(good)
    false_bound["absolute_value_bounds"]["a1_lower"] *= 2
    must_reject("false norm bound", false_bound)

    false_radius = copy.deepcopy(good)
    false_radius["rouche_radius"] = [1, 100]
    must_reject("nonisolating radius", false_radius)

    print("PASS: verifier rejected 8/8 corrupted certificates")


if __name__ == "__main__":
    main()
