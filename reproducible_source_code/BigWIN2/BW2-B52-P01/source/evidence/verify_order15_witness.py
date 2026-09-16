#!/usr/bin/env python3
"""Direct all-pairs verifier for the order-15 certificate.

This intentionally does not import the exhaustive-search implementation.  It
checks the Cayley-set axioms and all 21 unordered vertex pairs directly from
the serialized certificate.
"""

from __future__ import annotations

import argparse
import json
from itertools import combinations
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--witness", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    witness = json.loads(args.witness.read_text())
    modulus = witness["modulus"]
    labels = witness["labels"]
    connection_set = set(witness["connection_set"])
    vertices = tuple(labels)

    assert witness["group"] == "Z15"
    assert modulus == 15
    assert len(labels) == 7
    assert len(set(labels.values())) == 7
    assert 0 not in connection_set
    assert all(0 < s < modulus for s in connection_set)
    assert connection_set == {(-s) % modulus for s in connection_set}

    rows = []
    for u, v in combinations(vertices, 2):
        expected_edge = not (u.startswith("c") and v.startswith("c"))
        forward = (labels[v] - labels[u]) % modulus
        reverse = (labels[u] - labels[v]) % modulus
        forward_adjacent = forward in connection_set
        reverse_adjacent = reverse in connection_set
        assert forward_adjacent == reverse_adjacent == expected_edge
        rows.append(
            {
                "pair": [u, v],
                "expected_edge": expected_edge,
                "forward_difference": forward,
                "reverse_difference": reverse,
                "verified": True,
            }
        )

    output = {
        "certificate": str(args.witness),
        "checks": {
            "seven_distinct_labels": True,
            "zero_excluded_from_connection_set": True,
            "connection_set_symmetric": True,
            "all_21_pairs_match_K_1_1_5": True,
        },
        "pair_count": len(rows),
        "pairs": rows,
    }
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
