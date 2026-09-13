#!/usr/bin/env python3
"""Exact cellular-homology certificates for Sigma(K4-e,{k},3).

Only the Python standard library is used.  The script fixes explicit cell
bases, constructs d1 and d2 from the cubical product rule, obtains an integral
basis of ker(d1) from a deterministic spanning tree, and computes a Smith
reduction U*R*V=D of the relation matrix R in that kernel basis.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import deque
from itertools import product
from pathlib import Path


VERTICES = ("a", "b", "c", "d")
EDGES = (("a", "c"), ("a", "d"), ("b", "c"), ("b", "d"), ("c", "d"))
ATOMS = tuple(("v", v) for v in VERTICES) + tuple(("e", u, v) for u, v in EDGES)


def dim(atom):
    return 0 if atom[0] == "v" else 1


def atom_text(atom):
    return atom[1] if atom[0] == "v" else f"[{atom[1]},{atom[2]}]"


def cell_text(cell):
    return " x ".join(atom_text(a) for a in cell)


def cells(anchor, degree):
    ans = []
    for c in product(ATOMS, repeat=3):
        if sum(dim(a) for a in c) != degree:
            continue
        if not any(a == ("v", anchor) for a in c):
            continue
        ans.append(c)
    return ans


def zero_matrix(m, n):
    return [[0 for _ in range(n)] for _ in range(m)]


def identity(n):
    a = zero_matrix(n, n)
    for i in range(n):
        a[i][i] = 1
    return a


def matmul(a, b):
    if not a or not b:
        return []
    assert len(a[0]) == len(b)
    bt = list(zip(*b))
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def matrices(anchor):
    bases = [cells(anchor, q) for q in range(3)]
    indices = [{c: i for i, c in enumerate(b)} for b in bases]
    ds = [None]
    for q in (1, 2):
        source, target = bases[q], bases[q - 1]
        d = zero_matrix(len(target), len(source))
        for j, c in enumerate(source):
            preceding_degree = 0
            for pos, a in enumerate(c):
                if a[0] == "e":
                    sign = -1 if preceding_degree % 2 else 1
                    for endpoint, endpoint_sign in ((a[1], -1), (a[2], 1)):
                        face = list(c)
                        face[pos] = ("v", endpoint)
                        face = tuple(face)
                        d[indices[q - 1][face]][j] += sign * endpoint_sign
                preceding_degree += dim(a)
        ds.append(d)
    return bases, ds[1], ds[2]


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.parent[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        return True


def edge_endpoints(d1, edge_index):
    nz = [(i, d1[i][edge_index]) for i in range(len(d1)) if d1[i][edge_index]]
    assert len(nz) == 2 and sorted(v for _, v in nz) == [-1, 1]
    tail = next(i for i, v in nz if v == -1)
    head = next(i for i, v in nz if v == 1)
    return tail, head


def spanning_tree_and_kernel(d1):
    n0, n1 = len(d1), len(d1[0])
    ends = [edge_endpoints(d1, j) for j in range(n1)]
    dsu = DSU(n0)
    tree, chords = [], []
    for j, (tail, head) in enumerate(ends):
        (tree if dsu.union(tail, head) else chords).append(j)
    components = len({dsu.find(i) for i in range(n0)})

    adjacency = [[] for _ in range(n0)]
    for j in tree:
        tail, head = ends[j]
        adjacency[tail].append((head, j, 1))
        adjacency[head].append((tail, j, -1))
    for row in adjacency:
        row.sort()

    kernel = []
    for chord in chords:
        tail, head = ends[chord]
        parent = {tail: None}
        todo = deque([tail])
        while todo and head not in parent:
            u = todo.popleft()
            for v, edge, traversal_sign in adjacency[u]:
                if v not in parent:
                    parent[v] = (u, edge, traversal_sign)
                    todo.append(v)
        assert head in parent
        path = []
        v = head
        while v != tail:
            u, edge, traversal_sign = parent[v]
            path.append((edge, traversal_sign))
            v = u
        z = [0] * n1
        z[chord] = 1
        for edge, traversal_sign in path:
            z[edge] -= traversal_sign
        kernel.append(z)
    # Columns are the fundamental cycles.
    kernel_matrix = [[kernel[j][i] for j in range(len(kernel))] for i in range(n1)]
    return components, tree, chords, kernel_matrix


def row_swap(a, i, j):
    a[i], a[j] = a[j], a[i]


def row_add(a, target, source, multiple):
    if multiple:
        a[target] = [x + multiple * y for x, y in zip(a[target], a[source])]


def row_scale(a, row, multiple):
    a[row] = [multiple * x for x in a[row]]


def col_swap(a, i, j):
    for row in a:
        row[i], row[j] = row[j], row[i]


def col_add(a, target, source, multiple):
    if multiple:
        for row in a:
            row[target] += multiple * row[source]


def smith_form(original):
    """Return U,D,V and an elementary-operation audit with U*A*V=D.

    This is the standard Euclidean pivot algorithm.  Once a pivot has zero
    row and column, an entry of the trailing block not divisible by the pivot
    is folded into the pivot row; Euclidean reduction then strictly decreases
    the pivot.  Hence finalized positive pivots divide the whole trailing block
    and therefore all later pivots.
    """
    a = [row[:] for row in original]
    m = len(a)
    n = len(a[0]) if m else 0
    u = identity(m)
    v = identity(n)
    ops = []

    def rs(i, j):
        row_swap(a, i, j); row_swap(u, i, j); ops.append(["row_swap", i, j])

    def ra(i, j, q):
        row_add(a, i, j, q); row_add(u, i, j, q); ops.append(["row_add", i, j, q])

    def rneg(i):
        row_scale(a, i, -1); row_scale(u, i, -1); ops.append(["row_neg", i])

    def cs(i, j):
        col_swap(a, i, j); col_swap(v, i, j); ops.append(["col_swap", i, j])

    def ca(i, j, q):
        col_add(a, i, j, q); col_add(v, i, j, q); ops.append(["col_add", i, j, q])

    k = 0
    while k < m and k < n:
        nonzero = [(abs(a[i][j]), i, j)
                   for i in range(k, m) for j in range(k, n) if a[i][j]]
        if not nonzero:
            break
        _, i, j = min(nonzero)
        if i != k:
            rs(k, i)
        if j != k:
            cs(k, j)

        while True:
            changed = False
            for i in range(k + 1, m):
                if a[i][k]:
                    q = a[i][k] // a[k][k]
                    ra(i, k, -q)
                    if a[i][k]:
                        rs(i, k)
                    changed = True
                    break
            if changed:
                continue
            for j in range(k + 1, n):
                if a[k][j]:
                    q = a[k][j] // a[k][k]
                    ca(j, k, -q)
                    if a[k][j]:
                        cs(j, k)
                    changed = True
                    break
            if changed:
                continue

            bad = None
            pivot = a[k][k]
            for i in range(k + 1, m):
                for j in range(k + 1, n):
                    if a[i][j] % pivot:
                        bad = (i, j)
                        break
                if bad:
                    break
            if bad is None:
                break
            # The pivot column is zero below k.  Adding the offending row to
            # the pivot row preserves the pivot and exposes the bad entry.
            ra(k, bad[0], 1)

        if a[k][k] < 0:
            rneg(k)
        k += 1

    return u, a, v, ops


def transpose(a):
    return [list(row) for row in zip(*a)]


def rank_from_smith(d):
    return sum(1 for i in range(min(len(d), len(d[0]) if d else 0)) if d[i][i])


def is_diagonal(d):
    return all(x == 0 for i, row in enumerate(d) for j, x in enumerate(row) if i != j)


def write_tsv(path, matrix):
    path.write_text("\n".join("\t".join(str(x) for x in row) for row in matrix) + "\n")


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def determinant_bareiss(a):
    a = [row[:] for row in a]
    n = len(a)
    assert all(len(row) == n for row in a)
    if n == 0:
        return 1
    sign, previous = 1, 1
    for k in range(n - 1):
        if a[k][k] == 0:
            pivot_row = next((i for i in range(k + 1, n) if a[i][k]), None)
            if pivot_row is None:
                return 0
            row_swap(a, k, pivot_row)
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator // previous
            a[i][k] = 0
        previous = pivot
    return sign * a[-1][-1]


def sparse_rows_for_kernel(b1, chords, kernel_matrix):
    rows = []
    for column, chord in enumerate(chords):
        terms = []
        for edge_index, coefficient in enumerate(row[column] for row in kernel_matrix):
            if coefficient:
                terms.append({"coefficient": coefficient,
                              "edge_index": edge_index,
                              "edge_cell": cell_text(b1[edge_index])})
        rows.append({"basis_index": column, "chord_edge_index": chord,
                     "chord_cell": cell_text(b1[chord]), "terms": terms})
    return rows


def run_anchor(anchor, out_root):
    out = out_root / f"anchor_{anchor}"
    out.mkdir(parents=True, exist_ok=True)
    bases, d1, d2 = matrices(anchor)
    components, tree, chords, kernel = spanning_tree_and_kernel(d1)
    relation = [[d2[edge][j] for j in range(len(bases[2]))] for edge in chords]

    chain_zero = matmul(d1, d2)
    kernel_zero = matmul(d1, kernel)
    reconstructed = matmul(kernel, relation)
    assert chain_zero == zero_matrix(len(bases[0]), len(bases[2]))
    assert kernel_zero == zero_matrix(len(bases[0]), len(chords))
    assert reconstructed == d2

    u, diagonal, v, operations = smith_form(relation)
    assert is_diagonal(diagonal)
    assert matmul(matmul(u, relation), v) == diagonal
    smith_rank = rank_from_smith(diagonal)
    invariant_factors = [diagonal[i][i] for i in range(smith_rank)]
    assert all(x > 0 for x in invariant_factors)
    assert all(invariant_factors[i + 1] % invariant_factors[i] == 0
               for i in range(len(invariant_factors) - 1))
    det_u, det_v = determinant_bareiss(u), determinant_bareiss(v)
    assert abs(det_u) == abs(det_v) == 1

    for degree, basis in enumerate(bases):
        (out / f"B{degree}.tsv").write_text(
            "index\tcell\n" + "".join(f"{i}\t{cell_text(c)}\n" for i, c in enumerate(basis)))
    write_tsv(out / "d1.tsv", d1)
    write_tsv(out / "d2.tsv", d2)
    write_tsv(out / "kernel_basis.tsv", kernel)
    write_tsv(out / "relations.tsv", relation)
    write_tsv(out / "smith_U.tsv", u)
    write_tsv(out / "smith_D.tsv", diagonal)
    write_tsv(out / "smith_V.tsv", v)
    (out / "smith_operations.json").write_text(json.dumps(operations, separators=(",", ":")) + "\n")
    (out / "kernel_basis_sparse.json").write_text(
        json.dumps(sparse_rows_for_kernel(bases[1], chords, kernel), indent=2) + "\n")
    (out / "spanning_tree.json").write_text(json.dumps({
        "tree_edge_indices": tree,
        "chord_edge_indices": chords,
    }, indent=2) + "\n")

    beta0 = components
    beta1 = len(chords) - smith_rank
    beta2 = len(bases[2]) - smith_rank
    torsion = [x for x in invariant_factors if x > 1]
    summary = {
        "anchor": anchor,
        "anchor_degree": 2 if anchor in ("a", "b") else 3,
        "cell_counts": [len(x) for x in bases],
        "boundary_shapes": {"d1": [len(d1), len(d1[0])],
                            "d2": [len(d2), len(d2[0])]},
        "verified": {
            "d1_d2_zero": True,
            "fundamental_cycles_in_kernel": True,
            "d2_equals_kernel_basis_times_relations": True,
            "U_relations_V_equals_D": True,
            "D_is_Smith_diagonal": True,
            "det_U": det_u,
            "det_V": det_v,
        },
        "spanning_tree_edge_count": len(tree),
        "kernel_rank_d1": len(chords),
        "rank_d2": smith_rank,
        "smith_invariant_factors_nonzero": invariant_factors,
        "torsion_invariant_factors": torsion,
        "homology": {"H0": {"free_rank": beta0, "torsion": []},
                     "H1": {"free_rank": beta1, "torsion": torsion},
                     "H2": {"free_rank": beta2, "torsion": []}},
        "smith_operation_count": len(operations),
        "basis_convention": {
            "vertices": list(VERTICES),
            "oriented_edges": [list(e) for e in EDGES],
            "atom_order": [atom_text(a) for a in ATOMS],
            "product_order": "lexicographic induced by atom_order, left factor first",
            "boundary": "d[u,v]=v-u with Koszul product signs",
            "kernel": "Kruskal tree in B1 order; each fundamental cycle has chord coefficient +1",
        },
    }
    summary_path = out / "summary.json"
    summary_path.write_text(json.dumps(summary, indent=2) + "\n")

    # Exclude the manifest itself so repeated generation is byte-for-byte
    # deterministic and does not create a self-referential hash entry.
    files = sorted(p for p in out.iterdir() if p.is_file() and p.name != "manifest.json")
    manifest = {p.name: {"sha256": sha256(p), "bytes": p.stat().st_size} for p in files}
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    return summary


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("evidence/diamond_n3"))
    args = parser.parse_args()
    summaries = [run_anchor(anchor, args.output) for anchor in ("a", "c")]
    combined = {
        "graph": {"vertices": list(VERTICES), "edges": [list(e) for e in EDGES],
                  "name": "K4-e (diamond)"},
        "n": 3,
        "anchors": summaries,
    }
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / "summary.json").write_text(json.dumps(combined, indent=2) + "\n")
    print(json.dumps(combined, indent=2))


if __name__ == "__main__":
    main()
