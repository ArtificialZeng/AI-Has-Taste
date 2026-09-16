"""Exact, deterministic triage enumeration; run from PROJECT_DIR.

No proposed recurrence is used to generate permutations or counts.
The min-element decomposition enumerates 312-avoiders uniquely.
For pi=(alpha+1),1,(beta+k+1), LDS(pi)=max(LDS(alpha)+1,LDS(beta)).
"""
import hashlib
import json
from functools import lru_cache
from itertools import combinations, permutations
from pathlib import Path


@lru_cache(None)
def avoid312(n, height):
    if n == 0:
        return ((),)
    if height == 0:
        return ()
    out = []
    for k in range(n):
        for alpha in avoid312(k, height - 1):
            left = tuple(x + 1 for x in alpha) + (1,)
            for beta in avoid312(n - k - 1, height):
                out.append(left + tuple(x + k + 1 for x in beta))
    return tuple(out)


def contains(p, pattern):
    for indices in combinations(range(len(p)), len(pattern)):
        values = tuple(p[i] for i in indices)
        ranks = {x: j + 1 for j, x in enumerate(sorted(values))}
        if tuple(ranks[x] for x in values) == pattern:
            return True
    return False


def square(p):
    return tuple(p[x - 1] for x in p)


def avoids132(p):
    # For each j, find i<j<k with p[i]<p[k]<p[j].
    if len(p) < 3:
        return True
    prefix_min = p[0]
    for j in range(1, len(p) - 1):
        if any(prefix_min < x < p[j] for x in p[j + 1:]):
            return False
        prefix_min = min(prefix_min, p[j])
    return True


def main():
    rows = []
    endpoint_lists = {}
    brute_checks = []
    for n in range(13):
        pool = avoid312(n, 4)
        valid = tuple(p for p in pool if avoids132(square(p)))
        endpoints = tuple(p for p in valid if p and p[-1] == 1)
        row = {"n": n, "avoid312_54321": len(pool),
               "a_n": len(valid), "b_n_ending_in_1": len(endpoints)}
        rows.append(row)
        endpoint_lists[str(n)] = endpoints
        if n <= 7:
            brute_pool = set()
            brute_valid = set()
            for p in permutations(range(1, n + 1)):
                assert avoids132(p) == (not contains(p, (1, 3, 2)))
                if not contains(p, (3, 1, 2)) and not contains(p, (5, 4, 3, 2, 1)):
                    brute_pool.add(p)
                    if not contains(square(p), (1, 3, 2)):
                        brute_valid.add(p)
            assert len(pool) == len(set(pool))
            assert set(pool) == brute_pool
            assert set(valid) == brute_valid
            brute_checks.append({"n": n, "set_equality": True,
                                 "direct_pattern_detector_checked": True})
        if n >= 6:
            rhs = sum(rows[n - j]["a_n"] for j in range(1, 5)) + n - 1
            row["recurrence_rhs"] = rhs
            row["recurrence_matches"] = row["a_n"] == rhs
        print(json.dumps(row), flush=True)
    t = [1]
    for n in range(1, 13):
        t.append(sum(t[n - j] for j in range(1, min(4, n) + 1)))
        convolution = sum(rows[k]["b_n_ending_in_1"] * t[n - k]
                          for k in range(1, n + 1))
        assert rows[n]["a_n"] == convolution
    out = {"job_id": "newwin-00001-p06-triage-aaf5e6140737",
           "scope": "Exact finite observation, n=0..12; not an all-n proof",
           "source_sha256": hashlib.sha256(Path("source.md").read_bytes()).hexdigest(),
           "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           "rows": rows, "bruteforce_crosschecks": brute_checks,
           "suffix_composition_counts": t,
           "convolution_matches_through": 12,
           "endpoint_permutations": endpoint_lists}
    path = Path("evidence/triage_counts.json")
    tmp = path.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(out, indent=2) + "\n")
    tmp.replace(path)


if __name__ == "__main__":
    main()
