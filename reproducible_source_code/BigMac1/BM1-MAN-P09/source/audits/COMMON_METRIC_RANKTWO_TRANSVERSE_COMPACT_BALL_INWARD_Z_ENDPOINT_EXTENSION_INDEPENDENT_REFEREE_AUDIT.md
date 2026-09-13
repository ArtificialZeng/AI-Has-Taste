# Independent referee audit: inward-Z endpoint extension

Date: 2026-08-25  
Verdict: **PASS — EXACT INDEPENDENTLY AUDITED PARTIAL THEOREM**  
Severity count: **fatal 0, major 0, minor/expository 1**

The original fixed crossing-lens constant, the full compact-ball quartic,
the general common-metric gate, and the arbitrary-node bridge remain open.
This audit certifies only the displayed endpoint cell.

## 1. Frozen claim and independence boundary

The frozen inputs were bound before mathematical work:

| Artifact | SHA-256 |
|---|---|
| `tmp/research/compact_ball_inward_z_endpoint_extension.py` | `2ab0f3f532fbfe0d2fc6b2aa3301ff4857f783161f109ad4d846cbcbf266df4f` |
| `tmp/research/common_metric_ranktwo_transverse_compact_ball_inward_z_endpoint_extension_source_candidate.md` | `146743ebe254682bee761d0378b90a1e76ca139063ca83cb6f5a7c1b625243c9` |
| `tmp/research/compact_ball_inward_z_endpoint_extension_source_freeze_manifest.sha256` | `ae3ede1048aad9625884963ffbff66437dbd6c36540244cdb82a94efb999a0a8` |
| `tmp/research/compact_ball_inward_z_endpoint_extension_source_test_results.txt` | `fffba3f683967920849dacc8056f5569b5ae13c6c72866a78a4dab52413b4e5a` |

The referee did not import, execute, or parse the frozen source and did not
read or copy its intermediate polynomial or control table.  Its bytes were
used only for SHA-256.  The final claim note supplied the proposition to be
checked.

The independent verifier is
`tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_inward_z_endpoint_extension_independent_referee.py`,
SHA-256
`0928e8ab3c9c6027feb646af68a7dc4d567d34970887eb672520d120c6a387ab`.
It uses CPython 3.11.15 and SymPy 1.14.0 from the project `.venv`.

## 2. Exact theorem certified

For

```text
0<S<=1/10000,               1/4<=X<=131/520,
|M|<=1/1000,               |omega|,|nu|<=1/100,
A=1+M,                     lambda=A/S,
y0=12/(25A)+nu,
b=(45M+18)/(25A)-(3/5)X+omega-(10636/275)(X-1/5),
x=-1/5+X,                  y=3/5+S*y0,
Z=9/13-X^2+S*b-S^2*y0^2,
```

both lifts `z=+-sqrt(Z)` are legal, strictly dangerous rank-two data and the
original fully conjugated Hermitian scalar gate is strictly positive.

This is an infinite exact local theorem, not a numerical finite result.  No
proof assistant was used.

## 3. Definition-level reconstruction

The referee reordered the Gram construction.  Instead of starting from the
`(r,f)` compression matrix, it used the signed columns

```text
g_z   = ell f,
g_mix = h r + (j-i k) f,
H     = g_z g_z^* + g_mix g_mix^*.
```

It independently checked the compression frame, Hermiticity,
`det(C)=(5/9)SZ`, invariance under `z -> -z`, and rank-two legality when
`S,Z>0`.  It then formed `Q=lambda H`, multiplied the complete `3 x 3`
matrix to obtain every entry of `Q^2`, and evaluated the literal fully
conjugated gate.  A second cyclic Gram-vector evaluation agreed exactly.

Reduction was done in the order

```text
z^2=Z,   h^2=S,   q^2=1-S,
```

which removed the signed lift and all frame radicals.  Deleting the first
gate square or flipping the danger-term sign causes this independent identity
to fail closed.

## 4. Lossless clearing and continuum certificate

The verifier substituted the endpoint sheet into the reconstructed raw gate
and checked both directions of the positive clearing

```text
P = 25^8 A^8 S^3 (36 Gamma).
```

Because `A>0` and `S>0`, positivity of the cleared polynomial is equivalent
to positivity of the original gate.  The exact structural counts are:

