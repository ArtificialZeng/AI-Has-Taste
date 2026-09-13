#!/usr/bin/env python3
"""Acceptance and adversarial rejection tests for the global branch cover."""

from __future__ import annotations

import copy
import hashlib
import json
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERIFIER = ROOT / "code/verify_global_fixed_cover.py"
GOOD = ROOT / "certificates/negative/target13_global_fixed_cover_manifest.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(path: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["python3", str(VERIFIER), "--manifest", str(path)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


def main() -> int:
    baseline = run(GOOD)
    assert baseline.returncode == 0, baseline.stdout + baseline.stderr
    report = json.loads(baseline.stdout)
    assert report == {
        "branches": 162,
        "covered_block_variables": 4761,
        "status": "VERIFIED_GLOBAL_TARGET13_UNSAT",
    }
    original = json.loads(GOOD.read_text())

    mutations: list[tuple[str, object]] = []
    changed_claim = copy.deepcopy(original)
    changed_claim["claim"] = "unsupported stronger claim"
    mutations.append(("changed-claim", changed_claim))
    removed_branch = copy.deepcopy(original)
    removed_branch["branches"].pop()
    mutations.append(("removed-branch", removed_branch))
    changed_branch_hash = copy.deepcopy(original)
    changed_branch_hash["branches"][0]["sha256"] = "0" * 64
    mutations.append(("changed-branch-hash", changed_branch_hash))
    changed_distribution = copy.deepcopy(original)
    changed_distribution["symmetry"]["orbit_size_distribution"] = {
        "6": 0, "15": 7, "30": 155
    }
    mutations.append(("changed-distribution", changed_distribution))
    boolean_coverage = copy.deepcopy(original)
    boolean_coverage["symmetry"]["covered_block_variables"] = True
    mutations.append(("boolean-coverage", boolean_coverage))
    changed_total_nodes = copy.deepcopy(original)
    changed_total_nodes["enumeration"]["total_branching_nodes"] += 1
    mutations.append(("changed-total-nodes", changed_total_nodes))

    with tempfile.TemporaryDirectory(prefix="cyclic315-global-cert-audit-") as directory:
        temporary = Path(directory)
        for name, payload in mutations:
            path = temporary / f"{name}.json"
            path.write_text(json.dumps(payload))
            rejected = run(path)
            assert rejected.returncode != 0, (name, rejected.stdout, rejected.stderr)
            assert json.loads(rejected.stdout)["status"] == "REJECTED"

        bad_instance = json.loads((ROOT / "experiments/instance.json").read_text())
        bad_instance["columns"][0]["resources"][0] = 144
        bad_instance_path = temporary / "bad-instance.json"
        bad_instance_path.write_text(json.dumps(bad_instance))
        wrong_semantics = copy.deepcopy(original)
        wrong_semantics["instance"] = {
            "path": str(bad_instance_path),
            "sha256": sha256(bad_instance_path),
        }
        wrong_semantics_path = temporary / "wrong-instance-semantics.json"
        wrong_semantics_path.write_text(json.dumps(wrong_semantics))
        rejected = run(wrong_semantics_path)
        assert rejected.returncode != 0, rejected.stdout + rejected.stderr
        assert json.loads(rejected.stdout)["status"] == "REJECTED"

    print("global 162-branch cover and corruption tests: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
