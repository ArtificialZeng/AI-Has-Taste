#!/usr/bin/env python3
"""Independent fail-closed verifier for the explicit 11-vertex minimizer.

The verifier reconstructs the tournament and proves both bounds without
calling or importing any packing search:

* the serialized 15 triples are transitive and pairwise arc-disjoint;
* every transitive triple uses a within-part pair of the cyclic 4+4+3
  partition; there are exactly 6+6+3=15 such pairs, and a packing cannot reuse
  one, so no packing has more than 15 triples.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from itertools import combinations
from pathlib import Path


REQUIRED_KEYS = {"schema_version", "n", "claimed_value", "parts", "bits", "witness"}


def pair_index(n: int, a: int, b: int) -> int:
    if not 0 <= a < b < n:
        raise ValueError("pair endpoints out of range or unordered")
    return a * (2 * n - a - 1) // 2 + b - a - 1


def beats(bits: str, n: int, a: int, b: int) -> bool:
    if a == b:
        raise ValueError("loop queried")
    if a < b:
        return bits[pair_index(n, a, b)] == "1"
    return bits[pair_index(n, b, a)] == "0"


def transitive(bits: str, n: int, triple: tuple[int, int, int]) -> bool:
    a, b, c = triple
    wins = (
        int(beats(bits, n, a, b)) + int(beats(bits, n, a, c)),
        int(beats(bits, n, b, a)) + int(beats(bits, n, b, c)),
        int(beats(bits, n, c, a)) + int(beats(bits, n, c, b)),
    )
    return sorted(wins) == [0, 1, 2]


def verify(path: Path) -> dict[str, object]:
    try:
        raw = path.read_bytes()
        data = json.loads(raw)
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        raise ValueError(f"unreadable certificate: {error}") from error
    if not isinstance(data, dict) or set(data) != REQUIRED_KEYS:
        raise ValueError("certificate keys do not exactly match schema")
    if data["schema_version"] != 1 or data["n"] != 11 or data["claimed_value"] != 15:
        raise ValueError("wrong schema or endpoint")
    bits = data["bits"]
    if not isinstance(bits, str) or len(bits) != 55 or set(bits) - {"0", "1"}:
        raise ValueError("bits must be a 55-character binary string")

    parts = data["parts"]
    if not isinstance(parts, list) or [len(p) if isinstance(p, list) else -1 for p in parts] != [4, 4, 3]:
        raise ValueError("parts must have sizes 4,4,3")
    if sorted(v for part in parts for v in part) != list(range(11)):
        raise ValueError("parts do not partition the vertices")
    part_of = {v: i for i, part in enumerate(parts) for v in part}
    for a in range(11):
        for b in range(a + 1, 11):
            pa, pb = part_of[a], part_of[b]
            if pa == pb:
                continue
            expected = (pa + 1) % 3 == pb
            if beats(bits, 11, a, b) != expected:
                raise ValueError(f"cross-part arc {(a, b)} violates cyclic orientation")

    witness_raw = data["witness"]
    if not isinstance(witness_raw, list) or len(witness_raw) != 15:
        raise ValueError("witness must list exactly 15 triples")
    used_pairs: set[tuple[int, int]] = set()
    witness: list[tuple[int, int, int]] = []
    for entry in witness_raw:
        if not isinstance(entry, list) or len(entry) != 3 or not all(isinstance(v, int) for v in entry):
            raise ValueError("each witness entry must be three integers")
        triple = tuple(entry)
        if not 0 <= triple[0] < triple[1] < triple[2] < 11:
            raise ValueError(f"witness triple is not strictly ordered: {triple}")
        if not transitive(bits, 11, triple):
            raise ValueError(f"cyclic witness triple: {triple}")
        for pair in combinations(triple, 2):
            if pair in used_pairs:
                raise ValueError(f"reused pair: {pair}")
            used_pairs.add(pair)
        witness.append(triple)

    within_pairs = {
        pair
        for part in parts
        for pair in combinations(sorted(part), 2)
    }
    if len(within_pairs) != 15:
        raise ValueError("within-part pair count is not 15")
    transitive_count = 0
    for triple in combinations(range(11), 3):
        if transitive(bits, 11, triple):
            transitive_count += 1
            if not (set(combinations(triple, 2)) & within_pairs):
                raise ValueError(f"transitive triple lacks a within-part pair: {triple}")

    return {
        "certificate_sha256": hashlib.sha256(raw).hexdigest(),
        "value": 15,
        "witness_pairs": len(used_pairs),
        "within_pairs": len(within_pairs),
        "transitive_triples_checked": transitive_count,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args()
    result = verify(args.certificate)
    print("MINIMIZER_OK " + " ".join(f"{key}={value}" for key, value in result.items()))


if __name__ == "__main__":
    try:
        main()
    except (AssertionError, KeyError, TypeError, ValueError) as error:
        print(f"MINIMIZER_FAIL: {error}")
        raise SystemExit(1)
