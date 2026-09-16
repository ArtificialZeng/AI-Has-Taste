#!/usr/bin/env python3
"""Exact finite checks for research-proof.md; these are not the all-n proof.

Run: python3 -B evidence/research-verifier.py > evidence/research-verifier.json
Only the project source and existing triage JSON are read. No network/packages.
"""
import hashlib
import json
from collections import defaultdict
from datetime import datetime, timezone
from math import comb
from pathlib import Path
from time import perf_counter

ROOT = Path(__file__).resolve().parents[1]
JOB = "primary-20260914-grid-narayana-research-12ef05d8a66f"


def clean(d):
    return {k: v for k, v in d.items() if v}


def generic_a(f):
    """Monomials u^i v^j t^p c^q, with c independent of t."""
    g = defaultdict(int)
    for (i, j, p, q), a in f.items():
        g[i+1, j, p, q] += a
        g[i, j, p, q+1] += a
        if i:
            g[i-1, j, p+1, q] += a
    return clean(g)


def generic_b(f):
    g = defaultdict(int)
    for (i, j, p, q), a in f.items():
        g[i, j+1, p, q] += a
        g[i, j, p, q+1] += a
        if j:
            g[i, j-1, p+1, q] += a
        elif i:
            g[i-1, 0, p+1, q] += a
    return clean(g)


def specialize_states(f):
    g = defaultdict(int)
    for (i, j, p, q), a in f.items():
        for k in range(q+1):
            g[i, j, p+k] += a*comb(q, k)
    return clean(g)


def terminal_generic(f):
    return {(p, q): a for (i, j, p, q), a in generic_a(f).items()
            if i == j == 0}


def terminal_specialized(h, n):
    out = [0]*(2*n)
    for (p, q), a in h.items():
        for k in range(q+1):
            out[p+k] += a*comb(q, k)
    return out


def laurent_power(n):
    f = {(0, 0, 0): 1}
    for _ in range(n):
        g = defaultdict(int)
        for (i, p, q), a in f.items():
            g[i+1, p, q] += a
            g[i, p, q+1] += a
            g[i-1, p+1, q] += a
        f = dict(g)
    by_exp = defaultdict(dict)
    for (i, p, q), a in f.items():
        by_exp[i][p, q] = a
    return dict(by_exp)


def poly_product(f, g):
    h = defaultdict(int)
    for (p, q), a in f.items():
        for (r, s), b in g.items():
            h[p+r, q+s] += a*b
    return clean(h)


