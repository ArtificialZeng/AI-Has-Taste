#!/Users/mac/4prove-or-disprove-math/.research-venv/bin/python
"""Direct exact implementation of the Theorem 30 residue-choice CSP.

This module does not import or use the Proposition 36 generator.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from typing import Iterable


@dataclass(frozen=True)
class CSPInstance:
    n: int
    survivor: frozenset[int]
    omitted: tuple[int, ...]
    domains: tuple[tuple[int, ...], ...]  # entry k-2 is Omega_k^+
    witnesses: tuple[tuple[int, tuple[tuple[int, int], ...]], ...]


def build_instance(n: int, survivor: Iterable[int]) -> CSPInstance:
    a_set = frozenset(survivor)
    x_set = frozenset(range(2, n + 2))
    if not a_set <= x_set:
        raise ValueError("survivor is not a subset of X_n")
    omitted = tuple(sorted(x_set - a_set))
    domains_list: list[tuple[int, ...]] = []
    for k in range(2, n + 1):
        forbidden = {x % k for x in a_set if x > k}
        forbidden.add((n + 2) % k)
        domains_list.append(tuple(a for a in range(k) if a not in forbidden))
    witnesses: list[tuple[int, tuple[tuple[int, int], ...]]] = []
    for m in omitted:
        choices = tuple(
            (k, m % k)
            for k in range(2, m)
            if (m % k) in domains_list[k - 2]
        )
        witnesses.append((m, choices))
    return CSPInstance(n, a_set, omitted, tuple(domains_list), tuple(witnesses))


def is_local(instance: CSPInstance) -> bool:
    return all(instance.domains) and all(choices for _, choices in instance.witnesses)


def solve(instance: CSPInstance, required: Iterable[int] | None = None):
    """Decide the covering CSP; return (sat, assignment, deterministic proof tree).

    Only residue choices capable of covering a required omitted point are
    branched upon.  Once all required points are covered, unused variables can
    take any value in their nonempty domains.
    """
    if any(not domain for domain in instance.domains):
        k = next(k for k in range(2, instance.n + 1) if not instance.domains[k - 2])
        return False, None, {"leaf": "empty_domain", "k": k}

    required_tuple = tuple(sorted(instance.omitted if required is None else required))
    if not set(required_tuple) <= set(instance.omitted):
        raise ValueError("required points must be omitted points")
    witness_map = dict(instance.witnesses)
    domain_sets = tuple(frozenset(d) for d in instance.domains)
    UNSET = -1

    def covered(m: int, assignment: tuple[int, ...]) -> bool:
        return any(assignment[k - 2] == residue for k, residue in witness_map[m])

    @lru_cache(maxsize=None)
    def search(assignment: tuple[int, ...]):
        uncovered = [m for m in required_tuple if not covered(m, assignment)]
        if not uncovered:
            completed = list(assignment)
            for i, value in enumerate(completed):
                if value == UNSET:
                    completed[i] = min(domain_sets[i])
            return True, tuple(completed), {"leaf": "covered"}

        options_by_m: list[tuple[int, tuple[tuple[int, int], ...]]] = []
        for m in uncovered:
            options = tuple(
                (k, residue)
                for k, residue in witness_map[m]
                if assignment[k - 2] == UNSET
            )
            # An assigned matching residue would have made m covered; assigned
            # nonmatching variables cannot become witnesses later.
            options_by_m.append((m, options))
        m, options = min(options_by_m, key=lambda item: (len(item[1]), item[0]))
        if not options:
            return False, None, {
                "leaf": "uncovered_clause",
                "m": m,
                "assigned_relevant": [
                    [k, assignment[k - 2]]
                    for k, _ in witness_map[m]
                    if assignment[k - 2] != UNSET
                ],
            }

        branches = []
        for k, residue in options:
            assert residue in domain_sets[k - 2]
            child_assignment = list(assignment)
            child_assignment[k - 2] = residue
            sat, model, tree = search(tuple(child_assignment))
            branches.append({"choose": [k, residue], "then": tree})
            if sat:
                return True, model, {"clause": m, "branches": branches}
        return False, None, {"clause": m, "branches": branches}

    initial = tuple(UNSET for _ in range(instance.n - 1))
    return search(initial)


def irreducible_unsat_core(instance: CSPInstance) -> tuple[int, ...]:
    """Deletion-minimal omitted-point core, in deterministic ascending order."""
    sat, _, _ = solve(instance)
    if sat:
        raise ValueError("instance is satisfiable")
    core = list(instance.omitted)
    changed = True
    while changed:
        changed = False
        for m in tuple(core):
            trial = [x for x in core if x != m]
            if not solve(instance, trial)[0]:
                core = trial
                changed = True
    return tuple(core)


def instance_record(instance: CSPInstance) -> dict[str, object]:
    return {
        "n": instance.n,
        "A": sorted(instance.survivor),
        "omitted": list(instance.omitted),
        "domains": {str(k): list(instance.domains[k - 2]) for k in range(2, instance.n + 1)},
        "clauses": {
            str(m): [[k, residue] for k, residue in choices]
            for m, choices in instance.witnesses
        },
    }
