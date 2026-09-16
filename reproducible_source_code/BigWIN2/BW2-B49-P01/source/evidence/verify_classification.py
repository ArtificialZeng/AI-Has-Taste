#!/usr/bin/env python3
"""Exact exhaustive classifier for five-edge bondage sets of the labeled graph T.

The calculation uses only integer bit masks.  It checks the graph, independently
enumerates all dominating sets of cardinality at most eight, tests all C(36,5)
edge sets, obtains the full abstract automorphism group with VF2, and checks the
resulting orbit partition.  For every orbit representative it also supplies and
checks an explicit dominating nine-set after deletion.

Run from the project root with

    python3 evidence/verify_classification.py

It writes deterministic certificates to evidence/classification.json and
evidence/minimum-bondage-sets.txt.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path

import networkx as nx


VERTICES = tuple(range(24))
EDGES = (
    (0, 1), (0, 2), (0, 3), (1, 4), (1, 5), (2, 6), (2, 7), (3, 4),
    (3, 8), (4, 9), (5, 10), (5, 11), (6, 11), (6, 12), (7, 12),
    (7, 13), (8, 13), (8, 14), (9, 15), (9, 16), (10, 16),
    (10, 17), (11, 17), (12, 18), (13, 19), (14, 15), (14, 19),
    (15, 20), (16, 20), (17, 21), (18, 21), (18, 22), (19, 22),
    (20, 23), (21, 23), (22, 23),
)
ALL_VERTICES = (1 << 24) - 1
EDGE_ID = {edge: i for i, edge in enumerate(EDGES)}


def mask_from_indices(indices):
    ans = 0
    for i in indices:
        ans |= 1 << i
    return ans


def indices_from_mask(mask):
    return tuple(i for i in range(mask.bit_length()) if (mask >> i) & 1)


def edge_tuple(mask):
    return tuple(EDGES[i] for i in indices_from_mask(mask))


def json_edges(mask):
    return [list(e) for e in edge_tuple(mask)]


def json_vertices(mask):
    return list(indices_from_mask(mask))


def dominates(vertex_mask, closed_neighborhoods):
    covered = 0
    pending = vertex_mask
    while pending:
        bit = pending & -pending
        covered |= closed_neighborhoods[bit.bit_length() - 1]
        pending ^= bit
    return covered == ALL_VERTICES


def graph_data():
    assert len(EDGES) == 36
    assert len(set(EDGES)) == 36
    assert all(0 <= u < v < 24 for u, v in EDGES)
    assert list(EDGES) == sorted(EDGES)

    adjacency = [0] * 24
    incident = [[] for _ in VERTICES]
    for i, (u, v) in enumerate(EDGES):
        adjacency[u] |= 1 << v
        adjacency[v] |= 1 << u
        incident[u].append((v, i))
        incident[v].append((u, i))
    degrees = [m.bit_count() for m in adjacency]
    assert degrees == [3] * 24

    reached = 1
    previous = -1
    while reached != previous:
        previous = reached
        frontier = reached
        while frontier:
            bit = frontier & -frontier
            reached |= adjacency[bit.bit_length() - 1]
            frontier ^= bit
    assert reached == ALL_VERTICES
    return adjacency, incident, [adjacency[v] | (1 << v) for v in VERTICES]


def enumerate_minimum_dominating_sets(closed_neighborhoods):
    counts = {}
    dominating_eights = []
    for size in range(9):
        count = 0
        for combination in itertools.combinations(VERTICES, size):
            dmask = mask_from_indices(combination)
            if dominates(dmask, closed_neighborhoods):
                count += 1
                if size == 8:
                    dominating_eights.append(dmask)
        counts[size] = count
    assert all(counts[k] == 0 for k in range(8))
    assert counts[8] == 1767
    return counts, dominating_eights


def destruction_clauses(dmask, incident):
    """Minimal edge masks whose deletion makes this D fail at one outside vertex."""
    clauses = set()
    for v in VERTICES:
        if (dmask >> v) & 1:
            continue
        cross = 0
        for neighbor, edge_id in incident[v]:
            if (dmask >> neighbor) & 1:
                cross |= 1 << edge_id
        assert cross
        clauses.add(cross)
    return tuple(sorted(clauses, key=lambda m: (m.bit_count(), indices_from_mask(m))))


def classify_five_sets(dominating_eights, incident):
    clause_families = [destruction_clauses(d, incident) for d in dominating_eights]

    # Families with many one-edge clauses generally prune the live candidates
    # fastest.  This affects runtime only, not the enumerated domain or result.
    def priority(clauses):
        singles = sum(1 for c in clauses if c.bit_count() == 1)
        pairs = sum(1 for c in clauses if c.bit_count() == 2)
        return (singles, pairs, len(clauses))

    clause_families.sort(key=priority, reverse=True)
    candidates = [mask_from_indices(c) for c in itertools.combinations(range(36), 5)]
    assert len(candidates) == 376_992
    shrink_trace = [[0, len(candidates)]]

    for step, clauses in enumerate(clause_families, 1):
        single_union = 0
        larger = []
        for clause in clauses:
            if clause.bit_count() == 1:
                single_union |= clause
            else:
                larger.append(clause)

        kept = []
        for fmask in candidates:
            killed = bool(fmask & single_union)
            if not killed:
                for clause in larger:
                    if fmask & clause == clause:
                        killed = True
                        break
            if killed:
                kept.append(fmask)
        candidates = kept
        if step <= 10 or step % 100 == 0 or step == len(clause_families):
            shrink_trace.append([step, len(candidates)])
        assert candidates, "the published five-edge witness should survive"

    # Replay against all original, unsorted dominating sets.
    for fmask in candidates:
        for dmask in dominating_eights:
            assert any((fmask & c) == c for c in destruction_clauses(dmask, incident))
    return candidates, shrink_trace


def compose(p, q):
    """Permutation p after q."""
    return tuple(p[q[v]] for v in VERTICES)


def generated_subgroup(generators):
    identity = VERTICES
    closure = {identity}
    queue = [identity]
    while queue:
        h = queue.pop()
        for g in generators:
            product = compose(h, g)
            if product not in closure:
                closure.add(product)
                queue.append(product)
    return closure


def automorphism_data():
    graph = nx.Graph()
    graph.add_nodes_from(VERTICES)
    graph.add_edges_from(EDGES)
    automorphisms = []
    for mapping in nx.algorithms.isomorphism.GraphMatcher(graph, graph).isomorphisms_iter():
        p = tuple(mapping[v] for v in VERTICES)
        assert sorted(p) == list(VERTICES)
        image_edges = {tuple(sorted((p[u], p[v]))) for u, v in EDGES}
        assert image_edges == set(EDGES)
        automorphisms.append(p)
    automorphisms = sorted(set(automorphisms))
    assert len(automorphisms) == 48

    generators = []
    subgroup = generated_subgroup(generators)
    for p in automorphisms:
        if p not in subgroup:
            generators.append(p)
            subgroup = generated_subgroup(generators)
        if len(subgroup) == len(automorphisms):
            break
    assert subgroup == set(automorphisms)

    edge_actions = []
    for p in automorphisms:
        action = []
        for u, v in EDGES:
            image = tuple(sorted((p[u], p[v])))
            action.append(EDGE_ID[image])
        assert sorted(action) == list(range(36))
        edge_actions.append(tuple(action))
    return automorphisms, generators, edge_actions


def image_edge_mask(fmask, action):
    image = 0
    for edge_id in indices_from_mask(fmask):
        image |= 1 << action[edge_id]
    return image


def orbit_partition(candidates, automorphisms, edge_actions):
    member_set = set(candidates)
    unseen = set(candidates)
    records = []
    while unseen:
        seed = min(unseen, key=indices_from_mask)
        orbit = {image_edge_mask(seed, action) for action in edge_actions}
        assert orbit <= member_set
        representative = min(orbit, key=indices_from_mask)
        stabilizer = sum(
            1 for action in edge_actions if image_edge_mask(representative, action) == representative
        )
        assert len(orbit) * stabilizer == len(automorphisms)
        unseen.difference_update(orbit)
        records.append(
            {
                "representative_mask": representative,
                "representative": json_edges(representative),
                "orbit_size": len(orbit),
                "stabilizer_size": stabilizer,
            }
        )
    records.sort(key=lambda r: indices_from_mask(r["representative_mask"]))
    assert sum(r["orbit_size"] for r in records) == len(candidates)
    return records


def reduced_closed_neighborhoods(fmask, adjacency):
    reduced = list(adjacency)
    for edge_id in indices_from_mask(fmask):
        u, v = EDGES[edge_id]
        reduced[u] &= ~(1 << v)
        reduced[v] &= ~(1 << u)
    return [reduced[v] | (1 << v) for v in VERTICES]


def attach_nine_witnesses(records, adjacency):
    unresolved = set(range(len(records)))
    witness_masks = [None] * len(records)
    reduced_neighborhoods = [
        reduced_closed_neighborhoods(r["representative_mask"], adjacency) for r in records
    ]
    tested = 0
    for combination in itertools.combinations(VERTICES, 9):
        tested += 1
        dmask = mask_from_indices(combination)
        for record_id in tuple(unresolved):
            if dominates(dmask, reduced_neighborhoods[record_id]):
                witness_masks[record_id] = dmask
                unresolved.remove(record_id)
        if not unresolved:
            break
    assert not unresolved
    for record, dmask, closed in zip(records, witness_masks, reduced_neighborhoods):
        assert dmask is not None and dmask.bit_count() == 9
        assert dominates(dmask, closed)
        record["gamma_after_deletion"] = 9
        record["dominating_nine_witness"] = json_vertices(dmask)
        del record["representative_mask"]
    return tested


def main():
    project = Path(__file__).resolve().parent.parent
    evidence = project / "evidence"
    adjacency, incident, closed = graph_data()
    domination_counts, dominating_eights = enumerate_minimum_dominating_sets(closed)
    candidates, shrink_trace = classify_five_sets(dominating_eights, incident)

    # The witness quoted in the source is edges 02,14,15,26,27.
    source_witness_edges = ((0, 2), (1, 4), (1, 5), (2, 6), (2, 7))
    source_witness = mask_from_indices(EDGE_ID[e] for e in source_witness_edges)
    assert source_witness in set(candidates)

    automorphisms, generators, edge_actions = automorphism_data()
    records = orbit_partition(candidates, automorphisms, edge_actions)
    nine_sets_tested = attach_nine_witnesses(records, adjacency)

    lines = []
    for fmask in sorted(candidates, key=indices_from_mask):
        lines.append(" ".join(f"{u}-{v}" for u, v in edge_tuple(fmask)))
    family_text = "\n".join(lines) + "\n"
    family_path = evidence / "minimum-bondage-sets.txt"
    family_path.write_text(family_text, encoding="ascii")
    family_sha256 = hashlib.sha256(family_text.encode("ascii")).hexdigest()

    result = {
        "method": "exact integer bit-mask exhaustive enumeration",
        "graph": {
            "vertices": 24,
            "edges": 36,
            "simple": True,
            "connected": True,
            "degree_sequence": [3] * 24,
        },
        "dominating_set_counts_by_size_0_through_8": [domination_counts[k] for k in range(9)],
        "gamma_T": 8,
        "five_edge_subsets_tested": 376_992,
        "minimum_bondage_set_count": len(candidates),
        "minimum_bondage_family_file": "evidence/minimum-bondage-sets.txt",
        "minimum_bondage_family_sha256": family_sha256,
        "candidate_shrink_trace": shrink_trace,
        "source_witness_present": True,
        "automorphism_group_order": len(automorphisms),
        "automorphism_generators": [list(p) for p in generators],
        "generator_count": len(generators),
        "orbit_count": len(records),
        "orbit_size_sum": sum(r["orbit_size"] for r in records),
        "size_nine_combinations_scanned_until_all_orbits_had_witnesses": nine_sets_tested,
        "orbits": records,
    }
    output = json.dumps(result, indent=2, sort_keys=True) + "\n"
    (evidence / "classification.json").write_text(output, encoding="utf-8")
    print(output, end="")


if __name__ == "__main__":
    main()
