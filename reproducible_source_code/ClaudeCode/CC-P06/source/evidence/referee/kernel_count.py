#!/usr/bin/env python3
"""Second, theory-based count for the claimed diagrams (independent of rdp's search).

Fact (proved in the referee report): if L1, L2 are loops with the same signature then
L1 xor L2 is totally even, and the totally even sets are exactly the boundaries
d(S) = xor of the boundaries of the cells in S, for S in the kernel of the cell
adjacency matrix A over GF(2) (every cell has an even number of neighbours in S).
So the solutions of sig(L) are exactly the loops L xor d(S), S in ker A, with the
same signature.  For every solution L found by rdp we enumerate all 2^dim S and
count; this must reproduce the rdp count from every L.
"""
import json
import itertools
from rdp import check_solution


def kernel_basis(m, n):
    cells = [(r, c) for r in range(m) for c in range(n)]
    idx = {x: i for i, x in enumerate(cells)}
    rows = []
    for (r, c) in cells:
        mask = 0
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if (r + dr, c + dc) in idx:
                mask |= 1 << idx[(r + dr, c + dc)]
        rows.append(mask)
    # nullspace of A over GF(2): reduced row echelon
    ncol = len(cells)
    piv = []
    R = rows[:]
    rank = 0
    pivcols = []
    for col in range(ncol):
        sel = None
        for i in range(rank, len(R)):
            if R[i] >> col & 1:
                sel = i
                break
        if sel is None:
            continue
        R[rank], R[sel] = R[sel], R[rank]
        for i in range(len(R)):
            if i != rank and R[i] >> col & 1:
                R[i] ^= R[rank]
        pivcols.append(col)
        rank += 1
    free = [c for c in range(ncol) if c not in pivcols]
    basis = []
    for f in free:
        v = 1 << f
        for i, pc in enumerate(pivcols):
            if R[i] >> f & 1:
                v |= 1 << pc
        basis.append(v)
    for v in basis:  # sanity: A v = 0
        for rmask in rows:
            assert bin(rmask & v).count('1') % 2 == 0
    return cells, basis


def boundary(m, n, cells, S):
    inS = {cells[i] for i in range(len(cells)) if S >> i & 1}
    E = set()
    for r in range(m + 1):
        for c in range(n):  # h edge between cell (r-1,c) and (r,c)
            if ((r - 1, c) in inS) != ((r, c) in inS):
                E.add(('h', r, c))
    for r in range(m):
        for c in range(n + 1):  # v edge between cell (r,c-1) and (r,c)
            if ((r, c - 1) in inS) != ((r, c) in inS):
                E.add(('v', r, c))
    return frozenset(E)


def is_totally_even(m, n, E):
    from collections import Counter as C
    deg = C()
    for (t, r, c) in E:
        a, b = ((r, c), (r, c + 1)) if t == 'h' else ((r, c), (r + 1, c))
        deg[a] += 1
        deg[b] += 1
    if any(d % 2 for d in deg.values()):
        return False
    for r in range(m):
        for c in range(n):
            k = (('h', r, c) in E) + (('h', r + 1, c) in E) + (('v', r, c) in E) + (('v', r, c + 1) in E)
            if k % 2:
                return False
    return True


if __name__ == '__main__':
    data = json.load(open('solutions.json'))
    for name, d in data.items():
        rows = d['rows']
        m, n = len(rows), len(rows[0])
        cells, basis = kernel_basis(m, n)
        Ts = []
        for bits in itertools.product((0, 1), repeat=len(basis)):
            S = 0
            for b, v in zip(bits, basis):
                if b:
                    S ^= v
            Ts.append(boundary(m, n, cells, S))
        assert all(is_totally_even(m, n, T) for T in Ts)
        assert len(set(Ts)) == len(Ts)
        sols = [frozenset(tuple(e) for e in s) for s in d['solutions']]
        counts = []
        for L in sols:
            found = set()
            for T in Ts:
                X = L ^ T
                if X and check_solution(rows, X)[0]:
                    found.add(X)
            counts.append((len(found), found == set(sols)))
        print(f'{name}: dim ker = {len(basis)}; rdp count = {d["count"]}; kernel count from each solution = {counts}')
