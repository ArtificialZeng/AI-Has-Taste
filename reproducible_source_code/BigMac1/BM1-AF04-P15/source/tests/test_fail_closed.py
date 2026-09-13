#!/usr/bin/env python3
"""Negative tests for certificate parsing; no discovery output is imported."""

from __future__ import annotations

import json
import pathlib
import subprocess
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
VERIFY = ROOT / "certificates" / "verify_finite_census.py"
VALID = ROOT / "certificates" / "baseline_0124.json"
VALID_V2 = ROOT / "certificates" / "census_max5.json"


def run(document: object) -> int:
    with tempfile.NamedTemporaryFile("w", suffix=".json", encoding="utf-8") as stream:
        json.dump(document, stream)
        stream.flush()
        return subprocess.run(
            ["python3", str(VERIFY), "--schema-only", stream.name],
            check=False, capture_output=True, text=True,
        ).returncode


def main() -> int:
    base = json.loads(VALID.read_text(encoding="utf-8"))
    assert run(base) == 0
    assert run(json.loads(VALID_V2.read_text(encoding="utf-8"))) == 0

    missing = json.loads(json.dumps(base))
    del missing["records"][0]["nodes"]
    assert run(missing) != 0

    tampered_type = json.loads(json.dumps(base))
    tampered_type["records"][0]["maximum_length"] = 62.0
    assert run(tampered_type) != 0

    extra = json.loads(json.dumps(base))
    extra["trusted_answer"] = 62
    assert run(extra) != 0

    bad_alphabet = json.loads(json.dumps(base))
    bad_alphabet["records"][0]["alphabet"] = [0, 2, 4, 8]
    assert run(bad_alphabet) != 0

    bad_witnesses = json.loads(json.dumps(base))
    bad_witnesses["records"][0]["maximizers"] = []
    assert run(bad_witnesses) != 0

    bad_digest = json.loads(VALID_V2.read_text(encoding="utf-8"))
    bad_digest["records"][0]["maximizers_sha256"] = "xyz"
    assert run(bad_digest) != 0

    missing_record = json.loads(VALID_V2.read_text(encoding="utf-8"))
    del missing_record["records"][-1]
    assert run(missing_record) != 0

    print("FAIL_CLOSED_TESTS_OK valid_cases=2 rejected_corruptions=7")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
