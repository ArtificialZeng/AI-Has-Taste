#!/Users/mac/4prove-or-disprove-math/.research-venv/bin/python
"""Build deterministic graph6 streams for rooted canonicalization by labelg.

Every distinguished start is first swapped to vertex 0.  Running
`labelg -fazzzzzzz` then canonically labels the graph subject to vertex 0's
singleton color class.  Line order is retained by labelg and is the census
order consumed by census_modular.cpp.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def decode_graph6(line: bytes) -> list[int]:
    raw = line.strip()
    if not raw or raw[0] != 8 + 63:
        raise ValueError("expected a headerless order-eight graph6 record")
    bits: list[int] = []
    for byte in raw[1:]:
        value = byte - 63
        if not 0 <= value < 64:
            raise ValueError("invalid graph6 byte")
        bits.extend((value >> shift) & 1 for shift in range(5, -1, -1))
    adj = [0] * 8
    cursor = 0
    for j in range(1, 8):
        for i in range(j):
            if bits[cursor]:
                adj[i] |= 1 << j
                adj[j] |= 1 << i
            cursor += 1
    return adj


def encode_graph6(adj: list[int], root: int) -> bytes:
    order = list(range(8))
    order[0], order[root] = order[root], order[0]
    bits = [
        (adj[order[i]] >> order[j]) & 1
        for j in range(1, 8)
        for i in range(j)
    ]
    bits.extend([0] * (-len(bits) % 6))
    encoded = bytearray([8 + 63])
    for offset in range(0, len(bits), 6):
        encoded.append(63 + sum(bits[offset + k] << (5 - k) for k in range(6)))
    return bytes(encoded)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("inventory", type=Path)
    parser.add_argument("base_output", type=Path)
    parser.add_argument("augmented_output", type=Path)
    parser.add_argument("metadata_output", type=Path)
    args = parser.parse_args()

    records = [decode_graph6(line) for line in args.inventory.read_bytes().splitlines()]
    if len(records) != 11094:
        raise ValueError(f"expected 11094 inventory records, got {len(records)}")

    base_count = 0
    augmented_count = 0
    nonedge_count = 0
    with args.base_output.open("wb") as base_handle, args.augmented_output.open("wb") as aug_handle:
        for adj in records:
            for start in range(8):
                base_handle.write(encode_graph6(adj, start) + b"\n")
                base_count += 1
            for v in range(1, 8):
                for u in range(v):
                    if adj[u] >> v & 1:
                        continue
                    nonedge_count += 1
                    augmented = adj[:]
                    augmented[u] |= 1 << v
                    augmented[v] |= 1 << u
                    for start in range(8):
                        aug_handle.write(encode_graph6(augmented, start) + b"\n")
                        augmented_count += 1

    metadata = {
        "inventory_records": len(records),
        "base_rooted_records": base_count,
        "nonedges": nonedge_count,
        "augmented_rooted_records": augmented_count,
        "ordering": "inventory line; nonedge lexicographic (v=1..7,u=0..v-1); start=0..7",
        "root_prelabel": "swap distinguished start with vertex 0",
        "required_labelg_partition": "azzzzzzz",
        "inventory_sha256": sha256(args.inventory),
        "base_precanonical_sha256": sha256(args.base_output),
        "augmented_precanonical_sha256": sha256(args.augmented_output),
        "script_sha256": sha256(Path(__file__)),
    }
    args.metadata_output.write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n")
    print(json.dumps(metadata, sort_keys=True))


if __name__ == "__main__":
    main()
