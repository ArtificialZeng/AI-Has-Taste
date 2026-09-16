"""Mechanism-derived bit-stack language versus deterministic input sorting.

Run from project root: python3 evidence/first_return_exact.py
All generation is exact; no pattern basis or fitted coefficients are used.
"""
from collections import Counter
from itertools import permutations
from pathlib import Path
import hashlib
import json
import math

ROOT = Path(__file__).resolve().parents[1]
JOB = 'primary-20260912-stack22-mechanism-research-897e72adb69b'


def canonical(pi):
    stack, word = [], []
    i, want = 0, 1
    while True:
        if want in stack[:2]:
            j = stack.index(want)
            stack.pop(j)
            word.append('Q' + str(j+1))
            want += 1
        elif i < len(pi):
            j = int(bool(stack) and pi[i] > stack[0])
            stack.insert(j, pi[i])
            word.append('P' + str(j+1))
            i += 1
        else:
            return tuple(word) if not stack else None


def bit_words(n):
    """Generate rank words with independent 0/1 comparison obligations."""
    def visit(stack, pushes, word):
        if pushes == n and not stack:
            yield word
            return
        if pushes < n:
            yield from visit((int(bool(stack)),) + stack, pushes+1, word+('P1',))
            if stack:
                yield from visit((1, 0) + stack[1:], pushes+1, word+('P2',))
        if stack and word[-1] != 'P2':
            yield from visit(stack[1:], pushes, word+('Q1',))
        if len(stack) >= 2 and stack[0] == 0:
            yield from visit(stack[:1] + stack[2:], pushes, word+('Q2',))
    yield from visit((), 0, ())


def reconstruct(word):
    stack, labels = [], []
    want = 1
    for op in word:
        j = int(op[1])-1
        if op[0] == 'P':
            token = len(labels)
            labels.append(None)
            stack.insert(j, token)
        else:
            labels[stack.pop(j)] = want
            want += 1
    assert not stack and None not in labels
    return tuple(labels)


def save(data):
    dst = ROOT/'evidence/first_return_exact.json'
    tmp = dst.with_suffix('.tmp')
    tmp.write_text(json.dumps(data, indent=2)+'\n')
    tmp.replace(dst)


def main():
    data = dict(job_id=JOB, source_sha256=hashlib.sha256((ROOT/'source.md').read_bytes()).hexdigest(),
                arithmetic='exact integers; exhaustive permutations and complete bit-language generation', rows=[])
    for n in range(9):
        expected = {}
        for pi in permutations(range(1, n+1)):
            w = canonical(pi)
            if w is not None:
                assert w not in expected
                expected[w] = pi
        actual = Counter(bit_words(n))
        missing = set(expected) - set(actual)
        extra = set(actual) - set(expected)
        duplicates = sum(v-1 for v in actual.values())
        wrong_reconstructions = sum(reconstruct(w) != expected.get(w) for w in actual)
        row = dict(n=n, inputs=math.factorial(n), canonical=len(expected), generated=sum(actual.values()),
                   missing=len(missing), extra=len(extra), duplicate_derivations=duplicates,
                   wrong_reconstructions=wrong_reconstructions,
                   trace_set_sha256=hashlib.sha256('\n'.join(' '.join(w) for w in sorted(actual)).encode()).hexdigest())
        data['rows'].append(row)
        if missing or extra:
            data['first_failure'] = dict(missing=min(missing) if missing else None, extra=min(extra) if extra else None)
        save(data)
        print(json.dumps(row), flush=True)
        assert not (missing or extra or duplicates or wrong_reconstructions)


if __name__ == '__main__':
    main()
