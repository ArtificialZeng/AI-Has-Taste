# Independent referee audit: next-`X` sigma moving-sheet cell

Date: 2026-08-23  
Verdict: **PASS as an exact strict partial theorem.**

The result proves the original fully conjugated Hermitian scalar gate only on
the displayed moving-sheet cell.  It does not prove the full compact-ball
quartic, the full balanced common-metric gate, the arbitrary-node theorem, or
the optimal constant of a fixed crossing lens.

## 1. Bound statement and isolated verifier

The audited candidate is

```text
tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_next_x_sigma_layer.md
```

with SHA-256

```text
c94f4775dc9e29568a0fe913c39fc1677d3aaa57c7b4e07cea8c54be70e3501c.
```

The predecessor used only for the closed stitch is

```text
tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_adjacent_x_layer.md
```

with SHA-256

```text
95028dc46a177a8e856200eaba3f954086d6b4335aef34efac6be09783e39e92.
```

The new standalone referee verifier is

```text
audit/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_next_x_sigma_independent.py
```

with SHA-256

```text
6dbfc208d481791fd35924bcae4920e23f03b19c1dd9c22f32a6ef3251077443.
```

It imports no discovery code, source verifier, serialized certificate, or
cached quartic/coefficient table.  It binds both theorem statements by hash
before mathematical work.

## 2. Formal endpoint audited

For

```text
0<S<=1/10000,
1/31<=X<=1/30,
|M|<=1/1000,
|omega|,|nu|<=1/100,
```

put

```text
A       = 1+M,
lambda  = A/S,
y0      = 12/(25A)+nu,
wc      = -3(5MX-15M+5X-6)/(25A),
Y       = S y0,
W       = S(wc+omega),
Z       = 3X-X^2-Y^2+W,
x       = -1/5+X,
y       = 3/5+Y.
```

The audited conclusion is the strict inequality `36 Gamma>0` for the
original Hermitian `Q,Q^2` gate, together with `lambda>0`, `0<Z<1/8`, strict
danger, and rank-two positive definiteness.  Both `X` endpoints and every
sign endpoint in the closed `(M,omega,nu)` box are included.  The quantifier
`S>0` is essential.

## 3. Reconstruction from the original gate

The verifier begins with the original frame

```text
r   = (-a,0,c zeta),
f_h = (-ch,q,-ah zeta),
n_h = (cq,h,aq zeta),
a=1/sqrt(6), c=sqrt(5/6), zeta=(4+3i)/5,
q^2=1-h^2.
```

It reduces all entries modulo `q^2=1-h^2` and verifies independently that
`(r,f_h,n_h)` is orthonormal.  In the transverse basis it constructs

```text
C = [[h^2, h(j+ik)],
     [h(j-ik), j^2+k^2+(5/9)Z]],
j=(1+5x)/(3sqrt(5)), k=(-3+5y)/(3sqrt(5)),
H=U C U*, Q=lambda H.
```

It then forms `Q^2` by matrix multiplication before reconstructing

```text
Gamma(Q)
 =4a^2 |(Qp)_2|^2
  +|c conjugate((Qp)_1)+a(Qp)_3+i(ac-(Q^2)_31)|^2
  +|c conjugate((Qp)_2)-i(Q^2)_32|^2
  -32a^2 Re((Qp)_1)^2.
```

Both cyclic `Q^2` entries and every complex conjugation are therefore
retained.  A second derivation constructs the constant, linear, and quadratic
Gram vector

```text
B0 + lambda L + lambda^2 M2
```

and verifies its squared norm minus the danger square is exactly the same
raw gate.  After eliminating `q`, `36 Gamma` is a quartic in `lambda` with
constant term `5`.

## 4. Exact legality and rank

The independent bounds reproduce

```text
999/1000 <= A <= 1001/1000,
wc+omega >= 2549/3700,
wc+omega-S y0^2
 >= 7639086233111/11088900000000 > 0,
Z <= 100173181/1001000000 < 1/8,
1-x^2-y^2-Z
 >= 95037195293/185185000000 > 1/2.
```

Because `S>0` and `A>0`, `lambda=A/S>0`.  Also

```text
Z >= 3X-X^2
     +S*7639086233111/11088900000000 > 0,
```

since `0<X<3`.  Directly from the original compression,

```text
C_11=S>0,                 det C=(5/9)SZ>0.
```

Thus `C` is positive definite, `U` is an isometry, and multiplication by
`lambda>0` gives a Hermitian PSD `Q` of rank exactly two.  The exact identity

```text
x^2+y^2+Z=2/5+(13/5)X+(6/5)Y+W
```

gives the displayed strict-danger reserve.  No zero denominator, loss of
rank, or sphere-boundary datum survives these strict rational bounds.

## 5. Fresh quotient and continuum certificate

The verifier substitutes `lambda=(1+M)/S` term by term into the newly
generated raw polynomial.  It does not load the predecessor's quotient.
Writing `N=S^3(36 Gamma)`, it multiplies by the positive factor

```text
25^8(1+M)^8
```

and verifies an exact `S^2` factor.  The resulting polynomial `qhat` obeys

