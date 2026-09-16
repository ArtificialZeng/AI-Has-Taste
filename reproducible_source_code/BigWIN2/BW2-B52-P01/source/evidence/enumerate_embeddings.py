#!/usr/bin/env python3
"""Exact exhaustive search for induced K_{1,1,5} embeddings.

Translation fixes the first singleton vertex a at zero.  The other singleton
label b is enumerated over every nonzero group element, and the five labels of
the independent part C are enumerated as an unordered subset of the remaining
elements.  This loses no embeddings because the five C vertices are twins.

For each labeling we form both orientations of every edge and nonedge
difference.  A symmetric Cayley connection set exists exactly when those two
sets are disjoint.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class AbelianGroup:
    name: str
    moduli: tuple[int, ...]

    @property
    def zero(self) -> tuple[int, ...]:
        return tuple(0 for _ in self.moduli)

    @property
    def elements(self) -> tuple[tuple[int, ...], ...]:
        return tuple(itertools.product(*(range(m) for m in self.moduli)))

    def sub(self, x: tuple[int, ...], y: tuple[int, ...]) -> tuple[int, ...]:
        return tuple((a - b) % m for a, b, m in zip(x, y, self.moduli))


GROUPS = (
    AbelianGroup("Z10", (10,)),
    AbelianGroup("Z11", (11,)),
    AbelianGroup("Z12", (12,)),
    AbelianGroup("Z2xZ6", (2, 6)),
    AbelianGroup("Z13", (13,)),
    AbelianGroup("Z14", (14,)),
)


def oriented_differences(group: AbelianGroup, pairs):
    result = set()
    for x, y in pairs:
        result.add(group.sub(x, y))
        result.add(group.sub(y, x))
    return result


def test_labeling(group: AbelianGroup, b, c_labels):
    a = group.zero
    edge_pairs = [(a, b)]
    edge_pairs.extend((a, c) for c in c_labels)
    edge_pairs.extend((b, c) for c in c_labels)
    nonedge_pairs = itertools.combinations(c_labels, 2)
    edge_differences = oriented_differences(group, edge_pairs)
    nonedge_differences = oriented_differences(group, nonedge_pairs)
    return edge_differences.isdisjoint(nonedge_differences), edge_differences


def encode(element):
    return element[0] if len(element) == 1 else list(element)


def exhaustive_search(group: AbelianGroup):
    elements = group.elements
    a = group.zero
    tested = 0
    valid = []
    by_b = []
    for b in elements:
        if b == a:
            continue
        tested_for_b = 0
        valid_for_b = 0
        available = tuple(x for x in elements if x not in (a, b))
        for c_labels in itertools.combinations(available, 5):
            tested += 1
            tested_for_b += 1
            works, connection_set = test_labeling(group, b, c_labels)
            if works:
                valid_for_b += 1
                valid.append(
                    {
                        "a": encode(a),
                        "b": encode(b),
                        "C": [encode(c) for c in c_labels],
                        "S": [encode(s) for s in sorted(connection_set)],
                    }
                )
        by_b.append(
            {"b": encode(b), "tested": tested_for_b, "valid": valid_for_b}
        )
    expected = (len(elements) - 1) * len(
        tuple(itertools.combinations(range(len(elements) - 2), 5))
    )
    assert tested == expected
    return {
        "group": group.name,
        "moduli": list(group.moduli),
        "order": len(elements),
        "normalization": "a=0; b ranges over every nonzero element; C is every unordered 5-subset of Gamma\\{0,b}",
        "expected_labelings": expected,
        "tested_labelings": tested,
        "valid_labelings": len(valid),
        "counts_by_b": by_b,
        "witnesses": valid,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    source_path = Path(__file__).resolve().parents[1] / "source.md"
    payload = {
        "method": "exact exhaustive integer enumeration; no floating point",
        "source_sha256": hashlib.sha256(source_path.read_bytes()).hexdigest(),
        "groups": [exhaustive_search(group) for group in GROUPS],
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
