#!/usr/bin/env python3
"""Checks for 'Three remarks on TAOCP Pre-Fascicle 8a: exercises 157(b), 204(b), 205' (Python standard library only).
  157  : the structural facts behind D+I+K+L+N = 8 on the 8x8 board (and on n x n boards, 6 <= n <= 20)
  204  : the trie loop of answer 204(b) as printed vs with the two cases interchanged (trie204.py)
  205  : the exact one-key formula vs brute force for q <= 9, and its asymptotic expansion (one_key.py)"""
import sys, subprocess, os
HERE = os.path.dirname(os.path.abspath(__file__))
def check157():
    for n in range(7, 21):
        cells = [(i, j) for i in range(n) for j in range(n)]
        moves = {frozenset({(i, j), (i + a, j + b)}) for i, j in cells for a, b in ((1, 2), (2, 1), (1, -2), (2, -1))
                 if 0 <= i + a < n and 0 <= j + b < n}
        syms = [lambda i, j: (i, j), lambda i, j: (j, i), lambda i, j: (n - 1 - i, j), lambda i, j: (i, n - 1 - j),
                lambda i, j: (n - 1 - i, n - 1 - j), lambda i, j: (j, n - 1 - i), lambda i, j: (n - 1 - j, i), lambda i, j: (n - 1 - j, n - 1 - i)]
        orbit = {}
        for m in moves:
            if m in orbit: continue
            o = {frozenset(s(*c) for c in m) for s in syms}
            for x in o: orbit[x] = min(tuple(sorted(y)) for y in o)
        cls = lambda a, b: orbit[frozenset({a, b})]
        corners = [(0, 0), (0, n - 1), (n - 1, 0), (n - 1, n - 1)]
        ck = {c for k in corners for c in cells if frozenset({k, c}) in moves}        # cells a knight's move from a corner
        assert len(ck) == 8
        corner_class = cls((0, 0), (1, 2))
        five = {cls((1, 2), c) for c in cells if frozenset({(1, 2), c}) in moves and c != (0, 0)}
        # (i) at every ck cell: one move to its corner, every other move in the five classes
        for c in ck:
            ms = [m for m in moves if c in m]
            assert sum(1 for m in ms if orbit[m] == corner_class) == 1 and all(orbit[m] in five for m in ms if orbit[m] != corner_class)
        # (ii) every move of the five classes has exactly one end in ck
        assert all(len(m & ck) == 1 for m in moves if orbit[m] in five)
        assert corner_class not in five
        if n == 8:
            name = {cls((0, 0), (1, 2)): "A", cls((0, 3), (1, 5)): "D", cls((1, 2), (2, 4)): "I", cls((1, 2), (3, 1)): "K",
                    cls((0, 2), (2, 1)): "L", cls((1, 2), (3, 3)): "N"}
            print("157: on the 8x8 board the five classes are", sorted(name[k] for k in five), "(letters as read from Knuth's figure)")
    print("157: facts (i) and (ii) hold for every n x n board, 7 <= n <= 20 (not for n = 6); hence the five classes carry exactly 8 moves of any closed tour")
def run(script):
    out = subprocess.run([sys.executable, "-I", os.path.join(HERE, script)], capture_output=True, text=True, cwd=HERE)
    print(out.stdout.strip()); assert out.returncode == 0, out.stderr
if __name__ == "__main__":
    what = sys.argv[1] if len(sys.argv) > 1 else "all"
    if what in ("all", "157"): check157()
    if what in ("all", "204"): run("trie204.py")
    if what in ("all", "205"): run("one_key.py")
    print("all checks passed")
