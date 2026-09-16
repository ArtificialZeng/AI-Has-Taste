"""Exact certificate: no nonnegative 2x2 lag-4 SE from A_11 to B_11.

For R=[[x,12z],[z,11x]], AR=RB. Conversely, every nonnegative integer
2x2 solution of AR=RB has this form. Similarly, every S with SA=BS is
S=[[11u,12v],[v,u]]. Since

    A^4 = [[18217, 6384], [5852, 18217]],

the product identity RS=A^4 is equivalent to

    11*x*u + 12*z*v = 18217,   x*v + z*u = 532.                 (1)

The proof checks a short necessary-condition certificate for (1), and then
independently exhausts the original four-variable system.
"""

from math import isqrt


def mul(left, right):
    return [
        [sum(left[i][k] * right[k][j] for k in range(len(right)))
         for j in range(len(right[0]))]
        for i in range(len(left))
    ]


A = [[1, 12], [11, 1]]
A4 = [[18217, 6384], [5852, 18217]]
assert mul(mul(A, A), mul(A, A)) == A4

# Put p=xu, q=zv, r=xv, s=zu. The first equation in (1) forces
# q=1+11t and p=1655-12t for exactly 0 <= t <= 137. Also pq=rs,
# while the second equation gives r+s=532. Thus
# H(t)=532^2/4-pq=132t^2-18193t+69101 must equal ((r-s)/2)^2.
square_residues_mod_64 = {n * n % 64 for n in range(64)}
assert square_residues_mod_64 == {0, 1, 4, 9, 16, 17, 25, 33, 36, 41, 49, 57}


def h(t):
    return 132 * t * t - 18193 * t + 69101


assert h(4) == -1559 and h(133) == -15620
# H is convex, so on [4,133] it is at most its larger endpoint value.
for t in range(4, 134):
    assert h(t) < 0

edge_cases = [0, 1, 2, 3, 134, 135, 136, 137]
edge_residues = [h(t) % 64 for t in edge_cases]
assert edge_residues == [45, 32, 27, 30, 23, 58, 37, 24]
assert all(residue not in square_residues_mod_64 for residue in edge_residues)

# Independent finite replay of (1): xu <= floor(18217/11)=1656.
# Each x,u determines zv. Divisor enumeration is complete. On zv=0 the
# axes are bounded by the second equation; u=v=0 cannot satisfy the first.
solutions = []
for x in range(1657):
    for u in range(1657):
        remainder = 18217 - 11 * x * u
        if remainder < 0:
            break
        if remainder % 12:
            continue
        zv = remainder // 12
        if zv == 0:
            pairs = [(0, v) for v in range(533)]
            pairs += [(z, 0) for z in range(1, 533)]
        else:
            pairs = []
            divisor = 1
            while divisor * divisor <= zv:
                if zv % divisor == 0:
                    pairs.append((divisor, zv // divisor))
                    if divisor * divisor != zv:
                        pairs.append((zv // divisor, divisor))
                divisor += 1
        for z, v in pairs:
            if x * v + z * u == 532:
                solutions.append((x, z, u, v))

assert solutions == []

for t in range(138):
    value = h(t)
    assert value < 0 or isqrt(value) ** 2 != value

print("PASS: no nonnegative 2x2 lag-4 shift equivalence for k=11")
