#!/usr/bin/env python3
"""Reconstruct the complete gap-3 certificate from prime factorizations.

Run at the project root: python3 evidence/reconstruct_gap3.py
No CAS, floating point, random sampling, or imported earlier search code.
The proof of completeness is in five-prime-proof.md.
"""
from hashlib import sha256
from math import isqrt, prod
from pathlib import Path
import json
import platform

JOB = "newwin-00001-p16-research-ba4f5e168b06"
SOURCE_HASH = "8b4fed18ea31443b084f7ff6a5cca49f4221bce85a82b8c026ce64f0a125e6d2"


def prime_by_trial(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def sieve(bound):
    flags = [True] * (bound + 1)
    flags[:2] = [False, False]
    for p in range(2, isqrt(bound) + 1):
        if flags[p]:
            for j in range(p * p, bound + 1, p):
                flags[j] = False
    return [p for p in range(2, bound + 1) if flags[p]]


def factor(n):
    original = n
    fs = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            e = 0
            while n % d == 0:
                n //= d
                e += 1
            fs.append([d, e])
        d += 1
    if n > 1:
        fs.append([n, 1])
    assert prod(p ** e for p, e in fs) == original
    assert all(prime_by_trial(p) for p, _ in fs)
    return fs


def divisors_from_factors(fs):
    ds = [1]
    for p, e in fs:
        ds = [d * p ** j for d in ds for j in range(e + 1)]
    return sorted(ds)


def last_pair(prefix):
    A = prod(prefix)
    B = prod(p - 1 for p in prefix)
    c = 2 * B - A
    assert c > 0
    N = 2 * A * B - 3 * c
    assert N > 0
    fs = factor(N)
    ds = divisors_from_factors(fs)
    small = [u for u in ds if u * u <= N]
    # Independent direct divisor enumeration checks the factor expansion.
    assert small == [d for d in range(1, isqrt(N) + 1) if N % d == 0]
    checks = []
    integral = []
    ordered = []
    solutions = []
    for u in small:
        v = N // u
        xr, yr = (u + 2 * B) % c, (v + 2 * B) % c
        checks.append({"u": u, "v": v, "x_remainder": xr,
                       "y_remainder": yr})
        if xr or yr:
            continue
        x, y = (u + 2 * B) // c, (v + 2 * B) // c
        assert A * x * y - 2 * B * (x - 1) * (y - 1) == 3
        entry = {"u": u, "v": v, "x": x, "y": y}
        integral.append(entry)
        if not prefix[-1] < x < y:
            continue
        witnesses = []
        for z in (x, y):
            for d in range(2, isqrt(z) + 1):
                if z % d == 0:
                    witnesses.append({"number": z, "divisor": d,
                                      "cofactor": z // d})
                    break
        accepted = prime_by_trial(x) and prime_by_trial(y)
        assert accepted == (len(witnesses) == 0)
        ordered.append({**entry, "composite_witnesses": witnesses})
        if accepted:
            solutions.append(prefix + [x, y])
    # Separate exact enumeration without factoring N. The original equation
    # gives y=[2B(x-1)-3]/(cx-2B); y>x and cx-2B>0 imply cx<4B.
    direct_pairs = []
    direct_count = 0
    for x in range(prefix[-1] + 1, (4 * B - 1) // c + 1):
        direct_count += 1
        denominator = c * x - 2 * B
        if denominator <= 0:
            continue
        y, remainder = divmod(2 * B * (x - 1) - 3, denominator)
        if remainder == 0 and y > x:
            direct_pairs.append([x, y])
    assert direct_pairs == [[p["x"], p["y"]] for p in ordered]
    return {"prefix": prefix, "A": A, "B": B, "c": c, "N": N,
            "prime_factorization": fs, "small_divisors": small,
            "divisor_checks": checks, "integral_pairs": integral,
            "ordered_integral_pairs": ordered, "solutions": solutions,
            "direct_x_values_checked": direct_count,
            "direct_ordered_integral_pairs": direct_pairs}


def factor_text(fs):
    return " * ".join(str(p) if e == 1 else f"{p}^{e}" for p, e in fs)


def main():
    assert sha256(Path("source.md").read_bytes()).hexdigest() == SOURCE_HASH
    assert 5 * 7 * 11 * 13 * 17 < 2 * 4 * 6 * 10 * 12 * 16
    assert 3 * 15 ** 4 < 4 * 14 ** 4
    primes = sieve(46)  # The proved largest p3 cutoff is 47.
    assert primes == [p for p in range(2, 47) if prime_by_trial(p)]
    endpoints = {5: 47, 7: 23, 11: 17, 13: 15}
    assert list(endpoints) == [p for p in primes if 5 <= p < 15]
    cutoffs, rows = [], []
    for p, t in endpoints.items():
        left, right = 3 * p * t ** 3, 4 * (p - 1) * (t - 1) ** 3
        assert left <= right
        considered = [q for q in primes if p < q < t]
        retained = [q for q in considered if 3*p*q < 4*(p-1)*(q-1)]
        cutoffs.append({"p2": p, "p3_cutoff": t, "lhs": left,
                        "rhs": right, "considered_p3": considered,
                        "retained_p3": retained})
        rows.extend(last_pair([3, p, q]) for q in retained)
    assert len(rows) == 13
    ordered = [dict(prefix=r["prefix"], **pair) for r in rows
               for pair in r["ordered_integral_pairs"]]
    assert len(ordered) == 6
    assert all(pair["composite_witnesses"] for pair in ordered)
    assert all(not r["solutions"] for r in rows)
    # Compare reconstructed values with the earlier direct-divisor artifact.
    old = json.loads(Path("evidence/gap-divisor-check.json").read_text())
    old3 = [r for r in old["tables"] if r["gap"] == 3]
    assert [r["prefix"] for r in rows] == [r["prefix"] for r in old3]
    for new, prior in zip(rows, old3):
        for key in ("A", "B", "c", "N", "small_divisors", "solutions"):
            assert new[key] == prior[key]
        assert [(d["u"], d["v"], d["x_remainder"], d["y_remainder"])
                for d in new["divisor_checks"]] == [
               (d["u"], d["v"], d["x_remainder"], d["y_remainder"])
               for d in prior["divisor_checks"]]
    # Nonvacuous boundary control outside the five-prime theorem.
    control = last_pair([3, 7])
    assert control["solutions"] == [[3, 7, 13, 19]]
    out = {"job_id": JOB, "status": "exact_certificate_pending_fresh_review",
           "python": platform.python_version(), "source_sha256": SOURCE_HASH,
           "scope": "No five distinct odd primes have R-2*phi(R)=3.",
           "arithmetic": "exact integer factorization and divisor expansion",
           "cutoffs": cutoffs, "row_count": len(rows),
           "small_divisor_count": sum(len(r["small_divisors"]) for r in rows),
           "ordered_integral_pair_count": len(ordered),
           "direct_x_values_checked": sum(r["direct_x_values_checked"] for r in rows),
           "direct_x_enumeration_agrees": True,
           "ordered_integral_pairs": ordered, "rows": rows,
           "solutions": [], "agrees_with_triage": True,
           "four_prime_control": control,
           "limitations": "Completeness uses the written proof; this is not a referee report."}
    Path("evidence/gap3-factor-certificate.json").write_text(
        json.dumps(out, indent=2) + "\n")
    table = ["# Gap-3 factor certificate", "", "Generated by `reconstruct_gap3.py`.",
             "All arithmetic is exact; completeness is proved in `five-prime-proof.md`.",
             "", "For each prefix, A=product(p), B=product(p-1), c=2B-A, N=2AB-3c.",
             "The divisor column lists every positive u with u^2 <= N and u dividing N.",
             "An ordered pair satisfies p3 < x < y and x=(u+2B)/c, y=(N/u+2B)/c.",
             "", "| Prefix | A | B | c | N (prime factorization) | All small divisors u | Ordered integral (x,y) |",
             "|---|---:|---:|---:|---|---|---|"]
    for r in rows:
        pairs = "; ".join(f"({d['x']},{d['y']})" for d in r["ordered_integral_pairs"]) or "none"
        table.append(f"| {','.join(map(str,r['prefix']))} | {r['A']} | {r['B']} | {r['c']} | {r['N']} = {factor_text(r['prime_factorization'])} | {','.join(map(str,r['small_divisors']))} | {pairs} |")
    table += ["", "Exactly six ordered integral pairs survive; each has a composite member:", ""]
    for pair in ordered:
        w = pair["composite_witnesses"][0]
        table.append(f"- Prefix {tuple(pair['prefix'])}, (x,y)=({pair['x']},{pair['y']}): {w['number']}={w['divisor']}*{w['cofactor']}.")
    table += ["", "Integral pairs that violate p3 < x < y (also rejected):", ""]
    for r in rows:
        for d in r["integral_pairs"]:
            if not r["prefix"][-1] < d["x"] < d["y"]:
                table.append(f"- Prefix {tuple(r['prefix'])}: ({d['x']},{d['y']}).")
    table += ["", "The factors displayed as prime were checked by trial division through their integer square roots.",
              "Expanding their prime powers gives exactly the displayed small-divisor lists.",
              "There are " + str(out["small_divisor_count"]) + " small-divisor checks in the 13 rows.",
              "The JSON additionally records both congruence remainders for every divisor.",
              "Directly solving for y over the proved range p3 < x < 4B/c gives exactly the same six ordered pairs without factoring N.",
              "The same solver recovers the four-prime control (3,7,13,19), whose gap is 3.", ""]
    Path("evidence/gap3-factor-certificate.md").write_text("\n".join(table))
    print(json.dumps({k: out[k] for k in ("row_count", "small_divisor_count",
                     "ordered_integral_pair_count", "direct_x_values_checked",
                     "direct_x_enumeration_agrees", "solutions", "agrees_with_triage")}))


if __name__ == "__main__":
    main()
