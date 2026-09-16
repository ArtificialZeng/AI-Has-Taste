"""Separate exact-rank implementation using every original matrix coordinate.

Enumerates points via permutations, not recursive matchings; does not import
the candidate generator or its elimination code. Reuses saved candidate data.
Run: python3 evidence/verify_triage_rank.py > evidence/triage-rank-verification.json
"""
import json
from itertools import permutations, combinations_with_replacement
from pathlib import Path
import sympy as sp
from sympy.polys.matrices import DomainMatrix


def rank(columns, nrows):
    if not columns:
        return 0
    matrix = sp.Matrix(nrows, len(columns), lambda i, j: columns[j][i])
    return DomainMatrix.from_Matrix(matrix).convert_to(sp.QQ).rank()


data = json.loads(Path('evidence/triage-rank.json').read_text())
results = []
for case in data['cases']:
    n, a = case['n'], case['a']
    points = [p for p in permutations(range(n))
              if all(p[p[i]] == i for i in range(n))
              and sum(p[i] == i for i in range(n)) == a]
    assert len(points) == case['point_count']
    recovered = {tuple((i+1, p[i]+1) for i in range(n) if i < p[i]) for p in points}
    assert recovered == {tuple(map(tuple, m)) for m in case['points']}
    coordinates = [[int(p[i] == j) for p in points] for i in range(n) for j in range(n)]
    lower, checks = [], []
    for grade in case['grades']:
        d = grade['degree']
        lower_rank = rank(lower, len(points))
        candidate = [record['monomial'] for record in case['candidate_data']
                     if len(record['monomial']) == d]
        candidate_columns = [[int(all(p[i-1] == j-1 for i, j in m)) for p in points]
                             for m in candidate]
        augmented_rank = rank(lower+candidate_columns, len(points))
        # All monomials in all n^2 coordinates, including diagonals and repeats.
        degree_columns = []
        for indices in combinations_with_replacement(range(n*n), d):
            degree_columns.append([int(all(coordinates[j][i] for j in indices))
                                   for i in range(len(points))])
        lower += degree_columns
        full_rank = rank(lower, len(points))
        assert (lower_rank, augmented_rank, full_rank) == (
            grade['lower_rank'], grade['augmented_rank'], grade['full_filtered_rank'])
        checks.append(dict(degree=d, lower_rank=lower_rank,
                           augmented_rank=augmented_rank, full_rank=full_rank,
                           original_coordinate_monomials_through_degree=len(lower)))
    results.append(dict(n=n, a=a, checks=checks))
print(json.dumps(dict(domain='QQ', sympy=sp.__version__,
                     scope='Independent point enumeration and full-coordinate exact rank; candidate generation is reused',
                     all_checks_passed=True, cases=results), indent=2))
