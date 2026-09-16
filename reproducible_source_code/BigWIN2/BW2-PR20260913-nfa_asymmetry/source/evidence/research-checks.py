#!/usr/bin/env python3
"""Exact diagnostics for the proof; no computation proves its infinite scope.

Run from the project root: python3 evidence/research-checks.py
No imports of the triage implementation. One process, no workers or network.
"""
from collections import Counter
from pathlib import Path
import hashlib
import json
import math
import time

JOB = 'primary-20260913-nfa-asymmetry-research-71ec4a8ef3d7'


def matrix_mul(a, b):
    answer = []
    for mask in a:
        row = 0
        while mask:
            bit = mask & -mask
            row |= b[bit.bit_length() - 1]
            mask -= bit
        answer.append(row)
    return tuple(answer)


def matrix_power(a, exponent):
    result = tuple(1 << i for i in range(len(a)))
    while exponent:
        if exponent & 1:
            result = matrix_mul(result, a)
        exponent >>= 1
        if exponent:
            a = matrix_mul(a, a)
    return result


def inclusion(a, b):
    return all(not (x & ~y) for x, y in zip(a, b))


def empty_automaton(n):
    return [[set(), set()] for _ in range(n)]


def prefix_separator(accepted, rejected):
    a, b = accepted
    c, d = rejected
    k = min(a, c)
    edges = empty_automaton(k + 2)
    if a < c:
        for i in range(k):
            edges[i][0].add(i + 1)
        edges[k][1].add(k + 1)
        edges[k + 1][0].add(k + 1)
        branch = 'earlier_prefix'
    else:
        for i in range(k + 1):
            edges[i][0].add(i + 1)
        edges[k + 1][0].add(k + 1)
        edges[k + 1][1].add(k + 1)
        branch = 'later_prefix'
    return edges, 0, k + 1, branch


def reverse_automaton(machine):
    edges, initial, final, branch = machine
    reversed_edges = empty_automaton(len(edges))
    for i, row in enumerate(edges):
        for letter in (0, 1):
            for j in row[letter]:
                reversed_edges[j][letter].add(i)
    return reversed_edges, final, initial, branch.replace('prefix', 'suffix')


def modulus_separator(accepted, r):
    edges = empty_automaton(r + 1)
    for i in range(r):
        edges[i][0].add((i + 1) % r)
    edges[accepted[0] % r][1].add(r)
    edges[r][0].add(r)
    return edges, 0, r, 'modulus'


def accepts_iteratively(machine, exponents):
    # Independent representation: sets of destinations and literal symbol steps.
    edges, initial, final, _ = machine
    reachable = {initial}
    for letter, length in ((0, exponents[0]), (1, 1), (0, exponents[1])):
        for _ in range(length):
            reachable = {j for i in reachable for j in edges[i][letter]}
    return final in reachable


def verify_machine(machine, w, x, bound, counts):
    assert len(machine[0]) <= bound, (w, x, 'state count')
    assert accepts_iteratively(machine, w), (w, x, 'does not accept')
    assert not accepts_iteratively(machine, x), (w, x, 'does not reject')
    counts[machine[3]] += 1


def constructor_checks():
    counts = Counter()
    pairs = 0
    no_constructor = 0
    for q in range(3, 9):
        H = (q - 1) ** 2 + 1
        L = math.lcm(*range(1, q + 1))
        # Every ordered distinct pair with total number of zeros at most 40.
        for total in range(1, 41):
            for a in range(total + 1):
                for c in range(total + 1):
                    if a == c:
                        continue
                    w, x = (a, total - a), (c, total - c)
                    pairs += 1
                    if (a - c) % L:
                        r = next(r for r in range(2, q + 1) if (a - c) % r)
                        verify_machine(modulus_separator(w, r), w, x, H + 1, counts)
                    elif min(a, c) < H:
                        verify_machine(prefix_separator(w, x), w, x, H + 1, counts)
                    elif min(w[1], x[1]) < H:
                        machine = reverse_automaton(prefix_separator(w[::-1], x[::-1]))
                        verify_machine(machine, w, x, H + 1, counts)
                    else:
                        no_constructor += 1
        # Force short-block constructors even where the modulus branch also works.
        # Includes every threshold k=0,...,H-1, both orientations, and both ends.
        for k in range(H):
            for displacement in (1, q, L):
                for padding in (0, H - 1, H, H + 1):
                    early = (k, padding + displacement)
                    late = (k + displacement, padding)
                    for w, x in ((early, late), (late, early)):
                        machine = prefix_separator(w, x)
                        verify_machine(machine, w, x, H + 1, counts)
                        verify_machine(reverse_automaton(machine), w[::-1], x[::-1], H + 1, counts)
    return {'q_range': [3, 8], 'total_zeros_range': [1, 40],
            'ordered_pairs_across_q': pairs, 'verified_constructors': dict(counts),
            'long_congruent_pairs_no_constructor_expected': no_constructor,
            'forced_short_block_thresholds': 'every k=0,...,H_q-1; displacements 1,q,L_q; padding 0,H_q-1,H_q,H_q+1',
            'failures': 0}


