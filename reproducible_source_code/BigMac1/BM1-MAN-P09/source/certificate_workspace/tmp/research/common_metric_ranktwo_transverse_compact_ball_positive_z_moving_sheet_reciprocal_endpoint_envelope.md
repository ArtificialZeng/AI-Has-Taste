# The reciprocal moving-sheet envelope through `X=1/24`

## Honest scope

This is a strict exact partial theorem for one positive-`Z` moving-sheet
family of the compact-ball scalar gate.  It is not a full positive-`Z`
collar, not an arbitrary-scale result, not the complete compact ball, not the
common-metric theorem, and not the optimal constant of a fixed crossing
lens.  No argument from CE-046, CE-048, CE-059, or CE-060 is used.

## The new closed layer

Let

```text
0<S<=1/10000,
1/30<=X<=1/24,
|M|<=1/1000,
|omega|,|nu|<=1/100.
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

Then `lambda>0`, `0<Z<1/8`, the point is strictly dangerous, the
transverse compression is positive definite of rank two, and the original
fully conjugated Hermitian `Q,Q^2` scalar gate satisfies

```text
36 Gamma(S,Z,x,y,lambda)>0.
```

Both `X` endpoints are included.  The theorem has `S>0`; `S=0` appears only
as the algebraic closure after exact positive-factor clearing.  Together
with the preceding audited cells, the same parametric family is therefore
strictly positive on the joined interval

```text
0<=X<=1/24.
```

## Exact legality and rank

The unchanged parameter estimates give

```text
999/1000<=A<=1001/1000,
wc+omega>=5061/7400.
```

Uniformly on the new layer,

```text
wc+omega-S*y0^2
 >= 7583641733111/11088900000000 >0.
```

As `3X-X^2>0`, this proves `Z>0`.  Keeping the exact negative `-X^2`
at the monotone upper endpoint gives

```text
Z <= 277785751/2252250000 < 1/8.
```

The exact identity

```text
x^2+y^2+Z=2/5+(13/5)X+(6/5)Y+W
```

gives

```text
1-x^2-y^2-Z
 >= 273074560879/555555000000 >0.
```

Finally, the first leading principal entry of the transverse compression
`C` is `S>0` and

```text
det C=(5/9)SZ>0.
```

Thus `C` is positive definite, and multiplication by `lambda>0` yields a
legal rank-two Hermitian PSD matrix `Q`.

## Fully conjugated gate and sigma-sensitive sign proof

The source verifier independently reconstructs the orthonormal transverse
frame, Hermitian `Q`, `Q^2`, all conjugated leakage terms, and the exact
danger scalar.  Eliminating only `q^2=1-h^2` gives the original gate as a
quartic in `lambda` with constant term five.

Set `lambda=(1+M)/S`, let `N=S^3(36 Gamma)`, apply the moving-sheet map
sparsely, multiply by the strictly positive factor

```text
25^8(1+M)^8,
```

and divide by the exactly verified `S^2` factor.  The quotient has exactly
twenty `(S,X)` monomials.  Its first layer is the nonnegative expression

```text
152587890625 M^2 S(1+M)^8(5M^2+14M+14).
```

The quadratic layer is

```text
aS^2+bSX+cX^2,
```

with exact uniform bounds `a,b,c>0`; in particular

```text
c>=c0=
2564950982194530478444050838857341987999
/1274019840000000000000000000.
```

On this cell the lossless projective coordinate has the much smaller range

```text
sigma=S/X,
0<sigma<=3/1000.
```

After dividing by `X^2`, retain every exact factor `sigma^i` in the sixteen
higher `(S,X)` terms.  The 947 centered parameter monomials give the exact
absolute remainder

```text
31997078803545499164155903109724810371375554352899761405136081
/9784472371200000000000000000000000000000000000000000.
```

Discarding the additional positive terms `a sigma^2+b sigma`, the remaining
strict margin is already

```text
19666826464450448575286154539314661657460944445647100238594863919
/9784472371200000000000000000000000000000000000000000
>0.
```

Every cleared or divided factor is positive on the actual domain, so this is
strict positivity of the original Hermitian gate rather than a sufficient
coefficient surrogate.

## Why the next reciprocal endpoint is not included

The same sigma-sensitive gate remainder remains strictly positive at
`X=1/23`, and the datum remains dangerous and rank two.  Nevertheless, the
requested lower-layer condition `Z<1/8` genuinely fails there.  At the exact
legal parameter point

```text
S=1/10000,
X=1/23,
M=1/1000,
omega=1/100,
nu=-1/100,
```

one has

```text
Z=68173435531857725471/530058529000000000000,

Z-1/8=
1916119406857725471/530058529000000000000 >0.
```

The danger reserve and determinant remain positive, and the raw gate at this
point is also exactly positive.  Thus `1/23` is a failure of the prescribed
`Z<1/8` layer scope, not a gate counterexample.  Among the requested
reciprocal endpoints `1/29,...,1/24`, the largest admissible and proved one
is `1/24`; the immediately next reciprocal lies outside the lower-`Z` cap.

## Proof/falsification artifacts

The discovery script tests all requested reciprocal endpoints, the next
endpoint `1/23`, and 32 exact legal raw-gate nodes at the last passing and
first scope-failing endpoints:

```text
tmp/research/compact_ball_positive_z_moving_sheet_reciprocal_endpoint_envelope_discovery.py
```

The fail-closed source verifier reconstructs the fully conjugated raw gate
and the complete exact certificate from definitions:

```text
tmp/research/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_reciprocal_endpoint_envelope.py
```

The finite exact falsification nodes are not used as the continuum proof.
An independently written referee is still required before ledger or
manuscript promotion.
