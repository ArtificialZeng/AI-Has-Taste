#!/usr/bin/env python3
"""Independent fail-closed verifier for the conductor-105 weight-20 result.

This program uses only the Python standard library.  It does not import the
Z3 discovery program or the certificate builder.  It reconstructs all exact
cyclotomic data, checks the displayed representatives, and independently
replays the complete seven-fiber enumeration recorded by the manifest.
"""

import argparse
import hashlib
import json
import math
import re
import struct
import sys
from collections import Counter, defaultdict
from pathlib import Path


class VerificationError(Exception):
    """Raised whenever serialized or recomputed evidence fails a check."""


def require(condition, message):
    if not condition:
        raise VerificationError(message)


def require_keys(value, expected, label):
    require(isinstance(value, dict), f"{label} must be an object")
    require(set(value) == set(expected), f"{label} has missing or unknown fields")


def digest_text(value, label):
    require(isinstance(value, str), f"{label} must be text")
    require(re.fullmatch(r"[0-9a-f]{64}", value) is not None, f"bad {label}")


def safe_sibling(name, base=None):
    """Resolve one plain filename beside the verifier; reject traversal."""
    require(isinstance(name, str) and name, "artifact path must be nonempty text")
    candidate = Path(name)
    require(not candidate.is_absolute(), "absolute artifact path rejected")
    require(len(candidate.parts) == 1 and candidate.name == name, "path traversal rejected")
    require(name not in (".", ".."), "invalid artifact filename")
    directory = Path(__file__).resolve().parent if base is None else Path(base).resolve()
    resolved = (directory / name).resolve()
    require(resolved.parent == directory, "artifact escaped certificate directory")
    return resolved


def trim(poly):
    answer = list(poly)
    while len(answer) > 1 and answer[-1] == 0:
        answer.pop()
    return answer


def monic_divide(dividend, divisor):
    work = trim(dividend)
    divisor = trim(divisor)
    require(divisor and divisor[-1] == 1, "cyclotomic divisor is not monic")
    require(len(work) >= len(divisor), "cyclotomic degree underflow")
    quotient = [0] * (len(work) - len(divisor) + 1)
    for shift in range(len(quotient) - 1, -1, -1):
        lead = work[shift + len(divisor) - 1]
        quotient[shift] = lead
        for index, coefficient in enumerate(divisor):
            work[shift + index] -= lead * coefficient
    require(not any(work), "inexact cyclotomic division")
    return trim(quotient)


def divisors(number):
    return [candidate for candidate in range(1, number + 1) if number % candidate == 0]


def cyclotomic(number):
    known = {}
    for value in divisors(number):
        polynomial = [-1] + [0] * (value - 1) + [1]
        for proper in divisors(value)[:-1]:
            polynomial = monic_divide(polynomial, known[proper])
        known[value] = polynomial
    return known[number]


def residue_columns(number, phi):
    degree = len(phi) - 1
    answer = []
    for exponent in range(number):
        vector = [0] * degree
        if exponent < degree:
            vector[exponent] = 1
        else:
            for offset, coefficient in enumerate(phi[:-1]):
                source = answer[exponent - degree + offset]
                for row in range(degree):
                    vector[row] -= coefficient * source[row]
        answer.append(tuple(vector))
    return answer


def vector_sum(subset, columns):
    return tuple(sum(columns[index][row] for index in subset) for row in range(len(columns[0])))


def affine_orbit(subset, number=105):
    units = (unit for unit in range(number) if math.gcd(unit, number) == 1)
    return {
        tuple(sorted((translation + unit * exponent) % number for exponent in subset))
        for unit in units
        for translation in range(number)
    }


def subset_sum_table(vectors):
    zero = (0,) * len(vectors[0])
    table = [zero]
    for vector in vectors:
        table.extend(tuple(a + b for a, b in zip(old, vector)) for old in tuple(table))
    return table


def inclusion_minimal(subset, columns):
    """Meet-in-the-middle exact test of every nonempty proper subset."""
    middle = len(subset) // 2
    left = subset_sum_table([columns[index] for index in subset[:middle]])
    right = subset_sum_table([columns[index] for index in subset[middle:]])
    right_masks = defaultdict(list)
    for mask, value in enumerate(right):
        right_masks[value].append(mask)
    left_full = (1 << middle) - 1
    right_full = (1 << (len(subset) - middle)) - 1
    for left_mask, value in enumerate(left):
        opposite = tuple(-entry for entry in value)
        for right_mask in right_masks.get(opposite, ()):
            empty = left_mask == 0 and right_mask == 0
            full = left_mask == left_full and right_mask == right_full
            if not empty and not full:
                return False
    return True


