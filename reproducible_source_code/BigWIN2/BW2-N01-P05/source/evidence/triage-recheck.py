"""Exact bounded triage verification; not a classification for arbitrary k."""
import sys
sys.dont_write_bytecode = True
from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
from importlib.util import spec_from_file_location, module_from_spec
from itertools import combinations, groupby
from pathlib import Path
import json
import time

HERE = Path(__file__).resolve().parent
spec = spec_from_file_location('intake', HERE / 'check-p05-small.py')
base = module_from_spec(spec)
spec.loader.exec_module(base)


def direct_stack(word):
    stack, out = [], []
    for x in word:
        while True:
            proposed = stack + [x]
            forbidden = any(proposed[i] == proposed[l] != proposed[j]
                            for i, j, l in combinations(range(len(proposed)), 3))
            if not forbidden:
                stack.append(x)
                break
            out.append(stack.pop())
    return tuple(out + stack[::-1])


def trunc(w):
    return tuple(x for x, _ in groupby(w))


def canon(w):
    d = {}
    return tuple(d.setdefault(x, len(d)) for x in w)


def trace(w, k):
    words = [w]
    for _ in range(k):
        a = direct_stack(words[-1])
        assert a == base.phi_recursive(words[-1]) == base.phi_stack(words[-1])
        words.append(a)
    return words


def main():
    start = time.monotonic()
    original = HERE / 'p05-intake-check.json'
    saved = json.loads(original.read_text())
    cases = []
    for case in saved['cases']:
        k, n = case['k'], case['length']
        expected = {tuple(w) for w in case['witnesses']}
        actual, total = set(), 0
        for w in base.rgs(n, k):
            total += 1
            a, b = w, w
            for _ in range(k-1):
                a, b = base.phi_stack(a), base.phi_recursive(b)
                assert a == b
            if not base.sorted_word(a):
                actual.add(w)
        assert total == base.stirling(n, k)
        assert actual == expected
        data = dict(k=k, length=n, enumerated=total, witnesses=len(actual))
        if n == 2*k+2:
            hist, examples, cores, fiber = Counter(), {}, Counter(), Counter()
            q_not_maximal = []
            for w in sorted(actual):
                orbit = trace(w, k)
                assert not base.sorted_word(orbit[k-1])
                assert base.sorted_word(orbit[k])
                multiplicity = w.count(0)
                assert orbit[1][-multiplicity:] == (0,) * multiplicity
                q = trunc(orbit[1][:-multiplicity])
                reduced_excess = len(q) - 2*(k-1)
                key = f'first_multiplicity={multiplicity},reduced_excess={reduced_excess}'
                hist[key] += 1
                examples.setdefault(key, dict(word=w, orbit=orbit, q=q))
                cores[len(trunc(w))] += 1
                fiber[(canon(q), multiplicity)] += 1
                z = q
                for _ in range(k-2):
                    z = base.phi_recursive(z)
                if base.sorted_word(z):
                    q_not_maximal.append(w)
            data.update(reduction_histogram=dict(sorted(hist.items())),
                        examples=examples, initial_truncation_lengths=dict(sorted(cores.items())),
                        q_not_maximal=q_not_maximal,
                        same_excess_target_fibers=[dict(q=q, first_multiplicity=m, count=c)
                            for (q,m),c in sorted(fiber.items()) if len(q)==2*(k-1)+2])
        cases.append(data)
    out = dict(job_id='newwin-00001-p05-triage-39e6415a55b0',
               recorded_at_utc=datetime.now(timezone.utc).isoformat(),
               status='exact finite observation; no all-k classification or novelty claim',
               coverage='all restricted growth words, k=3,4; n=2k,2k+1,2k+2',
               algorithms='two original maps on every input; additional full-triple stack on every excess-two witness',
               source_sha256=sha256((HERE.parent/'source.md').read_bytes()).hexdigest(),
               original_data_sha256=sha256(original.read_bytes()).hexdigest(),
               script_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
               elapsed_seconds=time.monotonic()-start, cases=cases)
    path = HERE / 'triage-recheck.json'
    temporary = path.with_suffix('.json.tmp')
    temporary.write_text(json.dumps(out, indent=2)+'\n')
    temporary.replace(path)
    print(json.dumps({**{a:b for a,b in out.items() if a!='cases'},
        'cases':[{a:b for a,b in c.items() if a not in ('examples','same_excess_target_fibers')} for c in cases]},indent=2))


if __name__ == '__main__':
    main()
