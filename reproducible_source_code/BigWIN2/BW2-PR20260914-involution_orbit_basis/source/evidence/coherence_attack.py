"""Test whether the proposed basis could be standard for a monomial order.

Construct exact straightening relations by QQ evaluation. A necessary condition
for standardness is m>b for every nonzero degree-d term b in the normal form of
a noncandidate degree-d monomial m. Seek a positive multiplicative cycle using
a floating LP, then verify its coefficients and every relation exactly.
Run: python3 evidence/coherence_attack.py 5 1
LP alone is diagnostic; only the exact certificate is mathematical evidence.
"""
import json
import sys
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from flint import fmpq_mat
from triage_rank import candidates
from research_rank import all_matchings, columns_for, atomic_json


def attack(n, a):
    k = (n-a)//2
    points = [frozenset(p) for p in all_matchings(n,k)]
    basis = [m for d in range(k+1) for m in candidates(n,a,d)[0]]
    assert len(basis) == len(points)
    columns = columns_for(basis, points)
    mat = fmpq_mat(columns).transpose()
    edges = list(combinations(range(1,n+1),2))
    relations, constraints = [], []
    for d in range(1,k+1):
        excluded = [m for m in all_matchings(n,d) if m not in basis]
        if not excluded:
            continue
        rhs = fmpq_mat(columns_for(excluded, points)).transpose()
        coeff = mat.solve(rhs)
        assert mat*coeff == rhs
        for j,m in enumerate(excluded):
            terms = [(b,str(coeff[i,j])) for i,b in enumerate(basis) if coeff[i,j]]
            assert all(len(b) <= d for b,c in terms)
            rel = len(relations)
            relations.append(dict(monomial=m, evaluation_expansion=terms))
            for b,c in terms:
                if len(b) == d:
                    diff = [int(e in m)-int(e in b) for e in edges]
                    constraints.append(dict(relation=rel, leading=m, smaller=b,
                                            exponent_difference=diff))
    matrix = np.array([c['exponent_difference'] for c in constraints],dtype=float)
    primal = linprog(np.zeros(len(edges)), A_ub=-matrix,
                     b_ub=-np.ones(len(constraints)),bounds=[(None,None)]*len(edges),
                     method='highs')
    result = dict(n=n,a=a,arithmetic='QQ straightening; LP discovery only',
                  edges=edges, basis=basis,relations=relations,constraints=constraints,
                  primal_status=int(primal.status), exact_obstruction=False)
    if primal.success:
        weights = [str(Fraction(float(w)).limit_denominator(1000000)) for w in primal.x]
        wf = list(map(Fraction,weights))
        assert all(sum(x*y for x,y in zip(c['exponent_difference'],wf)) > 0
                   for c in constraints)
        result.update(feasible_rational_weights=weights, exact_feasibility_verified=True)
    elif primal.status == 2:
        dual = linprog(np.arange(len(constraints),dtype=float),
                       A_eq=np.vstack([matrix.T,np.ones((1,len(constraints)))]),
                       b_eq=np.r_[np.zeros(len(edges)),1.0],bounds=(0,None),method='highs')
        assert dual.success
        weights = [Fraction(float(w)).limit_denominator(1000000) for w in dual.x]
        assert all(w >= 0 for w in weights) and sum(weights) == 1
        assert all(sum(w*c['exponent_difference'][i] for w,c in zip(weights,constraints)) == 0
                   for i in range(len(edges)))
        result.update(exact_obstruction=True,
                      cycle=[dict(constraint=i,weight=str(w)) for i,w in enumerate(weights) if w])
    atomic_json(Path(f'evidence/coherence-n{n}a{a}.json'),result)
    print(json.dumps({k:v for k,v in result.items() if k not in
                      ['edges','basis','relations','constraints']},indent=2))


if __name__ == '__main__':
    attack(*map(int,sys.argv[1:]))
