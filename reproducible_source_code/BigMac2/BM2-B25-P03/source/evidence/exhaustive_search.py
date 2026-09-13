#!/Users/mac/4prove-or-disprove-math/.research-venv/bin/python
"""Exact exhaustive search for the frozen F_3^2 cross-part problem.

The program enumerates all C(9,4)=126 four-subsets and all 5P4=120
injections into the complement.  It emits one valid injection for every
subset if the universal claim is true, or complete per-injection failure data
for the first counterexample.  Only integer arithmetic modulo 3 is used.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path


G = tuple((x, y) for x in range(3) for y in range(3))
DIRECTION_REPRESENTATIVES = ((1, 0), (0, 1), (1, 1), (1, 2))


def neg(v: tuple[int, int]) -> tuple[int, int]:
    return ((-v[0]) % 3, (-v[1]) % 3)


def direction_index(a: tuple[int, int], b: tuple[int, int]) -> int:
    d = ((a[0] - b[0]) % 3, (a[1] - b[1]) % 3)
    if d == (0, 0):
        raise ValueError("cross edge cannot be a loop")
    for i, rep in enumerate(DIRECTION_REPRESENTATIVES):
        if d == rep or d == neg(rep):
            return i
    raise AssertionError(f"unclassified nonzero difference {d}")


def point(v: tuple[int, int]) -> list[int]:
    return [v[0], v[1]]


def mapping_record(
    subset: tuple[tuple[int, int], ...], image: tuple[tuple[int, int], ...]
) -> dict[str, object]:
    indices = [direction_index(a, b) for a, b in zip(subset, image)]
    mask = sum(1 << i for i in set(indices))
    return {
        "image": [point(v) for v in image],
        "direction_indices": indices,
        "direction_mask": mask,
    }


def enumerate_problem() -> dict[str, object]:
    witness_records: list[dict[str, object]] = []
    total_injections_checked = 0
    valid_count_histogram: dict[int, int] = {}
    min_valid = None
    max_valid = None

    for subset_number, subset in enumerate(itertools.combinations(G, 4)):
        subset_set = set(subset)
        complement = tuple(v for v in G if v not in subset_set)
        valid: list[tuple[tuple[int, int], ...]] = []
        failures: list[dict[str, object]] = []

        for injection_number, image in enumerate(itertools.permutations(complement, 4)):
            total_injections_checked += 1
            record = mapping_record(subset, image)
            if record["direction_mask"] == 15:
                valid.append(image)
            else:
                failures.append(
                    {
                        "injection_number": injection_number,
                        **record,
                    }
                )

        if not valid:
            return {
                "schema": "f3-square-cross-rainbow-exhaustion-v1",
                "result": "counterexample",
                "group_order": 9,
                "subsets_expected": 126,
                "injections_per_subset_expected": 120,
                "subsets_completed_before_failure": subset_number,
                "total_injections_checked": total_injections_checked,
                "failing_subset_number": subset_number,
                "failing_subset": [point(v) for v in subset],
                "complement": [point(v) for v in complement],
                "all_120_failures": failures,
            }

        count = len(valid)
        valid_count_histogram[count] = valid_count_histogram.get(count, 0) + 1
        min_valid = count if min_valid is None else min(min_valid, count)
        max_valid = count if max_valid is None else max(max_valid, count)
        chosen = valid[0]
        witness_records.append(
            {
                "subset_number": subset_number,
                "subset": [point(v) for v in subset],
                "complement": [point(v) for v in complement],
                "valid_injection_count": count,
                "witness": mapping_record(subset, chosen),
            }
        )

    return {
        "schema": "f3-square-cross-rainbow-exhaustion-v1",
        "result": "universal_witnesses",
        "group_order": 9,
        "point_order": [point(v) for v in G],
        "direction_representatives": [point(v) for v in DIRECTION_REPRESENTATIVES],
        "subsets_expected": 126,
        "subsets_checked": len(witness_records),
        "injections_per_subset": 120,
        "total_injections_checked": total_injections_checked,
        "valid_injection_count_min": min_valid,
        "valid_injection_count_max": max_valid,
        "valid_injection_count_histogram": {
            str(k): valid_count_histogram[k] for k in sorted(valid_count_histogram)
        },
        "witnesses": witness_records,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = enumerate_problem()
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    args.output.write_text(payload, encoding="utf-8")
    digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()
    print(json.dumps({"output": str(args.output), "sha256": digest, **{
        key: result.get(key) for key in (
            "result", "subsets_checked", "total_injections_checked",
            "valid_injection_count_min", "valid_injection_count_max",
            "valid_injection_count_histogram",
        )
    }}, sort_keys=True))


if __name__ == "__main__":
    main()
