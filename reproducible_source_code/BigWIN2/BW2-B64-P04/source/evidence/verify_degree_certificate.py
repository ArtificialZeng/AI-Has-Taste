#!/usr/bin/env python3
"""Exact small-degree checks of the coefficient in degree_certificate.md.

The default run enumerates every monic irreducible binary polynomial in
degrees 3, 4, and 5.  For each polynomial it constructs the trace Gram
matrix, chooses the first off-diagonal 1 in its inverse, builds the two-path
monomial, and evaluates that ANF coefficient directly by the Boolean Mobius
formula.  Only integer bit operations are used.
"""


def degree(x):
    return x.bit_length() - 1


def polynomial_multiply(a, b):
    z = 0
    while b:
        if b & 1:
            z ^= a
        b >>= 1
        a <<= 1
    return z


def polynomial_mod(a, p):
    d = degree(p)
    while a and degree(a) >= d:
        a ^= p << (degree(a) - d)
    return a


def field_multiply(a, b, p):
    return polynomial_mod(polynomial_multiply(a, b), p)


def field_square(a, p):
    return field_multiply(a, a, p)


def field_inverse(a, p, n):
    if not a:
        return 0
    z, x, exponent = 1, a, (1 << n) - 2
    while exponent:
        if exponent & 1:
            z = field_multiply(z, x, p)
        x = field_square(x, p)
        exponent >>= 1
    return z


def field_trace(a, p, n):
    z, x = 0, a
    for _ in range(n):
        z ^= x
        x = field_square(x, p)
    return z


def polynomial_gcd(a, b):
    while b:
        a, b = b, polynomial_mod(a, b)
    return a


def is_irreducible(p, n):
    x, y = 2, 2
    for _ in range(1, n // 2 + 1):
        y = field_square(y, p)
        if polynomial_gcd(y ^ x, p) != 1:
            return False
    y = x
    for _ in range(n):
        y = field_square(y, p)
    return y == x


def matrix_inverse_binary(a):
    n = len(a)
    rows = [
        sum(a[i][j] << j for j in range(n)) | (1 << (n + i))
        for i in range(n)
    ]
    for column in range(n):
        pivot = next(i for i in range(column, n) if (rows[i] >> column) & 1)
        rows[column], rows[pivot] = rows[pivot], rows[column]
        for i in range(n):
            if i != column and ((rows[i] >> column) & 1):
                rows[i] ^= rows[column]
    return [
        [(rows[i] >> (n + j)) & 1 for j in range(n)] for i in range(n)
    ]


def determinant_binary(a):
    n = len(a)
    rows = [sum(a[i][j] << j for j in range(n)) for i in range(n)]
    rank = 0
    for column in range(n):
        pivot = next(
            (i for i in range(rank, n) if (rows[i] >> column) & 1), None
        )
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for i in range(rank + 1, n):
            if (rows[i] >> column) & 1:
                rows[i] ^= rows[rank]
        rank += 1
    return int(rank == n)


def direct_certificate(n, p):
    basis, x = [], 1
    for _ in range(n):
        basis.append(x)
        x = field_multiply(x, 2, p)
    gram = [
        [
            field_trace(field_multiply(basis[i], basis[j], p), p, n)
            for j in range(n)
        ]
        for i in range(n)
    ]
    dual_coordinates = matrix_inverse_binary(gram)
    r, a = next(
        (r, a)
        for r in range(n)
        for a in range(n)
        if r != a and dual_coordinates[a][r]
    )

    s, k = 0, 1
    columns = [j for j in range(n) if j != s]
    columns.remove(k)
    columns.insert(0, k)
    rows = [i for i in range(n) if i not in (r, a)] + [a]
    first = [(rows[i], columns[i]) for i in range(n - 1)]
    second = [(r, s)] + [(rows[i], columns[i + 1]) for i in range(n - 2)]
    edges = first + second
    variables = [("p", i, j) for i, j in edges] + [
        ("u", j) for j in range(n) if j != s
    ]

    coefficient = 0
    for mask in range(1 << len(variables)):
        matrix = [[0] * n for _ in range(n)]
        vector = [0] * n
        for bit, variable in enumerate(variables):
            if not ((mask >> bit) & 1):
                continue
            if variable[0] == "p":
                matrix[variable[1]][variable[2]] = 1
            else:
                vector[variable[1]] = 1

        product = [
            sum(matrix[i][j] * vector[j] for j in range(n)) & 1
            for i in range(n)
        ]
        field_element = sum(product[i] << i for i in range(n))
        inverse = field_inverse(field_element, p, n)
        inverse_coordinates = [(inverse >> i) & 1 for i in range(n)]
        output_k = 0
        for a_prime in range(n):
            minor = [
                [matrix[i][j] for j in range(n) if j != k]
                for i in range(n)
                if i != a_prime
            ]
            output_k ^= determinant_binary(minor) & inverse_coordinates[a_prime]
        coefficient ^= output_k

    predicted = dual_coordinates[a][r]
    assert predicted == coefficient == 1
    return r, a, coefficient


def main():
    total = 0
    for n in range(3, 6):
        polynomials = [
            p
            for p in range((1 << n) | 1, 1 << (n + 1), 2)
            if is_irreducible(p, n)
        ]
        print(f"n={n}: {len(polynomials)} irreducible polynomials")
        for p in polynomials:
            r, a, coefficient = direct_certificate(n, p)
            total += 1
            print(f"  p={p:#x}, (r,a)=({r},{a}), coefficient={coefficient}")
    print(f"PASS: {total} exact direct Mobius coefficient checks")


if __name__ == "__main__":
    main()
