#!/usr/bin/env python3
"""Materialize four corrupt order-31 certificates and require rejection."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]
VERIFIER = Path("audit/order31_independent_aggregate.py")
PREFLIGHT = Path("certificates/order31_preflight.json")
RESULTS = Path("results/order31_sweep")


def make_case(case_root: Path) -> None:
    preflight = json.loads((ROOT / PREFLIGHT).read_text(encoding="utf-8"))
    for relative in [VERIFIER, PREFLIGHT]:
        destination = case_root / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / relative, destination)
    shutil.copytree(ROOT / RESULTS, case_root / RESULTS)
    for relative in preflight["sha256"]:
        source = ROOT / relative
        destination = case_root / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)


def missing_residue_119(case_root: Path) -> None:
    (case_root / RESULTS /
     "order31_chunk119_of_120.summary.done").unlink()


def residue_000_count_mismatch(case_root: Path) -> None:
    path = case_root / RESULTS / "order31_chunk000_of_120.summary.done"
    text = path.read_text(encoding="ascii")
    match = re.search(r"\btrees=(\d+)\b", text)
    if match is None:
        raise RuntimeError("residue-000 summary lacks trees field")
    replacement = f"trees={int(match.group(1)) + 1}"
    path.write_text(text[:match.start()] + replacement + text[match.end():],
                    encoding="ascii")


def terminal_coefficient_tamper(case_root: Path) -> None:
    paths = sorted((case_root / RESULTS).glob("*.exceptions.done"))
    path = next((candidate for candidate in paths
                 if candidate.stat().st_size > 0), None)
    if path is None:
        raise RuntimeError("no serialized exception is available to tamper")
    lines = path.read_text(encoding="ascii").splitlines()
    prefix, coefficients = lines[0].rsplit("coefficients=", 1)
    values = coefficients.split(",")
    values[-1] = str(int(values[-1]) + 1)
    lines[0] = prefix + "coefficients=" + ",".join(values)
    path.write_text("\n".join(lines) + "\n", encoding="ascii")


def preflight_hash_tamper(case_root: Path) -> None:
    path = case_root / PREFLIGHT
    data = json.loads(path.read_text(encoding="utf-8"))
    relative = sorted(data["sha256"])[0]
    digest = data["sha256"][relative]
    data["sha256"][relative] = digest[:-1] + ("0" if digest[-1] != "0" else "1")
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n",
                    encoding="utf-8")


def run_verifier(case_root: Path) -> subprocess.CompletedProcess[str]:
    environment = dict(os.environ)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    return subprocess.run(
        [sys.executable, str(case_root / VERIFIER)],
        cwd=case_root,
        env=environment,
        text=True,
        capture_output=True,
        check=False,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "results" / "fail_closed_rejection_tests.json",
    )
    args = parser.parse_args()
    temp_parent = ROOT / "tmp"
    temp_parent.mkdir(parents=True, exist_ok=True)

    cases: list[tuple[str, Callable[[Path], None], str]] = [
        ("missing_residue_119", missing_residue_119,
         "missing paired completed files for residue 119"),
        ("residue_000_count_mismatch", residue_000_count_mismatch,
         "checker/generator count mismatch at residue 0"),
        ("terminal_coefficient_tamper", terminal_coefficient_tamper,
         "rebuilt coefficients disagree"),
        ("preflight_hash_tamper", preflight_hash_tamper,
         "artifact hash drift"),
    ]

    records: list[dict[str, object]] = []
    for name, mutate, expected in cases:
        with tempfile.TemporaryDirectory(
                prefix=f"fail-closed-{name}.", dir=temp_parent) as temporary:
            case_root = Path(temporary)
            make_case(case_root)
            mutate(case_root)
            completed = run_verifier(case_root)
            passed = completed.returncode != 0 and expected in completed.stderr
            normalized_stderr = completed.stderr.strip().replace(
                str(case_root), "<CASE_ROOT>")
            record = {
                "case": name,
                "exit_code": completed.returncode,
                "expected_rejection": expected,
                "stderr": normalized_stderr,
                "status": "PASS" if passed else "FAIL",
            }
            records.append(record)
            if not passed:
                print(json.dumps(record, sort_keys=True), file=sys.stderr)
                return 1

    result = {
        "status": "PASS",
        "verifier": VERIFIER.as_posix(),
        "cases": records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n",
                           encoding="utf-8")
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
