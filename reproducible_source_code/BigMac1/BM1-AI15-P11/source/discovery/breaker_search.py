#!/usr/bin/env python3
"""Deterministic exact-integer breaker search for Erdos problem 993.

This is discovery code, not a proof of the infinite conjecture.  It searches
several explicitly delimited families and writes every retained tree as an
edge list together with its full independently checkable coefficient list.
No floating-point arithmetic is used to decide unimodality or Delta > 0.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import random
import sys
import time
from collections import deque
from fractions import Fraction
from functools import lru_cache
from pathlib import Path


SEED = 993_20260829
ROOTED_COUNTS = [0, 1, 1, 2, 4, 9, 20, 48, 115, 286, 719, 1842, 4766]


def trim(a: list[int]) -> list[int]:
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def poly_add(a: list[int] | tuple[int, ...], b: list[int] | tuple[int, ...]) -> list[int]:
    c = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        c[i] += x
    for i, x in enumerate(b):
        c[i] += x
    return trim(c)


def poly_mul(a: list[int] | tuple[int, ...], b: list[int] | tuple[int, ...]) -> list[int]:
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                c[i + j] += x * y
    return trim(c)


def poly_pow(a: list[int] | tuple[int, ...], exponent: int) -> list[int]:
    ans = [1]
    base = list(a)
    e = exponent
    while e:
        if e & 1:
            ans = poly_mul(ans, base)
        e >>= 1
        if e:
            base = poly_mul(base, base)
    return ans


def exact_delta(a: list[int] | tuple[int, ...]) -> tuple[int | None, tuple[int, int, int] | None]:
    """Return exact Delta and a maximizing triple; None for length < 3."""
    n = len(a)
    if n < 3:
        return None, None
    suffix_value = [0] * n
    suffix_index = [0] * n
    value = a[-1]
    index = n - 1
    for j in range(n - 1, -1, -1):
        if a[j] > value:
            value = a[j]
            index = j
        suffix_value[j] = value
        suffix_index[j] = index
    left_value = a[0]
    left_index = 0
    best: int | None = None
    triple = None
    for middle in range(1, n - 1):
        if a[middle - 1] > left_value:
            left_value = a[middle - 1]
            left_index = middle - 1
        margin = min(left_value - a[middle], suffix_value[middle + 1] - a[middle])
        if best is None or margin > best:
            best = margin
            triple = (left_index, middle, suffix_index[middle + 1])
    return best, triple


def is_unimodal(a: list[int] | tuple[int, ...]) -> bool:
    went_down = False
    for x, y in zip(a, a[1:]):
        if y < x:
            went_down = True
        elif y > x and went_down:
            return False
    return True


def local_reversal_score(a: list[int] | tuple[int, ...]) -> tuple[Fraction | None, tuple[int, int] | None]:
    """Max min(normalized descent at i, normalized later ascent at j).

    It is positive exactly when there is a descent followed later by an
    ascent.  Zero can occur for a unimodal sequence with a plateau, so it is
    only a discovery score; exact_delta remains the decision statistic.
    """
    if len(a) < 3:
        return None, None
    slopes = [Fraction(a[i + 1] - a[i], a[i + 1] + a[i]) for i in range(len(a) - 1)]
    best_descent = -slopes[0]
    best_descent_index = 0
    best = None
    pair = None
    for j in range(1, len(slopes)):
        candidate = min(best_descent, slopes[j])
        if best is None or candidate > best:
            best = candidate
            pair = (best_descent_index, j)
        descent = -slopes[j]
        if descent > best_descent:
            best_descent = descent
            best_descent_index = j
    return best, pair


def frac_json(x: Fraction | None) -> dict[str, int] | None:
    if x is None:
        return None
    return {"numerator": x.numerator, "denominator": x.denominator}


def tree_coefficients(edges: list[tuple[int, int]], n: int, root: int = 0) -> list[int]:
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    parent = [-2] * n
    parent[root] = -1
    order = [root]
    for v in order:
        for w in adj[v]:
            if parent[w] == -2:
                parent[w] = v
                order.append(w)
    if len(order) != n:
        raise ValueError("edge list is disconnected")
    states: list[tuple[list[int], list[int]] | None] = [None] * n
    for v in reversed(order):
        excluded = [1]
        included_without_x = [1]
        for w in adj[v]:
            if parent[w] == v:
                assert states[w] is not None
                child_a, child_b = states[w]
                excluded = poly_mul(excluded, poly_add(child_a, child_b))
                included_without_x = poly_mul(included_without_x, child_a)
        states[v] = (excluded, [0] + included_without_x)
    assert states[root] is not None
    return poly_add(*states[root])


Rooted = tuple["Rooted", ...]


@lru_cache(maxsize=None)
def rooted_size(t: Rooted) -> int:
    return 1 + sum(rooted_size(c) for c in t)


@lru_cache(maxsize=None)
def rooted_state(t: Rooted) -> tuple[tuple[int, ...], tuple[int, ...]]:
    excluded = [1]
    included_without_x = [1]
    for child in t:
        child_a, child_b = rooted_state(child)
        excluded = poly_mul(excluded, poly_add(child_a, child_b))
        included_without_x = poly_mul(included_without_x, child_a)
    return tuple(excluded), tuple([0] + included_without_x)


def generate_rooted(max_n: int) -> dict[int, list[Rooted]]:
    """All unlabeled rooted trees via the unique child-multiset decomposition."""
    by_size: dict[int, list[Rooted]] = {1: [()]}
    all_types: list[Rooted] = [()]
    for n in range(2, max_n + 1):
        options = sorted(all_types, key=lambda t: (rooted_size(t), repr(t)))
        out: list[Rooted] = []

        def rec(remaining: int, start: int, children: list[Rooted]) -> None:
            if remaining == 0:
                out.append(tuple(children))
                return
            for idx in range(start, len(options)):
                weight = rooted_size(options[idx])
                if weight > remaining:
                    break
                children.append(options[idx])
                rec(remaining - weight, idx, children)
                children.pop()

        rec(n - 1, 0, [])
        if len(set(out)) != len(out):
            raise AssertionError("rooted generator produced duplicates")
        by_size[n] = out
        all_types.extend(out)
    return by_size


def rooted_edges(t: Rooted) -> tuple[int, list[tuple[int, int]]]:
    edges: list[tuple[int, int]] = []
    next_vertex = 1

    def visit(subtree: Rooted, vertex: int) -> None:
        nonlocal next_vertex
        for child in subtree:
            child_vertex = next_vertex
            next_vertex += 1
            edges.append((vertex, child_vertex))
            visit(child, child_vertex)

    visit(t, 0)
    return next_vertex, edges


def hub_from_rooted(t: Rooted, copies: int) -> tuple[int, list[tuple[int, int]]]:
    """A new hub adjacent to the root of each of `copies` copies of t."""
    base_n, base_edges = rooted_edges(t)
    edges: list[tuple[int, int]] = []
    offset = 1
    for _ in range(copies):
        edges.append((0, offset))
        edges.extend((u + offset, v + offset) for u, v in base_edges)
        offset += base_n
    return offset, edges


def path_arm_hub_edges(arms: list[int]) -> tuple[int, list[tuple[int, int]]]:
    """Center--branch vertices; branch i supports arms[i] pendant P2's."""
    edges: list[tuple[int, int]] = []
    next_vertex = 1
    for arm_count in arms:
        branch = next_vertex
        next_vertex += 1
        edges.append((0, branch))
        for _ in range(arm_count):
            x = next_vertex
            y = next_vertex + 1
            next_vertex += 2
            edges.extend(((branch, x), (x, y)))
    return next_vertex, edges


