# Independent audit: affine-omega tilted moving sheet

Date: 2026-08-24. Verdict: **PASS as an exact partial-theorem candidate**, 
subject to root replay. The audit does not authorize a full compact-ball,
common-metric, or fixed-lens claim.

## Audited scope

The claimed closed chart is

```text
1/5<=X<=3/13,
0<S<=1/10000,
|M|<=1/1000,
|omega|,|nu|<=1/100,
omega_phys=omega-(10636/275)(X-1/5).
```

All centered parameters, every positive scale, and both signs of the real
lift `z=+-sqrt(Z)` are quantified. The left endpoint is the exact seam with
the predecessor centered sheet. The right endpoint remains strictly inside
the compact-ball chart.

## Independence of implementation

The referee is a standalone no-cache program. It imports neither discovery
script, source verifier, predecessor verifier, nor serialized polynomial or
control table. Its dependency hashes bind only the frozen analytic notes and
the frozen source file.

The referee reconstruction order is deliberately different:

1. Build the signed-`z` Gram columns and an independently oriented kernel.
2. Form `H=UCU*`, `Q=lambda H`, `Q^2`, and the literal fully conjugated gate.
3. Rebuild the Gram-vector gate with permuted constant/linear/quadratic
   components and prove exact equality with the literal gate.
4. Substitute the tilted affine sheet directly into the gate and clear the
   exact positive denominator; no sparse source map is used.
5. Convert to Bernstein controls using a dense tau-first transform followed
   by the seam variable, rather than the source's nested sparse conversion.
6. Bound each control by an independently implemented centered absolute
   estimate and rebuild legality in a different order.

## Exact agreement

The source reports 134 terms before the moving substitution. After their
respective sparse and direct-affine reconstructions, source and referee
independently return the following identical decisive data:

```text
quotient/higher/centered-monomial counts: 22/18/1013,
Bernstein bidegree: (5,7),
strict controls: 48/48,
minimum control index: (0,0),
strict reserve:
2564950982194530478444050838857341987999
/31850496000000000000000000000,

Z lower:
8879008598718934873/15857127000000000000,
Z upper:
8316795197/13013000000,
endpoint Tmax: -1/100,
endpoint danger lower bound: 1/1000000,
exact legal nodes: 72/72.
```

The source uses a sparse moving quotient; the referee obtains the same 22
terms by direct affine expansion. Both isolate the identical nonnegative
first layer

```text
25^8 M^2 S (1+M)^8 (5M^2+14M+14).
```

The strict reserve belongs to the remaining quotient and therefore proves
strict gate positivity even where the first layer vanishes.

The exact endpoint data also agree:

```text
left seam 36 Gamma =
213355344357890421512795094325969057679
/40000000000000000000000000000000000,

right endpoint 36 Gamma =
184421770823082033734271204948812328298851568079
/16726464040000000000000000000000000000000000.
```

At the maximal danger corner of `X=3/13`, both implementations verify
`danger=1/1000000`, positive `Z`, positive determinant, and positive original
gate. There are no exact negative nodes.

## Legality and boundary classification

The signed-`z` compression has

```text
det C=(5/9)SZ>0,
0<Z<1,
lambda=(1+M)/S>0.
```

The exact danger calculation proves the stronger uniform statement
`D>=S/100>0`, including the closed endpoint. Thus the chart contains no
danger-boundary point. Separately, the original definitions imply

```text
lim_(S->0+) D = 3/5-(13/5)X.
```

It is negative for every `X>3/13`; therefore a bounded center independent of
`S` cannot continue scale-uniform strict danger past this endpoint. This is a
legality obstruction and not a negative raw gate or counterexample. In
particular `X=1/4` remains outside this route.

## Fail-closed matrix

Both source and referee pass normal exact execution and external-cache
`py_compile`. Both reject:

```text
python -O,
an intentionally bad dependency hash,
an intentionally deleted quotient term.
```

Every attack returns nonzero. Direct `shasum -a 256 -c` succeeds for the
source-freeze, theorem, and independent-referee manifests.

## Frozen executable hashes

```text
50c81b2ce85f5d162844a477e329d79301b1e54facbddd9f4b6506446a00992f
tmp/research/verify_common_metric_ranktwo_transverse_compact_ball_affine_omega_tilt_extension.py

becc0405facab40e95aac34e718453010bb18fea29c8ab73e69657157d9a1acd
tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_affine_omega_tilt_extension_independent_referee.py
```

No CE-046/048/059/060 route, sampled SDP, dropped complex phase, or
real-part monotonicity is used. No proof assistant was used. The theorem is
only the stated affine-tilted five-real-parameter slice and makes no
maximality claim for the raw gate.
