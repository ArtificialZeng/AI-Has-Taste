# Exact coverage audit for the stitched five-parameter `X` sheet

Date: 2026-08-26. Status: **exact source-side coverage audit, frozen before
opening a genuinely independent compact-ball direction**. This note does not
prove a new gate inequality and does not modify any ledger, release, PDF, or
ZIP.

## 1. Ambient lossless coordinates

The audited full-cone reduction uses

```text
S=h^2 in (0,1],  lambda>0,
(x,y,z) in the open unit ball,
Z=z^2,
det(C)=(5/9) S Z.
```

The sign `z -> -z` is the two-to-one Cholesky redundancy.  In the normalized
shape/scale coordinates `(S,mu,x,y,Z)`, where `mu=lambda*S`, the stitched
family below has

```text
0<S<=1/10000,
mu=1+M in [999/1000,1001/1000],
|M|<=1/1000, |omega|,|nu|<=1/100.
```

Thus its `X`-projection reaches `[0,1]`, but it covers neither arbitrary
`S`, arbitrary positive scale, nor an open three-dimensional shape region.

## 2. Exact image as a union of six chart maps

Put

```text
A=1+M,
lambda=A/S,
y0=12/(25A)+nu,
b0=(45M+18)/(25A)-(3/5)X+omega,
b1=b0-(10636/275)(X-1/5),
xold=-1/5+X,
y=3/5+S*y0,
X0=83059/100000,
Xstar=1019767/1040000,
Xcap=497/500.
```

The exact physical image is the union of both signed lifts
`z=+-sqrt(Z)` of the following maps, over the common parameter box above:

| `X` interval | `x` | `Z` |
|---|---|---|
| `0<=X<=1/5` | `xold` | `3X-X^2+S*b0-S^2*y0^2` |
| `1/5<=X<=3/13` | `xold` | `3X-X^2+S*b1-S^2*y0^2` |
| `3/13<=X<=X0` | `xold` | `9/13-X^2+S*b1-S^2*y0^2` |
| `X0<=X<=Xstar` | `xold` | `9/13-X^2+S*b1-S^2*y0^2+2(X-X0)` |
| `Xstar<=X<=Xcap` | `xold` | `9/13-X^2+S*b1-S^2*y0^2+2(Xstar-X0)` |
| `Xcap<=X<=1` | `xold-(3/2)(X-Xcap)` | `9/13-X^2+S*b1-S^2*y0^2+2(Xstar-X0)+2(X-Xcap)` |

In every row `y=3/5+S*y0` and `mu=A`.  This parametric union is the exact
meaning of “the stitched five-real-parameter `X` sheet.”  It is not one
global formula.  The seven parameter-level seam equalities are exact:

```text
X=1/5:    b and Z agree,
X=3/13:   Z agrees,
X=X0:     Z agrees,
X=Xstar:  Z agrees,
X=Xcap:   x and Z agree.
```

The verifier counts the two equalities at `1/5` and the two at `Xcap`
separately, hence `7/7`.

## 3. Boundary and closure

The physical parameter domain has the closed faces

```text
X=0,1 and all internal seam values,
S=1/10000,
M=+-1/1000, omega=+-1/100, nu=+-1/100,
```

and the excluded limiting face `S=0`.  The latter is only an algebraic
closure: `lambda=(1+M)/S` diverges there and it is not a physical point of
this chart.  Both signed `z` lifts are included; `Z>0` on every audited row,
so the rank-one face `Z=0` is not part of this sheet.  Every audited row is
strictly inside the danger ball.  Consequently the sheet reaches neither the
sphere boundary nor arbitrary scale/shape faces merely because its
one-dimensional `X` projection is `[0,1]`.

Also

```text
y0>=46999/100100>0,
y=3/5+S*y0>3/5
```

throughout the physical image.  This simple eliminated inequality is a
useful exact separator from independent directions.

## 4. An exact uncovered rational direction

Consider

```text
(S,lambda,x,y,Z)=(1/2,1,5/8,0,1/8).
```

It is a strict legal rank-two datum because

```text
1-x^2-y^2-Z=31/64>0,
det(C)=(5/9)SZ=5/144>0.
```

It is not in the stitched `X` sheet because its `y=0`, whereas every
physical sheet point has `y>3/5`.  It is also outside the principal audited
full-scale rational box because `x=5/8>1/2`, outside the center box because
`x>1/8`, outside the high-`Z` phase tube because `x>1/8`, outside the
`Z=0` boundary, and outside the fixed sharp-equality lift.  This is therefore
an exact **coverage gap**, not a negative gate, target counterexample,
maximality claim, or reuse of CE-046/048/059/060.

The next minimal proof/disproof gate may be taken on this rational shape ray,
with `0<S<=1` and all positive scales, before attempting any neighborhood.

## 5. Audit bindings and replay

The companion verifier binds fifteen reduction/source/referee descriptions,
rechecks the seven seams, exact interval union, strict `y` separator, and the
rational witness arithmetic:

```text
.venv/bin/python -B tmp/research/verify_compact_ball_stitched_x_sheet_coverage_audit.py
```

It intentionally does not import a gate coefficient table or infer a theorem
from numerical nodes.  The authoritative source/referee hashes are embedded
in the verifier and fail closed on byte drift.
