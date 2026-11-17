"""Closed knight's tours of the n x n board with 7.5 n + 13 crossings, for every even n >= 30.

A crossing is a pair of moves of the tour whose segments (between the centres of the cells) meet at a point
interior to both.  The best construction in print has 12 n + O(1) crossings.

The tour T_n is built from the description in the paper (function `tour`):
  * the field: the cells away from the walls are joined to (x+1, y+2) and (x-1, y-2);
  * pattern A along the top wall, B and A along the bottom wall, a pattern of period 2 along the left and right walls;
  * 179 cells near the corners and near the middle of the bottom wall (the patches) have the moves of the cell at the
    same place, relative to the nearest corner or to the column n/2, in the tour of side 40 in tour40.txt.
For n >= 40 the tour is also built in a second way, by inserting periods into T_40 or T_42 (function `stretch`).

  python3 crossing_tours.py 100              build T_100, check that it is a closed tour, count its crossings
  python3 crossing_tours.py --range 30 500   the same for every even n in the range
  python3 crossing_tours.py --patterns 40 500  check that the two constructions agree
  python3 crossing_tours.py --joins 30 120   check that the joins of the strands of T_n are exactly those listed in Lemma 6
                                             (Table 1 and the five rules with their ranges), that every other cell lies on
                                             one join, that the passes are those of Table 2, and the statements about the
                                             patches and the boxes that the proof uses
  python3 crossing_tours.py --arith 30 3000  from the list of joins of Lemma 6 alone, without building a tour: the strands
                                             form a single cycle, with the passes of Table 2 (the arithmetic of Lemma 7)
  python3 crossing_tours.py --steps 40 120   check that T_{n+8} runs through the strands in the same cyclic order as
                                             T_n, with 24 more strands
  python3 crossing_tours.py --variant 48 600 the variant with 43 n / 6 + 24 crossings, n = 48, 60, 72, ...
  python3 crossing_tours.py --write 64 t64.txt   write T_64 as a list of moves x,y-x,y
  python3 crossing_tours.py --file t64.txt 64    check a tour given as a file
Standard library only."""
import sys, os, time
HERE = os.path.dirname(os.path.abspath(__file__))
F2 = frozenset({(1, 2), (-1, -2)})
def load(fn):
    return [tuple(tuple(int(v) for v in c.split(",")) for c in t.split("-")) for t in open(fn).read().split()]
def moves_of(edges):
    mv = {}
    for a, b in edges:
        mv.setdefault(a, set()).add((b[0] - a[0], b[1] - a[1])); mv.setdefault(b, set()).add((a[0] - b[0], a[1] - b[1]))
    return mv
# ---------------------------------------------------------------- the description of the paper
def left_pattern(x, y):
    """moves of the cell (x, y) of the left wall pattern, x = 0..5"""
    e = y % 2 == 0
    return [{(1, 2), (2, 1)}, {(-1, -2), (1, 2)} if e else {(-1, -2), (2, 1)}, {(-2, -1), (-1, -2)} if e else {(-2, -1), (1, -2)},
            {(-2, -1), (1, 2)} if e else {(-1, 2), (1, 2)}, set(F2), set(F2)][x]
def right_pattern(d, y):
    """moves of the cell (n-1-d, y) of the right wall pattern, d = 0..5"""
    e = y % 2 == 0
    return [{(-2, -1), (-1, -2)}, {(-2, -1), (1, 2)} if e else {(-1, -2), (1, 2)}, {(-1, 2), (2, 1)} if e else {(1, 2), (2, 1)},
            {(-1, -2), (1, -2)} if e else {(-1, -2), (2, 1)}, set(F2), set(F2)][d]
