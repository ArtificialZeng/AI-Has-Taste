# Recentered inward-Z adjacent cell to X=7/8: exact source candidate

Date: 2026-08-25. Status: **exact source-level partial-theorem candidate,
pending a genuinely independent definition-level referee**.

## 1. Statement and strict scope

Let

```text
0<S<=1/10000,             17/20<=X<=7/8,
|M|<=1/1000,             |omega|,|nu|<=1/100,
A=1+M,                   lambda=A/S,
y0=12/(25A)+nu,
b=(45M+18)/(25A)-(3/5)X+omega-(10636/275)(X-1/5),
x=-1/5+X,                y=3/5+S y0,
Z_old=9/13-X^2+S b-S^2 y0^2,
Z=Z_old+2(X-83059/100000).
```

For both lifts `z=+-sqrt(Z)`, the source candidate proves that the displayed
data are legal, strictly dangerous and rank two and that the original fully
conjugated Hermitian scalar gate is strictly positive.  At `X=17/20`, every
raw-gate input `(lambda,x,y,Z)` and the cleared gate splice exactly to the
independently audited preceding recentered cell.

This is one adjacent local cell.  It does not prove the full compact ball,
the general complex common-metric theorem, arbitrary nodes or dimension, or
a fixed crossing-lens optimal constant.

## 2. Definition-level and sparse reconstruction

The source reconstructs the signed compact-ball frame, the Hermitian `Q`,
all entries of `Q^2`, and the original conjugated leakage gate.  The gate has
exact degree four in `Z`.  It then uses the 134-term pre-map and exact sparse
composition in `(S,X)`; no monolithic substitution, stored quartic, control
table, sampled SDP, or floating sign decision is used.

Clearing only the positive factor

```text
25^8 A^8 S^3
```

and removing the manifestly nonnegative layer

```text
S^3 25^8 M^2 A^8 (5M^2+14M+14)
```

gives

```text
cleared/core (S,X) coefficient counts: 34/34,
centered monomials:                       1659,
bidegree (S,X):                           (7,4).
```

## 3. Continuum certificate

On

```text
X=17/20+(7/8-17/20)u,     S=tau/10000,
0<=u,tau<=1,
```

all 40 centered rational lower controls of the fresh bidegree-`(7,4)`
Bernstein tensor are strictly positive.  A weakest index is `(7,0)`, with
exact reserve

```text
36396400755316082608953526916356109068914066995807402520780718071668303870073911227
/239735779200073728000000000000000000000000000000000000000000000000000000.
```

The full weakest-control polynomial is printed in the test log.  Positivity
of all controls and nonnegativity of tensor Bernstein weights prove the
continuum statement; the 72 nodes below are diagnostics only.

## 4. Exact full-cell legality

The exact monotonicity bounds are

```text
dZ/dX >= 676699/2750000 > 0,
Z >= 97261562093134873/15857127000000000000 > 0,
Z < 40307/2600000 < 1,
T_max = -434919/17875 < 0,
```

where `T=(6/5)y0+b`.  From

```text
D=1-x^2-y^2-Z
 =(2/5)(X-3/13)-2(X-83059/100000)-S T
```

one obtains

```text
D >= 109767/650000 > 0,
det(C)=(5/9)SZ
      >= [97261562093134873/28542828600000000000] S > 0.
```

Thus the complete cell is legal, strictly dangerous and rank two for both
signed lifts.

## 5. Breaker and fail-closed tests

The literal original raw gate was evaluated at three exact scales, the
left/middle/right `X` values and all eight centered corners.  All 72 nodes
are legal and gate-positive.

The final source rejects optimized Python, a corrupted predecessor hash, a
changed sparse-`Z` normalization and deletion of one exact core coefficient.
These are fail-closed implementation attacks, not mathematical evidence.

No route excluded by CE-046, CE-048, CE-059 or CE-060 is used.  No proof
assistant is used.

## 6. Replay and next mandatory gate

```text
.venv/bin/python tmp/research/compact_ball_inward_z_recentered_lift_x7_8_exact_gate.py
```

The next gate is a separate no-import referee that reconstructs the original
Hermitian `Q,Q^2` gate, the predecessor splice, 40 controls, all full-cell
legality bounds, both signed lifts, 72 diagnostics and negative tests without
reading the source coefficient or control objects.  Until then, this is a
source candidate and must not be promoted to the project ledgers or paper.
