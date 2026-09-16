#!/usr/bin/env python3
"""Exact exhaustive enumeration for the r=3 four-layer starter problem.

There are three vertices in every tail residue class modulo 4.  Balance says
that their outgoing steps are a permutation of (1,2,3), so the full search
space has exactly (3!)^4 = 1296 assignments.  The program first enumerates the
entire space (no symmetry breaking), then groups the Hamilton starters under
translations of Z_12 and tests every starter for a simple rainbow 3-arc path.

The JSON output is a replayable finite certificate.  It gives every balanced
assignment orbit under translations, and for every assignment that is even a
permutation of Z_12 it gives all directed cycles.  Thus every possible starter
is visibly excluded if none of these cycles has length 12.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path


R = 3
N = 4 * R
STEPS = tuple(range(1, R + 1))
PERMS = tuple(itertools.permutations(STEPS))


def assignment_from_layers(layers: tuple[tuple[int, ...], ...]) -> tuple[int, ...]:
    """Return s[x], where layers[j][t] is the step at x=j+4t."""
    ans = [0] * N
    for j in range(4):
        for t in range(R):
            ans[j + 4 * t] = layers[j][t]
    return tuple(ans)


def is_hamilton(step_at: tuple[int, ...]) -> bool:
    succ = tuple((x + step_at[x]) % N for x in range(N))
    if len(set(succ)) != N:
        return False
    seen = set()
    x = 0
    while x not in seen:
        seen.add(x)
        x = succ[x]
    return x == 0 and len(seen) == N


def directed_cycles(step_at: tuple[int, ...]) -> list[list[int]] | None:
    """Return the cycles of the successor permutation, or None if not bijective."""
    succ = tuple((x + step_at[x]) % N for x in range(N))
    if len(set(succ)) != N:
        return None
    unseen = set(range(N))
    cycles = []
    while unseen:
        start = min(unseen)
        cycle = []
        x = start
        while x in unseen:
            unseen.remove(x)
            cycle.append(x)
            x = succ[x]
        assert x == start
        cycles.append(cycle)
    return cycles


def translate(step_at: tuple[int, ...], a: int) -> tuple[int, ...]:
    """Translate every starter arc by a in Z_12."""
    return tuple(step_at[(x - a) % N] for x in range(N))


def canonical_translation(step_at: tuple[int, ...]) -> tuple[int, ...]:
    return min(translate(step_at, a) for a in range(N))


def beta_table(step_at: tuple[int, ...]) -> list[list[int]]:
    beta = [[-1] * (R + 1) for _ in range(4)]
    for x, s in enumerate(step_at):
        j = x % 4
        t = (x - j) // 4
        assert beta[j][s] == -1
        beta[j][s] = t
    assert all(beta[j][s] >= 0 for j in range(4) for s in STEPS)
    return beta


def colour(beta: list[list[int]], x: int, s: int) -> int:
    j = x % 4
    t = (x - j) // 4
    return (t - beta[j][s]) % R


def rainbow_paths(step_at: tuple[int, ...]):
    beta = beta_table(step_at)
    for start in range(N):
        for path_steps in itertools.product(STEPS, repeat=R):
            vertices = [start]
            colours = []
            x = start
            simple = True
            for s in path_steps:
                colours.append(colour(beta, x, s))
                x = (x + s) % N
                if x in vertices:
                    simple = False
                    break
                vertices.append(x)
            if simple and len(set(colours)) == R:
                yield {
                    "vertices": vertices,
                    "steps": list(path_steps),
                    "arcs": [[vertices[i], vertices[i + 1]] for i in range(R)],
                    "colours": colours,
                }


def detailed_witness(step_at: tuple[int, ...], path: dict) -> dict:
    beta = beta_table(step_at)
    cycle_vertices = [0]
    x = 0
    for _ in range(N):
        x = (x + step_at[x]) % N
        cycle_vertices.append(x)
    cycle_steps = [step_at[x] for x in cycle_vertices[:-1]]

    colour_calculations = []
    for x, s, k in zip(path["vertices"][:-1], path["steps"], path["colours"]):
        j = x % 4
        t = (x - j) // 4
        colour_calculations.append(
            {
                "tail": x,
                "step": s,
                "j": j,
                "t": t,
                "beta_j_s": beta[j][s],
                "colour_mod_3": k,
                "identity": f"{t}-{beta[j][s]} = {k} (mod 3)",
            }
        )

    balance_tails = {
        str(s): [x for x in range(N) if step_at[x] == s] for s in STEPS
    }
    return {
        "step_at_tail_0_to_11": list(step_at),
        "cycle_vertices_including_return": cycle_vertices,
        "cyclic_step_word_from_0": cycle_steps,
        "balance_tails_by_step": balance_tails,
        "beta_rows_j_0_to_3_columns_s_1_to_3": [row[1:] for row in beta],
        "rainbow_path": path,
        "colour_calculations": colour_calculations,
    }


def main() -> None:
    all_starters = []
    compatible = []
    first_path = {}
    all_assignments = []
    bijective_records = []
    assignments_checked = 0

    for layers in itertools.product(PERMS, repeat=4):
        assignments_checked += 1
        step_at = assignment_from_layers(layers)
        all_assignments.append(step_at)
        cycles = directed_cycles(step_at)
        if cycles is not None:
            bijective_records.append(
                {
                    "step_at_tail_0_to_11": list(step_at),
                    "successor_0_to_11": [(x + step_at[x]) % N for x in range(N)],
                    "cycles": cycles,
                    "cycle_lengths": sorted(map(len, cycles)),
                }
            )
        if not is_hamilton(step_at):
            continue
        all_starters.append(step_at)
        path = next(rainbow_paths(step_at), None)
        if path is not None:
            compatible.append(step_at)
            first_path[step_at] = path

    # This quotient is performed only after the full, unsymmetrized search.
    # Translation is safe: it preserves all steps, permutes the four tail
    # residues, and conjugates the successor map on Z_12.
    orbit_members: dict[tuple[int, ...], list[tuple[int, ...]]] = {}
    for assignment in all_assignments:
        orbit_members.setdefault(canonical_translation(assignment), []).append(assignment)

    orbit_records = []
    for representative in sorted(orbit_members):
        members = orbit_members[representative]
        cycles = directed_cycles(representative)
        orbit_records.append(
            {
                "representative_step_at_tail_0_to_11": list(representative),
                "number_of_enumerated_members": len(members),
                "translation_stabilizer_size": sum(
                    translate(representative, a) == representative for a in range(N)
                ),
                "successor_is_bijective": cycles is not None,
                "cycle_lengths_if_bijective": (
                    sorted(map(len, cycles)) if cycles is not None else None
                ),
            }
        )

    assert assignments_checked == len(PERMS) ** 4 == 1296
    assert len(all_assignments) == sum(len(v) for v in orbit_members.values())
    assert all(is_hamilton(s) for s in all_starters)
    assert all(canonical_translation(s) in orbit_members for s in all_assignments)
    assert sum(12 // rec["translation_stabilizer_size"] for rec in orbit_records) == len(all_assignments)

    # Generate the same domain a second way: scan all 3^12 step assignments
    # and retain exactly those satisfying the four balance conditions.
    alternate_domain = {
        word
        for word in itertools.product(STEPS, repeat=N)
        if all(sorted(word[j::4]) == list(STEPS) for j in range(4))
    }
    assert alternate_domain == set(all_assignments)

    cycle_type_counts: dict[str, int] = {}
    for rec in bijective_records:
        key = "+".join(map(str, rec["cycle_lengths"]))
        cycle_type_counts[key] = cycle_type_counts.get(key, 0) + 1
    bijective_orbit_count = len(
        {canonical_translation(tuple(rec["step_at_tail_0_to_11"])) for rec in bijective_records}
    )

    witness = None
    if all_starters:
        representative = min(all_starters)
        witness = detailed_witness(representative, first_path[representative])
    output = {
        "parameters": {"r": R, "n": N, "steps": list(STEPS)},
        "domain_argument": {
            "description": "For each j in Z_4, balance assigns steps 1,2,3 bijectively to tails j,j+4,j+8.",
            "permutations_per_layer": len(PERMS),
            "layers": 4,
            "assignments_checked": assignments_checked,
            "alternate_generation": "all 3^12 words filtered by the four layer-balance predicates",
            "alternate_domain_size": len(alternate_domain),
            "the_two_generated_domains_are_equal": True,
        },
        "successor_permutation_count": len(bijective_records),
        "successor_permutation_translation_orbit_count": bijective_orbit_count,
        "successor_permutation_cycle_type_counts": cycle_type_counts,
        "hamilton_starter_count": len(all_starters),
        "chain_compatible_starter_count": len(compatible),
        "balanced_assignment_translation_orbit_count": len(orbit_records),
        "rainbow_path_tested_hamilton_starter_count": len(all_starters),
        "truth_values_established": {"E_3": bool(all_starters), "C_3": bool(compatible)},
        "logical_note": "C_3 is false because C_3 implies E_3 and the exhaustive domain contains no Hamilton starter.",
        "explicit_E3_C3_witness_if_true": witness,
        "all_bijective_successor_assignments": bijective_records,
        "balanced_assignment_translation_orbits": orbit_records,
    }
    encoded = json.dumps(output, indent=2, sort_keys=True) + "\n"
    out_path = Path(__file__).with_name("r3_enumeration.json")
    out_path.write_text(encoded, encoding="utf-8")
    print(encoded, end="")
    print("sha256=" + hashlib.sha256(encoded.encode()).hexdigest())


if __name__ == "__main__":
    main()
