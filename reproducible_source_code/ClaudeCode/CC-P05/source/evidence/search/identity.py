"""check: in every closed 8x8 knight's tour, classes D, I, K, L, N (Knuth's letters) contain exactly 8 moves in total"""
import random
from ortools.sat.python import cp_model
from classes import classes, edges, idx, orbit
letter = {0: "A", 8: "D", 12: "I", 13: "K", 5: "L", 14: "N"}            # from Knuth's figure: 00-12 A, 03-15 D, 12-24 I, 12-31 K, 02-21 L, 12-33 N
five = [8, 12, 13, 5, 14]
ck = {(1, 2), (2, 1), (1, 5), (2, 6), (5, 1), (6, 2), (5, 6), (6, 5)}
assert all(sum(1 for c in e if c in ck) == 1 for k in five for e in classes[k])          # each move of the five classes has exactly one end in ck
nb = lambda c: [e for e in edges if c in e]
assert all({orbit[e] for e in nb(c)} == {0, *five} for c in ck)                            # the moves at a ck cell: one class A move, the rest in the five classes
counts = []
for seed in range(20):
    md = cp_model.CpModel(); X = {e: md.NewBoolVar("") for e in edges}; arcs = []
    for (a, b), v in X.items():
        f = md.NewBoolVar(""); g = md.NewBoolVar(""); md.Add(f + g == v); arcs += [(idx[a], idx[b], f), (idx[b], idx[a], g)]
    md.AddCircuit(arcs)
    rnd = random.Random(seed); md.Maximize(sum(rnd.randint(-5, 5) * v for v in X.values()))
    s = cp_model.CpSolver(); s.parameters.max_time_in_seconds = 5; s.parameters.num_workers = 8; s.parameters.random_seed = seed; s.Solve(md)
    used = [e for e, v in X.items() if s.Value(v)]
    counts.append(tuple(sum(1 for e in used if orbit[e] == k) for k in five))
print("D I K L N counts in 20 random tours:", counts)
print("sums:", sorted({sum(c) for c in counts}))
