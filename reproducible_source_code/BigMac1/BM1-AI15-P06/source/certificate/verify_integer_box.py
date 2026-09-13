#!/usr/bin/env python3
"""Independent exact verifier for integer_box_side5.json.

The verifier trusts only the scope parameters and claimed clique numbers.  It
reconstructs all vertices and edges, verifies each lower-bound witness, and
uses a separate fixed-target recursive algorithm to refute a clique one larger
than the claimed maximum.  No floating-point arithmetic or discovery arrays
are imported.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import sys
from pathlib import Path


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def l1(x: tuple[int, ...], y: tuple[int, ...]) -> int:
    total = 0
    for k in range(len(x)):
        delta = x[k] - y[k]
        total += delta if delta >= 0 else -delta
    return total


def adjacency_for_distance(vertices: list[tuple[int, ...]], d: int) -> list[int]:
    n = len(vertices)
    adjacency = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if l1(vertices[i], vertices[j]) == d:
                adjacency[i] |= 1 << j
                adjacency[j] |= 1 << i
    return adjacency


def coloring_bound(candidates: int, adjacency: list[int]) -> int:
    """Greedily color the induced graph; number of colors bounds clique size."""
    colors = 0
    uncolored = candidates
    while uncolored:
        colors += 1
        color_class_candidates = uncolored
        while color_class_candidates:
            bit = color_class_candidates & -color_class_candidates
            vertex = bit.bit_length() - 1
            uncolored ^= bit
            color_class_candidates ^= bit
            color_class_candidates &= ~adjacency[vertex]
    return colors


class FixedTargetSearch:
    """Decide whether a graph contains a clique of exactly `target` vertices."""

    def __init__(self, adjacency: list[int], target: int):
        self.adjacency = adjacency
        self.target = target
        self.nodes = 0

    def color_order(self, candidates: int) -> tuple[list[int], list[int]]:
        """Return a valid coloring order and prefix color-count bounds."""
        order: list[int] = []
        bounds: list[int] = []
        color = 0
        uncolored = candidates
        while uncolored:
            color += 1
            available = uncolored
            while available:
                bit = available & -available
                vertex = bit.bit_length() - 1
                order.append(vertex)
                bounds.append(color)
                uncolored ^= bit
                available ^= bit
                available &= ~self.adjacency[vertex]
        return order, bounds

    def exists(self, candidates: int, need: int) -> bool:
        self.nodes += 1
        if need == 0:
            return True
        if candidates.bit_count() < need:
            return False
        order, bounds = self.color_order(candidates)
        # Process colors from high to low.  After the already-processed
        # vertices are removed, bounds[index] colors the entire remaining
        # prefix, so it is a valid fail-closed upper bound.
        for index in range(len(order) - 1, -1, -1):
            if bounds[index] < need:
                return False
            vertex = order[index]
            bit = 1 << vertex
            if self.exists(candidates & self.adjacency[vertex], need - 1):
                return True
            candidates &= ~bit
        return False

    def run(self) -> bool:
        return self.exists((1 << len(self.adjacency)) - 1, self.target)


def main() -> int:
    if sys.version_info < (3, 10):
        raise SystemExit("FAIL: Python >= 3.10 is required (uses int.bit_count)")
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", nargs="?", type=Path, default=Path("certificate/integer_box_side5.json"))
    args = parser.parse_args()
    raw = args.certificate.read_bytes()
    data = json.loads(raw)
    required = {
        "schema", "coordinate_set", "dimension", "vertex_count", "results",
        "largest_over_all_distances",
    }
    if not isinstance(data, dict) or not required.issubset(data):
        raise SystemExit("FAIL: malformed certificate")
    coordinates = data["coordinate_set"]
    dimension = data["dimension"]
    if coordinates != list(range(len(coordinates))) or len(coordinates) < 2:
        raise SystemExit("FAIL: coordinates must be the canonical consecutive integer set")
    if not isinstance(dimension, int) or dimension < 1:
        raise SystemExit("FAIL: invalid dimension")
    vertices = list(itertools.product(coordinates, repeat=dimension))
    if len(vertices) != data["vertex_count"]:
        raise SystemExit("FAIL: vertex count mismatch")
    # The fixed-target verifier's exclude branch can deliberately have one
    # stack frame per vertex.  Make that finite, reconstructed bound explicit
    # instead of depending on Python's unrelated default limit of 1000.
    sys.setrecursionlimit(max(sys.getrecursionlimit(), len(vertices) + 256))
    expected_distances = list(range(1, dimension * (len(coordinates) - 1) + 1))
    if [row.get("distance") for row in data["results"]] != expected_distances:
        raise SystemExit("FAIL: incomplete or reordered distance list")

    verifier_nodes = {}
    computed_maxima = []
    for row in data["results"]:
        d = row["distance"]
        claimed = row["maximum_clique_size"]
        witness_points = [tuple(point) for point in row["witness_points"]]
        if len(witness_points) != claimed or len(set(witness_points)) != claimed:
            raise SystemExit(f"FAIL: malformed witness for D={d}")
        if any(point not in set(vertices) for point in witness_points):
            raise SystemExit(f"FAIL: witness outside box for D={d}")
        if any(l1(x, y) != d for x, y in itertools.combinations(witness_points, 2)):
            raise SystemExit(f"FAIL: witness is not equilateral for D={d}")

        if d % 2 == 1:
            # Independently audit the parity identity on every pair.  It gives
            # omega <= 2 for odd d; the supplied edge gives equality.
            for x, y in itertools.combinations(vertices, 2):
                if (l1(x, y) - (sum(x) - sum(y))) % 2 != 0:
                    raise SystemExit("FAIL: parity identity audit")
            if claimed != 2:
                raise SystemExit(f"FAIL: odd-distance maximum must be 2 for D={d}")
            verifier_nodes[str(d)] = 0
        else:
            adjacency = adjacency_for_distance(vertices, d)
            decision = FixedTargetSearch(adjacency, claimed + 1)
            if decision.run():
                raise SystemExit(f"FAIL: found clique larger than claim for D={d}")
            verifier_nodes[str(d)] = decision.nodes
        computed_maxima.append(claimed)

    if max(computed_maxima) != data["largest_over_all_distances"]:
        raise SystemExit("FAIL: aggregate maximum mismatch")
    print(json.dumps({
        "status": "PASS",
        "certificate_sha256": hashlib.sha256(raw).hexdigest(),
        "verifier_sha256": sha256(Path(__file__).resolve()),
        "dimension": dimension,
        "coordinate_set": coordinates,
        "verified_largest_equilateral_size": max(computed_maxima),
        "fixed_target_search_nodes": verifier_nodes,
        "python": sys.version.split()[0],
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
