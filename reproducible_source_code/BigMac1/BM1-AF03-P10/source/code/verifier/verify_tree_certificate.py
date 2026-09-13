#!/usr/bin/env python3
"""Fail-closed, standard-library verifier for the finite tree certificate.

The verifier does not import the discovery generator or NetworkX.  It proves
completeness of each supplied list by enumerating every Prüfer word, decoding
it to a labelled tree, and taking the set of AHU free-tree canonical codes.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import sys
from collections import Counter, deque
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CERTIFICATE = ROOT / "certificates" / "trees_n2_n9.json"
EXPECTED_COUNTS = {2: 1, 3: 1, 4: 2, 5: 3, 6: 6, 7: 11, 8: 23, 9: 47}


class VerificationError(Exception):
    pass


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def adjacency_from_edges(edges: list[list[int]], n: int) -> list[set[int]]:
    if len(edges) != n - 1:
        raise VerificationError("a tree must have exactly n-1 edges")
    adjacency = [set() for _ in range(n)]
    seen = set()
    for edge in edges:
        if not isinstance(edge, list) or len(edge) != 2:
            raise VerificationError("each edge must be a two-entry list")
        u, v = edge
        if type(u) is not int or type(v) is not int:
            raise VerificationError("edge endpoints must be integers")
        if not (0 <= u < v < n):
            raise VerificationError("edges must be sorted, loopless, and in range")
        if (u, v) in seen:
            raise VerificationError("duplicate edge")
        seen.add((u, v))
        adjacency[u].add(v)
        adjacency[v].add(u)
    visited = {0}
    stack = [0]
    while stack:
        vertex = stack.pop()
        for neighbour in adjacency[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                stack.append(neighbour)
    if len(visited) != n:
        raise VerificationError("edge list is disconnected")
    return adjacency


def canonical_tree_code_from_adjacency(adjacency: list[set[int]]) -> str:
    n = len(adjacency)
    degree = [len(neighbours) for neighbours in adjacency]
    leaves = deque(i for i, d in enumerate(degree) if d <= 1)
    remaining = n
    while remaining > 2:
        layer = len(leaves)
        if layer == 0:
            raise VerificationError("cycle detected")
        remaining -= layer
        for _ in range(layer):
            leaf = leaves.popleft()
            degree[leaf] = 0
            for neighbour in adjacency[leaf]:
                if degree[neighbour] > 0:
                    degree[neighbour] -= 1
                    if degree[neighbour] == 1:
                        leaves.append(neighbour)
    centres = sorted(set(leaves))
    if n == 1:
        centres = [0]

    def rooted(vertex: int, parent: int) -> str:
        children = sorted(
            rooted(neighbour, vertex)
            for neighbour in adjacency[vertex]
            if neighbour != parent
        )
        return "(" + "".join(children) + ")"

    if len(centres) == 1:
        return "C" + rooted(centres[0], -1)
    if len(centres) == 2:
        halves = sorted(
            (rooted(centres[0], centres[1]), rooted(centres[1], centres[0]))
        )
        return "B" + "".join(halves)
    raise VerificationError("invalid centre count")


def decode_prufer(word: tuple[int, ...], n: int) -> list[set[int]]:
    degree = [1] * n
    for value in word:
        degree[value] += 1
    adjacency = [set() for _ in range(n)]
    for value in word:
        leaf = next(index for index, d in enumerate(degree) if d == 1)
        adjacency[leaf].add(value)
        adjacency[value].add(leaf)
        degree[leaf] -= 1
        degree[value] -= 1
    last = [index for index, d in enumerate(degree) if d == 1]
    if len(last) != 2:
        raise VerificationError("internal Prüfer decoder failure")
    u, v = last
    adjacency[u].add(v)
    adjacency[v].add(u)
    return adjacency


def all_unlabeled_codes_from_prufer(n: int) -> set[str]:
    codes = set()
    for word in itertools.product(range(n), repeat=n - 2):
        adjacency = decode_prufer(word, n)
        codes.add(canonical_tree_code_from_adjacency(adjacency))
    return codes


def reconstruct_from_three_circuits(edges: list[list[int]], n: int) -> str:
    if n == 2:
        return canonical_tree_code_from_adjacency([{1}, {0}])
    triples = [(u, v, n + index) for index, (u, v) in enumerate(edges)]
    incidence_degree = Counter(item for triple in triples for item in triple)
    internal = {item for item, degree in incidence_degree.items() if degree >= 2}
    relabel = {item: index for index, item in enumerate(sorted(internal))}
    reconstructed: list[list[int]] = []
    next_leaf = len(relabel)
    for triple in triples:
        core = sorted(item for item in triple if item in internal)
        if len(core) == 2:
            reconstructed.append(sorted((relabel[core[0]], relabel[core[1]])))
        elif len(core) == 1:
            reconstructed.append([relabel[core[0]], next_leaf])
            next_leaf += 1
        else:
            raise VerificationError("invalid zero-core triple for n>=3")
    if next_leaf != n:
        raise VerificationError("three-circuit reconstruction has wrong order")
    adjacency = adjacency_from_edges(sorted(reconstructed), n)
    return canonical_tree_code_from_adjacency(adjacency)


def cycle_incidence_signature(edges: list[list[int]], n: int) -> list[list[list[int]]]:
    """Recompute the full per-element circuit-size profile of cone(T)."""

    adjacency: list[list[tuple[int, int]]] = [[] for _ in range(n)]
    for edge_index, (u, v) in enumerate(edges):
        adjacency[u].append((v, edge_index))
        adjacency[v].append((u, edge_index))
    profiles = [Counter() for _ in range(2 * n - 1)]
    for source in range(n):
        parent: list[tuple[int, int] | None] = [None] * n
        parent[source] = (-1, -1)
        stack = [source]
        while stack:
            vertex = stack.pop()
            for neighbour, edge_index in adjacency[vertex]:
                if parent[neighbour] is None:
                    parent[neighbour] = (vertex, edge_index)
                    stack.append(neighbour)
        for target in range(source + 1, n):
            path_edges = []
            vertex = target
            while vertex != source:
                step = parent[vertex]
                if step is None:
                    raise VerificationError("disconnected tree during circuit computation")
                vertex, edge_index = step
                path_edges.append(edge_index)
            circuit = [source, target] + [n + edge_index for edge_index in path_edges]
            size = len(circuit)
            for element in circuit:
                profiles[element][size] += 1
    return sorted(
        [[[size, count] for size, count in sorted(profile.items())] for profile in profiles]
    )


def require_exact_keys(value: dict, keys: set[str], where: str) -> None:
    if not isinstance(value, dict) or set(value) != keys:
        raise VerificationError(f"unexpected or missing keys at {where}")


def verify(path: Path) -> dict[str, object]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise VerificationError(f"cannot parse certificate: {exc}") from exc
    require_exact_keys(
        payload,
        {"endpoint", "exact_arithmetic", "orders", "schema_version"},
        "top level",
    )
    if payload["schema_version"] != 1 or payload["exact_arithmetic"] is not True:
        raise VerificationError("unsupported schema or nonexact certificate")
    if payload["endpoint"] != "all unlabeled simple trees of orders 2 through 9":
        raise VerificationError("wrong endpoint")
    if not isinstance(payload["orders"], list) or len(payload["orders"]) != 8:
        raise VerificationError("orders must be a list covering 2 through 9")

    verified_counts = {}
    for expected_n, order in zip(range(2, 10), payload["orders"], strict=True):
        require_exact_keys(order, {"expected_unlabeled_count", "n", "trees"}, f"order {expected_n}")
        if order["n"] != expected_n:
            raise VerificationError("orders are missing, duplicated, or out of order")
        if order["expected_unlabeled_count"] != EXPECTED_COUNTS[expected_n]:
            raise VerificationError("claimed unlabeled count is wrong")
        if not isinstance(order["trees"], list):
            raise VerificationError("trees must be a list")

        supplied_codes = set()
        supplied_ids = set()
        supplied_signatures = set()
        for row in order["trees"]:
            require_exact_keys(
                row,
                {
                    "canonical_code",
                    "cycle_incidence_signature",
                    "degree_sequence",
                    "edges",
                    "id",
                    "reconstruction_code",
                },
                f"order {expected_n} tree row",
            )
            if not isinstance(row["id"], str) or row["id"] in supplied_ids:
                raise VerificationError("tree IDs must be unique strings")
            supplied_ids.add(row["id"])
            adjacency = adjacency_from_edges(row["edges"], expected_n)
            code = canonical_tree_code_from_adjacency(adjacency)
            if row["canonical_code"] != code:
                raise VerificationError("stored canonical code does not match edges")
            degrees = sorted(len(neighbours) for neighbours in adjacency)
            if row["degree_sequence"] != degrees:
                raise VerificationError("stored degree sequence does not match edges")
            reconstructed = reconstruct_from_three_circuits(row["edges"], expected_n)
            if row["reconstruction_code"] != reconstructed or reconstructed != code:
                raise VerificationError("three-circuit reconstruction failed")
            circuit_signature = cycle_incidence_signature(row["edges"], expected_n)
            if row["cycle_incidence_signature"] != circuit_signature:
                raise VerificationError("stored circuit-incidence signature is forged")
            signature_key = json.dumps(circuit_signature, separators=(",", ":"))
            if signature_key in supplied_signatures:
                raise VerificationError("cycle-incidence invariant collision")
            supplied_signatures.add(signature_key)
            if code in supplied_codes:
                raise VerificationError("duplicate unlabeled tree")
            supplied_codes.add(code)

        complete_codes = all_unlabeled_codes_from_prufer(expected_n)
        if supplied_codes != complete_codes:
            missing = len(complete_codes - supplied_codes)
            extra = len(supplied_codes - complete_codes)
            raise VerificationError(
                f"certificate is not exhaustive at order {expected_n}: missing={missing}, extra={extra}"
            )
        if len(supplied_codes) != EXPECTED_COUNTS[expected_n]:
            raise VerificationError("independently enumerated count disagrees")
        verified_counts[str(expected_n)] = len(supplied_codes)

    return {
        "certificate_sha256": sha256(path),
        "counts": verified_counts,
        "status": "VERIFIED",
        "verifier_sha256": sha256(Path(__file__).resolve()),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", nargs="?", type=Path, default=DEFAULT_CERTIFICATE)
    args = parser.parse_args()
    try:
        result = verify(args.certificate.resolve())
    except VerificationError as exc:
        print(f"REJECTED: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
