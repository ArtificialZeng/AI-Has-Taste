#!/usr/bin/env python3
"""Find and exactly verify r=7 balanced Hamilton/chain witnesses.

The CP-SAT model has one Boolean y[x,s] for every allowed arc x -> x+s.
It imposes one outgoing arc per vertex, one use of every step in every tail
class modulo 4, and a single directed circuit through all 28 vertices.
The latter also implies one incoming arc per vertex.  After solving, separate
plain-Python assertions verify the explicit witness and a depth-first search
finds a simple seven-arc path with all seven development colours.

This is a witness search, not an exhaustive nonexistence certificate.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from ortools.sat.python import cp_model


R = 7
N = 4 * R
STEPS = tuple(range(1, R + 1))


def build_and_solve() -> tuple[int, ...]:
    model = cp_model.CpModel()
    use = {
        (x, s): model.new_bool_var(f"arc_{x}_{s}")
        for x in range(N)
        for s in STEPS
    }

    for x in range(N):
        model.add_exactly_one(use[x, s] for s in STEPS)
    for j in range(4):
        for s in STEPS:
            model.add_exactly_one(use[x, s] for x in range(j, N, 4))

    # Every literal is an allowed non-loop arc.  AddCircuit selects exactly
    # one incoming and outgoing arc at every node and forbids subtours.
    model.add_circuit(
        [(x, (x + s) % N, use[x, s]) for x in range(N) for s in STEPS]
    )

    # Safe translation normalization: translate any step-1 tail to vertex 0.
    model.add(use[0, 1] == 1)

    solver = cp_model.CpSolver()
    solver.parameters.num_search_workers = 1
    solver.parameters.random_seed = 0
    solver.parameters.cp_model_presolve = True
    status = solver.solve(model)
    if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        raise RuntimeError(
            "No witness was returned; this status is not an UNSAT certificate: "
            + solver.status_name(status)
        )
    return tuple(
        next(s for s in STEPS if solver.boolean_value(use[x, s]))
        for x in range(N)
    )


def verify_starter(step_at: tuple[int, ...]) -> list[int]:
    assert len(step_at) == N
    assert all(s in STEPS for s in step_at)
    for j in range(4):
        assert sorted(step_at[j::4]) == list(STEPS)

    succ = [(x + step_at[x]) % N for x in range(N)]
    assert sorted(succ) == list(range(N))
    cycle = [0]
    x = 0
    for _ in range(N):
        x = succ[x]
        cycle.append(x)
    assert cycle[-1] == 0
    assert len(set(cycle[:-1])) == N
    return cycle


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


def first_rainbow_path(step_at: tuple[int, ...]) -> dict | None:
    beta = beta_table(step_at)

    def extend(vertices: list[int], steps: list[int], colours: list[int]):
        if len(steps) == R:
            return vertices[:], steps[:], colours[:]
        x = vertices[-1]
        for s in STEPS:
            y = (x + s) % N
            k = colour(beta, x, s)
            if y in vertices or k in colours:
                continue
            vertices.append(y)
            steps.append(s)
            colours.append(k)
            found = extend(vertices, steps, colours)
            if found is not None:
                return found
            vertices.pop()
            steps.pop()
            colours.pop()
        return None

    for start in range(N):
        found = extend([start], [], [])
        if found is not None:
            vertices, steps, colours = found
            assert len(set(vertices)) == R + 1
            assert sorted(colours) == list(range(R))
            return {
                "vertices": vertices,
                "steps": steps,
                "arcs": [[vertices[i], vertices[i + 1]] for i in range(R)],
                "development_colours": colours,
            }
    return None


def make_output(step_at: tuple[int, ...]) -> dict:
    cycle = verify_starter(step_at)
    beta = beta_table(step_at)
    path = first_rainbow_path(step_at)
    if path is None:
        raise RuntimeError("The first starter had no rainbow path; C_7 remains open")

    calculations = []
    selected_arcs_by_cycle = [None] * R
    for x, s, k in zip(
        path["vertices"][:-1], path["steps"], path["development_colours"]
    ):
        j = x % 4
        t = (x - j) // 4
        base_tail = j + 4 * beta[j][s]
        assert (base_tail + 4 * k) % N == x
        selected_arcs_by_cycle[k] = [x, (x + s) % N]
        calculations.append(
            {
                "tail": x,
                "step": s,
                "j": j,
                "t": t,
                "beta_j_s": beta[j][s],
                "colour": k,
                "check": f"{t}-{beta[j][s]} = {k} (mod 7)",
                "base_tail_plus_4_colour_mod_28": x,
            }
        )
    assert all(arc is not None for arc in selected_arcs_by_cycle)

    balance_tails = {
        str(s): [x for x in range(N) if step_at[x] == s] for s in STEPS
    }
    assert all(sorted(x % 4 for x in tails) == [0, 1, 2, 3]
               for tails in balance_tails.values())
    cycle_steps = [step_at[x] for x in cycle[:-1]]
    assert sum(cycle_steps) % N == 0

    return {
        "parameters": {"r": R, "n": N, "steps": list(STEPS)},
        "claim_scope": "Explicit existence witnesses only; no enumeration or uniqueness claim.",
        "model": {
            "variables": "y[x,s] for x in Z_28 and s in {1,...,7}",
            "constraints": [
                "exactly one selected outgoing allowed arc at each x",
                "for every j mod 4 and s, exactly one selected tail x congruent to j uses s",
                "OR-Tools AddCircuit on all 196 allowed labelled arcs",
                "safe translation normalization y[0,1]=1",
            ],
            "warning": "Solver feasibility is only how the witness was found; the serialized witness is checked directly below.",
        },
        "step_at_tail_0_to_27": list(step_at),
        "successor_0_to_27": [(x + step_at[x]) % N for x in range(N)],
        "cycle_vertices_including_return": cycle,
        "cyclic_step_word_from_0": cycle_steps,
        "balance_tails_by_step": balance_tails,
        "beta_rows_j_0_to_3_columns_s_1_to_7": [row[1:] for row in beta],
        "rainbow_path": path,
        "colour_calculations": calculations,
        "selected_arc_from_each_developed_cycle_H_k_k_0_to_6": selected_arcs_by_cycle,
        "truth_values_established": {"E_7": True, "C_7": True},
        "direct_verification": {
            "cycle_has_28_distinct_tails": True,
            "cycle_returns_to_zero": True,
            "each_step_has_one_tail_in_each_mod_4_class": True,
            "path_has_8_distinct_vertices": True,
            "path_colours_are_exactly_0_to_6": True,
        },
    }


def main() -> None:
    output = make_output(build_and_solve())
    encoded = json.dumps(output, indent=2, sort_keys=True) + "\n"
    out_path = Path(__file__).with_name("r7_witness.json")
    out_path.write_text(encoded, encoding="utf-8")
    print(encoded, end="")
    print("sha256=" + hashlib.sha256(encoded.encode()).hexdigest())


if __name__ == "__main__":
    main()
