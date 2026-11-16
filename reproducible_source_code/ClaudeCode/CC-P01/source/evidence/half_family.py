"""Whirling knight's tours with the least number of coils, built from stretchable rings   (Knuth, TAOCP 7.2.2.4, ex. 231(a)).

Python 3 standard library only.

  python half_family.py tours_half_coils.txt seeds_half_coils.txt            n = 0, 2 (mod 8): n/2 coils
  python half_family.py tours_plus2_coils.txt seeds_plus2_coils.txt          n = 4, 6 (mod 8): n/2 + 2 coils
  python half_family.py tours_odd_coils.txt seeds_odd_coils.txt              n = 1 (mod 4): (n+3)/2 coils, or (n+1)/2 if n = 1 (mod 24)
  ... -K 20                                                                  check 20 levels of each family (default 8)
  ... -n 1000 -o tour1000.txt                                                write the tour for one n

Data.  The first file holds a tour T for every admissible n below the seeds; its header gives the number of coils.
The second file holds, for six values N1 (one in each class modulo 24), a tour T1 of the N1 x N1 board that contains
the tour T0 of the central (N1-24) x (N1-24) board from the first file, except for one arc u -> v; the rest of T1 is
a path from u through all cells of the outer ring (depth < 12) to v.  Each ring adds 12 coils.

Construction.  With a = 19, h = N1/2, b = N1 - 19 and e >= 0, the board of side N1 + 24e is obtained from the board
of side N1 by inserting 6e, 12e, 6e rows and columns at the cuts a, h, b.  A ring cell z of the big board takes the
move of the ring cell pull(z) of T1, where pull undoes the insertion and maps an inserted row or column to one of the
3, 2, 3 rows or columns next to the cut, with the same residue modulo 3, 2, 3.  T_{e+1} is T_e (shifted by (12,12))
with the arc fwd(u) -> fwd(v) replaced by that ring path.

The function certify() checks the finite conditions (Z), (S), (W), (C) of the paper, which imply that T_k is a
whirling tour with N_k/2 coils for every k.  Independently, main() builds T_1..T_K and checks each one directly.
"""
import sys, math, argparse
from fractions import Fraction as F

W = 12
def load(file, coils=None):
    d = {}
    for line in open(file):
        if not line.strip(): continue
        head, t = line.strip().split(" tour=")
        n = int(head.split()[0][2:])
        d[n] = [tuple(map(int, s.split(","))) for s in t.split()]
        if coils is not None: coils[n] = int(head.split()[1][6:])
    return d

