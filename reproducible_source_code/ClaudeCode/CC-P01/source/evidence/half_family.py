"""Whirling knight's tours with the least number of coils, built from stretchable rings   (Knuth, TAOCP 7.2.2.4, ex. 231(a)).

Python 3 standard library only.

  python half_family.py tours_half_coils.txt seeds_half_coils.txt            n = 0, 2 (mod 8): n/2 coils
  python half_family.py tours_plus2_coils.txt seeds_plus2_coils.txt          n = 4, 6 (mod 8): n/2 + 2 coils
  python half_family.py tours_odd_coils.txt seeds_odd_coils.txt              n = 1 (mod 4): (n+3)/2 coils, or (n+1)/2 if n = 1 (mod 24)
  python half_family.py tours_odd3_coils.txt seeds_odd3_coils.txt            n = 3 (mod 4): (n+3)/2 coils, or (n+1)/2 if n = 19 (mod 24)
  ... -K 20                                                                  check 20 levels of each family (default 8)
  ... -n 1000 -o tour1000.txt                                                write the tour for one n

Data.  The first file holds a tour T for every admissible n below the seeds; its header gives the number of coils.
The second file holds, for six values N1 (one in each class modulo 24), a seed tour T1 of the N1 x N1 board.  T1 is
obtained from the tour T0 of the central (N1-24) x (N1-24) board (first file, shifted by (12,12)) by replacing
disjoint pieces Q_1..Q_r of T0 by disjoint paths P_1..P_r, where P_i has the same first and last cell as Q_i; the
paths P_i together visit all cells of the outer ring (depth < 12) and all cells of the pieces.
  * Without an entry omega= in the header, r = 1 and Q_1 is the single arc of T0 that is missing in T1.
  * With omega=D,L0,L1 let Omega be the set of inner cells of depth < D whose distance to the second nearest side
    of the board is in [L0, L1).  The pieces are the maximal subpaths of T0 all of whose arcs have an end in Omega,
    except those that are paths of T1 as well.
An entry shift=S moves the first and third zones and the cuts a, b by S cells towards the middle.

Construction.  With a = 19 + S, h = floor(N1/2), b = N1 - 19 - S and e >= 0, the board of side N1 + 24e is obtained
from the board of side N1 by inserting 6e, 12e, 6e rows and columns at the cuts a, h, b.  A ring cell z of the big
board takes the move of the ring cell pull(z) of T1, where pull undoes the insertion and maps an inserted row or
column to one of the 3, 2, 3 rows or columns next to the cut, with the same residue modulo 3, 2, 3.  A cell x of a
piece, other than its last cell, keeps its move in T1 at its new position fwd(x).  All other cells keep their moves
in T_e, shifted by (12,12).  This is T_{e+1}.

The function certify() checks the finite conditions (Z), (S), (W), (C) of the paper, which imply that T_k is a
whirling tour with c0 + 12k coils for every k.  Independently, main() builds T_1..T_K and checks each one directly.
"""
import sys, argparse
from fractions import Fraction as F

