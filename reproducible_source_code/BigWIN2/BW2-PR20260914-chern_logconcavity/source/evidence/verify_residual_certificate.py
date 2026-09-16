#!/usr/bin/env python3
"""Verify the residual certificate without SymPy or the generator's code.

Each expansion coefficient has total degree <=4 in k,r, hence each
quadratic prefix has degree <=8. Exact comparison on a 9-by-9 tensor grid
proves the polynomial identities, not merely a finite family of inequalities.
The reported coefficients themselves must be nonnegative.
"""
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent


@lru_cache(None)
def reduce_n(n, depth):
    if depth == 0:
        return {n: 1}
    out = defaultdict(int)
    for step in (1, 2):
        for q, c in reduce_n(n - step, depth - 1).items():
            out[q] += (n - 1) * c
    return dict(out)


@lru_cache(None)
def newton_times(factors, index, depth):
    # Formal reduction is used even for negative indices. This produces
    # the same polynomial coefficients; no support truncation is allowed.
    out = defaultdict(int)
    if not factors:
        for n in (index, index + 1):
            for q, c in reduce_n(n, depth).items():
                out[q] += c
    else:
        for q, c in newton_times(factors[:-1], index, depth).items():
            out[q] += (index + factors[-1]) * c
        for q, c in newton_times(factors[:-1], index - 1, depth).items():
            out[q] += index * c
    return dict(out)


@lru_cache(None)
def twice_R(k, r):
    # Substitute A_{n,1}=x(x+2-n)S_{n-1}-(n+1)S_n directly
    # into the four lower-mode terms of equation (5.2).
    out = defaultdict(int)
    components = (
        (2, (2-k, 0, 3-k), 1),
        (-2*k, (2-k,), 2),
        (1, (3-k, 2-k), 1),
        (2, (1, 3-k, 0, 4-k), 0),
        (-2*(k-1), (1, 3-k), 1),
        (1, (1, 4-k, 3-k), 0),
    )
    for weight, factors, depth in components:
        for n, c in newton_times(factors, r, depth).items():
            out[n-r] += weight * c
    assert all(-5 <= i <= 1 or c == 0 for i, c in out.items())
    return dict(out)


@lru_cache(None)
def four_minor_coefficients(k, r):
    out = defaultdict(int)
    for a, x in twice_R(k, r).items():
        for b, y in twice_R(k, r).items():
            out[tuple(sorted((a, b)))] += x*y
    for a, x in twice_R(k, r-1).items():
        for b, y in twice_R(k, r+1).items():
            out[tuple(sorted((a-1, b+1)))] -= x*y
    return dict(out)


@lru_cache(None)
def D(n, h):
    if n == h == 0:
        return 1
    if h <= 0 or n < h+1 or n > 2*h:
        return 0
    return (n-1)*(D(n-1, h-1)+D(n-2, h-1))


def multiply_row(row, constant):
    return [(i+constant)*(row[i] if i < len(row) else 0)
            + i*(row[i-1] if 0 < i <= len(row) else 0)
            for i in range(len(row)+1)]


def make_term(row, factors, weight=1):
    for constant in factors:
        row = multiply_row(row, constant)
    return [weight*c for c in row]


def main():
    certificate = json.loads((ROOT/'j2-residual-symbolic.json').read_text())
    entries = certificate['prefixes']
    expected_pairs = {tuple(sorted((a,b))) for a in range(-5,2) for b in range(-5,2)}
    expected_pairs |= {tuple(sorted((a-1,b+1))) for a in range(-5,2) for b in range(-5,2)}
    assert {tuple(p['pair']) for p in entries} == expected_pairs
    assert len(entries) == len(expected_pairs) == 41
    trace_pairs = defaultdict(list)
    for pair in expected_pairs:
        trace_pairs[sum(pair)].append(pair)
    for pairs in trace_pairs.values():
        pairs.sort(key=lambda pair: pair[1]-pair[0])
    identity_checks = positive_coeffs = zero_polynomials = 0
    for entry in entries:
        a,b = entry['pair']
        trace = entry['trace']
        assert trace == a+b
        terms = {tuple(t['monomial']): Fraction(t['coefficient']) for t in entry['terms']}
        assert len(terms) == len(entry['terms'])
        assert all(u >= 0 and v >= 0 and u+v <= 8 and c >= 0 for (u,v),c in terms.items())
        positive_coeffs += sum(c > 0 for c in terms.values())
        zero_polynomials += not any(terms.values())
        pairs = trace_pairs[trace]
        prefix_pairs = pairs[:pairs.index((a,b))+1]
        for x in range(9):
            for y in range(9):
                kk = x+y+b-a+4
                rr = 2*x+y+b-2*a+2
                q = four_minor_coefficients(kk,rr)
                actual = Fraction(sum(q.get(pair,0) for pair in prefix_pairs),4)
                claimed = sum(c*x**u*y**v for (u,v),c in terms.items())
                assert actual == claimed, (entry['pair'],x,y,actual,claimed)
                identity_checks += 1
    rows = {(row['k'],row['j']): row['B'] for row in json.loads((ROOT/'exact-coefficients.json').read_text())}
    value_checks = minors = 0
    for k in range(4,33):
        tt = [make_term(rows[k-1,1], [2-k]),
              make_term(rows[k-2,0], [3-k,2-k], Fraction(1,2)),
              make_term(rows[k-2,1], [1,3-k]),
              make_term(rows[k-3,0], [1,4-k,3-k], Fraction(1,2))]
        bs = [sum(t[r] if r < len(t) else 0 for t in tt) for r in range(2*k+1)]
        for r,b in enumerate(bs):
            assert sum(c*D(r+i,k-3) for i,c in twice_R(k,r).items()) == 2*b
            assert (b > 0) == (k-2 <= r <= 2*k-1)
            value_checks += 1
            left = bs[r-1] if r else 0
            right = bs[r+1] if r+1 < len(bs) else 0
            minor = b*b-left*right
            q = four_minor_coefficients(k,r)
            assert sum(c*D(r+a,k-3)*D(r+b,k-3) for (a,b),c in q.items()) == 4*minor
            assert minor >= 0
            minors += 1
    report = {'kind': 'exact independent implementation verification; same research context, not referee acceptance',
              'certificate_prefixes': len(entries),
              'degree_bound': 'p_i total degree <=4, W total degree <=8; separately degree <=8 in X,Y',
              'tensor_grid': '0<=X,Y<=8, 81 points for each polynomial',
              'exact_identity_comparisons': identity_checks,
              'strictly_positive_serialized_coefficients': positive_coeffs,
              'zero_prefix_polynomials': zero_polynomials,
              'negative_serialized_coefficients': 0,
              'product_data_residual_value_comparisons': value_checks,
              'residual_minor_value_comparisons': minors,
              'finite_crosscheck_scope': '4<=k<=32, every 0<=r<=2k',
              'certificate_sha256': hashlib.sha256((ROOT/'j2-residual-symbolic.json').read_bytes()).hexdigest()}
    (ROOT/'residual-certificate-verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__ == '__main__':
    main()