def prescribed(n):
    """items (i)-(iv) of the paper: dict cell -> set of moves; the cells of the patches are absent"""
    h = n // 2; pr = {}
    for x in range(6, n - 6):
        for y in range(3, n - 3): pr[(x, y)] = set(F2)                              # (i) the field
    for x in range(4, n - 4): pr[(x, n - 3)] = set(F2)
    for x in list(range(2, h - 3)) + list(range(h, n - 4)): pr[(x, 2)] = set(F2)
    for x in range(3, n - 5):                                                        # (ii) top wall: pattern A
        pr[(x, n - 2)] = {(2, 1), (-1, -2)}; pr[(x + 2, n - 1)] = {(-2, -1), (-1, -2)}
    for x in range(5, h - 4):                                                        # (iii) bottom wall: pattern B, then A
        pr[(x, 0)] = {(-2, 1), (1, 2)}; pr[(x - 2, 1)] = {(2, -1), (1, 2)}
    for x in range(h - 1, n - 5):
        pr[(x, 0)] = {(2, 1), (1, 2)}; pr[(x + 2, 1)] = {(-2, -1), (1, 2)}
    for y in range(8, n - 8):                                                        # (iv) left and right walls
        for d in range(6): pr[(d, y)] = left_pattern(d, y); pr[(n - 1 - d, y)] = right_pattern(d, y)
    return pr
_T40 = []
def tour(n, n0=40):
    """T_n (n even, n >= 30) from the description; the patches are taken from the tour of side n0 (40, or 42 = T_42)"""
    assert n % 2 == 0 and n >= 30, "n must be even and at least 30"
    if not _T40: _T40.append([tuple(sorted(e)) for e in load(os.path.join(HERE, "tour40.txt"))])
    base = _T40[0] if n0 == 40 else tour(n0)
    if n == n0 == 40: return list(base)
    h, h0 = n // 2, n0 // 2; mv0 = moves_of(base); pr = prescribed(n); mv = dict(pr)
    for x in range(n):
        for y in range(n):
            if (x, y) in pr: continue
            middle = (y == 0 and h - 4 <= x <= h - 2) or (y == 1 and h - 6 <= x <= h) or (y == 2 and h - 3 <= x <= h - 1)
            if middle: x0 = x - h + h0                                                 # the 13 cells near the middle of the bottom wall
            else: x0 = x if x < h else x - (n - n0)                                    # relative to the nearest corner
            y0 = y if y < h else y - (n - n0)
            mv[(x, y)] = mv0[(x0, y0)]
    edges = set()
    for c, ms in mv.items():
        for d in ms: edges.add(frozenset((c, (c[0] + d[0], c[1] + d[1]))))
    return [tuple(sorted(e)) for e in edges]
def patch_cells(n):
    pr = prescribed(n); return [(x, y) for x in range(n) for y in range(n) if (x, y) not in pr]