def record_candidate(label: str, edges: list[tuple[int, int]], n: int, coefficients: list[int] | None = None) -> dict:
    coeffs = coefficients if coefficients is not None else tree_coefficients(edges, n)
    delta, triple = exact_delta(coeffs)
    score, pair = local_reversal_score(coeffs)
    return {
        "label": label,
        "n": n,
        "edges": [list(e) for e in edges],
        "coefficients": coeffs,
        "delta": delta,
        "delta_triple": list(triple) if triple else None,
        "unimodal": is_unimodal(coeffs),
        "local_reversal_score": frac_json(score),
        "local_reversal_pair": list(pair) if pair else None,
    }


def better_score(candidate: dict, incumbent: dict | None) -> bool:
    if incumbent is None:
        return True
    a = candidate["local_reversal_score"]
    b = incumbent["local_reversal_score"]
    if a is None:
        return False
    if b is None:
        return True
    return Fraction(a["numerator"], a["denominator"]) > Fraction(b["numerator"], b["denominator"])


def binomial_scaled(n: int, scale: int) -> list[int]:
    return [math.comb(n, k) * scale**k for k in range(n + 1)]


def path_arm_branch_state(t: int) -> tuple[list[int], list[int]]:
    # A=(1+2x)^t, B=x(1+x)^t.
    return binomial_scaled(t, 2), [0] + binomial_scaled(t, 1)


