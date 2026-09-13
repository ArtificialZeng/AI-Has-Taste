#!/usr/bin/env python3
"""Acceptance and adversarial rejection tests for the no-import verifier."""

from __future__ import annotations

import json
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERIFIER = ROOT / "code" / "verify_packing_certificate.py"
GOOD = ROOT / "certificates" / "packing12.json"


def run(path: Path, expected: int = 12) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["python3", str(VERIFIER), str(path), "--expected-blocks", str(expected)],
        text=True,
        capture_output=True,
        check=False,
    )


def main() -> int:
    accepted = run(GOOD)
    assert accepted.returncode == 0, accepted.stdout + accepted.stderr
    report = json.loads(accepted.stdout)
    assert report["status"] == "VERIFIED"
    assert report["developed_blocks"] == 372
    assert report["distinct_triples"] == 3720

    original = json.loads(GOOD.read_text())
    corruptions: list[tuple[str, object]] = []

    duplicate = json.loads(json.dumps(original))
    duplicate["base_blocks"][1] = duplicate["base_blocks"][0]
    corruptions.append(("duplicate-orbit", duplicate))

    collision = json.loads(json.dumps(original))
    collision["base_blocks"][1] = [0, 1, 4, 12, 24]
    corruptions.append(("triple-collision", collision))

    out_of_range = json.loads(json.dumps(original))
    out_of_range["base_blocks"][0][-1] = 31
    corruptions.append(("out-of-range", out_of_range))

    unsorted = json.loads(json.dumps(original))
    unsorted["base_blocks"][0] = [1, 0, 4, 12, 23]
    corruptions.append(("unsorted", unsorted))

    extra_key = json.loads(json.dumps(original))
    extra_key["unverified_claim"] = True
    corruptions.append(("unknown-key", extra_key))

    wrong_count = json.loads(json.dumps(original))
    wrong_count["base_blocks"].pop()
    corruptions.append(("wrong-count", wrong_count))

    non_integer = json.loads(json.dumps(original))
    non_integer["base_blocks"][0][0] = False
    corruptions.append(("boolean-is-not-integer", non_integer))

    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        for name, payload in corruptions:
            path = root / f"{name}.json"
            path.write_text(json.dumps(payload) + "\n")
            rejected = run(path)
            assert rejected.returncode != 0, f"accepted corruption {name}: {rejected.stdout}"
            assert json.loads(rejected.stdout)["status"] == "REJECTED"

        malformed = root / "malformed.json"
        malformed.write_text('{"schema":')
        rejected = run(malformed)
        assert rejected.returncode != 0
        assert json.loads(rejected.stdout)["status"] == "REJECTED"

    print("positive verifier and adversarial rejection tests: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
