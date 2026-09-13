# Independent referee audit: reciprocal moving-sheet endpoint envelope

Date: 2026-08-24.

## Verdict

**PASS as an exact strict partial theorem, with the scope qualifications below.**

For

```text
0<S<=1/10000,
1/30<=X<=1/24,
|M|<=1/1000,
|omega|,|nu|<=1/100,
```

and the displayed moving-sheet map in

```text
tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_reciprocal_endpoint_envelope.md
```

the independent reconstruction proves `lambda>0`, `0<Z<1/8`, strict
danger, rank-two positive definiteness, and strict positivity of the
original fully conjugated Hermitian `Q,Q^2` scalar gate.  Both `X` endpoints
are included.

This is not a full positive-`Z` collar, an arbitrary-scale result, a
full-compact-ball theorem, the common-metric theorem, or a result on the
optimal fixed crossing-lens constant.  The general fixed crossing-lens
problem remains open.

## Independence and reconstruction

The referee verifier

```text
audit/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_reciprocal_endpoint_envelope_independent_referee.py
```

imports no project verifier, coefficient table, certificate, or claimed
rational constant.  Starting from the original vectors `p,r,f,n`, it
independently checks the transverse-frame Gram identities modulo
`q^2=1-h^2`, forms the Hermitian compression, constructs `Q=lambda H` and
`Q^2`, and evaluates every conjugated leakage term in the original gate.
The resulting `36 Gamma` is independently recovered as a quartic in
`lambda` with constant term `5`.

The verifier then composes the moving sheet with a separately implemented
sparse bivariate evaluator.  It does not read the candidate verifier or its
serialized output.

## Legality, danger, and rank at the closing endpoint

The independent exact bounds at `X=1/24` are

```text
A=1+M >= 999/1000 > 0,
wc+omega >= 5061/7400,

wc+omega-S*y0^2
 >= 7583641733111/11088900000000 > 0,

Z <= 277785751/2252250000 < 1/8,

1-x^2-y^2-Z
 >= 273074560879/555555000000 > 0.
```

The last displayed reserve is only a positive reserve; it is strictly less
than `1/2`.  No `>1/2` danger-reserve claim is valid for this cell.

Because `S>0`, `A>0` gives `lambda=A/S>0`.  The transverse compression has
first leading principal entry `S` and the independently verified identity

```text
det C=(5/9)SZ>0.
```

It is therefore positive definite of rank two, and multiplication by
`lambda>0` produces a legal rank-two Hermitian PSD matrix `Q`.

## Exact quotient and sigma envelope

Set `N=S^3(36 Gamma)`, substitute `lambda=(1+M)/S`, apply the moving sheet,
clear the positive factor `25^8(1+M)^8`, and divide by the exact `S^2`
factor.  The referee reconstruction gives:

```text
moving (S,X) support                 20 terms
higher terms after the quadratic    16 terms
centered parameter monomials       947 terms
```

The first layer is exactly

```text
152587890625 M^2 S(1+M)^8(5M^2+14M+14) >= 0.
```

All three centered lower bounds on the quadratic coefficients are positive.
Using the lossless projective bound `sigma=S/X<=3/1000`, the independently
computed higher-term absolute remainder at `X=1/24` is

```text
Rabs =
31997078803545499164155903109724810371375554352899761405136081
/9784472371200000000000000000000000000000000000000000.
```

After discarding the two additional positive quadratic terms, the remaining
strict margin is

```text
19666826464450448575286154539314661657460944445647100238594863919
/9784472371200000000000000000000000000000000000000000
>0.
```

Thus the cleared quotient is strictly positive.  On the actual domain the
relation back to the raw gate divides only by
`25^8(1+M)^8 S>0`, so this certifies the original fully conjugated gate and
not merely a coefficient surrogate.

## Reciprocal endpoint decisions

The verifier recomputed the complete sigma envelope and all legality bounds
at every requested reciprocal endpoint.  No monotonic extrapolation was
substituted for these decisions.

| endpoint | gate envelope | `Z<1/8` cap | strict danger | decision |
|---:|:---:|:---:|:---:|:---:|
| `1/29` | PASS | PASS | PASS | included |
| `1/28` | PASS | PASS | PASS | included |
| `1/27` | PASS | PASS | PASS | included |
| `1/26` | PASS | PASS | PASS | included |
| `1/25` | PASS | PASS | PASS | included |
| `1/24` | PASS | PASS | PASS | included |

The strict gate margin decreases through this tested list but remains
positive at `1/24`.  The `1/24` endpoint therefore closes the requested
reciprocal list.

## Exact `X=1/23` witness and its classification

At

```text
S=1/10000,
X=1/23,
M=1/1000,
omega=1/100,
nu=-1/100,
```

the independently evaluated values are

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

Moreover, the same continuum sigma-envelope calculation still has the
strict positive margin

```text
82404612644559432359220084104229375811726922085336396649287733436359
/41000143395225600000000000000000000000000000000000000000.
```

Therefore `X=1/23` is **solely a lower-`Z` scope failure**.  It is not a
negative gate value, a gate counterexample, a common-metric counterexample,
or a fixed-lens counterexample.

The phrase “maximal reciprocal endpoint” is valid only among the tested
discrete endpoints `1/n` in this moving-sheet family: `1/24` passes and the
immediately next tested reciprocal `1/23` violates the prescribed `Z<1/8`
cap.  Nothing here proves that `1/24` is a sharp boundary in the continuum
of real `X`; no such continuum-maximal claim should be made.

## Endpoints, stitch, and boundary attribution

The previously audited closed cells are

```text
[0,3/10000],
[3/10000,1/31],
[1/31,1/30],
```

and the new cell is `[1/30,1/24]`.  Their manifests verify, their independent
verifiers pass, and the shared endpoints `3/10000`, `1/31`, and `1/30` are
included on both adjoining sides.  Hence the joined moving-sheet statement
has no `X` gap.

The endpoint at `X=0` belongs to the first predecessor's `C0` chart, which
does not divide by `X`.  It is not proved by the reciprocal chart.

The actual parametric theorem always has `S>0`.  At `S=0`,
`lambda=(1+M)/S` is undefined.  The `S=0` point used in coefficient
bookkeeping is only the closure of the positively cleared quotient, not an
original rank-two datum or an additional theorem endpoint.

## Falsification and fail-closed checks

Before issuing PASS, the referee evaluated the original exact raw gate on
72 independently chosen rational nodes spanning `X=1/24`, the midpoint to
`1/23`, `X=1/23`, three positive `S` scales, and all eight corners of the
`(M,omega,nu)` box.  Every value was positive.  The minimum was

```text
9365332625900372158324018774573882679
/40000000000000000000000000000000000 > 0
```

at `(S,X,M,omega,nu)=(1/10000,1/24,-1/1000,-1/100,-1/100)`.
This finite test is falsification evidence only and is not used in the
continuum proof.

Fail-closed behavior was checked separately:

- ordinary exact run: exit `0`, final PASS;
- `python -O`: exit `1` before symbolic work;
- unknown command-line input: exit `2` before symbolic work.

The frozen checkpoint manifest is stale relative to the current workspace:
four listed files fail its August 18 hashes.  It was not used as a clean
release claim.  This audit has a separate manifest binding the candidate
statement, independent verifier, and this report.

No proof assistant was used.  The result is an exact SymPy/rational
computer-assisted partial theorem with a definition-level independent
verifier.