def validate_serialized_certificate(certificate):
    require_keys(
        certificate,
        {
            "schema", "conductor", "maximum_certified_weight", "equivalence",
            "claim", "matrix_sha256", "representatives", "finite_enumeration",
        },
        "certificate",
    )
    require(certificate["schema"] == "minimal105-weight20-fiber-certificate-v1", "bad schema")
    require(certificate["conductor"] == 105, "bad conductor")
    require(certificate["maximum_certified_weight"] == 20, "bad weight bound")
    require(certificate["equivalence"] == "S -> a + uS, a in Z/105Z, gcd(u,105)=1", "bad equivalence")
    require(isinstance(certificate["claim"], str) and certificate["claim"], "bad claim")
    digest_text(certificate["matrix_sha256"], "matrix digest")

    records = certificate["representatives"]
    require(isinstance(records, list) and len(records) == 9, "expected nine representatives")
    previous = None
    for index, record in enumerate(records):
        require_keys(record, {"weight", "subset", "orbit_size", "stabilizer_size"}, f"representative {index}")
        subset = record["subset"]
        require(isinstance(record["weight"], int), "noninteger weight")
        require(isinstance(subset, list) and subset, "bad subset")
        require(all(isinstance(x, int) and not isinstance(x, bool) for x in subset), "noninteger exponent")
        require(subset == sorted(set(subset)), "subset is not strictly sorted")
        require(all(0 <= x < 105 for x in subset), "exponent outside Z/105Z")
        require(subset[0] == 0, "representative is not translation-normalized")
        require(record["weight"] == len(subset), "weight mismatch")
        require(record["weight"] <= 20, "representative exceeds bound")
        require(isinstance(record["orbit_size"], int) and record["orbit_size"] > 0, "bad orbit size")
        require(isinstance(record["stabilizer_size"], int) and record["stabilizer_size"] > 0, "bad stabilizer")
        key = (record["weight"], tuple(subset))
        require(previous is None or previous < key, "representatives not strictly ordered")
        previous = key
    require([r["weight"] for r in records].count(20) == 2, "expected exactly two weight-20 records")

    finite = certificate["finite_enumeration"]
    require_keys(finite, {"path", "sha256", "verifier", "method"}, "finite_enumeration")
    safe_sibling(finite["path"])
    require(finite["verifier"] == Path(__file__).name, "wrong verifier binding")
    digest_text(finite["sha256"], "manifest digest")
    require(isinstance(finite["method"], str) and finite["method"], "bad method")
    return certificate


def validate_manifest_shape(manifest):
    require_keys(
        manifest,
        {
            "schema", "conductor", "weight_bound", "fiber_prime", "base_conductor",
            "root_decomposition", "phi_15", "fiber_mask_count", "distinct_fiber_values",
            "fiber_value_group_size_histogram", "maximum_fiber_value_group_size",
            "affine_blocker_count", "representative_orbit_sizes",
            "normalized_vanishing_tuple_count", "tuple_count_by_weight",
            "tuple_stream_sha256", "blocker_witness_stream_sha256",
            "first_blocker_witness_count_by_representative", "unblocked_tuple_count",
            "enumeration_order",
        },
        "manifest",
    )
    require(manifest["schema"] == "minimal105-fiber-enumeration-v1", "bad manifest schema")
    require(manifest["conductor"] == 105 and manifest["weight_bound"] == 20, "bad manifest scope")
    require(manifest["fiber_prime"] == 7 and manifest["base_conductor"] == 15, "bad fiber split")
    digest_text(manifest["tuple_stream_sha256"], "tuple stream digest")
    digest_text(manifest["blocker_witness_stream_sha256"], "witness stream digest")


