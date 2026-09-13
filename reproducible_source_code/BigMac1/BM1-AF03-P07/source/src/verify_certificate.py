#!/usr/bin/env python3
"""Fail-closed driver for the no-import independent C++ verifier."""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import subprocess
import sys
from typing import Any


class Rejected(ValueError):
    pass


def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise Rejected(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def exact_keys(obj: dict[str, Any], keys: set[str], where: str) -> None:
    if set(obj) != keys:
        raise Rejected(
            f"{where} keys differ: missing={sorted(keys-set(obj))}, "
            f"extra={sorted(set(obj)-keys)}"
        )


def integer(value: Any, where: str, minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:
        raise Rejected(f"{where} must be an integer >= {minimum}")
    return value


def sha256(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_certificate(path: pathlib.Path) -> dict[str, Any]:
    try:
        cert = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)
    except (OSError, UnicodeError, json.JSONDecodeError, Rejected) as exc:
        raise Rejected(f"certificate parse failed: {exc}") from exc
    if not isinstance(cert, dict):
        raise Rejected("certificate root must be an object")
    exact_keys(
        cert,
        {
            "schema_version",
            "theorem_endpoint",
            "algorithm",
            "max_n",
            "baselines",
            "n8_audit_counts",
            "required_result",
        },
        "certificate",
    )
    if integer(cert["schema_version"], "schema_version") != 1:
        raise Rejected("unsupported schema_version")
    expected_endpoint = (
        "Gaetz-et-al-Conjecture-7.6-for-initial-straight-increasing-tableaux-on-[n]"
    )
    if cert["theorem_endpoint"] != expected_endpoint:
        raise Rejected("theorem_endpoint mismatch")
    if cert["algorithm"] != "Gaetz-et-al-Algorithm-1-exact-finite-congruence-closure":
        raise Rejected("algorithm mismatch")
    if integer(cert["max_n"], "max_n") != 8:
        raise Rejected("only the audited max_n=8 endpoint is accepted")
    if cert["required_result"] != "CERTIFIED_FINITE_RESULT":
        raise Rejected("required_result mismatch")
    baselines = cert["baselines"]
    if not isinstance(baselines, list) or len(baselines) != 9:
        raise Rejected("baselines must contain exactly n=0,...,8")
    baseline_keys = {
        "n",
        "all_tableaux",
        "initial_tableaux",
        "initial_classes",
        "urts",
        "interval_complete",
    }
    for n, row in enumerate(baselines):
        if not isinstance(row, dict):
            raise Rejected(f"baseline[{n}] must be an object")
        exact_keys(row, baseline_keys, f"baseline[{n}]")
        if integer(row["n"], f"baseline[{n}].n") != n:
            raise Rejected("baseline n values must be exactly 0,...,8 in order")
        for key in ("all_tableaux", "initial_tableaux", "initial_classes", "urts"):
            integer(row[key], f"baseline[{n}].{key}", 1)
        if type(row["interval_complete"]) is not bool or not row["interval_complete"]:
            raise Rejected(f"baseline[{n}] must claim interval_complete=true")
    audit = cert["n8_audit_counts"]
    if not isinstance(audit, dict):
        raise Rejected("n8_audit_counts must be an object")
    exact_keys(
        audit,
        {"primitive_rule_count", "primitive_tests", "closure_tests", "merges"},
        "n8_audit_counts",
    )
    for key, value in audit.items():
        integer(value, f"n8_audit_counts.{key}")
    return cert


def core_result(core: pathlib.Path, n: int) -> dict[str, Any]:
    completed = subprocess.run(
        [str(core), "--n", str(n)],
        text=True,
        capture_output=True,
        check=False,
    )
    if completed.returncode != 0:
        raise Rejected(
            f"verifier core failed for n={n}, exit={completed.returncode}: "
            f"{completed.stderr.strip()}"
        )
    try:
        result = json.loads(completed.stdout, object_pairs_hook=unique_object)
    except (json.JSONDecodeError, Rejected) as exc:
        raise Rejected(f"invalid core JSON for n={n}: {exc}") from exc
    if not isinstance(result, dict):
        raise Rejected("core output must be an object")
    exact_keys(
        result,
        {
            "n",
            "all_tableaux",
            "initial_tableaux",
            "initial_classes",
            "urts",
            "primitive_rule_count",
            "primitive_tests",
            "closure_tests",
            "merges",
            "interval_complete",
            "seconds",
        },
        f"core result n={n}",
    )
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=pathlib.Path, required=True)
    parser.add_argument("--core", type=pathlib.Path, required=True)
    parser.add_argument("--core-source", type=pathlib.Path, required=True)
    parser.add_argument("--only-n", type=int, choices=range(9))
    args = parser.parse_args()
    try:
        cert = load_certificate(args.certificate)
        if not args.core.is_file() or not args.core_source.is_file():
            raise Rejected("core binary/source is missing")
        ns = [args.only_n] if args.only_n is not None else list(range(9))
        for n in ns:
            result = core_result(args.core.resolve(), n)
            expected = cert["baselines"][n]
            for key in (
                "n",
                "all_tableaux",
                "initial_tableaux",
                "initial_classes",
                "urts",
                "interval_complete",
            ):
                if result[key] != expected[key]:
                    raise Rejected(
                        f"n={n} mismatch for {key}: computed={result[key]!r}, "
                        f"certificate={expected[key]!r}"
                    )
            if n == 8:
                for key, expected_value in cert["n8_audit_counts"].items():
                    if result[key] != expected_value:
                        raise Rejected(
                            f"n=8 audit mismatch for {key}: "
                            f"computed={result[key]!r}, certificate={expected_value!r}"
                        )
        print(
            "CERTIFIED_FINITE_RESULT",
            f"verified_n={','.join(map(str, ns))}",
            f"certificate_sha256={sha256(args.certificate)}",
            f"driver_sha256={sha256(pathlib.Path(__file__))}",
            f"core_source_sha256={sha256(args.core_source)}",
            f"core_binary_sha256={sha256(args.core)}",
        )
        return 0
    except Rejected as exc:
        print(f"VERIFIER_REJECT: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
