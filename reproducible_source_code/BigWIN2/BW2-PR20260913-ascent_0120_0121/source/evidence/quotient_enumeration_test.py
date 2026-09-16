"""Exact checks of the proved quotient and independently assembled series.

Run: python3 evidence/quotient_enumeration_test.py
Only quotient-enumeration-results.json is written. Python 3 standard library
is sufficient except for the optional exact small rational-function check,
which uses SymPy (installed in this environment).
"""
from collections import Counter, defaultdict
from itertools import combinations, product
from math import comb
from pathlib import Path
import hashlib
import json
import random
import sys
import time

JOB = "primary-20260913-ascent-0120-0121-research-3f4c053fe3cf"
MAX_EXACT_PREFIX = 15
MAX_SERIES_DEGREE = 28
SOURCE_HASH = "c3511d885d5d487049ba8d52247444c1e27c6005f320a593c5aa5ffbb7bfd48b"
started = time.monotonic()
assert hashlib.sha256(Path("source.md").read_bytes()).hexdigest() == SOURCE_HASH


def rank_children(s):
    k, mask = s
    m = (mask & -mask).bit_length() - 1
    for t in range(k):
        if t <= m:
            yield k, mask | (1 << t)
        else:
            low = (1 << t) - 1
            r = (mask & low).bit_count()
            yield k + 1 - r, ((mask & ~low) >> r) | (1 << (t-r))


# Reference state: all increasing ordered value pairs and their banned
# endpoints, rather than the simplified forbidden-letter identity.
ROOT = (0, 0, frozenset({0}), frozenset(), frozenset())


def exact_children(s):
    a, last, seen, pairs, banned = s
    for v in range(a+2):
        if v in banned:
            continue
        new_banned = banned | frozenset(
            u for pair in pairs if pair[1] < v for u in pair)
        new_pairs = pairs | frozenset((u, v) for u in seen if u < v)
        yield v, (a+(last < v), v, seen | {v}, new_pairs, new_banned)


def project(s):
    a, last, seen, pairs, banned = s
    assert max(seen) <= a
    if max(seen) < 2:
        assert not banned
        return "b", a, last
    eligible = [v for v in range(a+2) if v not in banned]
    h = [i for i, v in enumerate(eligible) if v in seen]
    assert h and eligible[min(h)] == last
    assert eligible[-1] == a+1 and a+1 not in seen
    assert h[-1] < len(eligible)-1
    return "p", len(eligible), sum(1 << i for i in h)


def projected_children(p):
    mode, x, y = p
    if mode == "p":
        return [("p", k, mask) for k, mask in rank_children((x, y))]
    return [("b", x+(y < v), v) for v in (0, 1)] + [
        ("p", x+1, 1 << (v-2)) for v in range(2, x+2)]


# Complete reachability by exact-state merging. Future exact states depend
# only on the five displayed components, so merging loses no continuations.
# A concrete representative word is kept to test the new banned-set lemma.
states = {ROOT: (1, (0,))}
exact_counts = [1, 1]
coverage = []
for n in range(1, MAX_EXACT_PREFIX+1):
    nxt = {}
    edges = 0
    for s, (multiplicity, w) in states.items():
        p = project(s)
        if p[0] == "p":
            simplified = {0} | {
                u for i, u in enumerate(w) if u > 0
                and any(v > u for v in w[i+1:])}
            assert simplified == s[4], (w, s, simplified)
        children = list(exact_children(s))
        actual = Counter(project(cs) for v, cs in children)
        assert actual == Counter(projected_children(p)), (w, p, actual)
        if p[0] == "p":
            assert all(cp[1] <= p[1] for cp in actual)
        edges += len(children)
        for v, cs in children:
            old_count, old_w = nxt.get(cs, (0, w+(v,)))
            nxt[cs] = old_count+multiplicity, old_w
    coverage.append({"prefix_length": n, "exact_states": len(states),
                     "represented_words": sum(m for m, w in states.values()),
                     "edges_checked": edges})
    states = nxt
    exact_counts.append(sum(m for m, w in states.values()))
    print("exact", n, coverage[-1]["exact_states"], flush=True)


def mixed_counts(N):
    binary = {(0, 0): 1}
    post = {}
    counts = [1, 1]
    state_sizes = [0, 0]
    for n in range(1, N):
        nb, np = defaultdict(int), defaultdict(int)
        for (a, last), mult in binary.items():
            for v in (0, 1):
                nb[a+(last < v), v] += mult
            for v in range(2, a+2):
                np[a+1, 1 << (v-2)] += mult
        for s, mult in post.items():
            for cs in rank_children(s):
                np[cs] += mult
        binary, post = nb, np
        counts.append(sum(binary.values())+sum(post.values()))
        state_sizes.append(len(post))
    return counts, state_sizes


counts, state_sizes = mixed_counts(MAX_SERIES_DEGREE)
assert counts[:len(exact_counts)] == exact_counts

# A separate backward continuation computation followed by the explicit
# binomial convolution in formula (1). No binary-state DP is used here.
L = (MAX_SERIES_DEGREE+1)//2
domain = [(k, mask) for k in range(2, L+1)
          for mask in range(1, 1 << (k-1))]
assert len(domain) == (1 << L)-L-1
index = {s: i for i, s in enumerate(domain)}
edge_indices = [[index[cs] for cs in rank_children(s)] for s in domain]
for s, edges in zip(domain, edge_indices):
    assert len(edges) == s[0]
    assert all(2 <= domain[j][0] <= s[0] for j in edges)
