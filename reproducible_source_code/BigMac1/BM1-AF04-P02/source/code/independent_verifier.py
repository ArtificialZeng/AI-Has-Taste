#!/usr/bin/env python3
"""Fail-closed verifier for the STS(15) Pasch quotient certificate.

Trust base: Python integer/set/list semantics and the serialized certificate.
This module neither imports the discovery program nor invokes nauty.  Pasches
are reconstructed from alternating cycle graphs, not by the discovery
program's four-block-subset scan.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import sys
from collections import Counter, deque
from pathlib import Path

N = 15


class VerificationError(Exception):
    pass


def reject(message):
    raise VerificationError(message)


def no_duplicate_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            reject(f"duplicate JSON key {key!r}")
        result[key] = value
    return result


def load_json(path):
    try:
        with open(path, encoding="utf-8") as stream:
            return json.load(stream, object_pairs_hook=no_duplicate_object)
    except VerificationError:
        raise
    except Exception as exc:
        reject(f"cannot parse {path}: {exc}")


def require_keys(obj, required, context, allow_extra=False):
    if not isinstance(obj, dict):
        reject(f"{context} must be an object")
    missing = set(required) - set(obj)
    extra = set(obj) - set(required)
    if missing or (extra and not allow_extra):
        reject(
            f"{context} keys mismatch; missing={sorted(missing)}, extra={sorted(extra)}"
        )


def parse_blocks(raw, context):
    if not isinstance(raw, list) or len(raw) != 35:
        reject(f"{context} must contain exactly 35 blocks")
    blocks = []
    for i, block in enumerate(raw):
        if (
            not isinstance(block, list)
            or len(block) != 3
            or any(type(x) is not int for x in block)
        ):
            reject(f"{context} block {i} is not a three-integer list")
        triple = tuple(block)
        if tuple(sorted(triple)) != triple:
            reject(f"{context} block {i} is not strictly normalized")
        if len(set(triple)) != 3 or triple[0] < 0 or triple[-1] >= N:
            reject(f"{context} block {i} has invalid points")
        blocks.append(triple)
    if blocks != sorted(blocks) or len(set(blocks)) != 35:
        reject(f"{context} blocks are not sorted and distinct")
    pairs = Counter(
        pair for block in blocks for pair in itertools.combinations(block, 2)
    )
    if len(pairs) != 105 or set(pairs.values()) != {1}:
        reject(f"{context} is not an STS(15): pair coverage is not one")
    return tuple(blocks)


def operation_table(blocks):
    operation = [[None] * N for _ in range(N)]
    for x in range(N):
        operation[x][x] = x
    for a, b, c in blocks:
        operation[a][b] = operation[b][a] = c
        operation[a][c] = operation[c][a] = b
        operation[b][c] = operation[c][b] = a
    if any(value is None for row in operation for value in row):
        reject("incomplete Steiner quasigroup operation table")
    return operation


def cycle_pasches(blocks):
    """Find Pasches as 4-cycles in the union of two derived matchings."""
    operation = operation_table(blocks)
    answer = set()
    for x in range(N):
        for y in range(x + 1, N):
            xy = operation[x][y]
            remaining = set(range(N)) - {x, y, xy}
            adjacency = {z: {operation[x][z], operation[y][z]} for z in remaining}
            if any(
                len(neighbors) != 2 or not neighbors <= remaining
                for neighbors in adjacency.values()
            ):
                reject("derived cycle graph is not 2-regular")
            seen = set()
            for start in sorted(remaining):
                if start in seen:
                    continue
                component = set()
                queue = [start]
                while queue:
                    z = queue.pop()
                    if z in component:
                        continue
                    component.add(z)
                    queue.extend(adjacency[z] - component)
                seen |= component
                if len(component) == 4:
                    configuration = set()
                    for z in component:
                        configuration.add(tuple(sorted((x, z, operation[x][z]))))
                        configuration.add(tuple(sorted((y, z, operation[y][z]))))
                    if len(configuration) != 4:
                        reject("a derived 4-cycle did not give four blocks")
                    answer.add(tuple(sorted(configuration)))
    return tuple(sorted(answer))


def pasch_mate(configuration):
    old = set(configuration)
    support = sorted(set().union(*map(set, old)))
    if len(old) != 4 or len(support) != 6:
        reject("malformed Pasch configuration in replay")
    pair_multiset = Counter(
        pair for block in old for pair in itertools.combinations(block, 2)
    )
    if set(pair_multiset.values()) != {1} or len(pair_multiset) != 12:
        reject("Pasch removed side does not cover 12 distinct pairs")
    mate = {
        triple
        for triple in itertools.combinations(support, 3)
        if triple not in old
        and all(pair in pair_multiset for pair in itertools.combinations(triple, 2))
    }
    if len(mate) != 4:
        reject("Pasch mate does not have four blocks")
    mate_pairs = Counter(
        pair for block in mate for pair in itertools.combinations(block, 2)
    )
    if mate_pairs != pair_multiset:
        reject("Pasch switch does not preserve exact pair multiplicities")
    return tuple(sorted(mate))


def switched_system(blocks, configuration):
    result = tuple(
        sorted((set(blocks) - set(configuration)) | set(pasch_mate(configuration)))
    )
    # Reuse the strict parser through a JSON-shaped copy.
    return parse_blocks(
        [list(block) for block in result], "reconstructed switched system"
    )


def point_signature(blocks, pasches=None):
    if pasches is None:
        pasches = cycle_pasches(blocks)
    point_counts = Counter()
    block_counts = Counter()
    for configuration in pasches:
        support = set().union(*map(set, configuration))
        point_counts.update(support)
        block_counts.update(configuration)
    # The sorted point-count multiset alone distinguishes all 80 released
    # classes.  The richer per-point colors below accelerate exact mappings.
    class_signature = (
        len(pasches),
        tuple(sorted(point_counts[x] for x in range(N))),
    )
    point_colors = []
    blocks_by_point = {
        x: [block for block in blocks if x in block] for x in range(N)
    }
    for x in range(N):
        local_block_counts = tuple(
            sorted(block_counts[block] for block in blocks_by_point[x])
        )
        neighbor_counts = []
        for block in blocks_by_point[x]:
            neighbor_counts.extend(point_counts[y] for y in block if y != x)
        point_colors.append(
            (point_counts[x], local_block_counts, tuple(sorted(neighbor_counts)))
        )
    return class_signature, tuple(point_colors)


def find_isomorphism(source, target):
    """Exact backtracking on Steiner quasigroup homomorphisms."""
    source_pasches = cycle_pasches(source)
    target_pasches = cycle_pasches(target)
    source_sig, source_colors = point_signature(source, source_pasches)
    target_sig, target_colors = point_signature(target, target_pasches)
    if source_sig != target_sig:
        return None
    if Counter(source_colors) != Counter(target_colors):
        return None
    source_op = operation_table(source)
    target_op = operation_table(target)

    def propagate(mapping):
        mapping = dict(mapping)
        changed = True
        while changed:
            changed = False
            inverse = {value: key for key, value in mapping.items()}
            if len(inverse) != len(mapping):
                return None
            for x, y in itertools.combinations(sorted(mapping), 2):
                z = source_op[x][y]
                image_z = target_op[mapping[x]][mapping[y]]
                if source_colors[z] != target_colors[image_z]:
                    return None
                if z in mapping:
                    if mapping[z] != image_z:
                        return None
                else:
                    if image_z in inverse:
                        return None
                    mapping[z] = image_z
                    changed = True
                    break
        return mapping

    def search(mapping):
        mapping = propagate(mapping)
        if mapping is None:
            return None
        if len(mapping) == N:
            image_blocks = {
                tuple(sorted(mapping[x] for x in block)) for block in source
            }
            return mapping if image_blocks == set(target) else None
        used = set(mapping.values())
        unmapped = [x for x in range(N) if x not in mapping]
        candidate_sets = {
            x: [
                y
                for y in range(N)
                if y not in used and target_colors[y] == source_colors[x]
            ]
            for x in unmapped
        }
        if any(not candidates for candidates in candidate_sets.values()):
            return None
        # Fewest candidates first; mapped-neighbor interaction breaks ties.
        x = min(
            unmapped,
            key=lambda z: (
                len(candidate_sets[z]),
                -sum(
                    source_op[z][m] in mapping
                    for m in mapping
                    if m != z
                ),
                z,
            ),
        )
        for y in candidate_sets[x]:
            result = search({**mapping, x: y})
            if result is not None:
                return result
        return None

    return search({})


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def bfs(adjacency, source):
    distance = [-1] * len(adjacency)
    predecessor = [-1] * len(adjacency)
    distance[source] = 0
    queue = deque([source])
    while queue:
        x = queue.popleft()
        for y in sorted(adjacency[x]):
            if distance[y] == -1:
                distance[y] = distance[x] + 1
                predecessor[y] = x
                queue.append(y)
    return distance, predecessor


def verify_bfs(ids, edges, result):
    index = {vertex: i for i, vertex in enumerate(ids)}
    adjacency = [set() for _ in ids]
    for x, y in edges:
        adjacency[index[x]].add(index[y])
        adjacency[index[y]].add(index[x])

    components = []
    unseen = set(range(len(ids)))
    while unseen:
        root = min(unseen)
        distances, _ = bfs(adjacency, root)
        component = {i for i, distance in enumerate(distances) if distance >= 0}
        components.append(sorted(component))
        unseen -= component
    components.sort(key=lambda c: (-len(c), [ids[i] for i in c]))
    component_ids = [[ids[i] for i in c] for c in components]
    if component_ids != result["components"]:
        reject("reported components differ from independent BFS components")
    if [len(c) for c in components] != result["component_sizes"]:
        reject("reported component sizes are wrong")

    eccentricities = {}
    diameter_pairs = []
    main = components[0]
    main_set = set(main)
    main_diameter = -1
    distance_rows = {}
    for source in main:
        distances, _ = bfs(adjacency, source)
        if {i for i, d in enumerate(distances) if d >= 0} != main_set:
            reject("all-pairs BFS did not stay on the main component")
        eccentricity = max(distances[i] for i in main)
        eccentricities[ids[source]] = eccentricity
        distance_rows[source] = distances
        main_diameter = max(main_diameter, eccentricity)
    for i, source in enumerate(main):
        for target in main[i + 1 :]:
            if distance_rows[source][target] == main_diameter:
                diameter_pairs.append([ids[source], ids[target]])
    isolated = components[1]
    if len(isolated) != 1:
        reject("expected one isolated component")
    eccentricities[ids[isolated[0]]] = 0
    if result["diameter"] != main_diameter:
        reject("reported diameter is wrong")
    if result["component_diameters"] != [main_diameter, 0]:
        reject("reported component diameters are wrong")
    if result["all_diameter_pairs"] != diameter_pairs:
        reject("reported diameter-pair list is wrong")
    if result["diameter_pair_count"] != len(diameter_pairs):
        reject("reported diameter-pair count is wrong")
    if result["diameter_pair"] != diameter_pairs[0]:
        reject("reported chosen diameter pair is not the first certified pair")

    u_id, v_id = result["diameter_pair"]
    u, v = index[u_id], index[v_id]
    distances, predecessor = bfs(adjacency, u)
    expected_row = [None if d < 0 else d for d in distances]
    if result["distance_row_from_first_endpoint"] != expected_row:
        reject("reported endpoint distance row is wrong")
    layers = [
        [ids[i] for i, d in enumerate(distances) if d == level]
        for level in range(main_diameter + 1)
    ]
    if result["bfs_layers_from_first_endpoint"] != layers:
        reject("reported BFS layer certificate is wrong")
    path = [v]
    while path[-1] != u:
        path.append(predecessor[path[-1]])
    path.reverse()
    path_ids = [ids[i] for i in path]
    if result["geodesic"] != path_ids:
        reject("reported deterministic geodesic is wrong")
    if len(path_ids) - 1 != main_diameter:
        reject("geodesic length does not equal the diameter")
    if result["eccentricities"] != {
        key: eccentricities[key] for key in sorted(eccentricities)
    }:
        reject("reported eccentricities are wrong")
    radius = min(eccentricities[ids[i]] for i in main)
    centers = sorted(ids[i] for i in main if eccentricities[ids[i]] == radius)
    if result["radius"] != radius or result["centers"] != centers:
        reject("reported radius or centers are wrong")
    degrees = sorted(len(row) for row in adjacency)
    if result["degree_sequence"] != degrees:
        reject("reported degree sequence is wrong")
    return {
        "component_sizes": [len(c) for c in components],
        "diameter": main_diameter,
        "diameter_pairs": diameter_pairs,
        "radius": radius,
    }


def verify(directory):
    directory = Path(directory)
    paths = {
        "representatives": directory / "representatives.json",
        "edges": directory / "quotient_edges.json",
        "occurrences": directory / "switch_occurrences.json",
        "result": directory / "result.json",
    }
    documents = {name: load_json(path) for name, path in paths.items()}
    reps_doc = documents["representatives"]
    edges_doc = documents["edges"]
    occurrences_doc = documents["occurrences"]
    result = documents["result"]

    require_keys(
        reps_doc,
        {"schema", "point_set", "canonicalizer", "construction", "vertices"},
        "representatives root",
    )
    if reps_doc["schema"] != "sts15-representatives-v1":
        reject("wrong representatives schema")
    if reps_doc["point_set"] != list(range(N)):
        reject("wrong point set")
    vertices_raw = reps_doc["vertices"]
    if not isinstance(vertices_raw, list) or len(vertices_raw) != 80:
        reject("certificate must contain exactly 80 vertices")
    expected_ids = [f"V{i:03d}" for i in range(80)]
    ids = []
    representatives = {}
    pasches_by_id = {}
    signatures = {}
    for i, vertex in enumerate(vertices_raw):
        require_keys(
            vertex,
            {"id", "blocks", "canonical_graph6", "pasch_count", "seed_role"},
            f"vertex {i}",
        )
        vertex_id = vertex["id"]
        if vertex_id != expected_ids[i]:
            reject(f"vertex {i} has noncanonical ID/order {vertex_id!r}")
        if not isinstance(vertex["canonical_graph6"], str) or not vertex[
            "canonical_graph6"
        ]:
            reject(f"{vertex_id} has malformed opaque canonical_graph6 field")
        if vertex["seed_role"] not in (None, "projective", "anti-Pasch"):
            reject(f"{vertex_id} has invalid seed_role")
        blocks = parse_blocks(vertex["blocks"], vertex_id)
        pasches = cycle_pasches(blocks)
        if type(vertex["pasch_count"]) is not int or vertex["pasch_count"] != len(
            pasches
        ):
            reject(f"{vertex_id} has wrong Pasch count")
        signature, _ = point_signature(blocks, pasches)
        if signature in signatures:
            reject(
                f"{vertex_id} and {signatures[signature]} have the same isomorphism invariant"
            )
        signatures[signature] = vertex_id
        ids.append(vertex_id)
        representatives[vertex_id] = blocks
        pasches_by_id[vertex_id] = pasches
    # Distinct isomorphism invariants prove pairwise nonisomorphism.
    if len(signatures) != 80:
        reject("representatives are not pairwise separated")

    require_keys(edges_doc, {"schema", "vertices", "edges"}, "edge root")
    if edges_doc["schema"] != "sts15-pasch-edges-v1":
        reject("wrong edge schema")
    if edges_doc["vertices"] != ids:
        reject("edge vertex order differs from representative order")
    raw_edges = edges_doc["edges"]
    if not isinstance(raw_edges, list):
        reject("edges must be a list")
    edges = []
    for i, edge in enumerate(raw_edges):
        if (
            not isinstance(edge, list)
            or len(edge) != 2
            or any(type(x) is not str for x in edge)
        ):
            reject(f"edge {i} is malformed")
        x, y = edge
        if x not in representatives or y not in representatives or not x < y:
            reject(f"edge {i} has invalid, looping, or unsorted endpoints")
        edges.append((x, y))
    if edges != sorted(set(edges)):
        reject("edge list is not sorted and duplicate-free")

    require_keys(occurrences_doc, {"schema", "rows"}, "occurrence root")
    if occurrences_doc["schema"] != "sts15-pasch-switch-occurrences-v1":
        reject("wrong occurrence schema")
    rows = occurrences_doc["rows"]
    if set(rows) != set(ids):
        reject("occurrence rows do not cover exactly the 80 vertices")

    reconstructed_edges = set()
    total_occurrences = 0
    for source_id in ids:
        row = rows[source_id]
        require_keys(
            row,
            {
                "pasch_count",
                "self_switch_occurrences",
                "distinct_targets_including_self",
                "switches",
            },
            f"occurrence row {source_id}",
        )
        configurations = pasches_by_id[source_id]
        if row["pasch_count"] != len(configurations):
            reject(f"{source_id} occurrence-row Pasch count is wrong")
        if not isinstance(row["switches"], list) or len(row["switches"]) != len(
            configurations
        ):
            reject(f"{source_id} occurrence-row length is wrong")
        replay_targets = []
        for number, (configuration, item) in enumerate(
            zip(configurations, row["switches"])
        ):
            require_keys(item, {"removed", "added", "target"}, f"switch item {source_id}/{number}")
            expected_removed = [list(block) for block in configuration]
            expected_added = [list(block) for block in pasch_mate(configuration)]
            if item["removed"] != expected_removed or item["added"] != expected_added:
                reject(f"{source_id} switch {number} has wrong trade blocks")
            switched = switched_system(representatives[source_id], configuration)
            signature, _ = point_signature(switched)
            if signature not in signatures:
                reject(f"{source_id} switch {number} has no class-signature target")
            target_id = signatures[signature]
            if item["target"] != target_id:
                reject(f"{source_id} switch {number} reports the wrong target")
            isomorphism = find_isomorphism(switched, representatives[target_id])
            if isomorphism is None:
                reject(
                    f"{source_id} switch {number} is not isomorphic to {target_id}"
                )
            replay_targets.append(target_id)
            if source_id != target_id:
                reconstructed_edges.add(tuple(sorted((source_id, target_id))))
        total_occurrences += len(configurations)
        if row["self_switch_occurrences"] != sum(
            target == source_id for target in replay_targets
        ):
            reject(f"{source_id} self-switch occurrence count is wrong")
        if row["distinct_targets_including_self"] != sorted(set(replay_targets)):
            reject(f"{source_id} distinct-target row is wrong")
    if reconstructed_edges != set(edges):
        missing = sorted(reconstructed_edges - set(edges))
        extra = sorted(set(edges) - reconstructed_edges)
        reject(
            f"edge list is incomplete/unsound: missing={missing[:3]}, extra={extra[:3]}"
        )

    require_keys(
        result,
        {
            "schema",
            "graph_convention",
            "vertex_count",
            "edge_count",
            "components",
            "component_sizes",
            "component_diameters",
            "diameter",
            "diameter_pair",
            "diameter_pair_count",
            "all_diameter_pairs",
            "geodesic",
            "distance_row_from_first_endpoint",
            "bfs_layers_from_first_endpoint",
            "eccentricities",
            "radius",
            "centers",
            "degree_sequence",
            "projective_seed_id",
            "anti_pasch_id",
            "total_pasch_occurrences",
            "pasch_count_multiset",
            "max_pasch_count",
            "min_pasch_count",
        },
        "result root",
    )
    if result["schema"] != "sts15-pasch-result-v1":
        reject("wrong result schema")
    if result["vertex_count"] != 80 or result["edge_count"] != len(edges):
        reject("result vertex or edge count is wrong")
    pasch_counts = sorted(len(pasches_by_id[vertex]) for vertex in ids)
    if result["pasch_count_multiset"] != pasch_counts:
        reject("result Pasch-count multiset is wrong")
    if result["total_pasch_occurrences"] != total_occurrences:
        reject("result total Pasch occurrences is wrong")
    if result["min_pasch_count"] != min(pasch_counts) or result[
        "max_pasch_count"
    ] != max(pasch_counts):
        reject("result Pasch extrema are wrong")
    zero_ids = [vertex for vertex in ids if not pasches_by_id[vertex]]
    if zero_ids != [result["anti_pasch_id"]]:
        reject("anti-Pasch ID is wrong or not unique")
    projective_ids = [
        vertex["id"] for vertex in vertices_raw if vertex["seed_role"] == "projective"
    ]
    anti_seed_ids = [
        vertex["id"] for vertex in vertices_raw if vertex["seed_role"] == "anti-Pasch"
    ]
    if projective_ids != [result["projective_seed_id"]]:
        reject("projective seed marker is wrong or not unique")
    if anti_seed_ids != [result["anti_pasch_id"]]:
        reject("anti-Pasch seed marker is wrong or not unique")
    bfs_record = verify_bfs(ids, edges, result)

    hashes = {name: sha256_file(path) for name, path in paths.items()}
    verifier_hash = sha256_file(Path(__file__))
    return {
        "status": "VERIFIED",
        "vertices": len(ids),
        "pairwise_nonisomorphic_by_distinct_point_pasch_signatures": True,
        "pasch_occurrences_replayed": total_occurrences,
        "simple_edges_reconstructed": len(reconstructed_edges),
        **bfs_record,
        "input_sha256": hashes,
        "verifier_sha256": verifier_hash,
        "nauty_used": False,
        "discovery_module_imported": False,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", nargs="?", default="certificate")
    args = parser.parse_args()
    try:
        record = verify(args.directory)
    except VerificationError as exc:
        print(f"REJECTED: {exc}", file=sys.stderr)
        raise SystemExit(1)
    print(json.dumps(record, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
