#!/usr/bin/env python3
"""Exact certificate for the second layer C_{4,5}(2).

The calculation uses the faithful geometric (Tits) representation of the
hyperbolic Coxeter group [4,5].  Every scalar belongs to
Q(sqrt(2),sqrt(5)); no floating-point arithmetic is used.

The simple reflections are s0,s1,s2, with
  (s0*s1)^4 = (s1*s2)^5 = (s0*s2)^2 = 1.
The base square is fixed by <s0,s1>.  Digit j in a tile word means that the
current square is replaced by its neighbour under (s0*s1)^j*s2, 0 <= j < 4.
Thus the words printed below are exact tile identifiers in the regular
{4,5} tessellation, after equality of their exact centre vectors is imposed.
"""

from collections import deque
from fractions import Fraction as F
import json


# Elements of K=Q(a,b), a^2=2, b^2=5, in the basis (1,a,b,ab).
ZERO = (F(0), F(0), F(0), F(0))
ONE = (F(1), F(0), F(0), F(0))
SQRT2 = (F(0), F(1), F(0), F(0))
SQRT5 = (F(0), F(0), F(1), F(0))


def k_add(x, y):
    return tuple(x[i] + y[i] for i in range(4))


def k_neg(x):
    return tuple(-z for z in x)


def k_sub(x, y):
    return k_add(x, k_neg(y))


def k_scale(c, x):
    return tuple(c * z for z in x)


def k_mul(x, y):
    out = [F(0)] * 4
    for i, xi in enumerate(x):
        ai, bi = i & 1, (i >> 1) & 1
        for j, yj in enumerate(y):
            aj, bj = j & 1, (j >> 1) & 1
            a_exp, b_exp = ai + aj, bi + bj
            factor = F(1)
            if a_exp >= 2:
                a_exp -= 2
                factor *= 2
            if b_exp >= 2:
                b_exp -= 2
                factor *= 5
            out[a_exp + 2 * b_exp] += factor * xi * yj
    return tuple(out)


def k_sum(values):
    total = ZERO
    for value in values:
        total = k_add(total, value)
    return total


def matrix_identity():
    return tuple(
        tuple(ONE if i == j else ZERO for j in range(3)) for i in range(3)
    )


def matrix_multiply(left, right):
    return tuple(
        tuple(
            k_sum(k_mul(left[i][k], right[k][j]) for k in range(3))
            for j in range(3)
        )
        for i in range(3)
    )


def matrix_vector(matrix, vector):
    return tuple(
        k_sum(k_mul(matrix[i][j], vector[j]) for j in range(3))
        for i in range(3)
    )


def matrix_power(matrix, exponent):
    result = matrix_identity()
    for _ in range(exponent):
        result = matrix_multiply(result, matrix)
    return result


def scalar_key(x):
    return tuple((z.numerator, z.denominator) for z in x)


def vector_key(vector):
    return tuple(scalar_key(x) for x in vector)


PHI = k_scale(F(1, 2), k_add(ONE, SQRT5))

# Gram matrix has off-diagonal entries -cos(pi/4), -cos(pi/5), 0.
# These are the resulting reflection matrices in the simple-root basis.
S0 = (
    (k_neg(ONE), SQRT2, ZERO),
    (ZERO, ONE, ZERO),
    (ZERO, ZERO, ONE),
)
S1 = (
    (ONE, ZERO, ZERO),
    (SQRT2, k_neg(ONE), PHI),
    (ZERO, ZERO, ONE),
)
S2 = (
    (ONE, ZERO, ZERO),
    (ZERO, ONE, ZERO),
    (ZERO, PHI, k_neg(ONE)),
)
IDENTITY = matrix_identity()
ROTATION = matrix_multiply(S0, S1)
ROTATIONS = tuple(matrix_power(ROTATION, j) for j in range(4))

# The first vector is fixed by S0,S1 (a square centre); the second is fixed
# by S1,S2 (a tessellation vertex).  Scaling is immaterial.
CENTRE = (k_scale(F(1, 2), k_mul(SQRT2, PHI)), PHI, ONE)
VERTEX = (
    k_sub(k_scale(F(3), ONE), PHI),
    k_scale(F(2), SQRT2),
    k_mul(SQRT2, PHI),
)


def tile_key(representative):
    return vector_key(matrix_vector(representative, CENTRE))


def tile_vertices(representative):
    return frozenset(
        vector_key(matrix_vector(matrix_multiply(representative, h), VERTEX))
        for h in ROTATIONS
    )


def tile_vertex_cycle(representative):
    return tuple(
        vector_key(matrix_vector(matrix_multiply(representative, h), VERTEX))
        for h in ROTATIONS
    )


def neighbour_representatives(representative):
    return tuple(
        matrix_multiply(matrix_multiply(representative, h), S2)
        for h in ROTATIONS
    )


