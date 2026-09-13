#!/usr/bin/env python3
"""Destructive-input rejection tests for the no-import verifier."""

from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATE = ROOT / "certificates" / "trees_n2_n9.json"
VERIFIER = ROOT / "code" / "verifier" / "verify_tree_certificate.py"


def expect_rejection(payload: object, label: str) -> None:
    with tempfile.TemporaryDirectory(prefix="lv-tree-reject-") as directory:
        path = Path(directory) / "mutated.json"
        path.write_text(json.dumps(payload), encoding="utf-8")
        result = subprocess.run(
            [sys.executable, str(VERIFIER), str(path)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )
        if result.returncode == 0 or "REJECTED:" not in result.stderr:
            raise AssertionError(f"verifier accepted mutation: {label}")


def main() -> int:
    original = json.loads(CERTIFICATE.read_text(encoding="utf-8"))

    mutation = copy.deepcopy(original)
    mutation["orders"][-1]["trees"].pop()
    expect_rejection(mutation, "missing order-nine tree")

    mutation = copy.deepcopy(original)
    mutation["orders"][-1]["trees"][1] = copy.deepcopy(
        mutation["orders"][-1]["trees"][0]
    )
    mutation["orders"][-1]["trees"][1]["id"] = "n9_duplicate"
    expect_rejection(mutation, "duplicate unlabeled tree")

    mutation = copy.deepcopy(original)
    mutation["orders"][-1]["trees"][0]["edges"][0] = [0, 0]
    expect_rejection(mutation, "looped edge")

    mutation = copy.deepcopy(original)
    mutation["orders"][-1]["trees"][0]["reconstruction_code"] += "corrupt"
    expect_rejection(mutation, "forged reconstruction result")

    mutation = copy.deepcopy(original)
    mutation["orders"][-1]["trees"][0]["cycle_incidence_signature"][0][0][1] += 1
    expect_rejection(mutation, "forged cycle-incidence invariant")

    mutation = copy.deepcopy(original)
    mutation["unexpected"] = True
    expect_rejection(mutation, "unexpected schema field")

    print("6 fail-closed mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
