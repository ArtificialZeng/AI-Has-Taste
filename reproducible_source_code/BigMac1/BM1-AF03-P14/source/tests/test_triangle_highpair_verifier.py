#!/usr/bin/env python3
"""Mutation tests for the fail-closed triangle high-pair verifier."""

from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "results" / "triangle_highpair_no_go_certificate.json"
VERIFIER = ROOT / "src" / "verify_triangle_highpair_no_go.py"


def run(path: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VERIFIER), str(path)],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=180,
        check=False,
    )


def main() -> int:
    original = json.loads(CERT.read_text(encoding="utf-8"))
    good = run(CERT)
    if good.returncode != 0 or "PASS:" not in good.stdout:
        print("valid certificate was rejected", file=sys.stderr)
        print(good.stdout, good.stderr, file=sys.stderr)
        return 1

    mutations: list[tuple[str, dict]] = []

    item = copy.deepcopy(original)
    item["high_pairs"] = [[0, 1], [0, 2]]
    mutations.append(("missing high edge", item))

    item = copy.deepcopy(original)
    item["saturated_groebner_basis"][-1] = item["saturated_groebner_basis"][-1].replace("+4", "+5")
    mutations.append(("basis coefficient", item))

    item = copy.deepcopy(original)
    item["critical_system"]["saturating_product"] = "a0*a1*a2*a3*s"
    mutations.append(("dropped saturation factor", item))

    item = copy.deepcopy(original)
    item["ordered_closure_constraints"]["high_pair_closure"][2] = "a1+a2-a0-a3-1>0"
    mutations.append(("changed closure endpoint", item))

    item = copy.deepcopy(original)
    del item["proof_identities"]["triangle_gap"]
    mutations.append(("truncated proof", item))

    item = copy.deepcopy(original)
    item["saturated_groebner_basis"][0] += ";system(\"false\")"
    mutations.append(("expression injection", item))

    with tempfile.TemporaryDirectory(prefix="triangle-cert-mutations-") as tmp:
        tmpdir = Path(tmp)
        for index, (name, mutated) in enumerate(mutations):
            path = tmpdir / f"mutation_{index}.json"
            path.write_text(json.dumps(mutated), encoding="utf-8")
            result = run(path)
            if result.returncode == 0 or "PASS:" in result.stdout:
                print(f"mutation accepted: {name}", file=sys.stderr)
                return 1

    print(f"PASS: valid certificate accepted; {len(mutations)} corruptions rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

