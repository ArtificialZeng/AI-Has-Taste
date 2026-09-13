# Seam-preserving constant inward-Z chart on `Xstar <= X <= 99/100`

## Status and scope

This is a frozen **source candidate** pending an independent no-import
referee.  Let

```text
Xanchor = 83059/100000,
Xstar   = 1019767/1040000.
```

The independently audited recentered chart ends at `Xstar`.  The new chart is

```text
Z_constant = Z_recentered - 2 (X-Xstar)
           = Z_old + 2 (Xstar-Xanchor),
Xstar <= X <= 99/100.
```

Thus its perturbation vanishes exactly at the seam.  This is one local cell,
not a full compact-ball, general common-metric, arbitrary-node/dimension, or
fixed crossing-lens result.

## Original definition and three-layer seam

The source hash-binds the independently audited danger-root predecessor and
its source/referee manifests.  It reconstructs the signed frame, Hermitian
`Q`, all `9/9` entries of `Q^2`, and the fully conjugated raw gate from their
original definitions.  The gate is real after the signed-frame relations and
has exact degree four in `Z`.

At `X=Xstar`, the old and new chart parameters agree.  Multiplication by the
positive clearing factor preserves equality of the raw gates, and removal of
the same displayed nonnegative first layer preserves equality of the cores.
The source checks all three seam layers exactly before legality or controls.

The constant lift removes two `(S,X)` coefficients relative to the previous
chart: the cleared/core structure is `32/32/1581`, with bidegree `(7,4)`.

## Full-cell legality before positivity

The source orders this gate before the Bernstein calculation.  Exact bounds
on the complete parameter box are

```text
Z >= 143889690210214873/15857127000000000000,
Z <= 33258337711/1081600000000,
dZ/dX <= -1019767/520000 < 0,
dZ/dX >= -5455801/2750000,
T <= -8425123367/286000000,
danger >= (8425123367/286000000) S > 0,
det(C) >= [143889690210214873/28542828600000000000] S > 0.
```

The `S=0` danger base is zero at the seam and increases to
`9833/2600000` at the right endpoint.  Since the actual box has `S>0`, the
negative `T` bound supplies strict danger at the seam.  Both signed square
roots of `Z` are legal and `C` has strict rank two throughout the cell.

## Exact continuous positivity certificate

All 40 centered rational Bernstein lower controls are strictly positive.
The final source bytes assert that the weakest index is uniquely `(7,0)`,
with reserve

```text
336916849934297843831968152548875021542760484743285035401593929563252614799020866001627
------------------------------------------------------------------------------------------------.
1047953682726912000000000000000000000000000000000000000000000000000000000000
```

The complete weakest polynomial appears in the normal log.  All 72 exact
original-gate nodes are legal and positive, but they are diagnostics only;
the exact Bernstein tensor proves positivity on the continuum.

## Replay and referee gate

```sh
.venv/bin/python -B -u tmp/research/compact_ball_inward_z_constant_lift_x99_100_exact_gate.py
```

An independent referee must not import or execute the source.  It must
rebuild the definitions, predecessor binding, three seam layers, legality,
40 controls, unique weakest polynomial/reserve, diagnostics, attacks, and
frozen manifest before this candidate can be promoted to a local theorem.