def polynomial_from_path_arm_hub(arms: list[int]) -> list[int]:
    excluded = [1]
    included_without_x = [1]
    for t in arms:
        a, b = path_arm_branch_state(t)
        excluded = poly_mul(excluded, poly_add(a, b))
        included_without_x = poly_mul(included_without_x, a)
    return poly_add(excluded, [0] + included_without_x)


def run_lemma_audit(rooted: dict[int, list[Rooted]]) -> dict:
    sum_a, sum_b = [1, 1, 2], [2, 1, 1]
    conv_a, conv_b = [1, 1, 2], [1, 1, 3]
    ratio_tree: Rooted = (((), ()),)
    ratio_a, ratio_b = rooted_state(ratio_tree)
    ratio_edges_n, ratio_edges = rooted_edges(ratio_tree)
    star: Rooted = tuple(() for _ in range(6))
    star_a, star_b = rooted_state(star)
    star_n, star_edges = rooted_edges(star)

    first_ratio_failure = None
    tested = 0
    all_tree_polynomials_unimodal = True
    for n in range(1, 13):
        if len(rooted[n]) != ROOTED_COUNTS[n]:
            raise AssertionError(f"rooted count mismatch at n={n}")
        for t in rooted[n]:
            tested += 1
            a, b = rooted_state(t)
            total = poly_add(a, b)
            if not is_unimodal(total):
                all_tree_polynomials_unimodal = False
            ratios = []
            for k in range(min(len(a), len(b) - 1)):
                if a[k] and b[k + 1]:
                    ratios.append((k, Fraction(b[k + 1], a[k])))
            for x, y in zip(ratios, ratios[1:]):
                if y[1] > x[1] and first_ratio_failure is None:
                    rn, re = rooted_edges(t)
                    first_ratio_failure = {
                        "n": rn,
                        "edges": [list(e) for e in re],
                        "A": list(a),
                        "B": list(b),
                        "ratios": [
                            {"k": k, "numerator": q.numerator, "denominator": q.denominator}
                            for k, q in ratios
                        ],
                        "increase_between_k": [x[0], y[0]],
                    }
    return {
        "generic_sum_closure_counterexample": {
            "a": sum_a,
            "b": sum_b,
            "a_plus_b": poly_add(sum_a, sum_b),
        },
        "generic_convolution_closure_counterexample": {
            "a": conv_a,
            "b": conv_b,
            "convolution": poly_mul(conv_a, conv_b),
        },
        "root_ratio_monotonicity_counterexample": {
            "candidate_claim": "B[k+1]/A[k] is nonincreasing wherever both terms are positive",
            "n": ratio_edges_n,
            "edges": [list(e) for e in ratio_edges],
            "A": list(ratio_a),
            "B": list(ratio_b),
            "ratios": ["1", "2/3", "1"],
        },
        "root_mode_synchronization_counterexample": {
            "candidate_claim": "leftmost modes of A and B differ by at most one",
            "n": star_n,
            "edges": [list(e) for e in star_edges],
            "A": list(star_a),
            "B": list(star_b),
            "leftmost_modes": [3, 1],
        },
        "exhaustive_rooted_audit": {
            "max_n": 12,
            "counts_by_n": {str(n): len(rooted[n]) for n in range(1, 13)},
            "total_rooted_types": tested,
            "all_total_polynomials_unimodal": all_tree_polynomials_unimodal,
            "first_ratio_failure_found_by_sweep": first_ratio_failure,
        },
    }


