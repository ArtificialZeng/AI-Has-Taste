# Independent referee audit: adjacent-`X` positive-`Z` moving sheet

Date: 2026-08-23  
Verdict: **PASS as an exact strict partial theorem.**

The result does not prove the full compact-ball quartic, the common-metric
theorem, or the optimal constant of a fixed crossing lens.

## Bound statement

The audited theorem note is

```text
tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_adjacent_x_layer.md
```

with SHA-256

```text
95028dc46a177a8e856200eaba3f954086d6b4335aef34efac6be09783e39e92.
```

For

```text
0<S<=1/10000,
3/10000<=X<=1/31,
|M|<=1/1000,
|omega|,|nu|<=1/100,
```

and the exact parameter map printed in that note, the original Hermitian
`Q,Q^2` scalar gate satisfies `36 Gamma>0`.  The parameters are legal,
`lambda>0`, `0<Z<1/8`, the datum is strictly dangerous, and `Q` has positive
rank two.  Stitching with the independently certified predecessor cell gives
the same conclusion for `0<=X<=1/31`, with all the other quantifiers
unchanged.

## Isolated reconstruction

The referee verifier is

```text
audit/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_adjacent_x_layer_independent.py
```

with SHA-256

```text
e793ae55e0ed30f862ca20101aa8c2b54080f78219ad97ecbd97fbfcc751a6a5.
```

It imports no discovery module, source verifier, serialized certificate, or
cached coefficient table.  Starting from the original definitions it:

1. reconstructs the orthonormal transverse frame modulo
   `q^2=1-h^2`, its kernel vector, and the Hermitian compression;
2. proves directly that the compression determinant is `(5/9)h^2 Z`;
3. reconstructs the original gate from `Qp` and the two cyclic `Q^2`
   entries;
4. reconstructs the same gate independently as the norm square of its
   constant, linear, and quadratic Gram-vector pieces;
5. substitutes the exact moving-sheet map term by term into the newly
   generated raw polynomial and verifies the positive clearing
   `36 Gamma=Qhat/[25^8(1+M)^8 S]`;
6. generates the complete 20-term `(S,X)` quotient anew and recomputes all
   947 centered parameter monomials used in the continuum bound.

No floating-point value enters an acceptance decision.

## Legality and rank

Writing `A=1+M`, the closed parameter box gives `A>=999/1000>0`; because
`S>0`, `lambda=A/S>0`.  The verifier independently derives

```text
wc+omega >= 79093/114700,

Z >= 3X-X^2
     + S*(237033451226441/343755900000000) > 0,

Z <= 3005268611/31031000000 < 1/8,

1-x^2-y^2-Z
 >= 8886607262249/17222205000000 > 1/2.
```

The first leading compression entry is `S>0` and

```text
det C=(5/9)SZ>0.
```

Thus `C` is positive definite.  The transverse frame is an isometry and
`lambda>0`, so the original Hermitian `Q` is positive semidefinite of rank
two.  Since the gate depends on the compact coordinate only through
`Z=z^2`, both signs of `z` are included.

## Continuum sign and projective chart

The freshly reconstructed degree-one layer factors as a positive rational
multiple of

```text
M^2(1+M)^8(5M^2+14M+14),
```

and is nonnegative; the last quadratic factor equals
`5(M+7/5)^2+21/5`.  The three degree-two coefficients have a common exact
lower reserve

```text
2564950982194530478444050838857341987999
/1274019840000000000000000000 > 0.
```

For the adjacent cell,

```text
0<S<=1/10000<3/10000<=X,
```

so `S=X sigma` with `0<sigma<1` is lossless and division by `X^2` is legal.
The centered absolute remainder bound is monotone in `X`; its exact worst
margin at `X=1/31` is

```text
42950357876463827039627477692165648038556445276911579
/984800872161607680000000000000000000000000 > 0.
```

This proves the continuum, not a finite grid.  The verifier also reconstructs
the predecessor C0 and C1 margins from the same raw gate:

```text
C0, X<=S:
2157675883946338861464573804693908853416834606352657354865271
/1074954240000000000000000000000000000000000000000 > 0,

C1, S<=X:
89361321403752495288011515925096895113866165323668871164167
/44789760000000000000000000000000000000000000000 > 0.
```

The predecessor and adjacent closed cells both contain `X=3/10000`, so the
stitch has no gap.

## Zero and endpoint audit

- `X=0` is included only through the predecessor C0 chart; that chart divides
  by `S^2`, not by `X`, and `S>0`.
- `S=0` is not part of either theorem and cannot be added by continuity,
  because `lambda=(1+M)/S` is undefined there.  Algebraic coefficient
  extraction at `S=0` is not a geometric endpoint claim.
- `X=3/10000` and `X=1/31` are included.  All four parameter boxes are
  closed, and the lower bounds above hold at every sign endpoint.
- `Z=0`, `A=0`, and loss of rank are excluded by strict rational reserves.

The displayed theorem statement is mathematically acceptable.  For future
manuscript use, the merged conclusion should retain the explicit qualifier
`0<S<=1/10000`; an optional clarifying sentence is: “The endpoint `X=0` is
handled by predecessor chart C0, while `S=0` is outside the parameterization.”

## Attack at `X=1/30`

The inherited absolute-remainder margin at `X=1/30` is exactly

```text
-3902147921357110886357029674143626227976364394263
/171992678400000000000000000000000000000 < 0.
```

This is the sign of a sufficient lower bound, not of `36 Gamma`.  A separate
finite falsification run evaluated 32 exact legal parameter corners at
`X=1/31` and `X=1/30` and found zero negative original-gate values.  That
finite result does not certify the continuum at `X=1/30`; the latter remains
open.  No counterexample is recorded.

## Fail-closed tests and raw result

Environment: Python 3.11, SymPy 1.14.0.  The ordinary verifier exits zero.
It rejects `python -O` before importing SymPy and rejects a missing or
hash-mismatched theorem statement.  The decisive output is

```text
PASS standalone reconstruction of original Hermitian Q,Q^2 gate
PASS independent vector-quartic cross-check and lossless clearing
PASS continuous centered-box remainder certificate
PARAMETER_MONOMIALS_RECOMPUTED 947
PASS merged 0<=X<=1/31 with closed stitch at X=3/10000
PASS lambda>0, 0<Z<1/8, danger reserve>1/2, rank-two PSD
PASS X=0 belongs only to predecessor C0; S=0 is not in domain
RESULT=PASS exact strict raw 36Gamma on the stated merged family
SCOPE=partial moving-sheet theorem; no full compact-ball claim
```

The route uses none of CE-046, CE-048, CE-059, the rejected universal
allocation `s=-2`, or numerical SDP inference.  No proof assistant was used.
