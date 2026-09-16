"""Exact independent implementation for the research proof dossier.

No imports from earlier experiment scripts, no numerical logarithms, no
random sampling. The infinite assertions are proved in research-moment-proof.md.
"""
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, combinations_with_replacement
from math import comb, factorial, isqrt
from pathlib import Path
import json
import platform

ROOT = Path(__file__).resolve().parent.parent
JOB = 'newwin-00001-p10-research-b1ee08dba39b'


def tableaux(n):
    """Every SSYT of shape 22, exactly once; rows (a,b),(c,d)."""
    for a in range(n):
        for b in range(a, n):
            for c in range(a+1, n):
                for d in range(max(c, b+1), n):
                    yield a, b, c, d


def by_tableaux(y):
    return Counter(y[a]+y[b]+y[c]+y[d] for a, b, c, d in tableaux(len(y)))


def by_contents(y):
    out = Counter()
    for i, j in combinations(range(len(y)), 2):
        out[2*y[i]+2*y[j]] += 1
    for i, j, k in combinations(range(len(y)), 3):
        for r in (i, j, k):
            out[y[i]+y[j]+y[k]+y[r]] += 1
    for inds in combinations(range(len(y)), 4):
        out[sum(y[i] for i in inds)] += 2
    return out


def egf_product(a, b):
    order = len(a)-1
    return [sum(comb(j, k)*a[k]*b[j-k] for k in range(j+1))
            for j in range(order+1)]


def predicted_moments(p):
    p2 = [v*2**j for j, v in enumerate(p)]
    p3 = [v*3**j for j, v in enumerate(p)]
    square = egf_product(p, p)
    fourth = egf_product(square, square)
    double_square = egf_product(p2, p2)
    mixed = egf_product(p, p3)
    return [Fraction(a+3*b-4*c, 12)
            for a, b, c in zip(fourth, double_square, mixed)]


def coefficient(n, j):
    return Fraction(n*(n*n-1+3*2**(j-1)-3**j), 3)


def set_partitions(items):
    if not items:
        yield ()
        return
    first, *tail = items
    for partition in set_partitions(tail):
        yield ((first,),)+partition
        for k in range(len(partition)):
            yield partition[:k]+((first,)+partition[k],)+partition[k+1:]


PARTITIONS = {k: tuple(set_partitions(list(range(k)))) for k in (2, 3, 4)}


def primitive_from_distinct_indices(weights, n, j):
    total = 0
    for partition in PARTITIONS[len(weights)]:
        mobius = 1
        for block in partition:
            mobius *= (-1)**(len(block)-1)*factorial(len(block)-1)
        total += (mobius*n**(len(partition)-1)
                  * sum(sum(weights[i] for i in block)**j for block in partition))
    return total


def coefficient_by_contents(n, j):
    return (Fraction(primitive_from_distinct_indices((2, 2), n, j), 2)
            + Fraction(primitive_from_distinct_indices((2, 1, 1), n, j), 2)
            + Fraction(primitive_from_distinct_indices((1, 1, 1, 1), n, j), 12))


def polynomial_from_moments(p):
    e = [Fraction(1)]
    for k in range(1, len(p)):
        e.append(sum((-1)**(j-1)*e[k-j]*p[j] for j in range(1, k+1))/k)
    return [(-1)**k*v for k, v in enumerate(e)]


def polynomial_from_roots(roots):
    out = [Fraction(1)]
    for x in roots:
        new = [Fraction(0)]*(len(out)+1)
        for j, c in enumerate(out):
            new[j] += c
            new[j+1] -= x*c
        out = new
    return out


