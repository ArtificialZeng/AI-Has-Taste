"""Exhaustive exact Schur tests of zero-compressed pair profiles."""
from pathlib import Path
from math import comb
import hashlib
import json
import time

JOB = "primary-20260914-bigdescent-logconcavity-research-6ff0786c2423"
EDGES = (((0, 0), (1, 0)), ((0, 1), (2, 1)), ((0, 1), (2, 0)))
TRANS = [[[] for _ in range(9)] for _ in range(3)]
for a in range(3):
    for b in range(3):
        for aa, x in EDGES[a]:
            for bb, y in EDGES[b]:
                TRANS[x+y][3*a+b].append((3*aa+bb, x))
INITIAL = {(s, 0): 1 for s in (0, 2, 6, 8)}
ACCEPT = {4, 5, 7, 8}

def step(v, e):
    out = {}
    for (s, d), val in v.items():
        for new, inc in TRANS[e][s]:
            key = (new, d+inc)
            out[key] = out.get(key, 0) + val
    return out

def coefficients(v, total):
    h = [0]*(total+1)
    for (s, d), val in v.items():
        if s in ACCEPT:
            h[d] += val
    return h

def tensor(profile):
    v = INITIAL
    for e in profile:
        v = step(v, e)
    return coefficients(v, sum(profile))

def main(max_degree=14):
    start = time.perf_counter()
    counts = [0]*(max_degree+1)
    nonzero = [0]*(max_degree+1)
    inequalities = [0]*(max_degree+1)
    first_bad = None
    first_asymmetry = None
    smallest_positive = [None]*(max_degree+1)

    def check(v, degree, profile):
        nonlocal first_bad, first_asymmetry
        counts[degree] += 1
        h = coefficients(v, degree)
        nonzero[degree] += any(h)
        if h != h[::-1] and first_asymmetry is None:
            first_asymmetry = {"profile": profile, "h": h}
        for j in range(1, degree//2+1):
            inequalities[degree] += 1
            delta = h[j]-h[j-1]
            if delta < 0 and first_bad is None:
                first_bad = {"profile": profile, "degree": degree,
                             "j": j, "h": h, "difference": delta}
            if delta > 0 and (smallest_positive[degree] is None or
                             delta < smallest_positive[degree]):
                smallest_positive[degree] = delta

    def visit(v, degree, profile):
        check(v, degree, profile)
        check(step(v, 0), degree, profile+(0,))
        if degree >= max_degree:
            return
        for zero in (False, True):
            vv = step(v, 0) if zero else v
            pp = profile+(0,) if zero else profile
            for e in (1, 2):
                if degree+e <= max_degree:
                    visit(step(vv, e), degree+e, pp+(e,))

    check(INITIAL, 0, ())
    check(step(INITIAL, 0), 0, (0,))
    for lead in (False, True):
        v = step(INITIAL, 0) if lead else INITIAL
        p = (0,) if lead else ()
        for e in (1, 2):
            visit(step(v, e), e, p+(e,))
    expected = [2]+[sum(comb(l, d-l)*2**(l+1)
                         for l in range((d+1)//2, d+1))
                       for d in range(1, max_degree+1)]
    assert counts == expected, (counts, expected)
    out = {
        "job_id": JOB, "arithmetic": "exact Python integers",
        "total_degree_max": max_degree,
        "compressed_profile_counts_by_degree": counts,
        "nonzero_profile_counts_by_degree": nonzero,
        "Schur_inequalities_by_degree": inequalities,
        "profiles_checked": sum(counts),
        "Schur_inequalities_checked": sum(inequalities),
        "first_Schur_failure": first_bad,
        "first_asymmetry": first_asymmetry,
        "smallest_positive_difference_by_degree": smallest_positive,
        "coverage": "Every zero-compressed profile of total degree 0..14, including odd degrees, all optional zero gaps and both boundaries. Degree 0 has empty and single-zero profiles.",
        "Schur_rule": "For symmetric homogeneous H of degree d with h_j=[x^j y^(d-j)]H, the s_(d-j,j) coefficient is h_j-h_(j-1), with h_-1=0. h_0 is nonnegative directly.",
        "qualification": "Finite exhaustive evidence plus proved zero compression covers these degrees for all lengths. No all-degree proof or fresh referee.",
        "seconds": time.perf_counter()-start,
        "source_sha256": hashlib.sha256(Path('source.md').read_bytes()).hexdigest(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(out, indent=2))

if __name__ == '__main__':
    main()
