#!/usr/bin/env python3
"""Independent, fail-closed verifier for the finite n=7,8,9 certificate.

The verifier does not import discovery code, call nauty, run an optimizer, or
read cached numerical values.  It rebuilds all sparse unlabeled graphs from
the independent NetworkX graph atlas by unique multisets of connected
components, checks the two published-theorem routes combinatorially, and
checks every remaining Parseval-frame identity over ``fractions.Fraction``.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
import sys
from collections import Counter
from decimal import Decimal, InvalidOperation
from fractions import Fraction
from pathlib import Path
from typing import Any

import networkx as nx


SCHEMA = "sparse-complement-q2-exact-frame-certificate-v1"
FRACTION_PATTERN = re.compile(r"-?(?:0|[1-9][0-9]*)/[1-9][0-9]*\Z")
DECIMAL_PATTERN = re.compile(
    r"(?:0|(?:[1-9][0-9]*(?:\.[0-9]*[1-9])?|0\.[0-9]*[1-9])(?:e-?[1-9][0-9]*)?)\Z"
)


def no_duplicate_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def reject_json_constant(value: str) -> None:
    raise ValueError(f"non-standard JSON constant: {value}")


def is_strict_integer(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def require_keys(value: dict[str, Any], expected: set[str], location: str) -> None:
    if set(value) != expected:
        raise ValueError(
            f"{location}: keys differ; expected {sorted(expected)}, got {sorted(value)}"
        )


def parse_fraction(value: Any, location: str) -> Fraction:
    if not isinstance(value, str) or FRACTION_PATTERN.fullmatch(value) is None:
        raise ValueError(f"{location}: non-canonical rational")
    numerator_text, denominator_text = value.split("/")
    result = Fraction(int(numerator_text), int(denominator_text))
    if f"{result.numerator}/{result.denominator}" != value:
        raise ValueError(f"{location}: rational is not reduced/canonical")
    return result


def join_routed(h: nx.Graph) -> bool:
    components = [h.subgraph(c).copy() for c in nx.connected_components(h)]
    for mask in range(1, (1 << len(components)) - 1):
        left = nx.disjoint_union_all(
            [components[i] for i in range(len(components)) if mask & (1 << i)]
        )
        right = nx.disjoint_union_all(
            [components[i] for i in range(len(components)) if not mask & (1 << i)]
        )
        if (
            abs(len(left) - len(right)) <= 2
            and nx.is_connected(nx.complement(left))
            and nx.is_connected(nx.complement(right))
        ):
            return True
    return False


def connected_component_catalogue() -> list[nx.Graph]:
    """All possible nontrivial connected components with at most six edges.

    Such a component has at most seven vertices, so the graph atlas (complete
    through order seven) is sufficient.  Atlas entries are already one per
    isomorphism class.
    """
    catalogue = []
    for graph in nx.graph_atlas_g():
        if (
            2 <= len(graph) <= 7
            and graph.number_of_edges() <= 6
            and nx.is_connected(graph)
        ):
            catalogue.append(nx.convert_node_labels_to_integers(graph))
    catalogue.sort(
        key=lambda graph: (
            graph.number_of_edges(),
            len(graph),
            tuple(sorted(dict(graph.degree()).values())),
            nx.to_graph6_bytes(graph, header=False),
        )
    )
    for i, graph in enumerate(catalogue):
        for earlier in catalogue[:i]:
            if (
                len(graph) == len(earlier)
                and graph.number_of_edges() == earlier.number_of_edges()
                and nx.is_isomorphic(graph, earlier)
            ):
                raise ValueError("graph atlas contains duplicate connected isomorphism types")
    return catalogue


def integer_partitions(n: int, minimum: int = 1):
    """Yield nondecreasing integer partitions of n."""
    if n == 0:
        yield ()
        return
    for first in range(minimum, n + 1):
        for rest in integer_partitions(n - first, first):
            yield (first,) + rest


def burnside_unlabeled_counts(n: int, edge_limit: int) -> list[int]:
    """Independently count unlabeled n-vertex graphs by number of edges.

    For each conjugacy class of S_n, form the induced permutation on the
    unordered vertex pairs.  A fixed graph is a union of pair-orbits, so its
    edge enumerator is the product of (1+x^orbit_size).  Burnside averaging
    gives the exact number of graph isomorphism classes.  This calculation
    does not use the graph atlas catalogue that supplies representatives.
    """
    fixed_sums = [0] * (edge_limit + 1)
    factorial_n = math.factorial(n)
    for cycle_type in integer_partitions(n):
        permutation = [0] * n
        start = 0
        for length in cycle_type:
            cycle = list(range(start, start + length))
            start += length
            for index, vertex in enumerate(cycle):
                permutation[vertex] = cycle[(index + 1) % length]

        pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
        visited: set[tuple[int, int]] = set()
        orbit_lengths = []
        for pair in pairs:
            if pair in visited:
                continue
            current = pair
            orbit_length = 0
            while current not in visited:
                visited.add(current)
                orbit_length += 1
                current = tuple(
                    sorted((permutation[current[0]], permutation[current[1]]))
                )
            orbit_lengths.append(orbit_length)

        polynomial = [0] * (edge_limit + 1)
        polynomial[0] = 1
        for orbit_length in orbit_lengths:
            for degree in range(edge_limit, orbit_length - 1, -1):
                polynomial[degree] += polynomial[degree - orbit_length]

        multiplicities = Counter(cycle_type)
        class_size = factorial_n
        for length, multiplicity in multiplicities.items():
            class_size //= (length**multiplicity) * math.factorial(multiplicity)
        for edges, coefficient in enumerate(polynomial):
            fixed_sums[edges] += class_size * coefficient

    if any(value % factorial_n for value in fixed_sums):
        raise ValueError("Burnside average is unexpectedly nonintegral")
    return [value // factorial_n for value in fixed_sums]


def component_multiset_graphs(n: int, edge_limit: int) -> list[nx.Graph]:
    catalogue = connected_component_catalogue()
    component_lists: list[tuple[int, ...]] = []

    def extend(start: int, vertices: int, edges: int, chosen: tuple[int, ...]) -> None:
        component_lists.append(chosen)
        for index in range(start, len(catalogue)):
            graph = catalogue[index]
            next_vertices = vertices + len(graph)
            next_edges = edges + graph.number_of_edges()
            if next_vertices <= n and next_edges <= edge_limit:
                extend(index, next_vertices, next_edges, chosen + (index,))

    extend(0, 0, 0, ())
    result = []
    for chosen in component_lists:
        parts = [catalogue[index] for index in chosen]
        occupied = sum(len(part) for part in parts)
        parts.extend(nx.empty_graph(1) for _ in range(n - occupied))
        graph = nx.disjoint_union_all(parts) if parts else nx.empty_graph(n)
        result.append(graph)
    return result


def parse_graph6(value: Any, expected_n: int, location: str) -> nx.Graph:
    if not isinstance(value, str) or not value or any(ord(ch) < 63 or ord(ch) > 126 for ch in value):
        raise ValueError(f"{location}: invalid graph6 text")
    try:
        graph = nx.from_graph6_bytes(value.encode("ascii"))
    except Exception as exc:
        raise ValueError(f"{location}: graph6 parse failed") from exc
    if len(graph) != expected_n:
        raise ValueError(f"{location}: wrong graph order")
    canonical_encoding = nx.to_graph6_bytes(graph, header=False).decode("ascii").strip()
    if canonical_encoding != value:
        raise ValueError(f"{location}: graph6 text is not in canonical short encoding")
    return graph


def verify_frame_witness(raw: dict[str, Any], index: int) -> tuple[nx.Graph, int]:
    location = f"frame_witnesses[{index}]"
    require_keys(
        raw,
        {
            "n",
            "edge_limit",
            "graph6",
            "rank",
            "orthogonality_order",
            "directions",
            "weights",
            "discovery_only",
        },
        location,
    )
    n = raw["n"]
    rank = raw["rank"]
    if not is_strict_integer(n) or n not in {7, 8, 9}:
        raise ValueError(f"{location}: unsupported n")
    if (
        not is_strict_integer(raw["edge_limit"])
        or not is_strict_integer(rank)
        or raw["edge_limit"] != n - 3
        or rank != 3
    ):
        raise ValueError(f"{location}: endpoint or rank mismatch")
    if (
        not isinstance(raw["orthogonality_order"], list)
        or not all(is_strict_integer(x) for x in raw["orthogonality_order"])
        or sorted(raw["orthogonality_order"]) != list(range(n))
    ):
        raise ValueError(f"{location}: orthogonality order is not a permutation")
    graph = parse_graph6(raw["graph6"], n, location + ".graph6")
    if graph.number_of_edges() > n - 3:
        raise ValueError(f"{location}: graph exceeds edge endpoint")
    if not isinstance(raw["directions"], list) or len(raw["directions"]) != n:
        raise ValueError(f"{location}: wrong number of directions")
    directions: list[list[Fraction]] = []
    for i, row in enumerate(raw["directions"]):
        if not isinstance(row, list) or len(row) != rank:
            raise ValueError(f"{location}.directions[{i}]: wrong row length")
        directions.append(
            [parse_fraction(x, f"{location}.directions[{i}][{j}]") for j, x in enumerate(row)]
        )
    if not isinstance(raw["weights"], list) or len(raw["weights"]) != n:
        raise ValueError(f"{location}: wrong number of weights")
    weights = [
        parse_fraction(x, f"{location}.weights[{i}]")
        for i, x in enumerate(raw["weights"])
    ]
    if any(x <= 0 for x in weights):
        raise ValueError(f"{location}: a frame weight is nonpositive")

    # Exact support: P_ij = sqrt(x_i x_j) <w_i,w_j>; positive weights mean
    # its vanishing is decided exactly by this rational dot product.
    for i in range(n):
        for j in range(i):
            dot = sum(directions[i][k] * directions[j][k] for k in range(rank))
            if (dot == 0) != graph.has_edge(i, j):
                raise ValueError(f"{location}: exact off-diagonal support mismatch at {i},{j}")

    # Exact Parseval identity V^T V=I for V_i=sqrt(x_i) w_i.
    for a in range(rank):
        for b in range(rank):
            entry = sum(
                weights[i] * directions[i][a] * directions[i][b]
                for i in range(n)
            )
            target = Fraction(int(a == b), 1)
            if entry != target:
                raise ValueError(f"{location}: exact Parseval identity failed at {a},{b}")

    # The checked identities imply P=VV^T is a rank-r orthogonal projection.
    # Since 0<r<n, Q=I-2P has both eigenvalues and exactly G's support.
    if not (0 < rank < n):
        raise ValueError(f"{location}: trivial projection rank")

    discovery = raw["discovery_only"]
    if not isinstance(discovery, dict):
        raise ValueError(f"{location}.discovery_only: not an object")
    require_keys(
        discovery,
        {"seed", "maximum_zero_residual", "minimum_required_nonzero_margin"},
        location + ".discovery_only",
    )
    if not is_strict_integer(discovery["seed"]) or discovery["seed"] < 0:
        raise ValueError(f"{location}.discovery_only.seed: invalid integer")
    for key in ("maximum_zero_residual", "minimum_required_nonzero_margin"):
        value = discovery[key]
        if not isinstance(value, str) or DECIMAL_PATTERN.fullmatch(value) is None:
            raise ValueError(
                f"{location}.discovery_only.{key}: non-canonical decimal string"
            )
        try:
            decimal_value = Decimal(value)
        except InvalidOperation as exc:
            raise ValueError(f"{location}.discovery_only.{key}: invalid decimal") from exc
        if not decimal_value.is_finite() or decimal_value < 0:
            raise ValueError(f"{location}.discovery_only.{key}: nonfinite/negative decimal")
    return graph, n


def validate_header(certificate: dict[str, Any]) -> None:
    require_keys(
        certificate,
        {
            "schema",
            "endpoint",
            "external_theorems",
            "expected_route_counts",
            "frame_witnesses",
            "discovery_provenance",
        },
        "certificate",
    )
    if certificate["schema"] != SCHEMA:
        raise ValueError("certificate: unsupported schema")
    endpoint = certificate["endpoint"]
    if not isinstance(endpoint, dict):
        raise ValueError("certificate: endpoint is not an object")
    require_keys(
        endpoint,
        {"orders_certified", "edge_limit_formula", "field", "support_convention"},
        "endpoint",
    )
    if (
        not isinstance(endpoint["orders_certified"], list)
        or not all(is_strict_integer(value) for value in endpoint["orders_certified"])
        or endpoint["orders_certified"] != [7, 8, 9]
    ):
        raise ValueError("certificate: endpoint order list mismatch")
    if endpoint != {
        "orders_certified": [7, 8, 9],
        "edge_limit_formula": "n-3",
        "field": "real symmetric matrices",
        "support_convention": "off_diagonal_nonzero_iff_edge_of_G",
    }:
        raise ValueError("certificate: endpoint mismatch")
    expected_theorems = {
        "bipartite_complement": {
            "statement": "If H=bar(G) is bipartite and |E(H)|<=n-3, then q(G)=2.",
            "source": "Barrett--Fallat--Furst--Nasserasr--Rooney--Tait, Theorem 3.7",
            "doi": "10.13001/ela.2026.9443",
        },
        "balanced_connected_join": {
            "statement": "If X and Y are connected and ||V(X)|-|V(Y)||<=2, then q(X join Y)=2.",
            "source": "Levene--Oblak--Smigoc, Theorem 3.4 (connected k=1 case)",
            "doi": "10.1080/03081087.2023.2232090",
        },
    }
    if certificate["external_theorems"] != expected_theorems:
        raise ValueError("certificate: external theorem binding mismatch")

    counts = certificate["expected_route_counts"]
    if not isinstance(counts, dict) or set(counts) != {"7", "8", "9"}:
        raise ValueError("certificate: invalid route-count orders")
    for order, row in counts.items():
        if not isinstance(row, dict):
            raise ValueError(f"certificate: route count {order} is not an object")
        require_keys(row, {"total", "bipartite", "join", "frame"}, f"route count {order}")
        if not all(is_strict_integer(value) and value >= 0 for value in row.values()):
            raise ValueError(f"certificate: route count {order} has a noninteger value")

    provenance = certificate["discovery_provenance"]
    if not isinstance(provenance, dict):
        raise ValueError("certificate: discovery_provenance is not an object")
    require_keys(
        provenance,
        {
            "warning",
            "generator",
            "geng_command_template",
            "seed_range",
            "denominator_bound",
            "python",
            "networkx",
            "numpy",
            "scipy",
            "sympy",
        },
        "discovery_provenance",
    )
    for key in (
        "warning",
        "generator",
        "geng_command_template",
        "python",
        "networkx",
        "numpy",
        "scipy",
        "sympy",
    ):
        if not isinstance(provenance[key], str) or not provenance[key]:
            raise ValueError(f"discovery_provenance.{key}: invalid string")
    if (
        not isinstance(provenance["seed_range"], list)
        or len(provenance["seed_range"]) != 2
        or not all(is_strict_integer(value) for value in provenance["seed_range"])
        or provenance["seed_range"][0] < 0
        or provenance["seed_range"][1] < provenance["seed_range"][0]
    ):
        raise ValueError("discovery_provenance.seed_range: invalid integer interval")
    if (
        not is_strict_integer(provenance["denominator_bound"])
        or provenance["denominator_bound"] <= 0
    ):
        raise ValueError("discovery_provenance.denominator_bound: invalid integer")


def verify(path: Path) -> dict[str, Any]:
    raw_bytes = path.read_bytes()
    certificate = json.loads(
        raw_bytes,
        object_pairs_hook=no_duplicate_object,
        parse_constant=reject_json_constant,
    )
    if not isinstance(certificate, dict):
        raise ValueError("certificate root is not an object")
    validate_header(certificate)

    raw_witnesses = certificate["frame_witnesses"]
    if not isinstance(raw_witnesses, list):
        raise ValueError("frame_witnesses is not a list")
    witnesses = [verify_frame_witness(raw, i) for i, raw in enumerate(raw_witnesses)]
    for i in range(len(witnesses)):
        for j in range(i):
            if witnesses[i][1] == witnesses[j][1] and nx.is_isomorphic(witnesses[i][0], witnesses[j][0]):
                raise ValueError("duplicate isomorphism class in frame witnesses")

    actual_counts: dict[str, dict[str, int]] = {}
    used_witnesses: set[int] = set()
    for n in (7, 8, 9):
        graphs = component_multiset_graphs(n, n - 3)
        component_counts = Counter(graph.number_of_edges() for graph in graphs)
        burnside_counts = burnside_unlabeled_counts(n, n - 3)
        if component_counts != Counter(dict(enumerate(burnside_counts))):
            raise ValueError(
                f"order {n}: component enumeration disagrees with independent Burnside count"
            )
        counts = {"total": len(graphs), "bipartite": 0, "join": 0, "frame": 0}
        for graph in graphs:
            if nx.is_bipartite(graph):
                counts["bipartite"] += 1
                continue
            if join_routed(graph):
                counts["join"] += 1
                continue
            matches = [
                i
                for i, (witness_graph, witness_n) in enumerate(witnesses)
                if witness_n == n and nx.is_isomorphic(graph, witness_graph)
            ]
            if len(matches) != 1:
                raise ValueError(
                    f"order {n}: residual class has {len(matches)} exact frame witnesses"
                )
            used_witnesses.add(matches[0])
            counts["frame"] += 1
        actual_counts[str(n)] = counts

    if used_witnesses != set(range(len(witnesses))):
        raise ValueError("one or more frame witnesses do not belong to a residual class")
    if certificate["expected_route_counts"] != actual_counts:
        raise ValueError(
            f"route counts mismatch: expected {certificate['expected_route_counts']}, got {actual_counts}"
        )

    code_bytes = Path(__file__).read_bytes()
    return {
        "status": "VERIFIED",
        "endpoint": "q(G)=2 for all |V(G)| in {7,8,9} with e(bar(G))<=|V(G)|-3",
        "route_counts": actual_counts,
        "frame_witnesses": len(witnesses),
        "certificate_sha256": hashlib.sha256(raw_bytes).hexdigest(),
        "verifier_sha256": hashlib.sha256(code_bytes).hexdigest(),
        "proof_assistant": "none",
    }


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: verify_n9_certificate.py CERTIFICATE.json")
    try:
        result = verify(Path(sys.argv[1]))
    except Exception as exc:
        print(f"REJECTED: {type(exc).__name__}: {exc}", file=sys.stderr)
        raise SystemExit(1)
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