def check_tour(n, T, coils_claimed):
    """Exact check: all cells once, every step a counterclockwise knight move, winding number as claimed."""
    p = F(n - 1, 2)
    cells = {(i, j) for i in range(n) for j in range(n)}
    if n % 2: cells.discard((n // 2, n // 2))            # odd n: the central cell is removed
    ok = len(T) == len(cells) and set(T) == cells
    ray = (F(-1), F(1, 2 * n)); coils = 0
    for k in range(len(T)):
        (i, j), (i2, j2) = T[k], T[(k + 1) % len(T)]
        u, w = (i - p, j - p), (i2 - p, j2 - p)
        ok &= {abs(i - i2), abs(j - j2)} == {1, 2}
        ok &= u[0] * w[1] - w[0] * u[1] > 0
        if u[0] * ray[1] - ray[0] * u[1] > 0 and ray[0] * w[1] - w[0] * ray[1] > 0: coils += 1
    return ok and coils == coils_claimed

class Family:
    def __init__(self, T0, T1):
        self.N1 = N1 = max(max(v) for v in T1) + 1; self.N0 = max(max(v) for v in T0) + 1; assert N1 == self.N0 + 2 * W
        self.a, self.h, self.b = 19, N1 // 2, N1 - 19
        self.succ1 = succ1 = dict(zip(T1, T1[1:] + T1[:1]))
        depth = lambda v: min(v[0], v[1], N1 - 1 - v[0], N1 - 1 - v[1])
        self.ring = {v for v in succ1 if depth(v) < W}
        self.move = {v: (succ1[v][0] - v[0], succ1[v][1] - v[1]) for v in self.ring}
        us = [v for v in succ1 if v not in self.ring and succ1[v] in self.ring]
        vs = [succ1[v] for v in self.ring if succ1[v] not in self.ring]
        assert len(us) == 1 and len(vs) == 1, "the ring must be entered once and left once"
        self.u, self.v = us[0], vs[0]
        self.um = (succ1[self.u][0] - self.u[0], succ1[self.u][1] - self.u[1])
        succ0 = dict(zip(T0, T0[1:] + T0[:1]))
        # T1 = T0 shifted, minus the arc u -> v, plus the ring path
        for x, y in succ0.items():
            x, y = (x[0] + W, x[1] + W), (y[0] + W, y[1] + W)
            assert succ1[x] == y or (x, y) == (self.u, self.v)
        self.T = {0: succ0}
    def fwd(self, t, e):
        return t if t < self.a else t + 6 * e if t < self.h else t + 18 * e if t < self.b else t + 24 * e
    def pull(self, t, e):
        a, h, b = self.a, self.h, self.b
        if t < a: return t
        if t < a + 6 * e: return a - 3 + (t - a) % 3
        if t < h + 6 * e: return t - 6 * e
        if t < h + 18 * e: return h - 2 + (t - h - 6 * e) % 2
        if t < b + 18 * e: return t - 18 * e
        if t < b + 24 * e: return b + (t - b - 18 * e) % 3
        return t - 24 * e
    def levels(self, K):
        """Yield (k, successor map of T_k) for k = 1..K; only one level is kept in memory."""
        succ = self.T[0]
        for k in range(1, K + 1):
            e = k - 1; N = self.N1 + 24 * e
            succ = {(x[0] + W, x[1] + W): (y[0] + W, y[1] + W) for x, y in succ.items()}
            u = (self.fwd(self.u[0], e), self.fwd(self.u[1], e)); v = (self.fwd(self.v[0], e), self.fwd(self.v[1], e))
            assert succ[u] == v, f"level {k}: the arc to be replaced is missing"
            succ[u] = (u[0] + self.um[0], u[1] + self.um[1])
            for i in range(N):
                for j in range(N):
                    if min(i, j, N - 1 - i, N - 1 - j) < W:
                        m = self.move[(self.pull(i, e), self.pull(j, e))]
                        succ[(i, j)] = (i + m[0], j + m[1])
            yield k, succ
    @staticmethod
    def as_list(succ):
        out, cur = [], (0, 0)
        for _ in range(len(succ)): out.append(cur); cur = succ[cur]
        return out
    def tour(self, k):
        for kk, succ in self.levels(k): pass
        return self.as_list(succ)
    def certify(self):
        N1, a, h, b = self.N1, self.a, self.h, self.b
        succ1, move, u, v = self.succ1, self.move, self.u, self.v
        path, cur = [u], succ1[u]
        while cur != v: path.append(cur); cur = succ1[cur]
        path.append(v)
        assert set(path[1:-1]) == self.ring and len(path) == len(self.ring) + 2
        pos = {x: t for t, x in enumerate(path)}
        piece = lambda x, y: path[min(pos[x], pos[y]): max(pos[x], pos[y]) + 1]
        # (Z) the six zones
        zones = [(14, 21, 3), (h - 3, h + 3 + N1 % 2, 2), (N1 - 21, N1 - 14, 3)]      # the middle zone is symmetric
        for ax in (1, 0):                                    # ax = 1: columns; ax = 0: rows
            sh = lambda z, t: (z[0], z[1] + t) if ax else (z[0] + t, z[1])
            for A, B, tau in zones:
                assert B - A >= tau + 4 and not A <= u[ax] < B and not A <= v[ax] < B
                for z in self.ring:
                    if A <= z[ax] < B - tau: assert move[z] == move[sh(z, tau)], ("Z-a", z)
                    if A <= z[ax] < A + 2: assert all(A - 2 <= x[ax] < B for x in piece(z, sh(z, tau))), ("Z-b", z)
                    if B - 2 <= z[ax] < B: assert all(A <= x[ax] < B + 2 for x in piece(sh(z, -tau), z)), ("Z-c", z)
        assert 14 + 3 <= a <= 21 and N1 - 21 <= b <= N1 - 21 + 4          # the cuts lie in the zones
        # (S) the splice repeats one level up
        assert u[1] in (12, 13) and v[1] in (12, 13) and a + 6 <= u[0] < h and a + 6 <= v[0] < h
        us, vs = (u[0] - 6, u[1] - 12), (v[0] - 6, v[1] - 12)
        assert us in self.ring and succ1[us] == vs
        # (W) displacement of a cell relative to the pivot, per level: e * delta with delta in a box; delta x m >= 0
        def box(t):
            if t < a - 3: return (-12,)
            if t < a: return (-12, -6)
            if t < h - 2: return (-6,)
            if t < h: return (-6, 6)
            if t < b: return (6,)
            if t < b + 3: return (6, 12)
            return (12,)
        for x, m in list(move.items()) + [(u, self.um)]:
            for di in box(x[0]):
                for dj in box(x[1]):
                    assert di * m[1] - m[0] * dj >= 0, ("W", x)
        # (C) in the middle zone of the top side every move goes one column to the left
        assert all(move[(t, j)][1] == -1 for t in range(W) for j in range(h - 3, h + 3 + N1 % 2))
        return f"u={u} v={v}"

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("tours"); ap.add_argument("seeds"); ap.add_argument("-K", type=int, default=8)
    ap.add_argument("-n", type=int, default=None); ap.add_argument("-o", default=None)
    args = ap.parse_args()
    coils, scoils = {}, {}
    tours, seeds = load(args.tours, coils), load(args.seeds, scoils)
    for N1 in seeds: assert scoils[N1] == coils[N1 - 24] + 12
    if args.n is not None:
        n = args.n
        if n in tours: T, c = tours[n], coils[n]
        else:
            cand = [N1 for N1 in seeds if n > N1 and (n - N1) % 24 == 0]
            assert n in seeds or cand, "no tour or family for this n in these files"
            N1 = n if n in seeds else cand[0]; k = 1 + (n - N1) // 24
            fam = Family(tours[N1 - 24], seeds[N1]); T = fam.tour(k); c = coils[N1 - 24] + 12 * k
        ok = check_tour(n, T, c)
        print(f"n={n}: coils = {c} -> {'VALID' if ok else 'INVALID'}")
        if args.o: open(args.o, "w").write(f"n={n} coils={c} tour=" + " ".join(f"{i},{j}" for i, j in T) + "\n")
        sys.exit(0 if ok else 1)
    allok = True
    for n in sorted(tours):
        allok &= check_tour(n, tours[n], coils[n])
    print(f"explicit tours n = {', '.join(map(str, sorted(tours)))}: {'ALL VALID' if allok else 'SOME INVALID'}")
    for N1 in sorted(seeds):
        fam = Family(tours[N1 - 24], seeds[N1])
        info = fam.certify()
        ns = []
        for k, succ in fam.levels(args.K):
            n = N1 + 24 * (k - 1); allok &= check_tour(n, fam.as_list(succ), coils[N1 - 24] + 12 * k); ns.append(n)
        print(f"family {N1} + 24k ({scoils[N1]} + 12k coils): conditions (Z),(S),(W),(C) hold, {info}; "
              f"tours n = {ns[0]}, {ns[1]}, ..., {ns[-1]} checked directly: {'ALL VALID' if allok else 'SOME INVALID'}", flush=True)
    print("ALL VALID" if allok else "SOME TOUR IS INVALID")
