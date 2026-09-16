#!/usr/bin/env python3
"""Independent, fail-closed audit of the n=8 kernel certificate.

This file deliberately does not import the discovery modules or NetworkX.
It implements the n=8 graph6 decoder, alpha calculation, whiskered bases,
and integer kernel products directly.  A deterministic sample is also
reconstructed by scanning all 2^16 vertex subsets.
"""
from __future__ import annotations

import hashlib
import json
import platform
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
G6_FILE = ROOT / "experiments/breaker_graphs8.g6"
CERT_FILE = ROOT / "certificates/breaker_n8_alpha3_kernels.jsonl"


def graph6_n8(s: str) -> list[int]:
    # graph6 for n=8: one size byte ('G'=8+63), then ceil(28/6)=5 bytes.
    if len(s) != 6 or s[0] != "G" or any(not (63 <= ord(c) <= 126) for c in s):
        raise ValueError(f"noncanonical n=8 graph6 string: {s!r}")
    bits = []
    for c in s[1:]:
        z = ord(c) - 63
        bits.extend((z >> k) & 1 for k in range(5, -1, -1))
    adj = [0] * 8
    k = 0
    # graph6 upper triangle is read by columns.
    for j in range(1, 8):
        for i in range(j):
            if bits[k]:
                adj[i] |= 1 << j
                adj[j] |= 1 << i
            k += 1
    # The two padding bits in the last sextet must be zero in canonical g6.
    if any(bits[28:]):
        raise ValueError(f"nonzero graph6 padding: {s!r}")
    return adj


def independent(mask: int, adj: list[int]) -> bool:
    q = mask
    while q:
        b = q & -q
        q ^= b
        if adj[b.bit_length() - 1] & q:
            return False
    return True


def alpha8(adj: list[int]) -> int:
    return max(m.bit_count() for m in range(256) if independent(m, adj))


def ordered_layers(adj: list[int]) -> list[list[int]]:
    """The explicitly audited certificate basis order.

    Original-vertex masks x increase from 0 through 255.  For each x, leaf
    masks y traverse the standard descending submask sequence of ~x.  This
    is the order used by the serialized vector coordinates.
    """
    out = [[] for _ in range(9)]
    for x in range(256):
        if not independent(x, adj):
            continue
        allowed = 255 ^ x
        y = allowed
        while True:
            m = x | (y << 8)
            out[m.bit_count()].append(m)
            if y == 0:
                break
            y = (y - 1) & allowed
    return out


def direct_layers16(adj: list[int]) -> list[set[int]]:
    """Second basis implementation: literal scan of all 65,536 subsets."""
    wadj = adj[:] + [0] * 8
    for i in range(8):
        wadj[i] |= 1 << (8 + i)
        wadj[8 + i] |= 1 << i
    out = [set() for _ in range(9)]
    for m in range(1 << 16):
        if independent(m, wadj):
            out[m.bit_count()].add(m)
    return out


def verify_record(r: dict, adj: list[int], layers: list[list[int]]) -> None:
    required = {"alpha", "degree", "geng_index", "graph6", "hilbert",
                "matrix_shape", "side", "vector_length", "vector_sparse"}
    if set(r) != required:
        raise AssertionError(("record keys", set(r), required))
    h = [len(x) for x in layers]
    assert r["alpha"] == 3 and r["degree"] == 4 and r["side"] == "right"
    assert r["hilbert"] == h
    assert r["matrix_shape"] == [h[5], h[4]]
    assert h[4] <= h[5] and r["vector_length"] == h[4]
    v = [0] * h[4]
    previous = -1
    for pair in r["vector_sparse"]:
        assert isinstance(pair, list) and len(pair) == 2
        i, z = pair
        assert isinstance(i, int) and isinstance(z, int) and z != 0
        assert previous < i < len(v), "indices must be unique and sorted"
        previous = i
        v[i] = z
    assert any(v)
    lower_index = {m: j for j, m in enumerate(layers[4])}
    # For each degree-five row, sum coefficients of its five degree-four
    # subsets.  Missing subsets are impossible because subsets of independent
    # sets are independent.
    for upper in layers[5]:
        total = 0
        q = upper
        while q:
            b = q & -q
            q ^= b
            total += v[lower_index[upper ^ b]]
        assert total == 0


