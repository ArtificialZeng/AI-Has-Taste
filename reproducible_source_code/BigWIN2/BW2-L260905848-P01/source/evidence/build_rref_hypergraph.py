#!/usr/bin/env python3
"""Build the frozen F_2^5 forbidden-triple hypergraph exactly.

The vertex order is the lexicographic order of canonical RREF bases.  Each
edge is stored as three unsigned bytes (one vertex index in each ordered
part), in lexicographic (i,j,k) order.  The two edge predicates below are
deliberately different:

* primal: intersect the three explicitly enumerated vector-space masks;
* dual: compute orthogonal complements and row-reduce their six generators.

The script checks their agreement on every one of the 155^3 triples.
"""

from __future__ import annotations

import hashlib
import json
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EDGE_PATH = ROOT / "forbidden_triples_u8.bin"
SUMMARY_PATH = ROOT / "rref_hypergraph_summary.json"


def rref(rows: tuple[int, ...]) -> tuple[int, ...]:
    """Canonical reduced row echelon basis of binary bit-vector rows."""
    work = [row for row in rows if row]
    pivot_row = 0
    for column in range(5):
        pivot = 1 << column
        found = next(
            (index for index in range(pivot_row, len(work))
             if work[index] & pivot),
            None,
        )
        if found is None:
            continue
        work[pivot_row], work[found] = work[found], work[pivot_row]
        for index in range(len(work)):
            if index != pivot_row and work[index] & pivot:
                work[index] ^= work[pivot_row]
        pivot_row += 1
        if pivot_row == len(work):
            break
    return tuple(work[:pivot_row])


def span_mask(basis: tuple[int, ...]) -> int:
    """A 32-bit mask of all vectors in the row span."""
    vectors = [0]
    for row in basis:
        vectors += [vector ^ row for vector in vectors]
    mask = 0
    for vector in vectors:
        mask |= 1 << vector
    return mask


def orthogonal_basis(basis: tuple[int, ...]) -> tuple[int, ...]:
    vectors = tuple(
        vector for vector in range(1, 32)
        if all((vector & row).bit_count() % 2 == 0 for row in basis)
    )
    return rref(vectors)


def main() -> None:
    bases = sorted({
        rref(triple)
        for triple in combinations(range(1, 32), 3)
        if len(rref(triple)) == 3
    })
    assert len(bases) == 155
    assert all(len(basis) == 3 for basis in bases)
    primal_masks = [span_mask(basis) for basis in bases]
    assert all(mask.bit_count() == 8 for mask in primal_masks)

    dual_bases = [orthogonal_basis(basis) for basis in bases]
    assert all(len(basis) == 2 for basis in dual_bases)
    assert all(span_mask(basis).bit_count() == 4 for basis in dual_bases)

    edge_hash = hashlib.sha256()
    basis_hash = hashlib.sha256()
    for basis in bases:
        basis_hash.update(bytes(basis))

    intersection_size_distribution = {1: 0, 2: 0, 4: 0, 8: 0}
    dual_rank_distribution = {2: 0, 3: 0, 4: 0, 5: 0}
    forbidden = 0
    buffer = bytearray()
    with EDGE_PATH.open("wb") as edge_file:
        for first in range(155):
            for second in range(155):
                pair_mask = primal_masks[first] & primal_masks[second]
                for third in range(155):
                    intersection_size = (
                        pair_mask & primal_masks[third]
                    ).bit_count()
                    dual_rank = len(rref(
                        dual_bases[first]
                        + dual_bases[second]
                        + dual_bases[third]
                    ))
                    intersection_size_distribution[intersection_size] += 1
                    dual_rank_distribution[dual_rank] += 1
                    primal_forbidden = intersection_size == 1
                    dual_forbidden = dual_rank == 5
                    assert primal_forbidden == dual_forbidden, (
                        first, second, third, intersection_size, dual_rank
                    )
                    if primal_forbidden:
                        encoded = bytes((first, second, third))
                        buffer.extend(encoded)
                        edge_hash.update(encoded)
                        forbidden += 1
                        if len(buffer) >= 3 * 65536:
                            edge_file.write(buffer)
                            buffer.clear()
        edge_file.write(buffer)

    assert forbidden == 2_499_840
    assert EDGE_PATH.stat().st_size == 3 * forbidden
    assert sum(intersection_size_distribution.values()) == 155 ** 3
    assert dual_rank_distribution[5] == forbidden

    line_one_star = [
        index for index, mask in enumerate(primal_masks) if mask & (1 << 1)
    ]
    assert len(line_one_star) == 35
    edge_data_hash = hashlib.sha256(EDGE_PATH.read_bytes()).hexdigest()
    assert edge_data_hash == edge_hash.hexdigest()

    summary = {
        "field": 2,
        "ambient_dimension": 5,
        "subspace_dimension": 3,
        "vertex_order": "lexicographic canonical RREF row tuples",
        "vertices_per_part": len(bases),
        "rref_bases": [list(basis) for basis in bases],
        "rref_bases_sha256": basis_hash.hexdigest(),
        "edge_format": "three unsigned bytes (part-1, part-2, part-3 indices)",
        "edge_order": "lexicographic (part-1, part-2, part-3)",
        "edge_count": forbidden,
        "edge_file": EDGE_PATH.name,
        "edge_file_bytes": EDGE_PATH.stat().st_size,
        "edge_file_sha256": edge_hash.hexdigest(),
        "total_ordered_triples": 155 ** 3,
        "primal_intersection_size_distribution": {
            str(key): value
            for key, value in intersection_size_distribution.items()
        },
        "dual_span_rank_distribution": {
            str(key): value for key, value in dual_rank_distribution.items()
        },
        "all_primal_dual_classifications_agree": True,
        "star_through_vector_1_indices": line_one_star,
        "star_size": len(line_one_star),
        "star_product": len(line_one_star) ** 3,
    }
    SUMMARY_PATH.write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        key: summary[key]
        for key in (
            "vertices_per_part",
            "edge_count",
            "edge_file_sha256",
            "rref_bases_sha256",
            "primal_intersection_size_distribution",
            "dual_span_rank_distribution",
            "all_primal_dual_classifications_agree",
            "star_size",
            "star_product",
        )
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
