#!/usr/bin/env python3
"""Convert all 61 ES(6) DRAT leaves to LRAT and check them independently."""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import subprocess
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CUBE_DIR = ROOT / "tmp/cubes/es17_first_window_prime_extreme"
MANIFEST = CUBE_DIR / "manifest.json"
PROOF_DIR = ROOT / "tmp/certification/es17_61cubes_120s/proofs"
LRAT_DIR = ROOT / "tmp/certification/es17_61cubes_120s/lrat"
LOG_DIR = ROOT / "tmp/certification/es17_61cubes_120s/lrat_logs"
SUMMARY = ROOT / "tmp/certification/es17_61cubes_120s/lrat_summary.json"
CHECKER_DIR = ROOT / "literature/external/drat-trim"


def convert_and_check(tag: str) -> dict[str, int | float | str]:
    cnf = CUBE_DIR / f"cube_{tag}.cnf"
    drat = PROOF_DIR / f"cube_{tag}.drat"
    lrat = LRAT_DIR / f"cube_{tag}.lrat"
    conversion_log = LOG_DIR / f"cube_{tag}.convert.log"
    check_log = LOG_DIR / f"cube_{tag}.check.log"
    started = time.monotonic()
    converted = subprocess.run(
        [str(CHECKER_DIR / "drat-trim"), str(cnf), str(drat), "-L", str(lrat)],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    conversion_log.write_text(converted.stdout, encoding="utf-8")
    assert converted.returncode == 0 and "s VERIFIED" in converted.stdout, tag
    checked = subprocess.run(
        [str(CHECKER_DIR / "lrat-check"), str(cnf), str(lrat)],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    check_log.write_text(checked.stdout, encoding="utf-8")
    assert checked.returncode == 0 and "c VERIFIED" in checked.stdout, tag
    return {
        "cube": tag,
        "wall_seconds": round(time.monotonic() - started, 3),
        "drat_bytes": drat.stat().st_size,
        "lrat_bytes": lrat.stat().st_size,
        "status": "VERIFIED",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--jobs", type=int, default=8)
    args = parser.parse_args()
    LRAT_DIR.mkdir(parents=True, exist_ok=True)
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    tags = sorted(item["cube"] for item in manifest["cubes"])
    assert len(tags) == 61 and len(set(tags)) == 61
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as executor:
        results = list(executor.map(convert_and_check, tags))
    result = {
        "schema_version": 1,
        "cubes": 61,
        "all_lrat_verified": all(item["status"] == "VERIFIED" for item in results),
        "total_drat_bytes": sum(int(item["drat_bytes"]) for item in results),
        "total_lrat_bytes": sum(int(item["lrat_bytes"]) for item in results),
        "results": results,
    }
    SUMMARY.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print("verified_es17_lrat_leaves=61")
    print(f"verified_es17_total_lrat_bytes={result['total_lrat_bytes']}")
    print(f"summary={SUMMARY}")


if __name__ == "__main__":
    main()
