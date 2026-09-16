#!/usr/bin/env python3
"""Exact exhaustive signature join for the positive P4/Paw system through 61.

The two domains are enumerated in separate lexicographic passes.  Python
integers are arbitrary precision, and no pruning, randomness, or floating-point
arithmetic is used.  The JSON report is rewritten atomically after every layer
so an interrupted run still records its completed coverage.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from hashlib import sha256
import json
from math import comb
from pathlib import Path
import platform
import sys
from typing import Callable, Iterable


CODE_VERSION = "1.0.0"
MIN_SUM = 4
MAX_SUM = 61
SCRIPT_PATH = Path(__file__).resolve()
PROJECT_DIR = SCRIPT_PATH.parent.parent
OUTPUT_PATH = SCRIPT_PATH.parent / "signature_join_61.json"
SOURCE_PATH = PROJECT_DIR / "source.md"

Quadruple = tuple[int, int, int, int]
Signature = tuple[int, int, int, int]
Record = tuple[Quadruple, Signature]


def positive_quadruples(total: int) -> Iterable[Quadruple]:
    """Yield every ordered positive quadruple of the given sum, lexicographically."""
    for x0 in range(1, total - 2):
        for x1 in range(1, total - x0 - 1):
            for x2 in range(1, total - x0 - x1):
                x3 = total - x0 - x1 - x2
                yield (x0, x1, x2, x3)


def sigma_b(b: Quadruple) -> Signature:
    b0, b1, b2, b3 = b
    return (
        b0 + b1 + b2 + b3,
        3 * b0 * b1 - 5 * b0 * b3 + 3 * b1 * b2 + 3 * b2 * b3,
        8 * b0 * b3 * (b1 + b2),
        4 * b0 * b1 * b2 * b3,
    )


def sigma_a(a: Quadruple) -> Signature:
    a0, a1, a2, a3 = a
    return (
        a0 + a1 + a2 + a3,
        3 * (a0 * a1 + a0 * a2 + a0 * a3 + a1 * a2),
        2 * a1 * a2 * (a3 - 2 * a0),
        a0 * a1 * a2 * a3,
    )


def tuple_line(x: Quadruple) -> bytes:
    return (",".join(map(str, x)) + "\n").encode("ascii")


def record_line(record: Record) -> bytes:
    x, signature = record
    return (
        ",".join(map(str, x))
        + "|"
        + ",".join(map(str, signature))
        + "\n"
    ).encode("ascii")


def multiset_line(signature: Signature, multiplicity: int) -> bytes:
    return (
        ",".join(map(str, signature)) + "|" + str(multiplicity) + "\n"
    ).encode("ascii")


def match_line(match: dict[str, object]) -> bytes:
    return (
        ",".join(map(str, match["b"]))
        + "|"
        + ",".join(map(str, match["a"]))
        + "|"
        + ",".join(map(str, match["signature"]))
        + "\n"
    ).encode("ascii")


def build_side_records(
    total: int, signature_function: Callable[[Quadruple], Signature]
) -> tuple[list[Record], str]:
    records: list[Record] = []
    domain_hash = sha256()
    for x in positive_quadruples(total):
        domain_hash.update(tuple_line(x))
        records.append((x, signature_function(x)))
    return records, domain_hash.hexdigest()


def records_digest(records: list[Record]) -> str:
    digest = sha256()
    for record in records:
        digest.update(record_line(record))
    return digest.hexdigest()


def signature_multiset_digest(counter: Counter[Signature]) -> str:
    digest = sha256()
    for signature, multiplicity in sorted(counter.items()):
        digest.update(multiset_line(signature, multiplicity))
    return digest.hexdigest()


def matches_digest(matches: list[dict[str, object]]) -> str:
    digest = sha256()
    for match in matches:
        digest.update(match_line(match))
    return digest.hexdigest()


def orbit_key(b: Quadruple, a: Quadruple) -> tuple[Quadruple, Quadruple]:
    b_images = (b, (b[3], b[2], b[1], b[0]))
    a_images = (a, (a[0], a[2], a[1], a[3]))
    return min((bb, aa) for bb in b_images for aa in a_images)


def json_match(b: Quadruple, a: Quadruple, signature: Signature) -> dict[str, object]:
    return {"s": signature[0], "b": list(b), "a": list(a), "signature": list(signature)}


def atomic_write(report: dict[str, object]) -> None:
    temporary = OUTPUT_PATH.with_suffix(".json.tmp")
    temporary.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    temporary.replace(OUTPUT_PATH)


def initial_report() -> dict[str, object]:
    return {
        "schema": "p4-paw-exact-signature-join-v1",
        "code_version": CODE_VERSION,
        "program": str(SCRIPT_PATH.relative_to(PROJECT_DIR)),
        "program_sha256": sha256(SCRIPT_PATH.read_bytes()).hexdigest(),
        "source_sha256": sha256(SOURCE_PATH.read_bytes()).hexdigest(),
        "runtime": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
        },
        "arithmetic": "Python arbitrary-precision integers only",
        "randomness": "none",
        "domain": {
            "objects": "ordered quadruples in Z_{>0}^4",
            "minimum_sum": MIN_SUM,
            "maximum_sum": MAX_SUM,
            "enumeration_order": "lexicographic x0,x1,x2,x3, separately on each side",
            "pruning": "none",
            "expected_count_each_side": comb(MAX_SUM, 4),
        },
        "digest_contract": {
            "encoding": "ASCII",
            "tuple_records": "x0,x1,x2,x3\\n in enumeration order",
            "side_records": "x0,x1,x2,x3|s,c2,c3,c4\\n in enumeration order",
            "signature_multiset": "s,c2,c3,c4|multiplicity\\n in sorted-signature order",
            "matches": "b0,b1,b2,b3|a0,a1,a2,a3|s,c2,c3,c4\\n in sorted (b,a) order",
            "algorithm": "SHA-256",
        },
        "guard": {
            "purpose": "stop on any hit below 61 or any layer-61 orbit beyond the source orbit",
            "source_representative": {
                "b": [1, 16, 8, 36],
                "a": [4, 9, 16, 32],
            },
        },
        "status": "running",
        "completed_through": None,
        "first_matching_layer": None,
        "layers": [],
        "matches": [],
        "anomalies": [],
    }


def main() -> int:
    report = initial_report()
    atomic_write(report)

    source_b: Quadruple = (1, 16, 8, 36)
    source_a: Quadruple = (4, 9, 16, 32)
    expected_pairs = {
        (bb, aa)
        for bb in (source_b, (source_b[3], source_b[2], source_b[1], source_b[0]))
        for aa in (source_a, (source_a[0], source_a[2], source_a[1], source_a[3]))
    }
    expected_orbit = orbit_key(source_b, source_a)

    aggregate_a_records = sha256()
    aggregate_b_records = sha256()
    aggregate_a_domain = sha256()
    aggregate_b_domain = sha256()
    all_matches: list[dict[str, object]] = []
    total_a = 0
    total_b = 0

    for total in range(MIN_SUM, MAX_SUM + 1):
        # These are deliberately separate domain passes.
        a_records, a_domain_digest = build_side_records(total, sigma_a)
        b_records, b_domain_digest = build_side_records(total, sigma_b)
        expected_layer_count = comb(total - 1, 3)

        for record in a_records:
            aggregate_a_domain.update(tuple_line(record[0]))
            aggregate_a_records.update(record_line(record))
        for record in b_records:
            aggregate_b_domain.update(tuple_line(record[0]))
            aggregate_b_records.update(record_line(record))

        a_counter: Counter[Signature] = Counter(signature for _, signature in a_records)
        b_counter: Counter[Signature] = Counter(signature for _, signature in b_records)
        a_by_signature: defaultdict[Signature, list[Quadruple]] = defaultdict(list)
        for a, signature in a_records:
            a_by_signature[signature].append(a)

        layer_matches: list[dict[str, object]] = []
        for b, signature in b_records:
            for a in a_by_signature.get(signature, ()):
                layer_matches.append(json_match(b, a, signature))
        layer_matches.sort(key=lambda match: (match["b"], match["a"]))

        total_a += len(a_records)
        total_b += len(b_records)
        if layer_matches and report["first_matching_layer"] is None:
            report["first_matching_layer"] = total
        all_matches.extend(layer_matches)

        layer_orbits = sorted(
            {
                orbit_key(tuple(match["b"]), tuple(match["a"]))
                for match in layer_matches
            }
        )
        layer = {
            "s": total,
            "expected_domain_count_each_side": expected_layer_count,
            "a": {
                "domain_count": len(a_records),
                "domain_sha256": a_domain_digest,
                "distinct_signature_count": len(a_counter),
                "collision_excess": len(a_records) - len(a_counter),
                "records_sha256": records_digest(a_records),
                "signature_multiset_sha256": signature_multiset_digest(a_counter),
            },
            "b": {
                "domain_count": len(b_records),
                "domain_sha256": b_domain_digest,
                "distinct_signature_count": len(b_counter),
                "collision_excess": len(b_records) - len(b_counter),
                "records_sha256": records_digest(b_records),
                "signature_multiset_sha256": signature_multiset_digest(b_counter),
            },
            "match_count": len(layer_matches),
            "matches_sha256": matches_digest(layer_matches),
            "orbit_count_under_allowed_involutions": len(layer_orbits),
        }
        report["layers"].append(layer)
        report["completed_through"] = total
        report["matches"] = all_matches

        if (
            len(a_records) != expected_layer_count
            or len(b_records) != expected_layer_count
            or a_domain_digest != b_domain_digest
        ):
            report["anomalies"].append(
                {
                    "type": "coverage_failure",
                    "s": total,
                    "expected": expected_layer_count,
                    "a_actual": len(a_records),
                    "b_actual": len(b_records),
                }
            )
            report["status"] = "anomaly"
            atomic_write(report)
            return 2

        if layer_matches and total < MAX_SUM:
            report["anomalies"].append(
                {"type": "unexpected_match_below_61", "s": total, "matches": layer_matches}
            )
            report["status"] = "anomaly"
            atomic_write(report)
            return 2

        if total == MAX_SUM and any(key != expected_orbit for key in layer_orbits):
            report["anomalies"].append(
                {
                    "type": "unexpected_orbit_at_61",
                    "orbit_keys": [
                        {"b": list(key[0]), "a": list(key[1])} for key in layer_orbits
                    ],
                }
            )
            report["status"] = "anomaly"
            atomic_write(report)
            return 2

        atomic_write(report)

    actual_pairs = {(tuple(match["b"]), tuple(match["a"])) for match in all_matches}
    if actual_pairs != expected_pairs:
        report["anomalies"].append(
            {
                "type": "known_orbit_mismatch_at_61",
                "expected_pairs": [
                    {"b": list(b), "a": list(a)} for b, a in sorted(expected_pairs)
                ],
                "actual_pairs": [
                    {"b": list(b), "a": list(a)} for b, a in sorted(actual_pairs)
                ],
            }
        )

    expected_total = comb(MAX_SUM, 4)
    if total_a != expected_total or total_b != expected_total:
        report["anomalies"].append(
            {
                "type": "aggregate_coverage_failure",
                "expected_each_side": expected_total,
                "a_actual": total_a,
                "b_actual": total_b,
            }
        )

    report["aggregate"] = {
        "a_domain_count": total_a,
        "b_domain_count": total_b,
        "a_domain_sha256": aggregate_a_domain.hexdigest(),
        "b_domain_sha256": aggregate_b_domain.hexdigest(),
        "a_records_sha256": aggregate_a_records.hexdigest(),
        "b_records_sha256": aggregate_b_records.hexdigest(),
        "match_count": len(all_matches),
        "matches_sha256": matches_digest(all_matches),
        "expected_domain_identity": "sum_{s=4}^{61} binom(s-1,3) = binom(61,4)",
    }
    report["classification"] = {
        "ordered_match_count_at_first_layer": len(all_matches),
        "allowed_orbit_count_at_first_layer": len(
            {orbit_key(tuple(match["b"]), tuple(match["a"])) for match in all_matches}
        ),
        "allowed_orbit_representatives": [
            {"b": list(key[0]), "a": list(key[1])}
            for key in sorted(
                {orbit_key(tuple(match["b"]), tuple(match["a"])) for match in all_matches}
            )
        ],
    }
    report["status"] = "complete" if not report["anomalies"] else "anomaly"
    atomic_write(report)
    return 0 if report["status"] == "complete" else 2


if __name__ == "__main__":
    sys.exit(main())
