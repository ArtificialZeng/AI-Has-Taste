#!/usr/bin/env python3
"""Acceptance and corruption tests for the no-import verifier."""

from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATE = ROOT / "certificates" / "transitive_arrays_n_le_5.json"
VERIFIER = ROOT / "verifier" / "verify_certificate.py"


def run(path: Path) -> int:
    return subprocess.run(
        [sys.executable, str(VERIFIER), str(path)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    ).returncode


def main() -> int:
    if run(CERTIFICATE) != 0:
        raise AssertionError("valid certificate was rejected")
    original = json.loads(CERTIFICATE.read_text())
    mutations = []

    missing = copy.deepcopy(original)
    missing["n_values"]["5"]["arrays"].pop()
    mutations.append(("missing_array", missing))

    duplicate = copy.deepcopy(original)
    duplicate["n_values"]["4"]["arrays"][1] = duplicate["n_values"]["4"]["arrays"][0]
    mutations.append(("duplicate_array", duplicate))

    nontransitive = copy.deepcopy(original)
    nontransitive["n_values"]["3"]["arrays"][0] = "010001000"
    mutations.append(("nontransitive_array", nontransitive))

    bad_hash = copy.deepcopy(original)
    bad_hash["n_values"]["2"]["arrays_sha256"] = "0" * 64
    mutations.append(("bad_hash", bad_hash))

    unknown = copy.deepcopy(original)
    unknown["untrusted_extra_field"] = True
    mutations.append(("unknown_field", unknown))

    with tempfile.TemporaryDirectory() as directory:
        temp = Path(directory)
        for name, mutation in mutations:
            path = temp / f"{name}.json"
            path.write_text(json.dumps(mutation))
            if run(path) == 0:
                raise AssertionError(f"corrupt certificate accepted: {name}")
        malformed = temp / "malformed.json"
        malformed.write_text("{")
        if run(malformed) == 0:
            raise AssertionError("malformed JSON accepted")

    print(f"TESTS_PASSED valid=1 corrupt_rejected={len(mutations) + 1}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
