# Independent audit: maximal moving-sheet danger breakpoint

Date: 2026-08-24. Result: **PASS**, subject to independent root replay. The
strict-danger theorem has the exact half-open scope

```text
0<S<=1/10000,
1/5<=X<428905727/1858957100,
|M|<=1/1000,
|omega|,|nu|<=1/100.
```

The original gate certificate is strict on the closed `X` interval through
the displayed endpoint. The full compact ball, common-metric theorem, and
fixed crossing-lens problem remain open.

## Original-gate reconstruction

The source reconstructs every entry of the transverse frame, compression,
`Q,Q^2`, literal fully conjugated Hermitian gate, and a separately ordered
Gram-vector gate. It checks their exact equality before applying the moving
sheet and builds the quotient by sparse exact substitution.

The independent referee imports neither source/discovery code, cached
quartics, nor coefficient tables. It reconstructs signed-`z` Gram columns,
uses a different Gram-vector component order, and builds the quotient by
direct affine-power expansion. Both recover

```text
134 pre-map monomials,
20 quotient (S,X) terms of bidegree (5,4),
16 higher terms,
947 centered parameter monomials,
sigma=S/X<=1/2000.
```

They give the identical exact remainder and reserve

```text
Rabs =
311837602694763856953654581992404505154268305263846785274456274343807875982376092575027407
/103541941206646325492097536439091200000000000000000000000000000000000000000000000,

reserve =
208146457517980767271040318929344719831500991336682480497608668045656192124017623907424972593
/103541941206646325492097536439091200000000000000000000000000000000000000000000000 > 0.
```

Thus the closed gate statement is a continuum certificate, not an inference
from the 72-node diagnostic grid.

## Exact legality and boundary classification

Both programs independently simplify the coupled danger coefficient to

\[
 B=\frac95+\omega+\frac65\nu-\frac{63}{125A}-\frac35X
\]

and verify

```text
B>=585533340809/515860595250>0,
dB/dA=63/(125A^2)>0,
dB/domega=1,
dB/dnu=6/5,
dB/dX=-3/5.
```

For `D=1-x^2-y^2-Z`,

\[
 D=\frac35-\frac{13}{5}X-SB,\qquad
 \partial_XD=-\frac{13}{5}+\frac35S<0,\qquad
 \partial_SD=-B<0.
\]

The unique uniform minimum is therefore at
`S=1/10000`, `M=1/1000`, and `omega=nu=1/100`. There

\[
 D=-\frac{1858957100X-428905727}{715000000}.
\]

Hence strict danger holds exactly for
`X<428905727/1858957100`; at equality there is one unique zero-danger
corner. The source proves

```text
14/25<Z<=220824455717308720521/345572149964041000000<1,
```

and the referee independently proves

```text
Z<=552049179533075241627/863930374910102500000<1.
```

Since `det C=(5/9)SZ>0`, rank two and both signed-`z` constructions are
legal throughout the half-open theorem domain.

## Seam and boundary diagnostics

The exact affine coordinate sends `u=0` to the frozen `X=1/5` seam and
`u=1` to the breakpoint. Of 72 exact rational nodes, 71 are strictly
dangerous and one is the classified boundary corner. Every original gate
value is positive.

At the negative centered corner,

```text
X=1/5:
36 Gamma =
213355344357890421512795094325969057679
/40000000000000000000000000000000000 > 0,

X=428905727/1858957100:
36 Gamma =
440192380473245412784529502413179004647222033560333676023602100187
/62036421210789424476671714120000000000000000000000000000000000 > 0.
```

At the unique zero-danger corner,

```text
36 Gamma =
31769777656530376672684788597449530147261943789366551863977
/4459366315900461674520000000000000000000000000000000000 > 0,

Z =
220819670985134517424899959
/345572149964041000000000000 > 0,

danger = 0,

det C =
220819670985134517424899959
/6220298699352738000000000000000 > 0.
```

The requested `X=1/4` endpoint has exact worst-corner danger
`-8958387/178750000<0`. This is a nonlegal chart boundary, not a gate
counterexample. No CE entry is warranted.

## Fail-closed and provenance audit

Normal source and referee runs pass. Both reject optimized Python, a corrupted
dependency hash, and a deleted quotient term; both pass `py_compile` with
the cache outside the workspace.

Two pre-freeze referee runs stopped at derivative assertions because SymPy
retained an uncancelled `(M+1)/(M+1)` form. The assertions were minimally
replaced by exact checks of
`factor(derivative-expected)==0`; no constant, parameterization, or
mathematical inequality changed. The final frozen referee was then rerun from
definitions and passed normal and all attacks.

The exact discovery provenance has SHA-256
`68a4882218be6441475b2aa3c8084f45c16aeac09af46a0a4a597b3bba71a8f9`.
Neither proof verifier imports discovery code. The proof uses no
CE-046/048/059/060 route, real-part monotonicity, dropped phase, sampled SDP,
or monotone extrapolation.

## Bound artifacts

```text
e3f37ef598110eaad6c96a45eabff1e6313256923950057e8145568dbde865e0  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x4_breakpoint_extension.md
e6190b282d16b837adf22c252bb9dd82308ddcc2c3b34806ccae445d365a7b5d  tmp/research/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x4_breakpoint_extension.py
39c053b869f0b8a6a4af23873d9be4342517220f0a93aa777ffc89112d158873  tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x4_breakpoint_extension_independent_referee.py
5b064714363820cb9faddcf1b93ae11a0ddc52ffc6b074a94c26dccded03abde  tmp/research/audit/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x4_breakpoint_extension_test_results.txt
68a4882218be6441475b2aa3c8084f45c16aeac09af46a0a4a597b3bba71a8f9  tmp/research/compact_ball_positive_z_moving_sheet_x4_maximal_open_discovery.py
aa25a3f7240fbe6cd6076399757382919757b3b7ad34a5ba60e8ed662e770126  tmp/research/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x4_breakpoint_extension_source_freeze_manifest.sha256
fc84f3beb07f2b9d82f69d8a9a50039f64e13e76317069f388c50027102c9b52  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x4_breakpoint_extension_manifest.sha256
a86dbe3eea4d9bfaf2772383407e65a5960e6941344713377068ff048ffc5f4d  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x5_extension.md
4ad2db93ed2a14fc6d0d54b723fb55943f15e0ad85e0a130f1c568c473e5aaa3  tmp/research/common_metric_ranktwo_transverse_full_cone_compact_ball_reduction.md
```

No proof assistant was used. This is a maximal uniform strict-danger theorem
only for the displayed moving sheet and centered parameter box. It is not a
full compact-ball, common-metric, or fixed crossing-lens solution.