def verify_moments(y, weights, denominator, counts):
    n = len(y)
    p = [n]+[Fraction(sum(v**j for v in y), denominator**j) for j in range(1, n+1)]
    q = [Fraction(sum(m*v**j for v, m in weights.items()), denominator**j)
         for j in range(n+1)]
    assert predicted_moments(p) == q
    recovered = [n]
    for j in range(1, n+1):
        c = coefficient(n, j)
        if not c:
            counts['excluded_recovery_samples'] += 1
            return j
        remainder = predicted_moments(recovered+[0])[-1]
        recovered.append((q[j]-remainder)/c)
    assert recovered == p
    assert polynomial_from_moments(recovered) == polynomial_from_roots(
        [Fraction(v, denominator) for v in y])
    counts['complete_moment_and_newton_recoveries'] += 1
    return None


def exp2(k):
    return Fraction(2**k) if k >= 0 else Fraction(1, 2**(-k))


def h2(values):
    return Counter(a*b for a, b in combinations_with_replacement(values, 2))


def decode_h2(values, size):
    """Here ground truth pair products are dyadic rationals with square roots."""
    largest = max(values)
    num, den = isqrt(largest.numerator), isqrt(largest.denominator)
    assert num*num == largest.numerator and den*den == largest.denominator
    prefix = [Fraction(num, den)]
    while len(prefix) < size:
        used = h2(prefix)
        assert all(m <= values.get(v, 0) for v, m in used.items())
        residual = values-used
        prefix.append(max(residual)/prefix[0])
    assert h2(prefix) == values
    return prefix


def verify_boundary(y, weights, counts):
    if len(y) not in (2, 4):
        return
    parts = [exp2(v) for v in y]
    obs = Counter({exp2(v): m for v, m in weights.items()})
    if len(y) == 2:
        e2 = exp2(sum(y))
        assert obs == Counter({e2*e2: 1})
        assert [1, -sum(parts), e2] == polynomial_from_roots(parts)
    else:
        product = exp2(sum(y))
        assert sum(v*m for v, m in weights.items()) == 20*sum(y)
        pair_products = decode_h2(obs+Counter({product: 1}), 6)
        e2 = sum(pair_products)
        e3 = (e2*e2-sum(v*m for v, m in obs.items()))/sum(parts)
        assert [1, -sum(parts), e2, -e3, product] == polynomial_from_roots(parts)
    counts['fixed_sum_boundary_recoveries'] += 1


