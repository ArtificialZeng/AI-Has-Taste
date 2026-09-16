#!/usr/bin/env python3
"""Independent replay checks for the exhaustive m=5 output.

This implementation deliberately represents a digraph as a frozenset of
ordered pairs, unlike the C++ row-major bitmask implementation.
"""

import itertools
import pathlib
import re

N = 5


def regular_arcs(permutation):
    return frozenset(
        (permutation[u], permutation[v])
        for u in range(N)
        for v in range(N)
        if u != v and ((v - u) % N) in (1, 2)
    )


heads = tuple(tuple(v for v in range(N) if v != u) for u in range(N))
arc_index = {
    (u, v): 4 * u + k
    for u in range(N)
    for k, v in enumerate(heads[u])
}


def arcs_from_hex(value):
    return frozenset(
        (u, v)
        for u in range(N)
        for v in range(N)
        if u != v and value & (1 << arc_index[u, v])
    )


def objective(arcs):
    return sum(sum((u, v) in arcs for v in range(N)) ** 2 for u in range(N))


patterns = {regular_arcs(p) for p in itertools.permutations(range(N))}
assert len(patterns) == 24
log_path = pathlib.Path(__file__).with_name("reg5_m5_enum.log")
text = log_path.read_text(encoding="utf-8")
assert "enumerated_digraphs=1048576" in text
assert "partition_check=1048576" in text
reported_best = int(re.search(r"^maximum_L2_out=(\d+)$", text, re.M).group(1))
reported_count = int(re.search(r"^maximizer_count=(\d+)$", text, re.M).group(1))
hex_values = [int(x, 16) for x in re.findall(r"dense_hex=0x([0-9a-f]+)", text)]
assert len(hex_values) == reported_count
assert len(set(hex_values)) == reported_count

for value in hex_values:
    arcs = arcs_from_hex(value)
    assert objective(arcs) == reported_best
    assert all(not pattern <= arcs for pattern in patterns)
    missing = {
        (u, v)
        for u in range(N)
        for v in range(N)
        if u != v and (u, v) not in arcs
    }
    assert len(missing) == 2
    (u, v), (x, y) = missing
    assert (u, v) == (y, x)

print(f"distinct_labeled_Reg5_masks={len(patterns)}")
print(f"replayed_maximizers={len(hex_values)}")
print(f"all_reported_maximizers_Reg5_free=true")
print(f"all_reported_objectives_equal={reported_best}")
print("all_reported_maximizers_are_T4_5=true")
