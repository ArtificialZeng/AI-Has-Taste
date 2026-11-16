"""Certificate for the 10 x 10 board: every cycle cover of the whirling digraph, hence every whirling knight's tour,
has at least 7 and at most 9 coils.  cert10.txt gives two sets of weights yout(v), yin(v) in {-1, 0, 1} on the cells:
for the first, yout(u) + yin(w) <= [the arc u -> w crosses the ray R] on every arc, and the weights sum to 7; for the
second the inequality is reversed and the sum is 9.  R is the ray from the pivot in the direction (-21, 1).
This program checks the inequalities on all 288 arcs in integer arithmetic.  (Found by the ninth referee pass.)
  python3 cert10_verify.py        run in the folder that contains cert10.txt
"""
# Stand-alone exact check of cert10.txt (no solver, no numpy).
MOVES = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]
n = 10
dx, dy = -(2 * n + 1), 1
lo = {}; hi = {}
for line in open('cert10.txt'):
    if line.startswith('#'):
        continue
    kind, i, j, a, b = line.split()
    (lo if kind == 'lower' else hi)[(int(i), int(j))] = (int(a), int(b))
assert len(lo) == len(hi) == 100
narcs = 0
for i in range(n):
    for j in range(n):
        X, Y = 2 * i - (n - 1), 2 * j - (n - 1)
        for a, b in MOVES:
            i2, j2 = i + a, j + b
            if 0 <= i2 < n and 0 <= j2 < n:
                X2, Y2 = 2 * i2 - (n - 1), 2 * j2 - (n - 1)
                if X * Y2 - X2 * Y > 0:
                    narcs += 1
                    k = 1 if (X * dy - dx * Y > 0 and dx * Y2 - X2 * dy > 0) else 0
                    assert lo[(i, j)][0] + lo[(i2, j2)][1] <= k
                    assert hi[(i, j)][0] + hi[(i2, j2)][1] >= k
print('arcs checked:', narcs, '| lower bound', sum(a + b for a, b in lo.values()), '| upper bound', sum(a + b for a, b in hi.values()))
