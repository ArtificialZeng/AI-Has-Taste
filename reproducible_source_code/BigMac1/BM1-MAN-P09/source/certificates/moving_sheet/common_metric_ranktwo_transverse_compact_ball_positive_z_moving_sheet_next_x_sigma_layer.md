# A sigma-sensitive exact proof on the next positive-`Z` moving-sheet layer

## Honest scope

This note proves one strict adjacent cell of the compact-ball scalar gate.
It does not prove a full positive-`Z` collar, arbitrary normalized scale, the
full compact ball, the unrestricted common-metric theorem, or the optimal
constant of a fixed crossing lens.  The proof does not use CE-046, CE-048,
CE-059, or the CE-060 baseline-remainder route.

## The exact cell

Let

```text
0<S<=1/10000,
1/31<=X<=1/30,
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

Then `lambda>0`, `0<Z<1/8`, the compact-ball point is strictly
dangerous, the transverse compression is positive definite of rank two, and
the original fully conjugated Hermitian `Q,Q^2` scalar gate satisfies

```text
36 Gamma(S,Z,x,y,lambda)>0.
```

The endpoints `X=1/31` and `X=1/30` are included.  The actual theorem has
`S>0`; the closure `S=0` is used only after an exact positive-factor
clearing.  Joined to the preceding closed cell, this proves the same moving-
sheet family on the merged range `0<=X<=1/30`.

## Exact legality and rank

The unchanged bounds give `999/1000<=A<=1001/1000` and `y0>0`.
Uniformly through the new upper endpoint,

```text
wc+omega >= 2549/3700,
wc+omega-S*y0^2
 >= 7639086233111/11088900000000 > 0.
```

Since `3X-X^2>0` on this cell,

```text
Z >= 3X-X^2
     +S*7639086233111/11088900000000
  > 0,

Z <= 100173181/1001000000 < 1/8.
```

The exact danger identity is

```text
x^2+y^2+Z=2/5+(13/5)X+(6/5)Y+W,
```

and yields

```text
1-x^2-y^2-Z
 >= 95037195293/185185000000
 > 1/2.
```

For the original transverse compression `C`, its first leading principal
entry is `S>0` and

```text
det C=(5/9)SZ>0.
```

Thus `C` is positive definite.  Multiplication by `lambda>0` gives a legal
Hermitian positive semidefinite `Q` of rank two.

## Raw-gate reconstruction

The source verifier starts from the original orthonormal transverse frame,
forms the fully conjugated Hermitian matrix `Q`, its square `Q^2`, and the
three leakage terms of the scalar gate.  It eliminates only the exact
relation `q^2=1-h^2` and obtains a quartic in `lambda` with constant term
five.  No predecessor coefficient table or cached quartic is imported.

After setting `lambda=(1+M)/S`, let

```text
N=S^3(36 Gamma).
```

Substitute the moving-sheet map sparsely, multiply by the strictly positive
factor

```text
25^8(1+M)^8,
```

and divide by the exactly verified factor `S^2`.  The resulting quotient has
exactly twenty `(S,X)` monomials and bidegree `(5,4)`.  Its first layer is

```text
H1=152587890625 M^2 S(1+M)^8(5M^2+14M+14)>=0.
```

After removing `H1`, the homogeneous quadratic part is

```text
H2=aS^2+bSX+cX^2,
```

where exact centered-monomial bounds on the full
`(M,omega,nu)` box give `a,b,c>0`.  In particular,

```text
c >= c0
   =2564950982194530478444050838857341987999
    /1274019840000000000000000000 > 0.
```

## The decisive sigma-sensitive remainder

The old global sufficient estimate treated every point of the projective
chart as though `S/X` could equal one.  On the present cell the exact order
is much sharper:

```text
sigma=S/X,
0<sigma<=31/10000.
```

After division by the positive `X^2`, retain `sigma^i` on every monomial
`S^i X^j`.  Exact absolute centered-monomial bounds for all sixteen higher
`(S,X)` terms, comprising 947 parameter monomials, give the uniform total
remainder

```text
Rabs =
46499117573964545715217879542445250542603528830310449624295476899453
/17199267840000000000000000000000000000000000000000000000000.
```

Even if the positive `a sigma^2+b sigma` part of `H2/X^2` is discarded, the
remaining exact margin is

```text
c0-Rabs =
34580339142052196913279468445031671587443896471169689550375704523100547
/17199267840000000000000000000000000000000000000000000000000
>0.
```

Consequently the cleared quotient is strictly positive throughout the
entire closed `X` cell.  Since every divided or cleared factor is strictly
positive on the actual domain, this proves strict positivity of the original
Hermitian gate, not positivity of a surrogate.

## Symmetric falsification audit

The discovery script evaluates the original raw quartic on 72 exact legal
rational nodes: three positive `S` values, both `X` endpoints and their
midpoint, and all eight corners of the `(M,omega,nu)` box.  It finds no
negative value; the exact minimum is positive.  This finite test is not used
as the proof and is not claimed to cover the continuum.

## Artifacts

Exact discovery/falsification script:

```text
tmp/research/compact_ball_positive_z_moving_sheet_next_x_sigma_refined_discovery.py
```

Fail-closed source verifier, reconstructing the fully conjugated gate from
definitions:

```text
tmp/research/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_next_x_sigma_layer.py
```

The source verifier raises immediately under `python -O`.  The result still
requires an independently written referee reconstruction before promotion to
the shared claim ledger or a manuscript.
