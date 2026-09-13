# Constant-Z endpoint preflight at `X=1`

## Status

Exact definition-level chart-obstruction preflight.  This is not a raw-gate
counterexample, not a Bernstein-certificate failure, and not a maximality
claim for any chart or for the compact-ball theorem.

## Frozen predecessor

The preflight binds the independently audited constant-lift source on
`Xstar <= X <= 99/100`, where

```text
Xstar = 1019767/1040000,
Z_const = Z_old + 2*(Xstar - 83059/100000).
```

The bound source and independent referee hashes are checked by the executable
before any algebra is reconstructed.

## Exact reconstruction and seam

Starting from the original fully conjugated Hermitian `Q,Q^2` definition, the
preflight reconstructs the degree-four raw gate, the positive clearing, and
the complete `32/32/1581`, bidegree `(7,4)` core.  At `X=99/100` it checks the
parameter, cleared raw-gate, and cleared-core seam with the audited predecessor.

## Exact chart obstruction

On the full parameter box, `Z_const` is strictly decreasing in `X`.  At its
worst centered corner

```text
S=1/10000, M=-1/1000, omega=-1/100, nu=1/100,
```

the exact function is

```text
Z_worst(X) =
  (-15857127000000000000 X^2
   -62281028628000000 X
   +15747118081251934873)
  /15857127000000000000.
```

The endpoint signs are

```text
Z_const(1,S=0) = -20233/2600000 < 0,
Z_worst(1) = -172289947376065127/15857127000000000000 < 0.
```

Thus `99/100 <= X <= 1` is not a legal cell for this chart.  The remaining
checks distinguish the failure correctly:

```text
Z_upper = 31507/2600000 < 1,
dZ/dX in [-5510801/2750000,-99/50] < 0,
T_max = -5332081/178750 < 0,
danger_base in [9833/2600000,20233/2600000] > 0,
detC/S = (5/9) Z_worst(1)
       = -172289947376065127/28542828600000000000 < 0.
```

Consequently danger remains strict, while negative `Z` destroys real
both-sign/rank-two chart legality before any raw-gate sign question is posed.
The preflight intentionally does not run the 40 controls.

The positive root of the displayed exact quadratic is isolated by

```text
497/500 < root < 199/200,
Z_worst(497/500)
  = 17798406223702873/15857127000000000000 > 0,
Z_worst(199/200)
  = -13803700407925127/15857127000000000000 < 0.
```

Because strict `Z>0` is needed for the strict rank-two cell, the algebraic
root itself is not used as a closed strict endpoint.  The next source test is
the natural strict rational cell `99/100 <= X <= 497/500`.  This rational
choice is not claimed to be a largest rational endpoint.

## Replay

```bash
.venv/bin/python -B -u \
  tmp/research/compact_ball_inward_z_constant_lift_x1_endpoint_preflight.py
```

The frozen log has exit code `0`; that code means that the exact obstruction
classification was successfully verified, not that the cell passed legality.