W = 12
def load(file, coils=None, opts=None):
    d = {}
    for line in open(file):
        if not line.strip(): continue
        head, t = line.strip().split(" tour=")
        n = int(head.split()[0][2:])
        d[n] = [tuple(map(int, s.split(","))) for s in t.split()]
        if coils is not None: coils[n] = int(head.split()[1][6:])
        if opts is not None: opts[n] = dict(tok.split("=") for tok in head.split()[2:])
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
    def __init__(self, T0, T1, shift=0, omega=None):
        self.N1 = N1 = max(max(v) for v in T1) + 1; self.N0 = max(max(v) for v in T0) + 1; assert N1 == self.N0 + 2 * W
        self.s = shift = int(shift); self.a, self.h, self.b = 19 + shift, N1 // 2, N1 - 19 - shift
        self.succ1 = succ1 = dict(zip(T1, T1[1:] + T1[:1]))
        succ0 = {(x[0] + W, x[1] + W): (y[0] + W, y[1] + W) for x, y in zip(T0, T0[1:] + T0[:1])}
        pred0 = {w: u for u, w in succ0.items()}
        depth = lambda v: min(v[0], v[1], N1 - 1 - v[0], N1 - 1 - v[1])
        self.ring = ring = {v for v in succ1 if depth(v) < W}
        # the pieces Q_i of T0 (shifted): maximal runs of the arcs in `cut`
        if omega is None:
            cut = {x for x in succ0 if succ1[x] != succ0[x]}; assert len(cut) == 1
        else:
            D, L0, L1 = map(int, omega.split(","))
            along = lambda v: max(min(v[0], N1 - 1 - v[0]), min(v[1], N1 - 1 - v[1]))
            Om = {v for v in succ0 if depth(v) < D and L0 <= along(v) < L1}
            cut = {x for x in succ0 if x in Om or succ0[x] in Om}            # tails of the arcs with an end in Omega
        self.pieces, self.paths = [], []
        for x in sorted(cut):
            if pred0[x] in cut: continue
            Q = [x]
            while Q[-1] in cut: Q.append(succ0[Q[-1]])
            P = [x, succ1[x]]                                                # the path of T1 that replaces Q
            while P[-1] in ring or P[-1] in cut: P.append(succ1[P[-1]])
            assert P[-1] == Q[-1], "a piece and the path that replaces it must have the same ends"
            if P != Q: self.pieces.append(Q); self.paths.append(P)           # a path of T0 that T1 keeps is not a piece
        cut = {x for Q in self.pieces for x in Q[:-1]}                       # the cells of the pieces other than their last cells
        assert all(succ1[x] == succ0[x] for x in succ0 if x not in cut), "T1 must keep all other arcs of T0"
        G = [x for P in self.paths for x in P]
        assert len(G) == len(set(G)) and set(G) == ring | {x for Q in self.pieces for x in Q}, "the paths must be disjoint and cover"
        self.G = set(G); self.last = {P[-1] for P in self.paths}
        self.move = {x: (succ1[x][0] - x[0], succ1[x][1] - x[1]) for x in self.G - self.last}
        self.cut = cut
        self.T = {0: dict(zip(T0, T0[1:] + T0[:1]))}
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
            for x in self.cut:                                      # the cells of the pieces, at their new positions
                z = (self.fwd(x[0], e), self.fwd(x[1], e)); m = self.move[x]
                succ[z] = (z[0] + m[0], z[1] + m[1])
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
        N1, a, h, b, s = self.N1, self.a, self.h, self.b, self.s
        succ1, move, ring, G = self.succ1, self.move, self.ring, self.G
        pos = {x: (i, t) for i, P in enumerate(self.paths) for t, x in enumerate(P)}
        def piece(x, y):
            assert pos[x][0] == pos[y][0], "the two cells must lie on the same path"
            P = self.paths[pos[x][0]]; return P[min(pos[x][1], pos[y][1]): max(pos[x][1], pos[y][1]) + 1]
        # (Z) the six zones
        assert N1 >= 52 + 2 * s, "the three zones must be apart"
        zones = [(14 + s, 21 + s, 3), (h - 3, h + 3 + N1 % 2, 2), (N1 - 21 - s, N1 - 14 - s, 3)]
        for ax in (1, 0):                                    # ax = 1: columns; ax = 0: rows
            sh = lambda z, t: (z[0], z[1] + t) if ax else (z[0] + t, z[1])
            side = lambda z: z[1 - ax] < W                   # which of the two sides that the zone crosses
            for A, B, tau in zones:
                assert B - A >= tau + 4
                for z in G:
                    if A <= z[ax] < B: assert z in ring, ("Z: a cell outside the ring lies in a zone", z)
                    if A <= z[ax] < B - tau: assert sh(z, tau) in G and move[z] == move[sh(z, tau)], ("Z-a", z)
                    if A + tau <= z[ax] < B: assert sh(z, -tau) in G, ("Z-a", z)
                    if A <= z[ax] < A + 2:
                        assert all(x in ring and side(x) == side(z) and A - 2 <= x[ax] < B for x in piece(z, sh(z, tau))), ("Z-b", z)
                    if B - 2 <= z[ax] < B:
                        assert all(x in ring and side(x) == side(z) and A <= x[ax] < B + 2 for x in piece(sh(z, -tau), z)), ("Z-c", z)
        assert 14 + s + 3 <= a <= 21 + s and N1 - 21 - s <= b <= N1 - 21 - s + 4          # the cuts lie in the zones
        # (S) every arc of a piece reappears in the ring of T1, and the four cells stay in one segment in each coordinate
        seg = lambda t: 0 if t < a else 1 if t < h else 2 if t < b else 3
        psi = lambda x: (self.fwd(x[0], 1) - W, self.fwd(x[1], 1) - W)
        for Q in self.pieces:
            for x, y in zip(Q, Q[1:]):
                assert psi(x) in ring and psi(y) in ring and succ1[psi(x)] == psi(y), ("S", x, y)
                for k in (0, 1):
                    assert seg(x[k]) == seg(y[k]) == seg(psi(x)[k]) == seg(psi(y)[k]), ("S", x, y)
        # (W) displacement of a cell relative to the pivot, per level: e * delta with delta in a box; delta x m >= 0
        def box(t):
            if t < a - 3: return (-12,)
            if t < a: return (-12, -6)
            if t < h - 2: return (-6,)
            if t < h: return (-6, 6)
            if t < b: return (6,)
            if t < b + 3: return (6, 12)
            return (12,)
        for x, m in move.items():
            for di in box(x[0]):
                for dj in box(x[1]):
                    assert di * m[1] - m[0] * dj >= 0, ("W", x)
        # (C) in the middle zone of the top side every move goes one column to the left
        assert all(move[(t, j)][1] == -1 for t in range(W) for j in range(h - 3, h + 3 + N1 % 2))
        r = len(self.pieces); k = sum(1 for P in self.paths if any(x in ring for x in P))
        if r == 1: return f"piece {self.pieces[0][0]}->{self.pieces[0][-1]}"
        return f"{r} pieces with {len(self.cut)} arcs, {k} of the new paths pass through the ring"

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("tours"); ap.add_argument("seeds"); ap.add_argument("-K", type=int, default=8)
    ap.add_argument("-n", type=int, default=None); ap.add_argument("-o", default=None)
    args = ap.parse_args()
    coils, scoils, opts = {}, {}, {}
    tours, seeds = load(args.tours, coils), load(args.seeds, scoils, opts)
    for N1 in seeds: assert scoils[N1] == coils[N1 - 24] + 12
    if args.n is not None:
        n = args.n
        if n in tours: T, c = tours[n], coils[n]
        else:
            cand = [N1 for N1 in seeds if n > N1 and (n - N1) % 24 == 0]
            assert n in seeds or cand, "no tour or family for this n in these files"
            N1 = n if n in seeds else cand[0]; k = 1 + (n - N1) // 24
            fam = Family(tours[N1 - 24], seeds[N1], **opts[N1]); T = fam.tour(k); c = coils[N1 - 24] + 12 * k
        ok = check_tour(n, T, c)
        print(f"n={n}: coils = {c} -> {'VALID' if ok else 'INVALID'}")
        if args.o: open(args.o, "w").write(f"n={n} coils={c} tour=" + " ".join(f"{i},{j}" for i, j in T) + "\n")
        sys.exit(0 if ok else 1)
    allok = True
    for n in sorted(tours):
        allok &= check_tour(n, tours[n], coils[n])
    print(f"explicit tours n = {', '.join(map(str, sorted(tours)))}: {'ALL VALID' if allok else 'SOME INVALID'}")
    for N1 in sorted(seeds):
        fam = Family(tours[N1 - 24], seeds[N1], **opts[N1])
        info = fam.certify()
        ns = []
        for k, succ in fam.levels(args.K):
            n = N1 + 24 * (k - 1); allok &= check_tour(n, fam.as_list(succ), coils[N1 - 24] + 12 * k); ns.append(n)
        shown = ", ".join(map(str, ns)) if len(ns) <= 3 else f"{ns[0]}, {ns[1]}, ..., {ns[-1]}"
        print(f"family {N1} + 24k ({scoils[N1]} + 12k coils): conditions (Z),(S),(W),(C) hold, {info}; "
              f"tours n = {shown} checked directly: {'ALL VALID' if allok else 'SOME INVALID'}", flush=True)
    print("ALL VALID" if allok else "SOME TOUR IS INVALID")
