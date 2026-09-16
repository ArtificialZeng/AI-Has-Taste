"""Bounded exact recovery check; neither an all-k proof nor a referee report.

Run from the project root with python3 evidence/recovery-check.py.
Counts ordered disjoint independent-set pairs, separately from probe.py.
"""
from fractions import Fraction
from itertools import combinations
from math import factorial
from pathlib import Path
import hashlib
import json

JOB = "primary-20260914-lorentzian-cliques-triage-06c34b78afa0"


def coefficient(n, edges, a, b):
    def masks(size):
        for vertices in combinations(range(n), size):
            mask = sum(1 << v for v in vertices)
            if all(not (mask >> u & 1 and mask >> v & 1) for u, v in edges):
                yield mask
    first, second = list(masks(a)), list(masks(b))
    return sum(not (u & v) for u in first for v in second)


def determinant(m):
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
            - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
            + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))


A = [[0, 1, 1], [1, 0, 1], [1, 1, 1]]
# Characteristic polynomial from the three elementary matrix invariants.
trace = sum(A[i][i] for i in range(3))
minors = sum(A[i][i] * A[j][j] - A[i][j] * A[j][i]
             for i in range(3) for j in range(i + 1, 3))
charpoly = [1, -trace, minors, -determinant(A)]
assert charpoly == [1, -1, -3, -1]  # (z+1)(z^2-2z-1)

cycles, boundaries = [], []
previous = json.loads(Path("evidence/cycles.json").read_text())
for k in range(2, 8):
    n, beta = 2 * k, [k - 1, k - 1, 0]
    edges = [(i, (i + 1) % n) for i in range(n)]
    hessian = []
    counts = {}
    for i in range(3):
        row = []
        for j in range(3):
            exponent = beta.copy()
            exponent[i] += 1
            exponent[j] += 1
            c = coefficient(n, edges, exponent[0], exponent[1])
            counts[",".join(map(str, exponent))] = c
            row.append(c * factorial(exponent[0]) * factorial(exponent[1])
                       * factorial(exponent[2]))
        hessian.append(row)
    normalized = [[Fraction(v, 2 * factorial(k) ** 2) for v in row]
                  for row in hessian]
    assert normalized == [[0, 1, 1], [1, 0, 1],
                          [1, 1, Fraction(6 * (k - 1), k)]]
    assert determinant(normalized) == Fraction(-4 * k + 6, k) < 0
    if k <= 5:
        assert hessian == previous["checks"][k - 2]["H"]
    cycles.append({"k": k, "coefficients": counts, "hessian": hessian,
                   "normalized_determinant": str(determinant(normalized))})
    complete_edges = [(i, j) for i in range(k) for j in range(k, n)]
    boundary = coefficient(n, complete_edges, k - 1, k - 1)
    assert boundary == (12 if k == 2 else 2 * k * k)
    boundaries.append({"k": k, "coefficient": boundary,
                       "twice_k_squared": 2 * k * k})

result = {
    "job_id": JOB,
    "method": "Exact integer enumeration of ordered disjoint independent-set pairs",
    "coverage": "C_(2k) and K_(k,k), k=2..7 only",
    "target": A,
    "target_charpoly_descending": charpoly,
    "target_eigenvalues": ["-1", "1-sqrt(2)", "1+sqrt(2)"],
    "cycles": cycles,
    "complete_bipartite_boundary": boundaries,
    "correction": "K_(k,k) has coefficient 2k^2 only for k>=3; k=2 has 12",
    "scope": "Recovery evidence; no independent referee acceptance or novelty certification",
    "source_sha256": hashlib.sha256(Path("source.md").read_bytes()).hexdigest(),
    "saved_argument_sha256": hashlib.sha256(
        Path("evidence/even-cycle-argument.md").read_bytes()).hexdigest(),
}
destination = Path("evidence/recovery-check.json")
temporary = destination.with_suffix(".json.tmp")
temporary.write_text(json.dumps(result, indent=2) + "\n")
temporary.replace(destination)
print(json.dumps({"output": str(destination), "cycles": len(cycles),
                  "boundary_values": [r["coefficient"] for r in boundaries],
                  "all_exact_assertions_passed": True}))
