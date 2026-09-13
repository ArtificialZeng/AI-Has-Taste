#!/usr/bin/env python3
"""Independent exact checker for the constructive proof data.

This is a diagnostic supplement, not the proof of the infinite families.
It rebuilds every requested coloring from the serialized block specification,
checks it directly against the graph edge definition, and exhausts all binary
increment words for the four exceptional orders.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
SPEC_PATH = HERE / "builder_construction_spec.json"


def coloring_word(n: int, A: str, B: str) -> str | None:
    if n >= 9 and n % 2 == 1:
        return A * ((n - 5) // 2) + B
    if n >= 6 and n % 4 == 2:
        return A * (n // 2)
    if n == 20:
        return A * 3 + B + A * 2 + B
    if n >= 24 and n % 4 == 0:
        k = n // 4
        return A * (k - 1) + B + A * (k - 4) + B
    return None


def direct_graph_check(word: str) -> None:
    n = len(word)
    if any(ch not in "012" for ch in word):
        raise AssertionError("word contains a color outside {0,1,2}")
    offsets = [1, 3] + ([n // 2] if n % 2 == 0 else [])
    for i in range(n):
        for d in offsets:
            j = (i + d) % n
            if word[i] == word[j]:
                raise AssertionError(
                    f"improper word at n={n}: equal colors on edge ({i},{j})"
                )


def admissible_increment_word(signs: tuple[int, ...]) -> bool:
    """Exact equivalence test for a coloring normalized by c_0=0."""
    n = len(signs)
    if sum(signs) % 3:
        return False
    if any(
        signs[i] == signs[(i + 1) % n] == signs[(i + 2) % n]
        for i in range(n)
    ):
        return False
    if n % 2 == 0:
        m = n // 2
        if any(sum(signs[(i + j) % n] for j in range(m)) % 3 == 0 for i in range(n)):
            return False
    return True


def prove_exception_by_exhaustion(n: int) -> int:
    tested = 0
    for signs in itertools.product((-1, 1), repeat=n):
        tested += 1
        if admissible_increment_word(signs):
            raise AssertionError(f"unexpected admissible increment word for n={n}")
    return tested


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=10000)
    args = parser.parse_args()
    if args.max_n < 24:
        raise SystemExit("--max-n must be at least 24")

    raw = SPEC_PATH.read_bytes()
    spec = json.loads(raw)
    if spec.get("graph") != {
        "vertices": "Z/nZ",
        "offset_edges": [1, 3],
        "diameter_edge_for_even_n": True,
        "minimum_n": 6,
    }:
        raise AssertionError("unexpected graph specification")
    if spec.get("colors") != [0, 1, 2]:
        raise AssertionError("unexpected color set")
    A = spec["blocks"]["A"]
    B = spec["blocks"]["B"]
    if (A, B) != ("01", "21202"):
        raise AssertionError("unexpected construction blocks")
    exceptional = set(spec["exceptional_n"])
    if exceptional != {7, 8, 12, 16}:
        raise AssertionError("unexpected exception list")

    constructed = 0
    for n in range(6, args.max_n + 1):
        word = coloring_word(n, A, B)
        if n in exceptional:
            if word is not None:
                raise AssertionError(f"construction should be absent at n={n}")
            continue
        if word is None:
            raise AssertionError(f"construction family missed n={n}")
        if len(word) != n:
            raise AssertionError(f"wrong word length at n={n}")
        direct_graph_check(word)
        constructed += 1

    exhaustion = {n: prove_exception_by_exhaustion(n) for n in sorted(exceptional)}
    code_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    data_hash = hashlib.sha256(raw).hexdigest()
    print(
        json.dumps(
            {
                "status": "PASS",
                "constructed_orders_checked": constructed,
                "maximum_n": args.max_n,
                "exception_increment_words_exhausted": exhaustion,
                "spec_sha256": data_hash,
                "verifier_sha256": code_hash,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
