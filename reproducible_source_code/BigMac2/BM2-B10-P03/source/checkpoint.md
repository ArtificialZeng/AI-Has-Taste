# Checkpoint

Job: `bigMac-00010-p03-research-e4e9195495ff` (research pass 1,
2026-09-07).

## New proved subsidiary result

- `evidence/curvature_fixed_points.md` gives exact primal and dual
  Kantorovich certificates for an arbitrary lazy transport problem on three
  metric points. Specialization yields the full inverse-weight curvature
  vector on the central triangle-inequality chamber and each of the three
  one-long-edge chambers. The formulas agree componentwise on every
  shortest-path wall.
- Solving the resulting rational equal-curvature equations classifies every
  positive normalized fixed point as
  \[
  (1/3,1/3,1/3)
  \quad\text{or a permutation of}\quad
  (r,1,1)/(r+2),\qquad r\ge 2.
  \]
  Thus there are three nonuniform fixed rays, not merely the uniform point.
- The strict-chamber initial metric `(2/3,1/6,1/6)` has curvature vector
  `(6/5,6/5,6/5)`, so its exact constant solution has that singleton omega
  set. This disproves universal convergence to the uniform metric.
- `evidence/check_curvature.py` independently exercises the derived formulas
  with exact rational arithmetic on all 13,824 triples in `{1,...,24}^3`,
  including all sampled walls and the fixed-point criterion. This is a
  reproducible finite sanity check; the symbolic argument in the Markdown
  evidence, not the finite grid, proves the theorem.

## Scope and remaining obstacle

The original problem remains unresolved: no basin/stability classification or
omega-limit theorem has yet been proved for non-fixed interior trajectories,
and no canonical boundary ODE is asserted. The exact fixed rays show that a
phase portrait must account for continua of equilibria in the long-edge
chambers. `source.md` remains unchanged (SHA-256
`bcc451f7d2acfb9cfc3045ef9e623d0ae4b467638e99a72261849a16e2910e04`).

## One next test

Have a fresh referee independently rederive the three-point primal/dual
certificate and equations (4)--(8), checking wall agreement and the strict
counterexample `(2/3,1/6,1/6)` before accepting the exact result-note scope.
