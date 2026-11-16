"""rho(N, 12) >= 14 for EVERY N = 3 (mod 4), N >= 27: an explicit labelling and its verification.

The labelling of the outer cells (columns 0..11) of the left side, between the two diagonals, for N = 3 (mod 4):
with q0 = (3N - 25) / 4,
  rows i < q0:            I everywhere;
  rows q0 + r, r = 0..10: the eleven rows of HEAD;
  rows i >= q0 + 11:      B in column 0, N in column 1, O in the columns 2..11; but O in column 1 of row N-3.
Only the cells of the wedge are labelled: row N-2-t has the columns 0..t (t = 0, 1, ...), and above the middle row
i has the columns 0..i-1.  Then |B| - |N| = 12 (HEAD) + 1 (row N-3) + 1 (row N-2) = 14.

Part 1 checks this labelling directly for every N = 3 (mod 4) from N1 = 123 to Nmax (default 2003): no arc leads
from a cell labelled B or O to a cell labelled B or I, and |B| - |N| = 14.
Part 2 proves it for all N >= N1.  For a cell (i, j) and a knight move (a, b) the arc condition is x*b - a*y > 0
with x = 2i - (N-1), y = 2j - (N-1).  For a cell of row q0 + r this is  N(2a+b) + (4r-23)b - 2a(2j+1) > 0,
and for a cell of row N-2-t it is  N(a+b) - (3+2t)b - a(2j+1) > 0.  Both are linear in N.  The program lists every
pair (cell, move) whose labels would violate the rule, in the two regions where the labels are not uniform
(rows q0-3 .. q0+13 and rows N-12 .. N-2), and checks that the left-hand side is <= 0 at N = N1 and has a
coefficient of N that is <= 0, so that it is <= 0 for all N >= N1.  In the uniform rows in between the only
candidates are the moves (1,-2) and (-1,-2) from column 2 to column 0; they are checked for every such row.
For N < N1 the bound is given by ring_bound.py, which computes a labelling for each N separately.
Standard library only.   python3 ring_bound_all.py [Nmax]"""
import sys
HEAD = ["IBIIIBIIIBIB", "BIBNBIBNBBBO", "NBNBNBNBNBNO", "BNBNBNBNOOOO", "NINBNBOBOBOO", "BNBNBNBNOOOO",
        "IINBNOOOOOOO", "BNBOBOBOOOOO", "IINBNOOOOOOO", "BNOOOOOOOOOO", "BIOBOOOOOOOO"]
MOVES = ((1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1))
N1 = 123
def label_top(r, j):
    """label of the cell in row q0 + r, column j (0 <= j <= 11), for rows that are not near the bottom corner"""
    if r < 0: return "I"
    if r <= 10: return HEAD[r][j]
    return "B" if j == 0 else "N" if j == 1 else "O"
def label_bottom(t, j):
    """label of the cell in row N-2-t, column j <= min(t, 11), for rows below the head"""
    if j == 0: return "B"
    if j == 1: return "O" if t == 1 else "N"
    return "O"
def labelling(N):
    q0 = (3 * N - 25) // 4; lab = {}
    for i in range(N):
        for j in range(12):
            x, y = 2 * i - (N - 1), 2 * j - (N - 1)
            lo = (-(2 * N + 1), -(2 * N - 3)); hi = (-lo[1], lo[0])
            if not (lo[0] * y - x * lo[1] > 0 and x * hi[1] - hi[0] * y > 0): continue          # not in the wedge
            lab[(i, j)] = label_top(i - q0, j) if i - q0 <= 10 else label_bottom(N - 2 - i, j)
    return lab
def direct(N):
    lab = labelling(N)
    for (i, j), l in lab.items():
        if l not in "BO": continue
        x, y = 2 * i - (N - 1), 2 * j - (N - 1)
        for a, b in MOVES:
            w = (i + a, j + b)
            if w in lab and lab[w] in "BI" and x * b - a * y > 0: return None
    v = list(lab.values()); return v.count("B") - v.count("N")
def prove():
    bad = 0; n1 = n2 = 0
    # region 1: rows q0 + r, -3 <= r <= 13; the arc condition is N*al + be > 0
    for r in range(-3, 14):
        for j in range(12):
            if label_top(r, j) not in "BO": continue
            for a, b in MOVES:
                r2, j2 = r + a, j + b
                if not (0 <= j2 <= 11) or label_top(r2, j2) not in "BI": continue
                al, be = 2 * a + b, (4 * r - 23) * b - 2 * a * (2 * j + 1); n1 += 1
                if not (al <= 0 and al * N1 + be <= 0): bad += 1
    # region 2: rows N-2-t, 0 <= t <= 10, columns 0..min(t, 11); the arc condition is N*al + be > 0
    for t in range(0, 11):
        for j in range(0, min(t, 11) + 1):
            if label_bottom(t, j) not in "BO": continue
            for a, b in MOVES:
                t2, j2 = t - a, j + b
                if t2 < 0 or not (0 <= j2 <= min(t2, 11)) or label_bottom(t2, j2) not in "BI": continue
                al, be = a + b, -(3 + 2 * t) * b - a * (2 * j + 1); n2 += 1
                if not (al <= 0 and al * N1 + be <= 0): bad += 1
    # uniform rows: from column 2 to column 0, moves (1,-2) and (-1,-2); row q0 + r with r >= 11
    #   (1,-2):  N*0 + (4r-23)(-2) - 2*5 = 36 - 8r <= 0 for r >= 5;   (-1,-2): -4N - 8r + 56 < 0 for N >= 14
    assert all(36 - 8 * r <= 0 for r in range(11, 40)) and -4 * N1 + 56 < 0
    # the two regions do not overlap and lie in the wedge for N >= N1: q0 + 13 <= N - 13 and the head is not truncated
    q0 = (3 * N1 - 25) // 4
    assert q0 + 13 <= N1 - 13 and q0 - 3 >= 12
    # the targets of the listed moves lie in the rows q0-2 .. q0+15 and N-14 .. N-2; these rows are also the same
    # for every N >= N1: q0 + 15 < N - 12, so the rows up to q0 + 15 are full rows
    assert q0 + 15 < N1 - 12 and q0 - 2 >= 11
    return bad, n1, n2
if __name__ == "__main__":
    Nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 2003
    vals = {N: direct(N) for N in range(N1, Nmax + 1, 4)}
    ok1 = all(v == 14 for v in vals.values())
    print(f"part 1: the labelling is valid with |B| - |N| = 14 for every N = 3 (mod 4), {N1} <= N <= {Nmax}: {ok1}")
    small = {N: direct(N) for N in range(27, N1, 4)}
    print("        (for smaller N the same rule gives:", small, "; None = not valid there)")
    bad, n1, n2 = prove()
    print(f"part 2: {n1} + {n2} pairs (cell labelled B or O, move to a cell labelled B or I) in the listed rows;")
    print(f"        pairs that could violate the rule for some N >= {N1}: {bad}")
    print("PROVED: rho(N, 12) >= 14 for every N = 3 (mod 4), N >= " + str(N1) if ok1 and bad == 0 else "NOT PROVED")