# ---------------------------------------------------------------- the second construction: inserting periods
def stretch(base, n0, D, a1=10, P=4, TL=5, SL=8, Prow=None):
    """the configuration of side n0 + D obtained from a tour of side n0: D/2 columns are inserted at x = a1 and at
    x = a1 + n0/2 in the rows near the top and bottom walls, D rows at y = n0 - 1 - 2 a1 near the left wall and at
    y = n0 - 2 - 2 a1 near the right wall; an inserted cell copies the cell P places before it; the cells that are not
    within TL rows of the top or bottom wall or SL columns of the left or right wall follow the field"""
    h = n0 // 2; a2 = a1 + h; b = n0 - 1 - 2 * a1; b2 = 2 * (n0 - 1 - a2); N = n0 + D; H2 = D // 2
    mv = moves_of(base); Prow = Prow or P
    back = lambda t, a, q=P: t - q * ((t - a) // q + 1)
    def bx(X):
        if X < a1: return X
        if X < a1 + H2: return back(X, a1)
        if X < a2 + H2: return X - H2
        if X < a2 + D: return back(X - H2, a2)
        return X - D
    def by(Y, bb):
        if Y < bb: return Y
        if Y < bb + D: return back(Y, bb, Prow)
        return Y - D
    new = set(); bad = 0
    for X in range(N):
        for Y in range(N):
            top, bot, left, right = Y >= N - TL, Y < TL, X < SL, X >= N - SL
            if top or bot or left or right:
                x = X if left else (X - D if right else bx(X))
                y = Y - D if top else (Y if bot else (by(Y, b) if left else by(Y, b2)))
                ms = mv[(x, y)]
            else: ms = F2
            for d in ms:
                c2 = (X + d[0], Y + d[1])
                if not (0 <= c2[0] < N and 0 <= c2[1] < N): bad += 1; continue
                new.add(frozenset(((X, Y), c2)))
    deg = {}
    for e in new:
        for c in e: deg[c] = deg.get(c, 0) + 1
    bad += sum(1 for X in range(N) for Y in range(N) if deg.get((X, Y), 0) != 2)
    return [tuple(sorted(e)) for e in new], bad
def tour_by_insertion(n):
    """the second construction, n >= 40: periods inserted into T_40 (4 | n) or T_42"""
    n0 = 40 if n % 4 == 0 else 42
    if n == n0: return tour(n0)
    edges, bad = stretch(tour(n0), n0, n - n0)
    assert bad == 0, "the stretched configuration is not consistent"
    return edges
_V = []
def variant(n):
    """a tour of side n = 48 + 12 j with 43 n / 6 + 24 crossings (side walls with a pattern of period 6)"""
    assert n >= 48 and (n - 48) % 12 == 0, "n must be 48 + 12 j"
    if not _V: _V.append(load(os.path.join(HERE, "variant48.txt")))
    if n == 48: return [tuple(sorted(e)) for e in _V[0]]
    edges, bad = stretch(_V[0], 48, n - 48, a1=12, Prow=6)
    assert bad == 0, "the stretched configuration is not consistent"
    return edges
# ---------------------------------------------------------------- checks
def sequence(edges, n):
    """the cells in the order of the tour, starting at (0,0); None if the moves are not one closed knight's tour of the board"""
    adj = {}
    for a, b in edges:
        if (abs(a[0] - b[0]), abs(a[1] - b[1])) not in ((1, 2), (2, 1)): return None
        adj.setdefault(a, []).append(b); adj.setdefault(b, []).append(a)
    if len(adj) != n * n or any(len(v) != 2 for v in adj.values()): return None
    if any(not (0 <= x < n and 0 <= y < n) for (x, y) in adj): return None
    seq = []; prev = None; cur = (0, 0)
    while True:
        seq.append(cur); nxt = adj[cur][0] if adj[cur][0] != prev else adj[cur][1]
        prev, cur = cur, nxt
        if cur == (0, 0): break
    return seq if len(seq) == n * n else None
def crossings(edges):
    """number of pairs of moves whose segments meet at a point interior to both (exact integer arithmetic)"""
    def orient(p, q, r):
        v = (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0]); return (v > 0) - (v < 0)
    box = {}
    for k, (a, b) in enumerate(edges): box.setdefault((min(a[0], b[0]), min(a[1], b[1])), []).append(k)
    cnt = 0
    for k, (a, b) in enumerate(edges):
        x0, y0 = min(a[0], b[0]), min(a[1], b[1])
        for dx in range(-2, 3):
            for dy in range(-2, 3):
                for k2 in box.get((x0 + dx, y0 + dy), ()):
                    if k2 <= k: continue
                    c, d = edges[k2]
                    if a in (c, d) or b in (c, d): continue
                    if orient(a, b, c) * orient(a, b, d) < 0 and orient(c, d, a) * orient(c, d, b) < 0: cnt += 1
    return cnt
