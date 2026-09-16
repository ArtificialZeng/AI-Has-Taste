#!/usr/bin/env python3
"""Exact CP-SAT search for a 4-dimensional linear connectivity code.

An edge label is a vector in F_2^4, stored as four Boolean variables.  For
every nonzero covector a, edge e is selected when a dot label(e) = 1.  We
require the selected spanning subgraph to be connected by routing one unit
from vertex 0 to each other vertex.  At each vertex all 15 nonempty XORs of
the four incident labels are constrained to be nonzero, which is exactly the
condition that those four labels form a basis.

The labels on the four edges incident with vertex 0 are fixed to the standard
basis.  This loses no solutions, because the local basis condition and every
connectivity condition are invariant under GL(4,2) acting on all labels.
"""

import argparse
import json
from pathlib import Path

from ortools.sat.python import cp_model


VERTICES = [(i, j) for i in range(3) for j in range(4)]
INDEX = {v: k for k, v in enumerate(VERTICES)}
EDGES = []
for i in range(3):
    for j in range(4):
        EDGES.append((INDEX[(i, j)], INDEX[((i + 1) % 3, j)]))
for i in range(3):
    for j in range(4):
        EDGES.append((INDEX[(i, j)], INDEX[(i, (j + 1) % 4)]))
assert len(EDGES) == len({tuple(sorted(e)) for e in EDGES}) == 24


def add_xor_equals(model, variables, target, name):
    """Create Boolean y equal to XOR(variables), then constrain y=target."""
    y = model.new_bool_var(name)
    # XOR(variables, not y)=1 is equivalent to y=XOR(variables).
    model.add_bool_xor([*variables, y.negated()])
    model.add(y == target)


def build_model():
    model = cp_model.CpModel()
    bit = [[model.new_bool_var(f"x_{e}_{b}") for b in range(4)] for e in range(24)]

    incident = [[] for _ in range(12)]
    for e, (u, v) in enumerate(EDGES):
        incident[u].append(e)
        incident[v].append(e)
    assert all(len(es) == 4 for es in incident)

    # A basis at every vertex: every nonempty subset has nonzero XOR.
    for v, es in enumerate(incident):
        for subset in range(1, 16):
            nonzero_bits = []
            chosen = [es[k] for k in range(4) if (subset >> k) & 1]
            for b in range(4):
                y = model.new_bool_var(f"basis_{v}_{subset}_{b}")
                model.add_bool_xor([*[bit[e][b] for e in chosen], y.negated()])
                nonzero_bits.append(y)
            model.add_bool_or(nonzero_bits)

    # Global GL(4,2) symmetry breaking at root vertex 0.
    root_edges = incident[0]
    for k, e in enumerate(root_edges):
        for b in range(4):
            model.add(bit[e][b] == int(k == b))

    selected = {}
    for a in range(1, 16):
        for e in range(24):
            s = model.new_bool_var(f"sel_{a}_{e}")
            active_bits = [bit[e][b] for b in range(4) if (a >> b) & 1]
            model.add_bool_xor([*active_bits, s.negated()])
            selected[a, e] = s

        # A feasible integral flow is equivalent to connectivity: root 0 sends
        # one unit to each of the other 11 vertices along selected edges.
        outgoing = [[] for _ in range(12)]
        incoming = [[] for _ in range(12)]
        for e, (u, v) in enumerate(EDGES):
            f_uv = model.new_int_var(0, 11, f"flow_{a}_{e}_{u}_{v}")
            f_vu = model.new_int_var(0, 11, f"flow_{a}_{e}_{v}_{u}")
            model.add(f_uv <= 11 * selected[a, e])
            model.add(f_vu <= 11 * selected[a, e])
            outgoing[u].append(f_uv)
            incoming[v].append(f_uv)
            outgoing[v].append(f_vu)
            incoming[u].append(f_vu)
        for v in range(12):
            model.add(sum(outgoing[v]) - sum(incoming[v]) == (11 if v == 0 else -1))

    return model, bit, incident


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="evidence/linear_witness.json")
    parser.add_argument("--time-limit", type=float, default=900.0)
    args = parser.parse_args()

    model, bit, incident = build_model()
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = args.time_limit
    solver.parameters.num_search_workers = 1
    solver.parameters.random_seed = 5102
    solver.parameters.log_search_progress = True
    status = solver.solve(model)
    status_name = solver.status_name(status)
    print("status", status_name)
    print("wall_time", solver.wall_time)
    print("branches", solver.num_branches)
    print("conflicts", solver.num_conflicts)
    if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        return 2

    labels = [sum(solver.value(bit[e][b]) << b for b in range(4)) for e in range(24)]
    generators = []
    for b in range(4):
        mask = sum(((labels[e] >> b) & 1) << e for e in range(24))
        generators.append(f"{mask:06x}")
    certificate = {
        "graph": "C3 square C4",
        "vertices": [list(v) for v in VERTICES],
        "edges": [list(e) for e in EDGES],
        "edge_labels_hex": [f"{x:x}" for x in labels],
        "generators_24bit_hex": generators,
        "root_incident_edges": incident[0],
        "solver": {
            "name": "OR-Tools CP-SAT",
            "status": status_name,
            "wall_time_seconds": solver.wall_time,
            "branches": solver.num_branches,
            "conflicts": solver.num_conflicts,
            "random_seed": 5102,
            "workers": 1,
        },
    }
    output = Path(args.output)
    output.write_text(json.dumps(certificate, indent=2) + "\n")
    print("wrote", output)
    print("labels", " ".join(certificate["edge_labels_hex"]))
    print("generators", " ".join(generators))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
