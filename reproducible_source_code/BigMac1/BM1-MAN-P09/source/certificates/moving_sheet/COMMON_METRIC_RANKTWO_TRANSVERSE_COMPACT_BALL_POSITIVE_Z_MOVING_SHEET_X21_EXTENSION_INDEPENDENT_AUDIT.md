# Independent audit: moving-sheet `X21` closed cell

Date: 2026-08-24.  Result: **PASS**, with scope restricted to the displayed
five-real-parameter moving sheet on `1/22<=X<=1/21`.

## Audited conclusion

For

```text
0<S<=1/10000,
1/22<=X<=1/21,
|M|<=1/1000,
|omega|,|nu|<=1/100,
```

and the exact map in the theorem note, the original fully conjugated
Hermitian gate is strictly positive.  Exact legality gives

```text
lambda>0,
65/484 < Z <= 8870610403/63063000000 < 1/7,
1-x^2-y^2-Z >= 12594127899/26455000000 > 0,
det C=(5/9)SZ>0.
```

Thus both signs of `z`, strict danger, PSD rank two, and both closed `X`
endpoints are covered.  The seam coordinate `u=462(X-1/22)` has `u=0`
exactly at the independently audited predecessor endpoint; no continuity
argument or division by a cap coordinate is used.

## Independent reconstruction

The source verifier rebuilds the original `Q,Q^2` gate and an independent
three-component Gram-vector gate before forming a sparse moving quotient.
The referee imports no source/discovery code or cached polynomial.  It starts
from signed-`z` Gram columns, rebuilds the literal Hermitian gate and a
differently ordered Gram vector, and forms the moving quotient by direct
affine-power substitution.

Both routes obtain exactly:

```text
20 quotient (S,X) terms,
16 higher terms,
947 centered (M,omega,nu) monomials,
sigma=S/X<=11/5000,
```

with strict continuum reserve

```text
52950226750059588134240296073793083514499729090257777677521600042121
/26336378880000000000000000000000000000000000000000000000 > 0.
```

Both exact 72-node falsification grids are legal and positive.  The seam and
right-endpoint diagnostic values of `36 Gamma` are respectively

```text
14817150110247071841775080222180418970749
/53240000000000000000000000000000000000,

4188229430882337003171468410585844383897
/13720000000000000000000000000000000000.
```

## Fail-closed tests

Normal source and referee runs pass.  Both programs reject optimized Python,
an intentionally bad dependency hash, and an intentionally deleted quotient
term.  The deleted-term tests fail after the gate reconstruction at the exact
term-count/monomial gate, as intended.

## Bound artifacts

```text
360336cf4a74cc956a02a49e8523ffd45e3bff7aee2f69c45681722ad9cf4197  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x21_extension.md
4bb3fa86601d845c682884dc1fe934e493f2588143897497ac37f1e5d7dfbe6e  tmp/research/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x21_extension.py
415d90562062eab38f7f3041576aafba8ded8456a716fc9dc6e7310cd11424e4  tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x21_extension_independent_referee.py
5189571fc3913b3ff41dde268d2ce47cd89b18568748d76378007a1e0667d06d  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x22_extension.md
```

## Scope

This is a new exact adjacent-cell partial theorem.  It is not a full
positive-`Z` collar, does not allow arbitrary normalized scale, and does not
prove the compact ball, common-metric theorem, or fixed-lens constant.

