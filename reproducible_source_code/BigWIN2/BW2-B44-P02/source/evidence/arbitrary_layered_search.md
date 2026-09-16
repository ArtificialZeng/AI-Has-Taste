# Arbitrary sparse four-slot layered search

Provenance: `win-00044-p02-research-b2d03b556735`  
Date: 2026-09-06

## Exact finite model

The cyclic period has 13 layers and four potential vertices per layer. A
potential vertex may be inactive; every layer has at least one active vertex.
Edges may be chosen arbitrarily inside one layer and between consecutive
layers, including the layer-12/layer-0 boundary, and no other edges are
allowed. At least one edge is required across each layer boundary. This last
condition is necessary for the intended periodic chain, but it does not by
itself force all active vertices to be connected.

For denominator `D` in `{40,80}`, each active vertex `v` has integer numerator
`1 <= q_v <= D`, hence weight `q_v/D`; inactive slots have numerator zero.
The upper bound loses no possible strict-mass witness: if `q_v>D`, replacing it
by `D` preserves every neighbor's weighted-degree lower bound and decreases
mass. Binary variables choose the 286 possible edges. Product variables encode
`e_uv*q_v`, and every active `u` is constrained by

```text
sum(e_uv*q_v : v is a possible neighbor of u) >= D.
```

Every clique lies in the union of two consecutive layers. For each of the 13
eight-slot unions and each of its eight seven-subsets, the sum of its 21 edge
variables is at most 20. These 104 inequalities are exactly `K_7` exclusion
for this model. The strict target is imposed integrally as

```text
sum(q_v) <= 194  when D=40,
sum(q_v) <= 389  when D=80.
```

Weights are sorted within layers, layer zero is chosen to have minimum total
weight, and reflection is fixed by `A_1<=A_12`; these are safe symmetry cuts.
`evidence/arbitrary_layered_milp.py` gives a SciPy/HiGHS big-M formulation.
`evidence/arbitrary_layered_cpsat.py` gives the same finite model with native
integer products in OR-Tools CP-SAT and independently checks any returned
witness using integer arithmetic and explicit seven-subset enumeration. Both
solvers were restricted to one process; CP-SAT used one search worker.

## Control witness

The non-strict `D=40` control was recovered by CP-SAT from an explicit hint
and then checked exactly. In every layer the weights are

```text
(0,5,5,5)/40.
```

All edges among active vertices inside and between consecutive layers are
present. The exact checker reports 39 active vertices, 156 chosen edges, mass
`195/40=39/8`, minimum weighted-degree numerator 40, zero seven-cliques, one
39-vertex component both in the cyclic quotient and after deleting the wrap
edges, and wall time 15.14 seconds. This is the known complete-layered equality
construction and is only a model/control check, not a new result.

Reproduction:

```text
python3 evidence/arbitrary_layered_cpsat.py --denominator 40 \
  --time-limit 20 --allow-equality
```

## Strict searches: observed failure only

No strict-mass incumbent was found in any of the following bounded runs.

| Backend and grid | Limit / reported wall time | Search statistics | Final bound |
|---|---:|---:|---:|
| HiGHS, `D=40` | 240 s / 244.13 s | 25,275 nodes; 2,339,411 LP iterations | integer dual bound 191 versus cap 194 |
| HiGHS, `D=80` | 150 s / 150.55 s | 16,315 nodes; 1,404,704 LP iterations | integer dual bound 379 versus cap 389 |
| CP-SAT, `D=40` | 180 s / 169.54 s | 3,875,412 branches; 2,127,389 conflicts | best objective bound 15 versus cap 194 |
| CP-SAT, `D=80` | 120 s / 109.29 s | 3,004,174 branches; 1,216,077 conflicts | best objective bound 14 versus cap 389 |

The strict CP-SAT statuses were `UNKNOWN`; the HiGHS statuses were time-limit
reached with no primal incumbent. Thus these runs neither prove grid
infeasibility nor give a mathematical lower bound. They are useful negative
computational evidence because the exact model includes all active-cardinality
patterns from one through four per layer and all same/consecutive-layer edge
sets satisfying its boundary-use condition. Connectivity of a hypothetical
incumbent would still need exact checking; no incumbent was produced.

Reproduction uses the strict default (omit `--allow-equality`), for example:

```text
python3 evidence/arbitrary_layered_cpsat.py --denominator 40 --time-limit 180
python3 evidence/arbitrary_layered_cpsat.py --denominator 80 --time-limit 120
```

The quickest topology-level strengthening is to introduce active layer counts
`c_i` and branch only on patterns containing a high junction
`c_i+c_(i+1)>=7`. The prior exact complete-layered theorem proves that a strict
witness with all adjacent sums at most six cannot exist, even after edge
deletions. Fixing a dihedral representative of the high-junction count pattern
before solving should remove most of the activation/topology symmetry that
defeated both generic formulations.
