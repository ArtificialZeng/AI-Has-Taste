#!/usr/bin/env python3
"""Exact exhaustive optimizer for the finite Erdős #1200 invariant.

The search proves that no cover has cost strictly below a supplied exact
witness.  It uses standard-library integer bit masks and Fraction arithmetic.
"""
from __future__ import annotations

import argparse
import json
import platform
import sys
import time
from fractions import Fraction
from math import prod
from pathlib import Path


def primes_upto(n: int) -> list[int]:
    out = []
    for q in range(2, n + 1):
        if all(q % d for d in range(2, int(q**0.5) + 1)):
            out.append(q)
    return out


def class_mask(nmax: int, p: int, a: int) -> int:
    return sum(1 << (n - 1) for n in range(1, nmax + 1) if n % p == a)


def witness_cost(witness: list[list[int]]) -> Fraction:
    return sum((Fraction(1, p) for p, _ in witness), Fraction())


def verify_witness(nmax: int, witness: list[list[int]]) -> tuple[bool, int]:
    ps = primes_upto(nmax)
    used = set()
    covered = 0
    for p, a in witness:
        if p not in ps or p in used or not 0 <= a < p:
            return False, covered
        used.add(p)
        covered |= class_mask(nmax, p, a)
    return covered == (1 << nmax) - 1, covered


def prove_no_cheaper(nmax: int, witness: list[list[int]]) -> dict:
    ok, covered = verify_witness(nmax, witness)
    if not ok:
        raise ValueError("supplied incumbent is not a valid cover")
    ps = primes_upto(nmax)
    full = (1 << nmax) - 1
    target = witness_cost(witness)
    scale = prod(ps)
    weights = [scale // p for p in ps]
    target_scaled = target * scale
    assert target_scaled.denominator == 1
    target_int = target_scaled.numerator
    masks = {(p, a): class_mask(nmax, p, a) for p in ps for a in range(p)}
    calls = pruned_budget = pruned_capacity = cache_hits = 0
    started = time.time()

    def capacity_cannot_beat(uncovered: int, avail: int, cost: int) -> bool:
        need = uncovered.bit_count()
        items = []
        for i, p in enumerate(ps):
            if (avail >> i) & 1:
                gain = max((uncovered & masks[p, a]).bit_count() for a in range(p))
                if gain:
                    items.append((Fraction(weights[i], gain), weights[i], gain))
        if sum(g for _, _, g in items) < need:
            return True
        items.sort()
        used_cost = 0
        for _, weight, gain in items:
            take = min(need, gain)
            # Compare cost + used_cost + take*weight/gain >= target.
            if (cost + used_cost - target_int) * gain + take * weight >= 0:
                return True
            if take == gain:
                used_cost += weight
            need -= take
            if not need:
                return False
        return True

    # Pack the 41-bit coverage mask and 13-bit availability mask into one
    # Python integer.  This is mathematically identical to a tuple key and
    # substantially reduces the memory of the complete failed-state table.
    seen: set[int] = set()

    def dfs(cov: int, avail: int, cost: int) -> bool:
        nonlocal calls, pruned_budget, pruned_capacity, cache_hits
        calls += 1
        key = cov | (avail << nmax)
        if key in seen:
            cache_hits += 1
            return False
        if cov == full:
            return cost < target_int
        if cost >= target_int:
            pruned_budget += 1
            return False
        unc = full ^ cov
        if capacity_cannot_beat(unc, avail, cost):
            pruned_capacity += 1
            return False

        # Each completion covers any fixed uncovered point n with the unique
        # class n mod p of some unused p.  Branching over all such p is complete.
        n = (unc & -unc).bit_length()
        branches = []
        for i, p in enumerate(ps):
            if (avail >> i) & 1 and cost + weights[i] < target_int:
                m = masks[p, n % p]
                branches.append(((unc & m).bit_count(), p, i, m))
        branches.sort(reverse=True)
        for _, _, i, m in branches:
            if dfs(cov | m, avail ^ (1 << i), cost + weights[i]):
                return True
        seen.add(key)
        return False

    cheaper_exists = dfs(0, (1 << len(ps)) - 1, 0)
    return {
        "N": nmax,
        "python": sys.version,
        "platform": platform.platform(),
        "primes": ps,
        "witness": witness,
        "witness_cost_numerator": target.numerator,
        "witness_cost_denominator": target.denominator,
        "witness_covered_mask": covered,
        "cheaper_cover_exists": cheaper_exists,
        "states_entered": calls,
        "failed_states_stored": len(seen),
        "cache_hits": cache_hits,
        "budget_prunes": pruned_budget,
        "capacity_prunes": pruned_capacity,
        "elapsed_seconds": time.time() - started,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=41)
    ap.add_argument("--witness", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    witness = json.loads(args.witness.read_text())["classes"]
    result = prove_no_cheaper(args.n, witness)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    raise SystemExit(1 if result["cheaper_cover_exists"] else 0)


if __name__ == "__main__":
    main()