def inner(c, n): return 6 <= c[0] <= n - 7 and 3 <= c[1] <= n - 4
def joins(seq, n):
    """the strands (maximal runs of inner cells, strand k on the line 2x - y = k) in the order of the tour, and the joins
    between consecutive strands: list of ((k, end), (k', end'), number of cells between them), end = 'lo' or 'hi'"""
    L = len(seq); start = next(i for i in range(L) if not inner(seq[i], n) and inner(seq[(i + 1) % L], n)) + 1
    s = seq[start:] + seq[:start]; runs = []; i = 0
    while i < L:
        if inner(s[i], n):
            j = i
            while j < L and inner(s[j], n): j += 1
            runs.append((i, j - 1)); i = j
        else: i += 1
    strands, js = [], []
    for (i, j) in runs:
        k = 2 * s[i][0] - s[i][1]; up = s[j][1] > s[i][1] if j > i else None
        strands.append((k, i, j, up))
    for t in range(len(strands)):
        k, i, j, up = strands[t]; k2, i2, j2, up2 = strands[(t + 1) % len(strands)]
        gap = (i2 - j - 1) % L
        # the end at which the tour leaves strand k, and the end at which it enters strand k2
        def end_out(k, i, j, up):
            if up is not None: return "hi" if up else "lo"
            nxt = s[(j + 1) % L]; return "hi" if nxt[1] > s[j][1] or nxt[0] > s[j][0] + 0 and nxt[1] >= s[j][1] else "lo"
        def end_in(k2, i2, j2, up2):
            if up2 is not None: return "lo" if up2 else "hi"
            prv = s[i2 - 1]; return "lo" if prv[1] < s[i2][1] else "hi"
        js.append(((k, end_out(k, i, j, up)), (k2, end_in(k2, i2, j2, up2)), gap))
    return [k for k, _, _, _ in strands], js
def join_paths(seq, n):
    """the cells of each join, in the order of joins(seq, n)"""
    L = len(seq); start = next(i for i in range(L) if not inner(seq[i], n) and inner(seq[(i + 1) % L], n)) + 1
    s = seq[start:] + seq[:start]; out = []; cur = []
    for c in s:
        if inner(c, n):
            if cur: out.append(cur); cur = []
        else: cur.append(c)
    if cur: out.append(cur)
    return out
def box_of(c, n):
    """the box that contains the cell: within 9 columns of the left or right wall and 20 rows of the top or bottom wall
    (one box at each corner), or the columns n/2-7 .. n/2+1 of the rows 0..2; None for the other cells"""
    x, y = c; h = n // 2
    if min(x, n - 1 - x) <= 8 and min(y, n - 1 - y) <= 19: return ("corner", x < h, y < h)
    if h - 7 <= x <= h + 1 and y <= 2: return ("middle",)
    return None
def rule_of(a, b):
    """the rule of Lemma 5 that the join a - b follows, or None"""
    (k, e), (k2, e2) = sorted([a, b], key=lambda t: (t[0] % 2, t[0]))                  # the even index first
    if k % 2 or not k2 % 2 or e != e2: return None
    if e == "hi" and k2 == k + 3: return "top"
    if e == "hi" and k2 == k + 7: return "right"
    if e == "lo" and k2 == k - 5: return "B"
    if e == "lo" and k2 == k + 3: return "A"
    if e == "lo" and k2 == k + 7: return "left"
    return None
def table1(n):
    """the fourteen joins that follow no rule, as in Table 1 of the paper: ((k, end), (k', end'), cells)"""
    T = [((17 - n, "hi"), (21 - n, "lo"), 15), ((17 - n, "lo"), (19 - n, "lo"), 57),
         ((-6, "lo"), (0, "lo"), 15), ((-4, "lo"), (4, "lo"), 15), ((-2, "lo"), (2, "lo"), 13),
         ((n - 13, "lo"), (n - 5, "lo"), 3), ((n - 11, "lo"), (n - 8, "lo"), 2), ((n - 9, "lo"), (n - 1, "lo"), 3), ((n - 7, "lo"), (n - 4, "lo"), 2),
         ((n - 8, "hi"), (n + 3, "hi"), 14), ((n - 5, "hi"), (n - 2, "hi"), 8), ((n - 3, "hi"), (n + 5, "hi"), 15),
         ((2 * n - 22, "hi"), (2 * n - 18, "lo"), 15), ((2 * n - 20, "hi"), (2 * n - 18, "hi"), 57)]
    return {(frozenset((a, b)), c) for a, b, c in T}
