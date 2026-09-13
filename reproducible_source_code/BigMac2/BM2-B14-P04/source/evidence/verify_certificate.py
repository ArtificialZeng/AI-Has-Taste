#!/usr/bin/env python3
"""Exact independent checker for the B_3 relative-dimension certificates.

This uses only Python's standard library.  It regenerates rather than trusts
the stored PLE list.  All arithmetic involving the covering dual uses
fractions.Fraction.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from fractions import Fraction
from itertools import permutations
from pathlib import Path


ELEMENTS = tuple(range(8))
EXPECTED_SOURCE_SHA256 = "a91b0542ab546f82a1c5bdfa5d81d1b62f0c112ef70504ffa677a98f556a98e8"


def strict_below(a: int, b: int) -> bool:
    return a != b and (a & b) == a


def is_ple(order: tuple[int, ...]) -> bool:
    if len(order) != len(set(order)) or any(x not in ELEMENTS for x in order):
        return False
    pos = {x: i for i, x in enumerate(order)}
    return all(not (strict_below(a, b) and pos[a] > pos[b]) for a in order for b in order)


def enumerate_orders(mask: int, prefix: tuple[int, ...] = ()):
    """All linear extensions of the subposet induced by exactly `mask`."""
    if mask == 0:
        yield prefix
        return
    minimal = []
    for x in ELEMENTS:
        if (mask >> x) & 1 and not any(
            (mask >> y) & 1 and strict_below(y, x) for y in ELEMENTS
        ):
            minimal.append(x)
    assert minimal
    for x in minimal:
        yield from enumerate_orders(mask ^ (1 << x), prefix + (x,))


def all_nonempty_ples() -> list[tuple[int, ...]]:
    return [p for mask in range(1, 1 << 8) for p in enumerate_orders(mask)]


def brute_force_ples() -> tuple[list[tuple[int, ...]], int]:
    """Independent domain enumeration by filtering every partial permutation."""
    candidates = 0
    result = []
    for size in range(1, 9):
        for order in permutations(ELEMENTS, size):
            candidates += 1
            if is_ple(order):
                result.append(order)
    return result, candidates


def all_requirements() -> set[tuple]:
    result = {("element", x) for x in ELEMENTS}
    for a in ELEMENTS:
        for b in range(a + 1, 8):
            if strict_below(a, b) or strict_below(b, a):
                result.add(("comparable", a, b))
            else:
                result.add(("orientation", a, b))
                result.add(("orientation", b, a))
    return result


def covers(order: tuple[int, ...], req: tuple) -> bool:
    pos = {x: i for i, x in enumerate(order)}
    kind = req[0]
    if kind == "element":
        return req[1] in pos
    if kind == "comparable":
        return req[1] in pos and req[2] in pos
    if kind == "orientation":
        return req[1] in pos and req[2] in pos and pos[req[1]] < pos[req[2]]
    raise AssertionError(f"unknown requirement kind: {kind}")


def read_fraction(record: dict) -> Fraction:
    return Fraction(int(record["numerator"]), int(record["denominator"]))


def validate_upper(witness: list[list[int]], requirements: set[tuple]) -> dict:
    ples = [tuple(p) for p in witness]
    assert all(is_ple(p) for p in ples), "upper witness contains a non-PLE"
    missing = sorted(req for req in requirements if not any(covers(p, req) for p in ples))
    assert not missing, f"upper witness misses requirements: {missing}"
    return {"orders": [list(p) for p in ples], "cost": sum(map(len, ples))}


def validate_dual(cert: dict, requirements: set[tuple], ples: list[tuple[int, ...]]) -> dict:
    weights: dict[tuple, Fraction] = {}
    for record in cert["nonzero_weights"]:
        req = tuple(record["requirement"])
        assert req in requirements, f"invalid requirement in dual: {req}"
        assert req not in weights, f"duplicate requirement in dual: {req}"
        value = read_fraction(record["weight"])
        assert value > 0, f"listed weight is not positive: {req}"
        weights[req] = value
    claimed = read_fraction(cert["claimed_dual_value"])
    actual = sum(weights.values(), Fraction())
    assert actual == claimed, f"dual weights sum to {actual}, not {claimed}"

    slack_histogram: Counter[str] = Counter()
    tight = 0
    worst_load = Fraction()
    worst_orders: list[list[int]] = []
    maximum_reversed_complement_count = 0
    for order in [()] + ples:
        load = sum((weight for req, weight in weights.items() if covers(order, req)), Fraction())
        present = set(order)
        s = len(present & {1, 2, 4})
        d = len(present & {3, 5, 6})
        e = len(present & {0, 7})
        pos = {x: i for i, x in enumerate(order)}
        q = sum(a in pos and b in pos and pos[a] < pos[b] for a, b in ((6, 1), (5, 2), (3, 4)))
        maximum_reversed_complement_count = max(maximum_reversed_complement_count, q)
        assert q <= 1, f"two reversed complementary pairs occur in PLE {order}"
        formula = Fraction(e * d, 3) + Fraction(2, 3) * (
            s * (s - 1) // 2 + d * (d - 1) // 2
        ) + 2 * q
        assert load == formula, f"certificate does not match analytic load formula on {order}"
        slack = Fraction(len(order)) - load
        assert slack >= 0, f"dual inequality fails for {order}: load={load}, cost={len(order)}"
        slack_histogram[str(slack)] += 1
        if slack == 0:
            tight += 1
        if load > worst_load:
            worst_load = load
            worst_orders = [list(order)]
        elif load == worst_load:
            worst_orders.append(list(order))
    return {
        "value": str(actual),
        "nonzero_weight_count": len(weights),
        "constraints_checked_including_empty": len(ples) + 1,
        "tight_constraint_count": tight,
        "maximum_reversed_complement_count": maximum_reversed_complement_count,
        "slack_histogram": dict(sorted(slack_histogram.items())),
        "maximum_dual_load": str(worst_load),
        "orders_at_maximum_dual_load": worst_orders,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    project = args.project.resolve()
    certificate = args.certificate or project / "evidence" / "dual_certificate.json"
    source_digest = hashlib.sha256((project / "source.md").read_bytes()).hexdigest()
    assert source_digest == EXPECTED_SOURCE_SHA256, "immutable source.md has changed"
    cert = json.loads(certificate.read_text(encoding="utf-8"))
    assert cert["schema"] == "b3-relative-dimension-cover-dual-v1"

    requirements = all_requirements()
    assert len(requirements) == 45
    ples = all_nonempty_ples()
    assert len(ples) == 1323
    assert len(set(ples)) == len(ples)
    assert all(is_ple(p) for p in ples)
    brute_ples, partial_permutation_count = brute_force_ples()
    assert partial_permutation_count == 109600
    assert len(brute_ples) == len(set(brute_ples)) == 1323
    assert set(brute_ples) == set(ples), "the two independent PLE enumerations disagree"
    counts = Counter(map(len, ples))
    assert counts == {1: 8, 2: 37, 3: 114, 4: 240, 5: 348, 6: 336, 7: 192, 8: 48}

    upper = validate_upper(cert["upper_witness"], requirements)
    assert upper["cost"] == 16
    dual = validate_dual(cert, requirements, ples)
    assert dual["value"] == "16"
    report = {
        "status": "verified",
        "arithmetic": "exact rational",
        "source_sha256": source_digest,
        "ple_count": len(ples),
        "partial_permutations_checked_by_second_enumeration": partial_permutation_count,
        "independent_enumerations_match": True,
        "ple_counts_by_size": {str(k): counts[k] for k in sorted(counts)},
        "requirement_count": len(requirements),
        "upper_witness": upper,
        "covering_dual": dual,
        "conclusion": "minimum total element-occurrence cost is exactly 16; rdim(B_3)=2",
    }
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
