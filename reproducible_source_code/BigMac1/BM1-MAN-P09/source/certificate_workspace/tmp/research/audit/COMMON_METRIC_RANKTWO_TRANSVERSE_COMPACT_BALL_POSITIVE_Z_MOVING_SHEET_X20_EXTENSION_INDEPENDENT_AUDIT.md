# Independent audit: moving-sheet `X20` closed cell

Date: 2026-08-24. Result: **PASS**, with scope restricted to the displayed
five-real-parameter moving sheet on `1/21<=X<=1/20`.

## Audited conclusion

For

```text
0<S<=1/10000,
1/21<=X<=1/20,
|M|<=1/1000,
|omega|,|nu|<=1/100,
```

and the moving sheet in the theorem note, the original fully conjugated
Hermitian gate is strictly positive. The exact legality checks give

```text
lambda>0,
62/441 < Z <= 147720681/1001000000 < 3/20,
1-x^2-y^2-Z >= 261037535879/555555000000 > 0,
det C=(5/9)SZ>0.
```

Thus the datum is strictly dangerous, the compression and `Q` have rank two,
both signs of `z` are covered, and both closed `X` endpoints are included.
The seam coordinate `u=420(X-1/21)` has `u=0` exactly at the predecessor
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
sigma=S/X<=21/10000,
```

and the same strict continuum reserve

```text
10245818552627475299622517158179535681705483373323668207598839333535697
/5096079360000000000000000000000000000000000000000000000000 > 0.
```

The source and referee legality derivations are separate. The referee uses the
sharper independent upper bounds

```text
Z <= 73858839/500500000 < 3/20,
danger reserve >= 16314950159/34722187500 > 0.
```

Both 72-node exact falsification grids are legal and positive. Their common
seam and right-endpoint diagnostic values of `36 Gamma` are

```text
4188229430882337003171468410585844383897
/13720000000000000000000000000000000000,

13454196138451967922937008431058757679
/40000000000000000000000000000000000.
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
368946d9d2eb228b86fee50a36aa174fd86e667e8379f9d21516c33b4a10e986  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x20_extension.md
c914974b1f43c86a3bcc67851a64cc7fed0b83dd8fcade023af4ccb15ecd7386  tmp/research/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x20_extension.py
b61bd069a9bcc2da63d7ca3d6e103f2b07b723b0a722660b04ce952c6f82cba8  tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x20_extension_independent_referee.py
360336cf4a74cc956a02a49e8523ffd45e3bff7aee2f69c45681722ad9cf4197  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x21_extension.md
```

## Scope

This is an exact adjacent-cell partial theorem. It does not prove a full
positive-`Z` collar, arbitrary normalized scale, the compact-ball quartic on
the whole unit ball, the common-metric theorem, or the fixed-lens constant.
