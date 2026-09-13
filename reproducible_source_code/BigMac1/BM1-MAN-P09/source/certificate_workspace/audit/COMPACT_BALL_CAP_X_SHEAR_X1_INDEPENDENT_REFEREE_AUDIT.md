# Independent referee audit: compact-ball cap x-shear to X=1

## Verdict and exact scope

**PASS. Fatal 0, major 0, minor 0.**

The result has two exact parts.  First, the old chart family
`x=-1/5+X`, `y=3/5+S*y0` cannot be compact-ball legal at `X=1` for any
`S>0` and any `Z>=0`.  Second, the cap chart

```
x = x_old - (3/2)(X-497/500),
y = y_old,
Z = Z_constant + 2(X-497/500)
```

is legal and has a strictly positive raw gate throughout
`497/500 <= X <= 1`, `0<S<=1/10000`, and the frozen `M,omega,nu` box.
This is one charted local theorem.  It is not a theorem for the full compact
ball, unrestricted common metrics, fixed crossing lenses, or arbitrary nodes.

## Independence

The candidate source and source manifest were used only as opaque byte strings
for SHA-256.  They were never imported, executed, parsed, or read for a
specialization, coefficient table, controls, helpers, weakest index, weakest
polynomial, reserve, note, or source log.

The literal-free scout starts from the original signed frame and compact-ball
Hermitian compression.  It uses reversed signed-z Gram columns, an independent
cyclic multiplication of `Q^2`, q-then-z-then-h elimination, the fully
conjugated cyclic raw-gate identity, positive clearing, and a dense u-first
Bernstein conversion.  It contains no frozen structural counts, bidegree,
control count, weakest index, polynomial, or reserve.  All of them were
derived during the successful scout and only then frozen for the formal run.

## Old-family chart no-go

At `X=1`, the old family has `x=4/5` and
`y=3/5+S*y0`, where `y0>0` uniformly on the frozen box.  For an arbitrary
symbolic `Z>=0`, direct expansion gives

```
1-x^2-y^2-Z = -S(6*y0/5+S*y0^2)-Z < 0.
```

Thus no choice `Z>=0` can repair that particular x,y chart family at the
endpoint.  This is a chart-family no-go, not a negative raw gate, a target
counterexample, or a maximality result.

## Cap-chart legality

The cap shear gives

```
791/1000 <= x <= 397/500,
Zmin = 17798406223702873/15857127000000000000 > 0,
Zlower(X=1) = 17995576623934873/15857127000000000000 > 0,
Zupper = 10967/2600000 < 1.
```

The exact uniform bounds

```
T <= -1218219/40625 < 0,
danger_base >= 13993/2600000 > 0
```

imply strict compact-ball danger over the full cell.  The reconstructed
determinant identity `det(C)=(5/9)SZ`, both signed-z lifts, positive scale,
and rank-two gates all pass, including at `X=1`.  The new inputs, cleared raw
gate, and cleared core splice exactly with the audited constant-Z predecessor
at `X=497/500`.

## Exact positivity certificate

The formal reconstruction proves direct compression equals the reversed Gram
sum, all nine `Q^2` entries, equality of the fully conjugated and cyclic raw
gates, radical cancellation, and `deg_Z=4`.  Positive clearing is reversible.

The derived cleared/core/centered term counts are `48/48/2263`; the derived
bidegree in `(S,X)` is `(7,8)`.  Consequently the independently derived
Bernstein table has 72 controls.  All 72 exact centered lower bounds are
strictly positive.  The unique weakest control is `(7,8)`, with reserve

```
79085602723906157917988882974367991904890648543683584180560419945180485170965315227
/239735779200073728000000000000000000000000000000000000000000000000000000.
```

The complete weakest polynomial is printed in both successful exact logs;
its text SHA-256 is
`6510213895aa636f0ef06dd2d903a7b9e6cdf33003d1d6d8c184ce1730a53ccf`.

Seventy-two exact raw-gate nodes were generated from the diagnostic grid only
after the analytic certificate was complete.  Their minimum is strictly
positive, but no node value is used to prove the theorem.

## Adversarial audit and classification

Scout, formal normal, and both `py_compile` checks exit zero.  Eight attacks
were actually run serially and each exits one at its intended exact gate:
optimized Python, bad source, bad manifest, bad predecessor, bad
normalization, dropped `Q^2`, flipped danger, and dropped core support.

No legal negative and no certificate insufficiency were found.  The only
chart illegality is the precisely scoped old-family endpoint no-go.  There
was no resource failure, no numerical-to-theorem promotion, and no reuse of
CE-046/048/059/060.  One pre-freeze run failed closed because a SymPy
derivative was compared before rational cancellation; the corrected exact
comparison passed and this implementation event is not a mathematical
finding.
