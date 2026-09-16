#!/usr/bin/env python3
"""Falsify fixed-window state features for zero-residue child prediction."""

import argparse
import json
import platform

import numpy as np
from numba import njit


@njit
def zero_node_states_direct(k: int, capacity: int):
    modulus = 1 << k
    period = 3 * modulus
    residues = np.empty(capacity, dtype=np.int64)
    previous = np.empty(capacity, dtype=np.int64)
    count = 0
    x, y = 0, 1
    for n in range(2, period):
        x, y = y, ((y ^ n) - x) % modulus
        if y == 0:
            if count >= capacity:
                return residues, previous, -1
            residues[count] = n
            previous[count] = x
            count += 1
    return residues, previous, count


def ambiguity(records, feature):
    outcomes = {}
    counts = {}
    for record in records:
        key = feature(record)
        outcomes.setdefault(key, set()).add(record[3])
        counts[key] = counts.get(key, 0) + 1
    ambiguous = {key for key, values in outcomes.items() if len(values) > 1}
    return {
        "feature_classes": len(outcomes),
        "ambiguous_feature_classes": len(ambiguous),
        "records_in_ambiguous_classes": sum(counts[key] for key in ambiguous),
        "predictive": not ambiguous,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-parent-k", type=int, default=24)
    parser.add_argument("--max-window", type=int, default=12)
    parser.add_argument("--capacity", type=int, default=10000)
    parser.add_argument("--output")
    args = parser.parse_args()
    assert 1 <= args.max_window <= args.max_parent_k

    zero_node_states_direct(1, args.capacity)
    levels = []
    for k in range(1, args.max_parent_k + 2):
        residues, previous, count = zero_node_states_direct(k, args.capacity)
        assert count >= 0
        levels.append((
            [int(value) for value in residues[:count]],
            [int(value) for value in previous[:count]],
        ))

    records = []
    for k in range(1, args.max_parent_k + 1):
        residues, previous = levels[k - 1]
        children = set(levels[k][0])
        period = 3 << k
        for r, x in zip(residues, previous):
            outcome = int(r in children) + 2 * int(r + period in children)
            records.append((k, r, x, outcome))

    tests = []
    for width in range(1, args.max_window + 1):
        mask = (1 << width) - 1
        families = {
            "low-state-window": lambda z, mask=mask: (z[1] & mask, z[2] & mask),
            "low-window-plus-component-and-block": lambda z, mask=mask: (
                z[1] & mask,
                z[2] & mask,
                z[1] % 3,
                z[1] // (1 << z[0]),
            ),
            "low-window-plus-leading-time-window": lambda z, mask=mask, width=width: (
                z[1] & mask,
                z[2] & mask,
                z[1] % 3,
                z[1] // (1 << max(0, z[0] - width)),
            ),
        }
        eligible = [record for record in records if record[0] >= width]
        for name, feature in families.items():
            result = ambiguity(eligible, feature)
            result.update({"family": name, "window_bits": width, "records": len(eligible)})
            tests.append(result)

    record = {
        "schema_version": 1,
        "purpose": "attack fixed-window candidate state descriptions for the zero-lift child map",
        "semantics": "exact recurrence modulo powers of two using direct XOR",
        "max_parent_k": args.max_parent_k,
        "max_window_bits": args.max_window,
        "zero_nodes_with_defined_previous_state": len(records),
        "child_outcome_encoding": {"0": "dead", "1": "lower only", "2": "upper only", "3": "both"},
        "tests": tests,
        "conclusion_scope": (
            "A family with an ambiguous class is refuted only for the named fixed-window "
            "feature map. This does not rule out a richer or level-dependent finite quotient."
        ),
        "python": platform.python_version(),
        "numba": __import__("numba").__version__,
    }
    assert all(not item["predictive"] for item in tests)
    text = json.dumps(record, indent=2) + "\n"
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
