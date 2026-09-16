#!/usr/bin/env python3
"""Exact triage check; finite agreement is not a proof of the conjecture."""
import hashlib
import importlib.util
import json
from collections import defaultdict
from datetime import datetime, timezone
from math import comb
from pathlib import Path
from time import perf_counter

ROOT = Path(__file__).resolve().parents[1]
JOB = "primary-20260914-grid-narayana-triage-7308d1927a46"


def proposed(n):
    a = []
    for j in range(n):
        num = comb(n-1, j)*comb(n, j)
        assert num % (j+1) == 0
        a.append(num//(j+1))
    b = [comb(n, j)**2 for j in range(n+1)]
    h = [0]*(2*n)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            h[i+j] += x*y
    return h


def finish(states, n):
    h = [0]*(2*n)
    for (z, s, k), count in states.items():
        h[k] += count
        h[k+1] += (z+1)*count
    return h


def append_column(states):
    out = defaultdict(int)
    for (z, s, k), count in states.items():
        for a in range(z+2):
            for b in range(z+s+3-a):
                delta = max(0, b-s-1)
                zn = z+1-a-delta
                sn = max(0, s+1-b)
                assert zn >= 0
                out[zn, sn, k+(a > 0)+(b > 0)] += count
    return out


def main():
    start = perf_counter()
    spec = importlib.util.spec_from_file_location(
        "calibration", ROOT/"evidence/intake-calibration.py")
    calibration = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(calibration)
    saved = json.loads((ROOT/"evidence/intake-calibration.json").read_text())
    states = {(0, 0, 0): 1}
    rows = []
    for n in range(1, 11):
        h = finish(states, n)
        row = {"n": n, "coefficients": h, "total": sum(h),
               "proposed_coefficients": proposed(n),
               "matches_proposal": h == proposed(n),
               "transfer_states_including_support": len(states)}
        if n <= 6:
            direct, examined, _ = calibration.grid_count(n)
            row.update(direct_recomputed_coefficients=direct,
                       ambient_vectors_checked=examined,
                       matches_direct=h == direct,
                       matches_saved=h == saved["cases"][n-1]["actual_coefficients"])
            assert h == direct
        if n <= 4:
            direct, examined, ideals = calibration.grid_count(n, generic=True)
            row.update(generic_ideal_count=ideals,
                       generic_vectors_checked=examined,
                       matches_generic_ideals=h == direct)
            assert h == direct
        rows.append(row)
        if n < 10:
            states = append_column(states)
    print(json.dumps({"job_id": JOB,
        "observed_at": datetime.now(timezone.utc).isoformat(),
        "source_sha256": hashlib.sha256((ROOT/"source.md").read_bytes()).hexdigest(),
        "arithmetic": "exact integers; deterministic; no random sample",
        "scope": "transfer n=1..10; direct prefixes n=1..6; generic ideals n=1..4",
        "uniform_factorization_proved": False,
        "independent_referee": False,
        "cases": rows, "seconds": perf_counter()-start}, indent=2))


if __name__ == "__main__":
    main()