summed_cont = {k: [] for k in range(2, L+1)}
current = [1]*len(domain)
for d in range(MAX_SERIES_DEGREE-2):
    for k in summed_cont:
        summed_cont[k].append(sum(current[index[k, 1 << h]]
                                  for h in range(k-1)))
    current = [sum(current[j] for j in edges) for edges in edge_indices]

assembled = [1]+[1 << (n-1) for n in range(1, MAX_SERIES_DEGREE+1)]
for k, coeffs in summed_cont.items():
    r = 2*k-1
    for n in range(r, MAX_SERIES_DEGREE+1):
        assembled[n] += sum(coeffs[d]*comb(n-d-1, r-1)
                            for d in range(n-r+1))
assert assembled == counts

# Direct enumeration of binary words checks B_a and includes all ways to
# end in 0 or 1, zero ascents, and unattainable ascent/length combinations.
binary_checks = 0
for n in range(1, 14):
    observed = Counter(sum(u < v for u, v in zip(w, w[1:]))
                       for tail in product((0, 1), repeat=n-1)
                       for w in [(0,)+tail])
    assert observed[0] == 1
    for a in range(1, n+1):
        expected = comb(n, 2*a) if n >= 2*a else 0
        assert observed[a] == expected, (n, a, observed[a], expected)
        binary_checks += 1

# Held-out structured high-width initializations and full seen-set buildup.
# These directly exercise skipped values and non-RGF states far beyond
# the complete short-length exact-state census.
structured_checks = 0
for K in (2, 3, 8, 17, 32):
    pword = (0, 1)*(K-1)
    st = ROOT
    for v in pword[1:]:
        st = dict(exact_children(st))[v]
    for h in sorted({0, (K-2)//2, K-2}):
        cs = dict(exact_children(st))[h+2]
        label = ("p", K, 1 << h)
        assert project(cs) == label
        for t in range(h-1, -1, -1):
            # With no intervening ascent, eligible rank t has value t+2.
            cs = dict(exact_children(cs))[t+2]
            label = ("p", K, label[2] | (1 << t))
            assert project(cs) == label
        actual = Counter(project(vs) for v, vs in exact_children(cs))
        assert actual == Counter(projected_children(label))
        structured_checks += 1

# Deterministically seeded stress walks, with exact pairs as the reference.
rng = random.Random(20260913)
stress_edges = 0
for trial in range(40):
    st = ROOT
    for i in range(160):
        options = list(exact_children(st))
        p = project(st)
        assert Counter(project(cs) for v, cs in options) == Counter(projected_children(p))
        stress_edges += len(options)
        selector = trial % 4
        if i < 2*(trial % 15)+1:
            v = 1 if i % 2 == 0 else 0
            st = dict(options)[v]
        elif selector == 0:
            st = options[-1][1]
        elif selector == 1:
            st = options[0 if i % 2 else -1][1]
        else:
            st = rng.choice(options)[1]

# Exact symbolic small-width display, including a zero residual certificate.
import sympy as sp
z = sp.Symbol("z")
rational = {}
for K in (2, 3, 4):
    small = [(k, mask) for k in range(2, K+1)
             for mask in range(1, 1 << (k-1))]
    loc = {s: i for i, s in enumerate(small)}
    T = sp.zeros(len(small))
    for i, s in enumerate(small):
        for cs in rank_children(s):
            T[i, loc[cs]] += 1
    c = (sp.eye(len(small))-z*T).inv()*sp.ones(len(small), 1)
    assert all(sp.cancel(v) == 0 for v in (sp.eye(len(small))-z*T)*c-sp.ones(len(small), 1))
    answer = sp.cancel(sum(c[loc[K, 1 << h]] for h in range(K-1)))
    num, den = sp.fraction(answer)
    rational[str(K)] = {"summed_singleton_continuation": str(answer),
                        "numerator": str(num), "denominator": str(den),
                        "matrix_dimension": len(small),
                        "equation_residual_zero": True}

assert hashlib.sha256(Path("source.md").read_bytes()).hexdigest() == SOURCE_HASH
out = {"job_id": JOB, "source_sha256": SOURCE_HASH,
       "proof_file": "evidence/quotient-enumeration-proof.md",
       "exact_reference": {"max_prefix_length": MAX_EXACT_PREFIX,
                           "counts": exact_counts, "coverage": coverage,
                           "quotient_and_invariants_pass": True},
       "series_assembly": {"max_degree": MAX_SERIES_DEGREE,
                           "counts": counts, "postbinary_state_sizes": state_sizes,
                           "max_exit_width": L, "full_domain_size": len(domain),
                           "mixed_and_binomial_matrix_assembly_match": True},
       "binary_prefix_checks": binary_checks,
       "structured_large_width_checks": structured_checks,
       "seeded_stress": {"seed": 20260913, "walks": 40,
                         "steps_per_walk": 160, "edges_checked": stress_edges},
       "small_rational_continuations": rational,
       "python_version": sys.version,
       "sympy_version": sp.__version__,
       "runtime_seconds": round(time.monotonic()-started, 3),
       "qualification": "Exact finite checks and exact symbolic identities. The all-length claim relies on the written induction and unique binary-prefix decomposition, not extrapolation from these tests. No independent referee acceptance or priority certificate is asserted."}
Path("evidence/quotient-enumeration-results.json").write_text(json.dumps(out, indent=2)+"\n")
print(json.dumps(out, indent=2))
