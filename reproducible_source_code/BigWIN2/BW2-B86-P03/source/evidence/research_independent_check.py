#!/usr/bin/env python3
"""Independent exact certificate for x^4 and x^8 over F_11.

This checker does not import the triage checker.  Its primary computation uses
the homogeneity identity

  Delta_d(a,b) = #{t : (t+1)^d-t^d = b/a^d}  (a != 0),

then cross-checks every reconstructed entry by direct graph-pair enumeration.
All arithmetic is integer arithmetic reduced modulo 11.
"""

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import sys


P = 11
EXPONENTS = (4, 8)
SOURCE_SHA256 = "9b0a3b9fc1ae610c9ab9e3165640b060077794cfe36987fb04833f06c658b2dd"
MATRIX = ((1, 0, 0), (0, 0, 1), (0, 1, 0))


def determinant_mod_p(matrix):
    (a, b, c), (d, e, f), (g, h, i) = matrix
    return (a * e * i + b * f * g + c * d * h
            - c * e * g - b * d * i - a * f * h) % P


def matrix_vector(matrix, vector):
    return tuple(sum(r * v for r, v in zip(row, vector)) % P for row in matrix)


def normalize_rightmost(vector):
    """Canonical projective representative: rightmost nonzero coordinate is 1."""
    for coordinate in reversed(vector):
        if coordinate % P:
            inverse = pow(coordinate, -1, P)
            return tuple((inverse * value) % P for value in vector)
    raise ValueError("the zero vector is not a projective point")


def projective_set(exponent):
    points = {normalize_rightmost((x, pow(x, exponent, P), 1)) for x in range(P)}
    points.add(normalize_rightmost((0, 1, 0)))
    return points


def derivative_data(exponent):
    values = [
        (pow(t + 1, exponent, P) - pow(t, exponent, P)) % P
        for t in range(P)
    ]
    counts = [values.count(c) for c in range(P)]
    return values, counts


def homogeneous_table(exponent, base_counts):
    table = {}
    for a in range(P):
        for b in range(P):
            if (a, b) == (0, 0):
                continue
            if a == 0:
                table[(a, b)] = 0
            else:
                scale_inverse = pow(pow(a, exponent, P), -1, P)
                table[(a, b)] = base_counts[(b * scale_inverse) % P]
    return table


def pair_table(exponent):
    table = {(a, b): 0 for a in range(P) for b in range(P) if (a, b) != (0, 0)}
    graph = [(x, pow(x, exponent, P)) for x in range(P)]
    for x, fx in graph:
        for y, fy in graph:
            w = ((x - y) % P, (fx - fy) % P)
            if w != (0, 0):
                table[w] += 1
    return table


def encoded_table(table):
    return [
        {"a": a, "b": b, "count": table[(a, b)]}
        for a in range(P)
        for b in range(P)
        if (a, b) != (0, 0)
    ]


def histogram(table):
    return {str(k): v for k, v in sorted(Counter(table.values()).items())}


def make_certificate(project_dir):
    source_digest = sha256((project_dir / "source.md").read_bytes()).hexdigest()
    assert source_digest == SOURCE_SHA256
    assert determinant_mod_p(MATRIX) == 10

    source_set = projective_set(4)
    target_set = projective_set(8)
    mapped_set = {normalize_rightmost(matrix_vector(MATRIX, point)) for point in source_set}
    assert len(source_set) == len(target_set) == len(mapped_set) == 12
    assert mapped_set == target_set

    projective_mapping = [
        {
            "source_parameter": "infinity",
            "source_point": [0, 1, 0],
            "image_point": [0, 0, 1],
            "target_parameter": 0,
        },
        {
            "source_parameter": 0,
            "source_point": [0, 0, 1],
            "image_point": [0, 1, 0],
            "target_parameter": "infinity",
        },
    ]
    for x in range(1, P):
        source_point = (x, pow(x, 4, P), 1)
        image_point = normalize_rightmost(matrix_vector(MATRIX, source_point))
        u = pow(x, -3, P)
        assert image_point == (u, pow(u, 8, P), 1)
        projective_mapping.append(
            {
                "source_parameter": x,
                "source_point": list(source_point),
                "image_point": list(image_point),
                "target_parameter": u,
            }
        )
    assert {item["target_parameter"] for item in projective_mapping} == set(range(P)) | {"infinity"}

    difference_data = {}
    computed_tables = {}
    for exponent in EXPONENTS:
        values, base_counts = derivative_data(exponent)
        reconstructed = homogeneous_table(exponent, base_counts)
        directly_enumerated = pair_table(exponent)
        assert reconstructed == directly_enumerated
        assert len(reconstructed) == 120
        assert sum(reconstructed.values()) == 110
        computed_tables[exponent] = reconstructed
        difference_data[str(exponent)] = {
            "base_derivative_values_for_t_0_through_10": values,
            "base_counts_indexed_by_b_0_through_10": base_counts,
            "histogram": histogram(reconstructed),
            "full_120_entry_table": encoded_table(reconstructed),
        }

    assert histogram(computed_tables[4]) == {"0": 50, "1": 50, "3": 20}
    assert histogram(computed_tables[8]) == {"0": 30, "1": 70, "2": 20}

    return {
        "field": 11,
        "source_sha256": source_digest,
        "projective_certificate": {
            "matrix": [list(row) for row in MATRIX],
            "determinant_mod_11": determinant_mod_p(MATRIX),
            "normalization": "rightmost nonzero homogeneous coordinate scaled to 1",
            "all_12_images": projective_mapping,
            "image_set_equals_target_set": True,
        },
        "difference_certificate": {
            "definition": "count ordered (P,Q) in Gamma^2 with P-Q=(a,b)",
            "reconstruction_identity": "for a!=0, Delta_d(a,b)=#{t in F_11:(t+1)^d-t^d=b/a^d}; for a=0,b!=0 it is 0",
            "independent_direct_pair_cross_check": True,
            "data": difference_data,
            "histograms_differ": True,
        },
    }


def main():
    project_dir = Path(__file__).resolve().parent.parent
    certificate_path = Path(__file__).resolve().parent / "research_exact_certificate.json"
    computed = make_certificate(project_dir)
    serialized = json.dumps(computed, indent=2, sort_keys=True) + "\n"
    if "--write" in sys.argv:
        certificate_path.write_text(serialized, encoding="utf-8")
        print(f"wrote {certificate_path.relative_to(project_dir)}")
    else:
        assert certificate_path.read_text(encoding="utf-8") == serialized
        print("research_exact_certificate.json matches an independent exact recomputation")
    print("M(S_x^4)=S_x^8 for all 12 points; difference histograms are distinct")


if __name__ == "__main__":
    main()
