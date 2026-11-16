"""Stand-alone exact check of whirling knight's tours (definitions: Knuth, TAOCP Pre-Fascicle 8A, ex. 227/229).

Each line of the input file is  "n=<n> coils=<c> tour=i,j i,j ...".  For every line the program checks that
  * the cells are exactly the cells of the n x n board (centre removed when n is odd), each visited once;
  * every step, including the closing one, is a knight move that turns counterclockwise about the pivot,
    i.e. (i-p)(j'-q) > (i'-p)(j-q) with p = q = (n-1)/2;
  * the winding number about the pivot equals the stated number of coils.
The winding number is counted exactly as the number of steps that cross a fixed ray from the pivot that contains no
cell (direction (-1, 1/(2n)) in centred coordinates), using integer cross products only.

  python check_tour.py tours_n_coils.txt        (Python 3 standard library only)
"""
import sys
from fractions import Fraction as F

ok_all = True
for line in open(sys.argv[1]):
    if not line.strip():
        continue
    head, tour = line.strip().split(" tour=")
    n = int(head.split()[0][2:]); claimed = int(head.split()[1][6:])
    T = [tuple(map(int, s.split(","))) for s in tour.split()]
    p = F(n - 1, 2)
    cells = {(i, j) for i in range(n) for j in range(n)}
    if n % 2:
        cells.discard(((n - 1) // 2, (n - 1) // 2))
    ok = len(T) == len(cells) and set(T) == cells
    ray = (F(-1), F(1, 2 * n))
    coils = 0
    for k in range(len(T)):
        (i, j), (i2, j2) = T[k], T[(k + 1) % len(T)]
        u, w = (i - p, j - p), (i2 - p, j2 - p)
        ok &= {abs(i - i2), abs(j - j2)} == {1, 2}
        ok &= u[0] * w[1] - w[0] * u[1] > 0
        # the ray lies strictly inside the (less than half-turn) sweep from u to w
        if u[0] * ray[1] - ray[0] * u[1] > 0 and ray[0] * w[1] - w[0] * ray[1] > 0:
            coils += 1
    ok &= coils == claimed
    ok_all &= ok
    print(f"n={n}: {len(T)} cells, coils = {coils} (claimed {claimed}) -> {'VALID' if ok else 'INVALID'}")
print("ALL VALID" if ok_all else "SOME TOUR IS INVALID")
