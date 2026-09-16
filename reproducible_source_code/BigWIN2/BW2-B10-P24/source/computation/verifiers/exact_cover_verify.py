#!/usr/bin/env python3
"""Definition-level verifier for F(62)=31.

The upper bound is an exhaustive minimum vertex-cover search in the
four-uniform collision hypergraph.  It uses Python integers only.
"""

from itertools import combinations
import json
import platform
import sys
import time


N = 62
WITNESS = (2, 5, 9, 11, 19, 21, 31, 32, 34, 35, 37, 39, 41, 43, 44,
           46, 47, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62)


def collision_edges_by_products(n):
    groups = {}
    for a, b in combinations(range(1, n + 1), 2):
        groups.setdefault(a * b, []).append((a, b))
    edges = set()
    for pairs in groups.values():
        for (a, b), (c, d) in combinations(pairs, 2):
            q = frozenset((a, b, c, d))
            if len(q) == 4:
                edges.add(tuple(sorted(q)))
    return tuple(sorted(edges))


def collision_edges_by_four_subsets(n):
    edges = []
    for a, b, c, d in combinations(range(1, n + 1), 4):
        if a * b == c * d or a * c == b * d or a * d == b * c:
            edges.append((a, b, c, d))
    return tuple(edges)


def verify_witness(witness):
    assert len(witness) == len(set(witness)) == 31
    assert min(witness) >= 1 and max(witness) <= N
    seen = {}
    for a, b in combinations(witness, 2):
        p = a * b
        assert p not in seen, (p, seen[p], (a, b))
        seen[p] = (a, b)
    assert len(seen) == 465


class CoverSearch:
    def __init__(self, edges, n):
        self.edges = tuple(sum(1 << (v - 1) for v in e) for e in edges)
        self.inc = [0] * n
        for i, edge in enumerate(self.edges):
            bit = 1 << i
            for v in range(n):
                if edge >> v & 1:
                    self.inc[v] |= bit
        self.nodes = 0
        self.memo = set()

    def exists(self, uncovered, available, budget):
        self.nodes += 1
        while True:
            if budget < 0:
                return False
            if uncovered == 0:
                return True
            forced = 0
            scan = uncovered
            min_candidates = None
            while scan:
                i = (scan & -scan).bit_length() - 1
                cand = self.edges[i] & available
                if cand == 0:
                    return False
                if cand & (cand - 1) == 0:
                    forced |= cand
                if min_candidates is None or cand.bit_count() < min_candidates.bit_count():
                    min_candidates = cand
                scan &= scan - 1
            if not forced:
                break
            if forced.bit_count() > budget:
                return False
            budget -= forced.bit_count()
            available &= ~forced
            f = forced
            while f:
                v = (f & -f).bit_length() - 1
                uncovered &= ~self.inc[v]
                f &= f - 1

        key = (uncovered, available, budget)
        if key in self.memo:
            return False

        edge_count = uncovered.bit_count()
        max_degree = 0
        a = available
        while a:
            v = (a & -a).bit_length() - 1
            max_degree = max(max_degree, (self.inc[v] & uncovered).bit_count())
            a &= a - 1
        if (edge_count + max_degree - 1) // max_degree > budget:
            self.memo.add(key)
            return False

        packing = 0
        used = 0
        scan = uncovered
        while scan:
            i = (scan & -scan).bit_length() - 1
            cand = self.edges[i] & available
            if cand & used == 0:
                packing += 1
                used |= cand
                if packing > budget:
                    self.memo.add(key)
                    return False
            scan &= scan - 1

        candidates = min_candidates
        ordered = []
        while candidates:
            v = (candidates & -candidates).bit_length() - 1
            ordered.append(v)
            candidates &= candidates - 1
        # Natural order makes the exhaustive transcript deterministic and,
        # for this arithmetic hypergraph, substantially smaller than a
        # dynamic degree order.
        excluded = 0
        for v in ordered:
            vb = 1 << v
            if self.exists(uncovered & ~self.inc[v], available & ~excluded & ~vb, budget - 1):
                return True
            excluded |= vb
        self.memo.add(key)
        return False


def main():
    start = time.time()
    verify_witness(WITNESS)
    e1 = collision_edges_by_products(N)
    e2 = collision_edges_by_four_subsets(N)
    assert e1 == e2
    assert len(e1) == 1203
    search = CoverSearch(e1, N)
    has_cover_30 = search.exists((1 << len(e1)) - 1, (1 << N) - 1, 30)
    assert not has_cover_30
    record = {
        "claim": "F(62)=31 under the strict-pair convention",
        "collision_edges": len(e1),
        "witness_size": len(WITNESS),
        "witness_products": len(WITNESS) * (len(WITNESS) - 1) // 2,
        "cover_budget_rejected": 30,
        "recursive_nodes": search.nodes,
        "memoized_false_states": len(search.memo),
        "python": platform.python_version(),
        "elapsed_seconds": round(time.time() - start, 3),
        "status": "VERIFIED",
    }
    print(json.dumps(record, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
