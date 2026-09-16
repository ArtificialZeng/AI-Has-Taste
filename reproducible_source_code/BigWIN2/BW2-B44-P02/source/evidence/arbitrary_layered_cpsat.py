#!/usr/bin/env python3
"""Exact-grid CP-SAT search for arbitrary sparse 13-by-4 layered periods.

The mathematical model is the same as arbitrary_layered_milp.py, but native
integer product constraints avoid its weak big-M LP relaxation.  Solver
nonexistence or timeout is never interpreted as mathematical infeasibility.
"""

import argparse
from itertools import combinations

from ortools.sat.python import cp_model


LAYERS = 13
WIDTH = 4
N = LAYERS * WIDTH


def vertex(layer, position):
    return WIDTH * layer + position


def solve(denominator, time_limit, allow_equality):
    by_layer = [[vertex(i, j) for j in range(WIDTH)] for i in range(LAYERS)]
    pairs = []
    for layer in by_layer:
        pairs.extend(combinations(layer, 2))
    for i in range(LAYERS):
        pairs.extend(
            (u, v) for u in by_layer[i] for v in by_layer[(i + 1) % LAYERS]
        )
    pairs = [tuple(sorted(pair)) for pair in pairs]
    assert len(pairs) == len(set(pairs)) == 286
    pair_set = set(pairs)

    model = cp_model.CpModel()
    q = [model.new_int_var(0, denominator, f"q_{u}") for u in range(N)]
    active = [model.new_bool_var(f"a_{u}") for u in range(N)]
    edge = {pair: model.new_bool_var(f"e_{pair[0]}_{pair[1]}") for pair in pairs}
    product = {}

    for u in range(N):
        model.add(q[u] >= active[u])
        model.add(q[u] <= denominator * active[u])
    for i in range(LAYERS):
        model.add(sum(active[u] for u in by_layer[i]) >= 1)
        for j in range(WIDTH - 1):
            model.add(q[vertex(i, j)] <= q[vertex(i, j + 1)])

    incident = [[] for _ in range(N)]
    for u, v in pairs:
        model.add(edge[(u, v)] <= active[u])
        model.add(edge[(u, v)] <= active[v])
        for receiver, sender in ((u, v), (v, u)):
            z = model.new_int_var(0, denominator, f"z_{receiver}_{sender}")
            model.add_multiplication_equality(z, (edge[(u, v)], q[sender]))
            product[(receiver, sender)] = z
            incident[receiver].append(sender)
    for u in range(N):
        model.add(
            sum(product[(u, v)] for v in incident[u])
            >= denominator * active[u]
        )

    for i in range(LAYERS):
        union = by_layer[i] + by_layer[(i + 1) % LAYERS]
        for seven in combinations(union, 7):
            model.add(
                sum(edge[tuple(sorted(pair))] for pair in combinations(seven, 2))
                <= 20
            )
    for i in range(LAYERS):
        model.add(
            sum(
                edge[tuple(sorted((u, v)))]
                for u in by_layer[i]
                for v in by_layer[(i + 1) % LAYERS]
            )
            >= 1
        )

    cap = (39 * denominator - (0 if allow_equality else 1)) // 8
    model.add(sum(q) <= cap)
    for i in range(1, LAYERS):
        model.add(sum(q[u] for u in by_layer[0]) <= sum(q[u] for u in by_layer[i]))
    model.add(sum(q[u] for u in by_layer[1]) <= sum(q[u] for u in by_layer[12]))
    model.minimize(sum(q))

    # A model-control hint: 3 active vertices of weight denominator/8 in each
    # layer, with all available edges among them.  It is used only when the
    # equality cap admits this known exact point.
    if allow_equality:
        assert denominator % 8 == 0
        unit = denominator // 8
        for i in range(LAYERS):
            for j in range(WIDTH):
                u = vertex(i, j)
                value = 0 if j == 0 else unit
                model.add_hint(q[u], value)
                model.add_hint(active[u], int(j != 0))
        for u, v in pairs:
            model.add_hint(edge[(u, v)], int(q_value(u, unit) and q_value(v, unit)))

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = time_limit
    solver.parameters.num_search_workers = 1
    solver.parameters.log_search_progress = True
    status = solver.solve(model)
    print(f"denominator: {denominator}")
    print(f"numerator cap: {cap}")
    print(f"equality allowed: {allow_equality}")
    print(f"solver status: {solver.status_name(status)}")
    print(f"wall time: {solver.wall_time:.6f}")
    print(f"branches: {solver.num_branches}")
    print(f"conflicts: {solver.num_conflicts}")
    print(f"best objective bound: {solver.best_objective_bound}")
    if status not in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        print("exact witness check: no incumbent")
        return

    weights = [solver.value(item) for item in q]
    actives = [solver.value(item) for item in active]
    chosen = {pair for pair in pairs if solver.value(edge[pair])}
    assert all((weights[u] >= 1) == bool(actives[u]) for u in range(N))
    assert sum(weights) <= cap
    assert all(any(actives[u] for u in by_layer[i]) for i in range(LAYERS))
    weighted_degrees = []
    for u in range(N):
        degree = sum(
            weights[v]
            for v in range(N)
            if u != v and tuple(sorted((u, v))) in chosen
        )
        weighted_degrees.append(degree)
        if actives[u]:
            assert degree >= denominator
    clique7_count = 0
    for i in range(LAYERS):
        union = by_layer[i] + by_layer[(i + 1) % LAYERS]
        for seven in combinations(union, 7):
            if all(tuple(sorted(pair)) in chosen for pair in combinations(seven, 2)):
                clique7_count += 1
    assert clique7_count == 0
    for i in range(LAYERS):
        assert any(
            tuple(sorted((u, v))) in chosen
            for u in by_layer[i]
            for v in by_layer[(i + 1) % LAYERS]
        )

    def component_sizes(remove_wrap):
        remaining = {u for u in range(N) if actives[u]}
        sizes = []
        while remaining:
            stack = [remaining.pop()]
            size = 0
            while stack:
                u = stack.pop()
                size += 1
                for v in list(remaining):
                    if tuple(sorted((u, v))) not in chosen:
                        continue
                    if remove_wrap and {u // WIDTH, v // WIDTH} == {0, 12}:
                        continue
                    remaining.remove(v)
                    stack.append(v)
            sizes.append(size)
        return sorted(sizes, reverse=True)

    print("exact witness check: passed")
    print(f"exact mass numerator: {sum(weights)}")
    print(f"active vertices: {sum(actives)}")
    print(f"chosen edges: {len(chosen)}")
    print(
        "minimum weighted degree numerator: "
        f"{min(weighted_degrees[u] for u in range(N) if actives[u])}"
    )
    print(f"K7 count: {clique7_count}")
    print(f"quotient component sizes: {component_sizes(False)}")
    print(f"open-period component sizes: {component_sizes(True)}")
    print("weights by layer:")
    for i in range(LAYERS):
        print(" ".join(map(str, weights[WIDTH * i : WIDTH * (i + 1)])))
    print("chosen edge indices (zero-based vertices):")
    print(" ".join(f"{u}-{v}" for u, v in sorted(chosen)))


def q_value(u, unit):
    return 0 if u % WIDTH == 0 else unit


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--denominator", required=True, type=int, choices=(40, 80))
    parser.add_argument("--time-limit", type=float, default=300.0)
    parser.add_argument("--allow-equality", action="store_true")
    args = parser.parse_args()
    solve(args.denominator, args.time_limit, args.allow_equality)
