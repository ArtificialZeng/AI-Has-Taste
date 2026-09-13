# Independent audit: moving-sheet `X17` closed cell

Date: 2026-08-24. Result: **PASS**, with scope restricted to the displayed
five-real-parameter moving sheet on `1/18<=X<=1/17`.  Both exact
implementations, all fail-closed tests, and a direct provisional audit
manifest passed before this final report was frozen.

## Audited claim

For

```text
0<S<=1/10000,
1/18<=X<=1/17,
|M|<=1/1000,
|omega|,|nu|<=1/100,
```

the original fully conjugated Hermitian gate is strictly positive on the
displayed five-real-parameter moving sheet, for both real signs of `z` with
`z^2=Z`.  Both closed `X` endpoints are included.  The affine coordinate
`u=306(X-1/18)` makes the left seam exactly the frozen `X18` endpoint.

## Independent reconstruction

The source starts from the original transverse frame, reconstructs all
entries of `Q,Q^2`, checks Hermitian symmetry and the literal conjugated
gate, and separately obtains the same scalar by a Gram-vector ordering.  Its
moving-sheet quotient is built by a sparse exact substitution.

The referee imports neither source code, discovery code, cached quartic, nor
coefficient table.  It uses signed-`z` Gram columns, a different Gram-vector
component order, and direct affine-power substitution.  The source checks
the 134-term pre-map; both independently recover

```text
20 quotient (S,X) terms of bidegree (5,4),
16 higher terms,
947 centered (M,omega,nu) monomials,
sigma=S/X<=9/5000.
```

They give the identical strict continuum reserve

```text
56825922845924911137909427477635861991459577165298164167361883470142517
/28264468561920000000000000000000000000000000000000000000000 > 0.
```

The 72 exact seam/interior/endpoint falsification nodes are diagnostics only;
the displayed continuum reserve proves the result.

## Legality and the `Z=1/6` dependency audit

This cell crosses the predecessor's locator `Z=1/6`: at `X=1/17` the
`S -> 0+` base exceeds it by exactly `11/1734`.  Therefore the old `Z<1/6`
assertion was not silently removed.  The following files were searched and
their defining algebra was reconstructed:

```text
tmp/research/common_metric_ranktwo_transverse_full_cone_compact_ball_reduction.md
tmp/research/verify_common_metric_ranktwo_transverse_full_cone_compact_ball_reduction.py
audit/verify_common_metric_ranktwo_transverse_full_cone_compact_ball_reduction_referee.py
tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x19_extension.md
tmp/research/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x19_extension.py
tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x18_extension.md
tmp/research/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x18_extension.py
```

The lossless reduction's actual nonplanar hypotheses are exactly

```text
0<S=h^2<=1, lambda>0, Z=z^2>0, x^2+y^2+Z<1.
```

No inverse formula, PSD/rank argument, gate identity, denominator clearing,
or later moving-sheet bridge requires `Z<1/6`.  The only `Z<1/6` occurrences
in the predecessor `X19`/`X18` source artifacts are reported local endpoint
bounds.  The new source proves

```text
A>=999/1000>0,
53/324<Z<=50071149309/289289000000<1,
1-x^2-y^2-Z>=4220971659943/9444435000000>0,
det C=(5/9)SZ>0,
25^8*A^8*S>0.
```

The referee independently sharpens the last two envelopes to

```text
Z<=50070128289/289289000000<1,
danger>=4221004993243/9444435000000>0.
```

Thus `lambda=A/S>0`, the frame is real since `S<1`, every quotient divisor is
positive, `Q` is Hermitian PSD of rank two, and the point lies in the strict
open unit ball.  Both signed-`z` constructions are explicit; neither divides
by `z`.

## Endpoint diagnostics

At `S=1/10000`, `M=-1/1000`, `omega=nu=-1/100`, the exact values of
`36 Gamma` are

```text
X=1/18:
16590441965844177687836029861184257679
/40000000000000000000000000000000000 > 0,

X=1/17:
1552541492892247573695625585542882277607759
/3340840000000000000000000000000000000000 > 0.
```

## Fail-closed and trust boundary

Normal source and referee runs pass.  Both reject optimized Python and an
intentionally corrupted dependency hash.  The source rejects deletion of a
higher term at the exact `16/947` count; the referee independently rejects a
deleted quotient term at the exact 20-term gate.  Both pass `py_compile`.

## Bound artifacts

```text
e9ed0d778a4754a3b7144754b0277cf67c282bae6879676b4d24a34239cf12fc  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x17_extension.md
9273ffe9cc6fee174d151f1581d3cf971f8c16d782bdcf076c219bb89d23ccf3  tmp/research/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x17_extension.py
7213b61c7f8e10a25954db1c17bc5f583e1aa506143214e0e3620af9c5024b30  tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x17_extension_independent_referee.py
77ffad8e785bc1ba27dd3cbf067608c95e97cec351ac040b70d3ee6d47c7879f  tmp/research/audit/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x17_extension_test_results.txt
e6145a183c099e002bcee5c39ac03f098058dd56347532941bf8c0ddcf9a9d4d  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x18_extension.md
4ad2db93ed2a14fc6d0d54b723fb55943f15e0ad85e0a130f1c568c473e5aaa3  tmp/research/common_metric_ranktwo_transverse_full_cone_compact_ball_reduction.md
322d75bee07e6844b0fb4780aea6cafef69a273d472cbd199a7c861e5cb78c2b  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x17_extension_manifest.sha256
```

No proof assistant was used.  This is an exact adjacent-cell partial theorem,
not a full positive-`Z` collar, compact-ball theorem, common-metric theorem,
or fixed crossing-lens solution.  No maximality at `X=1/17` is asserted.