def main():
    source_hash = sha256((ROOT/'source.md').read_bytes()).hexdigest()
    proof_hash = sha256((ROOT/'evidence/research-moment-proof.md').read_bytes()).hexdigest()
    counts = Counter()
    for n in range(2, 65):
        assert len(tuple(tableaux(n))) == n*n*(n*n-1)//12
        for j in range(1, n+1):
            assert coefficient_by_contents(n, j) == coefficient(n, j)
            counts['mobius_coefficient_checks'] += 1

    grid_records = []
    for n in range(2, 9):
        buckets = {}
        collisions = 0
        for y in combinations_with_replacement(range(-2, 3), n):
            weights = by_tableaux(y)
            assert weights == by_contents(y)
            verify_moments(y, weights, 1, counts)
            verify_boundary(y, weights, counts)
            key = tuple(sorted(weights.items()))
            total = sum(exp2(v) for v in y)
            if key in buckets:
                assert n in (2, 4)
                assert all(total != old_total for _, old_total in buckets[key])
                collisions += 1
            buckets.setdefault(key, []).append((y, total))
            counts['exhaustive_grid_lists'] += 1
        grid_records.append({'length': n, 'lists': comb(n+4, 4),
                             'distinct_output_multisets': len(buckets),
                             'repeated_output_keys': collisions,
                             'same_sum_collisions': 0})

    # Chosen after writing statement v1: repeated, translated, separated,
    # and near-coincident exact log coordinates, plus excluded residue classes.
    heldout = []
    for n in (9, 10, 11, 12, 13, 14, 15, 16, 20, 22, 26, 34, 46, 60, 61):
        families = [
            ('constant', (7,)*n, 1),
            ('two_clusters', (0,)*(n//2)+(1000,)*(n-n//2), 1),
            ('irregular_rational', tuple((17*i*i+3*i)%101-50 for i in range(n)), 1009),
            ('translated_progression', tuple(97+3*i for i in range(n)), 1),
        ]
        for name, y, denominator in families:
            weights = by_tableaux(y)
            assert weights == by_contents(y)
            stop = verify_moments(y, weights, denominator, counts)
            assert stop == (5 if n == 14 else None)
            heldout.append({'length': n, 'family': name,
                            'log_numerators': list(y), 'log_denominator': denominator,
                            'tableaux': sum(weights.values()), 'recovery_zero_order': stop})
            counts['heldout_structured_samples'] += 1

    # A finite coefficient certificate, with a rigorously proved stopping rule:
    # A_(j+1)-A_j = 2*3^j-3*2^(j-1)>0 for j>=1.
    bound = 10**6
    squares = []
    orders = []
    j = 1
    while True:
        value = 1+3**j-3*2**(j-1)
        root = isqrt(value)
        orders.append({'order': j, 'A_j': value, 'floor_sqrt': root,
                       'is_square': root*root == value})
        if value > bound*bound:
            break
        if root*root == value and root >= 2:
            squares.append({'length': root, 'zero_order': j})
        j += 1
    assert squares == [{'length': 2, 'zero_order': 2},
                       {'length': 4, 'zero_order': 3},
                       {'length': 14, 'zero_order': 5}]
    residues = [n for n in range(60)
                if n % 4 == 2 and n % 3 in (1, 2) and n % 5 in (1, 4)]
    assert residues == [14, 26, 34, 46]
    for j in range(4, 2049):
        value = 1+3**j-3*2**(j-1)
        if j % 2 == 0:
            assert value % 8 == 2
        else:
            assert (value % 8, value % 3, value % 5) == (4, 1, 1)

    witnesses = []
    for ya, yb in [((2, 0), (1, 1)), ((3, 1, 1, 1), (2, 2, 2, 0))]:
        a, b = [int(exp2(v)) for v in ya], [int(exp2(v)) for v in yb]
        wa, wb = by_tableaux(ya), by_tableaux(yb)
        assert wa == wb and sum(a) != sum(b)
        witnesses.append({'a': a, 'b': b, 'sum_a': sum(a), 'sum_b': sum(b),
                           'complete_common_output': [[int(exp2(v)), m]
                                                     for v, m in sorted(wa.items())],
                           'scope': 'Unequal sums; not a counterexample to source.md.'})

    assert source_hash == sha256((ROOT/'source.md').read_bytes()).hexdigest()
    output = {
        'job_id': JOB, 'generated_at_utc': datetime.now(timezone.utc).isoformat(),
        'python': platform.python_version(), 'arithmetic': 'exact integers and Fraction',
        'source_sha256': source_hash, 'statement_v1_sha256': proof_hash,
        'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'independence_scope': 'Fresh code; no imports from earlier experiments; same proposer context, not referee review.',
        'counts': dict(counts),
        'grid_domain': 'Every nondecreasing integer log-base-2 list over {-2,-1,0,1,2}, lengths 2..8; positive dyadic rational inputs.',
        'grid_results': grid_records, 'heldout_samples': heldout,
        'necessary_exception_residues_mod60': residues,
        'finite_length_coefficient_bound': bound,
        'coefficient_zero_pairs_up_to_length_bound': squares,
        'finite_length_certificate': orders,
        'unequal_sum_boundary_witnesses': witnesses,
        'limitations': 'Finite exact verification only; no all-length resolution, no counterexample at length 14, no priority or independent-audit certification.'
    }
    destination = ROOT/'evidence/research-moment-check.json'
    temporary = destination.with_suffix('.json.tmp')
    temporary.write_text(json.dumps(output, indent=2)+'\n')
    temporary.replace(destination)
    print(json.dumps({'output': str(destination.relative_to(ROOT)), 'counts': dict(counts),
                      'grid_results': grid_records, 'finite_bound': bound,
                      'zero_pairs': squares}, indent=2), flush=True)


if __name__ == '__main__':
    main()
