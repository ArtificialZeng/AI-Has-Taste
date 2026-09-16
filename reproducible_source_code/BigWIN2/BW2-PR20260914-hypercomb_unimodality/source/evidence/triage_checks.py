#!/usr/bin/env python3
"""Exact bounded validation; no assertion beyond the stated finite coverage."""
import json
from pathlib import Path


def add(a, b):
    out = [0] * max(len(a), len(b))
    for i, v in enumerate(a):
        out[i] += v
    for i, v in enumerate(b):
        out[i] += v
    return out


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            out[i+j] += u*v
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def initial(ell):
    return [1, ell], [1, 3*ell-2, 3*(ell-1)**2, (ell-1)**2*(ell-2)]


def sequence(ell, upper):
    a = [1, 2*ell-3, (ell-1)*(ell-2)]
    b = [0, 1, ell-1]
    prev, curr = initial(ell)
    yield 0, prev
    yield 1, curr
    for n in range(2, upper+1):
        prev, curr = curr, add(mul(a, curr), mul(b, prev))
        yield n, curr


def modes(p):
    top = max(p)
    return [i for i, c in enumerate(p) if c == top]


def is_unimodal(p):
    falling = False
    for a, b in zip(p, p[1:]):
        if a > b:
            falling = True
        elif a < b and falling:
            return False
    return True


def direct(n, ell):
    # w_0,...,w_n are attachment vertices; each spine edge uses two.
    edges = []
    next_vertex = n+1
    for i in range(1, n+1):
        e = [i-1, i] + list(range(next_vertex, next_vertex+ell-2))
        edges.append(sum(1 << v for v in e))
        next_vertex += ell-2
    for i in range(n+1):
        e = [i] + list(range(next_vertex, next_vertex+ell-1))
        edges.append(sum(1 << v for v in e))
        next_vertex += ell-1
    out = [0]*(2*n+2)
    for s in range(1 << next_vertex):
        if all((s & e).bit_count() <= 1 for e in edges):
            out[s.bit_count()] += 1
    return next_vertex, out


def main():
    result = {'arithmetic': 'Python arbitrary-precision integers',
              'job_id': 'primary-20260914-hypercomb-unimodality-triage-6a3e653c04b5',
              'direct_enumeration': [], 'grids': [],
              'nonunimodal': [], 'nonlogconcave': [],
              'summand_identity_failures': [], 'mode_gap_max': -1}
    cases = [(n, 3) for n in range(1, 5)] + [(n, 4) for n in range(1, 3)] + [(1, 5)]
    for n, ell in cases:
        vertices, count = direct(n, ell)
        recurrence = dict(sequence(ell, n))[n]
        assert count == recurrence
        result['direct_enumeration'].append({'n': n, 'ell': ell, 'vertices': vertices,
                                             'subsets_checked': 1 << vertices,
                                             'coefficients': count, 'match': True})
    # Deliberately modest grid, plus checks outside the authors' quoted range.
    grid = {ell: 120 for ell in range(3, 41)}
    grid.update({3: 520, 4: 520, 12: 520, 13: 520, 50: 160, 100: 160, 1000: 80})
    count = 0
    for ell, upper in sorted(grid.items()):
        result['grids'].append({'ell': ell, 'n_min': 1, 'n_max': upper})
        z0, z1 = initial(ell)
        a = [1, 2*ell-3, (ell-1)*(ell-2)]
        b = [0, 1, ell-1]
        # F_0=0, F_1=1, F_n=a F_(n-1)+b F_(n-2).
        fm2, fm1 = [0], [1]
        for n, p in sequence(ell, upper):
            if n == 0:
                continue
            count += 1
            if not is_unimodal(p):
                result['nonunimodal'].append({'n': n, 'ell': ell})
            bad = [k for k in range(1, len(p)-1) if p[k]**2 < p[k-1]*p[k+1]]
            if bad:
                result['nonlogconcave'].append({'n': n, 'ell': ell, 'indices': bad})
            if n < 2:
                continue
            f = add(mul(a, fm1), mul(b, fm2))
            w = mul(z1, f)
            y = mul(mul(z0, b), fm1)
            assert p == add(w, y)
            wm, ym = modes(w), modes(y)
            gap = min(abs(i-j) for i in wm for j in ym)
            if gap > result['mode_gap_max']:
                result['mode_gap_max'] = gap
                result['mode_gap_witness'] = {'n': n, 'ell': ell, 'W_modes': wm,
                                              'Y_modes': ym, 'C_modes': modes(p)}
            if gap >= 2 and 'first_nonadjacent_modes' not in result:
                result['first_nonadjacent_modes'] = {'n': n, 'ell': ell, 'W': w,
                                                     'Y': y, 'C': p, 'W_modes': wm,
                                                     'Y_modes': ym, 'gap': gap}
            fm2, fm1 = fm1, f
    result['total_polynomials_checked'] = count
    result['limitations'] = 'Finite validation only; positive checks do not prove unimodality, log-concavity, or a uniform mode-gap bound.'
    Path(__file__).with_name('triage-checks.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: v for k, v in result.items() if k not in ['grids', 'direct_enumeration', 'first_nonadjacent_modes']}, indent=2))
    first = result.get('first_nonadjacent_modes')
    if first:
        print('FIRST NONADJACENT', json.dumps({k: v for k, v in first.items() if k not in ['W','Y','C']}))


if __name__ == '__main__':
    main()
