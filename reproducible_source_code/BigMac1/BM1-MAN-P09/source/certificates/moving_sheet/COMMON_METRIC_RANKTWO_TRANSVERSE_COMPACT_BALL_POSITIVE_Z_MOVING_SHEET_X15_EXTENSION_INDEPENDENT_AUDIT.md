# Independent audit: moving-sheet `X15` closed cell

Date: 2026-08-24. Result: **PASS**, with scope restricted to the displayed
five-real-parameter moving sheet on `1/16<=X<=1/15`. Both exact
implementations, all six fail-closed attacks, compilation, and the direct
source manifest passed before this report was frozen.

## Audited claim

For

```text
0<S<=1/10000,
1/16<=X<=1/15,
|M|<=1/1000,
|omega|,|nu|<=1/100,
```

the original fully conjugated Hermitian gate is strictly positive on the
displayed moving sheet, for both real signs of `z` with `z^2=Z`. Both closed
`X` endpoints are included. The affine coordinate `u=240(X-1/16)` makes the
left seam exactly the frozen `X16` endpoint.

## Independent reconstruction

The source reconstructs the transverse frame, all entries of `Q,Q^2`, the
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
sigma=S/X<=1/625.
```

Both give the identical exact remainder and strict continuum reserve

```text
Rabs = 17139859322735732224137800361514630715368934085852345912361009
       /6150937500000000000000000000000000000000000000000000,

reserve = 12366382505636800388307905057490747689083041004726403513462638991
          /6150937500000000000000000000000000000000000000000000 > 0.
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
47/256<Z<=1762418629/9009000000<1,
1-x^2-y^2-Z>=236963485879/555555000000>0,
det C=(5/9)SZ>0,
25^8*A^8*S>0.
```

The referee independently proves the sharper envelopes

```text
Z<=1762382593/9009000000<1,
danger>=236965708099/555555000000>0.
```

The left base already exceeds the obsolete descriptive locator `Z=1/6` by
`13/768`; no inverse formula, gate identity, PSD/rank argument, or denominator
clearing uses that locator. Thus `lambda=A/S>0`, `Q` is Hermitian PSD of rank
two, the datum is strictly dangerous, and both signed-`z` constructions are
legal without division by `z`.

## Endpoint diagnostics

At `S=1/10000`, `M=-1/1000`, `omega=nu=-1/100`, the exact values of
`36 Gamma` are

```text
X=1/16:
5243094533770053746415166844845583951
/10000000000000000000000000000000000 > 0,

X=1/15:
23847741893133467314954498194610657679
/40000000000000000000000000000000000 > 0.
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
3bf5600929c88308f9bb3cb6ce4bfbfe3b1fa9dc4632cdf49ef4ca0d3954adfb  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x15_extension.md
3b1e78e4117c34dcc04500b845fa52896308d2e815ed25df5bb4d83b9e312c27  tmp/research/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x15_extension.py
7982c8475f04bea59ce438c88bdae65f131fe3752327635ab3fa69b750889f9d  tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x15_extension_independent_referee.py
c6e900a4042aa57540898dc2b6f3eca180d4215516a02e2515a5fedc093ad405  tmp/research/audit/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x15_extension_test_results.txt
d45e166a16d57ae39e596e023056965ad14c362359f19ceb268216ecce1d640d  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x16_extension.md
4ad2db93ed2a14fc6d0d54b723fb55943f15e0ad85e0a130f1c568c473e5aaa3  tmp/research/common_metric_ranktwo_transverse_full_cone_compact_ball_reduction.md
ef4926cced7ccf1f1178ba0a2c3f598968e1e363a5c8b1b309aac67607c2e2ff  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x15_extension_manifest.sha256
```

No proof assistant was used. This is an exact adjacent-cell partial theorem,
not a full positive-`Z` collar, compact-ball theorem, common-metric theorem,
or fixed crossing-lens solution. No maximality at `X=1/15` is asserted.
