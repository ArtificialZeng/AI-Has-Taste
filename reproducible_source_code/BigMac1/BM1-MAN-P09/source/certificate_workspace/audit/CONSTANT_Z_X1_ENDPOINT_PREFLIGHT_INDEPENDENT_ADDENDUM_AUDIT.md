# Independent addendum: constant-Z endpoint preflight at X=1

## Verdict

**PASS. Fatal 0, major 0, minor 0 for this addendum.**

This addendum supersedes only the `X=1` endpoint-preflight discussion in
`COMMON_METRIC_RANKTWO_TRANSVERSE_COMPACT_BALL_INWARD_Z_CONSTANT_LIFT_X497_500_INDEPENDENT_REFEREE_AUDIT.md`.
The earlier discussion accidentally tested the old recentered-chart danger
formula.  It did not audit the frozen constant-Z endpoint preflight.  The
local theorem on `99/100 <= X <= 497/500`, its exact Bernstein certificate,
and its PASS verdict are unaffected.

## Independence boundary

The frozen endpoint-preflight source and its four-entry manifest were used
only as opaque byte strings for SHA-256:

- source: `18fbd9ab9937b9700db7ad87e3c1edefaec76f8657c750606452f9a9f7e393bb`;
- manifest: `128cbea09b378a24e4a60997695bad51c66118f63da5b645857e270f878c5533`.

The source, manifest, note, source log, and source output were not imported,
executed, parsed, or read for formulas or claims.  The reconstruction uses
the original compact-ball sheet, compression determinant, and frozen
predecessor/reduction definitions.

## Exact reconstruction

Let

```
X* = 1019767/1040000,
anchor = 83059/100000,
Zconst = Zold + 2(X* - anchor).
```

The independent shift is `779767/2600000`.  At `X=1`, `S=0`,

```
Zconst = -20233/2600000 < 0.
```

The original parameter formula gives `y0>0` and a uniformly negative
`b` at `X=1`.  Exact derivatives show that the lower corner over
`0<S<=1/10000` and the frozen `M,omega,nu` box is attained at
`S=1/10000`, `M=-1/1000`, `omega=-1/100`, `nu=1/100`, where

```
Zconst = -172289947376065127/15857127000000000000 < 0.
```

In fact `Zconst<0` throughout the positive-S endpoint box.

Reconstructing the original two-by-two compression gives

```
det(C) = S*(5/9)*Zconst,
det(C)/S = (5/9)*Zconst < 0.
```

At the lower corner the coefficient is

```
-172289947376065127/28542828600000000000.
```

Thus the endpoint obstruction is exactly constant-Z chart illegality through
negative `Z` and negative `det(C)`.

## Danger and root bracket

Danger is not the endpoint obstruction.  The independent identity is

```
D = Dbase - S*T,
Dbase(X=1) = 20233/2600000 > 0,
T <= -432183/14300 < 0.
```

Hence `D>Dbase>0` for every positive `S` in the endpoint box.

For the exact lower-corner `Z` function,

```
Zlower(497/500)
  = 17798406223702873/15857127000000000000 > 0,
Zlower(199/200)
  = -13803700407925127/15857127000000000000 < 0.
```

Its derivative is strictly negative on this interval, so its unique positive
crossing satisfies

```
497/500 < root < 199/200.
```

## Claim discipline and fail-closed gates

Negative `Z` makes the constant-Z chart illegal.  It is not evidence of a
negative raw gate, a Bernstein failure, maximality of `497/500`, a full-ball
or common-metric obstruction, or a reuse of CE-046/048/059/060.

The final script and `py_compile` exit zero.  Optimized Python, a bad opaque
source hash, and a bad opaque manifest hash were each actually run and exit
one at their intended gates.  Internal changed-shift and flipped-determinant
sentinels are also rejected.  Two pre-freeze implementation attempts used an
unsimplified SymPy direct equality and failed closed; after replacing it with
exact rational cancellation, the final frozen run passes.  Those events were
implementation diagnostics, not mathematical findings.
