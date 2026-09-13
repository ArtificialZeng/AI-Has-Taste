# Constant-Z chart on `99/100 <= X <= 497/500`

## Status and scope

This is a frozen **source candidate** pending an independent no-import
referee.  It extends the independently audited constant-Z chart by one
adjacent strict rational cell:

```text
Xanchor = 83059/100000,
Xstar   = 1019767/1040000,
Z_constant = Z_old + 2 (Xstar-Xanchor),
99/100 <= X <= 497/500.
```

The parameter box is

```text
0 < S <= 1/10000,
|M| <= 1/1000,
|omega|, |nu| <= 1/100.
```

This is one local compact-ball cell.  It is not the full compact-ball
theorem, the general complex common-metric gate, an arbitrary-node or
arbitrary-dimensional result, or the optimal fixed crossing-lens constant.
No endpoint maximality is asserted.

## Original definition and three-layer seam

The executable binds the audited `X<=99/100` predecessor and the frozen
`X=1` chart-obstruction preflight.  It independently reconstructs the signed
frame, Hermitian `Q`, all entries of `Q^2`, and the fully conjugated raw gate
from the original definitions.  Signed-frame variables cancel; the raw gate
has exact degree four in `Z`.

At `X=99/100`, the predecessor and new cell use the identical constant chart.
The source checks equality of the parameters, the positively cleared raw
gate, and the core after removal of the common nonnegative first layer.  The
complete cleared/core structure is `32/32/1581`, with bidegree `(7,4)`.

## Full-cell legality before positivity

The exact legality block executes before the continuous positivity
certificate.  On the complete parameter box it proves

```text
Z >= 17798406223702873/15857127000000000000 > 0,
Z <= 31507/2600000 < 1,
-5477801/2750000 <= dZ/dX <= -99/50 < 0,
T <= -5332081/178750 < 0,
danger >= 9833/2600000 > 0,
det(C) >= [17798406223702873/28542828600000000000] S > 0.
```

Therefore both signed square roots of `Z` are legal and `C` has strict rank
two on the whole cell.

The exact worst-corner polynomial for this constant chart has its positive
root strictly isolated by

```text
497/500 < root < 199/200.
```

The right endpoint `497/500` was selected as a natural strict rational point
below that root.  The algebraic chart root is not included, and neither this
choice nor the root is a maximality statement for other charts.

## Exact continuous positivity certificate

All 40 centered rational Bernstein lower controls are strictly positive.
The final source bytes assert that the weakest index is uniquely `(7,0)`,
with exact reserve

```text
237983128275106868164816372024450404725835762778737426332055936856452553581744586321
--------------------------------------------------------------------------------------.
719207337600221184000000000000000000000000000000000000000000000000000000
```

The complete weakest polynomial is printed in the frozen normal log.  All 72
exact original-gate nodes are legal and positive, but are diagnostics only;
the 40 exact Bernstein controls provide the continuous certificate.

## Chart-obstruction provenance

The separate frozen endpoint preflight rebuilds the same original gate and
shows that this constant chart is illegal at `X=1` because `Z<0`.  That result
is not a raw-gate counterexample and receives no counterexample number.

## Replay and next gate

```bash
.venv/bin/python -B -u \
  tmp/research/compact_ball_inward_z_constant_lift_x497_500_exact_gate.py
```

An independent referee must not import or execute this source.  It must
rebuild the original definitions, audited predecessor bindings, three seam
layers, full legality, all 40 controls, the unique weakest polynomial and
reserve, the 72 diagnostic nodes, the fail-closed attacks, and the frozen
manifest before this candidate can be promoted to a local theorem.
