"""Exact excess-two census and first-letter bridge test. Standard library only.

Enumeration contains one RGS per equivalence class, pruned only by the necessary
multiplicity bounds 2 <= count <= 4. Profile totals are checked independently
by the standard unlabeled-block multinomial formula. No random sampling.
"""
import sys
sys.dont_write_bytecode = True
import argparse
import json
from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
from itertools import combinations, groupby
from math import factorial
from pathlib import Path
from time import monotonic

HERE = Path(__file__).resolve().parent


def phi(w):
    stack, out, counts = [], [], Counter()
    for x in w:
        while counts[x] and stack[-1] != x:
            y = stack.pop()
            counts[y] -= 1
            out.append(y)
        stack.append(x)
        counts[x] += 1
    return tuple(out + stack[::-1])


def recursive(w):
    if not w:
        return ()
    x = w[0]
    pieces, segment, m = [], [], 0
    for y in w:
        if y == x:
            pieces.extend(recursive(segment))
            segment = []
            m += 1
        else:
            segment.append(y)
    pieces.extend(recursive(segment))
    return tuple(pieces) + (x,) * m


def direct(w):
    stack, out = [], []
    for x in w:
        while True:
            s = stack + [x]
            if not any(s[i] == s[l] != s[j]
                       for i, j, l in combinations(range(len(s)), 3)):
                stack.append(x)
                break
            out.append(stack.pop())
    return tuple(out + stack[::-1])


def trunc(w):
    return tuple(x for x, _ in groupby(w))


def canon(w):
    d = {}
    return tuple(d.setdefault(x, len(d)) for x in w)


def sorted_word(w):
    t = trunc(w)
    return len(t) == len(set(t))


def rgs_profiles(n, k):
    counts = [0] * k
    prefix = []

    def visit(used):
        left = n - len(prefix)
        needed = sum(max(0, 2-counts[x]) for x in range(k))
        if needed > left:
            return
        if not left:
            yield tuple(prefix)
            return
        for x in range(min(used+1, k)):
            if counts[x] == 4:
                continue
            prefix.append(x)
            counts[x] += 1
            yield from visit(max(used, x+1))
            counts[x] -= 1
            prefix.pop()
    yield from visit(0)


def orbit(w, passes):
    result = [tuple(w)]
    for _ in range(passes):
        a = phi(result[-1])
        assert a == recursive(result[-1]) == direct(result[-1])
        result.append(a)
    return result


def atomic_json(path, data):
    tmp = path.with_suffix('.json.tmp')
    tmp.write_text(json.dumps(data, indent=2) + '\n')
    tmp.replace(path)


def census(k):
    start = monotonic()
    n = 2*k+2
    total, by_profile, hits = 0, Counter(), []
    histogram, core_lengths, failures = Counter(), Counter(), []
    for w in rgs_profiles(n, k):
        total += 1
        profile = tuple(sorted(Counter(w).values(), reverse=True))
        by_profile[str(profile)] += 1
        a = w
        for _ in range(k-1):
            b = phi(a)
            assert b == recursive(a), w
            a = b
            if sorted_word(a):
                break
        if sorted_word(a):
            continue
        wo = orbit(w, k)
        assert sorted_word(wo[k]) and not sorted_word(wo[k-1])
        m = w.count(0)
        assert wo[1][-m:] == (0,)*m
        q = trunc(wo[1][:-m])
        qo = orbit(q, k-1)
        bridge = not sorted_word(qo[k-2])
        core_lengths[len(trunc(w))] += 1
        histogram[f'm={m},q_excess={len(q)-2*(k-1)}'] += 1
        item = dict(w=w, first_multiplicity=m, q=q, bridge=bridge)
        hits.append(item)
        if not bridge:
            failures.append(dict(**item, w_orbit=wo, q_orbit=qo))
    expected_four = factorial(n)//(factorial(4)*2**(k-1)*factorial(k-1))
    expected_triples = factorial(n)//(factorial(3)**2*2**(k-2)*2*factorial(k-2))
    assert by_profile[str((4,)+(2,)*(k-1))] == expected_four
    assert by_profile[str((3,3)+(2,)*(k-2))] == expected_triples
    result = dict(job_id='newwin-00001-p05-research-0171927ebd6e',
        recorded_at_utc=datetime.now(timezone.utc).isoformat(),
        status='exact finite observation, no all-k conclusion', k=k, n=n,
        coverage='all RGS with exactly k letters and every multiplicity >= 2',
        total=total, profile_totals=dict(by_profile),
        expected_profile_totals=dict(four=expected_four, two_triples=expected_triples),
        witnesses=len(hits), core_lengths=dict(core_lengths),
        reduction_histogram=dict(histogram), bridge_failures=failures, hits=hits,
        algorithms='run-stack and first-letter recursion on every visited iterate; full-triple check on all target and reduced orbits',
        source_sha256=sha256((HERE.parent/'source.md').read_bytes()).hexdigest(),
        script_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
        elapsed_seconds=monotonic()-start)
    path = HERE/f'research-census-k{k}.json'
    atomic_json(path, result)
    print(json.dumps({a:b for a,b in result.items() if a not in ('hits','bridge_failures')}, indent=2), flush=True)
    print('bridge_failures:', len(failures), flush=True)
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('k', type=int, nargs='+')
    args = parser.parse_args()
    for k in args.k:
        census(k)
