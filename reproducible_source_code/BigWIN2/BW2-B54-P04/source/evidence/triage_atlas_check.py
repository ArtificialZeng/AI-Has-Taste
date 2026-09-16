"""Exact finite triage check of 2*b(G)-2 <= gamma_R(G).

NetworkX's graph atlas contains one representative of every unlabeled graph on
at most seven vertices. Both optima are obtained by exhaustive finite search.
"""

from itertools import product

import networkx as nx


def roman_number(graph):
    vertices = list(graph)
    position = {vertex: i for i, vertex in enumerate(vertices)}
    feasible_weights = []
    for labels in product((0, 1, 2), repeat=len(vertices)):
        if all(
            labels[i] != 0
            or any(labels[position[u]] == 2 for u in graph.neighbors(vertex))
            for i, vertex in enumerate(vertices)
        ):
            feasible_weights.append(sum(labels))
    return min(feasible_weights)


def burning_number(graph):
    vertices = list(graph)
    distances = dict(nx.all_pairs_shortest_path_length(graph))
    order = len(vertices)
    for length in range(1, order + 1):
        balls = {
            (round_index, source): {
                vertex
                for vertex in vertices
                if distances[source][vertex] <= length - 1 - round_index
            }
            for round_index in range(length)
            for source in vertices
        }

        def search(round_index, sources, covered):
            if round_index == length:
                return tuple(sources) if len(covered) == order else None
            for source in vertices:
                if all(
                    distances[old_source][source] >= round_index - old_round
                    for old_round, old_source in enumerate(sources)
                ):
                    answer = search(
                        round_index + 1,
                        sources + [source],
                        covered | balls[round_index, source],
                    )
                    if answer is not None:
                        return answer
            return None

        witness = search(0, [], set())
        if witness is not None:
            return length, witness
    raise AssertionError("No burning sequence found")


max_margin_by_order = {}
first_equality_by_order = {}
checked = 0
equalities = 0
counterexamples = []

for graph in nx.graph_atlas_g():
    order = len(graph)
    if order < 2 or not nx.is_connected(graph):
        continue
    burning, witness = burning_number(graph)
    roman = roman_number(graph)
    margin = 2 * burning - 2 - roman
    checked += 1
    max_margin_by_order[order] = max(
        max_margin_by_order.get(order, -10**9), margin
    )
    if margin == 0:
        equalities += 1
        first_equality_by_order.setdefault(
            order, nx.to_graph6_bytes(graph, header=False).decode().strip()
        )
    if margin > 0:
        counterexamples.append(
            (
                order,
                nx.to_graph6_bytes(graph, header=False).decode().strip(),
                burning,
                roman,
                witness,
            )
        )

print("networkx", nx.__version__)
print("connected_unlabeled_graphs_checked", checked)
print("orders", sorted(max_margin_by_order))
print("max_violation_margin_by_order", max_margin_by_order)
print("equalities", equalities)
print("first_equality_graph6_by_order", first_equality_by_order)
print("counterexamples", counterexamples)
