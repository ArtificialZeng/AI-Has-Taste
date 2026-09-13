#!/Users/mac/4prove-or-disprove-math/.research-venv/bin/python
"""Independent set-based replay of the finite result.

This intentionally imports neither implementation used by the search.  Survivor
families are represented by frozensets, and the CSP is decided by dynamic
enumeration of all attainable coverage unions (rather than clause branching).
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SEARCH_CERT = ROOT / "evidence" / "first_incompatibility.json"
OUTPUT = ROOT / "evidence" / "independent_audit.json"


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def family(n: int, keep_profiles: bool = False):
    """Definition-5 unions using frozensets, with optional profile provenance."""
    states: dict[frozenset[int], tuple[int, ...]] = {frozenset(): ()}
    for k in range(2, n + 1):
        next_states: dict[frozenset[int], tuple[int, ...]] = {}
        for eliminated, profile in states.items():
            for residue in range(k):
                local = frozenset(
                    m for m in range(k + 1, n + 2) if m % k == residue
                )
                union = eliminated | local
                if union not in next_states:
                    next_states[union] = profile + (residue,)
        states = next_states
    x_n = frozenset(range(2, n + 2))
    if keep_profiles:
        return {x_n - eliminated: profile for eliminated, profile in states.items()}
    return frozenset(x_n - eliminated for eliminated in states)


def domains_and_clauses(n: int, a_set: frozenset[int]):
    omitted = frozenset(range(2, n + 2)) - a_set
    domains: dict[int, frozenset[int]] = {}
    for k in range(2, n + 1):
        forbidden = frozenset(x % k for x in a_set if x > k) | {(n + 2) % k}
        domains[k] = frozenset(range(k)) - forbidden
    clauses = {
        m: frozenset((k, m % k) for k in range(2, m) if m % k in domains[k])
        for m in omitted
    }
    return omitted, domains, clauses


def coverage_dp(n: int, a_set: frozenset[int]):
    """Theorem-30 decision by attainable coverage unions."""
    omitted, domains, clauses = domains_and_clauses(n, a_set)
    if any(not domains[k] for k in domains):
        return False, omitted, domains, clauses
    attainable = {frozenset()}
    for k in range(2, n + 1):
        blocks = {
            frozenset(m for m in omitted if m > k and m % k == residue)
            for residue in domains[k]
        }
        attainable = {old | block for old in attainable for block in blocks}
    return omitted in attainable, omitted, domains, clauses


def set_mask(a_set: frozenset[int]) -> int:
    return sum(1 << (m - 2) for m in a_set)


def main() -> None:
    expected = json.loads(SEARCH_CERT.read_text())
    expected_rows = {
        row["n"]: (
            row["N"],
            row["extendible_count_csp"],
            row["local_count"],
            row["exception_count"],
        )
        for row in expected["searched_n"]
    }
    rows = []
    found: list[frozenset[int]] = []
    families: dict[int, frozenset[frozenset[int]]] = {}
    for n in range(1, 25):
        f_n = family(n)
        families[n] = f_n
        extendible = 0
        local = 0
        extendible_sets = set()
        local_sets = set()
        exceptions = []
        for a_set in f_n:
            sat, omitted, domains, clauses = coverage_dp(n, a_set)
            local_here = all(domains.values()) and all(clauses.values())
            extendible += int(sat)
            local += int(local_here)
            if sat:
                extendible_sets.add(a_set)
            if local_here:
                local_sets.add(a_set)
            if local_here and not sat:
                exceptions.append(a_set)
        exceptions.sort(key=lambda a: tuple(sorted(a)))
        row = {
            "n": n,
            "N": len(f_n),
            "extendible_count_coverage_dp": extendible,
            "local_count": local,
            "exception_count": len(exceptions),
        }
        assert (len(f_n), extendible, local, len(exceptions)) == expected_rows[n]
        expected_layer = expected["searched_n"][n - 1]
        assert {int(x, 16) for x in expected_layer["survivor_masks_hex"]} == {
            set_mask(a) for a in f_n
        }
        assert {int(x, 16) for x in expected_layer["extendible_survivor_masks_hex"]} == {
            set_mask(a) for a in extendible_sets
        }
        assert {int(x, 16) for x in expected_layer["local_survivor_masks_hex"]} == {
            set_mask(a) for a in local_sets
        }
        rows.append(row)
        if exceptions:
            assert n == 24 and not found
            found = exceptions

    expected_sets = {
        frozenset(record["A"])
        for record in expected["first_layer"]["exceptions"]
    }
    assert set(found) == expected_sets

    f25 = family(25)
    extendible_via_definition26 = {
        a_set for a_set in families[24] if a_set | {26} in f25
    }
    extendible_via_dp = {
        a_set for a_set in families[24] if coverage_dp(24, a_set)[0]
    }
    assert extendible_via_definition26 == extendible_via_dp

    with_profiles = family(24, keep_profiles=True)
    profile_records = []
    for a_set in found:
        profile = with_profiles[a_set]
        # Directly replay S_24(r).
        replay = frozenset(
            m
            for m in range(2, 26)
            if all(m % k != profile[k - 2] for k in range(2, m))
        )
        assert replay == a_set
        profile_records.append(
            {
                "A": sorted(a_set),
                "profile": {str(k): profile[k - 2] for k in range(2, 25)},
            }
        )

    # Uniform L_24 witnesses for the entire classified family.
    domain_representatives = {}
    for k in range(2, 25):
        intersection = set(range(k))
        for a_set in found:
            _, domains, _ = domains_and_clauses(24, a_set)
            intersection &= set(domains[k])
        assert intersection
        domain_representatives[str(k)] = min(intersection)

    witness_rule = {}
    for m in range(3, 26):
        relevant = [a_set for a_set in found if m not in a_set]
        common = None
        for a_set in relevant:
            _, _, clauses = domains_and_clauses(24, a_set)
            common = set(clauses[m]) if common is None else common & set(clauses[m])
        assert common
        # Prefer the concise parity/mod-3/mod-5 witnesses used in the report.
        if m % 2 == 1:
            chosen = (2, 1)
        elif m % 3 == 0:
            chosen = (3, 0)
        elif m % 3 == 1:
            chosen = (3, 1)
        else:
            chosen = (5, m % 5)
        assert chosen in common
        witness_rule[str(m)] = list(chosen)

    output = {
        "audit_method": {
            "survivors": "frozenset union enumeration from Definition 5",
            "csp": "dynamic enumeration of attainable coverage unions",
            "imports_search_implementation": False,
        },
        "source_sha256": file_hash(ROOT / "source.md"),
        "search_certificate_sha256": file_hash(SEARCH_CERT),
        "layers": rows,
        "first_layer": 24,
        "exception_sets": [sorted(a) for a in found],
        "definition26_crosscheck": {
            "N24": len(families[24]),
            "N25": len(f25),
            "extendible_count": len(extendible_via_dp),
            "families_agree": True,
        },
        "realizing_profiles": profile_records,
        "uniform_local_certificate": {
            "domain_representatives": domain_representatives,
            "omitted_point_witnesses": witness_rule,
        },
    }
    OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": "pass",
        "first_layer": 24,
        "exception_count": len(found),
        "N24": len(families[24]),
        "N25": len(f25),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
