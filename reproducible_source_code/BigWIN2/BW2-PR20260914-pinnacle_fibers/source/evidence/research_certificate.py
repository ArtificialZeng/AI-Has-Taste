#!/usr/bin/env python3
"""Exact, standard-library recheck of the n=5 induced-order certificate.

Run from the project: python3 evidence/research_certificate.py
This is a researcher computation, not a fresh mathematical referee.
"""
from hashlib import sha256
from itertools import permutations, product
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
JOB = "primary-20260914-pinnacle-fibers-research-1f8e260fcbca"
SOURCE_HASH = "1df3a7b5d04986a7f3a816b6fd50b53b6a27d5b95b005273f1d100fe5f5bcba7"
NAMED = {
    "e": (1, 2, 3, 5, 4),
    "b": (1, 2, 5, 3, 4),
    "a": (1, 3, 5, 2, 4),
    "c": (1, 3, 4, 5, 2),
    "d": (1, 3, 5, 4, 2),
}
EXPECTED_TABLES = {
    "e": (0, 0, 0, 0, 1),
    "b": (0, 0, 0, 0, 2),
    "a": (0, 0, 1, 0, 2),
    "c": (0, 0, 1, 1, 1),
    "d": (0, 0, 1, 1, 2),
}


def digest(path):
    return sha256((ROOT / path).read_bytes()).hexdigest()


def pinnacles(p):
    return tuple(p[i] for i in range(1, len(p) - 1)
                 if p[i - 1] < p[i] > p[i + 1])


def inversion(p):
    result = [0] * len(p)
    for i, v in enumerate(p):
        result[v - 1] = sum(u < v for u in p[i + 1:])
    return tuple(result)


def decode(table):
    p = []
    for v, k in enumerate(table, 1):
        assert 0 <= k < v
        p.insert(v - 1 - k, v)
    return tuple(p)


def le(a, b):
    assert len(a) == len(b) == 5
    return all(x <= y for x, y in zip(a, b))


def row(p):
    return {"permutation": list(p), "iota": list(inversion(p)),
            "pinnacles": list(pinnacles(p))}


def main():
    retained = ["source.md", "evidence/triage_obstruction.json",
                "evidence/external/2408.02782v1.html",
                "evidence/external/2001.08185v3.html"]
    before = {path: digest(path) for path in retained}
    assert before["source.md"] == SOURCE_HASH

    # Two complete enumerations of S_5: direct permutations and inversion tables.
    direct = list(permutations(range(1, 6)))
    tables = list(product(*(range(v) for v in range(1, 6))))
    decoded = [decode(t) for t in tables]
    assert len(direct) == len(tables) == len(set(decoded)) == 120
    assert set(decoded) == set(direct)
    assert all(inversion(decode(t)) == t for t in tables)
    fiber = sorted(p for p in direct if pinnacles(p) == (5,))
    assert len(fiber) == 56
    prior = json.loads((ROOT / "evidence/triage_obstruction.json").read_text())
    assert prior["n"] == 5 and prior["sigma"] == [5]
    supplied = [(tuple(r["permutation"]), tuple(r["iota"]))
                for r in prior["fiber"]]
    assert len(supplied) == len(set(supplied)) == len(fiber)
    assert set(supplied) == {(p, inversion(p)) for p in fiber}

    vectors = [inversion(p) for p in fiber]
    order = [[le(s, t) for t in vectors] for s in vectors]
    joins, meets, upper_sets, lower_sets = {}, {}, {}, {}
    for i, j in product(range(56), repeat=2):
        upper = [k for k in range(56) if order[i][k] and order[j][k]]
        lower = [k for k in range(56) if order[k][i] and order[k][j]]
        least = [k for k in upper if all(order[k][q] for q in upper)]
        greatest = [k for k in lower if all(order[q][k] for q in lower)]
        assert len(least) == len(greatest) == 1
        joins[i, j], meets[i, j] = least[0], greatest[0]
        upper_sets[i, j], lower_sets[i, j] = upper, lower

    ids = {name: fiber.index(p) for name, p in NAMED.items()}
    names_by_id = {index: name for name, index in ids.items()}
    for name, p in NAMED.items():
        assert pinnacles(p) == (5,)
        assert inversion(p) == EXPECTED_TABLES[name]
    pair_records = []
    for x, y in product(NAMED, repeat=2):
        i, j = ids[x], ids[y]
        assert joins[i, j] in names_by_id and meets[i, j] in names_by_id
        pair_records.append({
            "pair": [x, y], "join": names_by_id[joins[i, j]],
            "meet": names_by_id[meets[i, j]],
            "all_upper_bounds": [list(fiber[k]) for k in upper_sets[i, j]],
            "all_lower_bounds": [list(fiber[k]) for k in lower_sets[i, j]],
        })

    cap = tuple(min(x, y) for x, y in
                zip(EXPECTED_TABLES["a"], EXPECTED_TABLES["c"]))
    box = sorted(decode(t) for t in product(*(range(x + 1) for x in cap)))
    assert box == sorted(p for p in direct if le(inversion(p), cap))
    assert box == [(1, 2, 3, 4, 5), (1, 2, 3, 5, 4),
                   (1, 3, 2, 4, 5), (1, 3, 2, 5, 4)]
    assert [p for p in box if pinnacles(p) == (5,)] == [NAMED["e"]]
    a, b, c, d, e = (ids[name] for name in ("a", "b", "c", "d", "e"))
    assert joins[b, c] == joins[a, c] == d
    assert meets[a, c] == meets[b, c] == e
    assert meets[a, d] == a and meets[a, b] == b and joins[b, e] == b
    lhs = meets[a, joins[b, c]]
    rhs = joins[meets[a, b], meets[a, c]]
    assert lhs == a and rhs == b and lhs != rhs
    assert before == {path: digest(path) for path in retained}

    result = {
        "job_id": JOB, "role": "research", "exact_verification_completed": True,
        "fresh_mathematical_referee": False,
        "script_sha256": digest("evidence/research_certificate.py"),
        "coverage": {"n": 5, "sigma": [5], "ambient_permutations": 120,
                     "fiber_elements": 56, "ordered_pairs_checked": 3136,
                     "named_ordered_pairs_serialized": 25,
                     "distributive_triples_checked": 1,
                     "other_n_checked_in_this_run": []},
        "enumeration": "All 120 permutations agree with all 120 decoded inversion tables; no symmetry reduction.",
        "complete_fiber": [row(p) for p in fiber],
        "named": {name: row(p) for name, p in NAMED.items()},
        "all_fiber_pairs_have_unique_meet_and_join": True,
        "named_pair_bounds": pair_records,
        "complete_ambient_common_lower_box_for_a_c": [row(p) for p in box],
        "distributive_law_failure": {"triple": ["a", "b", "c"],
                                    "lhs": names_by_id[lhs], "rhs": names_by_id[rhs],
                                    "lhs_permutation": list(fiber[lhs]),
                                    "rhs_permutation": list(fiber[rhs])},
        "retained_files_unchanged_sha256": before,
    }
    target = ROOT / "evidence/research_certificate.json"
    temporary = target.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(result, indent=2) + "\n")
    temporary.replace(target)
    print(json.dumps({"job_id": JOB, "coverage": result["coverage"],
                      "failure": result["distributive_law_failure"],
                      "certificate_sha256": digest(str(target.relative_to(ROOT)))}))


if __name__ == "__main__":
    main()
