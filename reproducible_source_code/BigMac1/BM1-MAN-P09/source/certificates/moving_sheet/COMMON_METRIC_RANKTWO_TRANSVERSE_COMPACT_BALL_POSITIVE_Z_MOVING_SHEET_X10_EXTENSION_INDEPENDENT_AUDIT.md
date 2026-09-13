# Independent audit: moving-sheet `X10` closed cell

Date: 2026-08-24. Result: **PASS**, with scope restricted to the displayed
five-real-parameter moving sheet on `1/11<=X<=1/10`. Both exact
implementations, all six fail-closed attacks, compilation, and the direct
source manifest passed before this report was frozen.

## Audited claim

For

```text
0<S<=1/10000,
1/11<=X<=1/10,
|M|<=1/1000,
|omega|,|nu|<=1/100,
```

the original fully conjugated Hermitian gate is strictly positive on the
displayed moving sheet, for both real signs of `z` with `z^2=Z`. Both closed
`X` endpoints are included. The affine coordinate `u=110(X-1/11)` makes the
left seam exactly the frozen `X11` endpoint.

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
sigma=S/X<=11/10000.
```

Both give the identical exact remainder and strict continuum reserve

```text
Rabs = 49402788328028888026519091478503109294374086495731924832776011169131
       /17199267840000000000000000000000000000000000000000000000000,

reserve = 34577435471298132570968167233095613728692125913504268075167223988830869
          /17199267840000000000000000000000000000000000000000000000000 > 0.
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
32/121<Z<=290363181/1001000000<1,
1-x^2-y^2-Z>=188815385879/555555000000>0,
det C=(5/9)SZ>0,
25^8*A^8*S>0.
```

The referee independently proves the sharper envelopes

```text
Z<=11614287/40040000<1,
danger>=188818719209/555555000000>0.
```

The left base exceeds the obsolete descriptive locator `Z=1/6` by `71/726`;
no inverse formula, gate identity, PSD/rank argument, or denominator clearing
uses that locator. Thus `lambda=A/S>0`, `Q` is Hermitian PSD of rank two, the
datum is strictly dangerous, and both signed-`z` constructions are legal
without division by `z`.

## Endpoint diagnostics

At `S=1/10000`, `M=-1/1000`, `omega=nu=-1/100`, the exact values of
`36 Gamma` are

```text
X=1/11:
58882961473898540310036519874857514970749
/53240000000000000000000000000000000000 > 0,

X=1/10:
53498106375203857863287641100293057679
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
`X<=1/11`; both implementations rebuild the present closed cell directly
from the fully conjugated original gate.

## Bound artifacts

```text
1d5139b283f50bbcb1ad4b49e6f47b5a8a85ccc730ace19c4d3f09a33dc32b83  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x10_extension.md
dd65ae3e8a2891b13f0fa3991dbe35057dd8c04480eee3b1528c9ce9cd4dcd5c  tmp/research/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x10_extension.py
b33291f23537e5e23ae04d02a83e0f4373ec0f9fd8dd2fb33589a15ce7004364  tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x10_extension_independent_referee.py
683f1752e8b96e43bcf59f1206a0c0faf0974fc23fe829e57b1ddfb6232aa268  tmp/research/audit/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x10_extension_test_results.txt
d426d2517cfbe5cb04b0680b481ca2d7921875665cd1758eb2c08675ba69b123  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x11_extension.md
4ad2db93ed2a14fc6d0d54b723fb55943f15e0ad85e0a130f1c568c473e5aaa3  tmp/research/common_metric_ranktwo_transverse_full_cone_compact_ball_reduction.md
50f2528c996ea93119a77a0bc2ae7b5028e366d45194ed784482a09217b0d02a  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x10_extension_manifest.sha256
```

No proof assistant was used. This is an exact adjacent-cell partial theorem,
not a full positive-`Z` collar, compact-ball theorem, common-metric theorem,
or fixed crossing-lens solution. No maximality at `X=1/10` is asserted.



