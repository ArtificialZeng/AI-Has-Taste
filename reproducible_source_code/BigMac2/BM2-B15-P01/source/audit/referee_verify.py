#!/usr/bin/env python3
"""Fresh exact checks for the frozen cyclic-prefix claim.

This verifier deliberately uses list-of-lists matrices and a separately
implemented polynomial-field arithmetic path rather than importing the
researcher's bit-row verifier.
"""

from hashlib import sha256
from itertools import product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def poly_mod(a, b):
    while a.bit_length() >= b.bit_length():
        a ^= b << (a.bit_length() - b.bit_length())
    return a


def field_mul(a, b, modulus):
    value = 0
    while b:
        if b & 1:
            value ^= a
        a <<= 1
        b >>= 1
    return poly_mod(value, modulus)


def field_pow(a, exponent, modulus):
    value = 1
    while exponent:
        if exponent & 1:
            value = field_mul(value, a, modulus)
        a = field_mul(a, a, modulus)
        exponent >>= 1
    return value


def irreducible_moduli(n):
    result = []
    for modulus in range((1 << n) | 1, 1 << (n + 1), 2):
        has_factor = False
        for degree in range(1, n // 2 + 1):
            for divisor in range(1 << degree, 1 << (degree + 1)):
                if poly_mod(modulus, divisor) == 0:
                    has_factor = True
                    break
            if has_factor:
                break
        if not has_factor:
            result.append(modulus)
    return result


def determinant(matrix):
    size = len(matrix)
    if size == 0:
        return 1
    work = [row[:] for row in matrix]
    for column in range(size):
        pivot = next((r for r in range(column, size) if work[r][column]), None)
        if pivot is None:
            return 0
        work[column], work[pivot] = work[pivot], work[column]
        for row in range(column + 1, size):
            if work[row][column]:
                work[row] = [x ^ y for x, y in zip(work[row], work[column])]
    return 1


def rank(matrix):
    if not matrix:
        return 0
    work = [row[:] for row in matrix]
    rows, columns = len(work), len(work[0])
    pivot_row = 0
    for column in range(columns):
        pivot = next((r for r in range(pivot_row, rows) if work[r][column]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        for row in range(rows):
            if row != pivot_row and work[row][column]:
                work[row] = [x ^ y for x, y in zip(work[row], work[pivot_row])]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def adjugate(matrix):
    n = len(matrix)
    # Output row a, column b is the minor obtained by deleting row b,
    # column a, exactly matching the frozen convention.
    return [
        [
            determinant([
                [matrix[h][j] for j in range(n) if j != a]
                for h in range(n) if h != b
            ])
            for b in range(n)
        ]
        for a in range(n)
    ]


def matvec(matrix, vector):
    return [sum(x * y for x, y in zip(row, vector)) & 1 for row in matrix]


def bits_to_int(vector):
    return sum(bit << i for i, bit in enumerate(vector))


def int_to_bits(value, n):
    return [(value >> i) & 1 for i in range(n)]


def evaluate(matrix, operand, modulus):
    n = len(matrix)
    image = matvec(matrix, operand)
    element = bits_to_int(image)
    if element == 0:
        inverse = 0
    else:
        inverse = field_pow(element, (1 << n) - 2, modulus)
        assert field_mul(element, inverse, modulus) == 1
    return bits_to_int(matvec(adjugate(matrix), int_to_bits(inverse, n)))


def assignment(n, variables, subset_mask):
    matrix = [[0] * n for _ in range(n)]
    operand = [0] * n
    for index, variable in enumerate(variables):
        if subset_mask & (1 << index):
            if variable[0] == "p":
                matrix[variable[1]][variable[2]] = 1
            else:
                operand[variable[1]] = 1
    return matrix, operand


def cyclic_prefix_check(n, modulus):
    i = 1
    r = 0 if n == 2 else n - 1
    alpha_inverse = field_pow(2, (1 << n) - 2, modulus)
    assert (alpha_inverse >> r) & 1
    assert r != i

    prefix = []
    seen = set()
    coefficients = []
    for k in range(n):
        sigma = lambda h: (h + k) % n
        variables = [("p", h, sigma(h)) for h in range(n) if h != r]
        variables.append(("u", sigma(i)))
        assert len(set(variables)) == n
        assert seen.isdisjoint(variables)
        seen.update(variables)

        coefficient = 0
        for subset_mask in range(1 << n):
            matrix, operand = assignment(n, variables, subset_mask)
            coefficient ^= evaluate(matrix, operand, modulus)
        expected = 1 << sigma(r)
        assert coefficient == expected
        coefficients.append(coefficient)
        prefix.append(variables)

    universe = {("p", h, j) for h in range(n) for j in range(n)}
    universe.update(("u", j) for j in range(n))
    assert universe - seen == {("p", r, j) for j in range(n)}
    return coefficients


def complete_anf_check(n, modulus):
    d = n * n + n
    truth = []
    for mask in range(1 << d):
        matrix = [
            [(mask >> (n * h + j)) & 1 for j in range(n)]
            for h in range(n)
        ]
        operand = [(mask >> (n * n + j)) & 1 for j in range(n)]
        truth.append(evaluate(matrix, operand, modulus))
    anf = truth[:]
    for bit in range(d):
        for mask in range(1 << d):
            if mask & (1 << bit):
                anf[mask] ^= anf[mask ^ (1 << bit)]
    support = [mask for mask, coefficient in enumerate(anf) if coefficient]
    return {
        "n": n,
        "modulus_bitmask": modulus,
        "support_size": len(support),
        "minimum_degree": min(mask.bit_count() for mask in support),
        "maximum_degree": max(mask.bit_count() for mask in support),
        "coordinate_monomials": sum(value.bit_count() for value in anf),
    }


def check_snapshot():
    snapshot = json.loads((ROOT / "audit/snapshot.json").read_text())
    actual = {}
    for relative_path, expected in snapshot["files"].items():
        digest = sha256((ROOT / relative_path).read_bytes()).hexdigest()
        assert digest == expected
        actual[relative_path] = digest
    encoded = json.dumps(actual, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    assert sha256(encoded.encode()).hexdigest() == snapshot["digest"]
    return snapshot["digest"], len(actual)


def main():
    snapshot_digest, frozen_files = check_snapshot()
    counts = {}
    coefficient_checks = 0
    complete = []
    for n in range(2, 8):
        moduli = irreducible_moduli(n)
        counts[str(n)] = len(moduli)
        for modulus in moduli:
            coefficient_checks += len(cyclic_prefix_check(n, modulus))
            if n <= 3:
                complete.append(complete_anf_check(n, modulus))
    print(json.dumps({
        "snapshot_digest": snapshot_digest,
        "frozen_files_verified": frozen_files,
        "irreducible_moduli_by_degree": counts,
        "prefix_coefficients_verified": coefficient_checks,
        "complete_anf": complete,
    }, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
