#!/usr/bin/env python3
"""Independently recheck every serialized CDS-coloring witness in JSON files."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from cds_search import cds, corner_rho, flow_rho, verify_coloring


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+", type=Path)
    args = parser.parse_args()
    checked_files = 0
    checked_records = 0
    checked_prefixes = 0
    for path in args.paths:
        payload = json.loads(path.read_text(encoding="utf-8"))
        for record in payload["records"]:
            if "coloring_zero_based" not in record:
                continue
            shape = tuple(record["shape"])
            target = cds(shape)
            if tuple(record["cds"]) != target:
                raise AssertionError(f"stored CDS mismatch in {path}: {shape}")
            okay, reason = verify_coloring(shape, target, record["coloring_zero_based"])
            if not okay:
                raise AssertionError(f"bad witness in {path}: {shape}: {reason}")
            for k in range(len(target) + 1):
                if corner_rho(shape, k) != flow_rho(shape, k):
                    raise AssertionError(f"independent rho mismatch in {path}: {shape}, k={k}")
                checked_prefixes += 1
            checked_records += 1
        checked_files += 1
    print(
        json.dumps(
            {
                "status": "verified",
                "files": checked_files,
                "witnesses": checked_records,
                "rho_prefixes_cross_checked": checked_prefixes,
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
