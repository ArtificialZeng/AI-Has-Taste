# Independent referee audit: inward-Z rational legality-frontier extension

Date: 2026-08-25  
Verdict: **PASS — EXACT INDEPENDENTLY AUDITED PARTIAL THEOREM**  
Severity count: **fatal 0, major 0, minor/expository 1**

The optimal constant of a fixed crossing lens, the full compact-ball
quartic, the general common-metric gate, and the arbitrary-node bridge remain
open.  This audit certifies only the rational inward-Z cell stated below and
the specified rational bracket for loss of this coordinate chart's legality.

## 1. Frozen claim and independence boundary

The referee bound the following bytes before mathematical work:

| Artifact | SHA-256 |
|---|---|
| `tmp/research/compact_ball_inward_z_legality_frontier_extension.py` | `1a2ef5c669d1602a27641f05ae1d051e7f03d6db99a8280085b3ececd23667a4` |
| `tmp/research/common_metric_ranktwo_transverse_compact_ball_inward_z_legality_frontier_extension_source_candidate.md` | `5e4109a188f3301412dd49f78039f2a0d4e107948f8e23c1bdc79cbcd4029aa0` |
| compact-ball reduction note | `4ad2db93ed2a14fc6d0d54b723fb55943f15e0ad85e0a130f1c568c473e5aaa3` |
| compact-ball reduction audit | `0a13cb475d667b5ff281f798628571756403e95fbb1eff118fa5cfcba8758f20` |
| predecessor independent verifier | `0928e8ab3c9c6027feb646af68a7dc4d567d34970887eb672520d120c6a387ab` |
| predecessor independent audit | `e217488778451a9745aaa630e943c974f8fc8671577ef40cd008deb36c0e7652` |

The candidate source program was not imported, executed, parsed, or read for
coefficients.  Its bytes were used only for SHA-256.  The claim note supplied
the proposition to test.  No candidate Bernstein table or decisive
coefficient was reused.

The independent verifier is
`tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_inward_z_legality_frontier_extension_independent_referee.py`,
SHA-256
`9d00fc3b026bd6751831e412205fb2803a9026c6eba38c408f5c861f886b1642`.
It uses project-local CPython 3.11.15 and SymPy 1.14.0.

## 2. Exact theorem certified

For

```text
0<S<=1/10000,               131/520<=X<=83059/100000,
|M|<=1/1000,               |omega|,|nu|<=1/100,
A=1+M,                     lambda=A/S,
y0=12/(25A)+nu,
b=(45M+18)/(25A)-(3/5)X+omega-(10636/275)(X-1/5),
x=-1/5+X,                  y=3/5+S*y0,
Z=9/13-X^2+S*b-S^2*y0^2,
```

both lifts `z=+-sqrt(Z)` are legal, strictly dangerous rank-two data, and
the original fully conjugated Hermitian scalar gate is strictly positive.
This is an infinite exact local theorem, not a numerical finite result.

In addition, the same polynomial Bernstein certificate remains strict when
the right endpoint is enlarged to `X=4153/5000`, but the worst exact chart
coordinate is then negative.  This proves a rational bracket for loss of
this coordinate chart's legality.  It is not a counterexample to the raw
Hermitian gate and not a maximality theorem for that gate.

## 3. Definition-level reconstruction

The referee began with the compact-ball compression matrix

```text
C=[[h^2, h(j+i k)], [h(j-i k), j^2+k^2+ell^2]],
H=U C U^*,     Q=lambda H.
```

It separately rebuilt the same `H` from the Cholesky/Gram columns

```text
g_mix=h r+(j-i k)f,       g_z=ell f,
H=g_mix g_mix^*+g_z g_z^*.
```

The two constructions agree entry by entry.  The verifier checks the frame,
Hermiticity, `det(C)=(5/9)SZ`, and invariance under `z -> -z`.  It then forms
the complete `3 x 3` matrix `Q`, multiplies it to obtain every entry of `Q^2`,
and evaluates the literal fully conjugated gate.  A separate cyclic-vector
construction agrees exactly.

The quotient reduction is applied in the order

```text
q^2=1-S,       z^2=Z,       h^2=S,
```

which is different from the predecessor referee's elimination order.  All
frame radicals and the signed lift cancel.  Deleting a raw-gate square or
flipping the danger sign makes the two constructions disagree and therefore
fails closed.

## 4. Positive clearing and continuum certificate

The referee substitutes the inward-Z sheet into the reconstructed raw gate
and verifies both directions of the positive clearing

```text
P=25^8 A^8 S^3 (36 Gamma).
```

Since `A>0` and `S>0`, this clearing is sign-equivalent to the original gate.
After removing only the manifestly nonnegative layer

```text
S^3 25^8 M^2 A^8 (5M^2+14M+14),
```

the independently recovered exact structural counts are:

| Object | Result |
|---|---:|
| nonzero `(S,X)` coefficients before layer removal | 32 |
| nonzero `(S,X)` coefficients after layer removal | 32 |
| centered `(S,X,M,omega,nu)` monomials | 1,581 |
| bidegree in `(S,X)` | `(7,4)` |

On the lossless map

```text
X=131/520+(83059/100000-131/520)u,
S=tau/10000,                    0<=u,tau<=1,
```