def run_repeated_hubs(rooted: dict[int, list[Rooted]], max_base_n: int, max_copies: int) -> dict:
    evaluated = 0
    best = None
    counterexample = None
    for base_n in range(1, max_base_n + 1):
        for idx, t in enumerate(rooted[base_n]):
            a0, b0 = rooted_state(t)
            total0 = poly_add(a0, b0)
            excluded = [1]
            included_without_x = [1]
            for copies in range(1, max_copies + 1):
                excluded = poly_mul(excluded, total0)
                included_without_x = poly_mul(included_without_x, a0)
                if copies == 1:
                    continue
                evaluated += 1
                coeffs = poly_add(excluded, [0] + included_without_x)
                delta, triple = exact_delta(coeffs)
                score, pair = local_reversal_score(coeffs)
                summary = {
                    "base_n": base_n,
                    "base_index": idx,
                    "copies": copies,
                    "tree_n": 1 + copies * base_n,
                    "delta": delta,
                    "delta_triple": list(triple) if triple else None,
                    "local_reversal_score": frac_json(score),
                    "local_reversal_pair": list(pair) if pair else None,
                }
                if better_score(summary, best):
                    n, edges = hub_from_rooted(t, copies)
                    best = record_candidate(f"repeated_hub_base{base_n}_{idx}_copies{copies}", edges, n, coeffs)
                    best.update({"base_n": base_n, "base_index": idx, "copies": copies})
                if delta is not None and delta > 0:
                    n, edges = hub_from_rooted(t, copies)
                    counterexample = record_candidate("repeated_hub_counterexample", edges, n, coeffs)
                    return {
                        "evaluated": evaluated,
                        "counterexample": counterexample,
                        "best": best,
                    }
    return {"evaluated": evaluated, "counterexample": counterexample, "best": best}


