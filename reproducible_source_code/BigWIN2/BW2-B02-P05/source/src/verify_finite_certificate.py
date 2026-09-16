#!/usr/bin/env python3
"""Fail-closed verifier for the finite diagnostic certificate.

The proof is symbolic and does not depend on this certificate.  This verifier
nevertheless recomputes both finite searches from the stated ranges, checks
the discovery-code hashes, and prints hashes binding its input and itself.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from endpoint_checker import check
from run_length_search import search


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATE = ROOT / "certificates" / "finite_check.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    raw = CERTIFICATE.read_bytes()
    data = json.loads(raw)
    if data.get("certificate_kind") != "finite_exact_diagnostics_not_used_as_theorem":
        raise SystemExit("FAIL: wrong or missing certificate kind")
    if data.get("theorem_dependency") is not False:
        raise SystemExit("FAIL: certificate must explicitly deny theorem dependency")

    expected_keys = {"implementation_a", "implementation_b"}
    if not expected_keys.issubset(data):
        raise SystemExit("FAIL: missing implementation record")

    record_a = data["implementation_a"]
    record_b = data["implementation_b"]
    if record_a.get("orders") != [3, 2000] or record_b.get("orders") != [3, 500]:
        raise SystemExit("FAIL: unexpected finite range")

    actual_a = search(2000)
    actual_b = check(500)
    if actual_a != record_a:
        raise SystemExit("FAIL: implementation A recomputation differs")
    if actual_b != record_b:
        raise SystemExit("FAIL: implementation B recomputation differs")

    print(
        json.dumps(
            {
                "status": "PASS",
                "certificate_sha256": hashlib.sha256(raw).hexdigest(),
                "verifier_sha256": sha256(Path(__file__)),
                "implementation_a_sha256": actual_a["code_sha256"],
                "implementation_b_sha256": actual_b["code_sha256"],
                "checked_pairs_total": actual_a["checked_pairs"]
                + actual_b["checked_pairs"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
