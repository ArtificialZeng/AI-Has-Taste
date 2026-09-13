# Referee audit: complex-scale half-width `5/92`

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
r   in [99/100,103/100],      t in [363/92,373/92],
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
6. all seven fresh `t`-derivative majorants on `[363/92,373/92]`;
7. all fourteen exact `m-(5/92)M` reserves.

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
896775556481533279336770926007341554681088 /
16481441167216725968620003969664490147404575
          > 5/92.
```

Thus the proof does not extrapolate the old `2/37` derivative constants.

## 3. Adversarial checks

The exact endpoint/seam attack covers all `96` combinations of the five
two-point axes and the three `r` values. Exactly `48` cases have `g>0` and
`48` have `g<=0`. Every case passes its branch endpoint test, the endpoint
slope test when applicable, strict `T=1` legality, and direct evaluation of
the original gate. The least attacked gate is

```text
127470839802864241085806509 / 54194925629649800000000 > 0.
```

This finite check is diagnostic only; continuum coverage comes from the two
exact center tensors and the fourteen derivative reserves.

Both complex phases remain live. At the new upper endpoint the exact witness
has imaginary-coordinate product `-279/100` and

```text
G(Q)=659709262001662465543697/181310688232200000000 > 0,
4*(G(Q)-G(Re Q))=-226554899274721441/145993420000000 < 0.
```

Consequently the proof does not erase either phase or invoke real-part
monotonicity. It also uses no discriminant, `N_D`, absorption inequality, or
fixed copositivity allocation.

## 4. Reproducibility and failure behavior

Normal runs passed under Python `3.11.15` and SymPy `1.14.0`:

```text
.venv/bin/python -B \
  tmp/research/verify_common_metric_tilted_rankone_complex_scale_t5over92_enlargement.py
.venv/bin/python -B \
  audit/verify_common_metric_tilted_rankone_complex_scale_t5over92_referee.py
```

Both programs fail closed under all requested negative tests:

- `python -O` stops at the `__debug__` guard;
- the bad-dependency environment variable stops at a SHA-256 mismatch;
- the dropped-sign environment variable stops at the seven-sign set check.

The source verifier hash is

```text
d357bbfaac1fd054c4bab671e488243f75bfc709acff2dde29e42c7e827043a7
```

and the independent referee hash is

```text
0df222da6d9b4a1f4bb58f2a7d1e842219ee3952dce022ce984cded57f9b3f7d
```

## 5. Scope

This is a seven-real-parameter local theorem (six bounded shape coordinates
and every legal coupling scale). It does not cover arbitrary active blocks,
the feasible-center branch, unbalanced densities, higher rank or dimension,
arbitrary nodes, the full common-metric theorem, or the fixed crossing-lens
constant.