def run_known_style_families(max_t: int, max_m: int, max_k: int, max_offset: int) -> dict:
    evaluated_galvin = 0
    best_galvin = None
    counterexample = None
    # Galvin T_{m,t,1}: [((1+2x)^t + x(1+x)^t)]^m + x(1+2x)^(mt).
    for t in range(1, max_t + 1):
        a, b = path_arm_branch_state(t)
        branch_total = poly_add(a, b)
        excluded = [1]
        included_without_x = [1]
        for m in range(1, max_m + 1):
            excluded = poly_mul(excluded, branch_total)
            included_without_x = poly_mul(included_without_x, a)
            coeffs = poly_add(excluded, [0] + included_without_x)
            evaluated_galvin += 1
            delta, triple = exact_delta(coeffs)
            score, pair = local_reversal_score(coeffs)
            summary = {
                "m": m,
                "t": t,
                "tree_n": 1 + m + 2 * m * t,
                "delta": delta,
                "delta_triple": list(triple) if triple else None,
                "local_reversal_score": frac_json(score),
                "local_reversal_pair": list(pair) if pair else None,
            }
            if better_score(summary, best_galvin):
                n, edges = path_arm_hub_edges([t] * m)
                best_galvin = record_candidate(f"galvin_m{m}_t{t}", edges, n, coeffs)
                best_galvin.update({"m": m, "t": t})
            if delta is not None and delta > 0:
                n, edges = path_arm_hub_edges([t] * m)
                counterexample = record_candidate("galvin_counterexample", edges, n, coeffs)
                break
        if counterexample:
            break

    evaluated_three_arm = 0
    best_three_arm = None
    if counterexample is None:
        for k in range(4, max_k + 1):
            for offset in range(0, max_offset + 1):
                arms = [3, k, k + offset]
                coeffs = polynomial_from_path_arm_hub(arms)
                evaluated_three_arm += 1
                delta, triple = exact_delta(coeffs)
                score, pair = local_reversal_score(coeffs)
                summary = {
                    "arms": arms,
                    "tree_n": 4 + 2 * sum(arms),
                    "delta": delta,
                    "delta_triple": list(triple) if triple else None,
                    "local_reversal_score": frac_json(score),
                    "local_reversal_pair": list(pair) if pair else None,
                }
                if better_score(summary, best_three_arm):
                    n, edges = path_arm_hub_edges(arms)
                    best_three_arm = record_candidate(f"three_arm_{arms}", edges, n, coeffs)
                    best_three_arm["arms"] = arms
                if delta is not None and delta > 0:
                    n, edges = path_arm_hub_edges(arms)
                    counterexample = record_candidate("three_arm_counterexample", edges, n, coeffs)
                    break
            if counterexample:
                break

    benchmark_n, benchmark_edges = path_arm_hub_edges([3, 4, 4])
    benchmark_coeffs = tree_coefficients(benchmark_edges, benchmark_n)
    log_concavity_breaks = [
        {
            "k": k,
            "difference_i_k_squared_minus_neighbors": benchmark_coeffs[k] ** 2
            - benchmark_coeffs[k - 1] * benchmark_coeffs[k + 1],
        }
        for k in range(1, len(benchmark_coeffs) - 1)
        if benchmark_coeffs[k] ** 2 < benchmark_coeffs[k - 1] * benchmark_coeffs[k + 1]
    ]
    benchmark = record_candidate("known_non_log_concave_3_4_4", benchmark_edges, benchmark_n, benchmark_coeffs)
    benchmark["log_concavity_breaks"] = log_concavity_breaks
    return {
        "galvin": {
            "parameter_box": {"1<=t<=": max_t, "1<=m<=": max_m},
            "evaluated": evaluated_galvin,
            "best": best_galvin,
        },
        "three_arm": {
            "parameter_box": {"4<=k<=": max_k, "0<=offset<=": max_offset, "arms": "[3,k,k+offset]"},
            "evaluated": evaluated_three_arm,
            "best": best_three_arm,
        },
        "known_26_vertex_benchmark": benchmark,
        "counterexample": counterexample,
    }


def random_tree(n: int, rng: random.Random) -> list[set[int]]:
    adj = [set() for _ in range(n)]
    for v in range(1, n):
        w = rng.randrange(v)
        adj[v].add(w)
        adj[w].add(v)
    return adj


def adjacency_edges(adj: list[set[int]]) -> list[tuple[int, int]]:
    return [(u, v) for u in range(len(adj)) for v in sorted(adj[u]) if u < v]


def subtree_prune_regraft(adj: list[set[int]], rng: random.Random) -> list[set[int]]:
    n = len(adj)
    root = rng.randrange(n)
    parent = [-2] * n
    parent[root] = -1
    order = [root]
    for v in order:
        for w in adj[v]:
            if parent[w] == -2:
                parent[w] = v
                order.append(w)
    v = rng.choice(order[1:])
    subtree = set()
    stack = [v]
    while stack:
        x = stack.pop()
        subtree.add(x)
        stack.extend(w for w in adj[x] if parent[w] == x)
    outside = [x for x in range(n) if x not in subtree]
    new_parent = rng.choice(outside)
    old_parent = parent[v]
    mutated = [set(neighbors) for neighbors in adj]
    mutated[old_parent].remove(v)
    mutated[v].remove(old_parent)
    mutated[new_parent].add(v)
    mutated[v].add(new_parent)
    return mutated


