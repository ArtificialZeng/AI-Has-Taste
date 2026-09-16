#!/usr/bin/env python3
"""Independent replay of the strict m=6 upper-bound search.

This checker represents arcs and Reg5 copies as frozensets of ordered pairs.
It enumerates degree vectors first, then Cartesian products of row subsets of
the specified sizes.  This is deliberately different from the dense-mask DFS
used by reg5_m6_enum.py.  It also parses and validates every reported free
maximizer from that run.
"""

import itertools
import pathlib
import re

N = 6
BOUND = 114


def regular_arcs(image):
    return frozenset(
        (image[i], image[j])
        for i in range(5)
        for j in range(5)
        if i != j and ((j - i) % 5) in (1, 2)
    )


patterns = {
    regular_arcs(image)
    for support in itertools.combinations(range(N), 5)
    for image in itertools.permutations(support)
}
assert len(patterns) == 144

heads = tuple(tuple(v for v in range(N) if v != u) for u in range(N))
row_choices = tuple(
    tuple(
        tuple(frozenset((u, v) for v in choice) for choice in itertools.combinations(heads[u], degree))
        for degree in range(N)
    )
    for u in range(N)
)

strict_degree_vectors = 0
strict_digraphs_checked = 0
strict_containing = 0
for degrees in itertools.product(range(N), repeat=N):
    score = sum(degree * degree for degree in degrees)
    if score <= BOUND:
        continue
    strict_degree_vectors += 1
    for rows in itertools.product(*(row_choices[u][degrees[u]] for u in range(N))):
        strict_digraphs_checked += 1
        arcs = frozenset().union(*rows)
        if any(pattern <= arcs for pattern in patterns):
            strict_containing += 1

assert strict_digraphs_checked == strict_containing

arc_order = tuple((u, v) for u in range(N) for v in heads[u])


def arcs_from_mask(mask):
    return frozenset(arc for bit, arc in enumerate(arc_order) if mask & (1 << bit))


enum_log = pathlib.Path(__file__).with_name("reg5_m6_enum.log").read_text(encoding="utf-8")
reported_best = int(re.search(r"^maximum_Reg5_free_L2_out=(\d+)$", enum_log, re.M).group(1))
reported_count = int(re.search(r"^maximizer_count=(\d+)$", enum_log, re.M).group(1))
reported_masks = [int(value, 16) for value in re.findall(r"dense_hex=0x([0-9a-f]+)", enum_log)]
assert len(reported_masks) == reported_count
assert len(set(reported_masks)) == reported_count

t4_count = 0
for mask in reported_masks:
    arcs = arcs_from_mask(mask)
    degrees = tuple(sum((u, v) in arcs for v in range(N)) for u in range(N))
    assert sum(degree * degree for degree in degrees) == reported_best == BOUND
    assert not any(pattern <= arcs for pattern in patterns)
    missing_pairs = []
    for u in range(N):
        for v in range(u + 1, N):
            uv = (u, v) in arcs
            vu = (v, u) in arcs
            if not uv and not vu:
                missing_pairs.append((u, v))
            else:
                assert uv and vu
    components = [{u} for u in range(N)]
    for u, v in missing_pairs:
        cu = next(component for component in components if u in component)
        cv = next(component for component in components if v in component)
        if cu is not cv:
            cu.update(cv)
            components.remove(cv)
    sizes = sorted(map(len, components))
    assert sizes == [1, 1, 2, 2]
    assert len(missing_pairs) == 2
    t4_count += 1

assert t4_count == reported_count
print(f"distinct_labeled_Reg5_sets={len(patterns)}")
print(f"strict_degree_vectors={strict_degree_vectors}")
print(f"strict_digraphs_checked={strict_digraphs_checked}")
print(f"strict_digraphs_containing_Reg5={strict_containing}")
print(f"strict_Reg5_free_digraphs=0")
print(f"replayed_maximizers={reported_count}")
print(f"all_replayed_objectives={reported_best}")
print(f"all_replayed_Reg5_free=true")
print(f"all_replayed_are_T4_6=true")
print(f"certified_upper_bound={BOUND}")