the referee expands a fresh dense polynomial in `(u,tau)` and applies the
direct binomial monomial-to-Bernstein transform.  It independently obtains:

- 40 controls of bidegree `(7,4)` in `(tau,u)`;
- 40/40 strict centered rational lower controls;
- no zero controls;
- unique weakest index `(0,0)`;
- exact weakest reserve

```text
119539987320009056100108078372012547879
/718761099264000000000000000000;
```

- complete weakest-control polynomial

```text
461578369140625 (M+1)^12 / 2741856.
```

Tensor Bernstein weights are nonnegative and sum to one, so this is a
continuum proof.  The 72 nodes below are diagnostics only.

A second independently generated tensor on

```text
131/520<=X<=4153/5000
```

also has 40/40 strict centered lower controls.  Thus the polynomial
certificate has not failed at the rational point where chart legality has
already failed.

## 5. Exact predecessor splice

The preceding sheet is rebuilt with the unsimplified expression

```text
Z_old=3X-X^2-3(X-3/13)+S*b-S^2*y0^2.
```

At `X=131/520`, the referee checks exact equality of every literal input
`(x,y,Z,lambda)` supplied to the single reconstructed raw-gate expression.
This is a definition-level termwise splice and does not compare imported
coefficient tables.

## 6. Full-cell legality and the rational root bracket

Exact derivatives and endpoint arithmetic give

```text
b_min = -24601484583/1017500000,
Z_min = 160243869095653/15857127000000000000 > 0,
Z < 170039/270400 < 1,
lambda > 0.
```

Writing `T=(6/5)y0+b`, the exact danger identity is

```text
D=1-x^2-y^2-Z=(2/5)(X-3/13)-S*T.
```

The exact full-cell bound `T<=-10931/13000` yields

```text
D >= 11/1300+(10931/13000)S > 0.
```

Moreover

```text
det(C)=(5/9)SZ
      >= [160243869095653/28542828600000000000] S > 0.
```

Thus every claimed point is legal, strictly dangerous, and rank two for
both signed lifts.

At the worst centered corner, the referee obtains the exact rational signs

```text
Z_min(83059/100000)
  = 160243869095653/15857127000000000000 > 0,
Z_min(4153/5000)
  = -103795949201927/15857127000000000000 < 0.
```

Its derivative is exactly

```text
-2X-(10801/2750000),
```

and is strictly decreasing and negative throughout the bracket.  Hence the
sign change is an exact chart-legality root bracket, not a numerical event.

## 7. Adversarial diagnostics and rejected routes

The verifier evaluates the original rational raw gate at three scales,
three `X` values, and all eight centered corners.  All 72 points are legal,
strictly dangerous, and gate-positive.  The minimum diagnostic value of
`36 Gamma` is

```text
18496743172049663138663507959661298309352100534665079
/16726464040000000000000000000000000000000000
```

at

```text
(S,X,M,omega,nu)=(1/10000,131/520,-1/1000,1/100,-1/100).
```

These nodes do not prove the theorem; the control tensor does.

The proof reconstructs the original compact-ball gate directly.  It uses no
real-part monotonicity (CE-046), feasible-center absorption (CE-048), fixed
copositivity allocation (CE-059), CE-060 route, sampled SDP, or floating sign
decision.

## 8. Fail-closed and reproducibility tests

| Test | Expected | Observed |
|---|---|---|
| normal definition-level replay | exit 0 | PASS |
| optimized Python `-O` | reject | exit 1 at `__debug__` gate |
| wrong source path/hash | reject | exit 1 at source SHA gate |
| delete one raw-gate square | reject | exit 1 at two-gate identity |
| flip the danger-term sign | reject | exit 1 at two-gate identity |
| delete one complete `(S,X)` core coefficient | reject | exit 1 at 32-coefficient gate |
| external-cache `py_compile` | exit 0 | PASS |
| predecessor source manifest | 6/6 | PASS |
| predecessor referee manifest | 7/7 | PASS |

The complete test record is
`tmp/research/compact_ball_inward_z_legality_frontier_extension_independent_referee_test_results.txt`,
SHA-256
`8ef0d83b61e8af32081281d0686555de93162117b942c19fad5163ee952cb8c9`.
It records the one pre-freeze symbolic-boolean implementation failure; that
failure was repaired and a complete from-scratch replay then passed.

### Minor/expository finding

The candidate note says its final source replay hash is recorded in a source
freeze manifest, but no dedicated legality-frontier source-freeze manifest
was present at audit time.  This audit nevertheless binds the exact candidate
source and claim note directly by SHA-256, and the independent release
manifest includes them.  The omission does not affect the mathematics, but a
future release should either add the dedicated source manifest or correct the
sentence.

## 9. Referee decision and strict scope

There is no fatal or major gap in the displayed cell theorem.  The correct
scientific status is therefore:

> **EXACT INDEPENDENTLY AUDITED PARTIAL THEOREM.**

It proves strict raw-gate positivity and legality only on the displayed
rational cell, plus a rational bracket showing where this particular chart
has already become illegal while the polynomial certificate remains strict.
It does not prove maximality, cover illegal points by another chart, settle
the remaining compact ball, prove the general common-metric theorem, supply
an arbitrary-node interpolation bridge, or determine a fixed crossing-lens
optimal constant.  No proof assistant was used.
