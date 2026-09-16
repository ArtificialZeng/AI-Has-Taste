"""Held-out n=9 objectwise test, after writing the full grammar/proof.

An additional independent attack traverses ALL legal rank words through n=6
and compares the bit test with direct reconstructed-value comparisons.
"""
from collections import Counter
from itertools import permutations
from pathlib import Path
import hashlib
import json

from first_return_exact import bit_words, canonical, reconstruct

ROOT = Path(__file__).resolve().parents[1]


def unrestricted(n):
    def visit(height, pushes, word):
        if pushes == n and height == 0:
            yield word
            return
        if pushes < n:
            for j in range(1, min(2, height+1)+1):
                yield from visit(height+1, pushes+1, word+('P'+str(j),))
        for j in range(1, min(2, height)+1):
            yield from visit(height-1, pushes, word+('Q'+str(j),))
    yield from visit(0, 0, ())


def direct_criteria(word):
    pi = reconstruct(word)
    stack = []
    i = 0
    for op in word:
        j = int(op[1])-1
        if op[0] == 'P':
            if stack and (pi[i] < stack[0]) != (j == 0):
                return False
            stack.insert(j, pi[i])
            i += 1
        else:
            stack.pop(j)
    return all(a == 'P1' and b == 'Q1' for a,b in zip(word,word[1:])
               if a[0] == 'P' and b[0] == 'Q')


def save(data):
    dst = ROOT/'evidence/first_return_holdout.json'
    tmp = dst.with_suffix('.tmp')
    tmp.write_text(json.dumps(data, indent=2)+'\n')
    tmp.replace(dst)


def main():
    data = dict(job_id='primary-20260912-stack22-mechanism-research-897e72adb69b',
                frozen_proof_sha256=hashlib.sha256((ROOT/'evidence/first_return_proof.md').read_bytes()).hexdigest(),
                frozen_grammar_sha256=hashlib.sha256((ROOT/'evidence/first_return_grammar.py').read_bytes()).hexdigest(),
                attack_rows=[])
    for n in range(7):
        accepted = set(bit_words(n))
        total = mismatches = comparisons_and_peaks = 0
        for w in unrestricted(n):
            total += 1
            direct = direct_criteria(w)
            comparisons_and_peaks += direct
            mismatches += direct != (w in accepted)
        row = dict(n=n, all_legal_words=total, direct_criteria_accepted=comparisons_and_peaks,
                   bit_accepted=len(accepted), mismatches=mismatches)
        data['attack_rows'].append(row)
        save(data)
        print(json.dumps(row), flush=True)
        assert mismatches == 0
    n = 9
    expected = {}
    for pi in permutations(range(1,n+1)):
        w = canonical(pi)
        if w is not None:
            assert w not in expected
            expected[w] = pi
    actual = Counter(bit_words(n))
    row = dict(n=n, inputs=362880, canonical=len(expected), bit_words=sum(actual.values()),
               missing=len(set(expected)-set(actual)), extra=len(set(actual)-set(expected)),
               duplicate_derivations=sum(v-1 for v in actual.values()),
               wrong_reconstructions=sum(reconstruct(w) != expected.get(w) for w in actual),
               trace_set_sha256=hashlib.sha256('\n'.join(' '.join(w) for w in sorted(actual)).encode()).hexdigest())
    data['heldout_n9'] = row
    save(data)
    print(json.dumps(row), flush=True)
    assert not any(row[k] for k in ['missing','extra','duplicate_derivations','wrong_reconstructions'])


if __name__ == '__main__':
    main()
