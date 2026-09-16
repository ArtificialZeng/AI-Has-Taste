"""Exact k=3 reconstruction and characteristic-free elimination certificates.

No imports from triage_symbolic.py; the old output is compared only after
constructing every matrix, solving every admissible cell, and counting it.
Run: python3 evidence/verify_sparse.py
All row/column/permutation indices in this file and output are one-based.
Sparse polynomials over Z use sorted tuples of variable names as monomials.
"""
from collections import Counter
from itertools import permutations, product
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
JOB = "newwin-00001-p12-research-79bff11d6956"
ONE = {(): 1}


def add(f, g):
    h = f.copy()
    for m, c in g.items():
        h[m] = h.get(m, 0) + c
        if h[m] == 0:
            del h[m]
    return h


def neg(f):
    return {m: -c for m, c in f.items()}


def mul(f, g):
    h = {}
    for m, c in f.items():
        for n, d in g.items():
            t = tuple(sorted(m + n))
            h[t] = h.get(t, 0) + c * d
            if h[t] == 0:
                del h[t]
    return h


def variables(f):
    return set(v for m in f for v in m)


def subst(f, values):
    result = {}
    for m, c in f.items():
        term = {(): c}
        for v in m:
            term = mul(term, values.get(v, {(v,): 1}))
        result = add(result, term)
    return result


def encode(f):
    return [[c, list(m)] for m, c in sorted(f.items())]


def matmul(a, b):
    assert len(a[0]) == len(b)
    result = []
    for row in a:
        out = []
        for c in range(len(b[0])):
            f = {}
            for t in range(len(b)):
                f = add(f, mul(row[t], b[t][c]))
            out.append(f)
        result.append(out)
    return result


def reconstruct(s, p):
    # Entry-wise geometric definition, using inverse positions, rather than
    # iterating over inversions to mark Boolean supports as in the first code.
    left = []
    for r in range(1, 5):
        a = s.index(r) + 1
        left.append([ONE.copy() if c == a else
                     {(f"x{a}{c}",): 1} if a < c and r > s[c-1] else {}
                     for c in range(1, 5)])
    right = []
    for r in range(1, 4):
        b = p.index(r) + 1
        right.append([ONE.copy() if c == b else
                      {(f"y{c}{b}",): 1} if c < b and p[c-1] > r else {}
                      for c in range(1, 4)])
    slices = []
    for face in (1, 2):
        e = [[ONE.copy() if r == c + face - 1 else {}
              for c in range(1, 4)] for r in range(1, 5)]
        slices.append(matmul(matmul(left, e), right))
    names = sorted(set(v for matrix in (left, right) for row in matrix
                       for f in row for v in variables(f)))
    n = sum(s[i] > s[j] for i in range(4) for j in range(i+1, 4))
    n += sum(p[i] > p[j] for i in range(3) for j in range(i+1, 3))
    assert n == len(names)
    for matrix in slices:
        for row in matrix:
            for f in row:
                assert all(c == 1 for c in f.values())
                assert all(len(m) <= 2 and len(set(m)) == len(m) for m in f)
    # Every constant entry is exactly a pivot 1, independently checked.
    constants = {(face, r, c) for face in (1, 2) for r in range(1, 5)
                 for c in range(1, 4) if () in slices[face-1][r-1][c-1]}
    pivots = {(face, s[p[c-1]+face-2], c)
              for face in (1, 2) for c in range(1, 4)}
    assert constants == pivots
    assert all(slices[a-1][r-1][c-1] == ONE for a, r, c in pivots)
    return slices, names


def enumerate_shapes():
    # Descending nested ranges make the partition inequalities intrinsic.
    for l1 in range(4):
        for l2 in range(min(l1, 2)+1):
            for l3 in range(min(l2, 1)+1):
                for m1 in range(min(l1, 2)+1):
                    for m2 in range(min(m1, l2, 1)+1):
                        yield (l1, l2, l3), (m1, m2, 0)


def forbidden(lam, mu):
    return [(face, r, c) for face, shape in enumerate((lam, mu), 1)
            for r in range(1, 5) for c in range(1, 4)
            if r + shape[c-1] > 4]


def certify_cell(slices, names, positions, pi):
    entries = [(pos, slices[pos[0]-1][pos[1]-1][pos[2]-1])
               for pos in positions]
    bad = [pos for pos, f in entries if () in f]
    if bad:
        assert all(f == ONE for pos, f in entries if pos in bad)
        return {"empty": True, "forbidden_pivot": list(bad[0])}
    equations = [(pos, f) for pos, f in entries if f]
    pivots = {}
    predecessors = {v: set() for v in names}
    for pos, f in equations:
        # Front equations solve for their unique linear y; back equations
        # for their unique linear x. This is tested from actual polynomials.
        prefix = "y" if pos[0] == 1 else "x"
        choices = [m[0] for m, c in f.items()
                   if len(m) == 1 and c == 1 and m[0].startswith(prefix)]
        assert len(choices) == 1, (pos, f, choices)
        v = choices[0]
        assert v not in pivots, (pos, v)
        assert [m for m in f if v in m] == [(v,)]
        pivots[v] = (pos, f)
        predecessors[v] = variables(f) - {v}
    # Topological sorting independently verifies the required acyclicity.
    order = []
    remaining = set(names)
    while remaining:
        available = sorted(v for v in remaining
                           if not (predecessors[v] & remaining))
        assert available, (equations, predecessors)
        order.extend(available)
        remaining.difference_update(available)
    # Also verify a closed order, independently of topological sorting:
    # x_ab has key (b,0,0,a), y_ij has key (pi(i),1,-pi(j),0).
    def order_key(v):
        a, b = int(v[1]), int(v[2])
        return (b, 0, 0, a) if v[0] == 'x' else (pi[a-1], 1, -pi[b-1], 0)
    assert all(order_key(u) < order_key(v)
               for v in names for u in predecessors[v])
    order = sorted(names, key=order_key)
    solutions = {}
    eliminated = []
    earlier = set()
    free = set(names) - set(pivots)
    for v in order:
        if v in pivots:
            pos, f = pivots[v]
            assert predecessors[v] <= earlier
            reduced = subst(f, solutions)
            assert reduced.get((v,)) == 1
            assert [m for m in reduced if v in m] == [(v,)]
            value = neg(add(reduced, {(v,): -1}))
            assert variables(value) <= free & earlier
            solutions[v] = value
            eliminated.append({"entry": list(pos), "pivot": v,
                               "equation": encode(f),
                               "value_in_free_variables": encode(value)})
        earlier.add(v)
    # These are identities over Z; no field sampling or divisions occur.
    assert all(not subst(f, solutions) for pos, f in entries)
    assert len(eliminated) == len(equations)
    assert len(free) == len(names) - len(equations)
    return {"empty": False, "h": len(equations), "dimension": len(free),
            "free_variables": sorted(free), "variable_order": order,
            "eliminations": eliminated}


