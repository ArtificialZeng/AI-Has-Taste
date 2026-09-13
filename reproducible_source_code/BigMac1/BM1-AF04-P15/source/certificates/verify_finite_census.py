#!/usr/bin/env python3
"""Fail-closed coordinator for the independent exact finite-census verifier."""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import re
import subprocess
import sys
import tempfile
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parent.parent
CPP = ROOT / "certificates" / "independent_tail_dfs.cpp"

TOP_KEYS = {"schema", "scope", "records", "arithmetic", "randomness", "external_baseline"}
SCOPES = {
    "additive-square-finite-census-v1":
        "baseline reproduction for one exact normalized alphabet",
    "additive-square-finite-census-v2":
        "all primitive normalized four-letter integer alphabets with maximum letter at most 5, one representative modulo reflection",
}
ALPHABETS = {
    "additive-square-finite-census-v1": [(0, 1, 2, 4)],
    "additive-square-finite-census-v2": [
        (0, 1, 2, 3),
        (0, 1, 2, 4),
        (0, 1, 3, 4),
        (0, 1, 2, 5),
        (0, 1, 3, 5),
        (0, 1, 4, 5),
        (0, 2, 3, 5),
    ],
}
RECORD_KEYS_V1 = {
    "alphabet", "nodes", "leaves", "maximum_length", "maximizer_count", "maximizers"
}
RECORD_KEYS_V2 = {
    "alphabet", "nodes", "leaves", "maximum_length", "maximizer_count",
    "maximizers_sha256", "witness"
}


def reject(condition: bool, message: str) -> None:
    if condition:
        raise ValueError(message)


def strict_int(value: Any, name: str, minimum: int = 0) -> int:
    reject(type(value) is not int, f"{name} must be an integer")
    reject(value < minimum, f"{name} is below {minimum}")
    return value


def parse_certificate(path: pathlib.Path) -> dict[str, Any]:
    try:
        document = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise ValueError(f"cannot parse certificate: {error}") from error
    reject(type(document) is not dict, "top level must be an object")
    reject(set(document) != TOP_KEYS, "top-level fields are missing or unexpected")
    schema = document["schema"]
    reject(schema not in {"additive-square-finite-census-v1", "additive-square-finite-census-v2"},
           "wrong schema")
    reject(document["scope"] != SCOPES[schema], "wrong scope declaration")
    reject(document["arithmetic"] != "signed exact integers", "wrong arithmetic declaration")
    reject(document["randomness"] != "none", "randomness must be none")
    reject(type(document["scope"]) is not str or not document["scope"], "invalid scope")
    reject(type(document["external_baseline"]) is not str, "invalid provenance field")
    records = document["records"]
    reject(type(records) is not list or not records, "records must be a nonempty array")
    seen: set[tuple[int, ...]] = set()
    for index, record in enumerate(records):
        reject(type(record) is not dict, f"record {index} is not an object")
        expected_keys = RECORD_KEYS_V1 if schema.endswith("v1") else RECORD_KEYS_V2
        reject(set(record) != expected_keys, f"record {index} fields are missing or unexpected")
        alphabet = record["alphabet"]
        reject(type(alphabet) is not list or len(alphabet) < 1, f"record {index}: bad alphabet")
        reject(any(type(x) is not int for x in alphabet), f"record {index}: noninteger letter")
        reject(alphabet != sorted(set(alphabet)), f"record {index}: alphabet not strictly sorted")
        reject(alphabet[0] != 0, f"record {index}: alphabet not translated")
        from math import gcd
        divisor = 0
        for value in alphabet:
            divisor = gcd(divisor, value)
        reject(len(alphabet) > 1 and divisor != 1, f"record {index}: alphabet not primitive")
        frozen = tuple(alphabet)
        reject(frozen in seen, f"record {index}: duplicate alphabet")
        seen.add(frozen)
        for key in ("nodes", "leaves", "maximum_length", "maximizer_count"):
            strict_int(record[key], f"record {index}.{key}")
        if schema.endswith("v1"):
            maximizers = record["maximizers"]
            reject(type(maximizers) is not list, f"record {index}: maximizers not an array")
            reject(any(type(x) is not str for x in maximizers), f"record {index}: bad maximizer")
            reject(len(maximizers) != record["maximizer_count"],
                   f"record {index}: maximizer list/count mismatch")
            reject(maximizers != sorted(set(maximizers)),
                   f"record {index}: maximizers not sorted and unique")
        else:
            digest = record["maximizers_sha256"]
            reject(type(digest) is not str or re.fullmatch(r"[0-9a-f]{64}", digest) is None,
                   f"record {index}: malformed maximizer digest")
            reject(type(record["witness"]) is not str or not record["witness"],
                   f"record {index}: malformed witness")
    reject([tuple(record["alphabet"]) for record in records] != ALPHABETS[schema],
           "record coverage or canonical order does not match the declared scope")
    return document


