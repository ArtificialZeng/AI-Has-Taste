#!/usr/bin/env python3
"""Positive and corrupted-input tests for the independent verifier."""

from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "annihilator_certificate.json"
VERIFY = ROOT / "certificates" / "verify_certificate.py"


def run(path: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(VERIFY), str(path)],
                          text=True, capture_output=True, check=False)


def main() -> int:
    good = run(CERT)
    if good.returncode != 0 or '"status": "VERIFIED"' not in good.stdout:
        raise AssertionError(f"valid certificate rejected: {good.stdout} {good.stderr}")
    original = json.loads(CERT.read_text(encoding="utf-8"))
    mutations = []

    changed_coefficient = copy.deepcopy(original)
    changed_coefficient["expected_l5"]["4"][0] += 1
    mutations.append(("changed_l5_coefficient", changed_coefficient))

    missing_field = copy.deepcopy(original)
    del missing_field["definitions"]["q"]
    mutations.append(("missing_definition", missing_field))

    extra_field = copy.deepcopy(original)
    extra_field["untrusted_hint"] = "accept me"
    mutations.append(("unknown_top_level_field", extra_field))

    wrong_type = copy.deepcopy(original)
    wrong_type["expected_recurrence"]["0"][0] = "2"
    mutations.append(("string_instead_of_integer", wrong_type))

    with tempfile.TemporaryDirectory(prefix="a278992-cert-test-") as tmp:
        tmpdir = Path(tmp)
        for name, payload in mutations:
            path = tmpdir / f"{name}.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            result = run(path)
            if result.returncode == 0:
                raise AssertionError(f"corrupted input accepted: {name}")

    print(f"PASS: valid certificate accepted; {len(mutations)} corruptions rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
