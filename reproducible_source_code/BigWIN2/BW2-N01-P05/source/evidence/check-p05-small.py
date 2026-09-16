"""Bounded intake check, not an all-k proof. Python standard library only."""
from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
from itertools import combinations
from math import comb
from pathlib import Path
import json
import platform
import time


def phi_stack(word):
    stack, output = [], []
    for x in word:
        # The existing stack avoids aba. A new occurrence must use new top x.
        while any(stack[i] == x and any(y != x for y in stack[i+1:])
                  for i in range(len(stack))):
            output.append(stack.pop())
        stack.append(x)
    return tuple(output + stack[::-1])


def phi_recursive(word):
    # Primary source Lemma 2.1, independently implemented from stack simulation.
    if not word:
        return ()
    x, output, segment, multiplicity = word[0], [], [], 0
    for y in word:
        if y == x:
            output.extend(phi_recursive(tuple(segment)))
            segment = []
            multiplicity += 1
        else:
            segment.append(y)
    output.extend(phi_recursive(tuple(segment)))
    return tuple(output) + (x,) * multiplicity


def sorted_word(word):
    return not any(word[i] == word[l] != word[j]
                   for i, j, l in combinations(range(len(word)), 3))


def rgs(n, k):
    def visit(prefix, maximum):
        if len(prefix) == n:
            if maximum + 1 == k:
                yield tuple(prefix)
            return
        if maximum + 1 + n - len(prefix) < k:
            return
        for x in range(min(k-1, maximum+1)+1):
            prefix.append(x)
            yield from visit(prefix, max(maximum, x))
            prefix.pop()
    yield from visit([0], 0)


def stirling(n, k):
    row = [1] + [0] * k
    for _ in range(n):
        row = [0] + [row[j-1]+j*row[j] for j in range(1, k+1)]
    return row[k]


def run():
    start = time.monotonic()
    cases = []
    for k in (3, 4):
        for extra in (0, 1, 2):
            n, total, witnesses, types = 2*k+extra, 0, [], Counter()
            for word in rgs(n, k):
                total += 1
                a, b = word, word
                for _ in range(k-1):
                    a, b = phi_stack(a), phi_recursive(b)
                    assert a == b, (word, a, b)
                if not sorted_word(a):
                    witnesses.append(list(word))
                    types[tuple(sorted(Counter(word).values(), reverse=True))] += 1
                    assert sorted_word(phi_stack(a)), word
            assert total == stirling(n, k), (n, k, total)
            if extra < 2:
                assert len(witnesses) == (1 if extra == 0 else comb(k+1, 2)+2*comb(k, 2))
            first_four = sum(w.count(0) == 4 for w in witnesses) if extra == 2 else None
            if extra == 2:
                assert first_four == comb(2*k+1, 3)-4*comb(k+1, 3)
            cases.append(dict(k=k, length=n, extra=extra, enumerated=total,
                              maximum_sort_count=len(witnesses),
                              multiplicity_types={str(t): c for t,c in sorted(types.items())},
                              first_letter_four_count=first_four, witnesses=witnesses))
    out = dict(schema=1, observed_at_utc=datetime.now(timezone.utc).isoformat(),
               python=platform.python_version(), domain="restricted growth strings, exactly k blocks; k=3,4; length=2k,2k+1,2k+2",
               arithmetic="exact integers", random_seed="not applicable; exhaustive deterministic enumeration",
               algorithms=["literal greedy aba-avoiding stack", "independent first-letter recursion, Lemma 2.1"],
               checks="both maps agree at each of k-1 iterations; full RGS counts equal Stirling numbers; prior Theorems 1.1/1.2 and Lemma 3.5 calibrated",
               status="finite observation only, not proof for arbitrary k",
               script_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
               elapsed_seconds=time.monotonic()-start, cases=cases)
    target = Path(__file__).with_name("p05-intake-check.json")
    target.write_text(json.dumps(out, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"output": str(target), "elapsed_seconds": out["elapsed_seconds"],
                      "cases": [{a:b for a,b in c.items() if a != "witnesses"} for c in cases]}, indent=2))


if __name__ == "__main__":
    run()
