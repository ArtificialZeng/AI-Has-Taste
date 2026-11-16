"""Lower bounds for the number of coils of a whirling knight's tour, from labelled wedges.   (Python 3, standard library)

Lemma.  Let W be a wedge: all cells whose directions from the pivot lie in an angular interval shorter than a half-turn.
Label its cells B, N, O, I so that no arc inside W leads from a cell labelled B or O to a cell labelled B or I.
Then every whirling tour has at least |B| - |N| coils.

This program builds the labellings of the paper and checks, for every board size up to the given bounds, that
  * the labelled set is exactly a wedge,
  * no arc inside it leads from B or O to B or I,
  * |B| - |N| has the stated value.

  python lower_bounds.py [max_even_n] [max_m]        (defaults 300 and 100; odd n = 2m+1)

Even n = 2h.  With a = h-1-i, b = j-h the wedge is  Q = {a,b >= 0},  S = {a <= -1, b >= -3a-2},  S' = {b <= -1, a >= -3b-2}.
  Q: B if a+b even, N if odd, except I at (0,b) with b = 1 (mod 4) and O at (a,0) with a = 1 (mod 4);
  S: B at (-1,b) with b = 1 (mod 4), otherwise I;      S': B at (a,-1) with a = 1 (mod 4), otherwise O.
  Value (h mod 2) + 4*floor((h+2)/4):  n/2 if n = 0, 2 (mod 8),  n/2 + 2 if n = 4, 6 (mod 8).
Odd n = 2m+1, centred coordinates (x,y) = (i-m, j-m).
  Axis wedge {y >= 1, 2|x| <= y}:  x = 0: N if 4 | y, else B;  x = +-1 and y = 2 (mod 4): B;  otherwise O if x < 0, I if x > 0.
      Value m + 2 if m = 2, 3 (mod 4), else m.
  Diagonal wedge {x,y >= 1, y <= 2x, x <= 2y}, with x = 3t + r, e = y - 3t:
      pattern 1 (m = 2 mod 3):  r=0: I (e<0), N (e=0), O (e>0);   r=1: I (e<=0), B (e=1), I (e=2), O (e>=3);
                                r=2: I (e<=0), B (e=1,2,4), O (e=3, e>=5);   and B at (1,2).
      pattern 2 (m = 1 mod 3):  r=0: I (e<=0), O (e>=1);          r=1: B (e=-1,1), I (other e<=2), O (e>=3);
                                r=2: I (e<=0), N (e=1), B (e=2,4), O (e=3, e>=5);   and B at (1,2), I at (2,1).
      Value m + 2 in both cases.
Small even boards.  For n = 8 and n = 10 two special labelled wedges (SMALL below) give at least 6 coils.
Odd n >= 9.  If a tour had (n-1)/2 coils, no arc could pass over a half-axis or a half-diagonal; the program checks
that then (2,1) has the single possible predecessor (4,0) and successor (3,3), and (1,2) has (3,3) and (0,4), which
forces a cycle of 16 cells.  So every tour has at least (n+1)/2 coils.
"""
import sys
MOV = ((1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1))
cross = lambda u, v: u[0] * v[1] - u[1] * v[0]
def between(d, A, B):
    """direction d lies in the closed interval from A counterclockwise to B (less than a half-turn)"""
    return (cross(A, d) > 0 or (cross(A, d) == 0 and A[0] * d[0] + A[1] * d[1] > 0)) and \
           (cross(d, B) > 0 or (cross(d, B) == 0 and B[0] * d[0] + B[1] * d[1] > 0))
def check(vec, A, B, label):
    """vec: cell -> direction vector about the pivot.  Returns |B| - |N| after checking the three conditions."""
    W = {v for v, d in vec.items() if between(d, A, B)}
    lab = {v: label(v) for v in vec}
    assert all((lab[v] is not None) == (v in W) for v in vec), "the labelled set is not the wedge"
    for u in W:
        if lab[u] in "BO":
            for m in MOV:
                w = (u[0] + m[0], u[1] + m[1])
                if w in W and cross(vec[u], vec[w]) > 0: assert lab[w] in "NO", ("bad arc", u, w)
    return sum(lab[v] == "B" for v in W) - sum(lab[v] == "N" for v in W)

def even_label(n):
    h = n // 2
    def f(v):
        a, b = h - 1 - v[0], v[1] - h
        if a >= 0 and b >= 0:
            if a == 0 and b % 4 == 1: return "I"
            if b == 0 and a % 4 == 1: return "O"
            return "B" if (a + b) % 2 == 0 else "N"
        if a <= -1 and b >= -3 * a - 2: return "B" if (a == -1 and b % 4 == 1) else "I"
        if b <= -1 and a >= -3 * b - 2: return "B" if (b == -1 and a % 4 == 1) else "O"
        return None
    return f
