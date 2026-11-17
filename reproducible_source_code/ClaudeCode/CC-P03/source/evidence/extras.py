"""(1) Number N_k(q) of removable k-sets for odd q >= 7: N_k(q) = q * (W3_k - W2_k), where W3_k / W2_k count removable
k-sets inside units 0..2 / units 1..2 of the window model (sets are anchored at their first unit).
Cross-check N_2 against brute force (132 q) and N_1 = 12 q.
(2) Petersen graph: largest removable set of L(P) by exhaustive monotone search."""
import itertools
from snark_check import T, SW, unit, mul, power, trace_nonzero, line_graph, three_colorable
T2 = power(T, 2)
def removable(R):
    D = [unit(frozenset(e for u, e in R if u == i)) for i in range(3)]
    return not trace_nonzero(mul(mul(mul(mul(SW, D[0]), D[1]), D[2]), T2))
def counts(units):
    L = [(u, e) for u in units for e in range(12)]; c = {}
    def dfs(start, R):
        c[len(R)] = c.get(len(R), 0) + 1
        for k in range(start, len(L)):
            if removable(R + [L[k]]): dfs(k + 1, R + [L[k]])
    dfs(0, []); return c
W3, W2 = counts([0, 1, 2]), counts([1, 2])
N = {k: W3[k] - W2.get(k, 0) for k in W3 if k >= 1}
print("W3:", dict(sorted(W3.items()))); print("W2:", dict(sorted(W2.items())))
print("N_k(q)/q for k = 1..9:", [N[k] for k in sorted(N)], " total removable nonempty sets / q =", sum(N.values()))
# Petersen
P = [(i, (i + 1) % 5) for i in range(5)] + [(i, i + 5) for i in range(5)] + [(5 + i, 5 + (i + 2) % 5) for i in range(5)]
LE, inc = line_graph(P); nv = len(P)
def rem(R):
    Rs = set(R); return not three_colorable(nv, [LE[k] for k in range(len(LE)) if k not in Rs])
assert rem([])
best = [0, 0]
def dfs(start, R):
    if len(R) > best[0]: best[0], best[1] = len(R), 0
    if len(R) == best[0]: best[1] += 1
    for k in range(start, len(LE)):
        if rem(R + [k]): dfs(k + 1, R + [k])
dfs(0, [])
print(f"Petersen graph: L(P) has {nv} vertices and {len(LE)} edges; largest removable set {best[0]}, attained {best[1]} times")
