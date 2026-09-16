#!/usr/bin/env python3
"""Strict comparison gate for the two exact A114216 replay records."""

import argparse
import hashlib
import json
from pathlib import Path


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("path_a", type=Path)
    ap.add_argument("path_b", type=Path)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    a = json.loads(args.path_a.read_text())
    b = json.loads(args.path_b.read_text())
    required_equal = {
        "target_index": (a["target_index"], b["target_index"]),
        "final_a": (a["final_a"], b["final_a"]),
        "final_digest": (
            a["final_digest_fnv1a_n_p_a_le64"],
            b["final_digest_fnv1a_n_p_a_le64"],
        ),
        "maximum_a_seen": (a["maximum_a_seen"], b["maximum_a_seen"]),
        "hits": (a["hits"], b["hits"]),
        "checkpoints": (a["checkpoints"], b["checkpoints"]),
    }
    failures = [name for name, pair in required_equal.items() if pair[0] != pair[1]]
    if failures:
        raise AssertionError("independent replay disagreement: " + ", ".join(failures))
    for label, record in (("A", a), ("B", b)):
        if record["checkpoints"][-1]["n"] == record["target_index"]:
            if (record["checkpoints"][-1]["digest"] !=
                    record["final_digest_fnv1a_n_p_a_le64"]):
                raise AssertionError(f"path {label} final digest is internally inconsistent")
    target = a["target_index"]
    frontier = 78_493_252
    frontier_hits = [h for h in a["hits"] if h["n"] == frontier]
    if target >= frontier and len(frontier_hits) != 1:
        raise AssertionError("historical frontier was not reproduced exactly once")
    interval_hits = [h for h in a["hits"] if frontier < h["n"] <= target]
    report = {
        "schema": "a114216-dual-comparison-v1",
        "status": "agreement",
        "path_a_sha256": digest(args.path_a),
        "path_b_sha256": digest(args.path_b),
        "target_index": target,
        "compared_checkpoint_count": len(a["checkpoints"]),
        "compared_complete_hit_count": len(a["hits"]),
        "historical_frontier_record": frontier_hits[0] if frontier_hits else None,
        "hits_after_78493252_through_target": interval_hits,
        "final_checkpoint": a["checkpoints"][-1],
        "final_digest_fnv1a_n_p_a_le64": a["final_digest_fnv1a_n_p_a_le64"],
        "maximum_a_seen": a["maximum_a_seen"],
    }
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
