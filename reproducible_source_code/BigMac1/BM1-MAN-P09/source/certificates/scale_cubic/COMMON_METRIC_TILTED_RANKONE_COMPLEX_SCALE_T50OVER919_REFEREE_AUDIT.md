# Referee audit: complex-scale half-width `50/919`

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
r   in [99/100,103/100],      t in [3626/919,3726/919],
```

and every legal scale `T`: `T>0` when `g<=0`, and `T>Delta*g/n` when `g>0`.
The applicable closure endpoint is also positive for the cleared gate. The two
closed `r` cells meet at `101/100`, so the seam is covered twice.

## 2. Definition-level reconstruction

The referee imports neither source verifier nor discovery code. From the fully
conjugated original Hermitian gate it reconstructs the Hermitian rank-two
zero-Schur-complement boundary, the complete legal `T` half-line, and
`P(T)=4*Delta^2*G(Q)` both by direct extraction and by a separate
phase-retaining residual-square formula. It reconstructs the seven terminal
signs `danger,Delta,n,C0,C1,N0,N1` and the complete dependency DAG.

For each `r` cell, exact nodal evaluation and Bernstein-basis inversion produce
the `t=4` tensor; applying the inverse tensor transform recovers the original
power-coefficient dictionary exactly. Each cell has `40,595` strictly positive
controls. Fresh absolute derivative majorants on
`[3626/919,3726/919]` give fourteen strictly positive reserves. The unique
finite bottleneck is low-cell `N0`, with

```text
rho_wide =
22832956414652720419288572875925058067205119308096 /
419658897924777012091564281675537127592865447699025
          > 50/919.
```

The exact comparison cross-product is
`542048826999460747984389198271984118232259188974>0`. The exact width gain
over `21/386` is `1/354734`.

## 3. Adversarial checks

The endpoint/seam attack covers all `96` exact combinations and splits into
`48` positive-`g` and `48` nonpositive-`g` cases. Every case passes its branch
endpoint test, the endpoint slope test when applicable, strict `T=1` legality,
and direct original-gate evaluation. The least attacked gate is

```text
40614857500397194448289907112063 /
17267773417544622036100000000 > 0.
```

This finite check is diagnostic only. Continuum coverage is furnished by the
two reconstructed center tensors and fourteen derivative reserves.

At the new upper endpoint, a strict live-phase witness has imaginary-coordinate
product `-279/100` and

```text
G(Q)=60746927109990602200372569492531/
  16695493268772709728100000000 > 0,
4*(G(Q)-G(Re Q))=-184269381654495888525183/
  118744947221210000000 < 0.
```

Therefore neither complex phase was erased and CE-046/048/059/060 was not
reused as a positive argument.

## 4. Reproducibility and failure behavior

Normal runs passed under the project Python `3.11.15` and SymPy `1.14.0`.
Both programs fail closed under optimized Python, dependency-hash tampering,
and deletion of a required terminal sign. Direct source and referee manifests
bind all theorem, code, audit, test, and predecessor dependencies.

The source verifier hash is

```text
6e9be003ceb0e89e50e9156ede7d54d6a79888bb7768ac854dd4318792d9e415
```

and the independent referee hash is

```text
a8cb4c4a99f644fbdd97191bf53504bf90a28f85227d3c1c8dfc907febdcf350
```

## 5. Scope

This is a seven-real-parameter local theorem: six bounded shape coordinates
and every legal coupling scale. It does not cover arbitrary active blocks,
the feasible-center branch, unbalanced densities, higher rank or dimension,
arbitrary nodes, the full common-metric theorem, or the fixed crossing-lens
constant. No proof assistant was used for this enlargement.
