"""Exact binary-capacity path counter, research pass 1.

Each interval [left,right] stores coefficients of binom(x-left,k).
No iteration over a capacity-sized domain occurs in compressed_count.
Only Python arbitrary-precision integers are used. See m2-compressed-proof.md.
"""

from dataclasses import dataclass


def binom_int(n, k):
    """Polynomial binomial coefficient, including negative integer n."""
    result = 1
    for j in range(1, k + 1):
        result = result * (n - j + 1) // j
    return result


def evaluate(coeffs, x):
    result, choose = 0, 1
    for k, c in enumerate(coeffs):
        if k:
            choose = choose * (x - k + 1) // k
        result += c * choose
    return result


def differences(values):
    out = []
    while values:
        out.append(values[0])
        values = [b - a for a, b in zip(values, values[1:])]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


@dataclass(frozen=True)
class Piece:
    left: int
    right: int
    coeffs: tuple

    def value(self, x):
        assert self.left <= x <= self.right
        return evaluate(self.coeffs, x - self.left)


def prefix_pieces(pieces):
    """Inclusive prefix, with the same intervals; return pieces and total."""
    out, total = [], 0
    for p in pieces:
        c = p.coeffs
        h = [total + c[0]]
        h.extend(c[k - 1] + c[k] for k in range(1, len(c)))
        h.append(c[-1])
        while len(h) > 1 and h[-1] == 0:
            h.pop()
        out.append(Piece(p.left, p.right, tuple(h)))
        total = evaluate(h, p.right - p.left)
    return out, total


def reflect_prefix(pieces, total, capacity, upper):
    """g(y)=H(min(U,capacity-y)), on 0<=y<=upper<=capacity."""
    out = []
    old_upper = pieces[-1].right
    # z>old_upper is a saturated constant interval. z=old_upper remains
    # in the reflected polynomial piece so the intervals are disjoint.
    cap_right = min(upper, capacity - old_upper - 1)
    if cap_right >= 0:
        out.append(Piece(0, cap_right, (total,)))
    for p in reversed(pieces):
        left = max(0, capacity - p.right)
        right = min(upper, capacity - p.left)
        if left > right:
            continue
        # On a short integer interval use its unique interpolant of degree
        # at most length-1. Then all samples are actual nonnegative counts,
        # which also gives the coefficient-size bound in the proof.
        degree = min(len(p.coeffs) - 1, right - left)
        samples = [evaluate(p.coeffs, capacity - left - j - p.left)
                   for j in range(degree + 1)]
        out.append(Piece(left, right, differences(samples)))
    assert out and out[0].left == 0 and out[-1].right == upper
    assert all(p.right + 1 == q.left for p, q in zip(out, out[1:]))
    return out


def compressed_count(capacities, return_trace=False):
    """Count x>=0, x_i+x_(i+1)<=a_i, x_t<=a_t, for any a>=0."""
    a = tuple(capacities)
    if any(type(x) is not int or x < 0 for x in a):
        raise ValueError('capacities must be nonnegative integers')
    if not a:
        return (1, []) if return_trace else 1
    upper = [a[0]] + [min(a[i - 1], a[i]) for i in range(1, len(a))]
    pieces = [Piece(0, upper[0], (1,))]
    trace = []
    for i in range(len(a)):
        assert len(pieces) <= i + 1
        assert max(len(p.coeffs) - 1 for p in pieces) <= i
        if return_trace:
            bound = (2 ** i) * ((max(a) + 1) ** i)
            assert all(abs(c) <= bound for p in pieces for c in p.coeffs)
        pref, total = prefix_pieces(pieces)
        if return_trace:
            trace.append({'layer': i + 1, 'upper': upper[i],
                          'piece_count': len(pieces),
                          'degree': max(len(p.coeffs) - 1 for p in pieces),
                          'max_coefficient_bits': max(abs(c).bit_length()
                              for p in pieces for c in p.coeffs),
                          'prefix_total_bits': total.bit_length()})
        if i + 1 < len(a):
            pieces = reflect_prefix(pref, total, a[i], upper[i + 1])
    return (total, trace) if return_trace else total


def fibre_count(c):
    """F_2(C) for an increasing positive 2-singleton shape, empty allowed."""
    c = tuple(c)
    if any(type(x) is not int or x <= 0 for x in c):
        raise ValueError('columns must be positive integers')
    if any(u > v or (u == v and u % 2) for u, v in zip(c, c[1:])):
        raise ValueError('target must be an increasing 2-singleton shape')
    s = tuple(reversed(c)) + (0,)
    a = [s[i] // 2 - (s[i + 1] + 1) // 2 for i in range(len(c))]
    return compressed_count(a)


if __name__ == '__main__':
    import json
    import sys
    a = json.loads(sys.argv[1])
    count, trace = compressed_count(a, return_trace=True)
    # Binary output matches the bit-complexity statement and avoids the
    # interpreter's limit on converting very large integers to decimal.
    print(json.dumps({'capacities': a, 'count_binary': bin(count),
                      'trace': trace}, indent=2))
