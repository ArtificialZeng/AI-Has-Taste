# An adjacent positive-`Z` moving-sheet `X` layer

## Honest scope

This is an exact strict partial theorem for one moving-sheet family of the
compact-ball scalar gate.  It extends the already audited family in the
`X` direction, but it is not a full positive-`Z` collar, not an
arbitrary-scale theorem, not the full compact ball, not the common-metric
theorem, and not the optimal constant of a fixed crossing lens.

The proof below depends on the independently audited raw-gate reconstruction
and sparse quotient identity in

```text
tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_family.md
```

and replays that source verifier before checking the new layer.

## Statement

Let

```text
0<S<=1/10000,
3/10000<=X<=1/31,
|M|<=1/1000,
|omega|,|nu|<=1/100.
```

Put

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

Then `lambda>0`, `0<Z<1/8`, the compact-ball datum is strictly
dangerous, the transverse compression is positive definite of rank two,
and the original Hermitian `Q,Q^2` scalar gate satisfies

```text
36 Gamma(S,Z,x,y,lambda)>0.
```

Joining this adjacent cell with the predecessor theorem gives the same
conclusion on the merged interval

```text
0<=X<=1/31.
```

The two closed `X` cells meet at `X=3/10000`, so no gap or limiting argument
is used in the stitch.

## Exact legality

The predecessor bounds on `A` and `y0` remain unchanged.  At the new upper
endpoint `X=1/31`, the exact uniform lower bound for `wc+omega` is

```text
79093/114700.
```

Since `3X-X^2>=0` on the displayed interval,

```text
Z >= 3X-X^2
     +S * 237033451226441/343755900000000
  > 0.
```

The simple upper bound is

```text
Z <= 3005268611/31031000000 < 1/8.
```

The exact danger identity

```text
x^2+y^2+Z = 2/5+(13/5)X+(6/5)Y+W
```

gives the strict reserve

```text
1-x^2-y^2-Z
 >= 8886607262249/17222205000000
 > 1/2.
```

For the original transverse compression `C`,

```text
det C=(5/9)SZ>0,
```

and its first leading principal entry is `S>0`.  Thus `C` is positive
definite; multiplying by `lambda>0` gives a legal Hermitian PSD matrix `Q`
of rank two.

## Exact sign certificate

The predecessor source reconstructs the original Hermitian `Q,Q^2` gate and
proves, after the same positive denominator clearing and removal of the
nonnegative first layer,

```text
Qhat-H1 = H2+R,
H2 >= c0(S^2+SX+X^2),
```

where

```text
c0 = 2564950982194530478444050838857341987999
     /1274019840000000000000000000 > 0.
```

It also binds the five exact absolute remainder bounds `B_d` printed in the
predecessor theorem.  Throughout the adjacent cell one has

```text
S<=1/10000<3/10000<=X,
```

so the single projective chart

```text
S=X sigma,       0<sigma<=1
```

is lossless.  After division by the positive `X^2`, the exact lower margin at
the worst allowed radius `X=1/31` is

```text
42950357876463827039627477692165648038556445276911579
/984800872161607680000000000000000000000000
>0.
```

Therefore the cleared quotient is strictly positive, and every clearing
factor is strictly positive.  This proves strict positivity of the original
`36 Gamma`, not merely positivity of a coefficient surrogate.

## Next discriminating boundary

Without changing any of the global absolute remainder bounds, the same
sufficient margin at `X=1/30` is exactly

```text
-3902147921357110886357029674143626227976364394263
/171992678400000000000000000000000000000 < 0.
```

This is only a failure of the inherited absolute-remainder certificate.  It
is **not** a negative value of the original gate, and it is not entered as a
counterexample.  The actual gate at and beyond that radius remains open to a
sharper signed remainder, subdivision, or an exact legal negative search.

## Fail-closed source verifier

```text
tmp/research/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_adjacent_x_layer.py
```

The verifier first replays the predecessor's raw Hermitian source
reconstruction and exact 20-term quotient, then checks all new rational
legality reserves, the joined interval, the strict projective margin, and the
certificate-only failure at `X=1/30`.  It raises immediately under
`python -O`.