def table2(n):
    """the fourteen passes of Table 2 of the paper, in the order of the tour: (first strand, last strand); by n mod 8"""
    N = n
    return {0: [(-6, 21 - N), (17 - N, 17 - N), (19 - N, -4), (4, N - 9), (N - 1, N - 4), (N - 7, -2), (2, N - 11), (N - 8, N - 8),
                (N + 3, 2 * N - 20), (2 * N - 18, 2 * N - 18), (2 * N - 22, N + 5), (N - 3, N - 2), (N - 5, N - 5), (N - 13, 0)],
            2: [(-6, 19 - N), (17 - N, 17 - N), (21 - N, -4), (4, N - 11), (N - 8, N - 8), (N + 3, 2 * N - 22), (2 * N - 18, 2 * N - 18),
                (2 * N - 20, N + 5), (N - 3, N - 2), (N - 5, N - 5), (N - 13, 2), (-2, N - 9), (N - 1, N - 4), (N - 7, 0)],
            4: [(-6, 21 - N), (17 - N, 17 - N), (19 - N, -4), (4, N - 13), (N - 5, N - 5), (N - 2, N - 3), (N + 5, 2 * N - 22),
                (2 * N - 18, 2 * N - 18), (2 * N - 20, N + 3), (N - 8, N - 8), (N - 11, -2), (2, N - 7), (N - 4, N - 1), (N - 9, 0)],
            6: [(-6, 19 - N), (17 - N, 17 - N), (21 - N, -4), (4, N - 7), (N - 4, N - 1), (N - 9, 2), (-2, N - 13), (N - 5, N - 5),
                (N - 2, N - 3), (N + 5, 2 * N - 20), (2 * N - 18, 2 * N - 18), (2 * N - 22, N + 3), (N - 8, N - 8), (N - 11, 0)]}[n % 8]
def rule_joins(n):
    """the joins of T_n that follow a rule, as in Lemma 6 of the paper: {rule: list of the even indices k}"""
    ev = lambda a, b: list(range(a, b + 1, 2))
    return {"left": ev(16 - n, -8), "top": ev(16 - n, n - 10) + [n - 4], "B": ev(6, n - 10),
            "A": [n - 6] + ev(n - 2, 2 * n - 20), "right": [n - 6] + ev(n, 2 * n - 24)}
BL, TL, TR, BR, MID = ("corner", True, True), ("corner", True, False), ("corner", False, False), ("corner", False, True), ("middle",)
def patch_rule_info(n):
    """the fourteen joins that follow a rule although their path contains a cell of a patch, as in (a) and (b) of the proof
    of Lemma 6: {(rule, even index): (number of cells of the path, box)}"""
    return {("left", 16 - n): (12, TL), ("left", 18 - n): (12, TL), ("left", -8): (12, BL), ("top", n - 10): (4, TR), ("top", n - 4): (10, TR),
            ("B", 6): (8, BL), ("B", 8): (8, BL), ("B", 10): (5, BL), ("B", 12): (4, BL), ("A", n - 6): (3, MID),
            ("right", n - 6): (12, TR), ("right", n): (12, TR), ("right", 2 * n - 26): (12, BR), ("right", 2 * n - 24): (12, BR)}
def patch_rule_joins(n): return set(patch_rule_info(n))
def table1_boxes(n):
    """the box of each join of Table 1 (its column "near")"""
    T = [((17 - n, "hi"), (21 - n, "lo"), TL), ((17 - n, "lo"), (19 - n, "lo"), TL), ((-6, "lo"), (0, "lo"), BL), ((-4, "lo"), (4, "lo"), BL),
         ((-2, "lo"), (2, "lo"), BL), ((n - 13, "lo"), (n - 5, "lo"), MID), ((n - 11, "lo"), (n - 8, "lo"), MID), ((n - 9, "lo"), (n - 1, "lo"), MID),
         ((n - 7, "lo"), (n - 4, "lo"), MID), ((n - 8, "hi"), (n + 3, "hi"), TR), ((n - 5, "hi"), (n - 2, "hi"), TR), ((n - 3, "hi"), (n + 5, "hi"), TR),
         ((2 * n - 22, "hi"), (2 * n - 18, "lo"), BR), ((2 * n - 20, "hi"), (2 * n - 18, "hi"), BR)]
    return {frozenset((a, b)): bx for a, b, bx in T}
