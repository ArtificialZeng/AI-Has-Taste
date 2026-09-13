# Independent audit: moving-sheet `X8` closed cell

Date: 2026-08-24. Result: **PASS**, with scope restricted to the displayed
five-real-parameter moving sheet on `1/9<=X<=1/8`. Both exact
implementations, all six fail-closed attacks, compilation, and the direct
source manifest passed before this report was frozen.

## Audited claim

For

```text
0<S<=1/10000,
1/9<=X<=1/8,
|M|<=1/1000,
|omega|,|nu|<=1/100,
```

the original fully conjugated Hermitian gate is strictly positive on the
displayed moving sheet, for both real signs of `z` with `z^2=Z`. Both closed
`X` endpoints are included. The affine coordinate `u=72(X-1/9)` makes the
left seam exactly the frozen `X9` endpoint.

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
sigma=S/X<=9/10000.
```

Both give the identical exact remainder and strict continuum reserve

```text
Rabs = 11826968083766045157078344875963179444223176294073816427994510187
       /4026531840000000000000000000000000000000000000000000000,

reserve = 655669467027014752823953668812526531392761922720180020869332444674853
          /326149079040000000000000000000000000000000000000000000000 > 0.
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
26/81<Z<=89951889/250250000<1,
1-x^2-y^2-Z>=152704310879/555555000000>0,
det C=(5/9)SZ>0,
25^8*A^8*S>0.
```

The referee independently proves the sharper envelopes

```text
Z<=719600097/2002000000<1,
danger>=305416955083/1111110000000>0.
```

The left base exceeds the obsolete descriptive locator `Z=1/6` by `25/162`;
no inverse formula, gate identity, PSD/rank argument, or denominator clearing
uses that locator. Thus `lambda=A/S>0`, `Q` is Hermitian PSD of rank two, the
datum is strictly dangerous, and both signed-`z` constructions are legal
without division by `z`.

## Endpoint diagnostics

At `S=1/10000`, `M=-1/1000`, `omega=nu=-1/100`, the exact values of
`36 Gamma` are

```text
X=1/9:
66007715558663416233147601903988257679
/40000000000000000000000000000000000 > 0,

X=1/8:
83491241421482514052725948713779882679
/40000000000000000000000000000000000 > 0.
```

At the same endpoint node,

```text
Z      = 39857763593045111/110889000000000000 > 0,
danger = 305116967/1110000000 > 0,
det C  = 39857763593045111/1996002000000000000000 > 0.
```

Together with the global strict continuum reserve, these exact values show
that `X=1/8` is not a chart, legality, rank, or certificate boundary.

## Fail-closed and trust boundary

Normal source and referee runs pass. Both reject optimized Python and an
intentionally corrupted dependency hash. The source rejects deletion of a
higher term at the exact `16/947` count; the referee independently rejects a
deleted quotient term at the exact 20-term gate. Both pass `py_compile` with
the cache outside the workspace.

The proof uses no CE-046/048/059/060 witness or rejected sufficient route,
no real-part monotonicity, no dropped phase, and no extrapolation from
`X<=1/9`; both implementations rebuild the present closed cell directly
from the fully conjugated original gate.

## Bound artifacts

```text
98d896613808cf42eb7f80c36dfeee39e3c1bc36d0de81718ca66b21bcdc3067  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x8_extension.md
6a68e71a059bf8ff867e51529a08130b295773a6a50cf5e3c092c935cfb1f8c1  tmp/research/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x8_extension.py
17cbf3b55c7f0cd9898d5bea8cce0bcdd6b2cb15fface8eff8bba62b44cf7af7  tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x8_extension_independent_referee.py
839bb2e1e86881759a8a530c06413ce08dd3923c839a7dbd36df10f87849a94a  tmp/research/audit/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x8_extension_test_results.txt
a159ddf16593fe599b7d40adbceeb5e760965796582d8c4a6cee62e89f6dbeab  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x9_extension.md
4ad2db93ed2a14fc6d0d54b723fb55943f15e0ad85e0a130f1c568c473e5aaa3  tmp/research/common_metric_ranktwo_transverse_full_cone_compact_ball_reduction.md
f4e2f4ca7951e1bd485b83110570e94b42124f505742399f394209406e897533  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x8_extension_manifest.sha256
```

No proof assistant was used. This is an exact adjacent-cell partial theorem,
not a full positive-`Z` collar, compact-ball theorem, common-metric theorem,
or fixed crossing-lens solution. No maximality at `X=1/8` is asserted.




