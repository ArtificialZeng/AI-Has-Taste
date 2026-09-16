#!/usr/bin/env python3
"""Recompute and verify serialized Ferrers block-allocation witnesses."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from block_allocation import block_flow_rho, verify_allocation
from cds_search import cds, corner_rho


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+", type=Path)
    args = parser.parse_args()
    files = records = prefixes = 0
    for path in args.paths:
        payload = json.loads(path.read_text(encoding="utf-8"))
        for record in payload["records"]:
            if "allocation" not in record:
                continue
            shape = tuple(record["shape"])
            target = cds(shape)
            if tuple(record["cds"]) != target:
                raise AssertionError(f"stored CDS mismatch in {path}: {shape}")
            okay, reason = verify_allocation(shape, target, record["allocation"])
            if not okay:
                raise AssertionError(f"bad allocation in {path}: {shape}: {reason}")
            for k in range(len(target) + 1):
                if corner_rho(shape, k) != block_flow_rho(shape, k):
                    raise AssertionError(f"rho mismatch in {path}: {shape}, k={k}")
                prefixes += 1
            records += 1
        files += 1
    print(
        json.dumps(
            {
                "status": "verified",
                "files": files,
                "allocations": records,
                "rho_prefixes_cross_checked": prefixes,
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
