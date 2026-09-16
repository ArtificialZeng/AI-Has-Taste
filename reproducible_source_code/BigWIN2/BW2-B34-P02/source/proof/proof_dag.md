# Proof dependency graph

Status: no resolution proof DAG exists. This graph records verified reductions,
proved partial leaves, and the fatal missing implication.

```text
T  Original LTC-CDS for every finite Young shape
|
+-- E1 [verified equivalence]
|     proper colorings of R_lambda
|       <-> edge-colorings of Ferrers B_lambda
|       <-> a partition of E(B_lambda) into matchings of sizes delta_k
|
+-- E2 [verified/published, independently evaluated]
|     rho_k = minimum Ferrers corner capacity (formula (1))
|     delta_k = rho_k - rho_{k-1}
|
+-- K4 [published]
|     L1, L2, L3, L4 hold for every partition graph
|     |
|     `-- K5 [OPEN: first strict prefix frontier]
|           every partition graph has a coloring whose five largest
|           class sizes are delta_1,...,delta_5
|
+-- F [proved in this pass, insufficient for T]
|     rectangles; hooks; at most two rows/columns; staircases
|
+-- BA [owner-context candidate equivalence; fresh audit pending]
|     CDS-coloring
|       <-> integer Ferrers row-block/column-block/color quotas
|     via colored detachment
|     |
|     +-- BA2 [owner-context candidate partial theorem]
|     |     the quota system is feasible for every shape with at most
|     |     two distinct row lengths
|     |
|     `-- BA3 [OPEN restricted frontier]
|           the quota system is feasible for every shape with at most
|           three distinct row lengths
|
+-- X [FATAL OPEN EDGE]
      prove integer feasibility of BA for every Ferrers block system,
      or find an exact infeasible BA system / Young-shape counterexample
```

Failed incoming edges to `X`:

- `arbitrary maximum matching -> extend recursively` is false at
  \(\lambda=(5,4,3,3)\); see `data/route-obstructions.json`.
- row-major First Fit, one fixed cyclic coloring, and even arbitrary distinct
  cyclic row shifts are not universal; see the same exact obstruction file.

The candidate proof of BA and BA2 is in `proof/two_level_candidate.md` and has
not passed a fresh mathematical audit.  Even if BA2 is accepted, it is a
strict restricted subproblem and does not replace the fatal general edge `X`.
Candidate C002 is the next three-row-length restriction and likewise does not
imply `T`.
