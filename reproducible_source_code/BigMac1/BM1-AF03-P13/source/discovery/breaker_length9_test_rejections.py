#!/usr/bin/env python3
"""Corruption tests for the independent length-9 verifier."""

from __future__ import annotations

import copy
import json
import tempfile
from pathlib import Path

from breaker_length9_verify_counterexample import verify


ROOT = Path(__file__).resolve().parents[1]
GOOD = ROOT / "experiments" / "breaker_length9_counterexample_certificate.json"


def must_reject(label: str, payload: object) -> None:
    with tempfile.TemporaryDirectory(prefix="snake_length9_reject_") as directory:
        path = Path(directory) / "bad.json"
        path.write_text(json.dumps(payload), encoding="utf-8")
        try:
            verify(path)
        except SystemExit as exc:
            if not str(exc).startswith("REJECT:"):
                raise AssertionError(f"{label}: unexpected rejection: {exc}") from exc
        else:
            raise AssertionError(f"{label}: corrupted input was accepted")


def main() -> None:
    good = json.loads(GOOD.read_text(encoding="utf-8"))
    cases = []

    payload = copy.deepcopy(good)
    del payload["word"]
    cases.append(("missing field", payload))

    payload = copy.deepcopy(good)
    payload["extra"] = True
    cases.append(("extra field", payload))

    payload = copy.deepcopy(good)
    payload["word"] = "RLRLRLRLR"
    cases.append(("wrong word", payload))

    payload = copy.deepcopy(good)
    payload["hstar_coefficients_ascending"][5] += 1
    cases.append(("wrong hstar", payload))

    payload = copy.deepcopy(good)
    payload["primitive_s_quartic_coefficients_ascending"][0] += 1
    cases.append(("wrong quartic", payload))

    payload = copy.deepcopy(good)
    payload["taylor_coefficients"][0]["imag"][0] += 1
    cases.append(("wrong Taylor data", payload))

    payload = copy.deepcopy(good)
    payload["absolute_value_bounds"]["a1_lower"] *= 2
    cases.append(("false norm bound", payload))

    payload = copy.deepcopy(good)
    payload["disk_radius"] = [12, 2]
    cases.append(("wrong conjectured radius", payload))

    for label, payload in cases:
        must_reject(label, payload)
    print(f"PASS: length-9 verifier rejected {len(cases)}/{len(cases)} corrupted certificates")


if __name__ == "__main__":
    main()
