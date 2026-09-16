"""Cheap exact triage check of the proposed S4 double-coset skeleton."""

from itertools import permutations


def compose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def inverse(p):
    q = [0] * len(p)
    for i, j in enumerate(p):
        q[j] = i
    return tuple(q)


def generated(n, generators):
    identity = tuple(range(n))
    group = {identity}
    frontier = [identity]
    while frontier:
        x = frontier.pop()
        for g in generators:
            y = compose(x, g)
            if y not in group:
                group.add(y)
                frontier.append(y)
    return group


def double_coset(H, r, L):
    return {compose(compose(h, r), ell) for h in H for ell in L}


def conjugate_group(r, L):
    rinv = inverse(r)
    return {compose(compose(r, ell), rinv) for ell in L}


def cycle_type(p):
    seen = set()
    lengths = []
    for i in range(len(p)):
        if i not in seen:
            j = i
            length = 0
            while j not in seen:
                seen.add(j)
                length += 1
                j = p[j]
            lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


e = (0, 1, 2, 3)
t12 = (1, 0, 2, 3)
t34 = (0, 1, 3, 2)
c1234 = (1, 2, 3, 0)
pi23 = (0, 2, 1, 3)
H = generated(4, [t12, t34])
L = generated(4, [c1234])
C_e = double_coset(H, e, L)
C_pi = double_coset(H, pi23, L)
I_e = H & conjugate_group(e, L)
I_pi = H & conjugate_group(pi23, L)
S4 = set(permutations(range(4)))

assert len(H) == len(L) == 4
assert len(I_e) == 1
assert len(I_pi) == 2
assert len(C_e) == 16 and len(C_pi) == 8
assert C_e.isdisjoint(C_pi) and C_e | C_pi == S4
assert sorted(cycle_type(x) for x in I_pi) == [(1, 1, 1, 1), (2, 2)]

print("|H|=4; |L|=4")
print("double-coset sizes for e,(23): 16,8; disjoint union size 24")
print("intersection orders for e,(23): 1,2")
print("nonidentity type in second intersection: (2,2)")
print("all assertions passed")
