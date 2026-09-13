#!/usr/bin/env python3
"""Build the compact exact fiber-enumeration manifest.

The program uses only integer arithmetic.  It is a certificate builder, not the
independent verifier; the latter reimplements the enumeration separately.
"""

import argparse
import hashlib
import json
import math
import struct
from collections import Counter, defaultdict
from pathlib import Path


def trim(poly):
    poly = list(poly)
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def quotient_exact(poly, divisor):
    poly = trim(poly)
    divisor = trim(divisor)
    if divisor[-1] != 1:
        raise RuntimeError("non-monic divisor")
    result = [0] * (len(poly) - len(divisor) + 1)
    for shift in range(len(result) - 1, -1, -1):
        lead = poly[shift + len(divisor) - 1]
        result[shift] = lead
        for index, coefficient in enumerate(divisor):
            poly[shift + index] -= lead * coefficient
    if any(poly):
        raise RuntimeError("inexact division")
    return trim(result)


def divisors(number):
    return [value for value in range(1, number + 1) if number % value == 0]


def cyclotomic(number):
    known = {}
    for value in divisors(number):
        poly = [-1] + [0] * (value - 1) + [1]
        for proper in divisors(value)[:-1]:
            poly = quotient_exact(poly, known[proper])
        known[value] = poly
    return known[number]


def columns(number, phi):
    degree = len(phi) - 1
    answer = []
    for exponent in range(number):
        vector = [0] * degree
        if exponent < degree:
            vector[exponent] = 1
        else:
            for index, coefficient in enumerate(phi[:-1]):
                for row, entry in enumerate(answer[exponent - degree + index]):
                    vector[row] -= coefficient * entry
        answer.append(tuple(vector))
    return answer


def subset_values(column_vectors):
    zero = (0,) * len(column_vectors[0])
    values = [zero]
    for vector in column_vectors:
        values += [tuple(a + b for a, b in zip(old, vector)) for old in values]
    return values


def orbit(subset, number):
    return {
        tuple(sorted((a + u * exponent) % number for exponent in subset))
        for a in range(number)
        for u in range(number)
        if math.gcd(u, number) == 1
    }


def pair_map():
    mapping = {}
    for exponent in range(105):
        pair = (exponent % 7, (-2 * exponent) % 15)
        if pair in mapping:
            raise RuntimeError("CRT map is not injective")
        mapping[pair] = exponent
    if len(mapping) != 105:
        raise RuntimeError("CRT map is not surjective")
    return mapping


