"""Path structure of two periodic matchings on the strands (indexed by integers k).
A matching is (modulus m, dict residue -> offset): strand k is joined to k + off[k mod m].
union_paths returns (number of infinite paths, number of finite cycles per common period)."""
from math import gcd
def lcm(a, b): return a * b // gcd(a, b)
def union_paths(M1, M2):
    (m1, o1), (m2, o2) = M1, M2; m = lcm(m1, m2)
    seen = set(); inf = 0; fin = 0
    for k0 in range(m):
        if k0 in seen: continue
        k = k0; steps = 0
        while True:
            seen.add(k % m)
            k += o1[k % m1]; seen.add(k % m)
            k += o2[k % m2]; steps += 1
            if k % m == k0: break
            assert steps < 100 * m
        if k == k0: fin += 1
        else: inf += abs(k - k0) // m
    return inf, fin
A_TOP = (2, {0: 3, 1: -3})            # top pattern A for even n: even k ~ k + 3
B_TOP = (2, {0: -5, 1: 5})            # top pattern B: even k ~ k - 5
A_BOT = (2, {0: 3, 1: -3})            # bottom pattern A: even k ~ k + 3
B_BOT = (2, {0: -5, 1: 5})            # bottom pattern B: even k ~ k - 5
def shifted(M, c):
    m, o = M; return (m, {(r + c) % m: o[r] for r in o})
if __name__ == "__main__":
    print("top A with bottom A:", union_paths(A_TOP, A_BOT), " top A with bottom B:", union_paths(A_TOP, B_BOT),
          " top B with bottom A:", union_paths(B_TOP, A_BOT), " top B with bottom B:", union_paths(B_TOP, B_BOT))
    from states2 import enumerate_states
    for P, maxcost in ((4, 10), (6, 11), (8, 16)):
        cb = enumerate_states((2, 1), P, 10, maxcost, F=4, limit=300000, tl=200)
        print(f"shallow wall, period {P}, cost <= {maxcost}: {len(cb.found)} matchings")
        for key, (cost, used) in sorted(cb.found.items(), key=lambda t: (t[1][0], str(t[0]))):
            if key is None: continue
            S = (P, dict(key)); out = []
            for c in range(lcm(P, 2)):
                for nm, T in (("A", A_TOP), ("B", B_TOP)):
                    inf, fin = union_paths(T, shifted(S, c))
                    if fin == 0 and inf % 2 == 0 and inf > 0: out.append(f"{nm}/shift {c}: {inf} paths")
            if out: print(f"  cost {cost} offsets {sorted(set(S[1].values()))} {S[1]}: " + "; ".join(out))
