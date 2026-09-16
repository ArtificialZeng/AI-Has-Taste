#!/usr/bin/env python3
"""Independent exact triage test; no claim of mathematical acceptance.

Fix the first three primes and solve the final two by positive divisor pairs.
This does not import or execute the supplied recursive prime enumeration.
Completeness arguments are documented in triage-math.md.
"""
from fractions import Fraction
from math import isqrt, prod
from pathlib import Path
import hashlib
import json
import platform


def is_prime(n):
    return n >= 2 and all(n % d != 0 for d in range(2, isqrt(n) + 1))


def divisors(n):
    return [d for d in range(1, isqrt(n) + 1) if n % d == 0]


def complete_last_pair(prefix, gap):
    A = prod(prefix)
    B = prod(p - 1 for p in prefix)
    c = 2 * B - A
    assert c > 0
    N = 2 * A * B - c * gap
    assert N > 0
    rows = []
    hits = []
    for u in divisors(N):
        v = N // u
        x, rx = divmod(u + 2 * B, c)
        y, ry = divmod(v + 2 * B, c)
        accepted = (rx == 0 and ry == 0 and prefix[-1] < x < y
                    and is_prime(x) and is_prime(y))
        rows.append({"u": u, "v": v, "x_floor": x, "x_remainder": rx,
                     "y_floor": y, "y_remainder": ry, "accepted": accepted})
        if accepted:
            full = prefix + [x, y]
            assert prod(full) - 2 * prod(p - 1 for p in full) == gap
            hits.append(full)
    return {"prefix": prefix, "gap": gap, "A": A, "B": B, "c": c,
            "N": N, "small_divisors": [r["u"] for r in rows],
            "divisor_checks": rows, "solutions": hits}


def main():
    # If p2 >= 15, even four equal remaining factors cannot give H > 2.
    assert 3 * 15**4 <= 4 * 14**4
    assert Fraction(5*7*11*13*17, 4*6*10*12*16) < 2
    p2_values = [p for p in range(5, 15) if is_prime(p)]
    cutoffs = []
    triples = []
    for p in p2_values:
        # If p3 >= t, H <= (3p)/(2(p-1)) * (t/(t-1))^3.
        t = p + 1
        while 3*p*t**3 > 4*(p-1)*(t-1)**3:
            t += 1
        considered = [q for q in range(p + 1, t) if is_prime(q)]
        retained = [q for q in considered if 3*p*q < 4*(p-1)*(q-1)]
        triples.extend([[3, p, q] for q in retained])
        cutoffs.append({"p2": p, "p3_excluded_at_or_above": t,
                        "cutoff_lhs": 3*p*t**3,
                        "cutoff_rhs": 4*(p-1)*(t-1)**3,
                        "considered_p3": considered, "retained_p3": retained})
    tables = [complete_last_pair(t, e) for t in triples for e in (1, 3)]
    solutions = [hit for table in tables for hit in table["solutions"]]
    # Nonvacuous boundary test: the same two-prime solver must recover
    # the four-prime gap-3 radical identified directly by exact arithmetic.
    control = complete_last_pair([3, 7], 3)
    assert [3, 7, 13, 19] in control["solutions"]
    assert 3*7*13*19 - 2*(2*6*12*18) == 3
    source = Path("source.md")
    result = {
        "job_id": "newwin-00001-p16-triage-b3295de4c9e7",
        "kind": "exact_finite_triage_observation_not_referee_acceptance",
        "python": platform.python_version(),
        "arithmetic": "integers and Fraction only; no random seed",
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "scope": "five increasing odd primes beginning with 3; R-2phi(R) in {1,3}",
        "p2_values": p2_values, "p3_cutoffs": cutoffs,
        "triple_count": len(triples), "gap_table_count": len(tables),
        "divisor_pair_checks": sum(len(t["divisor_checks"]) for t in tables),
        "solutions": solutions, "tables": tables,
        "positive_control": control,
        "limitations": "Universal exponent reduction and completeness require written proof review; no novelty or acceptance certification."
    }
    Path("evidence/gap-divisor-check.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: result[key] for key in
                     ("triple_count", "gap_table_count", "divisor_pair_checks", "solutions")}))
    print("positive control recovered [3, 7, 13, 19]")


if __name__ == "__main__":
    main()
