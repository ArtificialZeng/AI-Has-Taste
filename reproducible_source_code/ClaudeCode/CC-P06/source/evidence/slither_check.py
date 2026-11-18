"""Stand-alone check (Python 3 standard library only) for
   'A fully clued Slitherlink diagram with exactly five solutions'.
For each diagram it counts the single-loop solutions in two independent ways:
  (1) plain backtracking over the edges (clue and degree pruning, connectivity checked at the end);
  (2) from one solution L, all sets L xor E with E totally even (basis by F2 elimination), keeping single loops
      with the same clues.
usage: python3 slither_check.py            (all diagrams)"""
import sys
DIAGRAMS = {
 "five_13x13": "3222222122223 2222222221122 2222122223232 2222221222112 2212222222222 2222222222221 2221122211222 "
               "1222222222222 2222222222122 2112221222222 2323222212222 2211222222222 3222212222223",
 "six_12x12":  "322222100123 222111211222 122231122221 222221122210 213222222210 211122221121 121122221112 012222222312 "
               "012221122212 122221132222 222112112222 321001222123",
 "six_13x13":  "3222221132222 2221112122312 1222311221112 2222211221121 2132222112210 2111222112210 1211222221121 "
               "0122112221112 0122112222312 1211221122222 2101221132221 2012112111222 2221001222223",
 "knuth_6x6":  "322222 222232 222222 222222 232222 222223",
 "two_2x2":    "32 23",
}
EXPECTED = {"five_13x13": 5, "six_12x12": 6, "six_13x13": 6, "knuth_6x6": 4, "two_2x2": 2}

def build(rows):
    R, C = len(rows), len(rows[0])
    clue = [[int(ch) for ch in r] for r in rows]          # clue[r][c], r = 0 is the top row
    vid = lambda r, c: r * (C + 1) + c
    edges, ecells = [], []
    for r in range(R + 1):                                  # horizontal edges of vertex row r, then verticals below it
        for c in range(C):
            edges.append((vid(r, c), vid(r, c + 1)))
            ecells.append([x for x in ((r - 1) * C + c if r > 0 else None, r * C + c if r < R else None) if x is not None])
        if r < R:
            for c in range(C + 1):
                edges.append((vid(r, c), vid(r + 1, c)))
                ecells.append([x for x in (r * C + c - 1 if c > 0 else None, r * C + c if c < C else None) if x is not None])
    return R, C, clue, edges, ecells

def components(edges, sel):
    par = {}
    def f(x):
        while par.setdefault(x, x) != x:
            par[x] = par[par[x]]; x = par[x]
        return x
    for e in sel:
        a, b = edges[e]; par[f(a)] = f(b)
    return len({f(edges[e][0]) for e in sel})

def backtrack(rows):
    R, C, clue, edges, ecells = build(rows)
    NE, NV = len(edges), (R + 1) * (C + 1)
    target = [clue[i // C][i % C] for i in range(R * C)]
    cnt, rem = [0] * (R * C), [4] * (R * C)
    deg, vrem = [0] * NV, [0] * NV
    for a, b in edges: vrem[a] += 1; vrem[b] += 1
    val, sols = [0] * NE, []
    sys.setrecursionlimit(10000)
    def rec(e):
        if e == NE:
            sel = [k for k in range(NE) if val[k]]
            if sel and components(edges, sel) == 1: sols.append(frozenset(sel))
            return
        a, b = edges[e]
        for x in (0, 1):
            val[e] = x
            for cl in ecells[e]: cnt[cl] += x; rem[cl] -= 1
            deg[a] += x; deg[b] += x; vrem[a] -= 1; vrem[b] -= 1
            ok = all(cnt[cl] <= target[cl] <= cnt[cl] + rem[cl] for cl in ecells[e]) and \
                 all(deg[v] <= 2 and not (vrem[v] == 0 and deg[v] == 1) for v in (a, b))
            if ok: rec(e + 1)
            for cl in ecells[e]: cnt[cl] -= x; rem[cl] += 1
            deg[a] -= x; deg[b] -= x; vrem[a] += 1; vrem[b] += 1
        val[e] = 0
    rec(0)
    return sols, (R, C, clue, edges, ecells)

def totally_even_basis(R, C, edges, ecells):
    NE, NV = len(edges), (R + 1) * (C + 1)
    rows = [0] * (NV + R * C)
    for e, (a, b) in enumerate(edges):
        rows[a] |= 1 << e; rows[b] |= 1 << e
        for cl in ecells[e]: rows[NV + cl] |= 1 << e
    piv = {}
    for r in rows:
        for p, pr in piv.items():
            if r >> p & 1: r ^= pr
        if r:
            p = (r & -r).bit_length() - 1
            for k in list(piv):
                if piv[k] >> p & 1: piv[k] ^= r
            piv[p] = r
    basis = []
    for f in (e for e in range(NE) if e not in piv):
        v = 1 << f
        for p, pr in piv.items():
            if pr >> f & 1: v |= 1 << p
        basis.append(v)
    return basis

def via_totally_even(L, data):
    R, C, clue, edges, ecells = data
    basis = totally_even_basis(R, C, edges, ecells)
    Lm = sum(1 << e for e in L)
    def sig(m):
        s = [0] * (R * C)
        for e in range(len(edges)):
            if m >> e & 1:
                for cl in ecells[e]: s[cl] += 1
        return s
    s0 = sig(Lm); found = []
    for bits in range(1 << len(basis)):
        E = 0
        for i, b in enumerate(basis):
            if bits >> i & 1: E ^= b
        M = Lm ^ E; sel = [e for e in range(len(edges)) if M >> e & 1]
        deg = {}
        for e in sel:
            for v in edges[e]: deg[v] = deg.get(v, 0) + 1
        if sel and all(d == 2 for d in deg.values()) and sig(M) == s0 and components(edges, sel) == 1:
            found.append(M)
    return len(found), len(basis)

if __name__ == "__main__":
    ok = True
    for name, txt in DIAGRAMS.items():
        rows = txt.split()
        sols, data = backtrack(rows)
        k, dim = via_totally_even(next(iter(sols)), data)
        good = len(sols) == EXPECTED[name] == k
        ok &= good
        print(f"{name:12s} {len(rows)}x{len(rows[0])}: backtracking {len(sols)} solutions; totally even sets (dim {dim}) {k}; "
              f"expected {EXPECTED[name]}  {'OK' if good else 'MISMATCH'}")
    print("ALL OK" if ok else "SOME CHECK FAILED")
