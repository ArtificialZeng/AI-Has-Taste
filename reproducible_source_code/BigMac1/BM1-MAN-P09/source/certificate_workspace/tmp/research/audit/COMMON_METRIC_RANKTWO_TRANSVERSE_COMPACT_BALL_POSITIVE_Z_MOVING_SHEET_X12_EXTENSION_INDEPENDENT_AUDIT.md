# Independent audit: moving-sheet `X12` closed cell

Date: 2026-08-24. Result: **PASS**, with scope restricted to the displayed
five-real-parameter moving sheet on `1/13<=X<=1/12`. Both exact
implementations, all six fail-closed attacks, compilation, and the direct
source manifest passed before this report was frozen.

## Audited claim

For

```text
0<S<=1/10000,
1/13<=X<=1/12,
|M|<=1/1000,
|omega|,|nu|<=1/100,
```

the original fully conjugated Hermitian gate is strictly positive on the
displayed moving sheet, for both real signs of `z` with `z^2=Z`. Both closed
`X` endpoints are included. The affine coordinate `u=156(X-1/13)` makes the
left seam exactly the frozen `X13` endpoint.

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
sigma=S/X<=13/10000.
```

Both give the identical exact remainder and strict continuum reserve

```text
Rabs = 3114379854663674139231333260314294658025270121928656740857060669879
       /1100753141760000000000000000000000000000000000000000000000,

reserve = 2213003268761410659236428591512429182973110729878071343259142939330121
          /1100753141760000000000000000000000000000000000000000000000 > 0.
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
38/169<Z<=2190346129/9009000000<1,
1-x^2-y^2-Z>=70963145293/185185000000>0,
det C=(5/9)SZ>0,
25^8*A^8*S>0.
```

The referee independently proves the sharper envelopes

```text
Z<=547575271/2252250000<1,
danger>=35482035609/92592500000>0.
```

The left base exceeds the obsolete descriptive locator `Z=1/6` by `59/1014`;
no inverse formula, gate identity, PSD/rank argument, or denominator clearing
uses that locator. Thus `lambda=A/S>0`, `Q` is Hermitian PSD of rank two, the
datum is strictly dangerous, and both signed-`z` constructions are legal
without division by `z`.

## Endpoint diagnostics

At `S=1/10000`, `M=-1/1000`, `omega=nu=-1/100`, the exact values of
`36 Gamma` are

```text
X=1/13:
905733327727313423565954040361057123569919
/1142440000000000000000000000000000000000 > 0,

X=1/12:
37195712156397840116798309327688757679
/40000000000000000000000000000000000 > 0.
```

## Fail-closed and trust boundary

Normal source and referee runs pass. Both reject optimized Python and an
intentionally corrupted dependency hash. The source rejects deletion of a
higher term at the exact `16/947` count; the referee independently rejects a
deleted quotient term at the exact 20-term gate. Both pass `py_compile` with
the cache outside the workspace.

The proof uses no CE-046/048/059/060 witness or rejected sufficient route,
no real-part monotonicity, no dropped phase, and no extrapolation from
`X<=1/13`; both implementations rebuild the present closed cell directly
from the fully conjugated original gate.

## Bound artifacts

```text
114cd2645ebd383a1a98ab35e102f517a090d7c99f9fc1b73abe2807ead5b81b  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x12_extension.md
f85f292a5a6dab1091f5f0fa344e474b8da87a47ce7deccb0dc990f26025dd55  tmp/research/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x12_extension.py
4b84c66582fe995cf88dce7534435a32183bc00bcbfd95276a6c4177635721c7  tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x12_extension_independent_referee.py
4426b250fdf0378ad81175ba7d6a7855663f22aab2b45e6b67d09bba6965d855  tmp/research/audit/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x12_extension_test_results.txt
bc28de7eb9fb5f107414eac91f03a296271b3ca42086324c0bb9981051cef302  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x13_extension.md
4ad2db93ed2a14fc6d0d54b723fb55943f15e0ad85e0a130f1c568c473e5aaa3  tmp/research/common_metric_ranktwo_transverse_full_cone_compact_ball_reduction.md
cd108d8bd3bc29addfb159d59038350d2770ba6017a77b0350b6708c43f65fe9  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x12_extension_manifest.sha256
```

No proof assistant was used. This is an exact adjacent-cell partial theorem,
not a full positive-`Z` collar, compact-ball theorem, common-metric theorem,
or fixed crossing-lens solution. No maximality at `X=1/12` is asserted.

