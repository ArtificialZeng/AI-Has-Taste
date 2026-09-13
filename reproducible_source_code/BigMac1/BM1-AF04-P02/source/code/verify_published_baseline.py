#!/usr/bin/env python3
"""Check exact reproduction of the last published STS(15) baseline."""

import hashlib
import json
from pathlib import Path


def load(path):
    with open(path, encoding="utf-8") as stream:
        return json.load(stream)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    baseline_path = "certificate/published_baseline.json"
    result_path = "certificate/result.json"
    baseline = load(baseline_path)
    result = load(result_path)
    counts = baseline["standard_number_pasch_counts"]
    assert len(counts) == 80
    assert counts[-1] == 0 and counts.count(0) == 1
    assert sum(counts) == 1390
    assert sorted(counts) == result["pasch_count_multiset"]
    assert baseline["published_component_sizes"] == result["component_sizes"]
    assert baseline["diameter_stated_in_source"] is False
    print(
        json.dumps(
            {
                "status": "VERIFIED",
                "published_component_sizes_reproduced": [79, 1],
                "published_pasch_count_vector_length": 80,
                "published_pasch_total": 1390,
                "published_count_multiset_matches_reconstruction": True,
                "baseline_sha256": sha(baseline_path),
                "result_sha256": sha(result_path),
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