def gray_subset_values(columns):
    """Compute all mask values by a Gray walk (different from the builder DP)."""
    dimension = len(columns[0])
    answer = [None] * (1 << len(columns))
    current = [0] * dimension
    answer[0] = tuple(current)
    previous = 0
    for step in range(1, 1 << len(columns)):
        mask = step ^ (step >> 1)
        changed = mask ^ previous
        position = changed.bit_length() - 1
        sign = 1 if mask & changed else -1
        for row, entry in enumerate(columns[position]):
            current[row] += sign * entry
        answer[mask] = tuple(current)
        previous = mask
    require(all(item is not None for item in answer), "Gray walk missed a mask")
    return answer


def exponent_pair_inverse():
    mapping = {}
    for exponent in range(105):
        key = (exponent % 7, (-2 * exponent) % 15)
        require(key not in mapping, "CRT coordinate collision")
        mapping[key] = exponent
    require(len(mapping) == 105, "CRT coordinate map is incomplete")
    return mapping


def bits_to_sorted_list(bits):
    answer = []
    while bits:
        low = bits & -bits
        answer.append(low.bit_length() - 1)
        bits ^= low
    return answer


def replay_fiber_enumeration(records, orbit_sets):
    phi15 = cyclotomic(15)
    columns15 = residue_columns(15, phi15)
    values = gray_subset_values(columns15)
    groups = defaultdict(list)
    for mask in range(1 << 15):
        groups[values[mask]].append(mask)

    image_owner = {}
    for record_index, images in enumerate(orbit_sets):
        for image in images:
            require(image not in image_owner, "listed representative orbits overlap")
            image_owner[image] = record_index
    blockers = sorted(image_owner, key=lambda item: (len(item), item))
    require(len(blockers) == 1331, "unexpected number of affine blockers")
    blocker_bits = [sum(1 << exponent for exponent in blocker) for blocker in blockers]
    blocker_owner = [image_owner[blocker] for blocker in blockers]

    # Index each blocker by its two least exponents.  If it is contained in a
    # candidate, that pair necessarily occurs in the candidate.
    pair_candidates = defaultdict(list)
    for blocker_id, blocker in enumerate(blockers):
        require(len(blocker) >= 2, "degenerate blocker")
        pair_candidates[(blocker[0], blocker[1])].append(blocker_id)

    inverse = exponent_pair_inverse()
    fiber_bits = []
    for fiber in range(7):
        row = [0] * (1 << 15)
        singleton = [1 << inverse[fiber, residue] for residue in range(15)]
        for mask in range(1, 1 << 15):
            low = mask & -mask
            row[mask] = row[mask ^ low] | singleton[low.bit_length() - 1]
        fiber_bits.append(row)

    tuple_hash = hashlib.sha256()
    witness_hash = hashlib.sha256()
    by_weight = Counter()
    by_owner = Counter()
    total = 0
    unblocked = 0

    def consume(chosen, weight):
        nonlocal total, unblocked
        total += 1
        by_weight[weight] += 1
        tuple_hash.update(struct.pack(">7H", *chosen))
        candidate_bits = 0
        for fiber, mask in enumerate(chosen):
            candidate_bits |= fiber_bits[fiber][mask]
        subset = bits_to_sorted_list(candidate_bits)
        require(len(subset) == weight and subset and subset[0] == 0, "fiber reconstruction failure")

        possible = set()
        for left in range(len(subset)):
            for right in range(left + 1, len(subset)):
                possible.update(pair_candidates.get((subset[left], subset[right]), ()))
        witness = None
        for blocker_id in sorted(possible):
            blocker = blocker_bits[blocker_id]
            if candidate_bits & blocker == blocker:
                witness = blocker_id
                break
        if witness is None:
            unblocked += 1
            witness_hash.update(struct.pack(">H", 65535))
        else:
            witness_hash.update(struct.pack(">H", witness))
            by_owner[blocker_owner[witness]] += 1

    for value in sorted(groups):
        masks = groups[value]
        first_masks = [mask for mask in masks if mask & 1]
        if not first_masks:
            continue
        weights = {mask: mask.bit_count() for mask in masks}
        minimum = min(weights.values())
        chosen = [0] * 7

        def visit(position, running_weight):
            if position == 7:
                consume(tuple(chosen), running_weight)
                return
            remaining = 6 - position
            for mask in masks:
                new_weight = running_weight + weights[mask]
                if new_weight + remaining * minimum <= 20:
                    chosen[position] = mask
                    visit(position + 1, new_weight)

        for first in first_masks:
            first_weight = weights[first]
            if first_weight + 6 * minimum <= 20:
                chosen[0] = first
                visit(1, first_weight)

    histogram = Counter(len(masks) for masks in groups.values())
    return {
        "schema": "minimal105-fiber-enumeration-v1",
        "conductor": 105,
        "weight_bound": 20,
        "fiber_prime": 7,
        "base_conductor": 15,
        "root_decomposition": "zeta_105 = zeta_7 * zeta_15^(-2)",
        "phi_15": phi15,
        "fiber_mask_count": len(values),
        "distinct_fiber_values": len(groups),
        "fiber_value_group_size_histogram": {str(size): histogram[size] for size in sorted(histogram)},
        "maximum_fiber_value_group_size": max(map(len, groups.values())),
        "affine_blocker_count": len(blockers),
        "representative_orbit_sizes": [len(images) for images in orbit_sets],
        "normalized_vanishing_tuple_count": total,
        "tuple_count_by_weight": {str(weight): by_weight[weight] for weight in sorted(by_weight)},
        "tuple_stream_sha256": tuple_hash.hexdigest(),
        "blocker_witness_stream_sha256": witness_hash.hexdigest(),
        "first_blocker_witness_count_by_representative": {
            str(index): by_owner[index] for index in range(len(records))
        },
        "unblocked_tuple_count": unblocked,
        "enumeration_order": "fiber value lexicographic; masks numeric; seven-mask tuple lexicographic subject to mask0 bit0=1 and total popcount<=20",
    }


