#!/usr/bin/env python3
"""Aggregate the frozen rank/order discovery scans without changing them."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    records = []
    for rank in range(2, 6):
        for n in range(6, 16):
            path = args.input_dir / f"n{n}_r{rank}_scan.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            if data["n"] != n or data["rank"] != rank:
                raise AssertionError((path, data["n"], data["rank"]))
            records.append(
                {
                    "file": path.name,
                    "n": n,
                    "rank": rank,
                    "evaluations": data["evaluations"],
                    "best_top_ratio": data["best_top_ratio"],
                    "best_second_ratio": data["best_second_ratio"],
                    "strict_candidate": data["strict_candidate"],
                }
            )
    if any(record["strict_candidate"] for record in records):
        raise AssertionError("strict candidate present; aggregate conclusion must be changed")
    result = {
        "schema_version": 1,
        "scope": {"orders": [6, 15], "ranks": [2, 5]},
        "records": records,
        "total_evaluations": sum(record["evaluations"] for record in records),
        "strict_candidates": 0,
        "evidence_class": "numerical discovery only",
        "verdict": "NO_CANDIDATE_NOT_AN_EXCLUSION",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
