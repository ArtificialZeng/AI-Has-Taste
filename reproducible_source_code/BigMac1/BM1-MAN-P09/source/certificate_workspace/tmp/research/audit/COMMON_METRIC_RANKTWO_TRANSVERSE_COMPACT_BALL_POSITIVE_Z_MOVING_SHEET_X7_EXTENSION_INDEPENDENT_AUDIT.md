# Independent audit: moving-sheet `X7` closed cell

Date: 2026-08-24. Result: **PASS**, with scope restricted to the displayed
five-real-parameter moving sheet on `1/8<=X<=1/7`. Both exact
implementations, all six fail-closed attacks, compilation, and the direct
source manifest passed before this report was frozen.

## Audited claim

For

```text
0<S<=1/10000,
1/8<=X<=1/7,
|M|<=1/1000,
|omega|,|nu|<=1/100,
```

the original fully conjugated Hermitian gate is strictly positive on the
displayed moving sheet, for both real signs of `z` with `z^2=Z`. Both closed
`X` endpoints are included. The affine coordinate `u=56(X-1/8)` makes the
left seam exactly the frozen `X8` endpoint.

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
sigma=S/X<=1/1250.
```

Both give the identical exact remainder and strict continuum reserve

```text
Rabs = 76738949147207351558799383823406296934564924507081162185503083
       /25719120000000000000000000000000000000000000000000000,

reserve = 51702895899536933013759182485809519882915853166313231337814496917
          /25719120000000000000000000000000000000000000000000000 > 0.
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
23/64<Z<=2860512267/7007000000<1,
1-x^2-y^2-Z>=126910685879/555555000000>0,
det C=(5/9)SZ>0,
25^8*A^8*S>0.
```

The referee independently proves the sharper envelopes

```text
Z<=2860452207/7007000000<1,
danger>=126915447779/555555000000>0.
```

The left base exceeds the obsolete descriptive locator `Z=1/6` by `37/192`;
no inverse formula, gate identity, PSD/rank argument, or denominator clearing
uses that locator. Thus `lambda=A/S>0`, `Q` is Hermitian PSD of rank two, the
datum is strictly dangerous, and both signed-`z` constructions are legal
without division by `z`.

## Endpoint diagnostics

At `S=1/10000`, `M=-1/1000`, `omega=nu=-1/100`, the exact values of
`36 Gamma` are

```text
X=1/8:
83491241421482514052725948713779882679
/40000000000000000000000000000000000 > 0,

X=1/7:
37381778605583832954528361124091276383897
/13720000000000000000000000000000000000 > 0.
```

At the same endpoint node,

```text
Z      = 2218118610011710439/5433561000000000000 > 0,
danger = 126791221/555000000 > 0,
det C  = 2218118610011710439/97804098000000000000000 > 0.
```

Together with the global strict continuum reserve, these exact values show
that `X=1/7` is not a chart, legality, rank, or certificate boundary.

## Fail-closed and trust boundary

Normal source and referee runs pass. Both reject optimized Python and an
intentionally corrupted dependency hash. The source rejects deletion of a
higher term at the exact `16/947` count; the referee independently rejects a
deleted quotient term at the exact 20-term gate. Both pass `py_compile` with
the cache outside the workspace.

The proof uses no CE-046/048/059/060 witness or rejected sufficient route,
no real-part monotonicity, no dropped phase, and no extrapolation from
`X<=1/8`; both implementations rebuild the present closed cell directly
from the fully conjugated original gate.

## Bound artifacts

```text
76622dab1b117189e333db6b382b0c745a6586ea20ad9f6a85f0c43c788576c0  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x7_extension.md
05e480e1b0228a1101306374da2d0563766c4fa522725c1df380dd3f6661113d  tmp/research/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x7_extension.py
6d1b3a03a71118bb581eaface4da231e9b5bbbcc2217b8e63da188fa26f91339  tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x7_extension_independent_referee.py
2c28da4a886422022675b31e7db7f445cb4c873ec0b0549a366ec3a30b39ea01  tmp/research/audit/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x7_extension_test_results.txt
98d896613808cf42eb7f80c36dfeee39e3c1bc36d0de81718ca66b21bcdc3067  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x8_extension.md
4ad2db93ed2a14fc6d0d54b723fb55943f15e0ad85e0a130f1c568c473e5aaa3  tmp/research/common_metric_ranktwo_transverse_full_cone_compact_ball_reduction.md
1d8a857fc3d42a23470f778e799b7b617498ba6b29d503d8dd4dfde0f4bdde11  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x7_extension_manifest.sha256
```

No proof assistant was used. This is an exact adjacent-cell partial theorem,
not a full positive-`Z` collar, compact-ball theorem, common-metric theorem,
or fixed crossing-lens solution. No maximality at `X=1/7` is asserted.