def run_mutation(rng: random.Random, sizes: list[int], restarts: int, steps: int) -> dict:
    total_evaluated = 0
    retained = []
    counterexample = None
    for n in sizes:
        best = None
        for restart in range(restarts):
            adj = random_tree(n, rng)
            edges = adjacency_edges(adj)
            coeffs = tree_coefficients(edges, n)
            current_score, _ = local_reversal_score(coeffs)
            assert current_score is not None
            temperature = Fraction(1, 100)
            for step in range(steps):
                proposal = subtree_prune_regraft(adj, rng)
                proposal_edges = adjacency_edges(proposal)
                proposal_coeffs = tree_coefficients(proposal_edges, n)
                total_evaluated += 1
                delta, _ = exact_delta(proposal_coeffs)
                score, _ = local_reversal_score(proposal_coeffs)
                assert score is not None
                candidate = record_candidate(
                    f"mutation_n{n}_restart{restart}_step{step}",
                    proposal_edges,
                    n,
                    proposal_coeffs,
                )
                if better_score(candidate, best):
                    best = candidate
                if delta is not None and delta > 0:
                    counterexample = candidate
                    break
                # Exact comparison for improvements; seeded float only controls
                # occasional exploratory downhill moves and never certification.
                accept = score >= current_score
                if not accept:
                    exponent = float((score - current_score) / max(temperature, Fraction(1, 10**12)))
                    accept = rng.random() < math.exp(max(-700.0, exponent))
                if accept:
                    adj = proposal
                    coeffs = proposal_coeffs
                    current_score = score
                temperature *= Fraction(997, 1000)
            if counterexample:
                break
        if best is not None:
            retained.append(best)
        if counterexample:
            break
    return {
        "parameters": {"sizes": sizes, "restarts_per_size": restarts, "steps_per_restart": steps},
        "evaluated": total_evaluated,
        "retained_best_per_size": retained,
        "counterexample": counterexample,
    }


def spherical_coefficients(branching: list[int]) -> tuple[list[int], int]:
    child_a = [1]
    child_b = [0, 1]
    for degree in reversed(branching):
        new_a = poly_pow(poly_add(child_a, child_b), degree)
        new_b = [0] + poly_pow(child_a, degree)
        child_a, child_b = new_a, new_b
    level = 1
    nodes = 1
    for degree in branching:
        level *= degree
        nodes += level
    return poly_add(child_a, child_b), nodes


def run_spherical_grammar(rng: random.Random, samples: int, max_nodes: int) -> dict:
    evaluated = 0
    best = None
    counterexample = None
    seen: set[tuple[int, ...]] = set()
    fixed = [tuple([2] * m + [1] * n) for m in range(1, 7) for n in range(1, 13)]
    proposals = list(fixed)
    while len(proposals) < samples:
        depth = rng.randint(2, 9)
        proposals.append(tuple(rng.randint(1, 5) for _ in range(depth)))
    for branching_tuple in proposals:
        if branching_tuple in seen:
            continue
        seen.add(branching_tuple)
        branching = list(branching_tuple)
        level = 1
        nodes = 1
        for degree in branching:
            level *= degree
            nodes += level
        if nodes > max_nodes:
            continue
        coeffs, check_nodes = spherical_coefficients(branching)
        assert nodes == check_nodes
        evaluated += 1
        delta, triple = exact_delta(coeffs)
        score, pair = local_reversal_score(coeffs)
        summary = {
            "branching": branching,
            "tree_n": nodes,
            "delta": delta,
            "delta_triple": list(triple) if triple else None,
            "local_reversal_score": frac_json(score),
            "local_reversal_pair": list(pair) if pair else None,
        }
        if better_score(summary, best):
            best = summary | {"coefficients": coeffs, "unimodal": is_unimodal(coeffs)}
        if delta is not None and delta > 0:
            counterexample = summary | {"coefficients": coeffs, "unimodal": False}
            break
    return {
        "parameters": {"proposal_count": samples, "max_nodes": max_nodes, "branching_alphabet": [1, 2, 3, 4, 5]},
        "evaluated_after_size_filter_and_deduplication": evaluated,
        "best_compressed_candidate": best,
        "counterexample": counterexample,
    }


