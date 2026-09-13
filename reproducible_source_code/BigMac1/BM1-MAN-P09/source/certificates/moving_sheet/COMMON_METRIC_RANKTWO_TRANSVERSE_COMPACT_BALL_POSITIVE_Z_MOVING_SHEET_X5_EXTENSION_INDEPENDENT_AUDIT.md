# Independent audit: moving-sheet `X5` closed cell

Date: 2026-08-24. Result: **PASS**, with scope restricted to the displayed
five-real-parameter moving sheet on `1/6<=X<=1/5`. Both exact
implementations, all six fail-closed attacks, compilation, and the direct
source manifest passed before this report was frozen.

## Audited claim

For

```text
0<S<=1/10000,
1/6<=X<=1/5,
|M|<=1/1000,
|omega|,|nu|<=1/100,
```

the original fully conjugated Hermitian gate is strictly positive on the
displayed moving sheet, for both real signs of `z` with `z^2=Z`. Both closed
`X` endpoints are included. The affine coordinate `u=30(X-1/6)` makes the
left seam exactly the frozen `X6` endpoint.

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
sigma=S/X<=3/5000.
```

Both give the identical exact remainder and strict continuum reserve

```text
Rabs = 7795462879860907557152273097131526107765177332422578726811766729
       /2488320000000000000000000000000000000000000000000000000,

reserve = 1667291474739610477717961507182038181400927232555859140424396077757
          /829440000000000000000000000000000000000000000000000000 > 0.
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
17/36<Z<=560633181/1001000000<1,
1-x^2-y^2-Z>=44371085879/555555000000>0,
det C=(5/9)SZ>0,
25^8*A^8*S>0.
```

The referee independently proves the sharper envelopes

```text
Z<=560621169/1001000000<1,
danger>=44377752539/555555000000>0.
```

The left base exceeds the obsolete descriptive locator `Z=1/6` by `11/36`;
no inverse formula, gate identity, PSD/rank argument, or denominator clearing
uses that locator. Thus `lambda=A/S>0`, `Q` is Hermitian PSD of rank two, the
datum is strictly dangerous, and both signed-`z` constructions are legal
without division by `z`.

## Endpoint diagnostics

At `S=1/10000`, `M=-1/1000`, `omega=nu=-1/100`, the exact values of
`36 Gamma` are

```text
X=1/6:
148251911904404449931845373885972257679
/40000000000000000000000000000000000 > 0,

X=1/5:
213355344357890421512795094325969057679
/40000000000000000000000000000000000 > 0.
```

At the same endpoint node,

```text
Z      = 62104370217545111/110889000000000000 > 0,
danger = 44335981/555000000 > 0,
det C  = 62104370217545111/1996002000000000000000 > 0.
```

Together with the global strict continuum reserve, these exact values show
that `X=1/5` is not a chart, legality, rank, or certificate boundary.

## Fail-closed and trust boundary

Normal source and referee runs pass. Both reject optimized Python and an
intentionally corrupted dependency hash. The source rejects deletion of a
higher term at the exact `16/947` count; the referee independently rejects a
deleted quotient term at the exact 20-term gate. Both pass `py_compile` with
the cache outside the workspace.

The proof uses no CE-046/048/059/060 witness or rejected sufficient route,
no real-part monotonicity, no dropped phase, and no extrapolation from
`X<=1/6`; both implementations rebuild the present closed cell directly
from the fully conjugated original gate.

## Bound artifacts

```text
a86dbe3eea4d9bfaf2772383407e65a5960e6941344713377068ff048ffc5f4d  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x5_extension.md
60d7d2bc3c79d9261bd0d85917c488950a55aa9d941cea2e3101a475a594cad4  tmp/research/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x5_extension.py
a4738635fd660ec5bf2003a9b56f2a680ce327059d87f89d2c903ff2da923cf7  tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x5_extension_independent_referee.py
482b2db1de02e82b66c4b37eebf94700b6ac48969c6af245b9be5dd18306fe7f  tmp/research/audit/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x5_extension_test_results.txt
8c7abd4fae23fa44f34d7ddf729a9982f03180746c35f5e126d9f7fe2194471e  tmp/research/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x5_extension_source_freeze_manifest.sha256
db209c6987f806e90a5e521bee887a82b0394a8bb7090107ef1a4143e8ae0bfa  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x6_extension.md
4ad2db93ed2a14fc6d0d54b723fb55943f15e0ad85e0a130f1c568c473e5aaa3  tmp/research/common_metric_ranktwo_transverse_full_cone_compact_ball_reduction.md
10075e983b5ed6370ed9f505e7758f3ebe8c536bf98c002b1d869748d76d9359  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x5_extension_manifest.sha256
```

No proof assistant was used. This is an exact adjacent-cell partial theorem,
not a full positive-`Z` collar, compact-ball theorem, common-metric theorem,
or fixed crossing-lens solution. No maximality at `X=1/5` is asserted.






