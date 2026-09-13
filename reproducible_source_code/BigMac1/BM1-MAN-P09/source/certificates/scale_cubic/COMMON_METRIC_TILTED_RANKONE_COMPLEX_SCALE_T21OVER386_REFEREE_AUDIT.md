# Referee audit: complex-scale half-width `21/386`

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
r   in [99/100,103/100],      t in [1523/386,1565/386],
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
6. all seven fresh `t`-derivative majorants on `[1523/386,1565/386]`;
7. all fourteen exact `m-(21/386)M` reserves, with the derivative
   majorants freshly recomputed on `[1523/386,1565/386]` rather than inherited
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
4663813122843737977650051498551334435768458336 /
85718455710308009675929498510346753854808433775
          > 21/386.
```

The exact comparison cross-product is
`144295501214656178400409723533261255647808421>0`. Thus the proof does not
extrapolate the old `13/239` derivative constants.

## 3. Adversarial checks

The exact endpoint/seam attack covers all `96` combinations of the five
two-point axes and the three `r` values. Exactly `48` cases have `g>0` and
`48` have `g<=0`. Every case passes its branch endpoint test, the endpoint
slope test when applicable, strict `T=1` legality, and direct evaluation of
the original gate. The least attacked gate is

```text
19751109446339394000443880157 / 8397359187577272900000000 > 0.
```

This finite check is diagnostic only; continuum coverage comes from the two
exact center tensors and the fourteen derivative reserves.

Both complex phases remain live. At the new upper endpoint the exact witness
has imaginary-coordinate product `-279/100` and

```text
G(Q)=29541387207997411577757671059/
  8119057735779760900000000 > 0,
4*(G(Q)-G(Re Q))=-853391406768747308637/
  549933433790000000 < 0.
```

Consequently the proof does not erase either phase or invoke real-part
monotonicity. It also uses no discriminant, `N_D`, absorption inequality, or
fixed copositivity allocation.

## 4. Reproducibility and failure behavior

Normal runs passed under Python `3.11.15` and SymPy `1.14.0`:

```text
.venv/bin/python -B \
  tmp/research/verify_common_metric_tilted_rankone_complex_scale_t21over386_enlargement.py
.venv/bin/python -B \
  audit/verify_common_metric_tilted_rankone_complex_scale_t21over386_referee.py
```

Both programs fail closed under all requested negative tests:

- `python -O` stops at the `__debug__` guard;
- the bad-dependency environment variable stops at a SHA-256 mismatch;
- the dropped-sign environment variable stops at the seven-sign set check.

The source verifier hash is

```text
1c50d77fe25ca57b60085abcad2b6570c417bdaf6107950b7e8fa6ec64d9bb27
```

and the independent referee hash is

```text
141e7ce16042f2bac264e52715258e8689a5ade08cefa555d715b34f3e5afea5
```

The host `python3` executable has no SymPy installation and therefore cannot
run either verifier. This is an unavailable dependency, not a failed sign
check; the locked project environment above is the reproducible execution
environment.

## 5. Scope

This is a seven-real-parameter local theorem (six bounded shape coordinates
and every legal coupling scale). It does not cover arbitrary active blocks,
the feasible-center branch, unbalanced densities, higher rank or dimension,
arbitrary nodes, the full common-metric theorem, or the fixed crossing-lens
constant.