def binary_transfer_checks():
    results = []
    for n in range(1, 5):
        T = 1 << n
        P = math.lcm(*range(1, T + 1))
        unary_count = 1 << (n * n)
        H = (n - 1) ** 2 + 1
        L = math.lcm(*range(1, n + 1))
        for code in range(unary_count):
            R = tuple((code >> (n * i)) & ((1 << n) - 1) for i in range(n))
            short_prefix = matrix_power(R, n - 1)
            long_prefix = matrix_power(R, n - 1 + P)
            short_suffix = matrix_power(R, T)
            long_suffix = matrix_power(R, T + P)
            assert short_suffix == long_suffix, (n, code, 'subset periodicity')
            assert matrix_power(R, H) == matrix_power(R, H + L), (n, code, 'index identity')
            # Test R^(n-1) C R^(T+P) <= R^(n-1+P) C R^T for all singleton C.
            # The map C -> left*C*right preserves unions. Every Boolean C is
            # the union of its singleton edges, so this covers every C, including 0.
            for i in range(n):
                for j in range(n):
                    for start in range(n):
                        lhs = long_suffix[j] if short_prefix[start] & (1 << i) else 0
                        rhs = short_suffix[j] if long_prefix[start] & (1 << i) else 0
                        assert not lhs & ~rhs, (n, code, i, j, start, 'binary transfer')
        row = {'n': n, 'all_zero_relations': unary_count, 'T': T, 'P': P,
               'singleton_one_relations_per_zero_relation': n * n,
               'direct_basis_pairs': unary_count * n * n,
               'all_binary_relation_pairs_covered_by_union_argument': unary_count ** 2,
               'identity_H': H, 'identity_period': L, 'failures': 0}
        results.append(row)
        print('Completed exhaustive binary transfer for n=', n, flush=True)
    return results


def negative_controls():
    results = []
    # The graph has a zero-cycle, but a walk of n-2 edges need not touch it.
    for n in range(2, 13):
        R = [0] * n
        for i in range(n - 2):
            R[i] = 1 << (i + 1)
        R[n - 1] = 1 << (n - 1)
        L = math.lcm(*range(1, n + 1))
        short = matrix_power(tuple(R), n - 2)
        long = matrix_power(tuple(R), n - 2 + L)
        assert short[0] & (1 << (n - 2))
        assert not long[0] & (1 << (n - 2))
        results.append({'n': n, 'rows': R, 'exponent': n - 2, 'shift': L,
                        'witness_entry': [0, n - 2], 'short_value': 1, 'long_value': 0})
    return results


def sharp_witness_checks():
    # Exact compressed-word verification of the attaining witnesses for q=3,4.
    results = []
    for q in (3, 4):
        s = q - 1
        M, T = s * s, 1 << (s * s + 1)
        P = math.lcm(*range(1, T + 1))
        B = tuple([1 << (i + 1) for i in range(s)] + [3])
        C = tuple([1] + [0] * s)
        def accepted(a, b):
            word_relation = matrix_mul(matrix_mul(matrix_power(B, a), C), matrix_power(B, b))
            return bool(word_relation[0] & 1)
        assert not accepted(M, T + P)
        assert accepted(M + P, T)
        # The explicit M+2-state early-marker separator is evaluated through
        # matrix exponentiation because the words are very long.
        chain, initial, final, _ = prefix_separator((M, T + P), (M + P, T))
        chain_B = tuple(sum(1 << j for j in row[0]) for row in chain)
        chain_C = tuple(sum(1 << j for j in row[1]) for row in chain)
        def chain_accepted(a, b):
            word_relation = matrix_mul(matrix_mul(matrix_power(chain_B, a), chain_C), matrix_power(chain_B, b))
            return bool(word_relation[initial] & (1 << final))
        assert chain_accepted(M, T + P)
        assert not chain_accepted(M + P, T)
        results.append({'q': q, 'M': M, 'T': T, 'P_decimal': str(P),
                        'common_length_decimal': str(M + T + P + 1),
                        'easy_zero_relation_rows': list(B), 'easy_one_relation_rows': list(C),
                        'easy_accepts_u': False, 'easy_accepts_v': True,
                        'hard_chain_states': M + 2, 'hard_chain_accepts_u': True,
                        'hard_chain_accepts_v': False})
    return results


def main():
    started = time.monotonic()
    result = {'job_id': JOB,
              'status': 'exact finite diagnostics; no infinite or independent-audit conclusion',
              'constructors': constructor_checks(),
              'binary_transfer': binary_transfer_checks(),
              'negative_controls': negative_controls(),
              'attaining_witnesses': sharp_witness_checks(),
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'seconds': round(time.monotonic() - started, 3)}
    out = Path('evidence/research-checks.json')
    temporary = out.with_suffix('.json.tmp')
    temporary.write_text(json.dumps(result, indent=2) + '\n')
    temporary.replace(out)
    print(json.dumps({'output': str(out), 'seconds': result['seconds'], 'failures': 0}))


if __name__ == '__main__':
    main()