def compile_verifier(output: pathlib.Path) -> None:
    command = [
        "clang++", "-O3", "-std=c++20", "-Wall", "-Wextra", "-pedantic",
        str(CPP), "-o", str(output),
    ]
    completed = subprocess.run(command, check=False, capture_output=True, text=True)
    if completed.returncode != 0:
        raise RuntimeError(f"independent verifier failed to compile:\n{completed.stderr}")


def recompute(binary: pathlib.Path, alphabet: list[int]) -> dict[str, Any]:
    completed = subprocess.run(
        [str(binary), *(str(x) for x in alphabet)],
        check=False, capture_output=True, text=True,
    )
    if completed.returncode != 0:
        raise RuntimeError(f"enumerator rejected input:\n{completed.stderr}")
    values: dict[str, Any] = {"maximizers": []}
    scalar_keys = {"nodes", "leaves", "maximum_length", "maximizer_count"}
    for line in completed.stdout.splitlines():
        reject("=" not in line, "malformed enumerator output")
        key, value = line.split("=", 1)
        if key == "maximizer":
            values["maximizers"].append(value)
        else:
            reject(key not in scalar_keys or key in values, "unexpected/duplicate enumerator field")
            values[key] = strict_int(int(value), key)
    reject(set(values) != scalar_keys | {"maximizers"}, "incomplete enumerator output")
    reject(len(values["maximizers"]) != values["maximizer_count"],
           "enumerator maximizer count mismatch")
    return values


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=pathlib.Path)
    parser.add_argument("--schema-only", action="store_true")
    args = parser.parse_args()
    try:
        document = parse_certificate(args.certificate)
        if args.schema_only:
            print("SCHEMA_OK")
            return 0
        with tempfile.TemporaryDirectory(prefix="asq-cert-") as temp_dir:
            binary = pathlib.Path(temp_dir) / "independent_tail_dfs"
            compile_verifier(binary)
            for record in document["records"]:
                actual = recompute(binary, record["alphabet"])
                if document["schema"].endswith("v1"):
                    expected = {key: record[key] for key in RECORD_KEYS_V1 if key != "alphabet"}
                    reject(actual != expected, f"exact replay mismatch for {record['alphabet']}")
                else:
                    for key in ("nodes", "leaves", "maximum_length", "maximizer_count"):
                        reject(actual[key] != record[key],
                               f"exact replay mismatch for {record['alphabet']}: {key}")
                    maximizer_bytes = json.dumps(
                        actual["maximizers"], separators=(",", ":")
                    ).encode()
                    actual_digest = hashlib.sha256(maximizer_bytes).hexdigest()
                    reject(actual_digest != record["maximizers_sha256"],
                           f"exact replay mismatch for {record['alphabet']}: maximizer digest")
                    reject(record["witness"] not in actual["maximizers"],
                           f"exact replay mismatch for {record['alphabet']}: witness")
        input_hash = hashlib.sha256(args.certificate.read_bytes()).hexdigest()
        code_hash = hashlib.sha256(CPP.read_bytes()).hexdigest()
        print(json.dumps({
            "status": "VERIFIED",
            "records": len(document["records"]),
            "certificate_sha256": input_hash,
            "verifier_cpp_sha256": code_hash,
        }, sort_keys=True))
        return 0
    except (ValueError, RuntimeError) as error:
        print(f"REJECTED: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