def lemma_joins(n):
    """all joins of T_n according to Lemma 6: the fourteen of Table 1 and those that follow a rule; a set of pairs of ends"""
    J = {j for j, _ in table1(n)}
    other = {"left": ("lo", 7), "top": ("hi", 3), "B": ("lo", -5), "A": ("lo", 3), "right": ("hi", 7)}
    for r, ks in rule_joins(n).items():
        e, d = other[r]
        for k in ks: J.add(frozenset(((k, e), (k + d, e))))
    return J
def arith(n):
    """from the list of joins of Lemma 6 alone (no tour is built): do the 3n - 32 strands with these joins form a single
    cycle, and are its fourteen passes those of Table 2, in that order?"""
    J = lemma_joins(n); nxt = {}
    for j in J:
        a, b = tuple(j)
        if a in nxt or b in nxt: return False                 # an end in two joins
        nxt[a] = b; nxt[b] = a
    strands = range(16 - n, 2 * n - 16)
    if len(nxt) != 2 * len(strands) or any((k, e) not in nxt for k in strands for e in ("lo", "hi")): return False
    exc = {j for j, _ in table1(n)}
    order = []; passes = [[]]; cur = (-6, "lo")                # enter the strand -6 at its lower end
    while True:
        k, e = cur; order.append(k); passes[-1].append(k)
        out = (k, "hi" if e == "lo" else "lo"); cur = nxt[out]
        if frozenset((out, cur)) in exc: passes.append([])
        if cur == (-6, "lo"): break
        if len(order) > len(strands): return False
    passes.pop()
    ends = [(p[0], p[-1]) for p in passes]
    return len(order) == len(strands) == len(set(order)) and ends == table2(n)
