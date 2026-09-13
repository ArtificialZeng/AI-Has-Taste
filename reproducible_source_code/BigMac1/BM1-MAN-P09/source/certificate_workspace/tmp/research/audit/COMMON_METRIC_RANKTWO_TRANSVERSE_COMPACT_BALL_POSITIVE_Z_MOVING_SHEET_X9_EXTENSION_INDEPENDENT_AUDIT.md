# Independent audit: moving-sheet `X9` closed cell

Date: 2026-08-24. Result: **PASS**, with scope restricted to the displayed
five-real-parameter moving sheet on `1/10<=X<=1/9`. Both exact
implementations, all six fail-closed attacks, compilation, and the direct
source manifest passed before this report was frozen.

## Audited claim

For

```text
0<S<=1/10000,
1/10<=X<=1/9,
|M|<=1/1000,
|omega|,|nu|<=1/100,
```

the original fully conjugated Hermitian gate is strictly positive on the
displayed moving sheet, for both real signs of `z` with `z^2=Z`. Both closed
`X` endpoints are included. The affine coordinate `u=90(X-1/10)` makes the
left seam exactly the frozen `X10` endpoint.

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
sigma=S/X<=1/1000.
```

Both give the identical exact remainder and strict continuum reserve

```text
Rabs = 363757802203554163502406509408160127898873417615147567258650081
       /125382662553600000000000000000000000000000000000000000,

reserve = 252065893110471162872568856796737151621022711582384852432741349919
          /125382662553600000000000000000000000000000000000000000 > 0.
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
29/100<Z<=26031927661/81081000000<1,
1-x^2-y^2-Z>=518298057637/1666665000000>0,
det C=(5/9)SZ>0,
25^8*A^8*S>0.
```

The referee independently proves the sharper envelopes

```text
Z<=26031387121/81081000000<1,
danger>=518309168737/1666665000000>0.
```

The left base exceeds the obsolete descriptive locator `Z=1/6` by `37/300`;
no inverse formula, gate identity, PSD/rank argument, or denominator clearing
uses that locator. Thus `lambda=A/S>0`, `Q` is Hermitian PSD of rank two, the
datum is strictly dangerous, and both signed-`z` constructions are legal
without division by `z`.

## Endpoint diagnostics

At `S=1/10000`, `M=-1/1000`, `omega=nu=-1/100`, the exact values of
`36 Gamma` are

```text
X=1/10:
53498106375203857863287641100293057679
/40000000000000000000000000000000000 > 0,

X=1/9:
66007715558663416233147601903988257679
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
`X<=1/10`; both implementations rebuild the present closed cell directly
from the fully conjugated original gate.

## Bound artifacts

```text
a159ddf16593fe599b7d40adbceeb5e760965796582d8c4a6cee62e89f6dbeab  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x9_extension.md
8c668472aee9fe42bb740d1c4fe0671396140c379f189e45c41df4e94f2aa076  tmp/research/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x9_extension.py
fd076079aeee4c7d4dbb443156680f91182ca4c686be5dc6218dadae40da93f0  tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x9_extension_independent_referee.py
94e05e431e23b661e6e20a4d06359eb23e5dc87836a08a1de3ae21d4a9edda4a  tmp/research/audit/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x9_extension_test_results.txt
1d5139b283f50bbcb1ad4b49e6f47b5a8a85ccc730ace19c4d3f09a33dc32b83  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x10_extension.md
4ad2db93ed2a14fc6d0d54b723fb55943f15e0ad85e0a130f1c568c473e5aaa3  tmp/research/common_metric_ranktwo_transverse_full_cone_compact_ball_reduction.md
3165b90f8e40fdae79438308e0f5a1bda5c34f0ce3f3cc261571f3ce1eea2207  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x9_extension_manifest.sha256
```

No proof assistant was used. This is an exact adjacent-cell partial theorem,
not a full positive-`Z` collar, compact-ball theorem, common-metric theorem,
or fixed crossing-lens solution. No maximality at `X=1/9` is asserted.




