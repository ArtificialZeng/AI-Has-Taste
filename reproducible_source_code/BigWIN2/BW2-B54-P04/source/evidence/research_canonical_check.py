"""Exact finite sanity check for the canonical-RDF burning proof.

The NetworkX graph atlas contains one unlabeled representative of every graph
on at most seven vertices.  For every connected graph of orders 2--7, this
script exhaustively chooses a minimum-weight RDF having the fewest 1-labels,
checks the structural reductions used in research_proof.md, and simulates the
proof's legal-source burning strategy.  This checks implementation/timing on a
finite domain; research_proof.md supplies the universal argument.
"""

from itertools import product

import networkx as nx


def canonical_rdf(graph):
    vertices = list(graph)
    position = {vertex: i for i, vertex in enumerate(vertices)}
    best = None
    for labels in product((0, 1, 2), repeat=len(vertices)):
        if not all(
            labels[i] != 0
            or any(labels[position[u]] == 2 for u in graph.neighbors(vertex))
            for i, vertex in enumerate(vertices)
        ):
            continue
        key = (sum(labels), labels.count(1), labels)
        if best is None or key < best[0]:
            best = (key, labels)
    assert best is not None
    return dict(zip(vertices, best[1], strict=True))


def proof_strategy(graph, labels):
    vertices = list(graph)
    twos = {v for v in vertices if labels[v] == 2}
    ones = {v for v in vertices if labels[v] == 1}
    a, c = len(twos), len(ones)
    target_rounds = a + c // 2 + 1
    burned = set()
    sources = []

    for round_number in range(1, target_rounds + 1):
        old_burned = set(burned)
        unburned = set(vertices) - old_burned
        if not unburned:
            break

        if round_number <= a and (twos - old_burned):
            source = min(twos - old_burned)
        elif c == 1 and round_number == a + 1 and (ones - old_burned):
            source = min(ones - old_burned)
        else:
            source = min(unburned)

        assert source not in old_burned
        sources.append(source)
        spread = {
            neighbor
            for vertex in old_burned
            for neighbor in graph.neighbors(vertex)
        }
        burned = old_burned | spread | {source}

        if round_number == a:
            assert twos <= burned

    return target_rounds, sources, burned


checked = 0
case_counts = {"c=0": 0, "c=1": 0, "c>=2": 0}
max_slack = 0

for graph in nx.graph_atlas_g():
    if len(graph) < 2 or not nx.is_connected(graph):
        continue
    labels = canonical_rdf(graph)
    twos = {v for v in graph if labels[v] == 2}
    ones = {v for v in graph if labels[v] == 1}

    assert twos
    assert not any(
        graph.has_edge(one, two) for one in ones for two in twos
    )
    assert all(not graph.has_edge(u, v) for u in ones for v in ones if u < v)

    distance_to_twos = nx.multi_source_dijkstra_path_length(graph, twos)
    assert all(distance_to_twos[v] <= 1 for v in graph if labels[v] == 0)
    assert all(distance_to_twos[v] == 2 for v in ones)

    target_rounds, sources, burned = proof_strategy(graph, labels)
    assert burned == set(graph)
    assert len(sources) <= target_rounds

    c = len(ones)
    case = "c=0" if c == 0 else "c=1" if c == 1 else "c>=2"
    case_counts[case] += 1
    checked += 1
    max_slack = max(max_slack, target_rounds - len(sources))

print("networkx", nx.__version__)
print("connected_unlabeled_graphs_checked", checked)
print("orders", [2, 3, 4, 5, 6, 7])
print("canonical_RDF_case_counts", case_counts)
print("all_structural_assertions", True)
print("all_strategy_simulations_finished_by_target", True)
print("max_unused_rounds_after_early_finish", max_slack)
