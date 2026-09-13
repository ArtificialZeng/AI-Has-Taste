#!/usr/bin/env python3
"""Independent exact checks for the five-point union-closed census."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple


EXPECTED_COUNTS = {"0": 2, "1": 4, "2": 14, "3": 122, "4": 4960, "5": 2771104}


if not __debug__:
    raise SystemExit("verification requires assertions; do not run Python with -O")


def subsets_from_serialised(members: Sequence[Sequence[int]]) -> Tuple[int, ...]:
    return tuple(
        sorted(sum(1 << (point - 1) for point in subset) for subset in members)
    )


def check_union_closed(subsets: Sequence[int]) -> None:
    family = set(subsets)
    assert len(family) == len(subsets), "family has a duplicate member"
    for left in subsets:
        for right in subsets:
            assert left | right in family, "witness is not union-closed"


def recompute_witness(record: Dict[str, object], power: int) -> None:
    subsets = subsets_from_serialised(record["members"])
    check_union_closed(subsets)
    size = len(subsets)
    support = 0
    frequencies = [0, 0, 0, 0, 0]
    for subset in subsets:
        support |= subset
        for point in range(5):
            if subset & (1 << point):
                frequencies[point] += 1
    active = [frequencies[point] for point in range(5) if support & (1 << point)]
    value = sum((frequency ** power) * (2 * frequency - size) for frequency in active)
    assert size == record["family_size"]
    assert bin(support).count("1") == record["support_size"]
    assert frequencies == record["frequencies"]
    assert active == record["active_frequencies"]
    assert value == record["weight_value"]


def recompute_twin_witness(record: Dict[str, object], power: int) -> None:
    subsets = subsets_from_serialised(record["members"])
    check_union_closed(subsets)
    size = len(subsets)
    support = 0
    signatures = [0, 0, 0, 0, 0]
    frequencies = [0, 0, 0, 0, 0]
    for member_index, subset in enumerate(subsets):
        support |= subset
        for point in range(5):
            if subset & (1 << point):
                frequencies[point] += 1
                signatures[point] |= 1 << member_index
    active_signatures = sorted(
        {signatures[point] for point in range(5) if support & (1 << point)}
    )
    twin_frequencies = [bin(signature).count("1") for signature in active_signatures]
    value = sum(
        (frequency ** power) * (2 * frequency - size)
        for frequency in twin_frequencies
    )
    assert sorted(record["twin_class_frequencies"]) == sorted(twin_frequencies)
    assert value == record["weight_value"]


def union_closed_masks_four() -> List[int]:
    result: List[int] = []
    for family_mask in range(1 << 16):
        sets = [s for s in range(16) if family_mask & (1 << s)]
        if all(family_mask & (1 << (a | b)) for a in sets for b in sets):
            result.append(family_mask)
    return result


def trace_members(family_mask: int) -> Iterable[int]:
    for subset in range(16):
        if family_mask & (1 << subset):
            yield subset


def four_statistics(family_mask: int, sets: Sequence[int]) -> Tuple[int, int, Tuple[int, ...], Tuple[int, ...]]:
    support = 0
    frequencies = [0, 0, 0, 0]
    signatures = [0, 0, 0, 0]
    for member_index, subset in enumerate(sets):
        support |= subset
        for point in range(4):
            if subset & (1 << point):
                frequencies[point] += 1
                signatures[point] |= 1 << member_index
    return len(sets), support, tuple(frequencies), tuple(signatures)


def independent_five_summary() -> Dict[str, object]:
    """Recount extensions and every aggregate statistic independently."""

    uc4 = union_closed_masks_four()
    member_lists = [tuple(trace_members(family)) for family in uc4]
    stats = [
        four_statistics(family, sets)
        for family, sets in zip(uc4, member_lists)
    ]
    total = 0
    admissible = 0
    equality_count = 0
    minimum_margin = None
    size_histogram: Dict[int, int] = {}
    margin_histogram: Dict[int, int] = {}
    negative_counts = [0, 0, 0, 0]
    minimum_values = [None, None, None, None]
    twin_negative_counts = [0, 0, 0, 0]
    twin_minimum_values = [None, None, None, None]

    for lower_index, lower_family in enumerate(uc4):
        lower_sets = member_lists[lower_index]
        lower_count, lower_support, lower_freq, lower_sig = stats[lower_index]
        for upper_index, upper_family in enumerate(uc4):
            upper_sets = member_lists[upper_index]
            valid = True
            for lower in lower_sets:
                for upper in upper_sets:
                    if not (upper_family & (1 << (lower | upper))):
                        valid = False
                        break
                if not valid:
                    break
            if valid:
                total += 1
                upper_count, upper_support, upper_freq, upper_sig = stats[upper_index]
                size = lower_count + upper_count
                size_histogram[size] = size_histogram.get(size, 0) + 1
                support = lower_support | upper_support | (16 if upper_count else 0)
                if not support:
                    continue
                admissible += 1
                frequencies = tuple(
                    lower_freq[point] + upper_freq[point] for point in range(4)
                ) + (upper_count,)
                active_frequencies = [
                    frequencies[point]
                    for point in range(5)
                    if support & (1 << point)
                ]
                margin = 2 * max(active_frequencies) - size
                minimum_margin = margin if minimum_margin is None else min(minimum_margin, margin)
                margin_histogram[margin] = margin_histogram.get(margin, 0) + 1
                if margin == 0:
                    equality_count += 1

                combined_signatures = [
                    lower_sig[point] | (upper_sig[point] << lower_count)
                    for point in range(4)
                ] + [
                    ((1 << upper_count) - 1) << lower_count
                ]
                signature_to_frequency = {
                    combined_signatures[point]: frequencies[point]
                    for point in range(5)
                    if support & (1 << point)
                }
                twin_frequencies = list(signature_to_frequency.values())

                for power in range(4):
                    value = sum(
                        (frequency ** power) * (2 * frequency - size)
                        for frequency in active_frequencies
                    )
                    twin_value = sum(
                        (frequency ** power) * (2 * frequency - size)
                        for frequency in twin_frequencies
                    )
                    if value < 0:
                        negative_counts[power] += 1
                    if twin_value < 0:
                        twin_negative_counts[power] += 1
                    if minimum_values[power] is None or value < minimum_values[power]:
                        minimum_values[power] = value
                    if (
                        twin_minimum_values[power] is None
                        or twin_value < twin_minimum_values[power]
                    ):
                        twin_minimum_values[power] = twin_value

    return {
        "total": total,
        "admissible": admissible,
        "equality_count": equality_count,
        "minimum_margin": minimum_margin,
        "size_histogram": {str(k): v for k, v in sorted(size_histogram.items())},
        "margin_histogram": {str(k): v for k, v in sorted(margin_histogram.items())},
        "negative_counts": negative_counts,
        "minimum_values": minimum_values,
        "twin_negative_counts": twin_negative_counts,
        "twin_minimum_values": twin_minimum_values,
    }


def verify(payload: Dict[str, object], full_recount: bool) -> None:
    assert payload["counts_through_four"] == {
        key: EXPECTED_COUNTS[key] for key in ("0", "1", "2", "3", "4")
    }
    census = payload["five_point_census"]
    assert census["union_closed_family_count_including_empty_family"] == EXPECTED_COUNTS["5"]
    assert census["admissible_nonempty_support_count"] == EXPECTED_COUNTS["5"] - 2
    assert census["minimum_frankl_margin"] >= 0
    assert sum(census["size_histogram"].values()) == EXPECTED_COUNTS["5"]
    assert sum(census["frankl_margin_histogram"].values()) == EXPECTED_COUNTS["5"] - 2
    assert sum(census["eligible_upper_choice_histogram"].values()) == EXPECTED_COUNTS["4"]

    for power_text, row in census["weighting_templates"].items():
        power = int(power_text)
        smallest = row["smallest_negative_witness"]
        minimum = row["minimum_value_witness"]
        if row["negative_family_count"]:
            assert smallest is not None
            assert smallest["weight_value"] < 0
            recompute_witness(smallest, power)
        else:
            assert smallest is None
            assert row["minimum_value"] >= 0
        assert minimum is not None
        recompute_witness(minimum, power)
        assert minimum["weight_value"] == row["minimum_value"]

    for power_text, row in census["twin_reduced_weighting_templates"].items():
        power = int(power_text)
        smallest = row["smallest_negative_witness"]
        minimum = row["minimum_value_witness"]
        if row["negative_family_count"]:
            assert smallest is not None
            assert smallest["weight_value"] < 0
            recompute_twin_witness(smallest, power)
        else:
            assert smallest is None
            assert row["minimum_value"] >= 0
        assert minimum is not None
        recompute_twin_witness(minimum, power)
        assert minimum["weight_value"] == row["minimum_value"]

    if full_recount:
        replay = independent_five_summary()
        assert replay["total"] == EXPECTED_COUNTS["5"]
        assert replay["admissible"] == census["admissible_nonempty_support_count"]
        assert replay["equality_count"] == census["frankl_equality_count"]
        assert replay["minimum_margin"] == census["minimum_frankl_margin"]
        assert replay["size_histogram"] == census["size_histogram"]
        assert replay["margin_histogram"] == census["frankl_margin_histogram"]
        assert replay["negative_counts"] == [
            census["weighting_templates"][str(power)]["negative_family_count"]
            for power in range(4)
        ]
        assert replay["minimum_values"] == [
            census["weighting_templates"][str(power)]["minimum_value"]
            for power in range(4)
        ]
        assert replay["twin_negative_counts"] == [
            census["twin_reduced_weighting_templates"][str(power)]["negative_family_count"]
            for power in range(4)
        ]
        assert replay["twin_minimum_values"] == [
            census["twin_reduced_weighting_templates"][str(power)]["minimum_value"]
            for power in range(4)
        ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument(
        "--full-recount",
        action="store_true",
        help="independently test all 4960^2 four-point trace pairs",
    )
    args = parser.parse_args()
    payload = json.loads(args.input.read_text())
    verify(payload, args.full_recount)
    print("INDEPENDENT SMALL-FAMILY VERIFICATION PASS")


if __name__ == "__main__":
    main()