def self_test() -> None:
    assert tree_coefficients([], 1) == [1, 1]
    assert tree_coefficients([(0, 1)], 2) == [1, 2]
    assert tree_coefficients([(0, 1), (1, 2)], 3) == [1, 3, 1]
    assert exact_delta([1, 2, 6, 5, 6])[0] == 1
    assert not is_unimodal([1, 2, 6, 5, 6])
    assert is_unimodal([1, 2, 2, 1])
    n, edges = path_arm_hub_edges([3, 4, 4])
    coeffs = tree_coefficients(edges, n)
    assert n == 26
    assert coeffs == [1, 26, 300, 2040, 9142, 28551, 63933, 103736, 121376, 100144, 55499, 18683, 2979, 51, 1]
    assert coeffs[13] ** 2 - coeffs[12] * coeffs[14] == -378
    assert is_unimodal(coeffs)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("discovery/breaker_run.json"))
    parser.add_argument("--quick", action="store_true", help="small deterministic smoke run")
    args = parser.parse_args()
    started = time.time()
    self_test()
    rooted = generate_rooted(12)
    rng = random.Random(SEED)

    if args.quick:
        limits = {
            "max_base_n": 7,
            "max_copies": 20,
            "max_t": 12,
            "max_m": 12,
            "max_k": 30,
            "max_offset": 3,
            "mutation_sizes": [31, 40],
            "mutation_restarts": 1,
            "mutation_steps": 250,
            "spherical_samples": 250,
            "spherical_max_nodes": 250,
        }
    else:
        limits = {
            "max_base_n": 9,
            "max_copies": 80,
            "max_t": 50,
            "max_m": 50,
            "max_k": 120,
            "max_offset": 10,
            "mutation_sizes": [31, 40, 60, 100, 150],
            "mutation_restarts": 5,
            "mutation_steps": 3000,
            "spherical_samples": 5000,
            "spherical_max_nodes": 600,
        }

    lemma_audit = run_lemma_audit(rooted)
    repeated_hubs = run_repeated_hubs(rooted, limits["max_base_n"], limits["max_copies"])
    known_style = run_known_style_families(
        limits["max_t"], limits["max_m"], limits["max_k"], limits["max_offset"]
    )
    mutation = run_mutation(
        rng, limits["mutation_sizes"], limits["mutation_restarts"], limits["mutation_steps"]
    )
    spherical = run_spherical_grammar(rng, limits["spherical_samples"], limits["spherical_max_nodes"])

    counterexamples = [
        repeated_hubs["counterexample"],
        known_style["counterexample"],
        mutation["counterexample"],
        spherical["counterexample"],
    ]
    counterexamples = [x for x in counterexamples if x is not None]
    script_path = Path(__file__).resolve()
    result = {
        "schema": "breaker-search-v1",
        "role": "Gate 5 Breaker / counterexample hunter",
        "decision_rule": "Delta>0 using exact Python integers",
        "discovery_score_warning": "local_reversal_score guides search only and is never a certificate",
        "seed": SEED,
        "limits": limits,
        "environment": {
            "python": sys.version,
            "platform": platform.platform(),
            "executable": sys.executable,
            "script_sha256": hashlib.sha256(script_path.read_bytes()).hexdigest(),
        },
        "self_tests_passed": True,
        "lemma_audit": lemma_audit,
        "phases": {
            "repeated_hubs": repeated_hubs,
            "known_style_hub_and_path_arm_families": known_style,
            "fixed_order_subtree_prune_regraft": mutation,
            "spherically_symmetric_grammar": spherical,
        },
        "counterexamples_found": counterexamples,
        "elapsed_seconds": time.time() - started,
        "scientific_scope": "Negative search evidence only outside exact witness refutations; not a proof of global unimodality.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "output": str(args.output),
        "counterexample_count": len(counterexamples),
        "elapsed_seconds": result["elapsed_seconds"],
        "phase_counts": {
            "rooted_types": lemma_audit["exhaustive_rooted_audit"]["total_rooted_types"],
            "repeated_hubs": repeated_hubs["evaluated"],
            "galvin": known_style["galvin"]["evaluated"],
            "three_arm": known_style["three_arm"]["evaluated"],
            "mutation": mutation["evaluated"],
            "spherical": spherical["evaluated_after_size_filter_and_deduplication"],
        },
    }, indent=2))


if __name__ == "__main__":
    main()