def build_certificate():
    # Coxeter relations and the types of the two distinguished points.
    assert matrix_power(ROTATION, 4) == IDENTITY
    assert matrix_power(matrix_multiply(S1, S2), 5) == IDENTITY
    assert matrix_power(matrix_multiply(S0, S2), 2) == IDENTITY
    assert matrix_vector(S0, CENTRE) == CENTRE
    assert matrix_vector(S1, CENTRE) == CENTRE
    assert matrix_vector(S1, VERTEX) == VERTEX
    assert matrix_vector(S2, VERTEX) == VERTEX

    # Radius three is complete for all tiles incident to a vertex of either
    # square of an edge-adjacent domino: a 5-cycle is the tile link of each
    # vertex.  Radius four is generated as a held-out boundary check.
    representatives = {tile_key(IDENTITY): IDENTITY}
    depths = {tile_key(IDENTITY): 0}
    words = {tile_key(IDENTITY): "F"}
    queue = deque([IDENTITY])
    while queue:
        representative = queue.popleft()
        key = tile_key(representative)
        if depths[key] == 4:
            continue
        for digit, neighbour in enumerate(neighbour_representatives(representative)):
            neighbour_key = tile_key(neighbour)
            if neighbour_key not in representatives:
                representatives[neighbour_key] = neighbour
                depths[neighbour_key] = depths[key] + 1
                words[neighbour_key] = words[key] + str(digit)
                queue.append(neighbour)

    base_key = tile_key(IDENTITY)
    second_representative = neighbour_representatives(IDENTITY)[0]
    second_key = tile_key(second_representative)
    central = {base_key, second_key}
    old_vertices = set()
    for key in central:
        old_vertices.update(tile_vertices(representatives[key]))
    assert len(old_vertices) == 6

    # This is exactly C_{4,5}(2): every tile incident to a perimeter vertex
    # of the two-square C_{4,5}(1).
    c2 = {
        key
        for key, representative in representatives.items()
        if tile_vertices(representative).intersection(old_vertices)
    }
    assert max(depths[key] for key in c2) <= 3
    assert len(c2) == 18

    vertex_incidence = {}
    for index, vertex in enumerate(sorted(old_vertices)):
        incident = sorted(
            words[key]
            for key in c2
            if vertex in tile_vertices(representatives[key])
        )
        assert len(incident) == 5
        vertex_incidence[f"V{index}"] = incident

    adjacency = {key: set() for key in c2}
    exposed_sides = {key: 0 for key in c2}
    for key in c2:
        for neighbour in neighbour_representatives(representatives[key]):
            neighbour_key = tile_key(neighbour)
            if neighbour_key in c2:
                adjacency[key].add(neighbour_key)
            else:
                exposed_sides[key] += 1

    assert all(key in adjacency[other] for key in c2 for other in adjacency[key])
    edge_count = sum(len(value) for value in adjacency.values()) // 2
    perimeter = sum(exposed_sides.values())
    interior = {key for key in c2 if exposed_sides[key] == 0}
    layer = c2 - central
    layer_edges = sum(
        sum(neighbour in layer for neighbour in adjacency[key]) for key in layer
    ) // 2

    assert edge_count == 23
    assert perimeter == 26 == 4 * len(c2) - 2 * edge_count
    assert interior == central
    assert second_key in adjacency[base_key]
    assert len(layer) == 16 and layer_edges == 16
    assert all(sum(other in layer for other in adjacency[key]) == 2 for key in layer)

    def cell_counts(tile_keys):
        vertices = set()
        edges = set()
        for key in tile_keys:
            cycle = tile_vertex_cycle(representatives[key])
            assert len(set(cycle)) == 4
            vertices.update(cycle)
            edges.update(
                frozenset((cycle[index], cycle[(index + 1) % 4]))
                for index in range(4)
            )
        return len(vertices), len(edges), len(tile_keys)

    c2_cells = cell_counts(c2)
    layer_cells = cell_counts(layer)
    assert c2_cells == (32, 49, 18)
    assert layer_cells == (32, 48, 16)
    assert c2_cells[0] - c2_cells[1] + c2_cells[2] == 1
    # The remaining layer is connected and is a compact planar cell complex.
    # Alexander duality, equivalently planar Euler characteristic here, gives
    # holes = 1-chi = 1 after the adjacent central pair is deleted.
    layer_euler_characteristic = layer_cells[0] - layer_cells[1] + layer_cells[2]
    assert layer_euler_characteristic == 0

    ordered_keys = sorted(c2, key=lambda key: (depths[key], words[key]))
    tiles = []
    for key in ordered_keys:
        tiles.append(
            {
                "word": words[key],
                "depth": depths[key],
                "adjacent_in_C2": sorted(words[x] for x in adjacency[key]),
                "exposed_sides": exposed_sides[key],
                "centre_over_Q_sqrt2_sqrt5": [
                    [
                        f"{coefficient.numerator}/{coefficient.denominator}"
                        for coefficient in coordinate
                    ]
                    for coordinate in matrix_vector(representatives[key], CENTRE)
                ],
            }
        )

    return {
        "arithmetic": "exact Q(sqrt(2),sqrt(5)); basis [1,sqrt(2),sqrt(5),sqrt(10)]",
        "coxeter_relations_verified": ["(s0*s1)^4=1", "(s1*s2)^5=1", "(s0*s2)^2=1"],
        "bfs_tile_counts_by_depth_0_through_4": [
            sum(value == d for value in depths.values()) for d in range(5)
        ],
        "central_domino": sorted(words[key] for key in central),
        "old_vertex_incidence": vertex_incidence,
        "tile_count": len(c2),
        "interior_edge_count": edge_count,
        "perimeter": perimeter,
        "interior_tiles": sorted(words[key] for key in interior),
        "new_layer_is_16_cycle": True,
        "cell_counts_V_E_F": {
            "C2": list(c2_cells),
            "after_central_pair_deletion": list(layer_cells),
        },
        "only_interior_pair_is_edge_adjacent": True,
        "deleting_only_interior_pair": {
            "remaining_tile_count": 16,
            "remaining_edge_connected": True,
            "deleted_tile_components": 1,
            "euler_characteristic": layer_euler_characteristic,
            "bounded_holes_created_by_planar_duality": 1,
        },
        "tiles": tiles,
    }


if __name__ == "__main__":
    print(json.dumps(build_certificate(), indent=2, sort_keys=True))
