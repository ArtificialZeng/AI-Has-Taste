#!/usr/bin/env python3
"""Fail-closed comparison of discovery and independent finite reports."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--discovery", type=Path, nargs="+", required=True)
    parser.add_argument("--independent", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    discovery: dict[int, dict[str, object]] = {}
    for path in args.discovery:
        data = json.loads(path.read_text())
        if data.get("violations") != []:
            raise SystemExit(f"discovery report contains a violation: {path}")
        for row in data.get("orders", []):
            n = int(row["n"])
            if n in discovery:
                raise SystemExit(f"duplicate discovery order {n}")
            discovery[n] = row

    independent_data = json.loads(args.independent.read_text())
    if independent_data.get("violations") != []:
        raise SystemExit("independent report contains a violation")
    independent = {
        int(row["n"]): row for row in independent_data.get("orders", [])
    }

    expected = set(range(1, 16))
    if set(discovery) != expected or set(independent) != expected:
        raise SystemExit(
            f"incomplete orders: discovery={sorted(discovery)}, "
            f"independent={sorted(independent)}"
        )

    rows: list[dict[str, object]] = []
    for n in sorted(expected):
        left = discovery[n]
        right = independent[n]
        compared = {
            "n": n,
            "tree_count": int(left["nonisomorphic_trees"]),
            "md_counts": left["md_counts"],
        }
        if compared["tree_count"] != int(right["free_unlabeled_trees"]):
            raise SystemExit(f"tree-count mismatch at n={n}")
        if compared["md_counts"] != right["md_counts"]:
            raise SystemExit(f"dimension-distribution mismatch at n={n}")
        rows.append(compared)

    output = {
        "schema_version": 1,
        "kind": "finite_report_comparison",
        "status": "PASS",
        "orders_compared": [1, 15],
        "total_free_unlabeled_trees": sum(int(r["tree_count"]) for r in rows),
        "checks": [
            "both reports contain exactly orders 1 through 15",
            "both reports contain no conjecture violation",
            "free-tree counts agree at every order",
            "complete multiset-dimension distributions agree at every order",
        ],
        "rows": rows,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(
        "finite report comparison: PASS; "
        f"{output['total_free_unlabeled_trees']} trees through n=15"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
