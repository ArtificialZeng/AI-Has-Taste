"""Bounded exact intake calibration; not a proof or a referee audit."""
import itertools
import json
import platform
import time
from collections import defaultdict
from functools import lru_cache
from pathlib import Path
import sympy as sp

start = time.monotonic()
x = sp.Symbol('x')

@lru_cache(None)
def real_roots(coeff):
    p = sp.Poly.from_list(list(reversed(coeff)), x, domain=sp.QQ)
    if p.is_zero or p.degree() <= 1:
        return True
    return sum(int(m) for _, m in p.intervals()) == p.degree()

def clean(v):
    while len(v) > 1 and v[-1] == 0:
        v.pop()
    return tuple(v)

levels = []
failures = []
examples = []
for n in range(1, 8):
    boards = cases = refinements = words = 0
    # k=3 includes zero content coordinates and all effective smaller alphabets.
    for lam in itertools.combinations_with_replacement(range(1, 4), n):
        boards += 1
        data = defaultdict(lambda: [[0] * n for _ in range(3)])
        for w in itertools.product(*(range(1, h+1) for h in lam)):
            alpha = tuple(w.count(i) for i in range(1, 4))
            asc = sum(a < b for a, b in zip(w, w[1:]))
            data[alpha][w[0]-1][asc] += 1
            words += 1
        for alpha, rows in data.items():
            cases += 1
            total = clean([sum(row[d] for row in rows) for d in range(n)])
            if not real_roots(total):
                failures.append(dict(kind='total', lam=lam, alpha=alpha, coeff=total))
            for j, row in enumerate(rows, 1):
                coeff = clean(row)
                if any(coeff):
                    refinements += 1
                    if not real_roots(coeff):
                        failures.append(dict(kind='refinement', lam=lam, alpha=alpha,
                                             j=j, coeff=coeff))
            if lam == (2,2,2,3,3) and alpha == (2,2,1):
                examples.append(dict(lam=lam,alpha=alpha,total=total,refined=rows))
    levels.append(dict(n=n,boards=boards,nonempty_board_content_cases=cases,
                       nonzero_refinements=refinements,words_enumerated=words))

result = dict(purpose='Intake calibration only; finite real-rootedness, not all-parameter proof.',
              algorithm='Enumerate each legal word once for each nondecreasing board; group by exact content and first letter; SymPy rational real-root isolation with multiplicities.',
              domain='1<=n<=7; every nondecreasing lambda in {1,2,3}^n; every realized nonnegative length-3 content vector; mu=0.',
              excluded_checks='No interlacing verification or claim for n>7/k>3; zero polynomials skipped.',
              python=platform.python_version(),sympy=sp.__version__,randomness='none',
              levels=levels,failures=failures,examples=examples,
              distinct_polynomials=real_roots.cache_info().currsize,
              elapsed_seconds=time.monotonic()-start)
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
