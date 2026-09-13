#!/usr/bin/env python3
"""Independent exact replay of the 4-letter binary-uniform morphism census."""

from __future__ import annotations

import collections
import hashlib
import itertools
import json
import pathlib
import sys


def fixed_prefix(images: tuple[tuple[int, int], ...], length: int) -> list[int]:
    word = [0]
    while len(word) < length:
        word = [value for letter in word for value in images[letter]]
    return word[:length]


def first_square(word: list[int]) -> tuple[int, int, int] | None:
    # Deliberately independent direct multiset comparison, with no prefix-count
    # arrays and no import from the discovery executable.
    for end in range(2, len(word) + 1):
        for half in range(1, end // 2 + 1):
            start = end - 2 * half
            if collections.Counter(word[start:end-half]) == collections.Counter(word[end-half:end]):
                return start, half, end
    return None


def encode(images: tuple[tuple[int, int], ...]) -> str:
    return ";".join("".join(map(str, image)) for image in images)


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: verify_uniform2_no_go.py CERTIFICATE", file=sys.stderr)
        return 2
    path = pathlib.Path(sys.argv[1])
    try:
        certificate = json.loads(path.read_text(encoding="utf-8"))
        required = {
            "schema", "alphabet_size", "uniform_length", "prolongable_letter",
            "prefix_length", "morphisms", "latest_first_endpoint",
            "latest_first_count", "endpoint_histogram", "example_morphism",
        }
        if type(certificate) is not dict or set(certificate) != required:
            raise ValueError("missing or unexpected fields")
        if certificate["schema"] != "uniform2-abelian-square-no-go-v1":
            raise ValueError("wrong schema")
        if (certificate["alphabet_size"], certificate["uniform_length"],
                certificate["prolongable_letter"], certificate["prefix_length"]) != (4, 2, 0, 128):
            raise ValueError("wrong fixed scope")

        histogram: collections.Counter[int] = collections.Counter()
        latest_endpoint = -1
        latest: list[str] = []
        total = 0
        for tail in itertools.product(range(4), repeat=7):
            images = ((0, tail[0]), (tail[1], tail[2]),
                      (tail[3], tail[4]), (tail[5], tail[6]))
            square = first_square(fixed_prefix(images, 128))
            if square is None:
                raise ValueError(f"unresolved morphism {encode(images)}")
            endpoint = square[2]
            histogram[endpoint] += 1
            total += 1
            if endpoint > latest_endpoint:
                latest_endpoint = endpoint
                latest = [encode(images)]
            elif endpoint == latest_endpoint:
                latest.append(encode(images))

        actual_histogram = ",".join(f"{k}:{histogram[k]}" for k in sorted(histogram))
        checks = {
            "morphisms": total,
            "latest_first_endpoint": latest_endpoint,
            "latest_first_count": len(latest),
            "endpoint_histogram": actual_histogram,
            "example_morphism": sorted(latest)[0],
        }
        for key, value in checks.items():
            if certificate[key] != value:
                raise ValueError(f"mismatch: {key}")
        print(json.dumps({
            "status": "VERIFIED",
            "certificate_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "verifier_sha256": hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
            "morphisms": total,
        }, sort_keys=True))
        return 0
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as error:
        print(f"REJECTED: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
