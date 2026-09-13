# Independent referee audit: continuous moving-sheet cross-`Z` cap stitch

Date: 2026-08-24.

## Verdict

**PASS as an exact strict partial theorem.**

For every

```text
0<S<=1/10000,
1/24<=X<=1/23,
|M|<=1/1000,
|omega|,|nu|<=1/100,
```

with the moving-sheet definitions in

```text
tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_cross_z_cap_stitch.md,
```

the independent reconstruction proves `lambda>0`, `0<Z<1/7`, strict
danger, positive-definite rank-two transverse compression, and strict
positivity of the original fully conjugated Hermitian `Q,Q^2` scalar gate.

This is a genuine continuum theorem on the whole displayed parameter band.
It is not a full neighborhood of `Z=1/8`, not arbitrary in scale, not the
complete compact ball or common-metric theorem, and not a result on the
optimal constant of a fixed crossing lens.  Those larger problems remain
open.

## Independent reconstruction

The referee verifier is

```text
audit/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_cross_z_cap_stitch_independent_referee.py.
```

It imports no source verifier, discovery program, cached polynomial,
coefficient table, or claimed rational constant.  From the original vectors
`p,r,f,n`, it independently reconstructs:

1. the transverse-frame Gram identities modulo `q^2=1-h^2`;
2. the Hermitian transverse compression and its kernel;
3. `Q=lambda H`, `Q^2`, and all fully conjugated leakage terms;
4. the original `36 Gamma` quartic in `lambda`, with constant term `5`;
5. the cleared moving-sheet quotient and its centered-box envelope.

Recentring with `Z=T+1/8` leaves a polynomial in `T` with only a fixed
nonzero numerical denominator.  The proof itself composes the original
moving sheet directly and never divides by `T`.

## Exact outer-box exclusion

The moving `x` range is

```text
-19/120 <= x <= -18/115,
```

which lies inside the outer box's `[-1/4,1/2]` interval.  However,

```text
y-1/2 = 1/10+S*y0,
y0 >= 46999/100100 > 0.
```

Hence every actual point, where `S>0`, satisfies

```text
y-1/2 > 1/10.
```

The exact closure infimum is `1/10`; it is approached only as `S` tends to
zero and is never attained in the actual parameter domain.  The exact upper
bound recorded by the independent verifier is

```text
y-1/2 <= 33316333/333000000.
```

Thus no subdivision of this family can put an actual point into the outer
box condition `|y|<=1/2`.  This is only a coordinate-coverage obstruction,
not a negative gate value.

## Full-band legality and rank

The independent exact bounds are

```text
A=1+M >= 999/1000 > 0,

wc+omega >= 58109/85100,

wc+omega-S*y0^2
 >= 174146537361553/255044700000000 > 0,

Z <= 68106712749/529529000000 < 1/7,

1-x^2-y^2-Z
 >= 6220529775217/12777765000000 > 0.
```

Since `X>=1/24`, the term `3X-X^2` is strictly positive.  The second bound
therefore gives `Z>0`.  Also `lambda=A/S>0` because `S>0`.

The transverse compression has first leading principal entry `S` and the
independently verified identity

```text
det C=(5/9)SZ>0.
```

It is positive definite of rank two, and multiplication by `lambda>0`
produces a legal rank-two Hermitian PSD matrix `Q`.

## Lossless continuum gate certificate

After setting `lambda=(1+M)/S`, define `N=S^3(36 Gamma)`.  Direct sparse
composition of the moving sheet, clearing `25^8(1+M)^8`, and division by
the exactly verified `S^2` factor gives a quotient with

```text
20 (S,X) terms,
16 higher terms after the quadratic layer,
947 centered (M,omega,nu) monomials.
```

Its first layer is exactly the nonnegative expression

```text
152587890625 M^2 S(1+M)^8(5M^2+14M+14).
```

All three centered lower bounds on the quadratic coefficients are positive;
the `X^2` reserve is

