#!/usr/bin/env python3
"""Fail-closed tests for audit/independent_routh_verifier.py."""

from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "independent_routh_verifier", ROOT / "audit" / "independent_routh_verifier.py"
)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
GOOD_PATH = ROOT / "certificates" / "routh_audit_input.json"


def must_reject(label: str, payload: object) -> None:
    with tempfile.TemporaryDirectory(prefix="snake_routh_reject_") as directory:
        path = Path(directory) / "input.json"
        path.write_text(json.dumps(payload), encoding="utf-8")
        try:
            MODULE.verify(path)
        except SystemExit as error:
            if not str(error).startswith("REJECT:"):
                raise AssertionError(f"{label}: verifier did not fail closed: {error}") from error
        else:
            raise AssertionError(f"{label}: corrupted input was accepted")


def main() -> int:
    good = json.loads(GOOD_PATH.read_text(encoding="utf-8"))
    assert MODULE.verify(GOOD_PATH)["status"] == "INDEPENDENT_EXACT_AUDIT_PASS"

    mutations = []
    missing = copy.deepcopy(good)
    del missing["word"]
    mutations.append(("missing word", missing))
    extra = copy.deepcopy(good)
    extra["hint"] = "trust me"
    mutations.append(("unknown field", extra))
    wrong_word = copy.deepcopy(good)
    wrong_word["word"] = "LRLRLRLRLL"
    mutations.append(("wrong word", wrong_word))
    wrong_length = copy.deepcopy(good)
    wrong_length["length"] = 9
    mutations.append(("wrong length", wrong_length))
    wrong_center = copy.deepcopy(good)
    wrong_center["center"] = [-13, 2]
    mutations.append(("wrong center", wrong_center))
    wrong_radius = copy.deepcopy(good)
    wrong_radius["radius"] = [13, 2]
    mutations.append(("wrong radius", wrong_radius))
    zero_denominator = copy.deepcopy(good)
    zero_denominator["radius"] = [6, 0]
    mutations.append(("zero denominator", zero_denominator))
    nonintegral = copy.deepcopy(good)
    nonintegral["dimension"] = 24.0
    mutations.append(("nonintegral dimension", nonintegral))

    for label, payload in mutations:
        must_reject(label, payload)
    print(f"PASS: independent verifier accepted the witness and rejected {len(mutations)}/{len(mutations)} corruptions")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
