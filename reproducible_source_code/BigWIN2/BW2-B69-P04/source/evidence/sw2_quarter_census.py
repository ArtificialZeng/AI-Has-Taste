#!/usr/bin/env python3
"""Exact small census in the reflective quarter-octahedron tiling.

All arithmetic is over the integers in the hyperboloid/Klein model with
Lorentz form diag(-1,1,1,1).  The script first reconstructs SW2, the
48-chamber octahedron, and both 12-chamber quarter-octahedra described in
Proposition 7.10 of arXiv:2609.05349v1.  It then enumerates every convex
union of at most seven chambers in the reflection tiling by one quarter-
octahedron, and checks its boundary geometry exactly.

This is a bounded subsidiary census, not a resolution of Conjecture 7.11.
"""

from __future__ import annotations

import argparse
import itertools
import json
from collections import Counter, deque
from functools import lru_cache, reduce
from math import gcd
from pathlib import Path


J = (-1, 1, 1, 1)
IDENTITY = tuple(1 if i == j else 0 for i in range(4) for j in range(4))

# Face normals for SW2.  A normal n represents <n,X> <= 0, where
# <x,y> = -x0*y0 + x1*y1 + x2*y2 + x3*y3.
# The chamber in Klein coordinates is
#     x >= y >= z >= 0,  x+y+z <= 1.
SW2_NORMALS = (
    (0, -1, 1, 0),   # face 1: y <= x
    (1, 1, 1, 1),    # face 2: x+y+z <= 1
    (0, 0, 0, -1),   # face 3: z >= 0
    (0, 0, -1, 1),   # face 4: z <= y
)

EXPECTED_COXETER_ORDERS = (
    (1, 2, 2, 3),
    (2, 1, 4, 2),
    (2, 4, 1, 4),
    (3, 2, 4, 1),
)


def lorentz(a: tuple[int, ...], b: tuple[int, ...]) -> int:
    return sum(J[i] * a[i] * b[i] for i in range(4))


