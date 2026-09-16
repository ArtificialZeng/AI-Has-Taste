"""Audit the fixed witness with position choices; Python standard library only.

Does not import either triage enumerator. Reads the old TSV without rewriting it.
All decisive checks use integer arithmetic. Run from any working directory.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations
from pathlib import Path
import csv
import hashlib
import json

PROJECT = Path(__file__).resolve().parents[1]
JOB = 'primary-20260913-multiset-rook-research-14de8ccf88cc'
LAM = (3, 3, 3, 3, 4, 4)
ALPHA = (2, 2, 1, 1)
SOURCE_SHA = '2a88f14a8f18991b1253ef13abad929e8b00f48326545c52911ef89a6707f18f'
HTML_SHA = 'af09cd6949d991dfc7467dfb19704f0a2cc6842d05e0317f3bdfb69d40854f8a'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def asc(w):
    return sum(a < b for a, b in zip(w, w[1:]))

def multiply(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out

def evaluate(coeff, t):
    result = 0
    for c in reversed(coeff):
        result = result*t + c
    return result

def run():
    assert sha(PROJECT/'source.md') == SOURCE_SHA
    assert sha(PROJECT/'evidence/external/ajq-2502.05939v1.html') == HTML_SHA
    assert len(LAM) == sum(ALPHA) == 6
    assert all(0 < a <= b for a, b in zip(LAM, LAM[1:]))
    assert all(a > 0 for a in ALPHA)
    assert len(set(LAM)) > 1 and max(ALPHA) > 1

    # Choose the unique 3, then the two 1s among the remaining four slots.
    # The other two slots are 2s: 5*binomial(4,2)=30 distinct bases.
    bases = []
    for three in range(5):
        for ones in combinations([p for p in range(5) if p != three], 2):
            base = tuple(3 if p == three else 1 if p in ones else 2
                         for p in range(5))
            bases.append(base)
    assert len(bases) == len(set(bases)) == 30
    words = {}
    split = defaultdict(Counter)
    base_lines = ['base\tfirst_letter\tasc_4_at_5\tasc_4_at_6']
    for base in sorted(bases):
        inserted = (base[:4] + (4,) + base[4:], base + (4,))
        base_lines.append(''.join(map(str, base))+'\t'+str(base[0])+'\t'+
                          '\t'.join(str(asc(w)) for w in inserted))
        for position, w in zip((5, 6), inserted):
            assert w not in words
            assert tuple(w.count(i) for i in range(1, 5)) == ALPHA
            assert all(1 <= a <= b for a, b in zip(w, LAM))
            words[w] = asc(w)
            split[w[0], position][asc(w)] += 1
    assert len(words) == 60

    # Independent, differently constructed domain check: 6! labeled orders,
    # erase labels on equal values, then filter the row restrictions.
    labeled_values = (1, 1, 2, 2, 3, 4)
    raw = (tuple(labeled_values[i] for i in order)
           for order in permutations(range(6)))
    direct = {w for w in raw if all(a <= b for a, b in zip(w, LAM))}
    assert direct == set(words)

    old_rows = list(csv.DictReader((PROJECT/'evidence/six-letter-words.tsv').open(),
                                  delimiter='\t'))
    old = {}
    for row in old_rows:
        w = tuple(map(int, row['word']))
        assert w not in old and int(row['first_letter']) == w[0]
        old[w] = int(row['ascents'])
    assert len(old_rows) == 60 and old == words

    coefficients = {j: [sum(a == d and w[0] == j for w, a in words.items())
                        for d in range(5)] for j in range(1, 4)}
    assert coefficients == {1:[0,0,7,15,2], 2:[0,1,15,8,0], 3:[0,3,8,1,0]}
    assert multiply([0,0,1], multiply([7,1], [1,2])) == coefficients[1]
    assert multiply([0,1], [3,8,1]) + [0] == coefficients[3]
    assert 13 > 3**2   # sqrt(13)>3, so -4-sqrt(13)<-7.
    assert 13 < 4**2   # Both nonzero roots of R3 are negative.
    assert 193 > 0 and 193 < 15**2  # R2 discriminant; both roots negative.

    total = [sum(coefficients[j][d] for j in range(1,4)) for d in range(5)]
    cubic = [2,15,12,1]
    assert multiply([0,2], cubic) == total
    values = {t:evaluate(cubic,t) for t in (-11,-10,-2,-1,0)}
    assert values == {-11:-42,-10:52,-2:12,-1:-2,0:2}
    # IVT on (-11,-10),(-2,-1),(-1,0) exhausts all roots of the cubic.
    assert all(values[a]*values[b] < 0 for a,b in [(-11,-10),(-2,-1),(-1,0)])

    # Source Example 26: strict adjacent ascents, no endpoint sentinel.
    example_words = [b for b in bases if all(x <= h for x,h in
                     zip(b,(2,2,2,3,3))) ]
    example_counts = Counter(map(asc, example_words))
    assert len(example_words) == 12 and example_counts == {1:3,2:8,3:1}

    result = {
      'job_id':JOB, 'status':'exact finite audit; no referee acceptance',
      'lambda':LAM, 'alpha':ALPHA,
      'methods':['30 bases by disjoint position choices, 2 legal insertions each',
                 '720 labeled permutations, deduplicated after erasing labels'],
      'legal_word_count':len(words), 'old_tsv_rows_checked':len(old_rows),
      'old_tsv_set_and_ascent_counts_match':True,
      'coefficients_ascending_with_padding':coefficients,
      'split_by_first_letter_and_position_of_4':
          {f'{j},{p}':dict(sorted(split[j,p].items()))
           for j in range(1,4) for p in (5,6)},
      'exact_root_obstruction':{'ordered_pair':['R3','R1'],
          'degrees':[3,4], 'R3_least_root':'-4-sqrt(13)',
          'R1_least_root':'-7', 'integer_certificate':'13>3^2'},
      'total_coefficients_ascending':total,
      'total_real_root_certificate':{'factor':'2*t*(t^3+12*t^2+15*t+2)',
          'cubic_integer_values':values,
          'cubic_disjoint_sign_change_intervals':[[-11,-10],[-2,-1],[-1,0]],
          'additional_simple_root':0},
      'source_example_26':{'legal_words':len(example_words),
                          'ascent_counts':dict(sorted(example_counts.items()))},
      'source_sha256':SOURCE_SHA, 'primary_html_sha256':HTML_SHA,
      'original_word_list_sha256':sha(PROJECT/'evidence/six-letter-words.tsv'),
      'scope':'Refutes the interlacing clause, hence the frozen conjunction. '
              'Does not decide universal real-rootedness of the total. '
              'No global minimality or priority assertion.'}
    out=PROJECT/'evidence'
    (out/'research-base-insertions.tsv').write_text('\n'.join(base_lines)+'\n')
    (out/'research-six-letter-audit.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    run()
