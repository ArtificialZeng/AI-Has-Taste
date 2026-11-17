"""Stretch a tour with the uniform field (1,2) and periodic wall layers from side n to side n + D.
Top and bottom layers: D/2 columns are inserted at x = a1 and D/2 at x = a2 = a1 + n/2 (periodic copies, period Px).
Left layer: D rows are inserted at y = b = n - 1 - 2*a1; right layer: D rows at y = b2 = 2*(n - 1 - a2) (period Py).
Interior cells follow the field.  The corner patches and the patches at the midpoints of the top and bottom walls
are moved rigidly.   python stretch2.py tourfile n a1 D [D ...] [--Px 4] [--Py 4] [--TL 5] [--SL 8]"""
import sys
from kx import crossing_pairs
from stretch import load, moves_of, cycles
FIELD = {(1, 2), (-1, -2)}
def stretch2(used, n, D, a1, Px=4, Py=4, TL=5, SL=8):
    h = n // 2; a2 = a1 + h; b = n - 1 - 2 * a1; b2 = 2 * (n - 1 - a2); N = n + D; H2 = D // 2
    mv = moves_of(used)
    def copyback(t, a, P):                  # t in an inserted block that starts at a: copy from [a - P, a)
        return t - P * ((t - a) // P + 1)
    def bx(X):
        if X < a1: return X
        if X < a1 + H2: return copyback(X, a1, Px)
        if X < a2 + H2: return X - H2
        if X < a2 + D: return copyback(X - H2, a2, Px)
        return X - D
    def by(Y, bb):
        if Y < bb: return Y
        if Y < bb + D: return copyback(Y, bb, Py)
        return Y - D
    new = set(); bad = 0
    for X in range(N):
        for Y in range(N):
            top, bot, left, right = Y >= N - TL, Y < TL, X < SL, X >= N - SL
            if top or bot or left or right:
                x = X if left else (X - D if right else bx(X))
                y = Y - D if top else (Y if bot else (by(Y, b) if left else by(Y, b2)))
                ms = mv[(x, y)]
            else: ms = FIELD
            for d in ms:
                X2, Y2 = X + d[0], Y + d[1]
                if not (0 <= X2 < N and 0 <= Y2 < N): bad += 1; continue
                new.add(frozenset(((X, Y), (X2, Y2))))
    deg = {}
    for e in new:
        for c in e: deg[c] = deg.get(c, 0) + 1
    badcells = [(X, Y) for X in range(N) for Y in range(N) if deg.get((X, Y), 0) != 2]
    return [tuple(e) for e in new], bad + len(badcells), badcells
if __name__ == "__main__":
    av = sys.argv[1:]; OPTS = ("--Px", "--Py", "--TL", "--SL")
    A = [a for k, a in enumerate(av) if not a.startswith("--") and not (k > 0 and av[k - 1] in OPTS)]
    opt = lambda nm, d: type(d)(av[av.index(nm) + 1]) if nm in av else d
    fn, n, a1 = A[0], int(A[1]), int(A[2]); used = load(fn); base = len(crossing_pairs(used))
    print(f"n={n}: cycles {cycles(used)[:5]}, crossings {base}")
    for D in map(int, A[3:]):
        new, bad, cells = stretch2(used, n, D, a1, opt("--Px", 4), opt("--Py", 4), opt("--TL", 5), opt("--SL", 8))
        cyc = cycles(new); cr = len(crossing_pairs(new))
        print(f"n={n+D}: inconsistent {bad} {cells[:4]}, cycles {len(cyc)} (largest {cyc[:4]}), crossings {cr} = {cr/(n+D):.2f} n, slope {(cr-base)/D:.3f}", flush=True)