def matrix_multiply(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(
        sum(a[4 * i + k] * b[4 * k + j] for k in range(4))
        for i in range(4)
        for j in range(4)
    )


def matrix_vector(a: tuple[int, ...], v: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sum(a[4 * i + k] * v[k] for k in range(4)) for i in range(4))


def inverse_lorentz(a: tuple[int, ...]) -> tuple[int, ...]:
    # a^{-1} = J a^T J.
    return tuple(J[i] * a[4 * j + i] * J[j] for i in range(4) for j in range(4))


def reflection(normal: tuple[int, ...]) -> tuple[int, ...]:
    q = lorentz(normal, normal)
    assert q > 0
    entries = []
    for i in range(4):
        for j in range(4):
            numerator = 2 * normal[i] * normal[j] * J[j]
            assert numerator % q == 0
            entries.append((1 if i == j else 0) - numerator // q)
    result = tuple(entries)
    assert matrix_multiply(matrix_multiply(inverse_lorentz(result), result), IDENTITY) == IDENTITY
    return result


def primitive(v: tuple[int, ...]) -> tuple[int, ...]:
    common = reduce(gcd, (abs(x) for x in v if x), 0)
    assert common
    return tuple(x // common for x in v)


def determinant3(m: list[list[int]]) -> int:
    return (
        m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
    )


def null_vector_of_three(rows: list[tuple[int, ...]]) -> tuple[int, ...] | None:
    vector = []
    for column in range(4):
        minor = [[row[k] for k in range(4) if k != column] for row in rows]
        vector.append((1 if column % 2 == 0 else -1) * determinant3(minor))
    if not any(vector):
        return None
    common = reduce(gcd, (abs(x) for x in vector if x), 0)
    vector = [x // common for x in vector]
    if vector[0] < 0:
        vector = [-x for x in vector]
    if vector[0] <= 0:
        return None
    return tuple(vector)


def coxeter_order(a: tuple[int, ...], b: tuple[int, ...]) -> int:
    product = lorentz(a, b)
    aa, bb = lorentz(a, a), lorentz(b, b)
    if product == 0:
        return 2
    assert product < 0
    if 4 * product * product == aa * bb:
        return 3
    if 2 * product * product == aa * bb:
        return 4
    raise AssertionError((a, b, product, aa, bb))


def subgroup(reflections: tuple[tuple[int, ...], ...], generators: tuple[int, ...]) -> set[tuple[int, ...]]:
    result = {IDENTITY}
    queue = deque([IDENTITY])
    while queue:
        current = queue.popleft()
        for generator in generators:
            nxt = matrix_multiply(current, reflections[generator])
            if nxt not in result:
                result.add(nxt)
                queue.append(nxt)
    return result


def chamber_union_boundary(
    chambers: set[tuple[int, ...]],
    normals: tuple[tuple[int, ...], ...],
    reflections: tuple[tuple[int, ...], ...],
) -> tuple[list[tuple[int, ...]], dict[tuple[int, ...], set[int]], int]:
    pieces: list[tuple[tuple[int, ...], int]] = []
    for chamber in chambers:
        for face, generator in enumerate(reflections):
            if matrix_multiply(chamber, generator) not in chambers:
                pieces.append((primitive(matrix_vector(chamber, normals[face])), face + 1))
    planes = sorted({normal for normal, _ in pieces})
    types = {
        plane: {face_type for normal, face_type in pieces if normal == plane}
        for plane in planes
    }
    return planes, types, len(pieces)


def polyhedron_data(boundary_normals: list[tuple[int, ...]]) -> dict:
    """Recover exact vertices and boundary edges from oriented half-spaces."""
    facets = len(boundary_normals)
    vertices: dict[tuple[int, ...], int] = {}
    for triple in itertools.combinations(range(facets), 3):
        rows = [
            tuple(J[t] * boundary_normals[index][t] for t in range(4))
            for index in triple
        ]
        point = null_vector_of_three(rows)
        if point is None:
            continue
        if all(lorentz(normal, point) <= 0 for normal in boundary_normals):
            square_norm = lorentz(point, point)
            if square_norm <= 0:
                vertices[point] = square_norm

    incidence = {index: set() for index in range(facets)}
    vertex_facets: dict[tuple[int, ...], list[int]] = {}
    for point in vertices:
        containing = [
            index for index, normal in enumerate(boundary_normals)
            if lorentz(normal, point) == 0
        ]
        vertex_facets[point] = containing
        for index in containing:
            incidence[index].add(point)

    edges: list[tuple[int, int]] = []
    bad_edges: list[tuple[int, int, int]] = []
    for first, second in itertools.combinations(range(facets), 2):
        if len(incidence[first] & incidence[second]) >= 2:
            edges.append((first, second))
            product = lorentz(boundary_normals[first], boundary_normals[second])
            if product != 0:
                bad_edges.append((first, second, product))

    finite = sorted(point for point, q in vertices.items() if q < 0)
    ideal = sorted(point for point, q in vertices.items() if q == 0)
    degenerate_facets = sorted(index for index, points in incidence.items() if len(points) < 3)
    return {
        "facets": facets,
        "vertices": len(vertices),
        "edges": len(edges),
        "finite_vertices": [list(point) for point in finite],
        "ideal_vertices": [list(point) for point in ideal],
        "bad_edges": [list(edge) for edge in bad_edges],
        "degenerate_facets": degenerate_facets,
        "vertex_valences": sorted(len(vertex_facets[point]) for point in vertices),
        "euler_characteristic": len(vertices) - len(edges) + facets,
    }


def normalized_relation_graph(normals: list[tuple[int, ...]]) -> list[list[int]]:
    """Scale-free Gram data: 0=orthogonal and -1=parallel in this example."""
    graph = []
    for first in normals:
        row = []
        for second in normals:
            product = lorentz(first, second)
            if product == 0:
                row.append(0)
            elif product < 0 and product * product == lorentz(first, first) * lorentz(second, second):
                row.append(-1)
            elif first == second:
                row.append(1)
            else:
                raise AssertionError((first, second, product))
        graph.append(row)
    return graph


def find_graph_isomorphism(first: list[list[int]], second: list[list[int]]) -> list[int] | None:
    assert len(first) == len(second)
    for permutation in itertools.permutations(range(len(first))):
        if all(first[i][j] == second[permutation[i]][permutation[j]] for i in range(len(first)) for j in range(len(first))):
            return list(permutation)
    return None


def reconstruct_primary_geometry() -> tuple[list[tuple[int, ...]], dict]:
    sw_reflections = tuple(reflection(normal) for normal in SW2_NORMALS)
    orders = tuple(
        tuple(1 if i == j else coxeter_order(SW2_NORMALS[i], SW2_NORMALS[j]) for j in range(4))
        for i in range(4)
    )
    assert orders == EXPECTED_COXETER_ORDERS

    # B3 = <faces 1,3,4> has 48 chambers and gives the octahedron.
    octahedron = subgroup(sw_reflections, (0, 2, 3))
    assert len(octahedron) == 48
    octahedron_normals, octahedron_types, octahedron_pieces = chamber_union_boundary(
        octahedron, SW2_NORMALS, sw_reflections
    )
    expected_octahedron_normals = sorted(
        (1, x, y, z) for x in (-1, 1) for y in (-1, 1) for z in (-1, 1)
    )
    assert octahedron_normals == expected_octahedron_normals
    assert set().union(*octahedron_types.values()) == {2}
    octahedron_shape = polyhedron_data(octahedron_normals)
    assert (
        octahedron_shape["facets"],
        octahedron_shape["vertices"],
        octahedron_shape["edges"],
        len(octahedron_shape["ideal_vertices"]),
        len(octahedron_shape["finite_vertices"]),
    ) == (8, 6, 12, 6, 0)
    assert not octahedron_shape["bad_edges"]

    # The all-face-3 quarter is the orbit under <faces 1,2,4> of order 12.
    quarter_a = subgroup(sw_reflections, (0, 1, 3))
    assert len(quarter_a) == 12
    quarter_a_normals, quarter_a_types, quarter_a_pieces = chamber_union_boundary(
        quarter_a, SW2_NORMALS, sw_reflections
    )
    assert set().union(*quarter_a_types.values()) == {3}

    # The no-face-3 quarter is a symmetry sector x >= |y| inside O.
    # The rational timelike point has distinct positive spatial coordinates,
    # so it lies on no sector wall and selects chambers without ambiguity.
    test_point = (100, 20, 10, 5)
    quarter_b = {
        chamber for chamber in octahedron
        if (image := matrix_vector(chamber, test_point))[1] >= abs(image[2])
    }
    assert len(quarter_b) == 12
    quarter_b_normals, quarter_b_types, quarter_b_pieces = chamber_union_boundary(
        quarter_b, SW2_NORMALS, sw_reflections
    )
    assert 3 not in set().union(*quarter_b_types.values())

    quarter_a_shape = polyhedron_data(quarter_a_normals)
    quarter_b_shape = polyhedron_data(quarter_b_normals)
    for shape in (quarter_a_shape, quarter_b_shape):
        assert (
            shape["facets"], shape["vertices"], shape["edges"],
            len(shape["ideal_vertices"]), len(shape["finite_vertices"]),
        ) == (6, 5, 9, 3, 2)
        assert not shape["bad_edges"]

    relation_a = normalized_relation_graph(quarter_a_normals)
    relation_b = normalized_relation_graph(quarter_b_normals)
    isomorphism = find_graph_isomorphism(relation_a, relation_b)
    assert isomorphism is not None

    report = {
        "sw2": {
            "lorentz_normals_by_face": [list(normal) for normal in SW2_NORMALS],
            "coxeter_orders": [list(row) for row in orders],
            "klein_inequalities": ["y<=x", "x+y+z<=1", "z>=0", "z<=y"],
        },
        "octahedron_reconstruction": {
            "chambers": len(octahedron),
            "boundary_chamber_facets": octahedron_pieces,
            "boundary_planes": [list(normal) for normal in octahedron_normals],
            "shape": octahedron_shape,
        },
        "quarter_reconstructions": {
            "all_faces_type_3": {
                "chambers": len(quarter_a),
                "boundary_chamber_facets": quarter_a_pieces,
                "boundary_planes": [list(normal) for normal in quarter_a_normals],
                "shape": quarter_a_shape,
            },
            "no_faces_type_3": {
                "chambers": len(quarter_b),
                "boundary_chamber_facets": quarter_b_pieces,
                "boundary_planes": [list(normal) for normal in quarter_b_normals],
                "boundary_face_types": {
                    str(list(normal)): sorted(quarter_b_types[normal]) for normal in quarter_b_normals
                },
                "shape": quarter_b_shape,
            },
            "scale_free_gram_isomorphism_a_to_b": isomorphism,
        },
    }
    return quarter_b_normals, report


class ReflectiveQuarterCensus:
    def __init__(self, normals: list[tuple[int, ...]], maximum_size: int = 7):
        self.normals = tuple(normals)
        self.reflections = tuple(reflection(normal) for normal in normals)
        self.maximum_size = maximum_size
        self.levels: list[list[tuple[int, ...]]] = [[IDENTITY]]
        self.length = {IDENTITY: 0}
        for distance in range(1, maximum_size):
            new_level = []
            for chamber in self.levels[-1]:
                for generator in self.reflections:
                    nxt = matrix_multiply(chamber, generator)
                    if nxt not in self.length:
                        self.length[nxt] = distance
                        new_level.append(nxt)
            self.levels.append(new_level)
        self.ball = [chamber for level in self.levels for chamber in level]
        self.index = {chamber: i for i, chamber in enumerate(self.ball)}
        self.adjacency = [
            [
                self.index[nxt]
                for generator in self.reflections
                if (nxt := matrix_multiply(chamber, generator)) in self.index
            ]
            for chamber in self.ball
        ]

    @lru_cache(maxsize=None)
    def distance(self, first: int, second: int) -> int:
        relative = matrix_multiply(inverse_lorentz(self.ball[first]), self.ball[second])
        return self.length.get(relative, self.maximum_size + 1)

    @lru_cache(maxsize=None)
    def interval(self, first: int, second: int) -> frozenset[int] | None:
        """All chambers on all minimal galleries between two chambers."""
        distance = self.distance(first, second)
        if distance >= self.maximum_size:
            return None
        target = self.ball[second]
        output = {self.ball[first]}
        frontier = {self.ball[first]}
        for step in range(distance):
            next_frontier = set()
            desired = distance - step - 1
            for chamber in frontier:
                for generator in self.reflections:
                    nxt = matrix_multiply(chamber, generator)
                    relative = matrix_multiply(inverse_lorentz(nxt), target)
                    if self.length.get(relative) == desired:
                        next_frontier.add(nxt)
            output.update(next_frontier)
            frontier = next_frontier
            if len(output) > self.maximum_size:
                return None
        # A convex set of <= maximum_size chambers containing the identity is
        # connected, so all of its chambers lie in this radius-(max-1) ball.
        if any(chamber not in self.index for chamber in output):
            return None
        return frozenset(self.index[chamber] for chamber in output)

    def convex_hull(self, chamber_ids: set[int] | frozenset[int]) -> frozenset[int] | None:
        result = set(chamber_ids)
        while True:
            additions: set[int] = set()
            ordered = sorted(result)
            for position, first in enumerate(ordered):
                for second in ordered[position + 1:]:
                    interval = self.interval(first, second)
                    if interval is None:
                        return None
                    additions.update(interval - result)
            if not additions:
                return frozenset(result)
            result.update(additions)
            if len(result) > self.maximum_size:
                return None

    def enumerate_convex_sets(self) -> set[frozenset[int]]:
        all_sets = {frozenset({0})}
        frontier = {frozenset({0})}
        while frontier:
            new_frontier: set[frozenset[int]] = set()
            for current in frontier:
                boundary_neighbors = {
                    neighbor
                    for chamber in current
                    for neighbor in self.adjacency[chamber]
                    if neighbor not in current
                }
                for neighbor in boundary_neighbors:
                    hull = self.convex_hull(set(current) | {neighbor})
                    if hull is not None and len(hull) <= self.maximum_size and hull not in all_sets:
                        all_sets.add(hull)
                        new_frontier.add(hull)
            frontier = new_frontier
        return all_sets

    def boundary_normals(self, chamber_ids: frozenset[int]) -> list[tuple[int, ...]]:
        planes = set()
        for chamber_id in chamber_ids:
            chamber = self.ball[chamber_id]
            for face, generator in enumerate(self.reflections):
                neighbor = matrix_multiply(chamber, generator)
                if self.index.get(neighbor) not in chamber_ids:
                    planes.add(primitive(matrix_vector(chamber, self.normals[face])))
        return sorted(planes)

    @staticmethod
    def classification(shape: dict) -> str:
        if shape["finite_vertices"]:
            return "has_finite_boundary_vertex"
        if not shape["ideal_vertices"]:
            return "no_recovered_vertices"
        if shape["degenerate_facets"]:
            return "degenerate_boundary_facet"
        if shape["bad_edges"]:
            return "non_right_boundary_edge"
        if shape["euler_characteristic"] != 2:
            return "non_spherical_boundary"
        if any(valence != 4 for valence in shape["vertex_valences"]):
            return "non_four_valent_ideal_vertex"
        return "ideal_right_angled"

    def run(self) -> dict:
        convex_sets = self.enumerate_convex_sets()
        counts = Counter(len(chambers) for chambers in convex_sets)
        outcomes = Counter()
        valid = []
        for chambers in sorted(convex_sets, key=lambda item: (len(item), tuple(sorted(item)))):
            boundary = self.boundary_normals(chambers)
            shape = polyhedron_data(boundary)
            classification = self.classification(shape)
            outcomes[(len(chambers), classification)] += 1
            if classification == "ideal_right_angled":
                valid.append({
                    "quarter_count": len(chambers),
                    "rooted_chamber_ids": sorted(chambers),
                    "boundary_planes": [list(normal) for normal in boundary],
                    "shape": shape,
                })

        assert set(counts) == set(range(1, self.maximum_size + 1))
        assert all(item["quarter_count"] == 4 for item in valid)
        assert len(valid) == 3
        assert all(
            (item["shape"]["facets"], item["shape"]["vertices"], item["shape"]["edges"])
            == (8, 6, 12)
            for item in valid
        )
        return {
            "maximum_quarter_count": self.maximum_size,
            "quarter_reflection_ball_by_radius": [len(level) for level in self.levels],
            "quarter_reflection_ball_total": len(self.ball),
            "rooted_convex_unions_by_size": {str(size): counts[size] for size in sorted(counts)},
            "geometry_classification_by_size": {
                str(size): {
                    classification: outcomes[(size, classification)]
                    for _, classification in sorted(key for key in outcomes if key[0] == size)
                }
                for size in sorted(counts)
            },
            "ideal_right_angled_rooted_unions": valid,
            "conclusion": (
                "In the reflective tiling by the right-angled triangular bipyramid, "
                "every convex union of at most seven chambers that is ideal and "
                "right-angled has four chambers and is an ideal right-angled octahedron."
            ),
            "scope_limit": (
                "This does not enumerate the potentially non-reflective canonical "
                "quarter/half/octahedron decompositions in Proposition 7.10(2), and "
                "does not settle Conjecture 7.11."
            ),
        }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, help="optional JSON evidence path")
    args = parser.parse_args()

    quarter_normals, reconstruction = reconstruct_primary_geometry()
    census = ReflectiveQuarterCensus(quarter_normals, maximum_size=7).run()
    report = {
        "arithmetic": "exact integers with Lorentz form diag(-1,1,1,1)",
        "source_model": reconstruction,
        "reflective_quarter_census": census,
    }
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
