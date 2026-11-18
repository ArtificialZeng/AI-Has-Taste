#!/usr/bin/env python3
"""Referee's independent Slitherlink solution counter (fully clued diagrams).

Method: exact frontier ("plug") dynamic programming over the vertices of the
(m+1) x (n+1) vertex grid in row-major order, with memoised depth-first
evaluation.  At vertex (r,c) we decide the edge to the right, h[r][c], and the
edge going down, v[r][c].  The state is
  plugs[j]  : component label of the vertical edge crossing the frontier at
              column j (v[r-1][j] for j >= c, v[r][j] for j < c), 0 = none
  left      : label of h[r][c-1] (the edge entering (r,c) from the left)
  need[j]   : number of sides still required by the pending cell in column j
              (cell (r-1,j) for j >= c, cell (r,j) for j < c)
  closed    : a loop has already been closed (then no edge may ever be added)
Every partial path has its two ends on the frontier; joining the two ends of the
same path closes a loop, which is allowed only if no other path is open, and
afterwards no new edge may start.  So accepted assignments are exactly the
single closed loops meeting every clue.  No pruning beyond exact constraint
checks is done, and every branch is followed, so the count is exhaustive.

Edge naming in the output: ('h', r, c) is the edge (r,c)-(r,c+1);
('v', r, c) is the edge (r,c)-(r+1,c); vertices are (row, column).
"""
import sys

sys.setrecursionlimit(100000)


def normalize(plugs, left):
    mp = {}
    out = []
    for x in plugs:
        if x == 0:
            out.append(0)
        else:
            if x not in mp:
                mp[x] = len(mp) + 1
            out.append(mp[x])
    if left == 0:
        l2 = 0
    else:
        if left not in mp:
            mp[left] = len(mp) + 1
        l2 = mp[left]
    return tuple(out), l2


class Counter:
    def __init__(self, rows):
        self.clue = [[int(ch) for ch in row] for row in rows]
        self.m = len(self.clue)
        self.n = len(self.clue[0])
        assert all(len(r) == self.n for r in self.clue)
        assert all(0 <= x <= 4 for r in self.clue for x in r)  # 4 only for the 1x1 loop
        self.nsteps = (self.m + 1) * (self.n + 1)
        self.memo = {}

    def trans(self, k, st):
        m, n, clue = self.m, self.n, self.clue
        plugs, left, need, closed = st
        r, c = divmod(k, n + 1)
        up = plugs[c] if r >= 1 else 0
        lf = left
        out = []
        rights = (0, 1) if c < n else (0,)
        downs = (0, 1) if r < m else (0,)
        for rt in rights:
            if r >= 1 and c < n and need[c] != rt:
                continue  # bottom side of cell (r-1,c) is h[r][c] = rt
            for dn in downs:
                deg = (up > 0) + (lf > 0) + rt + dn
                if deg != 0 and deg != 2:
                    continue
                nd = list(need)
                ok = True
                if r < m:
                    if c >= 1:  # right side of cell (r,c-1) is v[r][c] = dn
                        x = nd[c - 1] - dn
                        if x < 0 or x > 1:
                            ok = False
                        nd[c - 1] = x
                    if c < n:   # new cell (r,c): top = rt, left = dn
                        x = clue[r][c] - rt - dn
                        if x < 0 or x > 2:
                            ok = False
                        nd[c] = x
                else:
                    if c < n:
                        nd[c] = 0
                if not ok:
                    continue
                p = list(plugs)
                ncl = closed
                if deg == 0:
                    p[c] = 0
                    nl = 0
                elif up and lf:
                    p[c] = 0
                    nl = 0
                    if up == lf:
                        if closed or any(p):
                            continue  # would leave a second component
                        ncl = True
                    else:
                        p = [lf if x == up else x for x in p]
                elif up or lf:
                    lab = up or lf
                    p[c] = lab if dn else 0
                    nl = lab if rt else 0
                else:
                    if closed:
                        continue  # a second loop would start
                    lab = max(p) + 1
                    p[c] = lab
                    nl = lab
                pp, l2 = normalize(p, nl)
                out.append((rt, dn, (pp, l2, tuple(nd), ncl)))
        return out

    def init_state(self):
        return (tuple([0] * (self.n + 1)), 0, tuple([0] * self.n), False)

    def f(self, k, st):
        if k == self.nsteps:
            return 1 if st[3] else 0
        key = (k, st)
        v = self.memo.get(key)
        if v is not None:
            return v
        tot = 0
        for rt, dn, nst in self.trans(k, st):
            tot += self.f(k + 1, nst)
        self.memo[key] = tot
        return tot

    def count(self):
        return self.f(0, self.init_state())

    def solutions(self):
        n = self.n
        res = []
        path = []

        def rec(k, st):
            if k == self.nsteps:
                if st[3]:
                    res.append(list(path))
                return
            r, c = divmod(k, n + 1)
            for rt, dn, nst in self.trans(k, st):
                if self.f(k + 1, nst) > 0:
                    if rt:
                        path.append(('h', r, c))
                    if dn:
                        path.append(('v', r, c))
                    rec(k + 1, nst)
                    if dn:
                        path.pop()
                    if rt:
                        path.pop()
        rec(0, self.init_state())
        return [frozenset(s) for s in res]


def edge_ends(e):
    t, r, c = e
    return ((r, c), (r, c + 1)) if t == 'h' else ((r, c), (r + 1, c))


def check_solution(rows, edges):
    """Independent check: single cycle, and recomputed clues equal the diagram."""
    m, n = len(rows), len(rows[0])
    deg = {}
    adj = {}
    for e in edges:
        a, b = edge_ends(e)
        for x in (a, b):
            assert 0 <= x[0] <= m and 0 <= x[1] <= n
        deg[a] = deg.get(a, 0) + 1
        deg[b] = deg.get(b, 0) + 1
        adj.setdefault(a, []).append(b)
        adj.setdefault(b, []).append(a)
    if any(d != 2 for d in deg.values()):
        return False, 'degree'
    start = next(iter(adj))
    seen = {start}
    stack = [start]
    while stack:
        x = stack.pop()
        for y in adj[x]:
            if y not in seen:
                seen.add(y)
                stack.append(y)
    if len(seen) != len(adj):
        return False, 'disconnected'
    sig = []
    for r in range(m):
        row = ''
        for c in range(n):
            k = (('h', r, c) in edges) + (('h', r + 1, c) in edges) + \
                (('v', r, c) in edges) + (('v', r, c + 1) in edges)
            row += str(k)
        sig.append(row)
    if sig != list(rows):
        return False, 'clues'
    return True, len(edges)


def draw(rows, edges):
    m, n = len(rows), len(rows[0])
    lines = []
    for r in range(m + 1):
        s = ''
        for c in range(n + 1):
            s += '+'
            if c < n:
                s += '---' if ('h', r, c) in edges else '   '
        lines.append(s)
        if r < m:
            s = ''
            for c in range(n + 1):
                s += '|' if ('v', r, c) in edges else ' '
                if c < n:
                    s += ' ' + rows[r][c] + ' '
            lines.append(s)
    return '\n'.join(lines)


if __name__ == '__main__':
    rows = sys.argv[1:]
    C = Counter(rows)
    cnt = C.count()
    print('count', cnt, 'memo states', len(C.memo))