def join_report(n, show=False):
    """checks for T_n: the joins without a rule are those of Table 1; every cell that is not inner lies on one join;
    there are eight long passes, of the stated lengths.  Returns (ok, lengths of the passes)"""
    seq = sequence(tour(n), n)
    if seq is None: return False, {"all": []}                   # not a single closed tour
    ks, js = joins(seq, n)
    exc = {(frozenset((a, b)), c) for a, b, c in js if rule_of(a, b) is None}
    ok = exc == table1(n) and len(ks) == 3 * n - 32 and len(set(ks)) == len(ks)
    ok = ok and sum(c for _, _, c in js) + sum(1 for c in seq if inner(c, n)) == n * n
    ok = ok and {frozenset((a, b)) for a, b, _ in js} == lemma_joins(n) and len(js) == len(lemma_joins(n))     # the complete list of Lemma 6
    pc0 = set(patch_cells(n)); viap = {}                      # the joins that follow a rule although they pass through a patch
    for (a, b, c), path in zip(js, join_paths(seq, n)):
        if any(q in pc0 for q in path):
            if rule_of(a, b) is not None: viap[(rule_of(a, b), a[0] if a[0] % 2 == 0 else b[0])] = c
        else: ok = ok and c == (12 if rule_of(a, b) in ("left", "right") else 3)       # the other joins have the paths of Lemma 5
    info = patch_rule_info(n)
    ok = ok and viap == {key: v[0] for key, v in info.items()}     # (a): which joins, and the number of cells of each path
    if n >= 40:                                                 # (b): each of the 28 joins lies in its own box
        tb = table1_boxes(n)
        for (a, b, c), path in zip(js, join_paths(seq, n)):
            r = rule_of(a, b); j = frozenset((a, b))
            if r is None: want = tb.get(j)
            elif any(q in pc0 for q in path): want = info[(r, a[0] if a[0] % 2 == 0 else b[0])][1]
            else: continue
            ok = ok and {box_of(q, n) for q in path} == {want}
    if n >= 40:                                                 # a join that follows no rule, or that meets a patch, stays in one box
        pc = set(patch_cells(n)); paths = join_paths(seq, n); ok = ok and len(paths) == len(js)
        for (a, b, c), path in zip(js, paths):
            ok = ok and len(path) == c
            if rule_of(a, b) is None or any(q in pc for q in path):
                bx = {box_of(q, n) for q in path}; ok = ok and len(bx) == 1 and None not in bx
    # passes: maximal stretches of the cyclic sequence of strands whose joins follow a rule
    m = len(js); cut = [t for t in range(m) if rule_of(js[t][0], js[t][1]) is None]     # the join after strand t has no rule
    passes = []
    for a, b in zip(cut, cut[1:] + [cut[0] + m]): passes.append([ks[t % m] for t in range(a + 1, b + 1)])
    ends = [(p[0], p[-1]) for p in passes]; t2 = table2(n)                # the passes are those of Table 2, in the same cyclic order
    rot = lambda L, i: L[i:] + L[:i]
    if not any(rot(ends, i) == t2 for i in range(14)):                    # the tour may be traversed the other way round
        passes = [p[::-1] for p in passes[::-1]]; ends = [(p[0], p[-1]) for p in passes]
    same = any(rot(ends, i) == t2 for i in range(14))
    ok = ok and same
    longp = sorted((p for p in passes if len(p) > 4), key=lambda p: min(p))
    kind = lambda p: "LT" if max(p) < 0 else ("BR" if min(p) >= n else "BT")
    kinds = sorted(kind(p) for p in longp)
    ok = ok and len(passes) == 14 and kinds == ["BR", "BR", "BT", "BT", "BT", "BT", "LT", "LT"]
    for p in longp:                                             # along a pass the index changes by -4 or +8 in two steps
        d = {p[i + 2] - p[i] for i in range(len(p) - 2)}
        ok = ok and len(d) == 1 and (d == {8} or d == {-8} if kind(p) == "BT" else d == {4} or d == {-4})
    if show:
        print(f"n = {n}: {len(ks)} strands, {m} joins, {len(exc)} without a rule:")
        for a, b, c in sorted(((sorted(j)[0], sorted(j)[1], c) for j, c in exc), key=lambda t: t[0]): print(f"    strand {a[0]} ({a[1]}) - strand {b[0]} ({b[1]}), {c} cells")
        print("  passes:", [(kind(p), len(p), p[0], p[-1]) for p in passes])
    lens = {kd: sorted(len(p) for p in longp if kind(p) == kd) for kd in ("LT", "BT", "BR")}
    lens["all"] = [len(p) for p in (rot(passes, next(i for i in range(14) if rot(ends, i) == t2)) if any(rot(ends, i) == t2 for i in range(14)) else passes)]
    return ok, lens
def same_order(n):
    """is the cyclic order of the strands of T_{n+8} that of T_n with 24 more strands, each old strand keeping its
    index or changing it by the amount of its region (0 or -8; 0 or 8; 8 or 16)?"""
    k1, _ = joins(sequence(tour(n), n), n); k2, _ = joins(sequence(tour(n + 8), n + 8), n + 8)
    if len(k2) != len(k1) + 24: return False
    cand = lambda k: {k, k - 8} if k < 0 else ({k + 8, k + 16} if k >= n else {k, k + 8})
    anchor = min(k for k in k1 if k >= 0)
    i1 = k1.index(anchor); a = k1[i1:] + k1[:i1]
    i2 = k2.index(anchor); b = k2[i2:] + k2[:i2]
    for bb in (b, [b[0]] + b[1:][::-1]):
        i = j = skipped = 0
        while i < len(a) and j < len(bb):
            if bb[j] in cand(a[i]): i += 1; j += 1
            else: j += 1; skipped += 1
        skipped += len(bb) - j
        if i == len(a) and skipped == 24: return True
    return False
