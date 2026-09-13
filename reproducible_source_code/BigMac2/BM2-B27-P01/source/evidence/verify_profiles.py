"""Exact symbolic checks for the five entropy profiles and derivatives."""

import sympy as sp


p = sp.symbols("p", positive=True)
q = 1 - p
A = p**3
B = p**2 * q
C = p * q**2
D = q**3
R = p * q
b = -p * sp.log(p) - q * sp.log(q)


def entropy(atoms):
    return -sum(atom * sp.log(atom) for atom in atoms)


profiles = [
    ([A, 3 * B, 3 * C, D], 3 * b - 3 * R * sp.log(3)),
    ([A, 2 * B, R, 2 * C, D], 3 * b - R * b - 2 * R * sp.log(2)),
    ([A, B, 2 * B, C, 2 * C, D], 3 * b - 2 * R * sp.log(2)),
    ([A, B, B, R, C, C, D], 3 * b - R * b),
    ([A, B, B, B, C, C, C, D], 3 * b),
]

for case, (atoms, target) in enumerate(profiles, start=1):
    difference = sp.expand_log(entropy(atoms) - target, force=True)
    assert sp.simplify(sp.factor(sp.expand(difference))) == 0
    print(f"case {case} atom/profile identity: exact zero")

assert sp.simplify(sp.diff(b, p, 2) + 1 / R) == 0
rb_second = -2 * b + 2 * (1 - 2 * p) * sp.log(q / p) - 1
derivative_difference = sp.expand_log(sp.diff(R * b, p, 2) - rb_second, force=True)
assert sp.simplify(sp.expand(derivative_difference)) == 0
print("b'' = -1/(p(1-p)): exact identity")
print("(p(1-p)b)'' formula: exact identity")

parameters = [
    (0, 3 * sp.log(3)),
    (1, 2 * sp.log(2)),
    (0, 2 * sp.log(2)),
    (1, 0),
    (0, 0),
]
for case, (delta, c) in enumerate(parameters, start=1):
    profile = 3 * b - delta * R * b - c * R
    if delta == 0:
        target_second = -3 / R + 2 * c
    else:
        target_second = -3 / R + 2 * b - 2 * (1 - 2 * p) * sp.log(q / p) + 1 + 2 * c
    difference = sp.expand_log(sp.diff(profile, p, 2) - target_second, force=True)
    assert sp.simplify(sp.expand(difference)) == 0
    print(f"case {case} second-derivative identity: exact zero")

