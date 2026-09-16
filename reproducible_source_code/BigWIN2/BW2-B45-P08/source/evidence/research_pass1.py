#!/usr/bin/env python3
"""Deterministic screening for the n=9 three-voter boundary and I_{5,1}.

This is a Z3 discovery/screening computation, not an UNSAT certificate generator.
Every reported SAT profile is recounted independently from the solver model.
"""

import argparse
import hashlib
import itertools
import json
import random
import time

import z3


N = 9
PAIRS = list(itertools.combinations(range(N), 2))


def tournament_bits(profile):
    positions = [{v: k for k, v in enumerate(order)} for order in profile]
    return tuple(sum(p[i] < p[j] for p in positions) >= 2 for i, j in PAIRS)


def solve_margin1(bits, voters, time_limit):
    """Find voters orders with exactly (voters+1)/2 supporters per arc."""
    x = [[z3.Bool(f"x_{p}_{i}_{j}") for i, j in PAIRS]
         for p in range(voters)]
    pair_index = {e: k for k, e in enumerate(PAIRS)}
    solver = z3.Solver()

    # On every triple, exclude the two cyclic orientations.  A complete
    # orientation with no directed triangle is a strict total order.
    for p in range(voters):
        for a, b, c in itertools.combinations(range(N), 3):
            ab = x[p][pair_index[a, b]]
            ac = x[p][pair_index[a, c]]
            bc = x[p][pair_index[b, c]]
            solver.add(z3.Or(z3.Not(ab), z3.Not(bc), ac))
            solver.add(z3.Or(ab, bc, z3.Not(ac)))

    target = (voters + 1) // 2
    for k, bit in enumerate(bits):
        literals = [x[p][k] if bit else z3.Not(x[p][k])
                    for p in range(voters)]
        solver.add(z3.PbEq([(lit, 1) for lit in literals], target))

    solver.set(timeout=max(1, round(1000 * time_limit)), random_seed=0)
    started = time.time()
    status = solver.check()
    wall = time.time() - started
    if status == z3.unsat:
        return "INFEASIBLE", None, wall
    if status != z3.sat:
        return "UNKNOWN", None, wall
    solution = solver.model()

    orders = []
    for p in range(voters):
        wins = [0] * N
        for k, (i, j) in enumerate(PAIRS):
            if z3.is_true(solution.eval(x[p][k], model_completion=True)):
                wins[i] += 1
            else:
                wins[j] += 1
        # In a transitive tournament, earlier vertices have more wins.
        orders.append(tuple(sorted(range(N), key=lambda v: -wins[v])))
    return "FEASIBLE", orders, wall


def recount(bits, orders):
    pos = [{v: k for k, v in enumerate(o)} for o in orders]
    expected = (len(orders) + 1) // 2
    counts = []
    for bit, (i, j) in zip(bits, PAIRS):
        count_ij = sum(p[i] < p[j] for p in pos)
        count = count_ij if bit else len(orders) - count_ij
        counts.append(count)
    return all(c == expected for c in counts), counts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--samples", type=int, default=5000)
    ap.add_argument("--seed", type=int, default=20260906)
    ap.add_argument("--limit", type=float, default=3.0,
                    help="per-instance CP-SAT seconds")
    ap.add_argument("--boundary-target", type=int, default=20)
    ap.add_argument("--output", default="evidence/research_pass1_results.json")
    args = ap.parse_args()

    rng = random.Random(args.seed)
    seen = set()
    records = []
    screening_unknowns = []
    tallies = {"draws": 0, "distinct_labeled": 0, "i31_sat": 0,
               "i31_unsat": 0, "i31_unknown": 0, "i51_sat": 0,
               "i51_unsat": 0, "i51_unknown": 0}
    started = time.time()

    identity = tuple(range(N))
    for draw in range(args.samples):
        source_profile = [identity]
        for _ in range(2):
            order = list(range(N))
            rng.shuffle(order)
            source_profile.append(tuple(order))
        bits = tournament_bits(source_profile)
        tallies["draws"] += 1
        if bits in seen:
            continue
        seen.add(bits)
        tallies["distinct_labeled"] += 1

        s3, p3, w3 = solve_margin1(bits, 3, args.limit)
        if s3 in ("OPTIMAL", "FEASIBLE"):
            ok3, _ = recount(bits, p3)
            assert ok3
            tallies["i31_sat"] += 1
            continue
        if s3 != "INFEASIBLE":
            tallies["i31_unknown"] += 1
            bitstring = "".join("1" if b else "0" for b in bits)
            screening_unknowns.append({
                "sha256_bitstring": hashlib.sha256(bitstring.encode()).hexdigest(),
                "upper_triangle_bits": bitstring,
                "source_three_profile": source_profile,
                "i31_status": s3,
                "i31_wall_seconds": w3,
            })
            continue
        tallies["i31_unsat"] += 1

        s5, p5, w5 = solve_margin1(bits, 5, args.limit)
        if s5 in ("OPTIMAL", "FEASIBLE"):
            ok5, counts5 = recount(bits, p5)
            assert ok5 and set(counts5) == {3}
            tallies["i51_sat"] += 1
        elif s5 == "INFEASIBLE":
            tallies["i51_unsat"] += 1
        else:
            tallies["i51_unknown"] += 1
        bitstring = "".join("1" if b else "0" for b in bits)
        records.append({
            "sha256_bitstring": hashlib.sha256(bitstring.encode()).hexdigest(),
            "upper_triangle_bits": bitstring,
            "source_three_profile": source_profile,
            "i31_status": s3,
            "i31_wall_seconds": w3,
            "i51_status": s5,
            "i51_wall_seconds": w5,
            "i51_profile": p5,
        })
        if len(records) >= args.boundary_target:
            break

    result = {
        "scope": "deterministic labeled random-profile screen; not isomorphism-deduplicated or exhaustive",
        "n": N,
        "seed": args.seed,
        "requested_samples": args.samples,
        "per_instance_limit_seconds": args.limit,
        "elapsed_seconds": time.time() - started,
        "tallies": tallies,
        "boundary_records": records,
        "i31_screening_unknowns": screening_unknowns,
        "limitations": [
            "Z3 INFEASIBLE is used only to select screening instances; no DRAT/LRAT proof is emitted.",
            "Only explicit SAT profiles and independent arc recounts are positive certificates.",
            "The sample is not the official 254-class catalogue and cannot decide the frozen claim.",
        ],
    }
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
        f.write("\n")
    print(json.dumps({"tallies": tallies, "records": len(records),
                      "elapsed_seconds": result["elapsed_seconds"]}, indent=2))


if __name__ == "__main__":
    main()
