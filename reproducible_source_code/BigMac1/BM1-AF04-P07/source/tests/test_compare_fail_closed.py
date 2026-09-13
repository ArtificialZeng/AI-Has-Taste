#!/usr/bin/env python3
"""Negative controls for the independent-sweep comparison gate."""

from __future__ import annotations

import json
import subprocess
import tempfile
from copy import deepcopy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "certificates" / "baseline_n9_builder_full.json"
CERTIFIER = ROOT / "certificates" / "baseline_n9_certifier_opt.json"
COMPARE = ROOT / "code" / "compare_sweeps.py"


def run(left: Path, right: Path, output: Path) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        ["python3", str(COMPARE), str(left), str(right), str(output)],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )


def main() -> None:
    builder = json.loads(BUILDER.read_text(encoding="utf-8"))
    certifier = json.loads(CERTIFIER.read_text(encoding="utf-8"))
    with tempfile.TemporaryDirectory() as temporary:
        root = Path(temporary)
        left = root / "builder.json"
        right = root / "certifier.json"
        output = root / "match.json"
        left.write_text(json.dumps(builder), encoding="utf-8")
        right.write_text(json.dumps(certifier), encoding="utf-8")
        positive = run(left, right, output)
        assert positive.returncode == 0 and b"SWEEPS_MATCH_OK" in positive.stdout
        print("POSITIVE_CONTROL_OK sweep-compare")

        controls: list[tuple[str, object]] = []
        bad_status = deepcopy(certifier)
        bad_status["status"] = "FAIL"
        controls.append(("non-pass", bad_status))

        changed_hash = deepcopy(certifier)
        changed_hash["slices"][0]["stream_sha256"] = "0" * 64
        controls.append(("stream-hash", changed_hash))

        changed_count = deepcopy(certifier)
        changed_count["slices"][0]["count"] += 1
        controls.append(("slice-count", changed_count))

        same_scanner = deepcopy(certifier)
        same_scanner["scanner_sha256"] = builder["scanner_sha256"]
        controls.append(("same-scanner", same_scanner))

        wrong_endpoint = deepcopy(certifier)
        wrong_endpoint["target"] = 8
        controls.append(("wrong-endpoint", wrong_endpoint))

        for name, payload in controls:
            right.write_text(json.dumps(payload), encoding="utf-8")
            result = run(left, right, output)
            assert result.returncode != 0 and b"SWEEPS_MATCH_FAIL" in result.stdout, (
                name,
                result.stdout,
            )
            print(f"REJECT_OK compare-{name}")

        right.write_bytes(b"{")
        malformed = run(left, right, output)
        assert malformed.returncode != 0 and b"SWEEPS_MATCH_FAIL" in malformed.stdout
        print("REJECT_OK compare-malformed-json")

    print("COMPARE_NEGATIVE_CONTROLS_OK count=6")


if __name__ == "__main__":
    main()
