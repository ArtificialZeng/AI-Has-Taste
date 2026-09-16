#!/usr/bin/env python3
"""Exact reconstruction of the 126 local templates in the TP4 route.

This is a coverage/counting certificate, not a universal sign certificate.
It uses only integer arithmetic except for one exact SymPy polynomial-identity
check for the exceptional cancellation (m,L)=(5,(3,4,5,6)).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import random
from itertools import combinations, permutations
from pathlib import Path


W1 = (1, 1)
W2 = (1, 3, 2)
H2 = (7, 10, 4)
W3 = (1, 7, 12, 6)
WITNESS_ROOTS = (2, 3, 5, 7, 11, 13)
LOCAL_COLUMNS = tuple(combinations(range(7), 4))


def parity_sign(p: tuple[int, ...]) -> int:
    inversions = sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4))
    return -1 if inversions % 2 else 1


SIGNED_PERMUTATIONS = tuple((p, parity_sign(p)) for p in permutations(range(4)))


def det4(a):
    return sum(
        sign * a[0][p[0]] * a[1][p[1]] * a[2][p[2]] * a[3][p[3]]
        for p, sign in SIGNED_PERMUTATIONS
    )


def poly_mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def g_polynomial(indices, roots):
    out = [1]
    for i in indices:
        out = poly_mul(out, [1, roots[i]])
    return out


def shifted_coefficient(poly, degree, shift):
    j = degree - shift
    return poly[j] if 0 <= j < len(poly) else 0


def subsets_through(m, maximum):
    return tuple(s for size in range(maximum + 1) for s in combinations(range(m), size))


def configuration_specs(m):
    """Yield (sets, weights, shifts) for every summand with union exactly [m]."""
    universe = set(range(m))
    subs1, subs2, subs3 = subsets_through(m, 1), subsets_through(m, 2), subsets_through(m, 3)

    # T1 = D(G0, x Q1, x G0, x^2 H2)
    for I in subs1:
        for H in subs2:
            if set(I) | set(H) == universe:
                yield (I, (), H), (W1[len(I)], 1, H2[len(H)]), (0, 1, 1, 2)

    # T2 = D(G0, x Q1, x G0, x^3 Q3)
    for I in subs1:
        for K in subs3:
            if set(I) | set(K) == universe:
                yield (I, (), K), (W1[len(I)], 1, W3[len(K)]), (0, 1, 1, 3)

    # T3 = D(G0, x Q1, x^2 Q2, x^2 H2)
    for I in subs1:
        for J in subs2:
            for H in subs2:
                if set(I) | set(J) | set(H) == universe:
                    yield (I, J, H), (W1[len(I)], W2[len(J)], H2[len(H)]), (0, 1, 2, 2)

    # T4 = D(G0, x Q1, x^2 Q2, x^3 Q3)
    for I in subs1:
        for J in subs2:
            for K in subs3:
                if set(I) | set(J) | set(K) == universe:
                    yield (I, J, K), (W1[len(I)], W2[len(J)], W3[len(K)]), (0, 1, 2, 3)


def structural_possible(m, L):
    """Test whether any local determinant has a support-perfect-matching."""
    for sets, _, shifts in configuration_specs(m):
        lows = shifts
        highs = (m,) + tuple(shifts[i + 1] + m - len(sets[i]) for i in range(3))
        for assignment in permutations(range(4)):
            if all(lows[row] <= L[assignment[row]] <= highs[row] for row in range(4)):
                return True
    return False


def vector_add(*vectors):
    out = {}
    for scale, vector in vectors:
        for key, value in vector.items():
            out[key] = out.get(key, 0) + scale * value
    return {key: value for key, value in out.items() if value}


def verify_row_reduction():
    """Derive A_{n+t} in the formal basis x^a G_j for t=0,1,2,3."""
    rows = [{(0, 0): 1}]
    current = rows[0]
    for t in range(3):
        following = {}
        for (a, j), coefficient in current.items():
            for key, multiplier in (
                ((a, j), a + 1),
                ((a + 1, j), t + 1 - a + j),
                ((a + 1, j + 1), j + 1),
            ):
                following[key] = following.get(key, 0) + coefficient * multiplier
        current = {key: value for key, value in following.items() if value}
        rows.append(current)

    expected = [
        {(0, 0): 1},
        {(0, 0): 1, (1, 0): 1, (1, 1): 1},
        {(0, 0): 1, (1, 0): 4, (1, 1): 3,
         (2, 0): 1, (2, 1): 3, (2, 2): 2},
        {(0, 0): 1, (1, 0): 11, (1, 1): 7,
         (2, 0): 11, (2, 1): 22, (2, 2): 12,
         (3, 0): 1, (3, 1): 7, (3, 2): 12, (3, 3): 6},
    ]
    assert rows == expected

    s1 = vector_add((1, rows[1]), (-1, rows[0]))
    s2 = vector_add((1, rows[2]), (-1, rows[0]), (-3, s1))
    s3 = vector_add((1, rows[3]), (-1, rows[0]), (-7, s1), (-4, s2))
    assert s1 == {(1, 0): 1, (1, 1): 1}
    assert s2 == {(1, 0): 1, (2, 0): 1, (2, 1): 3, (2, 2): 2}
    assert s3 == {(2, 0): 7, (2, 1): 10, (2, 2): 4,
                  (3, 0): 1, (3, 1): 7, (3, 2): 12, (3, 3): 6}
    return rows


def local_term(sets, weights, shifts, L, roots, polynomial_cache):
    m = len(roots)
    multiplier = 1
    for selected, weight in zip(sets, weights):
        multiplier *= weight
        for i in selected:
            multiplier *= 1 + roots[i]
    polynomials = [polynomial_cache[tuple(range(m))]]
    polynomials.extend(
        polynomial_cache[tuple(i for i in range(m) if i not in selected)]
        for selected in sets
    )
    matrix = [
        [shifted_coefficient(polynomials[row], degree, shifts[row]) for degree in L]
        for row in range(4)
    ]
    return multiplier * det4(matrix)


def aggregate_template(m, L, roots):
    """Evaluate the full grouped coefficient Psi_m(L) exactly at integer roots."""
    assert len(roots) == m
    cache = {
        selected: g_polynomial(selected, roots)
        for size in range(m + 1)
        for selected in combinations(range(m), size)
    }
    total = 0
    for sets, weights, shifts in configuration_specs(m):
        total += local_term(sets, weights, shifts, L, roots, cache)
    return total


def exceptional_symbolic_cancellation():
    """Prove exactly that the only structurally possible excluded slot vanishes."""
    import sympy as sp

    m, L = 5, (3, 4, 5, 6)
    roots = sp.symbols("r0:5")
    value = aggregate_template(m, L, roots)
    return sp.Poly(value, *roots).is_zero


def stress_vectors():
    vectors = [
        [1] * 6,
        [1, 2, 4, 8, 16, 32],
        [1, 10, 100, 1000, 10000, 100000],
        [1, 1, 1, 1, 1, 1000000],
        [1, 1, 1, 100, 10000, 1000000],
    ]
    rng = random.Random(260829224)
    vectors.extend([[rng.randint(1, 1000) for _ in range(6)] for _ in range(20)])
    return vectors


def build_manifest():
    rows = verify_row_reduction()
    assert exceptional_symbolic_cancellation()

    templates, excluded, counts = [], [], []
    for m in range(7):
        roots = WITNESS_ROOTS[:m]
        surviving = 0
        for L in LOCAL_COLUMNS:
            value = int(aggregate_template(m, L, roots))
            item = {"m": m, "L": list(L), "template_id": f"m{m}-L{''.join(map(str, L))}"}
            if value:
                assert structural_possible(m, L)
                surviving += 1
                item.update({"witness_roots": list(roots), "exact_witness_value": str(value)})
                templates.append(item)
            else:
                if structural_possible(m, L):
                    assert (m, L) == (5, (3, 4, 5, 6))
                    reason = "symbolic-cancellation"
                else:
                    reason = "identically-zero-support"
                item["reason"] = reason
                excluded.append(item)
        counts.append(surviving)
    assert counts == [1, 3, 9, 19, 25, 34, 35]
    assert len(templates) == 126 and len(excluded) == 119

    negative = []
    vectors = stress_vectors()
    for vector_number, vector in enumerate(vectors):
        for template in templates:
            m, L = template["m"], tuple(template["L"])
            value = aggregate_template(m, L, tuple(vector[:m]))
            if value < 0:
                negative.append({"vector": vector_number, "m": m, "L": list(L), "value": str(value)})
    assert not negative

    return {
        "schema_version": 1,
        "scope": "Exact exhaustive reconstruction of the 126 nonzero grouped local-coefficient templates; not a universal sign certificate and not a TP4 proof.",
        "consecutive_minor_domain": {
            "parameters": "integers n>=0 and 0<=k<=n",
            "rows": "(n,n+1,n+2,n+3)",
            "columns": "(k,k+1,k+2,k+3)",
            "minor": "D_K(A_n,A_{n+1},A_{n+2},A_{n+3}), K={k,k+1,k+2,k+3}",
        },
        "formal_row_expansions": [
            {f"x^{a}G_{j}": coefficient for (a, j), coefficient in sorted(row.items())}
            for row in rows
        ],
        "row_reduction": {
            "Q1": "G0+G1",
            "Q2": "G0+3G1+2G2",
            "H2": "7G0+10G1+4G2",
            "Q3": "G0+7G1+12G2+6G3",
            "identity": "D=D(G0,xQ1,xG0+x^2Q2,x^2H2+x^3Q3)=T1+T2+T3+T4",
        },
        "grouping": {
            "indices": "U subset [n], m=|U|<=6, L a four-subset of {0,...,6}",
            "identity": "D=sum_U sum_L Psi_U(L) det(T_fU(L,K))",
            "symmetry": "Psi_U(L) is invariant under relabelling U, hence template (m,L)",
            "definition": "Psi is the sum of the four exact subset expansions T1--T4 implemented by aggregate_template",
        },
        "survivor_counts_by_m": counts,
        "total_survivors": len(templates),
        "total_excluded": len(excluded),
        "templates": templates,
        "excluded": excluded,
        "exact_stress_test": {
            "vectors": vectors,
            "template_evaluations": len(vectors) * len(templates),
            "negative_values": negative,
            "interpretation": "finite exact observations only; they do not prove positivity for all positive roots",
        },
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    manifest = build_manifest()
    encoded = json.dumps(manifest, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(encoded, encoding="utf-8")
        print(f"wrote {args.output}")
        print(f"sha256 {hashlib.sha256(encoded.encode()).hexdigest()}")
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