| Object | Result |
|---|---:|
| nonzero `(S,X)` coefficients of `P` | 32 |
| nonzero `(S,X)` coefficients after layer removal | 32 |
| centered `(S,X,M,omega,nu)` monomials in the core | 1,581 |
| bidegree in `(S,X)` | `(7,4)` |

The removed layer is

```text
S^3 25^8 M^2 A^8 (5M^2+14M+14) >= 0.
```

For the exact cell map

```text
X=1/4+u/520,   S=tau/10000,   0<=u,tau<=1,
```

the referee first expanded a dense polynomial in `(tau,u)` and then applied
the direct binomial monomial-to-Bernstein formula.  This is algorithmically
different from accepting a stored control tensor.  The independent result is:

- bidegree `(7,4)`, hence 40 controls;
- all 40 centered rational lower controls are strictly positive;
- `zero=[]`;
- `(0,0)` is the unique global weakest control;
- its exact reserve is

```text
987933779504207075207504779933987999
/ 7187610992640000000000000000;
```

- all five controls in the `tau=0` row are strict; and
- the complete weakest-control polynomial is

```text
95367431640625 (M+1)^12 / 685464.
```

The centered lower bound is a rational coefficient `l1` bound on the entire
`(M,omega,nu)` box.  Tensor Bernstein weights are nonnegative and sum to one.
Thus the strict control bounds prove the whole continuum; the 72 rational
nodes are only adversarial diagnostics and play no role in the proof.

## 5. Seam and legality

The predecessor sheet was independently substituted into the raw gate.  At
old `X=1/4`, its cleared polynomial agrees term by term with the new cell at
`u=0`.

Monotonic derivatives and exact corner evaluation give

```text
b_min = -7674229/5291000,
Z_min = 129601350803598453349/206142651000000000000,
0<Z<108/169,
lambda>0.
```

Writing `T=(6/5)y0+b`, the exact identity is

```text
D = 1-x^2-y^2-Z = (2/5)(X-3/13)-S T.
```

The verifier finds `T<=-2736/3575<-1/100`, so on the full new cell

```text
D >= 1/130 + S/100 > 0,
det(C)=(5/9)SZ>0.
```

At the outer corner `(X,S)=(131/520,1/10000)`, the weaker bounds quoted by
the source note are exactly

```text
D >= 110013/13000000,
det(C) >=
129601350803598453349/3710567718000000000000000.
```

### Minor/expository clarification

The last two displayed fractions are outer-corner bounds, not uniform lower
bounds over `0<S<=1/10000`.  Indeed the endpoint-slice danger infimum as
`S->0+` is `11/1300`, and `det(C)` has infimum zero as `S->0+`.  This does
not damage strict legality or gate positivity: the correct full-cell bounds
above prove both.  A future manuscript should label the fractions explicitly
as outer-corner bounds.

## 6. Adversarial and reproducibility checks

Final-script tests:

| Test | Expected result | Observed |
|---|---|---|
| normal definition-level replay | exit 0 | PASS |
| `python -O` | reject | exit 1, optimized mode rejected |
| bad source path/hash | reject | exit 1, source SHA rejected |
| delete a raw-gate square | reject | exit 1, two gate reconstructions disagree |
| flip the danger-term sign | reject | exit 1, two gate reconstructions disagree |
| external-cache `py_compile` | exit 0 | PASS |
| direct source-freeze manifest | 6/6 | PASS |
| 72 exact rational nodes | positive diagnostics | 72/72 PASS |

The complete command/output record is
`tmp/research/compact_ball_inward_z_endpoint_extension_independent_referee_test_results.txt`,
SHA-256
`08c1f5485b526f6538faeff4ecc7f8eedf87cc9ceae26bc44801cbabacb7aba3`.
It also records the pre-freeze implementation failures and deliberate
interruptions; they were not hidden or relabeled as mathematical evidence.

## 7. Referee decision and strict scope

There are no fatal or major mathematical gaps in this cell theorem.  The
appropriate status is therefore:

> **EXACT INDEPENDENTLY AUDITED PARTIAL THEOREM.**

It proves strict gate positivity only on the displayed rational endpoint
cell and its exact splice to the preceding inward-Z sheet.  It does not prove
the remaining compact unit ball, arbitrary Bloch frames or kernels, the full
common-metric theorem, an arbitrary-node interpolation bridge, or the
optimal constant of a fixed crossing lens.  This audit does not authorize a
paper/PDF claim broader than that scope.
