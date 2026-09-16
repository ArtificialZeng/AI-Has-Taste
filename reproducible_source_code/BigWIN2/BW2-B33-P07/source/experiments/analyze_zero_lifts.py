#!/usr/bin/env python3
"""Summarize the exact zero-residue lift forest from saved modular evidence."""

import argparse
import hashlib
import json


KNOWN = {0, 6, 11, 23, 36, 42, 48, 54}


def load_levels(source):
    tests = source["sequence_period_tests"]
    levels = []
    for expected_k, item in enumerate(tests):
        assert item["k"] == expected_k
        assert item["modulus"] == 1 << expected_k
        assert item["period"] == 3 << expected_k
        residues = item["zero_residues"]
        assert residues == sorted(set(residues))
        assert all(0 <= r < item["period"] for r in residues)
        levels.append(set(residues))
    return tests, levels


def summarize(source_path):
    raw = source_path.read_bytes()
    source = json.loads(raw)
    tests, levels = load_levels(source)
    transitions = []
    for k in range(len(levels) - 1):
        period = 3 << k
        parent = levels[k]
        child = levels[k + 1]
        projected = {r % period for r in child}
        assert projected <= parent
        histogram = [0, 0, 0]
        lower_only = upper_only = both = 0
        for r in sorted(parent):
            lower = r in child
            upper = r + period in child
            count = int(lower) + int(upper)
            histogram[count] += 1
            if count == 1 and lower:
                lower_only += 1
            elif count == 1:
                upper_only += 1
            elif count == 2:
                both += 1
        transitions.append({
            "k": k,
            "parent_count": len(parent),
            "child_count": len(child),
            "parents_with_0_1_2_children": histogram,
            "lower_only": lower_only,
            "upper_only": upper_only,
            "both": both,
        })

    lower_runs = []
    for k, level in enumerate(levels[:-1]):
        for r in level - KNOWN:
            run = 0
            while k + run + 1 < len(levels) and r in levels[k + run + 1]:
                run += 1
            lower_runs.append((run, k, r))
    lower_runs.sort(reverse=True)

    level_summaries = []
    for item, level in zip(tests, levels):
        nonknown = sorted(level - KNOWN)
        by_mod3 = [sum(r % 3 == c for r in level) for c in range(3)]
        level_summaries.append({
            "k": item["k"],
            "period": item["period"],
            "zero_residue_count": len(level),
            "counts_by_mod_3": by_mod3,
            "least_nonknown_representative": nonknown[0] if nonknown else None,
        })

    return {
        "schema_version": 1,
        "source_file": str(source_path),
        "source_sha256": hashlib.sha256(raw).hexdigest(),
        "mathematical_scope": (
            "finite exact topology of Z_k through the saved maximum level; "
            "it does not certify any infinite branch property"
        ),
        "maximum_level": tests[-1]["k"],
        "level_summaries": level_summaries,
        "transitions": transitions,
        "longest_observed_nonknown_lower_run": {
            "edge_count": lower_runs[0][0],
            "start_level": lower_runs[0][1],
            "representative": lower_runs[0][2],
            "ties_at_maximum": sum(x[0] == lower_runs[0][0] for x in lower_runs),
        },
        "warning": (
            "A finite maximum lower run is reproduced evidence only and cannot "
            "be promoted to a uniform escape theorem."
        ),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "source", nargs="?", default="experiments/modular-falsification-evidence.json"
    )
    parser.add_argument("--output")
    args = parser.parse_args()
    from pathlib import Path

    result = summarize(Path(args.source))
    text = json.dumps(result, indent=2) + "\n"
    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
