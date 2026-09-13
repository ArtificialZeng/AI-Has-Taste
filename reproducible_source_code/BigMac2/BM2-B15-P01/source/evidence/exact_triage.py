"""Exact small ANFs and sparse certificates. Run from the project root."""
import json
from pathlib import Path


def poly_mod(a, b):
    while a and a.bit_length() >= b.bit_length():
        a ^= b << (a.bit_length() - b.bit_length())
    return a


def irreducibles(n):
    # Any reducible degree-n polynomial has a factor of degree <= n//2.
    return [p for p in range(1 << n, 1 << (n+1))
            if all(poly_mod(p, q) for d in range(1, n//2+1)
                   for q in range(1 << d, 1 << (d+1)))]


def multiply(a, b, p):
    out = 0
    while b:
        if b & 1:
            out ^= a
        a <<= 1
        b >>= 1
    return poly_mod(out, p)


def determinant(rows, n):
    rows = list(rows)
    for col in range(n):
        pivot = next((j for j in range(col, n) if (rows[j] >> col) & 1), None)
        if pivot is None:
            return 0
        rows[col], rows[pivot] = rows[pivot], rows[col]
        for j in range(col+1, n):
            if (rows[j] >> col) & 1:
                rows[j] ^= rows[col]
    return 1


def adjugate(rows, n):
    adj = []
    for a in range(n):
        row = 0
        for b in range(n):
            minor = []
            for h in range(n):
                if h != b:
                    x = rows[h]
                    minor.append((x & ((1 << a)-1)) | ((x >> (a+1)) << a))
            row |= determinant(minor, n-1) << b
        adj.append(row)
    return adj


def matvec(rows, u):
    return sum(((x & u).bit_count() & 1) << i for i, x in enumerate(rows))


def make_evaluator(n, p):
    inv = [0] + [next(b for b in range(1, 1 << n)
                     if multiply(a, b, p) == 1) for a in range(1, 1 << n)]
    cache = {}

    def evaluate(mask):
        pmask = mask & ((1 << (n*n))-1)
        u = mask >> (n*n)
        if pmask not in cache:
            rows = [(pmask >> (n*i)) & ((1 << n)-1) for i in range(n)]
            adj = adjugate(rows, n)
            det = determinant(rows, n)
            for j in range(n):
                assert matvec(rows, matvec(adj, 1 << j)) == (det << j)
                assert matvec(adj, matvec(rows, 1 << j)) == (det << j)
            cache[pmask] = (rows, adj)
        rows, adj = cache[pmask]
        return matvec(adj, inv[matvec(rows, u)])

    return evaluate


def subxor(a, evaluate):
    result, c = 0, a
    while True:
        result ^= evaluate(c)
        if c == 0:
            return result
        c = (c-1) & a


def prefix(n):
    r = 0 if n == 2 else n-1
    return r, [sum(1 << (n*h+(h+k) % n) for h in range(n) if h != r)
               | (1 << (n*n+(1+k) % n)) for k in range(n)]


def main():
    output = {'method': 'integer F_2 arithmetic; no floating point',
              'complete_anf': [], 'sparse_certificates': []}
    for n in range(2, 7):
        for p in irreducibles(n):
            evaluate = make_evaluator(n, p)
            r, supports = prefix(n)
            union, cert = 0, []
            for k, a in enumerate(supports):
                coeff = subxor(a, evaluate)
                expected = 1 << ((r+k) % n)
                assert coeff == expected
                assert a.bit_count() == n
                new = (a & ~union).bit_count()
                assert new == n
                union |= a
                cert.append({'mask': a, 'coefficient': coeff, 'new_variables': new})
            missing = ((1 << (n*n+n))-1) & ~union
            assert missing == ((1 << n)-1) << (r*n)
            output['sparse_certificates'].append(
                {'n': n, 'modulus_bitmask': p, 'omitted_row': r,
                 'prefix': cert, 'missing_mask': missing,
                 'coefficient_evaluations': n*(1 << n)})
            if n <= 3:
                d = n*n+n
                truth = [evaluate(a) for a in range(1 << d)]
                anf = truth[:]
                for bit in range(d):
                    for a in range(1 << d):
                        if a & (1 << bit):
                            anf[a] ^= anf[a ^ (1 << bit)]
                # Independent transform algorithm: direct subset sums for EVERY coefficient.
                assert all(v == subxor(a, truth.__getitem__) for a, v in enumerate(anf))
                ss = [a for a, v in enumerate(anf) if v]
                assert min(a.bit_count() for a in ss) == n
                assert all(anf[a] for a in supports)
                order = supports + [a for a in ss if a not in supports]
                seen, leap = 0, 0
                for a in order:
                    leap = max(leap, (a & ~seen).bit_count())
                    seen |= a
                assert leap == n
                output['complete_anf'].append(
                    {'n': n, 'modulus_bitmask': p, 'truth_table_size': len(truth),
                     'truth_table': truth, 'anf_nonzero': [[a, anf[a]] for a in ss],
                     'support_size': len(ss), 'minimum_degree': n,
                     'maximum_degree': max(a.bit_count() for a in ss),
                     'coordinate_monomials': sum(v.bit_count() for v in anf),
                     'certified_leap': leap,
                     'all_coefficients_checked_by_direct_subset_sum': True})
    Path('evidence/exact-triage.json').write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps({'complete_anf': [
        {k: row[k] for k in ('n', 'modulus_bitmask', 'truth_table_size', 'support_size',
                              'minimum_degree', 'maximum_degree', 'coordinate_monomials',
                              'certified_leap')} for row in output['complete_anf']],
        'sparse_moduli': len(output['sparse_certificates']),
        'sparse_prefix_supports': sum(len(row['prefix']) for row in output['sparse_certificates'])}, indent=2))


if __name__ == '__main__':
    main()