def report(n):
    t0 = time.time(); e = tour(n); seq = sequence(e, n); cr = crossings(e)
    ok = seq is not None
    print(f"n = {n}: closed knight's tour: {ok}; crossings: {cr} = 7.5 n + {cr - 15 * n // 2}   ({time.time() - t0:.1f} s)", flush=True)
    return ok and cr == 15 * n // 2 + 13
if __name__ == "__main__":
    av = sys.argv[1:]
    even = lambda a, b: range(int(a) + int(a) % 2, int(b) + 1, 2)
    if not av: print(__doc__); sys.exit(0)
    if av[0] == "--range":
        res = [report(n) for n in even(av[1], av[2])]
        print("ALL TOURS VALID WITH 7.5 n + 13 CROSSINGS" if all(res) else "FAILURE")
    elif av[0] == "--write":
        n = int(av[1]); open(av[2], "w").write(" ".join(f"{a[0]},{a[1]}-{b[0]},{b[1]}" for a, b in tour(n)) + "\n"); report(n)
    elif av[0] == "--patterns":
        res = []
        for n in even(av[1], av[2]):
            r = set(tour(n)) == set(tour_by_insertion(n)) and set(tour(n)) == set(tour(n, 42)) if n >= 42 else set(tour(n)) == set(tour_by_insertion(n))
            r = r and len(patch_cells(n)) == 179; res.append(r)
            if not r: print(f"n = {n}: the constructions do NOT agree")
        print(f"n = {av[1]}..{av[2]}: " + ("THE DESCRIPTION AND THE INSERTION OF PERIODS GIVE THE SAME TOUR; 179 PATCH CELLS" if all(res) else "FAILURE"))
    elif av[0] == "--joins":
        res = []; first = True; prev = {}
        for n in even(av[1], av[2]):
            ok, lens = join_report(n, show=first); first = False
            if n - 8 in prev:                                    # from n - 8 to n each pass keeps its length or grows by 2 or 4 strands; 24 in all
                d = [v - w for v, w in zip(lens["all"], prev[n - 8]["all"])]
                ok = ok and sorted(d) == [0] * 6 + [2] * 4 + [4] * 4
            prev[n] = lens; res.append(ok)
            print(f"n = {n}: joins as in Lemma 6, passes as in Table 2 with lengths {lens['all']}: {ok}", flush=True)
        print("ALL JOINS AND PASSES AS IN THE PAPER" if all(res) else "FAILURE")
    elif av[0] == "--arith":
        res = [arith(n) for n in even(av[1], av[2])]
        print(f"n = {av[1]}..{av[2]}: " + ("THE JOINS OF LEMMA 6 FORM A SINGLE CYCLE OF ALL STRANDS, WITH THE PASSES OF TABLE 2" if all(res) else "FAILURE"))
    elif av[0] == "--file":
        e = [tuple(sorted(m)) for m in load(av[1])]; n = int(av[2]); seq = sequence(e, n); cr = crossings(e)
        print(f"{av[1]}: n = {n}: closed knight's tour: {seq is not None}; crossings: {cr} = 7.5 n + {cr - 15 * n // 2}")
    elif av[0] == "--variant":
        res = []
        for n in range(int(av[1]), int(av[2]) + 1, 12):
            e = variant(n); ok = sequence(e, n) is not None; cr = crossings(e); res.append(ok and 6 * cr == 43 * n + 144)
            print(f"n = {n}: closed knight's tour: {ok}; crossings: {cr} = 43 n / 6 + {cr - 43 * n // 6}", flush=True)
        print("ALL VARIANT TOURS VALID WITH 43 n / 6 + 24 CROSSINGS" if all(res) else "FAILURE")
    elif av[0] == "--steps":
        res = []
        for n in even(av[1], av[2]):
            r = same_order(n); res.append(r); print(f"n = {n} -> {n + 8}: same cyclic order of strands, 24 more: {r}", flush=True)
        print("ALL STEPS CONFIRMED" if all(res) else "FAILURE")
    else:
        res = [report(int(a)) for a in av]
        print("ALL TOURS VALID WITH 7.5 n + 13 CROSSINGS" if all(res) else "FAILURE")
