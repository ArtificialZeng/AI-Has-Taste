# A lossless moving-sheet stitch across `Z=1/8`

## Honest scope

This note proves an exact strict gate-positive chart crossing the artificial
boundary `Z=1/8`.  It is a five-real-parameter moving-sheet partial theorem,
not a full neighborhood of that boundary, not an arbitrary-scale theorem,
not the complete compact ball or common-metric theorem, and not the optimal
constant of a fixed crossing lens.  It uses none of CE-046, CE-048, CE-059,
or CE-060.

## 1. The direct outer-box inclusion is exactly false

The previously audited outer compact box is

```text
-1/4<=x<=1/2,
|y|<=1/2,
1/8<=Z<=3/8,
```

for every displacement and positive scale.  Consider the moving-sheet band

```text
0<S<=1/10000,
1/24<=X<=1/23,
|M|<=1/1000,
|omega|,|nu|<=1/100,
```

with

```text
A       =1+M,
lambda  =A/S,
y0      =12/(25A)+nu,
wc      =-3(5MX-15M+5X-6)/(25A),
Y       =S y0,
W       =S(wc+omega),
Z       =3X-X^2-Y^2+W,
x       =-1/5+X,
y       = 3/5+Y.
```

Its `x` coordinate lies inside the outer interval:

```text
-19/120<=x<=-18/115.
```

But

```text
y0>=46999/100100>0,
y-1/2=1/10+S y0>1/10.
```

The exact closure infimum of the `y` gap is `1/10`; throughout the actual
band the gap is strictly larger.  Hence no subdivision in `X`, `S`, or the
other moving parameters can place even one actual point of this family in
`|y|<=1/2`.  The outer-box theorem therefore cannot supply a direct stitch.
This is a coordinate-coverage obstruction, not a negative gate.

## 2. The recentered cross-cap chart

Retain the lossless moving variables

```text
Y=y-3/5=S y0,
sigma=S/X,
T=Z-1/8.
```

No division by `T` occurs, so both signs of `T` and the exact boundary
`T=0` are covered by one calculation.  On the displayed band,

```text
0<sigma<=3/1250.
```

The theorem is:

> For every parameter point in the band above, `lambda>0`, `Z>0`, the
> compact-ball datum is strictly dangerous, the transverse compression is
> positive definite of rank two, and the original fully conjugated
> Hermitian `Q,Q^2` scalar gate satisfies `36 Gamma>0`.

Together with the preceding audited chart, this extends the same moving-sheet
family to `0<=X<=1/23`, now without imposing `Z<1/8`.

## 3. Exact legality

At the new upper endpoint,

```text
wc+omega>=58109/85100,

wc+omega-S*y0^2
 >=174146537361553/255044700000000>0.
```

Since `3X-X^2>0`, this proves `Z>0`.  A uniform upper bound is

```text
Z<=68106712749/529529000000<1/7.
```

The danger identity

```text
x^2+y^2+Z=2/5+(13/5)X+(6/5)Y+W
```

gives

```text
1-x^2-y^2-Z
 >=6220529775217/12777765000000>0.
```

For the transverse compression `C`, its first leading principal entry is
`S>0` and

```text
det C=(5/9)SZ>0.
```

Thus `C` is positive definite and multiplication by `lambda>0` produces a
legal rank-two Hermitian PSD matrix `Q`.

## 4. Exact gate sign

The source verifier reconstructs the original orthonormal transverse frame,
the fully conjugated `Q`, `Q^2`, the raw leakage vectors, and the danger
scalar from definitions.  After eliminating only `q^2=1-h^2`, the original
gate is a quartic in `lambda` with constant term five.

Set `lambda=(1+M)/S` and `N=S^3(36 Gamma)`.  Apply the moving-sheet map
sparsely, clear the strictly positive denominator

```text
25^8(1+M)^8,
```

and divide by the exactly verified factor `S^2`.  The quotient has twenty
`(S,X)` monomials.  Its first layer is nonnegative, and its quadratic layer

```text
aS^2+bSX+cX^2
```

has exact uniform bounds `a,b,c>0`, including

```text
c>=c0=
2564950982194530478444050838857341987999
/1274019840000000000000000000.
```

After the lossless substitution `S=sigma X` and division by positive `X^2`,
retain every power `sigma^i` in the sixteen higher terms.  Their 947 exact
centered parameter monomials have total absolute remainder

```text
341349404790343639470527055781196276834417458615095418095466792141
/125122507920000000000000000000000000000000000000000000000.
```

Even after discarding the additional positive `a sigma^2+b sigma` terms,
the exact margin is

```text
83854846318555455131346013627095055256473934297852585381468177735953
/41707502640000000000000000000000000000000000000000000000
>0.
```

Every cleared and divided factor is positive on the actual domain.  Hence
this is strict positivity of the original Hermitian gate, not a sign claim
about a surrogate polynomial.

## 5. Exact crossing witnesses

The same closed chart contains legal points on both sides of `Z=1/8`.

At

```text
S=1/10000, X=1/24,
M=-1/1000, omega=-1/100, nu=1/100,
```

one has

```text
Z=13676193016733111/110889000000000000,

Z-1/8=-184931983266889/110889000000000000<0.
```

At

```text
S=1/10000, X=1/23,
M=1/1000, omega=1/100, nu=-1/100,
```

one has

```text
Z=68173435531857725471/530058529000000000000,

Z-1/8=1916119406857725471/530058529000000000000>0.
```

Both points have positive scale, positive determinant, strict danger, and an
exactly positive original gate.  Since the full connecting parameter band is
proved strictly positive without dividing by `T`, this is a lossless stitch
across the cap rather than two disconnected point checks.

## 6. Artifacts and remaining scope

Discovery, inclusion certificate, and a 72-node exact falsification audit:

```text
tmp/research/compact_ball_positive_z_moving_sheet_cross_z_cap_stitch_discovery.py
```

Fail-closed source verifier:

```text
tmp/research/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_cross_z_cap_stitch.py
```

The finite node audit is not used as continuum proof.  The outer-box `y` gap
remains real: this theorem bridges `Z=1/8` only inside the narrow recentered
moving-sheet family.  An independently written referee is required before
shared-ledger or manuscript promotion.
