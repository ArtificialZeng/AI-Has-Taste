"""Certificate program for the coil spectrum of the SYMMETRIC tours: for every n >= 6, every odd number of coils
between the least and the greatest one of the centrally symmetric tours occurs, with quarter-turn symmetry if 4 does
not divide n and with half-turn symmetry if 4 | n.  Uses half_family.py and spectrum_family.py.  Standard library only.

  python3 spectrum_sym_family.py [-K 2] [-K3 1] [--class N0]   check everything; build and check all towers with <= K rings
  python3 spectrum_sym_family.py -n 1001 -c 777 [-o file]      build one symmetric tour

Files: as for spectrum_family.py, with the symmetric fast families (tours_symmax_coils.txt, seeds_symmax_coils.txt),
seeds_sym_slow_on_fast.txt, rings_sym_slow.txt, bases_sym_spectrum.txt, bases_sym_spectrum_fast.txt,
tours_sym_spectrum_small.txt, tours_sym_spectrum_mid.txt, and for n = 3 (mod 4) tours_sym_coils.txt,
seeds_sym3_coils.txt, seeds_sym_fast_on_slow.txt.  Every tour and every tower is also checked for its symmetry.
"""
import sys, argparse, os
import half_family as hf
W = 12
MOV = ((1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1))
def L(n):                                                   # least number of coils of a centrally symmetric tour (odd)
    if n < 11: return {6: 5, 7: 5, 8: 7, 9: 7, 10: 7}[n]
    l = (n // 2 if n % 8 in (0, 2) else n // 2 + 2) if n % 2 == 0 else ((n + 1) // 2 if n % 24 in (1, 19) else (n + 3) // 2)
    return l | 1
def M(n):                                                   # greatest number of coils of a centrally symmetric tour (odd)
    if n < 10: return {6: 5, 7: 5, 8: 7, 9: 7}[n]
    return n - 1 if n % 2 == 0 else n - 2
ORDER = lambda n: 2 if n % 4 == 0 else 4                    # half turn if 4 | n, quarter turn otherwise
def rotations(x, N, order):
    out = [x]
    for _ in range(order - 1):
        x = (N - 1 - x[1], x[0]) if order == 4 else (N - 1 - x[0], N - 1 - x[1]); out.append(x)
    return out
def load_all(file):
    """Lines 'n=.. coils=.. tour=i,j i,j ...' or 'n=.. coils=.. moves=0123...' (moves from the cell (0,0), digits index MOV)."""
    out = []
    for line in open(file):
        if not line.strip(): continue
        head = line.split(); n, c = int(head[0][2:]), int(head[1][6:])
        if head[2].startswith("moves="):
            T, cur = [], (0, 0)
            for ch in head[2][6:]: T.append(cur); m = MOV[int(ch)]; cur = (cur[0] + m[0], cur[1] + m[1])
            assert cur == (0, 0), "the moves must close the tour"
        else:
            T = [tuple(map(int, s.split(","))) for s in line.strip().split(" tour=")[1].split()]
        out.append((n, c, T))
    return out
succ_of = lambda T: dict(zip(T, T[1:] + T[:1]))
def wrap(fam, succ, e):
    """Put the ring of the family `fam`, stretched e times, around the tour `succ` of side fam.N0 + 24e."""
    N = fam.N1 + 24 * e
    s = {(x[0] + W, x[1] + W): (y[0] + W, y[1] + W) for x, y in succ.items()}
    f = lambda x: (fam.fwd(x[0], e), fam.fwd(x[1], e))
    for Q in fam.pieces:                                   # the tour inside must contain the stretched pieces
        for x, y in zip(Q, Q[1:]): assert s[f(x)] == f(y), "the tour inside does not contain a piece of the ring"
    for x in fam.cut:
        z = f(x); m = fam.move[x]; s[z] = (z[0] + m[0], z[1] + m[1])
    for i in range(N):
        for j in range(N):
            if min(i, j, N - 1 - i, N - 1 - j) < W:
                m = fam.move[(fam.pull(i, e), fam.pull(j, e))]; s[(i, j)] = (i + m[0], j + m[1])
    return s

class Class:
    def __init__(self, N0, tmax, cmax, smax, omax, sslow, rslow, bases):
        self.N0 = N0; self.L0, self.M0 = L(N0), M(N0)
        self.F = hf.Family(tmax[N0 - 24], smax[N0], **omax[N0]); assert cmax[N0 - 24] + 24 == self.M0
        self.X = smax[N0]                                                  # the fast seed tour, M0 coils
        self.S = hf.Family(self.F.tour(2), sslow[N0 + 48])                 # slow seed around the fast tower tour of side N0+24
        self.R = hf.Family(self.X, rslow[N0 + 24])                         # ring R around X (not stretched)
        self.bases = dict(bases); self.bases[self.M0] = self.X
    def certify(self):
        N0, F, S, R = self.N0, self.F, self.S, self.R
        infoF, infoS = F.certify(), S.certify()                            # (Z'),(S'),(W'),(C') and (Z),(S),(W),(C)
        order = ORDER(N0)
        assert not S.fast and len(S.pieces) == order and all(len(Q) == 2 for Q in S.pieces), "the slow seed must drop the rotations of one arc"
        Qd, = [Q for Q in S.pieces if all(x[1] in (W, W + 1) for x in Q)]   # the one on the left edge
        d0, d1 = [(x[0] - W, x[1] - W) for x in Qd]                        # delta in the board of side N0+24
        assert {tuple(Q) for Q in S.pieces} == set(zip(rotations(Qd[0], S.N1, order), rotations(Qd[1], S.N1, order)))
        for T_, n_ in ((self.X, N0), (hf.Family.as_list(S.succ1), N0 + 48), (hf.Family.as_list(R.succ1), N0 + 24), (F.tour(2), N0 + 24)):
            assert hf.symmetric(n_, T_, order), "a seed tour is not symmetric"
        # (dagger) zeta (called delta here) lies on the left edge between the cuts a and h of the slow seed, and the fast tower tours contain
        #     its translates: on the left side of the fast seed tour the move of delta's column is constant from
        #     delta's row (pulled back) to the cut of the fast seed
        assert d0[1] in (0, 1) and d1[1] in (0, 1) and S.a <= d0[0] + W < S.h and S.a <= d1[0] + W < S.h
        sX = succ_of(self.X); hF = F.h; mv = (d1[0] - d0[0], d1[1] - d0[1])
        assert all((sX[(i, d0[1])][0] - i, sX[(i, d0[1])][1] - d0[1]) == mv for i in range(min(d0[0], hF - 4), hF)), "condition (dagger) fails"
        assert d0[0] + 2 < hF + 24, "delta must lie above the block of the fast tower tour"
        # R: one dropped arc alpha, ring adds 12 coils, contains delta
        assert len(R.pieces) == order and all(len(Q) == 2 for Q in R.pieces)
        alphas = [[(x[0] - W, x[1] - W) for x in Q] for Q in R.pieces]; a0, a1 = alphas[0]
        T_R = hf.Family.as_list(R.succ1); assert hf.check_tour(N0 + 24, T_R, self.M0 + 12) and R.succ1[d0] == d1
        # bases
        P2 = [[(F.fwd(x[0], 1) - W, F.fwd(x[1], 1) - W) for x in Q] for Q in F.pieces]
        for c in range(self.L0, self.M0 + 1, 2):
            assert c in self.bases, f"no base with {c} coils for side {N0}"
            T = self.bases[c]; s = succ_of(T)
            assert hf.check_tour(N0, T, c) and hf.symmetric(N0, T, order), f"base {N0}, {c} is not a symmetric tour with {c} coils"
            assert all(s[x] == y for x, y in alphas), f"base {N0}, {c} lacks the arcs xi"
            if c >= self.M0 - 11: assert all(s[x] == y for Q in P2 for x, y in zip(Q, Q[1:])), f"base {N0}, {c} lacks the pieces of the fast ring"
        assert self.M0 - self.L0 >= 11
        return f"fast seed: {infoF}; slow seed: {infoS}; alpha {a0}->{a1}, delta {d0}->{d1} and their rotations; {(self.M0 - self.L0) // 2 + 1} bases"
    def tower(self, c, a, b):
        """Successor map of the tour: base with c coils, b fast rings, then a slow rings."""
        s = succ_of(self.bases[c]); k = a + b
        if b == 0:
            if k >= 1: s = wrap(self.R, s, 0)
            for e in range(0, k - 1): s = wrap(self.S, s, e)
        else:
            assert c >= self.M0 - 11
            for e in range(1, b + 1): s = wrap(self.F, s, e)
            for e in range(b - 1, k - 1): s = wrap(self.S, s, e)
        return s
    def plan(self, k):
        """All (coils, c, a, b) that the towers with k rings give."""
        out = {}
        for c in range(self.L0, self.M0 + 1, 2): out[c + 12 * k] = (c, k, 0)
        for c in range(self.M0 - 10, self.M0 + 1, 2):
            for b in range(1, k + 1): out.setdefault(c + 12 * k + 12 * b, (c, k - b, b))
        return out

class Class3:
    """n = 3 (mod 4): base side N0 in 123..143.  Rings: the multi-piece slow ring of half_family (seed of side N0+24
    around the tour U_0 of side N0 with the least number of coils), a fast ring around its tour U_1 (seed of side
    N0+48), and the fast ring of the fast family around the bases with the greatest numbers of coils."""
    def __init__(self, N0, tmax, cmax, smax, omax, t3, s3, o3, fp, ofp, slow, fast):
        self.N0 = N0; self.L0, self.M0 = L(N0), M(N0)
        self.Om = hf.Family(t3[N0], s3[N0 + 24], **o3[N0 + 24])            # slow seed (U_0, U_1), several pieces
        self.FP = hf.Family(s3[N0 + 24], fp[N0 + 48], **ofp[N0 + 48])      # fast seed (U_1, .)
        N1 = N0 - 72; self.FF = hf.Family(tmax[N1 - 24], smax[N1], **omax[N1]); assert cmax[N1 - 24] + 24 * 4 == self.M0
        self.X = self.FF.tour(4)                                           # the fast tower tour of side N0, M0 coils
        self.A = dict(slow); self.A[self.L0] = t3[N0]                      # bases with the pieces of the slow ring: L0 <= c <= M0-4
        self.B = dict(fast); self.B[self.M0] = self.X                      # bases with the pieces of the fast ring: M0-15 <= c <= M0
    def certify(self):
        N0, Om, FP, FF = self.N0, self.Om, self.FP, self.FF
        infoO, infoP, infoF = Om.certify(), FP.certify(), FF.certify()
        assert FP.fast and not Om.fast and FF.fast
        for T_, n_ in ((self.X, N0), (hf.Family.as_list(Om.succ1), N0 + 24), (hf.Family.as_list(FP.succ1), N0 + 48)):
            assert hf.symmetric(n_, T_, 4), "a seed tour is not symmetric"
        # (ddagger) the pieces of the fast ring around U_1 lie in the top right corner of U_1, among its ring cells, in rows
        #     above the first cut and columns beyond the last cut of the slow seed; there the ring is the same at all levels
        N1 = N0 + 24
        for Q in FP.pieces:                                 # each piece, turned into the top right corner
            ok = False
            for r in range(4):
                Qr = [rotations(x, FP.N1, 4)[r] for x in Q]
                ok |= all(min(x[0] - W, x[1] - W, N1 - 1 - (x[0] - W), N1 - 1 - (x[1] - W)) < W and x[0] - W < Om.a and x[1] - W >= Om.b
                          and x[0] < FP.h <= x[1] for x in Qr)
            assert ok, "condition (ddagger) fails"
        PO = [[(x[0] - W, x[1] - W) for x in Q] for Q in Om.pieces]
        PF = [[(FF.fwd(x[0], 4) - W, FF.fwd(x[1], 4) - W) for x in Q] for Q in FF.pieces]
        for bases, lo, hi, P, what in ((self.A, self.L0, self.M0 - 4, PO, "slow"), (self.B, self.M0 - 15, self.M0, PF, "fast")):
            for c in range(lo | 1, hi + 1, 2):
                assert c in bases, f"no base with {c} coils and the pieces of the {what} ring for side {N0}"
                T = bases[c]; s = succ_of(T)
                assert hf.check_tour(N0, T, c) and hf.symmetric(N0, T, 4), f"base {N0}, {c} is not a symmetric tour with {c} coils"
                assert all(s[x] == y for Q in P for x, y in zip(Q, Q[1:])), f"base {N0}, {c} lacks the pieces of the {what} ring"
        return (f"slow seed: {infoO}; fast seed around U_1: {infoP}; fast family: {infoF}; "
                f"{(self.M0 - 4 - self.L0) // 2 + 1} bases with the pieces of the slow ring and 8 with those of the fast ring")
    def tower(self, c, a, b, pure=False):
        """Base with c coils; then a slow rings and b fast rings around them (a >= 1), or, with pure=True, b fast rings."""
        if pure:
            assert a == 0 and c >= self.M0 - 15
            s = succ_of(self.B[c])
            for e in range(4, 4 + b): s = wrap(self.FF, s, e)
        else:
            assert (a >= 1 or b == 0) and c <= self.M0 - 4
            s = succ_of(self.A[c])
            for e in range(0, a): s = wrap(self.Om, s, e)
            for e in range(a - 1, a - 1 + b): s = wrap(self.FP, s, e)
        return s
    def towers(self, k):
        """All towers with k rings: (coils, c, a, b, pure)."""
        if k == 0: return [(c, c, 0, 0, False) for c in range(self.L0, self.M0 - 3, 2)] + [(c, c, 0, 0, True) for c in range(self.M0 - 14, self.M0 + 1, 2)]
        out = [(c + 12 * k + 12 * b, c, k - b, b, False) for c in range(self.L0, self.M0 - 3, 2) for b in range(0, k)]
        return out + [(c + 24 * k, c, 0, k, True) for c in range(self.M0 - 14, self.M0 + 1, 2)]
    def plan(self, k):
        out = {}
        for coils, c, a, b, pure in self.towers(k): out.setdefault(coils, (c, a, b, pure))
        return out

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-K", type=int, default=2, help="check all towers with at most K rings (n not 3 mod 4)")
    ap.add_argument("-K3", type=int, default=1, help="the same for n = 3 (mod 4)")
    ap.add_argument("--class", dest="cls", type=int, default=None)
    ap.add_argument("-n", type=int, default=None); ap.add_argument("-c", type=int, default=None); ap.add_argument("-o", default=None)
    ap.add_argument("--dir", default=os.path.dirname(os.path.abspath(__file__)))
    args = ap.parse_args(); D = args.dir + "/"
    cmax, sc, omax, o3, ofp = {}, {}, {}, {}, {}
    tmax, smax = hf.load(D + "tours_symmax_coils.txt", cmax), hf.load(D + "seeds_symmax_coils.txt", sc, omax)
    sslow, rslow = hf.load(D + "seeds_sym_slow_on_fast.txt"), hf.load(D + "rings_sym_slow.txt")
    t3, s3 = hf.load(D + "tours_sym_coils.txt"), hf.load(D + "seeds_sym3_coils.txt", None, o3)
    fp = hf.load(D + "seeds_sym_fast_on_slow.txt", None, ofp)
    bases, fastb = {}, {}
    for n, c, T in load_all(D + "bases_sym_spectrum.txt"): bases.setdefault(n, []).append((c, T))
    for n, c, T in load_all(D + "bases_sym_spectrum_fast.txt"): fastb.setdefault(n, []).append((c, T))
    classes = [N0 for N0 in range(48, 72) if N0 % 4 != 3]; classes3 = list(range(123, 144, 4))
    make = lambda N0: Class(N0, tmax, cmax, smax, omax, sslow, rslow, bases[N0])
    make3 = lambda N0: Class3(N0, tmax, cmax, smax, omax, t3, s3, o3, fp, ofp, bases[N0], fastb[N0])
    if args.n is not None:
        n, c = args.n, args.c; assert L(n) <= c <= M(n) and c % 2 == 1, "need an odd c with L(n) <= c <= M(n)"
        if n % 4 != 3:
            assert n >= 48, "for n < 48 see tours_spectrum_small.txt"
            N0 = 48 + (n - 48) % 24; k = (n - N0) // 24; cl = make(N0); cl.certify()
            c0, a, b = cl.plan(k)[c]; T = hf.Family.as_list(cl.tower(c0, a, b)); what = f"{b} fast and then {a} slow rings"
        else:
            assert n >= 123, "for n < 123 see tours_spectrum_small.txt and tours_spectrum_mid.txt"
            N0 = 123 + (n - 123) % 24; k = (n - N0) // 24; cl = make3(N0); cl.certify()
            c0, a, b, pure = cl.plan(k)[c]; T = hf.Family.as_list(cl.tower(c0, a, b, pure)); what = f"{a} slow and then {b} fast rings"
        ok = hf.check_tour(n, T, c) and hf.symmetric(n, T, ORDER(n))
        print(f"n={n}, {c} coils: base of side {N0} with {c0} coils, {what} -> {'VALID' if ok else 'INVALID'}")
        if args.o: open(args.o, "w").write(f"n={n} coils={c} tour=" + " ".join(f"{i},{j}" for i, j in T) + "\n")
        sys.exit(0 if ok else 1)
    allok = True
    if args.cls is None:
        for file, ns, text in (("tours_sym_spectrum_small.txt", range(6, 48), "every n from 6 to 47"),
                               ("tours_sym_spectrum_mid.txt", range(51, 120, 4), "every n = 3 (mod 4) from 51 to 119")):
            seen = {}
            for n, c, T in load_all(D + file):
                allok &= hf.check_tour(n, T, c) and hf.symmetric(n, T, ORDER(n)); seen.setdefault(n, set()).add(c)
            for n in ns: allok &= seen.get(n, set()) >= set(range(L(n), M(n) + 1, 2))
            print(f"{file}: a symmetric tour for {text} and every odd number of coils from L(n) to M(n) "
                  f"({sum(len(v) for v in seen.values())} tours): {'ALL VALID' if allok else 'SOMETHING IS MISSING OR INVALID'}", flush=True)
    for N0 in classes:
        if args.cls is not None and N0 != args.cls: continue
        cl = make(N0); info = cl.certify(); cnt = 0
        for k in range(0, args.K + 1):
            n = N0 + 24 * k; plan = cl.plan(k)
            allok &= set(plan) == set(range(L(n), M(n) + 1, 2))            # every odd number of coils from L(n) to M(n)
            # every tower with k rings, not only one for each number of coils
            todo = [(c, k, 0) for c in range(cl.L0, cl.M0 + 1, 2)] + [(c, k - b, b) for c in range(cl.M0 - 10, cl.M0 + 1, 2) for b in range(1, k + 1)]
            for c, a, b in todo:
                T = hf.Family.as_list(cl.tower(c, a, b)); allok &= hf.check_tour(n, T, c + 12 * a + 24 * b) and hf.symmetric(n, T, ORDER(n)); cnt += 1
        print(f"class {N0} + 24k: {info}; all {cnt} towers with at most {args.K} rings checked directly, sides {N0}..{N0 + 24 * args.K}: "
              f"{'ALL VALID' if allok else 'SOME INVALID'}", flush=True)
    for N0 in classes3:
        if args.cls is not None and N0 != args.cls: continue
        cl = make3(N0); info = cl.certify(); cnt = 0
        for k in range(0, args.K3 + 1):
            n = N0 + 24 * k; tw = cl.towers(k)
            allok &= {t[0] for t in tw} == set(range(L(n), M(n) + 1, 2))
            for coils, c, a, b, pure in tw:
                T = hf.Family.as_list(cl.tower(c, a, b, pure)); allok &= hf.check_tour(n, T, coils) and hf.symmetric(n, T, 4); cnt += 1
        print(f"class {N0} + 24k: {info}; all {cnt} towers with at most {args.K3} rings checked directly, sides {N0}..{N0 + 24 * args.K3}: "
              f"{'ALL VALID' if allok else 'SOME INVALID'}", flush=True)
    print("ALL VALID" if allok else "SOMETHING IS INVALID")
    sys.exit(0 if allok else 1)