def bits_to_subset(bits):
    subset = []
    while bits:
        low = bits & -bits
        subset.append(low.bit_length() - 1)
        bits ^= low
    return subset


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()
    certificate = json.loads(args.certificate.read_text(encoding="utf-8"))

    phi15 = cyclotomic(15)
    cols15 = columns(15, phi15)
    values = subset_values(cols15)
    groups = defaultdict(list)
    for mask, value in enumerate(values):
        groups[value].append(mask)
    for masks in groups.values():
        masks.sort()

    all_blockers = set()
    image_to_orbit = {}
    orbit_sizes = []
    for orbit_index, record in enumerate(certificate["representatives"]):
        images = orbit(tuple(record["subset"]), 105)
        if len(images) != record["orbit_size"]:
            raise RuntimeError("orbit size mismatch")
        orbit_sizes.append(len(images))
        for image in images:
            if image in image_to_orbit:
                raise RuntimeError("listed affine orbits overlap")
            image_to_orbit[image] = orbit_index
            all_blockers.add(image)
    ordered_blockers = sorted(all_blockers, key=lambda item: (len(item), item))
    blocker_bits = []
    blocker_orbit = []
    pair_index = defaultdict(list)
    for blocker_id, blocker in enumerate(ordered_blockers):
        bits = sum(1 << exponent for exponent in blocker)
        blocker_bits.append(bits)
        blocker_orbit.append(image_to_orbit[blocker])
        pair_index[blocker[:2]].append(blocker_id)

    exponent_for_pair = pair_map()
    fiber_bits = []
    for fiber in range(7):
        row = [0] * (1 << 15)
        for mask in range(1, 1 << 15):
            low = mask & -mask
            bit = low.bit_length() - 1
            row[mask] = row[mask ^ low] | (1 << exponent_for_pair[fiber, bit])
        fiber_bits.append(row)

    tuple_digest = hashlib.sha256()
    witness_digest = hashlib.sha256()
    count_by_weight = Counter()
    count_by_witness_orbit = Counter()
    tuple_count = 0
    unblocked = 0

    def consume(masks, total_weight):
        nonlocal tuple_count, unblocked
        tuple_count += 1
        count_by_weight[total_weight] += 1
        tuple_digest.update(struct.pack(">7H", *masks))
        bits = 0
        for fiber, mask in enumerate(masks):
            bits |= fiber_bits[fiber][mask]
        subset = bits_to_subset(bits)
        if len(subset) != total_weight or 0 not in subset:
            raise RuntimeError("tuple reconstruction failed")
        first_witness = None
        for left in range(len(subset)):
            for right in range(left + 1, len(subset)):
                for blocker_id in pair_index.get((subset[left], subset[right]), ()):
                    if first_witness is not None and blocker_id >= first_witness:
                        continue
                    blocker = blocker_bits[blocker_id]
                    if bits & blocker == blocker:
                        first_witness = blocker_id
        if first_witness is None:
            unblocked += 1
            witness_digest.update(struct.pack(">H", 65535))
        else:
            witness_digest.update(struct.pack(">H", first_witness))
            count_by_witness_orbit[blocker_orbit[first_witness]] += 1

    for value in sorted(groups):
        masks = groups[value]
        first_masks = [mask for mask in masks if mask & 1]
        if not first_masks:
            continue
        weights = {mask: mask.bit_count() for mask in masks}
        minimum = min(weights.values())
        chosen = [0] * 7

        def extend(position, running_weight):
            if position == 7:
                consume(tuple(chosen), running_weight)
                return
            remaining_after = 6 - position
            for mask in masks:
                new_weight = running_weight + weights[mask]
                if new_weight + remaining_after * minimum > 20:
                    continue
                chosen[position] = mask
                extend(position + 1, new_weight)

        for first in first_masks:
            first_weight = weights[first]
            if first_weight + 6 * minimum > 20:
                continue
            chosen[0] = first
            extend(1, first_weight)

    group_histogram = Counter(len(masks) for masks in groups.values())
    manifest = {
        "schema": "minimal105-fiber-enumeration-v1",
        "conductor": 105,
        "weight_bound": 20,
        "fiber_prime": 7,
        "base_conductor": 15,
        "root_decomposition": "zeta_105 = zeta_7 * zeta_15^(-2)",
        "phi_15": phi15,
        "fiber_mask_count": len(values),
        "distinct_fiber_values": len(groups),
        "fiber_value_group_size_histogram": {str(size): group_histogram[size] for size in sorted(group_histogram)},
        "maximum_fiber_value_group_size": max(map(len, groups.values())),
        "affine_blocker_count": len(ordered_blockers),
        "representative_orbit_sizes": orbit_sizes,
        "normalized_vanishing_tuple_count": tuple_count,
        "tuple_count_by_weight": {str(weight): count_by_weight[weight] for weight in sorted(count_by_weight)},
        "tuple_stream_sha256": tuple_digest.hexdigest(),
        "blocker_witness_stream_sha256": witness_digest.hexdigest(),
        "first_blocker_witness_count_by_representative": {
            str(index): count_by_witness_orbit[index]
            for index in range(len(certificate["representatives"]))
        },
        "unblocked_tuple_count": unblocked,
        "enumeration_order": "fiber value lexicographic; masks numeric; seven-mask tuple lexicographic subject to mask0 bit0=1 and total popcount<=20",
    }
    args.manifest.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps(manifest, sort_keys=True))


if __name__ == "__main__":
    main()
