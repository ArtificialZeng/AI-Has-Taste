#!/usr/bin/env python3
"""Exact graph6 enumeration and independent validation for the n=9 breaker.

Discovery utility only.  ``geng`` supplies a complete isomorph-free stream;
all parsing, edge counts, bipartiteness tests, and canonical relabelling below
are independent pure-Python implementations.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import platform
import shutil
import subprocess
import sys
from collections import Counter, defaultdict, deque
from pathlib import Path


N = 9
MAX_EDGES = 6
EXPECTED_NONBIP_COUNTS = {0: 0, 1: 0, 2: 0, 3: 1, 4: 2, 5: 8, 6: 25}


def decode_graph6(line: str) -> tuple[int, tuple[int, ...]]:
    """Decode the small-n graph6 format, rejecting noncanonical padding."""
    if not line or line.startswith(">>"):
        raise ValueError("expected one headerless graph6 record")
    values = [ord(ch) - 63 for ch in line]
    if any(value < 0 or value > 63 for value in values):
        raise ValueError("graph6 byte outside the allowed range")
    n = values[0]
    if n > 62:
        raise ValueError("this verifier intentionally accepts only n <= 62")
    needed = n * (n - 1) // 2
    payload = values[1:]
    if len(payload) != (needed + 5) // 6:
        raise ValueError("wrong graph6 payload length")
    bits: list[int] = []
    for value in payload:
        bits.extend((value >> shift) & 1 for shift in range(5, -1, -1))
    if any(bits[needed:]):
        raise ValueError("nonzero graph6 padding")
    adj = [0] * n
    cursor = 0
    for j in range(1, n):
        for i in range(j):
            if bits[cursor]:
                adj[i] |= 1 << j
                adj[j] |= 1 << i
            cursor += 1
    return n, tuple(adj)


def encode_graph6(adj: tuple[int, ...]) -> str:
    n = len(adj)
    if n > 62:
        raise ValueError("small graph6 only")
    bits = [((adj[i] >> j) & 1) for j in range(1, n) for i in range(j)]
    bits.extend([0] * ((-len(bits)) % 6))
    chars = [chr(n + 63)]
    for start in range(0, len(bits), 6):
        value = 0
        for bit in bits[start : start + 6]:
            value = (value << 1) | bit
        chars.append(chr(value + 63))
    return "".join(chars)


def edge_count(adj: tuple[int, ...]) -> int:
    return sum(value.bit_count() for value in adj) // 2


def is_bipartite(adj: tuple[int, ...]) -> bool:
    n = len(adj)
    colour = [-1] * n
    for root in range(n):
        if colour[root] != -1:
            continue
        colour[root] = 0
        queue = deque([root])
        while queue:
            u = queue.popleft()
            for v in range(n):
                if not ((adj[u] >> v) & 1):
                    continue
                if colour[v] == -1:
                    colour[v] = colour[u] ^ 1
                    queue.append(v)
                elif colour[v] == colour[u]:
                    return False
    return True


def relabel(adj: tuple[int, ...], order: tuple[int, ...]) -> tuple[int, ...]:
    """Return adjacency after new vertex i is old vertex order[i]."""
    n = len(adj)
    result = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if (adj[order[i]] >> order[j]) & 1:
                result[i] |= 1 << j
                result[j] |= 1 << i
    return tuple(result)


def canonical_graph6(adj: tuple[int, ...]) -> str:
    """Canonicalize exactly, enumerating permutations inside degree cells.

    All isomorphisms preserve degree.  Fixing degree cells in increasing order
    and trying every within-cell permutation therefore loses no isomorphism.
    This is deliberately independent of nauty and is practical for n=9.
    """
    cells: dict[int, list[int]] = defaultdict(list)
    for vertex, row in enumerate(adj):
        cells[row.bit_count()].append(vertex)
    perm_iters = [itertools.permutations(cells[d]) for d in sorted(cells)]
    best: str | None = None
    for pieces in itertools.product(*perm_iters):
        order = tuple(v for piece in pieces for v in piece)
        code = encode_graph6(relabel(adj, order))
        if best is None or code < best:
            best = code
    assert best is not None
    return best


def geng_records(geng: str, bipartite_only: bool) -> list[str]:
    args = [geng, "-q"]
    if bipartite_only:
        args.append("-b")
    args.extend([str(N), f"0:{MAX_EDGES}"])
    run = subprocess.run(args, check=True, capture_output=True, text=True)
    if run.stderr:
        raise RuntimeError(f"unexpected geng stderr: {run.stderr!r}")
    return run.stdout.splitlines()


def validate_records(lines: list[str]) -> tuple[list[dict[str, object]], Counter[int]]:
    seen_input: set[str] = set()
    seen_canonical: set[str] = set()
    records: list[dict[str, object]] = []
    counts: Counter[int] = Counter()
    for index, line in enumerate(lines):
        if line in seen_input:
            raise ValueError(f"duplicate literal graph6 record at index {index}")
        seen_input.add(line)
        n, adj = decode_graph6(line)
        if n != N:
            raise ValueError(f"record {index} has n={n}, expected {N}")
        if encode_graph6(adj) != line:
            raise ValueError(f"record {index} is not canonical graph6 encoding")
        edges = edge_count(adj)
        if not 0 <= edges <= MAX_EDGES:
            raise ValueError(f"record {index} has invalid edge count {edges}")
        canonical = canonical_graph6(adj)
        if canonical in seen_canonical:
            raise ValueError(f"independent canonicalizer found an isomorphic duplicate")
        seen_canonical.add(canonical)
        bip = is_bipartite(adj)
        counts[edges] += 1
        records.append(
            {
                "geng_graph6": line,
                "canonical_graph6": canonical,
                "edges": edges,
                "bipartite": bip,
            }
        )
    return records, counts


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_outputs(outdir: Path, geng: str) -> None:
    full_lines = geng_records(geng, bipartite_only=False)
    bip_lines = geng_records(geng, bipartite_only=True)
    full, full_counts = validate_records(full_lines)
    bip, bip_counts = validate_records(bip_lines)

    full_canon = {str(record["canonical_graph6"]) for record in full}
    bip_canon = {str(record["canonical_graph6"]) for record in bip}
    filtered_bip = {
        str(record["canonical_graph6"])
        for record in full
        if bool(record["bipartite"])
    }
    if not bip_canon <= full_canon:
        raise RuntimeError("geng -b emitted a graph absent from unrestricted geng")
    if bip_canon != filtered_bip:
        raise RuntimeError("independent bipartite filter disagrees with geng -b")

    nonbip = [record for record in full if not bool(record["bipartite"])]
    nonbip.sort(key=lambda record: (int(record["edges"]), str(record["canonical_graph6"])))
    nonbip_counts = Counter(int(record["edges"]) for record in nonbip)
    if {edge: nonbip_counts[edge] for edge in range(7)} != EXPECTED_NONBIP_COUNTS:
        raise RuntimeError("count regression against frozen expected profile")

    graph6_text = "".join(f"{record['canonical_graph6']}\n" for record in nonbip)
    graph6_path = outdir / "breaker_n9_nonbip_e_le6.g6"
    graph6_path.write_text(graph6_text, encoding="ascii")

    manifest = {
        "schema": "breaker-enumeration-v1",
        "scope": {"vertices": N, "min_edges": 0, "max_edges": MAX_EDGES},
        "generator": {
            "path": str(Path(geng).resolve()),
            "commands": [f"{geng} -q 9 0:6", f"{geng} -q -b 9 0:6"],
        },
        "environment": {
            "python": sys.version,
            "platform": platform.platform(),
        },
        "counts_by_edges": {
            str(edge): {
                "all": full_counts[edge],
                "bipartite": bip_counts[edge],
                "nonbipartite": nonbip_counts[edge],
            }
            for edge in range(7)
        },
        "counts_total": {
            "all": len(full),
            "bipartite": len(bip),
            "nonbipartite": len(nonbip),
        },
        "cross_checks": [
            "pure-Python graph6 round trip",
            "pure-Python exact edge count",
            "pure-Python BFS bipartiteness equals geng -b canonical set",
            "pure-Python exhaustive within-degree-cell canonical labels unique",
            "canonical bipartite set is an exact subset of unrestricted set",
        ],
        "graph6_file": graph6_path.name,
        "graph6_sha256": sha256(graph6_text.encode("ascii")),
        "records": nonbip,
    }
    manifest_path = outdir / "breaker_enumeration_manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(manifest["counts_by_edges"], indent=2))
    print(f"wrote {graph6_path}")
    print(f"wrote {manifest_path}")


def verify_outputs(outdir: Path) -> None:
    manifest_path = outdir / "breaker_enumeration_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("schema") != "breaker-enumeration-v1":
        raise ValueError("unsupported or absent schema")
    graph6_path = outdir / str(manifest["graph6_file"])
    raw = graph6_path.read_bytes()
    if sha256(raw) != manifest.get("graph6_sha256"):
        raise ValueError("graph6 SHA-256 mismatch")
    try:
        text = raw.decode("ascii")
    except UnicodeDecodeError as exc:
        raise ValueError("graph6 file is not ASCII") from exc
    if text and not text.endswith("\n"):
        raise ValueError("graph6 file must end with newline")
    records, counts = validate_records(text.splitlines())
    if any(bool(record["bipartite"]) for record in records):
        raise ValueError("bipartite record in nonbipartite certificate")
    expected_counts = manifest.get("counts_by_edges")
    if not isinstance(expected_counts, dict):
        raise ValueError("missing count table")
    for edge in range(7):
        if counts[edge] != EXPECTED_NONBIP_COUNTS[edge]:
            raise ValueError(f"frozen count regression at edge count {edge}")
        if counts[edge] != expected_counts[str(edge)]["nonbipartite"]:
            raise ValueError(f"count mismatch at edge count {edge}")
    listed = manifest.get("records")
    if not isinstance(listed, list):
        raise ValueError("missing record list")
    current_codes = [record["canonical_graph6"] for record in records]
    listed_codes = [record.get("canonical_graph6") for record in listed]
    if current_codes != listed_codes:
        raise ValueError("manifest record order/content mismatch")
    if len(records) != manifest.get("counts_total", {}).get("nonbipartite"):
        raise ValueError("total count mismatch")
    print(f"PASS: independently validated {len(records)} graph6 records")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--outdir", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if args.verify:
        verify_outputs(args.outdir)
        return
    geng = shutil.which("geng")
    if geng is None:
        raise SystemExit("geng not found on PATH")
    write_outputs(args.outdir, geng)


if __name__ == "__main__":
    main()
