#!/usr/bin/env python3
"""Independent fail-closed verifier for a positive cyclic packing certificate.

This program deliberately imports no discovery or instance-generation module.
It reconstructs the full translation development directly from the serialized
base blocks and checks every developed triple for uniqueness.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path

V = 31
EXPECTED_KEYS = {"schema", "v", "block_size", "strength", "lambda", "base_blocks"}
EXPECTED_HEADER = {
    "schema": "cyclic-315-packing-certificate-v1",
    "v": V,
    "block_size": 5,
    "strength": 3,
    "lambda": 1,
}


class Rejected(ValueError):
    """A malformed or mathematically invalid certificate."""


def translate(block: tuple[int, ...], shift: int) -> tuple[int, ...]:
    return tuple(sorted((point + shift) % V for point in block))


def canonical_translate(block: tuple[int, ...]) -> tuple[int, ...]:
    return min(translate(block, shift) for shift in range(V))


def load_strict(path: Path) -> tuple[bytes, dict[str, object]]:
    raw = path.read_bytes()
    try:
        text = raw.decode("utf-8")
        data = json.loads(text)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise Rejected(f"invalid UTF-8 JSON: {exc}") from exc
    if not isinstance(data, dict) or set(data) != EXPECTED_KEYS:
        raise Rejected("top-level keys do not exactly match the certificate schema")
    for key, value in EXPECTED_HEADER.items():
        if type(data.get(key)) is not type(value) or data.get(key) != value:
            raise Rejected(f"invalid header field {key!r}")
    return raw, data


def verify(path: Path, expected_blocks: int | None) -> dict[str, object]:
    raw, data = load_strict(path)
    serialized = data["base_blocks"]
    if not isinstance(serialized, list) or not serialized:
        raise Rejected("base_blocks must be a nonempty list")
    if expected_blocks is not None and len(serialized) != expected_blocks:
        raise Rejected(f"expected {expected_blocks} base blocks, found {len(serialized)}")

    blocks: list[tuple[int, ...]] = []
    for index, entry in enumerate(serialized):
        if not isinstance(entry, list) or len(entry) != 5:
            raise Rejected(f"base block {index} is not a list of length five")
        if any(type(point) is not int for point in entry):
            raise Rejected(f"base block {index} contains a non-integer")
        block = tuple(entry)
        if tuple(sorted(block)) != block:
            raise Rejected(f"base block {index} is not strictly increasing")
        if len(set(block)) != 5 or not all(0 <= point < V for point in block):
            raise Rejected(f"base block {index} has repeated or out-of-range points")
        blocks.append(block)

    representatives = [canonical_translate(block) for block in blocks]
    if len(set(representatives)) != len(representatives):
        raise Rejected("two base blocks represent the same translation orbit")

    developed: set[tuple[int, ...]] = set()
    owner: dict[tuple[int, ...], tuple[int, int, tuple[int, ...]]] = {}
    for block_index, block in enumerate(blocks):
        for shift in range(V):
            translated = translate(block, shift)
            if translated in developed:
                raise Rejected(f"duplicate developed block from base {block_index}, shift {shift}")
            developed.add(translated)
            for triple in itertools.combinations(translated, 3):
                if triple in owner:
                    previous = owner[triple]
                    raise Rejected(
                        "repeated triple "
                        f"{triple}: first at base/shift/block {previous}, "
                        f"again at base {block_index}, shift {shift}, block {translated}"
                    )
                owner[triple] = (block_index, shift, translated)

    expected_developed = V * len(blocks)
    expected_triples = expected_developed * 10
    if len(developed) != expected_developed or len(owner) != expected_triples:
        raise Rejected("internal count mismatch after full development")
    return {
        "status": "VERIFIED",
        "certificate_sha256": hashlib.sha256(raw).hexdigest(),
        "base_blocks": len(blocks),
        "developed_blocks": len(developed),
        "distinct_triples": len(owner),
        "total_triples_in_Z31": 31 * 30 * 29 // 6,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--expected-blocks", type=int)
    args = parser.parse_args()
    try:
        result = verify(args.certificate, args.expected_blocks)
    except (OSError, Rejected) as exc:
        print(json.dumps({"status": "REJECTED", "reason": str(exc)}, sort_keys=True))
        return 1
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
