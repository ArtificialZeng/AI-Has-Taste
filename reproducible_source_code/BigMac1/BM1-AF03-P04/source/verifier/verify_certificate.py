#!/usr/bin/env python3
"""Fail-closed, no-import verifier for the exact finite certificate."""

from __future__ import annotations

import hashlib
import itertools
import json
import math
import sys
from collections import Counter
from pathlib import Path


ROOT_KEYS = {
    "schema_version",
    "certificate_kind",
    "source_version",
    "theorem_endpoint",
    "construction",
    "n_values",
}
ENTRY_KEYS = {
    "n",
    "type_count",
    "color_histogram",
    "residual_instances",
    "arrays_sha256",
    "arrays",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def digest_lines(lines: list[str]) -> str:
    return hashlib.sha256(("\n".join(lines) + "\n").encode()).hexdigest()


def normalize(word: tuple[int, ...] | list[int]) -> str:
    seen: dict[int, int] = {}
    output: list[str] = []
    for symbol in word:
        if symbol not in seen:
            seen[symbol] = len(seen)
        output.append(str(seen[symbol]))
    return "".join(output)


def partitions(n: int, k: int):
    # Independent implementation: filter the finite Cartesian product.
    for word in itertools.product(range(k), repeat=n):
        if word[0] != 0 or set(word) != set(range(k)):
            continue
        if all(word[index] <= 1 + max(word[:index]) for index in range(1, n)):
            yield word


def reconstruct_types(n: int) -> set[str]:
    reconstructed = {"0" * (n * n)}

    # Reconstruct all two-color partitions from the quotient classification.
    for size in range(1, n + 1):
        for blocks in partitions(n, size):
            for order in itertools.permutations(range(size)):
                for diagonal in itertools.product((0, 1), repeat=size):
                    word = []
                    for i, j in itertools.product(range(n), repeat=2):
                        left, right = blocks[i], blocks[j]
                        if left == right:
                            word.append(diagonal[left])
                        else:
                            word.append(int(order[right] > order[left]))
                    candidate = normalize(word)
                    if len(set(candidate)) == 2:
                        reconstructed.add(candidate)

    # Proposition 3.14 says every type with >=3 colors has one of these forms.
    for size in range(3, n + 1):
        for blocks in partitions(n, size):
            reconstructed.add(normalize([blocks[i] for i in range(n) for _ in range(n)]))
            reconstructed.add(normalize([blocks[j] for _ in range(n) for j in range(n)]))
    return reconstructed


def check_transitivity(array: str, n: int) -> None:
    for i, j, k in itertools.product(range(n), repeat=3):
        require(
            array[i * n + k] in (array[i * n + j], array[j * n + k]),
            f"nontransitive array at n={n}, triple={(i, j, k)}",
        )


def verify_entry(key: str, entry: object) -> tuple[int, int]:
    require(type(entry) is dict, f"entry {key} is not an object")
    require(set(entry) == ENTRY_KEYS, f"entry {key} has missing/unknown fields")
    n = entry["n"]
    require(type(n) is int and str(n) == key and 2 <= n <= 5, f"invalid n entry {key}")
    arrays = entry["arrays"]
    require(type(arrays) is list and arrays, f"arrays for n={n} must be nonempty")
    require(all(type(array) is str for array in arrays), f"non-string array at n={n}")
    require(arrays == sorted(arrays), f"arrays for n={n} are not sorted")
    require(len(arrays) == len(set(arrays)), f"duplicate arrays for n={n}")
    for array in arrays:
        require(len(array) == n * n, f"wrong array length at n={n}")
        require(all("0" <= char <= "9" for char in array), f"invalid array symbol at n={n}")
        require(normalize([int(char) for char in array]) == array, f"noncanonical colors at n={n}")
        check_transitivity(array, n)

        # Directly check that every CYBE component has an admissible T-CYBE label.
        for j, i, k in itertools.product(range(n), repeat=3):
            c = array[i * n + j]
            middle = array[k * n + j]
            c_double_prime = array[k * n + i]
            require(
                middle in (c, c_double_prime),
                f"residual component is not a T-CYBE relation at n={n}",
            )

    require(type(entry["type_count"]) is int, f"invalid type_count at n={n}")
    require(entry["type_count"] == len(arrays), f"wrong type_count at n={n}")
    require(type(entry["residual_instances"]) is int, f"invalid residual count at n={n}")
    require(
        entry["residual_instances"] == len(arrays) * n**3,
        f"wrong residual_instances at n={n}",
    )
    require(type(entry["arrays_sha256"]) is str, f"invalid digest at n={n}")
    require(entry["arrays_sha256"] == digest_lines(arrays), f"array digest mismatch at n={n}")
    histogram = Counter(len(set(array)) for array in arrays)
    require(
        entry["color_histogram"] == {str(k): v for k, v in sorted(histogram.items())},
        f"color histogram mismatch at n={n}",
    )

    reconstructed = reconstruct_types(n)
    require(set(arrays) == reconstructed, f"certificate is incomplete or extraneous at n={n}")
    return len(arrays), len(arrays) * n**3


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: verify_certificate.py CERTIFICATE.json", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    try:
        raw = path.read_bytes()
        data = json.loads(raw)
        require(type(data) is dict, "certificate root is not an object")
        require(set(data) == ROOT_KEYS, "certificate root has missing/unknown fields")
        require(data["schema_version"] == 1, "unsupported schema_version")
        require(
            data["certificate_kind"] == "canonical_transitive_array_enumeration",
            "wrong certificate_kind",
        )
        require(type(data["source_version"]) is str and data["source_version"], "missing source version")
        require(type(data["theorem_endpoint"]) is str and data["theorem_endpoint"], "missing endpoint")
        require(type(data["construction"]) is str and data["construction"], "missing construction")
        values = data["n_values"]
        require(type(values) is dict and set(values) == {"2", "3", "4", "5"}, "wrong n range")
        total_types = 0
        total_residuals = 0
        for key in ("2", "3", "4", "5"):
            count, residuals = verify_entry(key, values[key])
            total_types += count
            total_residuals += residuals
        code_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
        input_hash = hashlib.sha256(raw).hexdigest()
        print(
            "VERIFIED "
            f"types={total_types} residual_instances={total_residuals} "
            f"input_sha256={input_hash} verifier_sha256={code_hash}"
        )
        return 0
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, TypeError) as error:
        print(f"REJECTED: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
