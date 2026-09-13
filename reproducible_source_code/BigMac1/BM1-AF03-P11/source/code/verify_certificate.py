#!/usr/bin/env python3
"""No-import verifier for the finite skeleton-enumeration certificate.

This program does not import either discovery enumerator or their outputs.  It
parses the claimed JSON, reconstructs every skeleton, evolves it using the
symbolic large-token map from the definition, and checks every integer count.
Malformed, incomplete, duplicated, or inconsistent records fail closed.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import pathlib
import sys
from typing import Iterator, Sequence


REQUIRED_TOP_KEYS = {
    "schema_version",
    "claim",
    "method",
    "source_statement_sha256",
    "discovery_sources",
    "records",
    "target_relation",
}
REQUIRED_RECORD_KEYS = {
    "length",
    "small_count",
    "large_count",
    "skeletons",
    "qualifying_skeletons",
    "permutation_count",
}
REQUIRED_RELATION_KEYS = {"parameter_n", "left", "multiplier", "right_base"}


class CertificateError(Exception):
    pass


def sha256_file(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def require_exact_keys(obj: dict, expected: set[str], location: str) -> None:
    actual = set(obj)
    if actual != expected:
        raise CertificateError(
            f"{location} keys differ: missing={sorted(expected-actual)}, "
            f"unexpected={sorted(actual-expected)}"
        )


def require_plain_int(value: object, location: str, minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:  # bool must be rejected
        raise CertificateError(f"{location} must be an integer >= {minimum}")
    return value


def parse_certificate(path: pathlib.Path) -> dict:
    try:
        with path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise CertificateError(f"cannot parse certificate: {exc}") from exc
    if type(data) is not dict:
        raise CertificateError("top level must be an object")
    require_exact_keys(data, REQUIRED_TOP_KEYS, "top level")
    if data["schema_version"] != 1:
        raise CertificateError("unsupported schema_version")
    for key in ("claim", "method", "source_statement_sha256"):
        if type(data[key]) is not str or not data[key]:
            raise CertificateError(f"{key} must be a nonempty string")
    if type(data["discovery_sources"]) is not dict:
        raise CertificateError("discovery_sources must be an object")
    if type(data["records"]) is not list or not data["records"]:
        raise CertificateError("records must be a nonempty array")
    if type(data["target_relation"]) is not dict:
        raise CertificateError("target_relation must be an object")
    require_exact_keys(data["target_relation"], REQUIRED_RELATION_KEYS, "target_relation")
    return data


def skeletons(length: int, small_count: int) -> Iterator[tuple[int, ...]]:
    """Generate every small-labelled/large-zero skeleton exactly once."""
    small_values = tuple(range(1, small_count + 1))
    for positions in itertools.combinations(range(length), small_count):
        for values in itertools.permutations(small_values):
            if len(positions) != len(values):
                raise CertificateError("internal skeleton generator length mismatch")
            word = [0] * length
            # Avoid zip(..., strict=True): the documented direct executable
            # command must also work with the system Python 3.9 interpreter.
            for position, value in zip(positions, values):
                word[position] = value
            yield tuple(word)


def symbolic_stack_map(word: Sequence[int], small_count: int) -> tuple[int, ...]:
    """Apply the lazy-large skeleton map in O(length) exact operations."""
    sentinel = small_count + 1
    stack: list[int] = []
    prefix_max1: list[int] = []
    prefix_max2: list[int] = []
    output: list[int] = []

    for token in word:
        value = sentinel if token == 0 else token
        # A large token is always pushed in the lazy factor map.  For a small
        # token, max2 > value is exactly "at least two stack entries exceed
        # value".  Prefix maxima make pop rollback constant-time.
        if token != 0:
            while prefix_max2 and prefix_max2[-1] > value:
                output.append(stack.pop())
                prefix_max1.pop()
                prefix_max2.pop()

        if not prefix_max1:
            max1, max2 = value, -1
        else:
            old1 = prefix_max1[-1]
            old2 = prefix_max2[-1]
            if value >= old1:
                max1, max2 = value, old1
            elif value >= old2:
                max1, max2 = old1, value
            else:
                max1, max2 = old1, old2
        stack.append(value)
        prefix_max1.append(max1)
        prefix_max2.append(max2)

    output.extend(reversed(stack))
    return tuple(0 if value == sentinel else value for value in output)


def half_decreasing(word: Sequence[int], small_count: int) -> bool:
    indices = range(len(word) - 2, 0, -2)
    return tuple(word[index] for index in indices) == tuple(range(1, small_count + 1))


def has_maximal_transient(word: tuple[int, ...], small_count: int) -> bool:
    maximum = 2 * small_count
    state = word
    for step in range(maximum + 1):
        if half_decreasing(state, small_count):
            return step == maximum
        state = symbolic_stack_map(state, small_count)
    raise CertificateError("a skeleton exceeded the certified maximum transient")


def verify_record(record: dict, retain_words: bool = False) -> dict:
    if type(record) is not dict:
        raise CertificateError("each record must be an object")
    require_exact_keys(record, REQUIRED_RECORD_KEYS, "record")
    values = {key: require_plain_int(record[key], f"record.{key}") for key in REQUIRED_RECORD_KEYS}
    length = values["length"]
    if length < 1:
        raise CertificateError("record.length must be positive")
    expected_small = (length - 1) // 2
    expected_large = length - expected_small
    if values["small_count"] != expected_small or values["large_count"] != expected_large:
        raise CertificateError(f"invalid small/large split at length {length}")

    total = 0
    qualifying = 0
    terminal_large = 0
    qualifying_words: set[tuple[int, ...]] | None = set() if retain_words else None
    for word in skeletons(length, expected_small):
        total += 1
        if has_maximal_transient(word, expected_small):
            qualifying += 1
            terminal_large += word[-1] == 0
            if qualifying_words is not None:
                qualifying_words.add(word)

    expected_total = math.factorial(length) // math.factorial(expected_large)
    permutation_count = qualifying * math.factorial(expected_large)
    if total != expected_total:
        raise CertificateError(f"internal generator total mismatch at length {length}")
    if values["skeletons"] != total:
        raise CertificateError(f"claimed skeleton count fails at length {length}")
    if values["qualifying_skeletons"] != qualifying:
        raise CertificateError(f"claimed qualifying count fails at length {length}")
    if values["permutation_count"] != permutation_count:
        raise CertificateError(f"claimed permutation count fails at length {length}")
    result = {
        "length": length,
        "skeletons": total,
        "qualifying_skeletons": qualifying,
        "qualifying_terminal_large": terminal_large,
        "permutation_count": permutation_count,
    }
    if qualifying_words is not None:
        result["_qualifying_words"] = qualifying_words
    return result


def verify(path: pathlib.Path, quick: bool) -> dict:
    data = parse_certificate(path)
    source_path = path.parent.parent / "problem" / "source_statement.md"
    if not source_path.is_file():
        raise CertificateError("bound source statement is missing")
    if sha256_file(source_path) != data["source_statement_sha256"]:
        raise CertificateError("source statement hash mismatch")

    records_by_length: dict[int, dict] = {}
    for raw_record in data["records"]:
        if type(raw_record) is not dict or "length" not in raw_record:
            raise CertificateError("record lacks length")
        length = require_plain_int(raw_record["length"], "record.length", 1)
        if length in records_by_length:
            raise CertificateError(f"duplicate record for length {length}")
        records_by_length[length] = raw_record
    if set(records_by_length) != set(range(1, 15)):
        raise CertificateError("records must cover every length 1..14 exactly once")

    selected = range(1, 11) if quick else range(1, 15)
    verified = [
        verify_record(records_by_length[length], retain_words=(not quick and length in (13, 14)))
        for length in selected
    ]
    if quick:
        return {"mode": "quick", "verified_records": verified}

    relation = data["target_relation"]
    n = require_plain_int(relation["parameter_n"], "target_relation.parameter_n", 1)
    left = require_plain_int(relation["left"], "target_relation.left")
    multiplier = require_plain_int(relation["multiplier"], "target_relation.multiplier", 1)
    right_base = require_plain_int(relation["right_base"], "target_relation.right_base")
    if n != 7 or multiplier != n + 1:
        raise CertificateError("target relation parameters are not n=7 and multiplier 8")
    computed = {item["length"]: item for item in verified}
    if left != computed[14]["permutation_count"]:
        raise CertificateError("target left side disagrees with recomputation")
    if right_base != computed[13]["permutation_count"]:
        raise CertificateError("target right base disagrees with recomputation")
    if left != multiplier * right_base:
        raise CertificateError("target integer equality fails")
    if computed[13]["qualifying_skeletons"] != computed[14]["qualifying_skeletons"]:
        raise CertificateError("lengths 13 and 14 have unequal qualifying skeleton totals")
    if computed[13]["qualifying_terminal_large"] != computed[13]["qualifying_skeletons"]:
        raise CertificateError("a qualifying length-13 skeleton lacks a terminal large token")
    if computed[14]["qualifying_terminal_large"] != computed[14]["qualifying_skeletons"]:
        raise CertificateError("a qualifying length-14 skeleton lacks a terminal large token")
    words13 = computed[13].pop("_qualifying_words")
    words14 = computed[14].pop("_qualifying_words")
    if {word + (0,) for word in words13} != words14:
        raise CertificateError("terminal-large extension is not a bijection on qualifying skeletons")

    return {
        "mode": "full",
        "verified_records": verified,
        "verified_relation": f"{left} = {multiplier} * {right_base}",
        "verified_skeleton_bijection": "Q_14 = {w followed by L : w in Q_13}",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=pathlib.Path)
    parser.add_argument("--quick", action="store_true", help="verify lengths 1..10 only")
    args = parser.parse_args()
    try:
        result = verify(args.certificate.resolve(), args.quick)
        result["certificate_sha256"] = sha256_file(args.certificate.resolve())
        result["verifier_sha256"] = sha256_file(pathlib.Path(__file__).resolve())
        print(json.dumps({"status": "PASS", **result}, sort_keys=True))
        return 0
    except CertificateError as exc:
        print(json.dumps({"status": "FAIL", "reason": str(exc)}, sort_keys=True), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