```text
36 Gamma = qhat/[25^8(1+M)^8 S]
```

on the actual domain.  It has exactly 20 `(S,X)` monomials and bidegree
`(5,4)`.

The isolated degree-one term is reconstructed as

```text
152587890625 M^2 S(1+M)^8(5M^2+14M+14),
```

and is nonnegative because

```text
5M^2+14M+14=5(M+7/5)^2+21/5.
```

For the quadratic layer `aS^2+bSX+cX^2`, fresh centered-monomial bounds over
the full parameter box give

```text
a >=
481040550200263282578648409035494777132062079
/114661785600000000000000000000000,

b >=
2301835302565365212028445402384697058519239
/191102976000000000000000000000,

c >= c0 =
2564950982194530478444050838857341987999
/1274019840000000000000000000.
```

All three are strictly positive, and `c0` is their minimum.

The decisive projective substitution is lossless because `X>=1/31>0`:

```text
sigma=S/X,                 0<sigma<=31/10000.
```

After division by `X^2`, a monomial `S^i X^j` is bounded as

```text
|S^i X^j|/X^2
 <= (31/10000)^i (1/30)^(i+j-2).
```

Applying this bound separately to the 16 higher `(S,X)` terms recomputes
947 centered parameter monomials.  Their total exact absolute contribution
is

```text
Rabs =
46499117573964545715217879542445250542603528830310449624295476899453
/17199267840000000000000000000000000000000000000000000000000.
```

Even discarding the positive `a sigma^2+b sigma` reserve leaves

```text
c0-Rabs =
34580339142052196913279468445031671587443896471169689550375704523100547
/17199267840000000000000000000000000000000000000000000000000 > 0.
```

Every cleared factor is strictly positive for `S>0` and `A>0`.  This proves
the continuum statement for the original gate; it is not an inference from
sampled positive nodes.

## 6. Falsification and boundary audit

As a separate non-proof diagnostic, the referee evaluated the original raw
quartic at 72 exact rational legal nodes: three positive `S` values, both
`X` endpoints and the midpoint, and all eight parameter-box corners.  No
negative occurred.  The exact minimum was

```text
5205504500118190263502525633461351583967759
/36940840000000000000000000000000000000000 > 0.
```

The finite test is not used in the continuum proof.

Endpoint conclusions are:

- `X=1/31` is included by both the independently audited predecessor cell
  and this cell, so the stitch is closed and has no limiting gap.
- `X=1/30` is included directly: every bound uses `X<=1/30` and the final
  exact margin is strict there.
- `S=0` is excluded.  It is used only for coefficient extraction after
  clearing; geometrically `lambda=(1+M)/S` is undefined there.
- `X=0` is not part of the new projective chart.  It belongs only to the
  predecessor's C0 chart, which divides by `S^2` rather than by `X`.
- The merged conclusion is therefore `0<S<=1/10000` and `0<=X<=1/30`, with
  `X=0` supplied by the predecessor and not by continuity in this cell.

I found no exact legal negative original gate and no hidden denominator,
rank, zero, conjugation, or endpoint gap.

## 7. Fail-closed and integrity tests

Environment: Python 3.14.7 with the checked-in portable SymPy 1.13.3 tree
selected by `PYTHONPATH=tmp/research/pydeps`.  Only one CPU process was used.
No proof assistant was used.

Recorded exit codes:

```text
independent verifier, ordinary mode:                         0
candidate source verifier, ordinary mode:                    0
independent verifier under python -O:                        1
candidate source verifier under python -O:                   1
independent verifier with missing statement:                 1
independent verifier with hash-mismatched statement:         1
independent verifier with hash-mismatched predecessor:       1
independent verifier py_compile:                             0
candidate source manifest, shasum -a 256 -c:                 0
new independent manifest, shasum -a 256 -c:                 0
new manifest with first digest corrupted in a stream:        1
```

The optimized-mode failures occur before importing SymPy.  Missing and
hash-mismatched inputs fail before symbolic reconstruction.  The source and
referee verifiers are ASCII/control-byte clean.

The restored global `CHECKPOINT_MANIFEST.sha256` exits `1` because four
shared living files have changed since that frozen checkpoint:
`APPROACH_REGISTRY.md`, `CLAIM_LEDGER.md`, `COUNTEREXAMPLE_DB.md`, and
`research_state.json`.  That global historical mismatch is reported rather
than silently treated as a candidate failure.  The dedicated candidate
manifest passes.

The new independent manifest binds the candidate, predecessor, official
source verifier, this verifier, and this report.  Replacing the first
digest's initial hexadecimal digit in a stream caused exactly that candidate
line to report `FAILED`, printed `1 computed checksums did NOT match`, and
exited `1`; the on-disk manifest was not modified.

## 8. Scientific status

**Partial theorem.**  The next cell is exactly certified and stitches the
moving-sheet family through `X=1/30`.  The full compact ball outside this
special moving sheet remains open, as do arbitrary normalized scales,
arbitrary nonplanar kernels beyond the compact reduction, the common-metric
theorem, the all-node bridge, and the fixed crossing-lens constant.
