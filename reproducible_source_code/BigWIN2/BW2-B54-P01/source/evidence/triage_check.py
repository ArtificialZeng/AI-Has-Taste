"""Exact, dependency-free arithmetic checks for the triaged k=11 instance."""


def mul(x, y):
    return [
        [sum(x[i][k] * y[k][j] for k in range(len(y))) for j in range(len(y[0]))]
        for i in range(len(x))
    ]


def power(x, exponent):
    result = [[1 if i == j else 0 for j in range(len(x))] for i in range(len(x))]
    base = x
    while exponent:
        if exponent & 1:
            result = mul(result, base)
        base = mul(base, base)
        exponent //= 2
    return result


A = [[1, 12], [11, 1]]
B = [[1, 132], [1, 1]]
P = [[1, 12], [1, 11]]
PINV = [[-11, 12], [1, -1]]  # det(P)=-1
S = [
    [3639181777320288676873, 675432186255210239002500],
    [56286015521267519916875, 330834707029117152443],
]

assert mul(A, P) == mul(P, B)
assert mul(PINV, P) == [[1, 0], [0, 1]]
assert S == mul(PINV, power(A, 22))
assert all(entry >= 0 for row in S for entry in row)
assert mul(S, A) == mul(B, S)
assert mul(P, S) == power(A, 22)
assert mul(S, P) == power(B, 22)

# This minimality is only for S_l=P^{-1}A^l, not for arbitrary SE witnesses.
for lag in range(1, 22):
    trial = mul(PINV, power(A, lag))
    assert any(entry < 0 for row in trial for entry in row)

print("PASS: exact similarity and lag-22 shift-equivalence identities verified")

