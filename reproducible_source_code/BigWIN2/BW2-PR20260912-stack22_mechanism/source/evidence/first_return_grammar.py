"""Expand the first-return specification, keeping derivation multiplicities.

This generator uses recursive word products, not the bit-stack traversal.
Run: python3 evidence/first_return_grammar.py
"""
from collections import Counter
from pathlib import Path
import hashlib
import json

from first_return_exact import bit_words, canonical, reconstruct

ROOT = Path(__file__).resolve().parents[1]


def wrap(p, words, q):
    return Counter({(p,)+w+(q,): multiplicity for w, multiplicity in words.items()})


def product(left, right):
    out = Counter()
    for u, a in left.items():
        for v, b in right.items():
            out[u+v] += a*b
    return out


def grammar(max_n):
    A, B, C, F = ([Counter() for _ in range(max_n+1)] for _ in range(4))
    E, D = ([Counter() for _ in range(max_n+1)] for _ in range(2))
    A[0][()] = C[0][()] = F[0][()] = 1
    for n in range(1, max_n+1):
        inside = B[n-1] + C[n-1]
        E[n] = wrap('P1', inside, 'Q1')
        nonempty_C = C[n-1] if n > 1 else Counter()
        D[n] = (wrap('P1', B[n-1], 'Q2') + wrap('P2', B[n-1], 'Q1')
                + wrap('P2', nonempty_C, 'Q1') + wrap('P2', B[n-1], 'Q2'))
        for k in range(1, n+1):
            A[n] += product(E[k]+D[k], A[n-k])
            C[n] += product(E[k], C[n-k])
            B[n] += product(E[k], B[n-k]) + product(D[k], A[n-k])
            F[n] += product(wrap('P1', A[k-1], 'Q1'), F[n-k])
    return A, B, C, F


def run_bits(word, initial):
    """Verify a positive-floor word and its endpoint, independently of grammar."""
    s = [initial]
    prev = None
    for op in word:
        if op == 'P1':
            s.insert(0, 1)
        elif op == 'P2':
            s[0] = 1
            s.insert(1, 0)
        elif op == 'Q1':
            if len(s) < 2 or prev == 'P2':
                return None
            s.pop(0)
        else:
            if len(s) < 2 or s[0] != 0:
                return None
            s.pop(1)
        prev = op
    return s[0] if len(s) == 1 else None


def main():
    A, B, C, F = grammar(8)
    data = dict(job_id='primary-20260912-stack22-mechanism-research-897e72adb69b',
                scope='Full recursive grammar words for 0<=n<=8; multiplicities retained', rows=[])
    for n in range(9):
        actual = Counter(bit_words(n))
        missing = set(actual)-set(F[n])
        extra = set(F[n])-set(actual)
        duplicates = {label: sum(v-1 for v in words[n].values())
                      for label, words in [('A', A), ('B', B), ('C', C), ('F', F)]}
        bad_boundary = (sum(run_bits(w, 0) != 0 for w in A[n])
                        + sum(run_bits(w, 1) != 0 for w in B[n])
                        + sum(run_bits(w, 1) != 1 for w in C[n]))
        bad_canonical = sum(canonical(reconstruct(w)) != w for w in F[n])
        row = dict(n=n, A=len(A[n]), B=len(B[n]), C=len(C[n]), F=len(F[n]),
                   missing=len(missing), extra=len(extra), duplicate_derivations=duplicates,
                   bad_boundary=bad_boundary, bad_canonical=bad_canonical,
                   language_A_equals_disjoint_B_union_C=(A[n] == B[n]+C[n] and not (set(B[n]) & set(C[n]))),
                   language_F_equals_C=(F[n] == C[n]),
                   trace_set_sha256=hashlib.sha256('\n'.join(' '.join(w) for w in sorted(F[n])).encode()).hexdigest())
        data['rows'].append(row)
        dst = ROOT/'evidence/first_return_grammar.json'
        tmp = dst.with_suffix('.tmp')
        tmp.write_text(json.dumps(data, indent=2)+'\n')
        tmp.replace(dst)
        print(json.dumps(row), flush=True)
        assert not (missing or extra or any(duplicates.values()) or bad_boundary or bad_canonical)
        assert row['language_A_equals_disjoint_B_union_C'] and row['language_F_equals_C']


if __name__ == '__main__':
    main()
