# Independent audit: moving-sheet `X19` closed cell

Date: 2026-08-24. Result: **PASS**, with scope restricted to the displayed
five-real-parameter moving sheet on `1/20<=X<=1/19`.

## Audited conclusion

For

```text
0<S<=1/10000,
1/20<=X<=1/19,
|M|<=1/1000,
|omega|,|nu|<=1/100,
```

and the moving sheet in the theorem note, the original fully conjugated
Hermitian gate is strictly positive. The exact legality checks give

```text
lambda>0,
59/400 < Z <= 56082418341/361361000000 < 1/6,
1-x^2-y^2-Z >= 4887491031701/10555545000000 > 0,
det C=(5/9)SZ>0.
```

Thus the datum is strictly dangerous, the compression and `Q` have rank two,
both signs of `z` are covered, and both closed `X` endpoints are included.
The seam coordinate `u=380(X-1/20)` has `u=0` exactly at the predecessor
endpoint, so no continuity argument is used at the stitch.

## Reconstruction and certificate

The source verifier begins with the transverse frame and compression,
rebuilds all entries of `Q` and `Q^2`, evaluates the literal conjugated gate,
and independently builds a three-component Gram-vector gate. It verifies
their identity before applying the moving sheet. Its quotient construction is
a sparse exact substitution from the freshly reconstructed quartic.

The referee imports neither source code, discovery code, cached quartics, nor
coefficient tables. It independently reconstructs signed-`z` Gram columns,
uses a different Gram-vector component ordering, and forms the moving
quotient by direct affine-power substitution. Both routes obtain exactly

```text
20 quotient (S,X) terms,
16 higher terms,
947 centered (M,omega,nu) monomials,
sigma=S/X<=1/500,
```

and the same strict continuum reserve

```text
26756976522448207008651434175031131058236664369690137089162898293759
/13308465593548800000000000000000000000000000000000000000 > 0.
```

The source and referee legality derivations are separate. The referee uses the
sharper independent upper bounds

```text
Z <= 56081277201/361361000000 < 1/6,
danger reserve >= 4887524365001/10555545000000 > 0.
```

Both 72-node exact falsification grids are legal and positive. Their common
seam and right-endpoint diagnostic values of `36 Gamma` are

```text
13454196138451967922937008431058757679
/40000000000000000000000000000000000,

1941635149051525232795626443278240808984959
/5212840000000000000000000000000000000000.
```

The continuum theorem is proved by the rational reserve, not by this grid.

## Fail-closed results

Normal source and referee runs pass. Both programs reject optimized Python
and an intentionally bad dependency hash. The source and referee also reject
an intentionally deleted quotient term after independently reconstructing
the original/Gram gate: the source fails at the exact higher-term/monomial
count and the referee fails at the complete 20-term gate.

## Bound artifacts

```text
cac9bdfdc7fddebfc31ff110bd77d5cfa79360e8fbc7a0ec3c9f04f90e5a9142  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x19_extension.md
1287290731cb2b5dd24789116f4f1dadc23dd213d45c90ae302f65101326fc34  tmp/research/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x19_extension.py
35e9d90c6ac1fcb8ba2d304e60ddd98d5a56f2e8347a174cfed9af009ba2a01c  tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x19_extension_independent_referee.py
368946d9d2eb228b86fee50a36aa174fd86e667e8379f9d21516c33b4a10e986  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x20_extension.md
```

## Scope

This is an exact adjacent-cell partial theorem. It does not prove a full
positive-`Z` collar, arbitrary normalized scale, the compact-ball quartic on
the whole unit ball, the common-metric theorem, or the fixed-lens constant.
