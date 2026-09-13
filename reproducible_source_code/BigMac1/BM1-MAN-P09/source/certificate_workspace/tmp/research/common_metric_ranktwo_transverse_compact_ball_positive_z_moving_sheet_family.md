# A strict positive-`Z` moving-sheet family for the compact-ball quartic

## Honest scope

This is a five-real-parameter strict partial theorem for the compact-ball
gate.  It is not a neighborhood of the whole sharp equality sheet, not the
full lower-`Z` box, not the full compact unit ball, not the unrestricted
complex Hermitian/common-metric theorem, and not the fixed crossing-lens
constant.  The normalized positive scale is restricted by
`lambda*S=1+M` with `|M|<=1/1000`; arbitrary positive scale is not claimed.

## The parametric family

Let

```text
0<S<=1/10000,
0<=X<=3/10000,
|M|<=1/1000,
|omega|<=1/100,
|nu|<=1/100.
```

Define

```text
A       = 1+M,
lambda  = A/S,
y0      = 12/(25A)+nu,
wc      = -3(5MX-15M+5X-6)/(25A),
Y       = S y0,
W       = S(wc+omega),
Z       = 3X-X^2-Y^2+W,
x       = -1/5+X,
y       =  3/5+Y.
```

Then `lambda>0`, the corresponding compact-ball point is strictly dangerous
and has `Z>0`, the transverse compression is positive definite and hence has
rank two, and the original Hermitian `Q,Q^2` scalar gate satisfies

```text
36 Gamma(S,Z,x,y,lambda) > 0.
```

The coordinate `Z` is `z^2`; either sign of `z` gives the same compression.

## Legality reserves

On the parameter box,

```text
999/1000 <= A <= 1001/1000,

46999/100100 <= y0 <= 16333/33300,
0<Y<=16333/333000000<1/1000,

1311167/1850000 <= wc+omega <= 73181/100100.
```

The lower bound uses the worst value of the additional term `-3X/5` in
`wc`; the upper bound occurs at `X=0`.  Consequently

```text
Z >= S * 7858868231111/11088900000000 > 0,
Z <= 974081/1001000000 < 1/1000.
```

The exact identity

```text
x^2+y^2+Z = 2/5+(13/5)X+(6/5)Y+W
```

gives

```text
1-x^2-y^2-Z
 >= 332826352979/555555000000
 > 299/500.
```

Thus these points lie strictly inside the danger ball.

For the original transverse frame, put

```text
j     = (1+5x)/(3 sqrt(5)),
kappa = (-3+5y)/(3 sqrt(5)),
C = [[S, sqrt(S)(j+i kappa)],
     [sqrt(S)(j-i kappa), j^2+kappa^2+(5/9)Z]].
```

Then

```text
det C=(5/9)SZ>0.
```

Since its leading principal entry is `S>0`, `C` is positive definite.  The
two transverse Gram columns are orthonormal, and multiplication by
`lambda>0` therefore produces a legal Hermitian PSD matrix `Q` of rank two.

## Exact sign proof

Starting from the original Hermitian `Q,Q^2` gate, let

```text
N=S^3(36 Gamma)
```

after the lossless substitution `lambda=(1+M)/S`.  Apply the moving-sheet
map above.  Its only coordinate denominator is positive.  After multiplying
by

```text
D=25^8(1+M)^8=152587890625(1+M)^8>0,
```

the result is exactly divisible by `S^2`.  Write

```text
Qhat = D N/S^2.
```

The sparse quotient contains exactly 20 `(S,X)` monomials and has bidegree
`(5,4)`.  Its constant layer is zero and its first layer is

```text
H1=152587890625 M^2 S(1+M)^8(5M^2+14M+14)>=0.
```

After removing `H1`, the homogeneous quadratic layer is

```text
H2=aS^2+bSX+cX^2.
```

Exact centered-monomial bounds on the full `(M,omega,nu)` box give

```text
a >= 481040550200263282578648409035494777132062079
     /114661785600000000000000000000000,

b >= 2301835302565365212028445402384697058519239
     /191102976000000000000000000000,

c >= c0
   = 2564950982194530478444050838857341987999
     /1274019840000000000000000000 > 0.
```

Hence `H2>=c0(S^2+SX+X^2)`.

All remaining terms are grouped by their excess total `(S,X)` degree
`d=1,...,5`.  Taking the sum of the exact absolute monomial bounds in
`(M,omega,nu)` yields 947 parameter monomials in total.  The five bounds are

```text
B1 = 1040210347071333285995390774300441067433076882959
     /17199267840000000000000000000000000,
B2 = 513625292315565411172470351664061881087569457669
     /28665446400000000000000000000000000,
B3 = 9574969116015939526109085821350045427090716403
     /6370099200000000000000000000000000,
B4 = 34218452213929153632941920549574435172203
     /1592524800000000000000000000000,
B5 = 1012066220495792924792495220066012001
     /530841600000000000000000000.
```

There are two lossless ordinary projective charts.

### Chart C0: `X<=S`

Set `X=S rho`, `0<=rho<=1`.  After dividing `Qhat-H1` by `S^2`, the quadratic
reserve is at least `c0`, while the absolute higher remainder is at most
`sum B_d S^d`.  At `S<=1/10000`, the exact margin is

```text
2157675883946338861464573804693908853416834606352657354865271
/1074954240000000000000000000000000000000000000000 > 0.
```

This chart includes `X=0`; no division by `X` is used.

### Chart C1: `S<=X`

Set `S=X sigma`, `0<=sigma<=1`.  After dividing `Qhat-H1` by `X^2`, the same
quadratic reserve applies and the remainder is at most `sum B_d X^d`.  The
chart works directly through the full range `X<=3/10000`, with exact margin

```text
89361321403752495288011515925096895113866165323668871164167
/44789760000000000000000000000000000000000000000 > 0.
```

Thus C1 contains the previously proved `1/4000<=X<=3/10000` main chart; the
old chart is not needed by this theorem.

Every pair `S>0,X>=0` belongs to C0 or C1.  They overlap exactly along
`X=S`, where `rho=sigma=1`.  Therefore they cover the complete parameter
rectangle stated above.  Since `H1>=0`, both charts prove `Qhat>0`.  Finally
`D>0` and `S>0`, so this is exactly `36 Gamma>0` for the raw gate.

## Verification artifacts

Source verifier, reconstructed from the original Hermitian gate:

```text
tmp/research/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_family.py
```

Independent signed-`z`/Gram referee and audit:

```text
audit/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_family_referee.py
audit/COMMON_METRIC_RANKTWO_TRANSVERSE_COMPACT_BALL_POSITIVE_Z_MOVING_SHEET_FAMILY_REFEREE_AUDIT.md
```

The manifest is

```text
tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_family_manifest.sha256
```
