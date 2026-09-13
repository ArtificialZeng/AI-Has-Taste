#!/Users/mac/4prove-or-disprove-math/.research-venv/bin/python
"""Fresh exact replay for the frozen n_*=24 referee candidate.

This file imports none of the candidate's Python implementations.  It generates
survivor families directly by residue-profile elimination, tests extendibility
both by next-layer membership and by a coverage-state CSP, and checks the
displayed two-clause cores.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def survivors(n: int) -> frozenset[frozenset[int]]:
    """Enumerate F_n directly from S_n(r), deduplicating after each modulus."""
    x_n = frozenset(range(2, n + 2))
    states = {x_n}
    for k in range(2, n + 1):
        next_states = set()
        for state in states:
            for residue in range(k):
                next_states.add(
                    state
                    - frozenset(
                        m for m in range(k + 1, n + 2) if m % k == residue
                    )
                )
        states = next_states
    return frozenset(states)


def instance(n: int, a_set: frozenset[int]):
    omitted = tuple(sorted(set(range(2, n + 2)) - set(a_set)))
    domains = {}
    for k in range(2, n + 1):
        forbidden = {x % k for x in a_set if x > k}
        forbidden.add((n + 2) % k)
        domains[k] = tuple(a for a in range(k) if a not in forbidden)
    clauses = {
        m: tuple((k, m % k) for k in range(2, m) if m % k in domains[k])
        for m in omitted
    }
    return omitted, domains, clauses


def csp_and_local(n: int, a_set: frozenset[int]) -> tuple[bool, bool]:
    """Exact coverage-state DP, represented by integer masks of omitted points."""
    omitted, domains, clauses = instance(n, a_set)
    local = all(domains.values()) and all(clauses.values())
    if not all(domains.values()):
        return False, local
    bit = {m: 1 << i for i, m in enumerate(omitted)}
    target = (1 << len(omitted)) - 1
    covered_states = {0}
    for k in range(2, n + 1):
        blocks = set()
        for residue in domains[k]:
            block = 0
            for m in omitted:
                if m > k and m % k == residue:
                    block |= bit[m]
            blocks.add(block)
        covered_states = {old | block for old in covered_states for block in blocks}
    return target in covered_states, local


def mask(a_set: frozenset[int]) -> int:
    return sum(1 << (m - 2) for m in a_set)


def main() -> None:
    snapshot = json.loads((ROOT / "audit" / "snapshot.json").read_text())
    assert all(sha256(ROOT / name) == digest for name, digest in snapshot["files"].items())
    frozen = json.loads((ROOT / "evidence" / "first_incompatibility.json").read_text())
    families = {n: survivors(n) for n in range(1, 26)}
    rows = []
    all_exceptions = {}
    for n in range(1, 25):
        family = families[n]
        next_family = families[n + 1]
        extendible_next = {
            a_set for a_set in family if a_set | {n + 2} in next_family
        }
        extendible_csp = set()
        local_sets = set()
        for a_set in family:
            sat, local = csp_and_local(n, a_set)
            if sat:
                extendible_csp.add(a_set)
            if local:
                local_sets.add(a_set)
        frozen_layer = frozen["searched_n"][n - 1]
        assert {mask(a) for a in family} == {
            int(value, 16) for value in frozen_layer["survivor_masks_hex"]
        }
        assert {mask(a) for a in extendible_csp} == {
            int(value, 16)
            for value in frozen_layer["extendible_survivor_masks_hex"]
        }
        assert {mask(a) for a in local_sets} == {
            int(value, 16) for value in frozen_layer["local_survivor_masks_hex"]
        }
        assert extendible_next == extendible_csp
        exceptions = local_sets - extendible_next
        all_exceptions[n] = exceptions
        rows.append(
            {
                "n": n,
                "N": len(family),
                "extendible": len(extendible_next),
                "local": len(local_sets),
                "exceptions": len(exceptions),
            }
        )

    expected = {
        frozenset({2} | subset)
        for subset in (
            set(),
            {8},
            {14},
            {20},
            {8, 14},
            {8, 20},
            {14, 20},
            {8, 14, 20},
        )
    }
    assert all(not all_exceptions[n] for n in range(1, 24))
    assert all_exceptions[24] == expected
    assert {
        frozenset(record["A"]) for record in frozen["first_layer"]["exceptions"]
    } == expected

    core_records = []
    for a_set in sorted(expected, key=lambda value: tuple(sorted(value))):
        omitted, domains, clauses = instance(24, a_set)
        assert 4 in omitted and 6 in omitted
        assert domains[2] == (1,)
        assert domains[3] == (0, 1)
        assert clauses[4] == ((3, 1),)
        assert clauses[6] == ((3, 0),)
        core_records.append(
            {
                "A": sorted(a_set),
                "Omega2": list(domains[2]),
                "Omega3": list(domains[3]),
                "clause4": [list(pair) for pair in clauses[4]],
                "clause6": [list(pair) for pair in clauses[6]],
            }
        )

    output = {
        "status": "pass",
        "arithmetic": "exact integer and finite-set operations",
        "imports_candidate_implementations": False,
        "snapshot_digest": snapshot["digest"],
        "source_sha256": sha256(ROOT / "source.md"),
        "coverage": "all survivors for 1<=n<=24; F_25 next-layer check",
        "rows": rows,
        "first_layer": 24,
        "exceptions": [sorted(value) for value in sorted(expected, key=lambda value: tuple(sorted(value)))],
        "core_records": core_records,
        "N25": len(families[25]),
        "csp_equals_next_layer_everywhere": True,
        "matches_frozen_full_families": True,
    }
    path = ROOT / "audit" / "referee_replay.json"
    path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": "pass", "first_layer": 24, "exceptions": 8, "N25": len(families[25])}, sort_keys=True))


if __name__ == "__main__":
    main()
