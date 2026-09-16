"""Exact convention calibration only; not a novel result or a general basis proof."""
import json, platform
import sympy as sp

def reverse_strip(tableau, mu):
    rows = [list(row) for row in tableau]
    while any(len(row) > (mu[i] if i < len(mu) else 0) for i, row in enumerate(rows)):
        corners = [i for i, row in enumerate(rows)
                   if len(row) > (mu[i] if i < len(mu) else 0)
                   and (i + 1 == len(rows) or len(rows[i + 1]) < len(row))]
        i = max(corners, key=lambda j: len(rows[j]))
        value = rows[i].pop()
        for j in range(i - 1, -1, -1):
            k = max(k for k, x in enumerate(rows[j]) if x < value)
            rows[j][k], value = value, rows[j][k]
    return [row for row in rows if row]

def matchings(vertices, fixed):
    if not vertices:
        if fixed == 0:
            yield ()
        return
    i, *rest = vertices
    if fixed > 0:
        yield from matchings(rest, fixed - 1)
    for j in rest:
        for tail in matchings([v for v in rest if v != j], fixed):
            yield ((i, j),) + tail

cases = [
    (3, 1, [[[1,2],[3]], [[1,3],[2]]]),
    (4, 0, [[[1,2],[3,4]], [[1,3],[2,4]]]),
]
results = []
for n, a, tableaux in cases:
    residuals = [reverse_strip(t, [2]) for t in tableaux]
    assert all(len(q) == 1 and len(q[0]) == 2 for q in residuals)
    # Transposing a two-entry row gives a two-entry column; inverse RSK is its transposition.
    edges = [tuple(q[0]) for q in residuals]
    loci = list(matchings(list(range(1, n + 1)), a))
    matrix = sp.Matrix([[1] + [int(edge in m) for edge in edges] for m in loci])
    results.append(dict(n=n, a=a, degree=1, tableaux=tableaux,
                        residual_tableaux=residuals, candidate_edges=edges,
                        locus_matchings=loci, evaluation_matrix=[[int(v) for v in row] for row in matrix.tolist()],
                        determinant=int(matrix.det()), rank=matrix.rank(),
                        lower_degree_rank=1, graded_rank_increment=matrix.rank()-1))
    assert abs(matrix.det()) == 1
print(json.dumps(dict(python=platform.python_version(), sympy=sp.__version__,
                     domain="exact integers/rationals", seed=None,
                     scope="Two smallest convention checks, not novel and not a universal verification",
                     cases=results), indent=2))