def verify(certificate_path):
    certificate_path = Path(certificate_path).resolve()
    certificate = validate_serialized_certificate(json.loads(certificate_path.read_text(encoding="utf-8")))
    finite = certificate["finite_enumeration"]
    manifest_path = safe_sibling(finite["path"], certificate_path.parent)
    require(manifest_path.is_file(), "enumeration manifest missing")
    manifest_bytes = manifest_path.read_bytes()
    actual_manifest_hash = hashlib.sha256(manifest_bytes).hexdigest()
    require(actual_manifest_hash == finite["sha256"], "enumeration manifest digest mismatch")
    manifest = json.loads(manifest_bytes)
    validate_manifest_shape(manifest)

    phi105 = cyclotomic(105)
    require(len(phi105) - 1 == 48, "unexpected degree of Phi_105")
    columns105 = residue_columns(105, phi105)
    matrix_encoding = json.dumps(columns105, separators=(",", ":")).encode()
    matrix_hash = hashlib.sha256(matrix_encoding).hexdigest()
    require(matrix_hash == certificate["matrix_sha256"], "cyclotomic matrix digest mismatch")

    records = certificate["representatives"]
    orbit_sets = []
    for index, record in enumerate(records):
        subset = tuple(record["subset"])
        require(not any(vector_sum(subset, columns105)), f"representative {index} does not vanish")
        require(inclusion_minimal(subset, columns105), f"representative {index} is not minimal")
        images = affine_orbit(subset)
        require(len(images) == record["orbit_size"], f"orbit size mismatch at representative {index}")
        require(5040 // len(images) == record["stabilizer_size"], f"stabilizer mismatch at representative {index}")
        require(min(images) == subset, f"representative {index} is not affine-canonical")
        orbit_sets.append(images)

    rebuilt = replay_fiber_enumeration(records, orbit_sets)
    require(rebuilt == manifest, "independent fiber enumeration differs from manifest")
    require(rebuilt["unblocked_tuple_count"] == 0, "an unblocked vanishing subset exists")
    return {
        "status": "VERIFIED",
        "certificate": str(certificate_path),
        "matrix_sha256": matrix_hash,
        "manifest_sha256": actual_manifest_hash,
        "normalized_vanishing_tuple_count": rebuilt["normalized_vanishing_tuple_count"],
        "affine_blocker_count": rebuilt["affine_blocker_count"],
        "unblocked_tuple_count": 0,
        "weight_20_representatives": [record["subset"] for record in records if record["weight"] == 20],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", nargs="?", type=Path, default=Path(__file__).with_name("weight20_certificate.json"))
    args = parser.parse_args()
    try:
        result = verify(args.certificate)
    except (VerificationError, OSError, UnicodeError, json.JSONDecodeError, struct.error) as error:
        print(f"VERIFICATION FAILED: {error}", file=sys.stderr)
        raise SystemExit(1)
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
