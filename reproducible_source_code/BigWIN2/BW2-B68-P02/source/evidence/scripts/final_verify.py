#!/usr/bin/env python3
"""Single reproducible entry point for the finite disproof evidence."""

from __future__ import annotations

import hashlib
import json
import platform
import subprocess
import time
from pathlib import Path

import networkx
import pysat


ROOT = Path(__file__).resolve().parents[2]
JOB_ID = "win-00068-p02-research-5cb899a40f40"
SOURCE_SHA256 = "6ce58a7ef27abff3de2371ca219430179879b43f26e8da5e94927a140aa70a75"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(command: list[str]) -> dict[str, object]:
    result = subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    assert result.returncode == 0, (command, result.stdout[-4000:])
    return {
        "command": command,
        "returncode": result.returncode,
        "output_sha256": hashlib.sha256(result.stdout.encode()).hexdigest(),
        "last_line": result.stdout.splitlines()[-1] if result.stdout.splitlines() else "",
    }


def load(path: str) -> dict[str, object]:
    return json.loads((ROOT / path).read_text())


def main() -> None:
    started = time.monotonic()
    assert sha256(ROOT / "source.md") == SOURCE_SHA256
    steps: list[dict[str, object]] = []

    steps.append(run(["bash", "tools/build_geng.sh"]))
    assert (ROOT / "tools/nauty-root/geng").read_bytes() == (ROOT / "tools/nauty-root/geng.rebuilt").read_bytes()
    steps.append(run(["bash", "tools/build_checkers.sh"]))
    assert (ROOT / "tools/drat-trim").read_bytes() == (ROOT / "tools/drat-trim.rebuilt").read_bytes()

    scripts = [
        "evidence/scripts/regenerate_census.py",
        "evidence/scripts/verify_census.py",
        "evidence/scripts/independent_census.py",
        "evidence/scripts/verify_witnesses.py",
        "evidence/scripts/check_cnf_bindings.py",
        "evidence/scripts/audit_resolution.py",
        "evidence/scripts/verify_second_encoding.py",
    ]
    for script in scripts:
        steps.append(run(["python3", script]))

    regeneration = load("evidence/census_regeneration.json")
    census = load("evidence/census_verification.json")
    independent = load("evidence/independent_census.json")
    witnesses = load("evidence/witness_verification.json")
    bindings = load("evidence/cnf_binding_verification.json")
    resolution = load("evidence/resolution_audit.json")
    second = load("evidence/second_encoding_replay.json")
    assert regeneration["status"] == census["status"] == independent["status"] == "pass"
    assert regeneration["total"] == census["total"] == independent["total"] == 45982
    assert all(row["byte_identical"] for row in regeneration["orders"])
    assert witnesses["status"] == "all positive witnesses pass"
    assert witnesses["verified_equitable_witnesses"] == 4352
    assert witnesses["verified_proper_nonequitable_witnesses"] == 16
    assert bindings["status"] == "pass" and bindings["checked_cnf_graph_bindings"] == 329
    assert resolution["status"] == "pass" and resolution["proofs_replayed"] == 329
    assert resolution["candidate_count"] == 16 and resolution["candidate_order"] == 16
    assert second["status"] == "pass" and second["drat_proofs_replayed"] == 16
    assert sha256(ROOT / "source.md") == SOURCE_SHA256

    report = {
        "status": "pass",
        "job_id": JOB_ID,
        "script": str(Path(__file__).relative_to(ROOT)),
        "scope": (
            "Rebuild and byte-reproduce the complete n=4,6,...,18 cubic census; "
            "independently prove census completeness/nonisomorphism; verify every positive "
            "coloring through n=16; bind and replay 329 primary DRAT certificates; and bind "
            "and replay a second encoding for all 16 least-order counterexamples."
        ),
        "source_sha256": SOURCE_SHA256,
        "python_version": platform.python_version(),
        "networkx_version": networkx.__version__,
        "pysat_version": pysat.__version__,
        "generator_sha256": sha256(ROOT / "tools/nauty-root/geng"),
        "canonizer_source_sha256": sha256(ROOT / "evidence/scripts/canonical_small.c"),
        "canonizer_binary_sha256": sha256(ROOT / "tools/canonical_small"),
        "drat_checker_source_sha256": sha256(ROOT / "tools/drat-trim.c"),
        "drat_checker_binary_sha256": sha256(ROOT / "tools/drat-trim"),
        "census_total": 45982,
        "classified_graphs_through_order_16": 4681,
        "positive_colorings_checked": 4368,
        "primary_cnf_bindings_checked": 329,
        "primary_drat_proofs_replayed": 329,
        "second_encoding_bindings_checked": 16,
        "second_encoding_drat_proofs_replayed": 16,
        "least_counterexample_order": 16,
        "least_counterexample_classes": 16,
        "steps": steps,
        "seconds": time.monotonic() - started,
    }
    output = ROOT / "evidence/final_verification.json"
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({key: report[key] for key in (
        "status", "census_total", "classified_graphs_through_order_16",
        "primary_drat_proofs_replayed", "second_encoding_drat_proofs_replayed",
        "least_counterexample_classes", "seconds")}, sort_keys=True))


if __name__ == "__main__":
    main()