def main():
    shapes = list(enumerate_shapes())
    assert len(shapes) == len(set(shapes)) == 55
    pairs = [(s, p) for s in permutations((1, 2, 3, 4))
             for p in permutations((1, 2, 3))]
    data = {(s, p): reconstruct(s, p) for s, p in pairs}
    matrices = [{"sigma": s, "pi": p, "variables": data[s, p][1],
                 "slices": [[[encode(f) for f in row] for row in matrix]
                            for matrix in data[s, p][0]]}
                for s, p in pairs]
    rows = []
    empty_count = total_equations = max_degree = 0
    for lam, mu in shapes:
        terms = []
        counts = Counter()
        for s, p in pairs:
            slices, names = data[s, p]
            cert = certify_cell(slices, names, forbidden(lam, mu), p)
            cert.update({"sigma": s, "pi": p, "nvariables": len(names)})
            terms.append(cert)
            if cert["empty"]:
                empty_count += 1
            else:
                counts[cert["dimension"]] += 1
                total_equations += cert["h"]
                for eq in cert["eliminations"]:
                    max_degree = max(max_degree, max(
                        [len(m) for c, m in eq["value_in_free_variables"]] or [0]))
        lengths = [5-j-lam[j-1] for j in (1, 2, 3)]
        lengths += [4-j-mu[j-1] for j in (1, 2, 3)]
        assert all(r > 0 for r in lengths)
        # Count monomials in the six-factor product directly, without the
        # convolution implementation used by the triage program.
        expected = Counter(sum(e) for e in product(*(range(r) for r in lengths)))
        assert counts == expected, (lam, mu, counts, expected)
        rows.append({"lambda": lam, "mu": mu, "q_integer_lengths": lengths,
                     "coefficients": [counts[i] for i in range(max(counts)+1)],
                     "nonempty_cells": sum(counts.values()), "cells": terms})
    # Historical output is a comparator only, never an input to derivation.
    oldpath = ROOT / "evidence/triage_symbolic.json"
    old = json.loads(oldpath.read_text())
    prior = {(tuple(r["lambda"]), tuple(r["mu"])): r for r in old["results"]}
    assert set(prior) == set(shapes)
    for row in rows:
        ref = prior[row["lambda"], row["mu"]]
        assert row["coefficients"] == ref["coefficients"]
        oldterms = {(tuple(t["sigma"]), tuple(t["pi"])):
                    (t["inversions"], t["h"], t["exponent"]) for t in ref["terms"]}
        newterms = {(c["sigma"], c["pi"]):
                    (c["nvariables"], c["h"], c["dimension"])
                    for c in row["cells"] if not c["empty"]}
        assert oldterms == newterms
    summary = {"job_id": JOB, "coefficient_ring": "Z", "shape_count": 55,
               "permutation_pairs": 144, "shape_pair_checks": 55*144,
               "empty_cells": empty_count, "nonempty_cells": 55*144-empty_count,
               "unit_pivot_equations": total_equations,
               "max_solution_polynomial_degree": max_degree,
               "all_sparse_entry_coefficients_one": True,
               "all_elimination_identities_verified_over_Z": True,
               "closed_variable_order_verified": True,
               "all_product_coefficient_identities": True,
               "all_prior_terms_match": True,
               "triage_json_sha256": hashlib.sha256(oldpath.read_bytes()).hexdigest(),
               "scope": "Exact finite certificates; theorem transfer in proof.md; fresh review pending"}
    report = dict(summary, augmented_matrices=matrices, results=rows)
    target = ROOT / "evidence/sparse_certificates.json"
    target.write_text(json.dumps(report, indent=2) + "\n")
    (ROOT / "evidence/sparse_summary.json").write_text(json.dumps(summary, indent=2)+"\n")
    table = ["# Complete k=3 coefficient census", "",
             "Coefficients are in ascending powers of q after division by q^9(q-1)^6.",
             "Generated by `python3 evidence/verify_sparse.py`. All 55 shapes are included.", "",
             "| lambda | mu | Six q-integer lengths | Nonempty cells | Coefficients |",
             "|---|---|---|---:|---|"]
    for row in rows:
        table.append("| " + " | ".join((str(row["lambda"]), str(row["mu"]),
                     str(row["q_integer_lengths"]), str(row["nonempty_cells"]),
                     str(row["coefficients"]))) + " |")
    (ROOT / "evidence/shape_table.md").write_text("\n".join(table) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
