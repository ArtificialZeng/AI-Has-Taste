#!/usr/bin/env python3
"""Generate exact recursive Frankl-complete local-configuration bounds.

The mathematical input consists only of published seed thresholds.  If at
most a_n distinct k-sets on at most n points can be Non-FC, point deletion
gives

    a_{n+1} = floor((n+1) a_n / (n+1-k)).

The output contains integers only and is intended to be independently
reconstructed by verify_fc_deletion_lift.py.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import comb
from pathlib import Path


SEEDS = {
    4: (8, 11, "FC(4,8)=12"),
    5: (7, 13, "FC(5,7)=14"),
    6: (8, 25, "FC(6,8)=26"),
}


def ceiling(q: Fraction) -> int:
    return -(-q.numerator // q.denominator)


def sequence(k: int, stop: int) -> list[dict[str, int | str]]:
    start, a, source = SEEDS[k]
    if stop < start:
        raise ValueError("stop precedes the certified seed")
    rows: list[dict[str, int | str]] = []
    for n in range(start, stop + 1):
        if n > start:
            previous = a
            a = (n * previous) // (n - k)
        else:
            previous = a

        direct = Fraction(SEEDS[k][1] * comb(n, k), comb(start, k))
        published_ceiling_form = 1 + ceiling(direct)
        row: dict[str, int | str] = {
            "k": k,
            "n": n,
            "non_fc_edge_upper_bound": a,
            "fc_threshold_upper_bound": a + 1,
            "deletion_lhs_multiplicity": n - k,
            "deletion_rhs_multiplier": n,
            "previous_non_fc_bound": previous,
            "direct_seed_floor_threshold": direct.numerator // direct.denominator + 1,
            "published_ceiling_form": published_ceiling_form,
            "seed_source": source,
        }
        if k == 4:
            row["closed_form_non_fc_bound"] = (comb(n, 4) + n) // 7
        rows.append(row)
    return rows


def build_payload(stop: int) -> dict[str, object]:
    return {
        "schema_version": 1,
        "theorem_scope": "recursive upper bounds for FC(k,n), k=4,5,6",
        "seeds": {
            str(k): {
                "n": n,
                "non_fc_edge_upper_bound": a,
                "equivalent_fc_threshold": a + 1,
                "source_statement": source,
            }
            for k, (n, a, source) in sorted(SEEDS.items())
        },
        "recurrence": "a_k(n)=floor(n*a_k(n-1)/(n-k))",
        "rows": {
            str(k): sequence(k, max(stop, SEEDS[k][0]))
            for k in sorted(SEEDS)
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--stop", type=int, default=50)
    args = parser.parse_args()
    if args.stop < 8:
        raise SystemExit("--stop must be at least 8")
    payload = build_payload(args.stop)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    for k, rows in payload["rows"].items():
        final = rows[-1]
        print(
            f"k={k}: n={final['n']}, "
            f"FC threshold <= {final['fc_threshold_upper_bound']}"
        )
    print("GENERATION PASS")


if __name__ == "__main__":
    main()
