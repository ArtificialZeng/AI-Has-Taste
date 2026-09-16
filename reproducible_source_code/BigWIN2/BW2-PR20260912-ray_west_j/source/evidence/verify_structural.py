"""Replay concrete insertion certificates without the active-pair search code."""
from itertools import combinations, permutations
from pathlib import Path
import json
from test_statistics import direct_g2, standardize

OUT = Path(__file__).resolve().parent
JOB = 'primary-20260912-ray-west-j-research-6795cc8901c9'


def insert(p, r, c, rho):
    """rho zero-based; r,c one-based original-grid multisets."""
    n = len(p)+2
    inserted_positions = (c[0]-1, c[1])
    inserted_values = (r[0], r[1]+1)
    keep_positions = [i for i in range(n) if i not in inserted_positions]
    keep_values = [v for v in range(1, n+1) if v not in inserted_values]
    ans = [0]*n
    for pos, v in zip(keep_positions, p):
        ans[pos] = keep_values[v-1]
    for i in (0, 1):
        ans[inserted_positions[i]] = inserted_values[rho[i]]
    assert sorted(ans) == list(range(1, n+1))
    return tuple(ans)


def active(p, r, c, rho):
    return all(not any(0 <= i < len(p) and p[i] == r[rho[t]]
                       for i in (c[t]-2, c[t]-1)) for t in (0, 1))


def main():
    grid = [(a,b) for a in range(1, 17) for b in range(1, 17)]
    grid += [(1,100), (100,1), (64,97), (97,64)]
    for a,b in grid:
        m = a+b
        p = tuple(range(a,0,-1))+tuple(range(m,a,-1))
        r,c,s,d = (1,a),(a+2,m+1),(a+2,m+1),(1,a)
        rho = (0,1)
        lhs, rhs = insert(p,r,c,rho), insert(p,s,d,rho)
        expected = ((a+2,)+tuple(range(a,1,-1))+(m+2,1)
                    +tuple(range(m+1,a+2,-1))+(a+1,))
        assert lhs == rhs == expected
        assert active(p,r,c,rho) and r[1] < s[0] and d[1] < c[0]
    assert insert((2,1),(1,1),(1,1),(1,0)) == (2,1,4,3)
    assert insert((2,1),(3,3),(3,3),(1,0)) == (2,1,4,3)
    data = json.loads((OUT/'gap-deletion-test.json').read_text())
    w = data['local_preservation_first_witnesses'][0]
    p,q = tuple(w['beta']),tuple(w['gamma'])
    i = w['deleted_position']-1
    assert standardize(p[:i]+p[i+1:]) == q
    certificate_checks = []
    for perm,key in ((p,'beta_configurations'),(q,'gamma_configurations')):
        for cert in w[key]:
            r,c,rho = cert['left'];s,d,sigma = cert['right']
            lhs,rhs = insert(perm,r,c,rho),insert(perm,s,d,sigma)
            assert lhs == rhs == tuple(cert['ambient'])
            assert active(perm,r,c,rho)
            assert r[1] < s[0] and (c[1] < d[0] or d[1] < c[0])
        g = direct_g2(perm)
        m = len(perm)
        j = (m**4+2*m**3+m*m+4*m+4)//2-g
        assert j == 1 == len(w[key])
        certificate_checks.append({'beta': perm,'g2':g,'j':j})
    original_gap = w['lost_gap']-1
    assert i not in (original_gap,original_gap+1)
    surviving_gap = original_gap-(i<original_gap)
    assert surviving_gap not in w['gamma_good_gaps']
    report = {'job_id': JOB,
              'two_decreasing_block_identities_checked': len(grid),
              'largest_identity_length': max(a+b for a,b in grid),
              'gap_preservation_witness_verified': certificate_checks,
              'surviving_gap_zero_based': surviving_gap,
              'status': 'Exact certificate replay. Finite identity checks corroborate the written all-parameter argument; they do not prove E or D.'}
    tmp=OUT/'structural-verification.json.tmp'
    tmp.write_text(json.dumps(report,indent=2)+'\n')
    tmp.replace(OUT/'structural-verification.json')
    print(json.dumps(report,indent=2))


if __name__ == '__main__':
    main()
