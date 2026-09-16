#!/usr/bin/env python3
"""MILP search for a sparse K7-free weighted 13-layer period.

There are at most four active vertices in each cyclic layer.  Edges may occur
inside a layer or between consecutive layers and nowhere else.  Weights are
integer multiples of 1/denominator.  HiGHS output is only computational
evidence; any returned witness is checked with integer arithmetic below.
"""

import argparse
from itertools import combinations

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import coo_matrix


LAYERS = 13
WIDTH = 4
N = LAYERS * WIDTH


def vertex(layer, position):
    return WIDTH * layer + position


def layer_of(u):
    return u // WIDTH


def build_and_solve(denominator, time_limit, mip_gap, allow_equality):
    vertices_by_layer = [
        [vertex(i, j) for j in range(WIDTH)] for i in range(LAYERS)
    ]
    pairs = []
    for layer in vertices_by_layer:
        pairs.extend(combinations(layer, 2))
    for i in range(LAYERS):
        pairs.extend(
            (u, v)
            for u in vertices_by_layer[i]
            for v in vertices_by_layer[(i + 1) % LAYERS]
        )
    pairs = [tuple(sorted(pair)) for pair in pairs]
    assert len(pairs) == 286 and len(set(pairs)) == 286
    pair_index = {pair: k for k, pair in enumerate(pairs)}
    incident = [[] for _ in range(N)]
    for k, (u, v) in enumerate(pairs):
        incident[u].append((k, v))
        incident[v].append((k, u))

    # q_u: integer weight numerator; a_u: activity; e_uv: edge;
    # z_(u<-v): the product e_uv*q_v, used in u's weighted degree.
    q0 = 0
    a0 = q0 + N
    e0 = a0 + N
    z0 = e0 + len(pairs)
    directed = []
    for k, (u, v) in enumerate(pairs):
        directed.extend(((u, v, k), (v, u, k)))
    z_index = {(u, v): z0 + k for k, (u, v, _) in enumerate(directed)}
    nvar = z0 + len(directed)

    lower = np.zeros(nvar)
    upper = np.full(nvar, np.inf)
    upper[q0 : q0 + N] = denominator
    upper[a0 : a0 + N] = 1
    upper[e0 : e0 + len(pairs)] = 1
    upper[z0:] = denominator
    integrality = np.zeros(nvar)
    integrality[q0 : q0 + N] = 1
    integrality[a0 : a0 + N] = 1
    integrality[e0 : e0 + len(pairs)] = 1

    rows = []
    lows = []
    highs = []

    def add(coefficients, low=-np.inf, high=np.inf):
        rows.append(coefficients)
        lows.append(low)
        highs.append(high)

    # q is positive exactly when the potential vertex is active.
    for u in range(N):
        add({q0 + u: 1, a0 + u: -1}, low=0)
        add({q0 + u: 1, a0 + u: -denominator}, high=0)

    # Sort weights within each layer.  This is a safe relabeling symmetry cut.
    for layer in range(LAYERS):
        for j in range(WIDTH - 1):
            add(
                {
                    q0 + vertex(layer, j): 1,
                    q0 + vertex(layer, j + 1): -1,
                },
                high=0,
            )
        add(
            {a0 + vertex(layer, j): 1 for j in range(WIDTH)},
            low=1,
        )

    # An edge has two active endpoints, and z=e*q is exact when e is binary.
    for k, (u, v) in enumerate(pairs):
        edge = e0 + k
        add({edge: 1, a0 + u: -1}, high=0)
        add({edge: 1, a0 + v: -1}, high=0)
        for receiver, sender in ((u, v), (v, u)):
            z = z_index[(receiver, sender)]
            add({z: 1, q0 + sender: -1}, high=0)
            add({z: 1, edge: -denominator}, high=0)
            add(
                {q0 + sender: 1, edge: denominator, z: -1},
                high=denominator,
            )

    # Every active vertex has normalized weighted open degree at least one.
    for u in range(N):
        coefficients = {a0 + u: -denominator}
        for _, v in incident[u]:
            coefficients[z_index[(u, v)]] = 1
        add(coefficients, low=0)

    # Exact K7 exclusion: any clique lies in one consecutive two-layer union.
    # Such a union has eight potential vertices, giving eight seven-subsets.
    for i in range(LAYERS):
        union = vertices_by_layer[i] + vertices_by_layer[(i + 1) % LAYERS]
        for seven in combinations(union, 7):
            coefficients = {
                e0 + pair_index[tuple(sorted(pair))]: 1
                for pair in combinations(seven, 2)
            }
            assert len(coefficients) == 21
            add(coefficients, high=20)

    # Each layer boundary is used.  This is necessary for a periodic chain,
    # although it does not by itself certify connectivity of all vertices.
    for i in range(LAYERS):
        coefficients = {}
        for u in vertices_by_layer[i]:
            for v in vertices_by_layer[(i + 1) % LAYERS]:
                coefficients[e0 + pair_index[tuple(sorted((u, v)))]] = 1
        add(coefficients, low=1)

    # Strict target sum(q)/denominator < 39/8, expressed integrally.
    mass_cap = (39 * denominator - (0 if allow_equality else 1)) // 8
    add({q0 + u: 1 for u in range(N)}, high=mass_cap)

    # Rotate so layer zero has minimum total weight, then reflect so A1<=A12.
    for i in range(1, LAYERS):
        coefficients = {
            q0 + vertex(0, j): 1 for j in range(WIDTH)
        }
        for j in range(WIDTH):
            key = q0 + vertex(i, j)
            coefficients[key] = coefficients.get(key, 0) - 1
        add(coefficients, high=0)
    coefficients = {}
    for j in range(WIDTH):
        coefficients[q0 + vertex(1, j)] = 1
        coefficients[q0 + vertex(12, j)] = -1
    add(coefficients, high=0)

    rr = []
    cc = []
    data = []
    for row_number, row in enumerate(rows):
        for column, value in row.items():
            rr.append(row_number)
            cc.append(column)
            data.append(value)
    matrix = coo_matrix((data, (rr, cc)), shape=(len(rows), nvar)).tocsc()

    objective = np.zeros(nvar)
    objective[q0 : q0 + N] = 1
    result = milp(
        objective,
        integrality=integrality,
        bounds=Bounds(lower, upper),
        constraints=LinearConstraint(matrix, np.array(lows), np.array(highs)),
        options={
            "disp": True,
            "time_limit": time_limit,
            "mip_rel_gap": mip_gap,
            "presolve": True,
        },
    )

    print(f"denominator: {denominator}")
    print(f"variables: {nvar}; constraints: {len(rows)}")
    print(f"numerator cap: {mass_cap}")
    print(f"equality allowed: {allow_equality}")
    print(f"solver status: {result.status}")
    print(f"solver message: {result.message}")
    if result.fun is not None:
        print(f"solver objective: {result.fun:.12g}")
    if result.mip_gap is not None:
        print(f"solver mip gap: {result.mip_gap:.12g}")
    if result.x is None:
        print("exact witness check: no incumbent")
        return

    values = np.rint(result.x).astype(np.int64)
    weights = values[q0 : q0 + N].tolist()
    active = values[a0 : a0 + N].tolist()
    chosen_edges = {
        pairs[k] for k in range(len(pairs)) if values[e0 + k] == 1
    }

    # Independent integer checks of the mathematically relevant conditions.
    assert all((weight >= 1) == bool(active[u]) for u, weight in enumerate(weights))
    assert sum(weights) <= mass_cap
    assert all(any(active[vertex(i, j)] for j in range(WIDTH)) for i in range(LAYERS))
    assert all(
        (u, v) not in chosen_edges or (active[u] and active[v]) for u, v in pairs
    )
    degrees = []
    for u in range(N):
        degree = sum(
            weights[v]
            for v in range(N)
            if tuple(sorted((u, v))) in chosen_edges
        )
        degrees.append(degree)
        if active[u]:
            assert degree >= denominator
    clique7_count = 0
    for i in range(LAYERS):
        union = vertices_by_layer[i] + vertices_by_layer[(i + 1) % LAYERS]
        for seven in combinations(union, 7):
            if all(tuple(sorted(pair)) in chosen_edges for pair in combinations(seven, 2)):
                clique7_count += 1
    assert clique7_count == 0
    for i in range(LAYERS):
        assert any(
            tuple(sorted((u, v))) in chosen_edges
            for u in vertices_by_layer[i]
            for v in vertices_by_layer[(i + 1) % LAYERS]
        )

    # Component diagnostics, including the within-period graph with wrap edges
    # (layer 12--0) removed.  These are reported, not assumed by the MILP.
    def components(remove_wrap):
        remaining = {u for u in range(N) if active[u]}
        answer = []
        while remaining:
            stack = [next(iter(remaining))]
            component = set(stack)
            remaining -= component
            while stack:
                u = stack.pop()
                for v in list(remaining):
                    edge = tuple(sorted((u, v)))
                    if edge not in chosen_edges:
                        continue
                    if remove_wrap and {layer_of(u), layer_of(v)} == {0, 12}:
                        continue
                    remaining.remove(v)
                    component.add(v)
                    stack.append(v)
            answer.append(sorted(component))
        return answer

    all_components = components(False)
    open_components = components(True)
    positive_degrees = [degrees[u] for u in range(N) if active[u]]
    print("exact witness check: passed")
    print(f"exact mass numerator: {sum(weights)}")
    print(f"active vertices: {sum(active)}")
    print(f"chosen edges: {len(chosen_edges)}")
    print(f"minimum weighted degree numerator: {min(positive_degrees)}")
    print(f"K7 count: {clique7_count}")
    print(f"quotient component sizes: {[len(c) for c in all_components]}")
    print(f"open-period component sizes: {[len(c) for c in open_components]}")
    print("weights by layer:")
    for i in range(LAYERS):
        print(" ".join(map(str, weights[WIDTH * i : WIDTH * (i + 1)])))
    print("chosen edge indices (zero-based vertices):")
    print(" ".join(f"{u}-{v}" for u, v in sorted(chosen_edges)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--denominator", type=int, choices=(40, 80), required=True)
    parser.add_argument("--time-limit", type=float, default=300.0)
    parser.add_argument("--mip-gap", type=float, default=0.0)
    parser.add_argument("--allow-equality", action="store_true")
    arguments = parser.parse_args()
    build_and_solve(
        arguments.denominator,
        arguments.time_limit,
        arguments.mip_gap,
        arguments.allow_equality,
    )