def axis_label(v):
    x, y = v
    if y < 1 or 2 * abs(x) > y: return None
    if x == 0: return "N" if y % 4 == 0 else "B"
    if abs(x) == 1 and y % 4 == 2: return "B"
    return "O" if x < 0 else "I"
def diag_label(pattern):
    def f(v):
        x, y = v
        if x < 1 or y < 1 or y > 2 * x or x > 2 * y: return None
        t, r = divmod(x, 3); e = y - 3 * t
        if (x, y) == (1, 2): return "B"
        if pattern == 1:
            if r == 0: return "I" if e < 0 else "N" if e == 0 else "O"
            if r == 1: return "I" if e <= 0 else "B" if e == 1 else "I" if e == 2 else "O"
            return "I" if e <= 0 else "B" if e in (1, 2, 4) else "O"
        if (x, y) == (2, 1): return "I"
        if r == 0: return "I" if e <= 0 else "O"
        if r == 1: return "B" if e in (-1, 1) else "I" if e <= 2 else "O"
        return "I" if e <= 0 else "N" if e == 1 else "B" if e in (2, 4) else "O"
    return f

# rows i = 0..n-1 from the top, columns j = 0..n-1; '.' marks cells outside the wedge
SMALL = {8: ((3, 1), (3, 7), ["........", "........", "........", "........", "....B...", "....IBOB", ".....IBO", ".....BIB"]),
         10: ((3, 1), (-1, 1), [".........B", "........OB", ".......OII", "......BBNB", ".....OBNII", ".....IIINB",
                                ".....IBIII", "......IINB", "......IIII", "......IIIB"])}
HALF_LINES = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
def forced_16_cycle(m):
    cells = {(x, y) for x in range(-m, m + 1) for y in range(-m, m + 1) if (x, y) != (0, 0)}
    ok = lambda u, w: w in cells and u in cells and cross(u, w) > 0 and \
        not any(cross(u, s) > 0 and cross(s, w) > 0 for s in HALF_LINES)
    succ = lambda u: [(u[0] + a, u[1] + b) for a, b in MOV if ok(u, (u[0] + a, u[1] + b))]
    pred = lambda w: [(w[0] - a, w[1] - b) for a, b in MOV if ok((w[0] - a, w[1] - b), w)]
    return pred((2, 1)) == [(4, 0)] and succ((2, 1)) == [(3, 3)] and pred((1, 2)) == [(3, 3)] and succ((1, 2)) == [(0, 4)]

if __name__ == "__main__":
    max_even = int(sys.argv[1]) if len(sys.argv) > 1 else 300
    max_m = int(sys.argv[2]) if len(sys.argv) > 2 else 100
    for n in range(4, max_even + 1, 2):
        h = n // 2
        vec = {(i, j): (2 * i - n + 1, 2 * j - n + 1) for i in range(n) for j in range(n)}
        val = check(vec, (1, 3), (-3, -1), even_label(n))
        assert val == h % 2 + 4 * ((h + 2) // 4) == (h + 2 if h % 4 in (2, 3) else h), (n, val)
    print(f"even n = 4..{max_even}: labelling valid; at least n/2 coils, and n/2 + 2 when n = 4 or 6 (mod 8)")
    for m in range(2, max_m + 1):
        vec = {(x, y): (x, y) for x in range(-m, m + 1) for y in range(-m, m + 1) if (x, y) != (0, 0)}
        va = check(vec, (1, 2), (-1, 2), axis_label)
        assert va == (m + 2 if m % 4 in (2, 3) else m), (m, va)
        if m % 3:
            vd = check(vec, (2, 1), (1, 2), diag_label(1 if m % 3 == 2 else 2))
            assert vd == m + 2, (m, vd)
    print(f"odd n = 5..{2 * max_m + 1}: labellings valid; at least (n+3)/2 coils unless n = 1 or 19 (mod 24)")
    for n, (A, B, G) in SMALL.items():
        vec = {(i, j): (2 * i - n + 1, 2 * j - n + 1) for i in range(n) for j in range(n)}
        assert check(vec, A, B, lambda v, G=G: None if G[v[0]][v[1]] == "." else G[v[0]][v[1]]) == 6
    print("n = 8 and n = 10: the special labelled wedges are valid and give at least 6 coils")
    assert all(forced_16_cycle(m) for m in range(4, max_m + 1))
    print(f"odd n = 9..{2 * max_m + 1}: (n-1)/2 coils would force a cycle of 16 cells; so at least (n+1)/2 coils")
