"""Exact verification of the proposed uniform quadratic theorem.

Run from project root: python3 evidence/verify_quadratic.py
Checks n=6..14; these finite checks supplement the symbolic proof, not replace it.
The relation matrices use only graph incidence, not evaluation on involutions.
"""
from itertools import combinations
from pathlib import Path
import json
from flint import fmpz_mat, fmpq_mat
from research_rank import all_matchings, forward_label, atomic_json
from triage_rank import candidates


def canonical(e,f):
    return tuple(sorted((tuple(sorted(e)),tuple(sorted(f)))))


def excluded(n):
    return sorted({canonical((1,2),(i,j)) for i,j in combinations(range(3,n+1),2)}
        | {canonical((1,3),(2,j)) for j in range(4,n+1)}
        | {canonical((1,j),(2,3)) for j in range(4,n+1)}
        | {canonical((1,5),(2,4)),canonical((1,5),(3,4)),canonical((2,5),(3,4))})


def main():
    results=[]
    for n in range(6,15):
        vertices=list(combinations(range(1,n+1),2))
        all_m=all_matchings(n,2)
        t=excluded(n)
        h=[m for m in all_m if m not in t]
        assert len(t)==len(vertices)
        dt=fmpz_mat([[int(v in m) for m in t] for v in vertices])
        det=int(dt.det())
        assert abs(det)==2
        dh=fmpq_mat([[int(v in m) for m in h] for v in vertices])
        aq=fmpq_mat(dt)
        coefficients=aq.solve(dh)
        assert aq*coefficients==dh
        scores=lambda m:sum(i*j for i,j in m)
        margins=[scores(h[j])-scores(t[i]) for i in range(len(t))
                 for j in range(len(h)) if coefficients[i,j]]
        assert margins and min(margins)>0
        forward={m for m in all_m if forward_label(n,m)['positive']}
        assert forward==set(h)
        inverse=set(candidates(n,n-4,2)[0])
        assert inverse==set(h)
        # The classifications in the three RSK cases are checked directly on
        # every four-element support, independently of incidence arithmetic.
        case_counts={'disjoint_failure':0,'crossing_failure':0,'nested_failure':0}
        for s1,s2,s3,s4 in combinations(range(1,n+1),4):
            checks=[(canonical((s1,s2),(s3,s4)),s2==2,'disjoint_failure'),
                    (canonical((s1,s3),(s2,s4)),s3==3,'crossing_failure'),
                    (canonical((s1,s4),(s2,s3)),s3==3 or s4<=5,'nested_failure')]
            for m,bad,label in checks:
                assert (m in t)==bad
                assert forward_label(n,m)['positive']==(not bad)
                case_counts[label]+=int(bad)
        entry=dict(n=n,edge_vertices=len(vertices),quadratic_monomials=len(all_m),
                   excluded_count=len(t),basis_count=len(h),incidence_determinant=det,
                   incidence_solve_verified=True,nonzero_coefficients=len(margins),
                   minimum_strict_margin=min(margins),
                   forward_inverse_and_symbolic_classifications_agree=True,
                   classification_counts=case_counts)
        results.append(entry)
        print(json.dumps(entry),flush=True)
        atomic_json(Path('evidence/quadratic-verification.json'),
                    dict(scope='n=6..14, finite supplement to the uniform proof',
                         arithmetic='exact ZZ determinants and QQ matrix identities',
                         complete=n==14,all_checks_passed=True,cases=results))


if __name__=='__main__':
    main()
