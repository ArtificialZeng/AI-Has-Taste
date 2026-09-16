"""Exact input enumeration; no pattern basis is used by the sorter.

Run: python3 evidence/triage_exact.py
Writes evidence/triage_exact.json atomically and prints progress.
"""
from functools import lru_cache
from itertools import permutations
from pathlib import Path
import hashlib
import json
import math

ROOT = Path(__file__).resolve().parents[1]


def trace_counter(pi, eager=False):
    n = len(pi)

    @lru_cache(None)
    def count(i, stack, want):
        if want == n + 1:
            return int(i == n and not stack)
        ways = 0
        for j in range(min(2, len(stack))):
            if stack[j] == want:
                ways += count(i, stack[:j] + stack[j+1:], want+1)
                if eager:
                    return ways
        if i < n:
            for j in range(min(2, len(stack)+1)):
                ways += count(i+1, stack[:j]+(pi[i],)+stack[j:], want)
        return ways

    return count(0, (), 1)


def small_on_top(pi):
    """Eager pop; otherwise insert new a at 1 iff empty or a<top, else 2."""
    stack = []
    want = 1
    i = 0
    log = []
    while True:
        legal = [j for j in range(min(2, len(stack))) if stack[j] == want]
        if legal:
            j = legal[0]
            log.append(["pop", j+1, stack.pop(j)])
            want += 1
        elif i < len(pi):
            a = pi[i]
            j = 0 if not stack or a < stack[0] else 1
            stack.insert(j, a)
            log.append(["push", j+1, a])
            i += 1
        else:
            return want == len(pi)+1, log, stack, want


def eager_witness(pi):
    @lru_cache(None)
    def visit(i, stack, want):
        if want == len(pi)+1:
            return ()
        for j in range(min(2, len(stack))):
            if stack[j] == want:
                rest = visit(i, stack[:j]+stack[j+1:], want+1)
                return None if rest is None else (("pop", j+1, want),)+rest
        if i < len(pi):
            for j in range(min(2, len(stack)+1)):
                rest = visit(i+1, stack[:j]+(pi[i],)+stack[j:], want)
                if rest is not None:
                    return (("push", j+1, pi[i]),)+rest
        return None
    return visit(0, (), 1)


def save(data):
    target = ROOT / 'evidence/triage_exact.json'
    tmp = target.with_suffix('.tmp')
    tmp.write_text(json.dumps(data, indent=2)+'\n')
    tmp.replace(target)


def main():
    known = [1, 1, 2, 6, 24, 116, 628, 3636, 21956]
    data = dict(job_id='primary-20260912-stack22-mechanism-triage-654532f4a556',
                source_sha256=hashlib.sha256((ROOT/'source.md').read_bytes()).hexdigest(),
                arithmetic='exact Python integers; exhaustive inputs',
                rows=[], first_eager_collision=None, first_greedy_failure=None)
    for n in range(9):
        totals = dict(n=n, inputs=math.factorial(n), sortable=0, eager_sortable=0,
                      greedy_sortable=0, eager_mismatches=0,
                      successful_traces=0, eager_traces=0)
        for pi in permutations(range(1, n+1)):
            full = trace_counter(pi)
            eager = trace_counter(pi, True)
            greedy, log, stack, want = small_on_top(pi)
            totals['sortable'] += bool(full)
            totals['eager_sortable'] += bool(eager)
            totals['greedy_sortable'] += greedy
            totals['eager_mismatches'] += (bool(full) != bool(eager))
            totals['successful_traces'] += full
            totals['eager_traces'] += eager
            if eager > 1 and data['first_eager_collision'] is None:
                data['first_eager_collision'] = dict(pi=pi, eager_trace_count=eager)
            if full and not greedy and data['first_greedy_failure'] is None:
                data['first_greedy_failure'] = dict(pi=pi, greedy_log=log,
                    stuck_stack=stack, wanted=want, successful_eager_trace=eager_witness(pi))
        totals['known_count'] = known[n]
        totals['calibration_matches'] = totals['sortable'] == known[n]
        data['rows'].append(totals)
        save(data)
        print(json.dumps(totals), flush=True)
    assert all(r['calibration_matches'] and not r['eager_mismatches'] for r in data['rows'])


if __name__ == '__main__':
    main()
