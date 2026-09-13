# Independent audit: moving-sheet `X6` closed cell

Date: 2026-08-24. Result: **PASS**, with scope restricted to the displayed
five-real-parameter moving sheet on `1/7<=X<=1/6`. Both exact
implementations, all six fail-closed attacks, compilation, and the direct
source manifest passed before this report was frozen.

## Audited claim

For

```text
0<S<=1/10000,
1/7<=X<=1/6,
|M|<=1/1000,
|omega|,|nu|<=1/100,
```

the original fully conjugated Hermitian gate is strictly positive on the
displayed moving sheet, for both real signs of `z` with `z^2=Z`. Both closed
`X` endpoints are included. The affine coordinate `u=42(X-1/7)` makes the
left seam exactly the frozen `X7` endpoint.

## Independent reconstruction

The source reconstructs the transverse frame, every entry of `Q,Q^2`, the
literal conjugated gate, and a separately ordered Gram-vector gate. Its
moving-sheet quotient uses a sparse exact substitution.

The referee imports neither source/discovery code, cached quartic, nor
coefficient table. It uses signed-`z` Gram columns, a different Gram-vector
component order, and direct affine-power substitution. The source checks the
134-term pre-map; both independently recover

```text
20 quotient (S,X) terms of bidegree (5,4),
16 higher terms,
947 centered (M,omega,nu) monomials,
sigma=S/X<=7/10000.
```

Both give the identical exact remainder and strict continuum reserve

```text
Rabs = 1257251838194657873607145216508101502726407271274850581262698563263
       /412782428160000000000000000000000000000000000000000000000,

reserve = 829786866392833217142265326573270702608949592728725149418737301436737
          /412782428160000000000000000000000000000000000000000000000 > 0.
```

The 72 exact seam/interior/endpoint nodes are falsification diagnostics only;
the displayed continuum reserve proves the result.

## Legality and signed-`z` audit

The compact-ball chart prerequisites are exactly

```text
0<S=h^2<=1, lambda>0, Z=z^2>0, x^2+y^2+Z<1.
```

The source proves

```text
A>=999/1000>0,
20/49<Z<=4254908629/9009000000<1,
1-x^2-y^2-Z>=92519185879/555555000000>0,
det C=(5/9)SZ>0,
25^8*A^8*S>0.
```

The referee independently proves the sharper envelopes

```text
Z<=4254818539/9009000000<1,
danger>=92524741429/555555000000>0.
```

The left base exceeds the obsolete descriptive locator `Z=1/6` by `71/294`;
no inverse formula, gate identity, PSD/rank argument, or denominator clearing
uses that locator. Thus `lambda=A/S>0`, `Q` is Hermitian PSD of rank two, the
datum is strictly dangerous, and both signed-`z` constructions are legal
without division by `z`.

## Endpoint diagnostics

At `S=1/10000`, `M=-1/1000`, `omega=nu=-1/100`, the exact values of
`36 Gamma` are

```text
X=1/7:
37381778605583832954528361124091276383897
/13720000000000000000000000000000000000 > 0,

X=1/6:
148251911904404449931845373885972257679
/40000000000000000000000000000000000 > 0.
```

At the same endpoint node,

```text
Z      = 52371001995545111/110889000000000000 > 0,
danger = 92434871/555000000 > 0,
det C  = 52371001995545111/1996002000000000000000 > 0.
```

Together with the global strict continuum reserve, these exact values show
that `X=1/6` is not a chart, legality, rank, or certificate boundary.

## Fail-closed and trust boundary

Normal source and referee runs pass. Both reject optimized Python and an
intentionally corrupted dependency hash. The source rejects deletion of a
higher term at the exact `16/947` count; the referee independently rejects a
deleted quotient term at the exact 20-term gate. Both pass `py_compile` with
the cache outside the workspace.

The proof uses no CE-046/048/059/060 witness or rejected sufficient route,
no real-part monotonicity, no dropped phase, and no extrapolation from
`X<=1/7`; both implementations rebuild the present closed cell directly
from the fully conjugated original gate.

## Bound artifacts

```text
db209c6987f806e90a5e521bee887a82b0394a8bb7090107ef1a4143e8ae0bfa  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x6_extension.md
997d20985aa98a09518a75eaf385bab41b5f0911953fda6ebc356f6088eb264d  tmp/research/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x6_extension.py
2f184c99b44cd0d85ca01a250f0d9e0514354c93d289d27a5ab0bcd747846110  tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x6_extension_independent_referee.py
7b763a4ebd0ec7f04d5a46d2c70582fd99a13086911c49e69a57e4f101d5778b  tmp/research/audit/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x6_extension_test_results.txt
76622dab1b117189e333db6b382b0c745a6586ea20ad9f6a85f0c43c788576c0  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x7_extension.md
4ad2db93ed2a14fc6d0d54b723fb55943f15e0ad85e0a130f1c568c473e5aaa3  tmp/research/common_metric_ranktwo_transverse_full_cone_compact_ball_reduction.md
558167986e94cfd52e55bfaa22c3c15aac124cba27a4ee8b5aaae91c831043c5  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x6_extension_manifest.sha256
```

No proof assistant was used. This is an exact adjacent-cell partial theorem,
not a full positive-`Z` collar, compact-ball theorem, common-metric theorem,
or fixed crossing-lens solution. No maximality at `X=1/6` is asserted.






