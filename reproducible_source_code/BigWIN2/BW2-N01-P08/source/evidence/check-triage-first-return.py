#!/usr/bin/env python3
"""Exact bounded tests of the newly derived Fuss coefficient identity.

Run from PROJECT_DIR:
  python3 evidence/check-triage-first-return.py
Only writes evidence/triage-first-return-check.json, atomically.
No floating arithmetic, random sampling, workers, or all-parameter claims.
"""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from importlib.util import spec_from_file_location, module_from_spec
from math import comb
from pathlib import Path
import json
import platform
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
spec = spec_from_file_location('intake', ROOT/'evidence/check-p08-small.py')
intake = module_from_spec(spec)
spec.loader.exec_module(intake)


def formula(m, n, k):
    result = [0]
    for j in range(1, k+1):
        c = Fraction(comb(n, k)*comb(k, j)*comb(m*n-k, j-1), n)
        assert c.denominator == 1
        result.append(c.numerator)
    return result


def words(m, n):
    def visit(word, east, north):
        if (east, north) == (n, m*n):
            yield word
            return
        if north < m*n:
            yield from visit(word+'N', east, north+1)
        if east < n and north >= m*(east+1):
            yield from visit(word+'E', east+1, north)
    yield from visit('', 0, 0)


def stats(word):
    return (sum(word[i:i+2] == 'NE' for i in range(len(word)-1)),
            sum(word[i:i+3] == 'NNE' for i in range(len(word)-2)))


def valid(word, m):
    height = 0
    for step in word:
        height += 1 if step == 'N' else -m
        if height < 0:
            return False
    return height == 0


def split_first_return(word, m):
    height = 0
    departures = {}
    for root, step in enumerate(word):
        if step == 'N' and height < m:
            departures[height] = root
        height += 1 if step == 'N' else -m
        if height == 0:
            break
    assert word[root] == 'E'
    ns = [departures[i] for i in range(m)]
    assert ns == sorted(ns)
    ends = ns[1:] + [root]
    parts = [word[start+1:end] for start, end in zip(ns, ends)]
    parts.append(word[root+1:])
    assert all(valid(part, m) for part in parts)
    assert ''.join('N'+part for part in parts[:m])+'E'+parts[m] == word
    return parts


def main():
    saved = json.loads((ROOT/'evidence/p08-intake-check.json').read_text())
    saved_rows = {(r['m'],r['n'],r['k']):r['coefficients_ascending']
                  for r in saved['rows']}
    rows = []
    for m in range(2, 5):
        for n in range(1, 9):
            counted = intake.counts(m, n)
            for k in range(1, n+1):
                predicted = formula(m,n,k)
                assert predicted == [counted[k][j] for j in range(k+1)]
                assert predicted == saved_rows[m,n,k]
                ratio = Fraction(comb(n-1,k-1), comb(m*n+1,k-1))
                ordinary = [Fraction(0)] + [
                    Fraction(comb(m*n+1,k-1)*comb(m*n-k,j-1)*comb(k,j), k)
                    for j in range(1,k+1)]
                assert [ratio*c for c in ordinary] == predicted
                rows.append(dict(m=m,n=n,k=k,coefficients_ascending=predicted,
                                 ordinary_size=m*n+1,ordinary_scalar=str(ratio)))

    boundary_cases = Counter()
    word_counts = []
    for m in range(2,5):
        for n in range(1,5):
            total = 0
            for word in words(m,n):
                total += 1
                parts = split_first_return(word,m)
                extra_k = int(parts[m-1] == '')
                extra_j = int(parts[m-1] == '' and parts[m-2] == '')
                internal = [stats(part) for part in parts]
                assert stats(word) == (sum(x[0] for x in internal)+extra_k,
                                       sum(x[1] for x in internal)+extra_j)
                boundary_cases[f'extra_peaks={extra_k},extra_nne={extra_j}'] += 1
            assert total == comb((m+1)*n,n)//(m*n+1)
            word_counts.append(dict(m=m,n=n,words=total))

    result = dict(job_id='newwin-00001-p08-triage-3c7429bdb0aa',
        python=platform.python_version(),domain='exact integers and rationals',
        source_sha256=sha256((ROOT/'source.md').read_bytes()).hexdigest(),
        handoff_files=[str(p.relative_to(ROOT)) for p in (ROOT/'literature').glob('*handoff*.md')],
        formula_scope={'m':[2,4],'n':[1,8],'k':'all 1..n'},
        tested_polynomials=len(rows),fresh_dynamic_programming_match=True,
        saved_table_match=True,ordinary_scalar_identity_match=True,
        decomposition_scope={'m':[2,4],'n':[1,4],'coverage':'all admissible words'},
        decomposition_words=sum(r['words'] for r in word_counts),
        decomposition_case_counts=dict(boundary_cases),word_counts=word_counts,
        failures=[],rows=rows,
        conclusion='Finite exact corroboration of a derivation; not independent proof acceptance.')
    target = ROOT/'evidence/triage-first-return-check.json'
    temporary = target.with_suffix('.json.tmp')
    temporary.write_text(json.dumps(result,indent=2)+'\n')
    temporary.replace(target)
    print(json.dumps({k:result[k] for k in ['tested_polynomials',
        'fresh_dynamic_programming_match','saved_table_match',
        'ordinary_scalar_identity_match','decomposition_words',
        'decomposition_case_counts','failures']}))


if __name__ == '__main__':
    main()
