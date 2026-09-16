#!/usr/bin/env python3
"""Exact checks for the K-independent block proof.

The assertions under ``symbolic_local_checks`` are precisely the finite local
mex identities used in evidence/uniform-block-proof.md.  The later recurrence
replays are redundant finite implementation checks, not an extrapolation in K.
"""


A = tuple(map(int, "0000111122"))
B = tuple(map(int, "2331020010"))
D = tuple(map(int, "1121020010"))
F = tuple(map(int, "112102"))
W = tuple(map(int, "02101"))


def mex(items):
    items = set(items)
    answer = 0
    while answer in items:
        answer += 1
    return answer


def proposed_value(K, n):
    """Value of A^K 0 B D^(K-1) F W^infinity at index n."""
    c = 10 * K + 1
    q = 2 * c + 5
    if n < c:
        return A[n % 10]
    t = n - c
    if t < 10:
        return B[t]
    if t < c - 1:
        return D[(t - 10) % 10]
    if t < c + 5:
        return F[t - (c - 1)]
    return W[(n - q) % 5]


def option_triple(K, n):
    c = 10 * K + 1
    return tuple(proposed_value(K, n - s) for s in (4, 6, c))


def symbolic_local_checks():
    # Initial and circular checks for A (the {4,6} recurrence before c).
    for n in range(10):
        options = (A[n - s] for s in (4, 6) if s <= n)
        assert mex(options) == A[n]
    for r in range(10):
        assert mex((A[(r - 4) % 10], A[(r - 6) % 10])) == A[r]

    # B starts at c.  A third option A[t] comes from subtracting c.
    b_options = []
    for t in range(10):
        x4 = A[(1 + t - 4) % 10] if t < 4 else B[t - 4]
        x6 = A[(1 + t - 6) % 10] if t < 6 else B[t - 6]
        options = (x4, x6, A[t])
        b_options.append(options)
        assert mex(options) == B[t]

    # Every D block sees circular D values at distances 4 and 6 and A[j]
    # at distance c.  The first seam is covered by B[4:] == D[4:].
    assert B[4:] == D[4:]
    d_options = []
    for j in range(10):
        options = (D[(j - 4) % 10], D[(j - 6) % 10], A[j])
        d_options.append(options)
        assert mex(options) == D[j]

    # K=1 represents a B-to-F seam; K=2 represents every D-to-F seam.
    f_options = [option_triple(1, 2 * 11 - 1 + j) for j in range(6)]
    assert f_options == [option_triple(2, 2 * 21 - 1 + j) for j in range(6)]
    assert tuple(mex(options) for options in f_options) == F

    # The first six W values include every 4/6 boundary interaction with F.
    # K=1 and K=2 again cover the absent-D and present-D cases.
    w_options = []
    for K in (1, 2):
        c = 10 * K + 1
        q = 2 * c + 5
        options = [option_triple(K, q + u) for u in range(6)]
        assert tuple(mex(item) for item in options) == W + W[:1]
        w_options.append(options)
    assert w_options[0] == w_options[1]

    # Once u>=6, the two short-move options are the cyclic neighbours in W.
    # For every value occurring in the proposed word, the mex identity holds
    # exactly when the c-predecessor differs from the proposed W value.
    for r in range(5):
        neighbours = (W[(r + 1) % 5], W[(r - 1) % 5])
        for h in range(4):
            assert (mex(neighbours + (h,)) == W[r]) == (h != W[r])

    # The possible finite c-predecessor blocks are pointwise different from W
    # at their actual alignments.  In the final regime W is shifted by one.
    assert all(D[j] != W[j % 5] for j in range(10))
    assert all(F[j] != W[j % 5] for j in range(6))
    assert all(W[j] != W[(j + 1) % 5] for j in range(5))

    return b_options, d_options, f_options, w_options[0]


def replay(K, stop):
    """Replay the SG recurrence and compare it with the proposed word."""
    c = 10 * K + 1
    values = []
    for n in range(stop):
        options = (values[n - s] for s in (4, 6, c) if s <= n)
        values.append(mex(options))
        assert values[-1] == proposed_value(K, n)
    q = 2 * c + 5
    assert values[q - 1] == 2
    assert values[q + 4] == 1


if __name__ == "__main__":
    tables = symbolic_local_checks()
    # Finite replays guard the formula implementation.  Universality comes
    # from the local reductions above and the written proof, not these samples.
    for K in tuple(range(1, 51)) + (100, 1000):
        c = 10 * K + 1
        replay(K, 3 * c + 20)
    labels = ("B", "D", "F", "W-boundary")
    for label, table in zip(labels, tables):
        encoded = " ".join("".join(map(str, row)) for row in table)
        print(f"{label} option tuples: {encoded}")
    print("symbolic local identities: PASS")
    print("redundant recurrence replays: K=1,...,50,100,1000 PASS")
