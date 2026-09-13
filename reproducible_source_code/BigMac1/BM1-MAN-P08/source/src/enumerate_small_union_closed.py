#!/usr/bin/env python3
"""Exact census of labelled union-closed families on at most five points.

The five-point search never scans the 2^32 possible set families.  Write a
family on [5] as a pair (A,B), where A consists of the members avoiding point
5 and B consists of their traces after point 5 is removed.  Then

  F is union-closed  iff  A and B are union-closed and A vee B is in B.

There are only 4960 union-closed families on four labelled points.  Bitsets
encode, for each a, which choices of B are stable under b -> a union b.
All decisions and all reported statistics use integer arithmetic.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


def popcount(value: int) -> int:
    """Python-3.9-compatible population count."""

    return bin(value).count("1")


def members(family_mask: int) -> Iterable[int]:
    while family_mask:
        bit = family_mask & -family_mask
        yield bit.bit_length() - 1
        family_mask ^= bit


def is_union_closed(family_mask: int) -> bool:
    sets = list(members(family_mask))
    for left in sets:
        for right in sets:
            if not (family_mask & (1 << (left | right))):
                return False
    return True


def union_closed_families_on_four_points() -> List[int]:
    return [mask for mask in range(1 << 16) if is_union_closed(mask)]


def family_statistics_on_four(
    family_mask: int,
) -> Tuple[int, int, Tuple[int, ...], int]:
    count = 0
    support = 0
    frequencies = [0, 0, 0, 0]
    separated_pairs = 0
    for subset in members(family_mask):
        count += 1
        support |= subset
        for point in range(4):
            if subset & (1 << point):
                frequencies[point] += 1
        for left in range(4):
            for right in range(left + 1, 4):
                if bool(subset & (1 << left)) != bool(subset & (1 << right)):
                    separated_pairs |= 1 << (4 * left + right)
    return count, support, tuple(frequencies), separated_pairs


def stable_upper_choices(uc4: Sequence[int]) -> List[int]:
    """Return a 4960-bit eligibility vector for each lower subset a."""

    flags: List[int] = []
    for lower_subset in range(16):
        eligible = 0
        for index, upper_family in enumerate(uc4):
            stable = True
            for upper_subset in members(upper_family):
                if not (upper_family & (1 << (lower_subset | upper_subset))):
                    stable = False
                    break
            if stable:
                eligible |= 1 << index
        flags.append(eligible)
    return flags


def decode_five_point_family(lower_family: int, upper_family: int) -> Tuple[int, ...]:
    result = list(members(lower_family))
    result.extend(subset | 16 for subset in members(upper_family))
    return tuple(sorted(result))


def serialise_family(subsets: Sequence[int], points: int = 5) -> List[List[int]]:
    return [
        [point + 1 for point in range(points) if subset & (1 << point)]
        for subset in subsets
    ]


def witness_record(
    lower_index: int,
    upper_index: int,
    lower_family: int,
    upper_family: int,
    size: int,
    frequencies: Sequence[int],
    support: int,
    value: int,
) -> Dict[str, object]:
    active_frequencies = [frequencies[i] for i in range(5) if support & (1 << i)]
    return {
        "lower_index": lower_index,
        "upper_index": upper_index,
        "family_size": size,
        "support_size": popcount(support),
        "frequencies": list(frequencies),
        "active_frequencies": active_frequencies,
        "weight_value": value,
        "members": serialise_family(
            decode_five_point_family(lower_family, upper_family)
        ),
    }


def twin_class_frequencies(
    support: int,
    frequencies: Sequence[int],
    separated_pairs: int,
    lower_support: int,
    upper_count: int,
    upper_frequencies: Sequence[int],
) -> List[int]:
    """One frequency for each nonempty incidence-column equivalence class."""

    def separated(left: int, right: int) -> bool:
        if right < 4:
            return bool(separated_pairs & (1 << (4 * left + right)))
        # Point 5 is absent below and present above.  It differs from point i
        # iff some lower member contains i or some upper trace avoids i.
        return bool(lower_support & (1 << left)) or upper_count > upper_frequencies[left]

    representatives: List[int] = []
    for point in range(5):
        if not (support & (1 << point)):
            continue
        if any(not separated(rep, point) for rep in representatives):
            continue
        representatives.append(point)
    return [frequencies[point] for point in representatives]


def brute_counts_through_four() -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for points in range(5):
        subset_count = 1 << points
        count = 0
        for family_mask in range(1 << subset_count):
            if is_union_closed(family_mask):
                count += 1
        counts[str(points)] = count
    return counts


def census_five() -> Dict[str, object]:
    uc4 = union_closed_families_on_four_points()
    stats = [family_statistics_on_four(mask) for mask in uc4]
    stable_flags = stable_upper_choices(uc4)
    all_upper_choices = (1 << len(uc4)) - 1

    total = 0
    admissible = 0
    equality_count = 0
    minimum_frankl_margin: Optional[int] = None
    size_histogram: Dict[int, int] = {}
    margin_histogram: Dict[int, int] = {}
    negative_counts = {power: 0 for power in range(4)}
    minimum_values: Dict[int, Optional[int]] = {power: None for power in range(4)}
    smallest_negative: Dict[int, Optional[Dict[str, object]]] = {
        power: None for power in range(4)
    }
    most_negative: Dict[int, Optional[Dict[str, object]]] = {
        power: None for power in range(4)
    }
    twin_negative_counts = {power: 0 for power in range(4)}
    twin_minimum_values: Dict[int, Optional[int]] = {
        power: None for power in range(4)
    }
    twin_smallest_negative: Dict[int, Optional[Dict[str, object]]] = {
        power: None for power in range(4)
    }
    twin_most_negative: Dict[int, Optional[Dict[str, object]]] = {
        power: None for power in range(4)
    }
    eligible_upper_histogram: Dict[int, int] = {}

    for lower_index, lower_family in enumerate(uc4):
        eligible = all_upper_choices
        for lower_subset in members(lower_family):
            eligible &= stable_flags[lower_subset]

        eligible_count = popcount(eligible)
        eligible_upper_histogram[eligible_count] = (
            eligible_upper_histogram.get(eligible_count, 0) + 1
        )
        lower_count, lower_support, lower_freq, lower_separated = stats[lower_index]

        while eligible:
            upper_bit = eligible & -eligible
            upper_index = upper_bit.bit_length() - 1
            eligible ^= upper_bit
            upper_family = uc4[upper_index]
            upper_count, upper_support, upper_freq, upper_separated = stats[upper_index]

            total += 1
            size = lower_count + upper_count
            size_histogram[size] = size_histogram.get(size, 0) + 1
            support = lower_support | upper_support
            if upper_count:
                support |= 16

            # Frankl's nontrivial formulation excludes empty support.  This
            # removes exactly the empty family and {empty set}.
            if not support:
                continue
            admissible += 1
            frequencies = tuple(
                lower_freq[i] + upper_freq[i] for i in range(4)
            ) + (upper_count,)
            active = [
                frequencies[i] for i in range(5) if support & (1 << i)
            ]
            twin_active = twin_class_frequencies(
                support,
                frequencies,
                lower_separated | upper_separated,
                lower_support,
                upper_count,
                upper_freq,
            )
            frankl_margin = 2 * max(active) - size
            minimum_frankl_margin = (
                frankl_margin
                if minimum_frankl_margin is None
                else min(minimum_frankl_margin, frankl_margin)
            )
            margin_histogram[frankl_margin] = margin_histogram.get(frankl_margin, 0) + 1
            if frankl_margin == 0:
                equality_count += 1

            for power in range(4):
                value = sum(
                    (frequency ** power) * (2 * frequency - size)
                    for frequency in active
                )
                previous_minimum = minimum_values[power]
                if previous_minimum is None or value < previous_minimum:
                    minimum_values[power] = value
                    most_negative[power] = witness_record(
                        lower_index,
                        upper_index,
                        lower_family,
                        upper_family,
                        size,
                        frequencies,
                        support,
                        value,
                    )
                if value < 0:
                    negative_counts[power] += 1
                    record = smallest_negative[power]
                    candidate_key = (
                        size,
                        popcount(support),
                        decode_five_point_family(lower_family, upper_family),
                    )
                    if record is None:
                        replace = True
                    else:
                        old_subsets = tuple(
                            sum(1 << (point - 1) for point in subset)
                            for subset in record["members"]
                        )
                        old_key = (
                            int(record["family_size"]),
                            int(record["support_size"]),
                            old_subsets,
                        )
                        replace = candidate_key < old_key
                    if replace:
                        smallest_negative[power] = witness_record(
                            lower_index,
                            upper_index,
                            lower_family,
                            upper_family,
                            size,
                            frequencies,
                            support,
                            value,
                        )

                twin_value = sum(
                    (frequency ** power) * (2 * frequency - size)
                    for frequency in twin_active
                )
                twin_previous_minimum = twin_minimum_values[power]
                if twin_previous_minimum is None or twin_value < twin_previous_minimum:
                    twin_minimum_values[power] = twin_value
                    twin_most_negative[power] = witness_record(
                        lower_index,
                        upper_index,
                        lower_family,
                        upper_family,
                        size,
                        frequencies,
                        support,
                        twin_value,
                    )
                    twin_most_negative[power]["twin_class_frequencies"] = twin_active
                if twin_value < 0:
                    twin_negative_counts[power] += 1
                    twin_record = twin_smallest_negative[power]
                    twin_candidate_key = (
                        size,
                        len(twin_active),
                        decode_five_point_family(lower_family, upper_family),
                    )
                    if twin_record is None:
                        twin_replace = True
                    else:
                        twin_old_subsets = tuple(
                            sum(1 << (point - 1) for point in subset)
                            for subset in twin_record["members"]
                        )
                        twin_old_key = (
                            int(twin_record["family_size"]),
                            len(twin_record["twin_class_frequencies"]),
                            twin_old_subsets,
                        )
                        twin_replace = twin_candidate_key < twin_old_key
                    if twin_replace:
                        twin_smallest_negative[power] = witness_record(
                            lower_index,
                            upper_index,
                            lower_family,
                            upper_family,
                            size,
                            frequencies,
                            support,
                            twin_value,
                        )
                        twin_smallest_negative[power]["twin_class_frequencies"] = twin_active

    return {
        "points": 5,
        "union_closed_family_count_including_empty_family": total,
        "admissible_nonempty_support_count": admissible,
        "minimum_frankl_margin": minimum_frankl_margin,
        "frankl_equality_count": equality_count,
        "size_histogram": {str(k): v for k, v in sorted(size_histogram.items())},
        "frankl_margin_histogram": {
            str(k): v for k, v in sorted(margin_histogram.items())
        },
        "eligible_upper_choice_histogram": {
            str(k): v for k, v in sorted(eligible_upper_histogram.items())
        },
        "weighting_templates": {
            str(power): {
                "formula": f"sum_x f_x^{power} (2 f_x - |F|)",
                "negative_family_count": negative_counts[power],
                "minimum_value": minimum_values[power],
                "smallest_negative_witness": smallest_negative[power],
                "minimum_value_witness": most_negative[power],
            }
            for power in range(4)
        },
        "twin_reduced_weighting_templates": {
            str(power): {
                "formula": (
                    f"sum_C f_C^{power} (2 f_C - |F|), one term per "
                    "nonempty incidence-column class C"
                ),
                "negative_family_count": twin_negative_counts[power],
                "minimum_value": twin_minimum_values[power],
                "smallest_negative_witness": twin_smallest_negative[power],
                "minimum_value_witness": twin_most_negative[power],
            }
            for power in range(4)
        },
    }


def build_payload() -> Dict[str, object]:
    return {
        "schema_version": 1,
        "arithmetic": "exact integers only",
        "definition": (
            "labelled set families; the empty family is counted in the census; "
            "Frankl and weighting statistics require nonempty support"
        ),
        "counts_through_four": brute_counts_through_four(),
        "five_point_census": census_five(),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    census = payload["five_point_census"]
    print(
        "five-point union-closed families:",
        census["union_closed_family_count_including_empty_family"],
    )
    print("minimum Frankl margin:", census["minimum_frankl_margin"])
    for power, row in census["weighting_templates"].items():
        print(
            f"p={power}: negative={row['negative_family_count']}, "
            f"minimum={row['minimum_value']}"
        )
    for power, row in census["twin_reduced_weighting_templates"].items():
        print(
            f"twin-reduced p={power}: negative={row['negative_family_count']}, "
            f"minimum={row['minimum_value']}"
        )
    print("SMALL-FAMILY CENSUS PASS")


if __name__ == "__main__":
    main()
