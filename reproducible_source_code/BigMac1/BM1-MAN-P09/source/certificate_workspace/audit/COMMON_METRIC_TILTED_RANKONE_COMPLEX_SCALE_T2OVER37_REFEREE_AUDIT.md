# Referee audit: complex-scale half-width `2/37`

Date: 2026-08-24. Verdict: **PASS — independently reconstructed exact
computer-assisted partial theorem**.

The unrestricted complex Hermitian gate, the general common-metric theorem,
and the fixed crossing-lens problem remain open. This audit certifies only the
box and legal scale half-lines quantified below.

## 1. Audited quantifiers

Fix `a=3/5`, `c=4/5`. The theorem holds simultaneously for every

```text
ell in [8,10],
w   in [-31/100,-29/100],
k   in [-301/100,-299/100],
z   in [-101/100,-99/100],
r   in [99/100,103/100],
t   in [146/37,150/37].
```

The `r` interval is proved by two closed exact cells

```text
[99/100,101/100] and [101/100,103/100].
```

Both cells include `r=101/100`; there is no uncovered seam. With

```text
Delta = r*t-z^2-w^2,
n     = t*(k^2+ell^2)+r-2*(k*z+ell*w),
g     = (12/25)*ell-z*k-w*ell-t,
```

the audited strict scale quantifier is every `T>0` if `g<=0`, and every
`T>Delta*g/n` if `g>0`. The closure endpoint `T=0` in the first branch and
`T=Delta*g/n` in the second branch are also proved strictly positive for the
cleared gate. Thus the theorem does not rely on sampling `T`.

## 2. Independent reconstruction

The referee program imports neither the source verifier nor the discovery
program. It reconstructs from the fully conjugated original Hermitian gate:

1. the rank-two zero-Schur-complement boundary matrix;
2. the exact legal `T` half-line;
3. the cubic `P(T)=4*Delta^2*G(Q)` and an independent residual-square form;
4. the seven terminal polynomials `danger, Delta, n, C0, C1, N0, N1`;
5. both `t=4` Bernstein tensors, including exact inverse reconstruction to the
   source polynomials, with `40,595` controls per `r` cell;
6. every absolute `t`-derivative majorant on the wider interval
   `[146/37,150/37]`;
7. all fourteen exact reserves `m-(2/37)M`.

All fourteen reserves are strictly positive. The unique finite ratio
bottleneck is lower-cell `N0`:

\[
 \rho_{\rm new}=
 \frac{2415423075934055837934601667899895734740928}
 {44380382719614145653999391003570131384913075},
 \qquad \frac2{37}<\rho_{\rm new}<\frac1{18}.
\]

The requested comparison is checked directly and exactly:

\[
 \frac1{19}<\frac2{37}<
 \frac{86248707481421051963533451880821625580096}
 {1582706318973118826676839520618941084666525}.
\]

The old frozen radius is not extrapolated: its audited center minima are
reconstructed at `t=4`, while every derivative bound used for the new theorem
is recomputed on the full wider box.

## 3. Terminal completeness and adversarial checks

The terminal dependency closure contains exactly all seven signs:

```text
danger, Delta, n                         -> legality
Delta, n, C0, C1                        -> g<=0 coefficients
Delta, n, N0, N1                        -> g>0 endpoint and slope
Delta, n                                -> g>0 curvature
```

No discriminant, `N_D`, real-part monotonicity, phase absorption, CE-046,
CE-048, CE-059, or floating-point sign is used.

The independent falsification track evaluated all `96` endpoint combinations
of `ell,w,k,z,t` and the three stitched `r` values. Exactly `48` lie in `g>0`
and `48` in `g<=0`. Every case passed its legal endpoint checks and a direct
original-gate check at `T=1`; the least attacked gate was

\[
 \frac{106696452910593980743701983}
 {45360697639860100000000}>0.
\]

This finite attack is diagnostic only. Continuum coverage comes from the two
exact Bernstein tensors and the fourteen derivative reserves.

At the new upper endpoint the audit also verifies a strictly legal witness
whose two imaginary matrix coordinates have product `-279/100` and for which

\[
 4\{\mathcal G(Q)-\mathcal G(\operatorname{Re}Q)\}
 =-\frac{12024664566834413421}{7748581070000000}<0.
\]

Consequently both phases remain live; replacing the Hermitian datum by its
real part would change the gate in the wrong direction.

## 4. Reproducibility and failure behavior

Normal exact run:

```text
.venv/bin/python -B \
  audit/verify_common_metric_tilted_rankone_complex_scale_t2over37_referee.py
```

Independent normal runs succeeded under Python/SymPy `3.13.5/1.13.3`; the
source calculation was also reproduced under the project environment
`3.11.15/1.14.0`.

The referee fails closed under optimized Python, a forged dependency hash,
and a dropped terminal sign. The source verifier independently exhibits the
same three failure modes. The referee verifier hash is

```text
8663b08b9b90bb2133f2783d22297b62edc9c710b07942c68069eac40a3660f2
```

## 5. Scope

This result enlarges one seven-real-parameter complex Hermitian island from
`|t-4|<=1/19` to `|t-4|<=2/37`. It does not prove the unrestricted complex
Hermitian gate, an arbitrary common metric, the fixed crossing-lens theorem,
or any arbitrary-node statement.
