# Referee audit: complex-scale half-width `13/239`

Date: 2026-08-24. Verdict: **PASS — independently reconstructed exact
computer-assisted partial theorem**.

The unrestricted complex Hermitian gate, common-metric theorem, arbitrary-node
bridge, and fixed crossing-lens problem remain open. This audit certifies only
the stated local box and its complete legal scale half-lines.

## 1. Quantifiers and result

Fix `a=3/5`, `c=4/5`. The gate is strictly positive for every

```text
ell in [8,10],                 w in [-31/100,-29/100],
k   in [-301/100,-299/100],   z in [-101/100,-99/100],
r   in [99/100,103/100],      t in [943/239,969/239],
```

and every legal scale `T`: `T>0` when `g<=0`, and `T>Delta*g/n` when `g>0`.
The applicable closure endpoint is also strictly positive for the cleared
gate.  The `r` interval is the union of two closed cells meeting at
`r=101/100`, so the seam is covered twice rather than omitted.

## 2. Definition-level reconstruction

The referee imports neither the source verifier nor discovery code. Starting
from the fully conjugated original Hermitian gate it reconstructs:

1. the Hermitian rank-two zero-Schur-complement boundary;
2. the complete legal `T` half-line;
3. `P(T)=4*Delta^2*G(Q)` as a cubic, and a second phase-retaining residual-
   square expression for the same polynomial;
4. the seven terminal signs `danger,Delta,n,C0,C1,N0,N1` and their complete
   dependency DAG;
5. both exact `t=4` center tensors;
6. all seven fresh `t`-derivative majorants on `[943/239,969/239]`;
7. all fourteen exact `m-(13/239)M` reserves, with the derivative
   majorants freshly recomputed on `[943/239,969/239]` rather than inherited
   from the narrower box.

The center tensors use an independent nodal method. For each axis the referee
evaluates the power basis and Bernstein basis at exact rational nodes, inverts
the Bernstein evaluation matrix, applies the resulting tensor transform, and
then applies the inverse tensor transform to recover the original polynomial
coefficient dictionary exactly. It reconstructs `40,595` strictly positive
controls in each `r` cell. This does not reuse the source absolute-power
majorant algorithm as a Bernstein engine.

All fourteen new reserves are strictly positive. The literal smallest reserve
is the high-cell danger value `87/500` (whose derivative is zero). The unique
finite radius-ratio bottleneck is low-cell `N0`, with the freshly recomputed

```text
rho_wide =
27162772450885609710321172264010161955258866496 /
499232790087220155922502903379517386791638099025
          > 13/239.
```

Thus the proof does not extrapolate the old `5/92` derivative constants.

## 3. Adversarial checks

The exact endpoint/seam attack covers all `96` combinations of the five
two-point axes and the three `r` values. Exactly `48` cases have `g>0` and
`48` have `g<=0`. Every case passes its branch endpoint test, the endpoint
slope test when applicable, strict `T=1` legality, and direct evaluation of
the original gate. The least attacked gate is

```text
3791537219332938219668993327 / 1612003174500796900000000 > 0.
```

This finite check is diagnostic only; continuum coverage comes from the two
exact center tensors and the fourteen derivative reserves.

Both complex phases remain live. At the new upper endpoint the exact witness
has imaginary-coordinate product `-279/100` and

```text
G(Q)=277875866038408051450137129651/
  76370356778401980100000000 > 0,
4*(G(Q)-G(Re Q))=-3241147859544180523713/
  2088624224110000000 < 0.
```

Consequently the proof does not erase either phase or invoke real-part
monotonicity. It also uses no discriminant, `N_D`, absorption inequality, or
fixed copositivity allocation.

## 4. Reproducibility and failure behavior

Normal runs passed under Python `3.11.15` and SymPy `1.14.0`:

```text
.venv/bin/python -B \
  tmp/research/verify_common_metric_tilted_rankone_complex_scale_t13over239_enlargement.py
.venv/bin/python -B \
  audit/verify_common_metric_tilted_rankone_complex_scale_t13over239_referee.py
```

Both programs fail closed under all requested negative tests:

- `python -O` stops at the `__debug__` guard;
- the bad-dependency environment variable stops at a SHA-256 mismatch;
- the dropped-sign environment variable stops at the seven-sign set check.

The source verifier hash is

```text
3e2cb11a74a7e77993f3464ccdd888f2dd5d495903b137444adf05344e68bf09
```

and the independent referee hash is

```text
c29f5c864a66c369c439976fb9873d8a22a4a935c3286e7656e16638371c71a8
```

## 5. Scope

This is a seven-real-parameter local theorem (six bounded shape coordinates
and every legal coupling scale). It does not cover arbitrary active blocks,
the feasible-center branch, unbalanced densities, higher rank or dimension,
arbitrary nodes, the full common-metric theorem, or the fixed crossing-lens
constant.