```text
c0 =
2564950982194530478444050838857341987999
/1274019840000000000000000000.
```

For every point in the full band, the unique projective coordinate

```text
sigma=S/X
```

satisfies

```text
0<sigma<=3/1250.
```

After the lossless substitution `S=sigma X` and division by positive `X^2`,
the sixteen higher terms have the exact absolute bound

```text
Rabs =
341349404790343639470527055781196276834417458615095418095466792141
/125122507920000000000000000000000000000000000000000000000.
```

Even after discarding the other two positive quadratic contributions, the
remaining strict margin is

```text
83854846318555455131346013627095055256473934297852585381468177735953
/41707502640000000000000000000000000000000000000000000000
>0.
```

This estimate uses the uniform bounds `sigma<=3/1250` and `X<=1/23` on
every higher monomial.  It therefore proves the continuum for all
`1/24<=X<=1/23`; it is not interpolation from endpoint samples.  Since all
cleared/divided factors are positive and there is no division by `T`, both
signs of `Z-1/8` and `Z=1/8` itself are covered by the same proof.

## Exact witnesses on both sides of the cap

At

```text
S=1/10000, X=1/24,
M=-1/1000, omega=-1/100, nu=1/100,
```

the independent values are

```text
Z = 13676193016733111/110889000000000000,

Z-1/8
  = -184931983266889/110889000000000000 < 0,

1-x^2-y^2-Z = 545608753/1110000000 > 0,

det C
  = 13676193016733111/1996002000000000000000 > 0,

36 Gamma
  = 9365830377568041224106345521801146679
    /40000000000000000000000000000000000 > 0.
```

At

```text
S=1/10000, X=1/23,
M=1/1000, omega=1/100, nu=-1/100,
```

one has

```text
Z = 68173435531857725471/530058529000000000000,

Z-1/8
  = 1916119406857725471/530058529000000000000 > 0,

1-x^2-y^2-Z = 8005914089/16445000000 > 0,

det C
  = 68173435531857725471/9541053522000000000000000 > 0,

36 Gamma
  = 18787436399685005999560713886421176269952340879
    /73441472040000000000000000000000000000000000 > 0.
```

The parameter box is connected, and a straight path between these two
witnesses stays inside it.  The moving map is continuous, so the opposite
signs imply an intervening point with `Z=1/8`.  More importantly, the exact
continuum envelope above already proves every point of the full band,
including that crossing.  This is therefore a continuous cross-cap theorem,
not the old `X=1/24` theorem joined to one positive point at `X=1/23`.

The preceding independently audited reciprocal-envelope cell includes
`X=1/24`; its manifest verifies.  Hence the closed stitch there extends the
same moving-sheet family, with the new theorem removing the `Z<1/8`
restriction on `[1/24,1/23]`.

## Falsification and fail-closed behavior

Before PASS, the referee evaluated the original exact raw gate at 72
rational nodes: three positive `S` scales, both `X` endpoints and their
midpoint, and all eight corners of the `(M,omega,nu)` box.  Every value was
positive.  The exact minimum was

```text
9365332625900372158324018774573882679
/40000000000000000000000000000000000 > 0
```

at `(S,X,M,omega,nu)=(1/10000,1/24,-1/1000,-1/100,-1/100)`.
These samples are falsification evidence only and are not used in the
continuum proof.

Fail-closed checks:

- normal exact run: exit `0`, final PASS;
- `python -O`: exit `1` before symbolic reconstruction;
- unrecognized command-line input: exit `2` before symbolic reconstruction;
- candidate source manifest: all six entries verify;
- independent predecessor audit manifest: all three entries verify.

The final independent audit manifest binds the candidate statement, the
standalone referee verifier, and this report.  No shared ledger, portfolio,
dispatch file, or manuscript was modified.

No proof assistant was used.  This is an exact rational/SymPy
computer-assisted partial theorem with a definition-level independent
verifier.