def main() -> None:
    raw_lines = G6_FILE.read_text(encoding="ascii").splitlines()
    graph_lines = [s for s in raw_lines if s and not s.startswith(">")]
    assert len(graph_lines) == 12346
    assert len(set(graph_lines)) == 12346

    adjs = []
    alpha_counts = Counter()
    alpha3_order = []
    alpha4_dimension_checks = 0
    alpha_ge5 = 0
    for idx, s in enumerate(graph_lines):
        adj = graph6_n8(s)
        adjs.append(adj)
        a = alpha8(adj)
        alpha_counts[a] += 1
        if a == 3:
            alpha3_order.append((idx, s))
        elif a == 4:
            # Independently check the dimension comparison needed to turn
            # Theorem 3.10's M_5 non-surjectivity into WLP failure.
            ik = Counter(m.bit_count() for m in range(256) if independent(m, adj))
            h5 = sum(ik[k] * choose(8-k, 5-k) for k in range(5))
            h6 = sum(ik[k] * choose(8-k, 6-k) for k in range(5))
            assert h5 > h6
            alpha4_dimension_checks += 1
        elif a >= 5:
            alpha_ge5 += 1
    assert dict(sorted(alpha_counts.items())) == {1: 1, 2: 409, 3: 6021, 4: 4985, 5: 842, 6: 80, 7: 7, 8: 1}

    cert_hash = hashlib.sha256(CERT_FILE.read_bytes()).hexdigest()
    assert cert_hash == "4cfa82ecefa3ebfd10f7bd90546f61ff7afb1c5a427a7aee7a637ab0eaa77dd4"
    seen = set()
    samples = {0, 1, 2, 17, 127, 511, 1023, 2047, 4095, 6018, 6019, 6020}
    count = 0
    with CERT_FILE.open(encoding="utf-8") as f:
        for line_number, line in enumerate(f, 1):
            r = json.loads(line)
            assert (r["geng_index"], r["graph6"]) == alpha3_order[count]
            assert r["graph6"] not in seen
            seen.add(r["graph6"])
            adj = adjs[r["geng_index"]]
            assert alpha8(adj) == 3
            layers = ordered_layers(adj)
            verify_record(r, adj, layers)
            if count in samples:
                literal = direct_layers16(adj)
                assert all(set(layers[d]) == literal[d] for d in range(9))
                # Recheck the same integer identity using literal ascending
                # row/subset traversal, independently of the ordered builder.
                v_by_mask = {layers[4][i]: z for i, z in r["vector_sparse"]}
                assert v_by_mask
                for upper in sorted(literal[5]):
                    assert sum(v_by_mask.get(upper ^ (1 << b), 0)
                               for b in range(16) if (upper >> b) & 1) == 0
            count += 1
    assert count == len(alpha3_order) == 6021
    assert alpha4_dimension_checks == 4985 and alpha_ge5 == 930

    result = {
        "status": "OK",
        "graphs": len(graph_lines),
        "unique_graph6_strings": len(set(graph_lines)),
        "alpha_counts": dict(sorted(alpha_counts.items())),
        "alpha3_certificates_verified": count,
        "certificate_sides": {"right_degree_4": count},
        "direct_16bit_samples": len(samples),
        "alpha4_dimension_checks": alpha4_dimension_checks,
        "alpha_ge5_structural_count": alpha_ge5,
        "certificate_sha256": cert_hash,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "python": sys.version,
        "platform": platform.platform(),
    }
    print(json.dumps(result, sort_keys=True))


def choose(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    num = den = 1
    for j in range(1, k + 1):
        num *= n - k + j
        den *= j
    return num // den


if __name__ == "__main__":
    main()
