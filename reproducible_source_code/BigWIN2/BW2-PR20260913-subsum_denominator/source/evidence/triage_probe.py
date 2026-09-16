"""Bounded exact triage tests; Python standard library only.

Run from project root: python3 evidence/triage_probe.py
No floating point arithmetic and no sampled coefficient indices.
"""
import hashlib
import json
import argparse
from fractions import Fraction
from pathlib import Path


def factor(a, s):
    b = a + [0] * s
    for j, v in enumerate(a):
        b[j + s] += v
    return b


def at(a, j):
    return a[j] if 0 <= j < len(a) else 0


def delta(a, j):
    return at(a, j)**2 - at(a, j - 1)*at(a, j + 1)


def witness(a, j):
    return dict(j=j, triple=[at(a, j-1), at(a, j), at(a, j+1)],
                minor=delta(a, j))


def direct(n):
    a = [1]
    for i in range(1, n+1):
        for _ in range((n // i).bit_length()):
            a = factor(a, i)
    return a


def shifts(n):
    return sorted(n >> k for k in range((n & -n).bit_length()))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-n', type=int, default=256)
    args = parser.parse_args()
    failures, stage_failures, cross_failures = [], [], []
    half_bound_failures = []
    least = None
    half_bound_count = 0
    summaries = []
    a = [1]
    checked_minors = 0
    stage_count = 0
    for n in range(1, args.max_n+1):
        for s in shifts(n):
            old = a
            a = factor(old, s)
            if n >= 9:
                stage_count += 1
                bad = next((j for j in range(1, len(a)-1) if delta(a,j)<0), None)
                if bad is not None:
                    stage_failures.append(dict(n=n, shift=s, **witness(a,bad)))
                for j in range(len(a)):
                    base = delta(old,j) + delta(old,j-s)
                    new = delta(a,j)
                    half_bound_count += 1
                    if 2*new < base:
                        half_bound_failures.append(dict(n=n,shift=s,j=j,
                            new_minor=new,sum_old_minors=base))
                    if base > 0 and (least is None or new*least['sum_old_minors'] < least['new_minor']*base):
                        least = dict(n=n,shift=s,j=j,new_minor=new,sum_old_minors=base)
                # Test the stronger termwise nonnegative cross-term shortcut.
                # Delta(new,j)=Delta(old,j)+Delta(old,j-s)+cross(old,j,s).
                if not cross_failures:
                    for j in range(1, len(a)-1):
                        c = (2*at(old,j)*at(old,j-s)
                             - at(old,j-1)*at(old,j+1-s)
                             - at(old,j+1)*at(old,j-1-s))
                        assert delta(a,j) == delta(old,j)+delta(old,j-s)+c
                        if c < 0:
                            cross_failures.append(dict(n=n, shift=s, j=j,
                                cross=c, old_coefficients=old,
                                old_minor=delta(old,j),
                                shifted_minor=delta(old,j-s), new_minor=delta(a,j)))
                            break
        if n <= 24:
            assert a == direct(n), ("recurrence mismatch",n)
        assert a == a[::-1]
        assert len(a)-1 == sum(i*(n//i).bit_length() for i in range(1,n+1))
        assert sum(a) == 2**sum((n//i).bit_length() for i in range(1,n+1))
        bad = [j for j in range(1,len(a)-1) if delta(a,j)<0]
        checked_minors += len(a)-2
        if bad:
            failures.append(dict(n=n, degree=len(a)-1,
                                 witnesses=[witness(a,j) for j in bad]))
        summaries.append(dict(n=n,degree=len(a)-1,negative_count=len(bad),
                              coefficients_sha256=hashlib.sha256(
                                  json.dumps(a,separators=(',',':')).encode()).hexdigest()))
    output = dict(job_id="primary-20260913-subsum-denominator-triage-e72bbaa7a9ab",
                  exact_range=[1,args.max_n], direct_product_crosscheck=[1,min(24,args.max_n)],
                  all_internal_minors_checked=checked_minors,
                  failures=failures, intermediate_stage_range=[9,args.max_n],
                  intermediate_stages_checked=stage_count,
                  intermediate_stage_failures=stage_failures,
                  half_bound_inequalities_checked=half_bound_count,
                  half_bound_failures=half_bound_failures,
                  minimum_stage_minor_ratio=least,
                  first_negative_cross_term=cross_failures,
                  rows=summaries)
    if least is not None:
        least['fraction'] = str(Fraction(least['new_minor'],least['sum_old_minors']))
    Path('evidence/triage_probe.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({k:v for k,v in output.items() if k!='rows'},indent=2))


if __name__ == '__main__':
    main()
