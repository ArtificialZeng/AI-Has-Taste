# Independent audit: moving-sheet `X16` closed cell

Date: 2026-08-24. Result: **PASS**, with scope restricted to the displayed
five-real-parameter moving sheet on `1/17<=X<=1/16`. Both exact
implementations, all six fail-closed attacks, compilation, and the direct
source manifest passed before this report was frozen.

## Audited claim

For

```text
0<S<=1/10000,
1/17<=X<=1/16,
|M|<=1/1000,
|omega|,|nu|<=1/100,
```

the original fully conjugated Hermitian gate is strictly positive on the
displayed five-real-parameter moving sheet, for both real signs of `z` with
`z^2=Z`. Both closed `X` endpoints are included. The affine coordinate
`u=272(X-1/17)` makes the left seam exactly the frozen `X17` endpoint.

## Independent reconstruction

The source starts from the original transverse frame, reconstructs every
entry of `Q,Q^2`, checks Hermitian symmetry and the literal conjugated gate,
and separately obtains the same scalar by a Gram-vector ordering. Its
moving-sheet quotient is built by a sparse exact substitution.

The referee imports neither source code, discovery code, cached quartic, nor
coefficient table. It uses signed-`z` Gram columns, a different Gram-vector
component order, and direct affine-power substitution. The source checks the
134-term pre-map; both independently recover

```text
20 quotient (S,X) terms of bidegree (5,4),
16 higher terms,
947 centered (M,omega,nu) monomials,
sigma=S/X<=17/10000.
```

They give the identical strict continuum reserve

```text
141635970781970514779535557286727779805714617592267929266532825868383583
/70448201072640000000000000000000000000000000000000000000000 > 0.
```

The 72 exact seam/interior/endpoint nodes are falsification diagnostics only;
the displayed continuum reserve proves the result.

## Legality and the `Z=1/6` dependency audit

This cell lies strictly beyond the predecessor's convenient locator
`Z=1/6`: at its left base `X=1/17`, `S -> 0+`, the excess is exactly
`11/1734`. Therefore the actual compact-ball prerequisites, rather than the
old descriptive locator, were reconstructed. They are exactly

```text
0<S=h^2<=1, lambda>0, Z=z^2>0, x^2+y^2+Z<1.
```

No inverse formula, PSD/rank argument, gate identity, denominator clearing,
or moving-sheet bridge requires `Z<1/6`. The source proves

```text
A>=999/1000>0,
50/289<Z<=735402099/4004000000<1,
1-x^2-y^2-Z>=242981998379/555555000000>0,
det C=(5/9)SZ>0,
25^8*A^8*S>0.
```

The referee independently uses monotonic endpoint choices and proves the
sharper envelopes

```text
Z<=183846771/1001000000<1,
danger>=971936326841/2222220000000>0.
```

Thus `lambda=A/S>0`, the frame is real since `S<1`, every quotient divisor is
positive, `Q` is Hermitian PSD of rank two, and the datum is strictly
dangerous in the open unit ball. Both signed-`z` constructions are explicit;
neither divides by `z`.

## Endpoint diagnostics

At `S=1/10000`, `M=-1/1000`, `omega=nu=-1/100`, the exact values of
`36 Gamma` are

```text
X=1/17:
1552541492892247573695625585542882277607759
/3340840000000000000000000000000000000000 > 0,

X=1/16:
5243094533770053746415166844845583951
/10000000000000000000000000000000000 > 0.
```

## Fail-closed and trust boundary

Normal source and referee runs pass. Both reject optimized Python and an
intentionally corrupted dependency hash. The source rejects deletion of a
higher term at the exact `16/947` count; the referee independently rejects a
deleted quotient term at the exact 20-term gate. Both pass `py_compile` with
the cache outside the workspace.

For the v10 portable package, both programs accept exactly their canonical
`certificate_workspace` layout and their grouped `certificates/moving_sheet`
layout.  Each derives the release-local `certificate_workspace` from
`__file__`, confines every resolved dependency to it before hashing, and
rejects an unknown layout.  This packaging adaptation changes neither the
exact gate nor any theorem value above.

## Bound artifacts

```text
d45e166a16d57ae39e596e023056965ad14c362359f19ceb268216ecce1d640d  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x16_extension.md
6b4835d5c00e56efa90d6451bd789554a0304be9880f45fc739066660d9ac2d4  tmp/research/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x16_extension.py
cfb2bd700c68ac9f37cfbe1bf9f87b5d46791dc953d54e33c920929583044d6e  tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x16_extension_independent_referee.py
b317db5c23d8f8fa0e791fe066a052c5f94353e9b60f067cce20bf8caf974c64  tmp/research/audit/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x16_extension_test_results.txt
e9ed0d778a4754a3b7144754b0277cf67c282bae6879676b4d24a34239cf12fc  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x17_extension.md
4ad2db93ed2a14fc6d0d54b723fb55943f15e0ad85e0a130f1c568c473e5aaa3  tmp/research/common_metric_ranktwo_transverse_full_cone_compact_ball_reduction.md
de35841d4965ee55fe1afb736dc158dba818dcfa6ad743c1d40284eae7644d68  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x16_extension_manifest.sha256
```

No proof assistant was used. This is an exact adjacent-cell partial theorem,
not a full positive-`Z` collar, compact-ball theorem, common-metric theorem,
or fixed crossing-lens solution. No maximality at `X=1/16` is asserted.
