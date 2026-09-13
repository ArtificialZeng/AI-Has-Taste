# Exact moving-equality-sheet blow-up for the lower compact-ball collar

Date: 2026-08-23.  Status: **exact raw-verified local reduction**.

This is a local structural lemma, not a positive-`Z` collar theorem.  It
explains why the natural Bernstein tensor and the first scale quotient fail
near the moving equality sheet without producing a negative gate direction.

## Coordinates

Use

```text
S=h^2,
mu=lambda*S=1+M,
X=x+1/5,
Y=y-3/5,
W=X^2+Y^2+Z-3X,
N=S^3(36 Gamma).
```

At `S=0`, the raw gate is

```text
N0 = 1250(1+M)^4/2187 * (3X+W)^2*(W^2+9Y^2).  (1.1)
```

The moving equality sheet is `Y=W=0`, with `X>0` and
`Z=3X-X^2`.

## First scale coefficient

Let `A1=[S^1]N`.  Exact raw reconstruction gives

```text
A1(X,0,3X-X^2,M)=0.                                (2.1)
```

Its lowest transverse term at `Y=W=0` is

```text
A1_lin = -100(1+M)^3 X^2/81 *
  ([5M(3-X)+6-5X]W+36Y).                          (2.2)
```

Thus `A1` alone is sign-indefinite.  This refutes only a termwise proof of
the scale quotient; it is not a gate-negative direction.

## Lossless double blow-up

Put

```text
W=S*w,
Y=S*v.
```

The first nonzero coefficient of `N` is the exact quadratic

```text
lim_(S->0) N(S,3X-X^2-S^2v^2+Sw,X,Sv,M)/S^2
 = a_w(w-w_c)^2+a_v(v-v_c)^2+R,
```

where

```text
a_w = 1250 X^2(1+M)^4/243,
a_v = 1250 X^2(1+M)^4/27,

w_c = -3(5MX-15M+5X-6)/[25(1+M)],
v_c = 12/[25(1+M)],

R = 40 X^2(1+M)^2/3.                              (3.1)
```

For `X>0` and `|M|<=1/1000`, all three coefficients are strictly positive.
Therefore the complete moving-sheet blow-up is strictly positive in every
transverse direction.  The overlap `X=0` is degenerate and must be checked
in a separate center chart; division by `X^2` is not valid there.

## First explicit projective chart

The smallest chart test centers the exact squares:

```text
W=S*(w_c+omega),
Y=S*(v_c+nu),
```

clears the positive denominator `1+M`, and divides only on `X>0` by
`S^2X^2`.  The first rational test cell is

```text
0<=S<=1/10000,
1/4000<=X<=3/10000,
|M|<=1/1000,
|omega|,|nu|<=1/100.
```

This cell lies near the internal moving equality sheet and stays away from
the forbidden overlap `X=0`.  A separate center chart is required before any
positive-`Z` theorem candidate can be asserted.

## Verification

The fail-closed raw verifier is

```text
tmp/research/verify_common_metric_ranktwo_transverse_compact_ball_lower_z_baseline_quadratic_no_go.py
```

It constructs the original Hermitian compression, `Q`, and `Q^2`, verifies
(1.1), (2.1), and the complete-square identity (3.1).  No numerical sample,
CE-046 monotonicity, CE-048 absorption, or CE-059 fixed allocation is used.
