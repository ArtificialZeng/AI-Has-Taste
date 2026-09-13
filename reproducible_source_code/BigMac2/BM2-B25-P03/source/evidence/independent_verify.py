#!/Users/mac/4prove-or-disprove-math/.research-venv/bin/python
"""Independent checker for exhaustive_certificate.json.

This deliberately does not import exhaustive_search.py.  It independently
constructs F_3^2, enumerates subsets and injections, validates serialized
witnesses, and recomputes the valid-injection-count distribution.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path


def canonical_line(p: tuple[int, int], q: tuple[int, int]) -> tuple[int, int]:
    dx, dy = ((p[0] - q[0]) % 3, (p[1] - q[1]) % 3)
    if (dx, dy) == (0, 0):
        raise AssertionError("loop encountered")
    minus = ((-dx) % 3, (-dy) % 3)
    return min((dx, dy), minus)


def as_tuple(v: list[int]) -> tuple[int, int]:
    assert isinstance(v, list) and len(v) == 2
    x, y = v
    assert type(x) is int and type(y) is int and 0 <= x < 3 and 0 <= y < 3
    return (x, y)


def verify(path: Path) -> dict[str, object]:
    raw = path.read_bytes()
    cert = json.loads(raw)
    universe = tuple(itertools.product(range(3), repeat=2))
    subsets = tuple(itertools.combinations(universe, 4))
    required_lines = {
        canonical_line((0, 0), v) for v in universe if v != (0, 0)
    }
    assert len(universe) == 9
    assert len(subsets) == 126
    assert len(required_lines) == 4
    assert cert["result"] == "universal_witnesses"
    assert cert["subsets_expected"] == cert["subsets_checked"] == 126
    assert cert["injections_per_subset"] == 120
    assert cert["total_injections_checked"] == 126 * 120 == 15120
    assert len(cert["witnesses"]) == 126

    recomputed_histogram: dict[int, int] = {}
    seen_subsets: set[tuple[tuple[int, int], ...]] = set()
    total = 0

    for expected_number, expected_subset in enumerate(subsets):
        row = cert["witnesses"][expected_number]
        assert row["subset_number"] == expected_number
        subset = tuple(as_tuple(v) for v in row["subset"])
        complement = tuple(as_tuple(v) for v in row["complement"])
        assert subset == expected_subset
        assert subset not in seen_subsets
        seen_subsets.add(subset)
        assert set(subset).isdisjoint(complement)
        assert set(subset) | set(complement) == set(universe)
        assert len(complement) == 5 and len(set(complement)) == 5

        image = tuple(as_tuple(v) for v in row["witness"]["image"])
        assert len(image) == len(set(image)) == 4
        assert set(image) <= set(complement)
        witness_lines = {
            canonical_line(a, b) for a, b in zip(subset, image)
        }
        assert witness_lines == required_lines
        asserted_indices = row["witness"]["direction_indices"]
        asserted_mask = row["witness"]["direction_mask"]
        assert sorted(asserted_indices) == [0, 1, 2, 3]
        assert asserted_mask == 15

        valid_count = 0
        injection_count = 0
        for candidate_image in itertools.permutations(complement, 4):
            injection_count += 1
            total += 1
            lines = [
                canonical_line(a, b) for a, b in zip(subset, candidate_image)
            ]
            if len(set(lines)) == 4:
                assert set(lines) == required_lines
                valid_count += 1
        assert injection_count == 120
        assert valid_count == row["valid_injection_count"]
        recomputed_histogram[valid_count] = recomputed_histogram.get(valid_count, 0) + 1

    asserted_histogram = {int(k): v for k, v in cert["valid_injection_count_histogram"].items()}
    assert recomputed_histogram == asserted_histogram
    assert min(recomputed_histogram) == cert["valid_injection_count_min"]
    assert max(recomputed_histogram) == cert["valid_injection_count_max"]
    assert total == 15120
    return {
        "verification": "pass",
        "certificate_sha256": hashlib.sha256(raw).hexdigest(),
        "subsets_reconstructed": len(subsets),
        "serialized_witnesses_verified": len(seen_subsets),
        "injections_independently_recomputed": total,
        "valid_injection_count_histogram": {
            str(k): recomputed_histogram[k] for k in sorted(recomputed_histogram)
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()
    report = verify(args.certificate)
    args.report.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
