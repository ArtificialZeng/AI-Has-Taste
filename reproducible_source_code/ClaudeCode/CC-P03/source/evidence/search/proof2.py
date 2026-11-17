"""All valid deletion sets inside a window of 3 units (units 0,1,2; twist before unit 0; T^(q-3) = T^2 for every odd q >= 7).
Valid = trace(SW D0 D1 D2 T^2) == 0. Validity is monotone (subsets of valid sets are valid), so DFS with pruning."""
from transfer import T, mul, SW, unit, trace_nonzero, power
from functools import lru_cache
T2 = power(T, 2)
assert power(T, 4) == T2
@lru_cache(maxsize=None)
def U(R): return unit(R)
def valid(R):
    parts = [frozenset(e for (u, e) in R if u == i) for i in range(3)]
    M = mul(mul(mul(mul(SW, U(parts[0])), U(parts[1])), U(parts[2])), T2)
    return not trace_nonzero(M)
L = [(u, e) for u in range(3) for e in range(12)]
best = 0; count = {}; opt = []
def dfs(start, R):
    global best
    n = len(R); count[n] = count.get(n, 0) + 1
    if n > best: best = n; opt.clear()
    if n == best: opt.append(tuple(R))
    for k in range(start, len(L)):
        R2 = R + [L[k]]
        if valid(R2): dfs(k + 1, R2)
dfs(0, [])
print("valid sets in a 3-unit window, by size:", dict(sorted(count.items())))
print("maximum size:", best, "; number of maximum sets:", len(opt))
anchored = [R for R in opt if any(u == 0 for u, e in R)]
print("maximum sets meeting unit 0 (one per rotation class on the cycle):", len(anchored))
for R in anchored: print("  ", R)