def generic_expected(n):
    a = laurent_power(n)
    h = poly_product(a[0], a[1])
    assert all(v % n == 0 for v in h.values())
    return {k: v//n for k, v in h.items()}


def extraction_sum(n):
    a, b = laurent_power(n), laurent_power(n+1)
    h = defaultdict(int)
    for k in range(1, n+1):
        for (p, q), v in poly_product(b[k], a[k]).items():
            h[p+k-1, q] += k*v
    den = n*(n+1)
    assert all(v % den == 0 for v in h.values())
    return {k: v//den for k, v in h.items()}


def raw_step(f):
    g = defaultdict(int)
    for (z, s, p), w in f.items():
        for a in range(z+2):
            for b in range(z+s+3-a):
                d = max(0, b-s-1)
                g[z+1-a-d, max(0, s+1-b), p+(a>0)+(b>0)] += w
    return dict(g)


def shift_raw(f):
    g = defaultdict(int)
    for (z, s, p), w in f.items():
        for i in range(z+1):
            for j in range(s+1):
                g[i, j, p] += w*comb(z, i)*comb(s, j)
    return clean(g)


def raw_terminal(f, n):
    h = [0]*(2*n)
    for (z, s, p), w in f.items():
        h[p] += w
        h[p+1] += w*(z+1)
    return h


def proposed(n):
    a = [comb(n-1, j)*comb(n, j)//(j+1) for j in range(n)]
    b = [comb(n, j)**2 for j in range(n+1)]
    h = [0]*(2*n)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            h[i+j] += x*y
    return h


def weak_vectors(length, budget):
    if not length:
        yield ()
    else:
        for a in range(budget+1):
            for tail in weak_vectors(length-1, budget-a):
                yield (a,)+tail


def direct_count(n):
    """All vectors of length d=2n-1 with total <=d, no pruning by ideals."""
    d = 2*n-1
    h, examined = [0]*(d+1), 0
    for a in weak_vectors(d, d):
        examined += 1
        low, high = [0], [0]
        for v in a[:n]:
            low.append(low[-1]+v)
        for v in a[n:]:
            high.append(high[-1]+v)
        if all(low[i]+high[j] <= i+j for i in range(n+1)
               for j in range(min(i, n-1)+1)):
            h[sum(v > 0 for v in a)] += 1
    assert examined == comb(2*d, d)
    return h, examined


def numeric_a(f, c, t):
    g = defaultdict(int)
    for (i, j), w in f.items():
        g[i+1, j] += w
        g[i, j] += c*w
        if i:
            g[i-1, j] += t*w
    return clean(g)


def numeric_b(f, c, t):
    g = defaultdict(int)
    for (i, j), w in f.items():
        g[i, j+1] += w
        g[i, j] += c*w
        if j:
            g[i, j-1] += t*w
        elif i:
            g[i-1, 0] += t*w
    return clean(g)


def numeric_t_power(f, n, c, t):
    for _ in range(n):
        f = numeric_b(numeric_a(f, c, t), c, t)
    return f


def trace_test(n, c, t):
    N, L = 2*n+2, n+2
    trace = 0
    outside_origin_rows = 0
    for i in range(N+1):
        for j in range(L+1):
            e = {(i, j): 1}
            at = numeric_a(numeric_t_power(e, n, c, t), c, t)
            ta = numeric_t_power(numeric_a(e, c, t), n, c, t)
            delta = at.get((i, j), 0)-ta.get((i, j), 0)
            trace += delta
            if i > 2*n or j > n:
                outside_origin_rows += abs(delta)
    boundary = 0
    for j in range(L+1):
        from_n = numeric_t_power({(N, j): 1}, n, c, t)
        from_np1 = numeric_t_power({(N+1, j): 1}, n, c, t)
        boundary += t*from_n.get((N+1, j), 0)-from_np1.get((N, j), 0)
    h = numeric_a(numeric_t_power({(0, 0): 1}, n-1, c, t), c, t).get((0, 0), 0)
    assert trace == boundary == -n*t*h
    assert outside_origin_rows == 0
    return {"n": n, "c": c, "t": t, "trace": trace,
            "boundary_flux": boundary, "minus_n_t_h": -n*t*h,
            "N": N, "L": L, "outer_diagonal_zero": True}


def main():
    start = perf_counter()
    source_digest = hashlib.sha256((ROOT/"source.md").read_bytes()).hexdigest()
    assert source_digest == "3475114886a7af30aad77d1c99dcf080b0b048690f814c3d5ac22f6b4e87b801"
    saved = json.loads((ROOT/"evidence/triage-transfer.json").read_text())
    commutator_cases = 0
    for i in range(6):
        for j in range(6):
            f = {(i, j, 0, 0): 1}
            ba, ab = generic_b(generic_a(f)), generic_a(generic_b(f))
            delta = clean({k: ba.get(k, 0)-ab.get(k, 0) for k in set(ba)|set(ab)})
            assert delta == ({(0, 0, 1, 0): 1} if i == j == 0 else {})
            commutator_cases += 1
    f, raw, cases = {(0, 0, 0, 0): 1}, {(0, 0, 0): 1}, []
    for n in range(1, 11):
        assert specialize_states(f) == shift_raw(raw)
        h = terminal_generic(f)
        assert h == generic_expected(n) == extraction_sum(n)
        hs = terminal_specialized(h, n)
        assert hs == raw_terminal(raw, n) == proposed(n)
        assert hs == saved["cases"][n-1]["coefficients"]
        row = {"n": n, "coefficients": hs, "total": sum(hs),
               "generic_c_t_identity": True, "coefficient_extraction_identity": True,
               "whole_state_basis_change": True, "raw_transfer_matches": True,
               "saved_triage_matches": True,
               "generic_terms": [{"t_exponent": p, "c_exponent": q, "coefficient": a}
                                 for (p, q), a in sorted(h.items())]}
        if n <= 5:
            direct, examined = direct_count(n)
            assert direct == hs
            row.update(direct_ideal_prefix_matches=True, ambient_vectors=examined)
        cases.append(row)
        if n < 10:
            f = generic_b(generic_a(f))
            raw = raw_step(raw)
    traces = [trace_test(n, c, t) for n in range(1, 6)
              for c, t in [(2, 3), (0, 0), (-2, 1), (3, -2)]]
    print(json.dumps({"job_id": JOB,
          "observed_at": datetime.now(timezone.utc).isoformat(),
          "source_sha256": source_digest,
          "arithmetic": "exact integer polynomial coefficients; deterministic",
          "proof_status": "finite verification of a separate all-n proof candidate",
          "independent_referee": False,
          "commutator_monomials_checked": commutator_cases,
          "scope": "full state basis change and generic (c,t) identity n=1..10; direct original inequalities n=1..5; finite-rank traces n=1..5 at four exact parameter pairs",
          "cases": cases, "trace_checks": traces,
          "all_checks_passed": True, "seconds": perf_counter()-start}, indent=2))


if __name__ == "__main__":
    main()
