#!/usr/bin/env python3
"""Independent exact projector/marginal audit for win-00085-p01.

This checker deliberately does not import or call the triage support-profile
checker.  It constructs ordinary dense Pauli matrices over the Gaussian
integers, multiplies them as matrices, forms each normalized code projector
rho = 2^{-n} sum_{g in S} g, performs every partial trace entry by entry, and
computes every marginal rank by exact Gaussian-rational elimination.
"""

from fractions import Fraction
from itertools import combinations


JOB_ID = "win-00085-p01-research-fce2de65d535"

CASES = {
    "S_A": ("ZZZZI", "XXIIX", "IIXXX"),
    "S_B": ("ZZIZX", "XIZXI", "IXXYI"),
    "S_+": ("XXIIXX", "IIXXXX", "ZZZZIX"),
    "S_-": ("XXZXII", "ZZXYII", "IZZZXX"),
}

# A Gaussian integer is the exact pair a + b i.
ZERO = (0, 0)
ONE = (1, 0)
MINUS_ONE = (-1, 0)
IUNIT = (0, 1)
MINUS_I = (0, -1)

PAULI_1 = {
    "I": ((ONE, ZERO), (ZERO, ONE)),
    "X": ((ZERO, ONE), (ONE, ZERO)),
    "Y": ((ZERO, MINUS_I), (IUNIT, ZERO)),
    "Z": ((ONE, ZERO), (ZERO, MINUS_ONE)),
}


def gadd(a, b):
    return a[0] + b[0], a[1] + b[1]


def gneg(a):
    return -a[0], -a[1]


def gmul(a, b):
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def madd(left, right):
    return tuple(
        tuple(gadd(left[r][c], right[r][c]) for c in range(len(left[0])))
        for r in range(len(left))
    )


def mmul(left, right):
    rows, middle, cols = len(left), len(right), len(right[0])
    result = [[ZERO for _ in range(cols)] for _ in range(rows)]
    # Sparse-aware but otherwise ordinary dense matrix multiplication.
    for r in range(rows):
        for k in range(middle):
            if left[r][k] == ZERO:
                continue
            for c in range(cols):
                if right[k][c] != ZERO:
                    result[r][c] = gadd(result[r][c], gmul(left[r][k], right[k][c]))
    return tuple(tuple(row) for row in result)


def mscale(scalar, matrix):
    return tuple(tuple(gmul(scalar, entry) for entry in row) for row in matrix)


def identity(size):
    return tuple(
        tuple(ONE if r == c else ZERO for c in range(size))
        for r in range(size)
    )


