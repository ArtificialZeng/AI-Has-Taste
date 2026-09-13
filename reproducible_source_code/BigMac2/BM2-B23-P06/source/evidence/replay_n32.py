#!/usr/bin/env python3
"""Independent coverage and forbidden-cycle replay for n32_manifest.json.

This verifier does not import the census generator.  It rebuilds each graph
from the frozen gcd definition, checks canonical domain coverage and digests,
and verifies every serialized odd-hole/odd-antihole witness edge by edge.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from math import gcd


def canonical_bytes(value) -> bytes:
    return json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")


def proper_divisors(n: int) -> list[int]:
    answer = []
    for candidate in range(1, n):
        quotient, remainder = divmod(n, candidate)
        if remainder == 0 and quotient >= 2:
            answer.append(candidate)
    return answer


def edge(n: int, selected: set[int], x: int, y: int) -> bool:
    return x != y and gcd(abs(x - y), n) in selected


def rebuilt_rows(n: int, selected: set[int]) -> list[int]:
    rows = []
    for x in range(n):
        row = sum(1 << y for y in range(n) if edge(n, selected, x, y))
        rows.append(row)
    return rows


def row_digest(rows: list[int]) -> str:
    width = (len(rows) + 7) // 8
    return hashlib.sha256(
        b"".join(value.to_bytes(width, byteorder="little") for value in rows)
    ).hexdigest()


def replay_cycle(record: dict) -> None:
    witness = record["witness"]
    assert witness is not None
    n = record["n"]
    selected = set(record["D"])
    cycle = witness["cycle"]
    side = witness["side"]
    assert side in {"graph", "complement"}
    assert len(cycle) >= 5 and len(cycle) % 2 == 1
    assert len(set(cycle)) == len(cycle)
    assert all(isinstance(v, int) and 0 <= v < n for v in cycle)

    def side_edge(x: int, y: int) -> bool:
        present = edge(n, selected, x, y)
        return present if side == "graph" else (x != y and not present)

    length = len(cycle)
    for i in range(length):
        for j in range(i + 1, length):
            cyclic_distance = min(j - i, length - (j - i))
            expected = cyclic_distance == 1
            actual = side_edge(cycle[i], cycle[j])
            assert actual == expected, (
                record["n"], record["dmask"], side, cycle, i, j, actual, expected
            )

    # Independently recalculate the declared unit/translation/dihedral normal form.
    candidates = []
    for multiplier in range(n):
        if gcd(multiplier, n) != 1:
            continue
        image = [(multiplier * vertex) % n for vertex in cycle]
        for order in (image, image[::-1]):
            for pivot in range(length):
                order_at_pivot = order[pivot:] + order[:pivot]
                offset = -order_at_pivot[0]
                candidates.append(tuple((vertex + offset) % n for vertex in order_at_pivot))
    assert tuple(cycle) == min(candidates)


def verify(manifest_path: Path) -> dict:
    raw = manifest_path.read_bytes()
    manifest = json.loads(raw)
    records = manifest["records"]
    assert manifest["domain"] == {"n_max": 32, "n_min": 1, "pair_count": 539}
    assert hashlib.sha256(canonical_bytes(records)).hexdigest() == manifest["records_sha256"]

    expected_keys = [
        (n, dmask)
        for n in range(1, 33)
        for dmask in range(1 << len(proper_divisors(n)))
    ]
    actual_keys = [(record["n"], record["dmask"]) for record in records]
    assert len(expected_keys) == 539
    assert actual_keys == expected_keys
    assert len(set(actual_keys)) == 539

    imperfect = 0
    perfect = 0
    graph_witnesses = 0
    complement_witnesses = 0
    witness_lengths: dict[str, int] = {}
    empty_structural_residue = 0
    for record in records:
        n = record["n"]
        dmask = record["dmask"]
        divisors = proper_divisors(n)
        selected = [d for i, d in enumerate(divisors) if dmask & (1 << i)]
        assert record["divisors"] == divisors
        assert record["D"] == selected
        rows = rebuilt_rows(n, set(selected))
        assert all(not (rows[v] & (1 << v)) for v in range(n))
        assert all(
            bool(rows[x] & (1 << y)) == bool(rows[y] & (1 << x))
            for x in range(n)
            for y in range(n)
        )
        assert row_digest(rows) == record["adjacency_sha256"]
        if record["status"] == "imperfect":
            imperfect += 1
            assert record["witness"] is not None
            assert record["structural_certificates"] == []
            replay_cycle(record)
            side = record["witness"]["side"]
            if side == "graph":
                graph_witnesses += 1
            else:
                complement_witnesses += 1
            key = str(len(record["witness"]["cycle"]))
            witness_lengths[key] = witness_lengths.get(key, 0) + 1
        else:
            perfect += 1
            assert record["status"] == "perfect"
            assert record["witness"] is None
            if not record["structural_certificates"]:
                empty_structural_residue += 1

    assert imperfect == manifest["summary"]["imperfect"]
    assert perfect == manifest["summary"]["perfect"]
    assert empty_structural_residue == manifest["summary"]["perfect_structural_residue"]
    return {
        "adjacency_rebuilds_verified": len(records),
        "complement_witnesses_verified": complement_witnesses,
        "coverage_keys_verified": len(actual_keys),
        "graph_witnesses_verified": graph_witnesses,
        "imperfect_records": imperfect,
        "manifest_sha256": hashlib.sha256(raw).hexdigest(),
        "perfect_records": perfect,
        "records_sha256": manifest["records_sha256"],
        "status": "pass",
        "structural_residue": empty_structural_residue,
        "witness_lengths": dict(sorted(witness_lengths.items(), key=lambda item: int(item[0]))),
        "witnesses_verified": imperfect,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    result = verify(args.manifest)
    args.output.write_bytes(canonical_bytes(result) + b"\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
