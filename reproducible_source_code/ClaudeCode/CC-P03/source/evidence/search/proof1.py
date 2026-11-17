"""(a) eventual period of Boolean powers of T; (b) symmetry facts; (c) for every odd q >= 5, all non-conflict pairs
(e in unit 0, f in unit delta) have cyclic distance <= D.  Uses representatives of T^k (period preserved, parity kept)."""
from transfer import T, mul, I, SW, unit, trace_nonzero, power, N
# (a) period
pw = [I]
for k in range(1, 400): pw.append(mul(pw[-1], T))
k0 = p = None
for a in range(400):
    for b in range(a + 1, 400):
        if pw[a] == pw[b]: k0, p = a, b - a; break
    if k0 is not None: break
print("T^k eventually periodic: T^%d = T^%d (k0=%d, p=%d)" % (k0, k0 + p, k0, p))
P2 = p if p % 2 == 0 else 2 * p; K = k0 + P2
def rep(k): return k if k < K else k0 + (k - k0) % P2
# (b) symmetry: SW T SW == T, SW U(R) SW == U(sigma R)
sig = {0: 1, 1: 0, 2: 2, 3: 3, 4: 4, 5: 5, 6: 9, 7: 10, 8: 11, 9: 6, 10: 7, 11: 8}
print("SW T SW == T:", mul(mul(SW, T), SW) == T)
import itertools
ok = all(mul(mul(SW, unit(frozenset(R))), SW) == unit(frozenset(sig[e] for e in R)) for k in range(0, 3) for R in itertools.combinations(range(12), k))
print("SW U(R) SW == U(sigma R) for |R| <= 2:", ok)
# (c) pairs: e in unit 0, f in unit delta; q = k1 + k2 + 2 with k1 = delta - 1, k2 = q - 1 - delta; same unit: delta = 0
U1 = {e: unit(frozenset([e])) for e in range(12)}
maxdist = 0; nc_by_dist = {}
for k1 in range(K):
    for k2 in range(K):
        if (k1 + k2) % 2 == 0: continue          # q odd
        q = k1 + k2 + 2
        if q < 5: continue
        A = pw[k1]; B = pw[k2]
        for e in range(12):
            left = mul(SW, U1[e])
            for f in range(12):
                M = mul(mul(mul(left, A), U1[f]), B)
                if not trace_nonzero(M):          # non-conflict (still uncolorable)
                    d = min(k1 + 1, k2 + 1)
                    nc_by_dist[d] = nc_by_dist.get(d, 0) + 1
                    maxdist = max(maxdist, d)
print("cyclic distances of non-conflict pairs in different units (over representatives):", sorted(nc_by_dist))
print("max cyclic distance D =", maxdist, " (K =", K, ")")