def kron(left, right):
    lr, lc, rr, rc = len(left), len(left[0]), len(right), len(right[0])
    return tuple(
        tuple(
            gmul(left[r // rr][c // rc], right[r % rr][c % rc])
            for c in range(lc * rc)
        )
        for r in range(lr * rr)
    )


def word_matrix(word):
    matrix = ((ONE,),)
    for letter in word:
        matrix = kron(matrix, PAULI_1[letter])
    return matrix


def conjugate_transpose(matrix):
    return tuple(
        tuple((matrix[c][r][0], -matrix[c][r][1]) for c in range(len(matrix)))
        for r in range(len(matrix[0]))
    )


def matrix_trace(matrix):
    value = ZERO
    for j in range(len(matrix)):
        value = gadd(value, matrix[j][j])
    return value


def identify_pauli(matrix, n):
    """Recover sign and tensor word from a nonzero dense Pauli matrix."""
    size = 1 << n
    nonzero_rows = [r for r in range(size) if matrix[r][0] != ZERO]
    assert len(nonzero_rows) == 1
    xmask = nonzero_rows[0]
    base = matrix[xmask][0]
    zmask = 0
    for q in range(n):
        bit = 1 << (n - 1 - q)
        column = bit
        row = column ^ xmask
        amplitude = matrix[row][column]
        assert amplitude in (base, gneg(base))
        if amplitude == gneg(base):
            zmask |= bit
    letters = []
    for q in range(n):
        bit = 1 << (n - 1 - q)
        pair = (bool(xmask & bit), bool(zmask & bit))
        letters.append({(False, False): "I", (True, False): "X",
                        (False, True): "Z", (True, True): "Y"}[pair])
    word = "".join(letters)
    unsigned = word_matrix(word)
    scalar = None
    for r in range(size):
        for c in range(size):
            if unsigned[r][c] != ZERO:
                u = unsigned[r][c]
                v = matrix[r][c]
                # All nonzero Pauli entries and the scalar are Gaussian units.
                scalar = gmul(v, (u[0], -u[1]))
                break
        if scalar is not None:
            break
    assert scalar in (ONE, MINUS_ONE, IUNIT, MINUS_I)
    assert matrix == mscale(scalar, unsigned)
    assert scalar in (ONE, MINUS_ONE), "commuting Hermitian product acquired ±i"
    return ("+" if scalar == ONE else "-") + word


def enumerate_group(generator_words):
    n = len(generator_words[0])
    generators = tuple(word_matrix(word) for word in generator_words)
    unit = identity(1 << n)
    for left, right in combinations(generators, 2):
        assert mmul(left, right) == mmul(right, left)
    elements = []
    for selector in range(8):
        matrix = unit
        for j, generator in enumerate(generators):
            if selector & (1 << j):
                matrix = mmul(matrix, generator)
        elements.append((selector, matrix, identify_pauli(matrix, n)))
    assert len({signed for _, _, signed in elements}) == 8
    assert all(matrix == conjugate_transpose(matrix) for _, matrix, _ in elements)
    return elements


def subset_label(mask, n):
    return "{" + ",".join(str(q + 1) for q in range(n) if mask & (1 << q)) + "}"


def word_support_mask(signed_word):
    word = signed_word[1:]
    return sum((letter != "I") << q for q, letter in enumerate(word))


def embed_index(a_index, b_index, kept, traced, n):
    full = 0
    for position, q in enumerate(kept):
        if a_index & (1 << (len(kept) - 1 - position)):
            full |= 1 << (n - 1 - q)
    for position, q in enumerate(traced):
        if b_index & (1 << (len(traced) - 1 - position)):
            full |= 1 << (n - 1 - q)
    return full


def partial_trace(matrix, kept_mask, n):
    kept = [q for q in range(n) if kept_mask & (1 << q)]
    traced = [q for q in range(n) if not (kept_mask & (1 << q))]
    kept_size, traced_size = 1 << len(kept), 1 << len(traced)
    result = [[ZERO for _ in range(kept_size)] for _ in range(kept_size)]
    for ar in range(kept_size):
        for ac in range(kept_size):
            value = ZERO
            for b in range(traced_size):
                row = embed_index(ar, b, kept, traced, n)
                col = embed_index(ac, b, kept, traced, n)
                value = gadd(value, matrix[row][col])
            result[ar][ac] = value
    return tuple(tuple(row) for row in result)


# Exact Gaussian-rational arithmetic, used only by rank elimination.
def qpair(value):
    return Fraction(value[0]), Fraction(value[1])


def qsub(a, b):
    return a[0] - b[0], a[1] - b[1]


def qmul(a, b):
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def qdiv(a, b):
    norm = b[0] * b[0] + b[1] * b[1]
    assert norm != 0
    return ((a[0] * b[0] + a[1] * b[1]) / norm,
            (a[1] * b[0] - a[0] * b[1]) / norm)


def exact_rank(matrix):
    work = [[qpair(entry) for entry in row] for row in matrix]
    rows, cols = len(work), len(work[0])
    rank = 0
    for col in range(cols):
        pivot = next((r for r in range(rank, rows) if work[r][col] != (0, 0)), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        pivot_value = work[rank][col]
        for r in range(rank + 1, rows):
            if work[r][col] == (0, 0):
                continue
            factor = qdiv(work[r][col], pivot_value)
            for c in range(col, cols):
                work[r][c] = qsub(work[r][c], qmul(factor, work[rank][c]))
        rank += 1
        if rank == rows:
            break
    return rank


def power_of_two_log(value):
    assert value > 0 and value & (value - 1) == 0
    return value.bit_length() - 1


def audit_case(name, generator_words):
    n = len(generator_words[0])
    size = 1 << n
    elements = enumerate_group(generator_words)
    projector_numerator = tuple(tuple(ZERO for _ in range(size)) for _ in range(size))
    for _, matrix, _ in elements:
        projector_numerator = madd(projector_numerator, matrix)

    # rho = projector_numerator / 2^n and P_Q = projector_numerator / 8.
    assert matrix_trace(projector_numerator) == (size, 0)
    assert projector_numerator == conjugate_transpose(projector_numerator)
    assert mmul(projector_numerator, projector_numerator) == mscale((8, 0), projector_numerator)
    assert exact_rank(projector_numerator) == 1 << (n - 3)

    profiles = []
    for kept_mask in range(1 << n):
        reduced_numerator = partial_trace(projector_numerator, kept_mask, n)
        direct_rank = exact_rank(reduced_numerator)
        contained = sum(
            (word_support_mask(signed) & ~kept_mask) == 0
            for _, _, signed in elements
        )
        d_value = power_of_two_log(contained)
        predicted_rank = 1 << (kept_mask.bit_count() - d_value)
        assert direct_rank == predicted_rank
        profiles.append((kept_mask, direct_rank, contained, d_value))
    return n, elements, profiles


def histogram(values):
    result = {}
    for value in values:
        result[value] = result.get(value, 0) + 1
    return dict(sorted(result.items()))


def main():
    audited = {name: audit_case(name, words) for name, words in CASES.items()}
    print("# Independent exact code-projector and marginal-rank audit")
    print()
    print(f"Provenance: `{JOB_ID}`")
    print()
    print("All arithmetic below is exact. For each case the checker directly builds dense")
    print("Gaussian-integer matrices, verifies `R^2=8R`, and uses `rho=R/2^n`.")
    print("Every partial trace is formed entry by entry and ranked by exact")
    print("Gaussian-rational elimination; the triage checker is neither imported nor called.")
    print()

    for name in CASES:
        n, elements, profiles = audited[name]
        print(f"## {name}")
        print()
        print(f"`rho_{name[2:]} = 2^-{n} (" + " ".join(signed for _, _, signed in elements) + ")`")
        print()
        print("| selector | signed Pauli | support |")
        print("|---:|:---|:---|")
        for selector, _, signed in elements:
            support = subset_label(word_support_mask(signed), n)
            print(f"| `{selector:03b}` | `{signed}` | `{support}` |")
        print()
        print("| kept subsystem A | direct rank of Tr_(A^c)(rho) | contained group elements | d(A) |")
        print("|:---|---:|---:|---:|")
        for mask, rank, contained, d_value in profiles:
            print(f"| `{subset_label(mask, n)}` | {rank} | {contained} | {d_value} |")
        print()

    n_a, _, profile_a = audited["S_A"]
    n_b, _, profile_b = audited["S_B"]
    low_a = [mask for mask, rank, _, _ in profile_a if mask.bit_count() == 3 and rank == 4]
    low_b = [mask for mask, rank, _, _ in profile_b if mask.bit_count() == 3 and rank == 4]
    assert len(low_a) == len(low_b) == 2
    intersection_a = (low_a[0] & low_a[1]).bit_count()
    intersection_b = (low_b[0] & low_b[1]).bit_count()
    assert (intersection_a, intersection_b) == (1, 2)

    _, _, profile_plus = audited["S_+"]
    _, _, profile_minus = audited["S_-"]
    hist_plus = histogram(rank for mask, rank, _, _ in profile_plus if mask.bit_count() == 4)
    hist_minus = histogram(rank for mask, rank, _, _ in profile_minus if mask.bit_count() == 4)
    assert hist_plus == {8: 3, 16: 12}
    assert hist_minus == {4: 1, 16: 14}

    print("## Separating certificates")
    print()
    print("- Five qubits: the rank-4 three-subsystems are "
          f"`{subset_label(low_a[0], n_a)}`, `{subset_label(low_a[1], n_a)}` for S_A "
          f"(intersection size {intersection_a}), and "
          f"`{subset_label(low_b[0], n_b)}`, `{subset_label(low_b[1], n_b)}` for S_B "
          f"(intersection size {intersection_b}).")
    print(f"- Six qubits: the four-subsystem rank histograms are `{hist_plus}` for S_+ and "
          f"`{hist_minus}` for S_-.")
    print()
    print("`AUDIT_OK`: all four signed projector sums, all subsystem partial traces,")
    print("all exact ranks, and both certificates passed.")


if __name__ == "__main__":
    main()
