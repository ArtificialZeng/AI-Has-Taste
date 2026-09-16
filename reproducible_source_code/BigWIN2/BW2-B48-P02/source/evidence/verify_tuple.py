#!/usr/bin/env python3
"""Solver-free replay of the certificates for (E3,C3,E7,C7).

This verifier independently regenerates all (3!)^4 balanced r=3 assignments
and checks the explicit r=7 cycle and rainbow path stored in r7_witness.json.
It uses only the Python standard library.
"""

from __future__ import annotations

import itertools
import json
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent


def cycles_of(step_at: tuple[int, ...]) -> list[list[int]] | None:
    n = len(step_at)
    succ = [(x + step_at[x]) % n for x in range(n)]
    if len(set(succ)) != n:
        return None
    unseen = set(range(n))
    cycles = []
    while unseen:
        start = min(unseen)
        cycle = []
        x = start
        while x in unseen:
            unseen.remove(x)
            cycle.append(x)
            x = succ[x]
        assert x == start
        cycles.append(cycle)
    return cycles


def replay_r3() -> dict:
    r, n = 3, 12
    permutations = tuple(itertools.permutations(range(1, r + 1)))
    checked = bijective = hamilton = 0
    types = Counter()
    for layers in itertools.product(permutations, repeat=4):
        step_at = [0] * n
        for j in range(4):
            for t in range(r):
                step_at[j + 4 * t] = layers[j][t]
        checked += 1
        cycles = cycles_of(tuple(step_at))
        if cycles is None:
            continue
        bijective += 1
        lengths = tuple(sorted(map(len, cycles)))
        types[lengths] += 1
        hamilton += lengths == (n,)

    assert checked == 6**4 == 1296
    assert bijective == 15
    assert types == Counter({(6, 6): 12, (4, 8): 3})
    assert hamilton == 0

    stored = json.loads((HERE / "r3_enumeration.json").read_text())
    assert stored["domain_argument"]["assignments_checked"] == checked
    assert stored["successor_permutation_count"] == bijective
    assert stored["successor_permutation_cycle_type_counts"] == {
        "4+8": 3,
        "6+6": 12,
    }
    assert stored["hamilton_starter_count"] == hamilton
    assert stored["truth_values_established"] == {"E_3": False, "C_3": False}
    return {
        "balanced_assignments_checked": checked,
        "bijective_successor_assignments": bijective,
        "cycle_type_counts": {"4+8": 3, "6+6": 12},
        "hamilton_starters": hamilton,
        "E_3": False,
        "C_3": False,
    }


def replay_r7() -> dict:
    r, n = 7, 28
    stored = json.loads((HERE / "r7_witness.json").read_text())
    step_at = tuple(stored["step_at_tail_0_to_27"])
    assert len(step_at) == n
    assert all(1 <= s <= r for s in step_at)
    for j in range(4):
        assert sorted(step_at[j::4]) == list(range(1, r + 1))

    cycles = cycles_of(step_at)
    assert cycles is not None and len(cycles) == 1 and len(cycles[0]) == n
    assert stored["cycle_vertices_including_return"][:-1] == cycles[0]
    assert stored["cycle_vertices_including_return"][-1] == cycles[0][0] == 0

    beta = [[-1] * (r + 1) for _ in range(4)]
    for x, s in enumerate(step_at):
        j, t = x % 4, x // 4
        assert beta[j][s] == -1
        beta[j][s] = t
    assert stored["beta_rows_j_0_to_3_columns_s_1_to_7"] == [
        row[1:] for row in beta
    ]

    path = stored["rainbow_path"]
    vertices = path["vertices"]
    steps = path["steps"]
    colours = []
    assert len(vertices) == r + 1 and len(set(vertices)) == r + 1
    assert len(steps) == r
    for x, y, s in zip(vertices, vertices[1:], steps):
        assert 1 <= s <= r and y == (x + s) % n
        j, t = x % 4, x // 4
        colours.append((t - beta[j][s]) % r)
    assert colours == path["development_colours"]
    assert sorted(colours) == list(range(r))

    selected = stored["selected_arc_from_each_developed_cycle_H_k_k_0_to_6"]
    assert len(selected) == r
    for k, (x, y) in enumerate(selected):
        s = (y - x) % n
        assert 1 <= s <= r
        j = x % 4
        base_tail = j + 4 * beta[j][s]
        assert x == (base_tail + 4 * k) % n
    assert stored["truth_values_established"] == {"E_7": True, "C_7": True}
    return {
        "cycle_length": n,
        "balanced_orbits_checked": 4 * r,
        "rainbow_path_vertices": vertices,
        "rainbow_path_colours": colours,
        "E_7": True,
        "C_7": True,
    }


def main() -> None:
    result = {
        "r3_exhaustive_replay": replay_r3(),
        "r7_explicit_witness_replay": replay_r7(),
        "truth_value_tuple_E3_C3_E7_C7": [False, False, True, True],
    }
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    (HERE / "tuple_verification.json").write_text(encoded, encoding="utf-8")
    print(encoded, end="")


if __name__ == "__main__":
    main()
