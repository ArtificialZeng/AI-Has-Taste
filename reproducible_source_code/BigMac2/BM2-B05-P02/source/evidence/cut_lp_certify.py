#!/usr/bin/env python3
"""Generate and exactly check complete cut LPs for J_{m,1}.

The script uses one representative of each complementary pair of nontrivial
cuts: the shore not containing vertex ``a``.  Thus there are 2^(2m+1)-1
rows.  LP generation is deterministic; exact certificate checking will be
added once HiGHS solutions have exposed the optimal support.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
from typing import Any


def instance(m: int):
    if m < 2:
        raise ValueError("m must be at least 2")
    vertices = ["a"] + [f"b{i}" for i in range(1, m + 1)] + [f"x{i}" for i in range(1, m + 1)] + ["u"]
    edges: list[tuple[str, str]] = []
    # K_m on B.
    for i in range(1, m + 1):
        for j in range(i + 1, m + 1):
            edges.append((f"b{i}", f"b{j}"))
    # Subdivided a-b_i paths.
    for i in range(1, m + 1):
        edges.extend([("a", f"x{i}"), (f"b{i}", f"x{i}")])
    # K_1 joined to H_m.
    edges.extend(("u", v) for v in vertices if v != "u")
    return vertices, edges


def generate_lp(m: int, path: Path) -> None:
    vertices, edges = instance(m)
    index = {v: i for i, v in enumerate(vertices)}
    names = [f"e{k}" for k in range(len(edges))]
    lines = ["Minimize", " obj: " + " + ".join(names), "Subject To"]
    # Bit 0 corresponds to the first vertex after a.  Since a is kept out of
    # every represented shore, every distinct nontrivial cut occurs once.
    for mask in range(1, 1 << (len(vertices) - 1)):
        crossing = []
        for k, (v, w) in enumerate(edges):
            in_v = v != "a" and bool(mask & (1 << (index[v] - 1)))
            in_w = w != "a" and bool(mask & (1 << (index[w] - 1)))
            if in_v != in_w:
                crossing.append(names[k])
        if not crossing:
            raise AssertionError(f"empty cut at mask {mask}")
        lines.append(f" c{mask}: " + " + ".join(crossing) + " >= 2")
    lines.extend(["Bounds", *(f" {name} >= 0" for name in names), "End", ""])
    path.write_text("\n".join(lines), encoding="utf-8")
    map_path = path.with_suffix(".map")
    map_path.write_text(
        "\n".join(f"e{k} {v} {w}" for k, (v, w) in enumerate(edges)) + "\n",
        encoding="utf-8",
    )


def orbit_weights(m: int, data: dict[str, str]) -> list[Fraction]:
    """Expand six S_m-orbit weights in the same order as ``instance``."""
    w = {key: Fraction(value) for key, value in data.items()}
    _, edges = instance(m)
    ans: list[Fraction] = []
    for v, z in edges:
        pair = {v, z}
        if v.startswith("b") and z.startswith("b"):
            key = "bb"
        elif "a" in pair and any(q.startswith("x") for q in pair):
            key = "ax"
        elif any(q.startswith("b") for q in pair) and any(q.startswith("x") for q in pair):
            key = "bx"
        elif pair == {"u", "a"}:
            key = "ua"
        elif "u" in pair and any(q.startswith("b") for q in pair):
            key = "ub"
        elif "u" in pair and any(q.startswith("x") for q in pair):
            key = "ux"
        else:
            raise AssertionError((v, z))
        ans.append(w[key])
    return ans


def crosses(mask: int, endpoint_index: int) -> bool:
    """Membership in the represented shore (which never contains a)."""
    return endpoint_index != 0 and bool(mask & (1 << (endpoint_index - 1)))


def dual_certificate(m: int, kind: str) -> dict[int, Fraction]:
    vertices, _ = instance(m)
    index = {v: i for i, v in enumerate(vertices)}
    if kind == "singleton":
        # The singleton cut of a is represented by its complementary shore.
        dual = {(1 << (len(vertices) - 1)) - 1: Fraction(1, 2)}
        dual.update({1 << (i - 1): Fraction(1, 2) for i in range(1, len(vertices))})
        return dual
    if kind == "path":
        dual: dict[int, Fraction] = {}
        for i in range(1, m + 1):
            b = 1 << (index[f"b{i}"] - 1)
            x = 1 << (index[f"x{i}"] - 1)
            dual[b] = Fraction(1, 4)
            dual[x] = Fraction(3, 4)
            dual[b | x] = Fraction(1, 4)
        return dual
    raise ValueError(f"unknown dual type: {kind}")


def verify_instance(m: int, datum: dict[str, Any]) -> dict[str, Any]:
    vertices, edges = instance(m)
    index = {v: i for i, v in enumerate(vertices)}
    weights = orbit_weights(m, datum["primal_orbits"])
    claimed = Fraction(datum["claimed_optimum"])
    if len(weights) != len(edges) or any(q < 0 for q in weights):
        raise AssertionError("invalid primal vector")

    min_cut: Fraction | None = None
    tight_cuts = 0
    total_cuts = (1 << (len(vertices) - 1)) - 1
    for mask in range(1, total_cuts + 1):
        value = sum(
            weights[k]
            for k, (v, z) in enumerate(edges)
            if crosses(mask, index[v]) != crosses(mask, index[z])
        )
        if value < 2:
            raise AssertionError(f"J_{{{m},1}} cut mask {mask} has weight {value}")
        if min_cut is None or value < min_cut:
            min_cut = value
        if value == 2:
            tight_cuts += 1

    primal_objective = sum(weights)
    if primal_objective != claimed:
        raise AssertionError((primal_objective, claimed))

    dual = dual_certificate(m, datum["dual_type"])
    full_mask = total_cuts
    if any(mask <= 0 or mask > full_mask or q < 0 for mask, q in dual.items()):
        raise AssertionError("invalid dual support")
    loads: list[Fraction] = []
    for v, z in edges:
        load = sum(
            q
            for mask, q in dual.items()
            if crosses(mask, index[v]) != crosses(mask, index[z])
        )
        if load > 1:
            raise AssertionError(f"dual overload on {v}-{z}: {load}")
        loads.append(load)
    dual_objective = 2 * sum(dual.values())
    if dual_objective != claimed or dual_objective != primal_objective:
        raise AssertionError((primal_objective, dual_objective, claimed))

    return {
        "m": m,
        "vertices": len(vertices),
        "edges": len(edges),
        "distinct_nontrivial_cuts_checked": total_cuts,
        "minimum_primal_cut_weight": str(min_cut),
        "tight_primal_cuts": tight_cuts,
        "dual_support_size": len(dual),
        "maximum_dual_edge_load": str(max(loads)),
        "primal_objective": str(primal_objective),
        "dual_objective": str(dual_objective),
        "certified_optimum": str(claimed),
        "order": 2 * m + 2,
        "fractionally_hamiltonian": claimed == 2 * m + 2,
    }


def verify_file(path: Path, output: Path | None) -> None:
    raw = path.read_bytes()
    data = json.loads(raw)
    results = [
        verify_instance(int(m), datum)
        for m, datum in sorted(data["instances"].items(), key=lambda item: int(item[0]))
    ]
    summary = {
        "certificate_file": str(path),
        "certificate_sha256": hashlib.sha256(raw).hexdigest(),
        "arithmetic": "Python fractions.Fraction (exact rational arithmetic)",
        "cut_enumeration": "all nonempty shores not containing a; one per complementary pair",
        "instances": results,
        "status": "verified",
    }
    rendered = json.dumps(summary, indent=2, sort_keys=True) + "\n"
    if output is None:
        print(rendered, end="")
    else:
        output.write_text(rendered, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    gen = sub.add_parser("generate")
    gen.add_argument("m", type=int)
    gen.add_argument("output", type=Path)
    verify = sub.add_parser("verify")
    verify.add_argument("certificate", type=Path)
    verify.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.command == "generate":
        generate_lp(args.m, args.output)
    else:
        verify_file(args.certificate, args.output)


if __name__ == "__main__":
    main()
