#!/usr/bin/env python3
"""Run Kissat independently on every CNF in an exhaustive cube directory."""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import subprocess
import time
from pathlib import Path


def run_one(
    solver: Path,
    cnf: Path,
    log_dir: Path,
    seconds: int,
    proof_dir: Path | None,
) -> dict:
    log_path = log_dir / f"{cnf.stem}.log"
    command = [
        str(solver),
        "--unsat",
        "--statistics",
        f"--time={seconds}",
        str(cnf),
    ]
    proof_path = None
    if proof_dir is not None:
        proof_path = proof_dir / f"{cnf.stem}.drat"
        command.append(str(proof_path))
    started = time.monotonic()
    with log_path.open("w", encoding="utf-8") as stream:
        result = subprocess.run(command, stdout=stream, stderr=subprocess.STDOUT)
    elapsed = time.monotonic() - started
    status = {20: "UNSAT", 10: "SAT", 0: "UNKNOWN"}.get(
        result.returncode, f"ERROR_{result.returncode}"
    )
    return {
        "cube": cnf.stem,
        "status": status,
        "returncode": result.returncode,
        "wall_seconds": round(elapsed, 3),
        "cnf": str(cnf),
        "log": str(log_path),
        "proof": str(proof_path) if proof_path is not None else None,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--solver", type=Path, required=True)
    parser.add_argument("--cube-dir", type=Path, required=True)
    parser.add_argument("--log-dir", type=Path, required=True)
    parser.add_argument("--proof-dir", type=Path)
    parser.add_argument("--seconds", type=int, default=60)
    parser.add_argument("--jobs", type=int, default=4)
    parser.add_argument("--summary", type=Path, required=True)
    args = parser.parse_args()

    cnfs = sorted(args.cube_dir.glob("cube_*.cnf"))
    if not cnfs:
        raise SystemExit("no cube CNFs found")
    args.log_dir.mkdir(parents=True, exist_ok=True)
    if args.proof_dir is not None:
        args.proof_dir.mkdir(parents=True, exist_ok=True)

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as executor:
        futures = [
            executor.submit(
                run_one,
                args.solver.resolve(),
                cnf.resolve(),
                args.log_dir.resolve(),
                args.seconds,
                args.proof_dir.resolve() if args.proof_dir is not None else None,
            )
            for cnf in cnfs
        ]
        results = [future.result() for future in concurrent.futures.as_completed(futures)]
    results.sort(key=lambda item: item["cube"])

    counts: dict[str, int] = {}
    for result in results:
        counts[result["status"]] = counts.get(result["status"], 0) + 1
    summary = {
        "schema_version": 1,
        "solver": str(args.solver),
        "time_limit_seconds_per_cube": args.seconds,
        "jobs": args.jobs,
        "counts": counts,
        "complete_unsat_partition": counts == {"UNSAT": len(cnfs)},
        "results": results,
    }
    args.summary.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(counts, sort_keys=True))
    print(f"complete_unsat_partition={summary['complete_unsat_partition']}")


if __name__ == "__main__":
    main()
