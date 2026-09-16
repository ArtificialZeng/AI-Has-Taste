"""Exact, bounded triage checks. Run: python3 evidence/triage_checks.py.

Outputs evidence/triage_checks.json. No floating-point root computation.
These are calibration and theorem-hypothesis tests, not a uniform proof.
"""
from pathlib import Path
from itertools import permutations
from math import comb
import hashlib
import json
import platform
import sympy as s

ROOT = Path(__file__).resolve().parents[1]
JOB = "primary-20260914-triangular-square-roots-triage-fae16c3d4f8c"
SOURCE_HASH = "a1a75e5793dcd6534b63902eb3b6d415dfd60e8f129376f7af671b7b9401f1f3"
assert hashlib.sha256((ROOT / "source.md").read_bytes()).hexdigest() == SOURCE_HASH
N = 12
x = s.symbols("x")

# Eulerian recurrence, checked against exhaustive permutation enumeration.
A = [[1]]
for n in range(1, N + 1):
    old = A[-1]
    A.append([(n-k+1)*(old[k-1] if k else 0)
              + k*(old[k] if k < n else 0) for k in range(n+1)])
for n in range(1, 8):
    row = [0]*(n+1)
    for p in permutations(range(1, n+1)):
        row[1+sum(p[j] > p[j+1] for j in range(n-1))] += 1
    assert row == A[n]

# Independent rectangular lattice DP, checked against the binomial formula.
grid = [[0]*(N+1) for _ in range(N+1)]
grid[0][0] = 1
for a in range(N+1):
    for b in range(N+1):
        if a or b:
            grid[a][b] = ((grid[a-1][b] if a else 0)
                          + (grid[a][b-1] if b else 0)
                          + (grid[a-1][b-1] if a and b else 0))
D = [[grid[n-k][k] for k in range(n+1)] for n in range(N+1)]
assert all(D[n][k] == sum(comb(n-k,j)*comb(k,j)*2**j
                         for j in range(min(n-k,k)+1))
           for n in range(N+1) for k in range(n+1))

def square(T):
    return [[sum(T[n][i]*T[i][k] for i in range(k,n+1))
             for k in range(n+1)] for n in range(N+1)]

def polynomial(row):
    return s.Poly.from_list(row[::-1], x, domain=s.ZZ)

squared = {"A": square(A), "D": square(D)}
cases = []
for name, rows in squared.items():
    for n, row in enumerate(rows):
        p = polynomial(row)
        real_count = sum(int(f.count_roots(-s.oo,s.oo))*m
                         for f,m in p.sqf_list()[1])
        assert real_count == p.degree()
        assert all(c >= 0 for c in row) and any(c > 0 for c in row)
        cases.append({"matrix": name, "n": n, "coefficients_ascending": row,
                      "degree": int(p.degree()), "real_root_multiplicity": real_count,
                      "all_roots_nonpositive": True})

G = [polynomial(row) for row in squared["D"]]
assert [g.as_expr() for g in G[:4]] == [1,x+2,x*x+6*x+5,x**3+10*x*x+25*x+12]
assert all(G[n] == (x+3)*G[n-1]+(x-1)*G[n-2]+(x-1)*G[n-3]+x*G[n-4]
           for n in range(4,N+1))
isolation = []
previous = []
for n in range(1,N+1):
    data = G[n].intervals(eps=s.Rational(1,10**6))
    assert len(data) == n and all(m == 1 for ab,m in data)
    intervals = [ab for ab,m in data]
    assert all(b < 0 for a,b in intervals)
    assert all(intervals[i][1] < previous[i][0]
               and previous[i][1] < intervals[i+1][0] for i in range(n-1))
    isolation.append({"n": n, "simple_negative_roots": True,
                      "strictly_interlaces_previous": True,
                      "rational_intervals": [[str(a),str(b)] for a,b in intervals]})
    previous = intervals

# Exact failure of the direct Athanasiadis cone hypothesis at n=3.
basis = [x**(3-k)*(1+x)**k for k in range(4)]
coefficients = [-2,2,1,0]
assert s.expand(sum(c*b for c,b in zip(coefficients,basis))) == polynomial(A[3]).as_expr()

# Q(M) = M diag(1,M^{-1}); finite leading blocks determine these entries exactly.
def matrix(rows):
    return s.Matrix(N+1,N+1,lambda n,k: rows[n][k] if k <= n else 0)

def left_production(M):
    B = s.diag(s.ones(1,1),M[:N,:N])
    Q = M * B.inv()
    assert Q*B == M
    return Q

GM = matrix(squared["D"])
QG = left_production(GM)
witness = QG.extract([4,5,6],[0,1,2])
assert witness.det() == -32
reversed_G = s.Matrix(N+1,N+1,lambda n,k: GM[n,n-k] if k <= n else 0)
QR = left_production(reversed_G)
assert QR[5,1] == s.Rational(-59,145)
QA = left_production(matrix(squared["A"]))
assert QA[7,2] == -18694
known = s.Poly(x**3+14*x**2+59*x+64,x)
assert known.count_roots(-s.oo,s.oo) == 1

result = {
    "job_id": JOB, "source_sha256": SOURCE_HASH,
    "python": platform.python_version(), "sympy": s.__version__,
    "arithmetic": "ZZ/QQ exact; squarefree Sturm counts and rational root isolation",
    "range": [0,N], "seed": None,
    "Eulerian_permutation_enumeration_range": [1,7],
    "Delannoy_lattice_and_binomial_formula_agree": True,
    "ordinary_matrix_square_cases": cases,
    "D_source_recurrence_matches_range": [4,N],
    "D_interlacing_certificates": isolation,
    "A3_cone_basis": [str(s.expand(b)) for b in basis],
    "A3_cone_coordinates": coefficients,
    "left_production_obstructions": {
        "indexing": "zero based; Q(M)=M diag(1,M^-1)",
        "D_square": {"rows": [4,5,6], "columns": [0,1,2],
                     "submatrix": [[int(c) for c in row] for row in witness.tolist()],
                     "determinant": -32},
        "D_square_row_reversal": {"entry": [5,1], "value": "-59/145"},
        "A_square": {"entry": [7,2], "value": -18694}
    },
    "known_D_nonpreserver": {"polynomial": str(known.as_expr()), "real_roots": 1,
                              "scope": "Not a square-row counterexample"},
    "limitations": "Finite calibration only; production obstructions reject a sufficient criterion, not the original claim or all network methods."
}
target = ROOT / "evidence/triage_checks.json"
temporary = target.with_suffix(".json.tmp")
temporary.write_text(json.dumps(result,indent=2)+"\n")
temporary.replace(target)
print(json.dumps({"output": str(target.relative_to(ROOT)), "square_rows_checked":len(cases),
                  "D_strict_interlacing_range":[1,N], "D_Q_negative_minor":-32,
                  "D_reversed_Q_negative_entry":"-59/145", "A_Q_negative_entry":-18694}))
