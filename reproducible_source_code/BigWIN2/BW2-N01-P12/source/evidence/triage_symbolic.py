"""Exact finite evaluation of the cited permutation sum, not a fresh proof audit.

Koprowski--Lewis arXiv:2602.22129v1, Definitions 4.12, 4.16,
4.23 and Section 5.1. Zero-based indices in code.
Run from the project root: python3 evidence/triage_symbolic.py
"""
from itertools import product, permutations
from collections import Counter
from pathlib import Path
import json


def inv(w):
    return [(i, j) for i in range(len(w)) for j in range(i+1, len(w))
            if w[i] > w[j]]


def shapes():
    lam = [x for x in product(range(4), range(3), range(2))
           if x[0] >= x[1] >= x[2]]
    mus = [x for x in product(range(3), range(2), range(1))
           if x[0] >= x[1] >= x[2]]
    return [(a, b) for a in lam for b in mus
            if all(y <= x for x, y in zip(a, b))]


def generic_support(sigma, pi):
    # SE sigma-augmented L, NW pi-augmented R, with separate variables.
    # Each nonzero entry of these factors is either 1 or a distinct variable.
    # Nonempty products in L E_a R have distinct monomials, hence cannot
    # cancel in any characteristic; Boolean multiplication detects support.
    L = [[False]*4 for _ in range(4)]
    R = [[False]*3 for _ in range(3)]
    for i in range(4):
        L[sigma[i]][i] = True
    for i, j in inv(sigma):
        L[sigma[i]][j] = True
    for i in range(3):
        R[pi[i]][i] = True
    for i, j in inv(pi):
        R[pi[j]][i] = True
    return [[[any(L[r][t+a] and R[t][c] for t in range(3))
              for c in range(3)] for r in range(4)] for a in range(2)]


def coefficients(lengths):
    result = [1]
    for n in lengths:
        nxt = [0]*(len(result)+n-1)
        for i, v in enumerate(result):
            for j in range(n):
                nxt[i+j] += v
        result = nxt
    return result


def main():
    pairs = [(s, p, generic_support(s, p), len(inv(s))+len(inv(p)))
             for s in permutations(range(4)) for p in permutations(range(3))]
    results = []
    for lam, mu in shapes():
        exponents = Counter()
        terms = []
        for s, p, supp, nvars in pairs:
            if any(s[p[j]] >= 4-lam[j] or s[p[j]+1] >= 4-mu[j]
                   for j in range(3)):
                continue
            h = sum(supp[a][i][j] for a, shape in enumerate((lam, mu))
                    for j in range(3) for i in range(4-shape[j], 4))
            d = nvars-h
            assert d >= 0, (lam, mu, s, p, h, nvars)
            exponents[d] += 1
            terms.append({'sigma': [v+1 for v in s], 'pi': [v+1 for v in p],
                          'inversions': nvars, 'h': h, 'exponent': d})
        actual = [exponents[i] for i in range(max(exponents)+1)]
        expected = coefficients([4-j-lam[j] for j in range(3)] +
                                [3-j-mu[j] for j in range(3)])
        results.append({'lambda': lam, 'mu': mu, 'coefficients': actual,
                        'expected_coefficients': expected,
                        'equal': actual == expected, 'terms': terms})
    report = {'job_id': 'newwin-00001-p12-triage-3ebebbace8a4',
              'type': 'exact finite symbolic observation; theorem transfer unaudited',
              'shape_count': len(results), 'permutation_pairs_per_shape': len(pairs),
              'mu_zero_count': sum(not any(r['mu']) for r in results),
              'other_than_mu_zero_or_maximal': sum(any(r['mu']) and
                  (r['lambda'], r['mu']) != ((3,2,1), (2,1,0)) for r in results),
              'all_equal': all(r['equal'] for r in results), 'results': results}
    out = Path(__file__).with_name('triage_symbolic.json')
    out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k != 'results'}, indent=2))
    for r in results:
        if not r['equal']:
            print('MISMATCH', r['lambda'], r['mu'], r['coefficients'],
                  r['expected_coefficients'])


if __name__ == '__main__':
    main()
