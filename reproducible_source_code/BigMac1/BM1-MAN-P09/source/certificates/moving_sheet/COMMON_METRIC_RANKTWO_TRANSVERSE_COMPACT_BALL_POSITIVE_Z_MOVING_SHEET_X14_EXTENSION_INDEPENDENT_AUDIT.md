# Independent audit: moving-sheet `X14` closed cell

Date: 2026-08-24. Result: **PASS**, with scope restricted to the displayed
five-real-parameter moving sheet on `1/15<=X<=1/14`. Both exact
implementations, all six fail-closed attacks, compilation, and the direct
source manifest passed before this report was frozen.

## Audited claim

For

```text
0<S<=1/10000,
1/15<=X<=1/14,
|M|<=1/1000,
|omega|,|nu|<=1/100,
```

the original fully conjugated Hermitian gate is strictly positive on the
displayed moving sheet, for both real signs of `z` with `z^2=Z`. Both closed
`X` endpoints are included. The affine coordinate `u=210(X-1/15)` makes the
left seam exactly the frozen `X15` endpoint.

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
sigma=S/X<=3/2000.
```

Both give the identical exact remainder and strict continuum reserve

```text
Rabs = 223636329643104495729779188582847296089497629319248238107413247
       /79906524364800000000000000000000000000000000000000000,

reserve = 53550029757865949037427029808183214063735927456893583920630862251
          /26635508121600000000000000000000000000000000000000000 > 0.
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
44/225<Z<=1466262267/7007000000<1,
1-x^2-y^2-Z>=230085185879/555555000000>0,
det C=(5/9)SZ>0,
25^8*A^8*S>0.
```

The referee independently proves the sharper envelopes

```text
Z<=1466232237/7007000000<1,
danger>=230087566829/555555000000>0.
```

The left base exceeds the obsolete descriptive locator `Z=1/6` by `13/450`;
no inverse formula, gate identity, PSD/rank argument, or denominator clearing
uses that locator. Thus `lambda=A/S>0`, `Q` is Hermitian PSD of rank two, the
datum is strictly dangerous, and both signed-`z` constructions are legal
without division by `z`.

## Endpoint diagnostics

At `S=1/10000`, `M=-1/1000`, `omega=nu=-1/100`, the exact values of
`36 Gamma` are

```text
X=1/15:
23847741893133467314954498194610657679
/40000000000000000000000000000000000 > 0,

X=1/14:
9384471705669180411212404704709692383897
/13720000000000000000000000000000000000 > 0.
```

## Fail-closed and trust boundary

Normal source and referee runs pass. Both reject optimized Python and an
intentionally corrupted dependency hash. The source rejects deletion of a
higher term at the exact `16/947` count; the referee independently rejects a
deleted quotient term at the exact 20-term gate. Both pass `py_compile` with
the cache outside the workspace.

For the v11 portable package, both programs accept exactly their canonical
`certificate_workspace` layout and their grouped `certificates/moving_sheet`
layout. Each derives the release-local `certificate_workspace` from
`__file__`, confines every resolved dependency to it before hashing, and
rejects an unknown layout. This packaging adaptation changes neither the
exact gate nor any theorem value above.

## Bound artifacts

```text
676435f4c4626a827e86a1d63161a459155e26e5f69773ae7e07b412ce0d5384  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x14_extension.md
da695b3f2620861e82a14d1e4d037e3dbf7fb7d1170389ac0950fc86f59c3b73  tmp/research/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x14_extension.py
e7d785924e4b6e3039dcdff731a834ccd81346302b6dea017c93df843b5881d1  tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x14_extension_independent_referee.py
83134e5046f4680c37f3d65d3d76b9e4a5c942c98d778c6e18a53d9dbfeef73b  tmp/research/audit/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x14_extension_test_results.txt
3bf5600929c88308f9bb3cb6ce4bfbfe3b1fa9dc4632cdf49ef4ca0d3954adfb  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x15_extension.md
4ad2db93ed2a14fc6d0d54b723fb55943f15e0ad85e0a130f1c568c473e5aaa3  tmp/research/common_metric_ranktwo_transverse_full_cone_compact_ball_reduction.md
8da486a36d0be8aa2ce9b59d7996b4b00d163c0cd72afcba85fa06c0ae347bf5  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x14_extension_manifest.sha256
```

No proof assistant was used. This is an exact adjacent-cell partial theorem,
not a full positive-`Z` collar, compact-ball theorem, common-metric theorem,
or fixed crossing-lens solution. No maximality at `X=1/14` is asserted.
