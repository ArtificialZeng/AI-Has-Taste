# Independent audit: moving-sheet `X13` closed cell

Date: 2026-08-24. Result: **PASS**, with scope restricted to the displayed
five-real-parameter moving sheet on `1/14<=X<=1/13`. Both exact
implementations, all six fail-closed attacks, compilation, and the direct
source manifest passed before this report was frozen.

## Audited claim

For

```text
0<S<=1/10000,
1/14<=X<=1/13,
|M|<=1/1000,
|omega|,|nu|<=1/100,
```

the original fully conjugated Hermitian gate is strictly positive on the
displayed moving sheet, for both real signs of `z` with `z^2=Z`. Both closed
`X` endpoints are included. The affine coordinate `u=182(X-1/14)` makes the
left seam exactly the frozen `X14` endpoint.

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
sigma=S/X<=7/5000.
```

Both give the identical exact remainder and strict continuum reserve

```text
Rabs = 255498850715973729113515451642038401883570490078819913457313472259
       /90833633280000000000000000000000000000000000000000000000,

reserve = 182617490707934691476202171700015016148732632634921180086542686527741
          /90833633280000000000000000000000000000000000000000000000 > 0.
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
41/196<Z<=2926951353/13013000000<1,
1-x^2-y^2-Z>=222148685879/555555000000>0,
det C=(5/9)SZ>0,
25^8*A^8*S>0.
```

The referee independently proves the sharper envelopes

```text
Z<=2926891293/13013000000<1,
danger>=222151249979/555555000000>0.
```

The left base exceeds the obsolete descriptive locator `Z=1/6` by `25/588`;
no inverse formula, gate identity, PSD/rank argument, or denominator clearing
uses that locator. Thus `lambda=A/S>0`, `Q` is Hermitian PSD of rank two, the
datum is strictly dangerous, and both signed-`z` constructions are legal
without division by `z`.

## Endpoint diagnostics

At `S=1/10000`, `M=-1/1000`, `omega=nu=-1/100`, the exact values of
`36 Gamma` are

```text
X=1/14:
9384471705669180411212404704709692383897
/13720000000000000000000000000000000000 > 0,

X=1/13:
905733327727313423565954040361057123569919
/1142440000000000000000000000000000000000 > 0.
```

## Fail-closed and trust boundary

Normal source and referee runs pass. Both reject optimized Python and an
intentionally corrupted dependency hash. The source rejects deletion of a
higher term at the exact `16/947` count; the referee independently rejects a
deleted quotient term at the exact 20-term gate. Both pass `py_compile` with
the cache outside the workspace.

The proof uses no CE-046/048/059/060 witness or rejected sufficient route,
no real-part monotonicity, no dropped phase, and no extrapolation from
`X<=1/14`; both implementations rebuild the present closed cell directly
from the fully conjugated original gate.

## Bound artifacts

```text
bc28de7eb9fb5f107414eac91f03a296271b3ca42086324c0bb9981051cef302  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x13_extension.md
00fa00540037ae711ee014983884c4b95bcacfe7c39d586f4cbae7ec3cc80971  tmp/research/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x13_extension.py
05fd9905720283dea7a9e25707940217e66de2e381595d6061af7782bff6671e  tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x13_extension_independent_referee.py
abb754dcf1bde1f840bdcdd627b144048eff223f540d2619b06002b2f53ff813  tmp/research/audit/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x13_extension_test_results.txt
676435f4c4626a827e86a1d63161a459155e26e5f69773ae7e07b412ce0d5384  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x14_extension.md
4ad2db93ed2a14fc6d0d54b723fb55943f15e0ad85e0a130f1c568c473e5aaa3  tmp/research/common_metric_ranktwo_transverse_full_cone_compact_ball_reduction.md
eae0ed44d3e2e15a73298095ca951568fb789405ab2af65a9f11fe6def1533ce  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x13_extension_manifest.sha256
```

No proof assistant was used. This is an exact adjacent-cell partial theorem,
not a full positive-`Z` collar, compact-ball theorem, common-metric theorem,
or fixed crossing-lens solution. No maximality at `X=1/13` is asserted.
