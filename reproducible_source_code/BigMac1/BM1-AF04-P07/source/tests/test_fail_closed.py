#!/usr/bin/env python3
"""Negative controls: every deliberately corrupted artifact must be rejected."""

from __future__ import annotations

import json
import subprocess
import tempfile
from copy import deepcopy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "minimizer_11.json"
VERIFIER = ROOT / "code" / "verify_minimizer.py"


def rejected(payload: bytes) -> bool:
    with tempfile.NamedTemporaryFile(suffix=".json") as handle:
        handle.write(payload)
        handle.flush()
        result = subprocess.run(
            ["python3", str(VERIFIER), handle.name],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
    return result.returncode != 0 and b"MINIMIZER_FAIL" in result.stdout


def main() -> None:
    good = json.loads(CERT.read_text(encoding="utf-8"))
    controls: list[tuple[str, bytes]] = []
    controls.append(("invalid-json", b"{"))

    missing = deepcopy(good)
    del missing["bits"]
    controls.append(("missing-field", json.dumps(missing).encode()))

    flipped = deepcopy(good)
    cross_position = 3  # pair (0,4) in the upper-triangle ordering
    replacement = "0" if flipped["bits"][cross_position] == "1" else "1"
    flipped["bits"] = (
        flipped["bits"][:cross_position]
        + replacement
        + flipped["bits"][cross_position + 1 :]
    )
    controls.append(("flipped-cross-arc", json.dumps(flipped).encode()))

    duplicate = deepcopy(good)
    duplicate["witness"][1] = duplicate["witness"][0]
    controls.append(("duplicate-triple", json.dumps(duplicate).encode()))

    cyclic = deepcopy(good)
    cyclic["witness"][0] = [0, 4, 8]
    controls.append(("cyclic-triple", json.dumps(cyclic).encode()))

    bad_vertex = deepcopy(good)
    bad_vertex["witness"][0] = [0, 1, 11]
    controls.append(("out-of-range", json.dumps(bad_vertex).encode()))

    for name, payload in controls:
        assert rejected(payload), f"negative control was accepted: {name}"
        print(f"REJECT_OK {name}")
    print(f"NEGATIVE_CONTROLS_OK count={len(controls)}")


if __name__ == "__main__":
    main()
