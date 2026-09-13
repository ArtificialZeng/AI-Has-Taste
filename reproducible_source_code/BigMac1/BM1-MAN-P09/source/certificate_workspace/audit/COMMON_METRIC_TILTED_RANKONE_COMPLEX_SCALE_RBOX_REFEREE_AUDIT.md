# Referee audit: five-shape complex scale box with an active-block `r` layer

Date: 2026-08-23.  Verdict: **PASS as an exact independently audited
computer-assisted six-real-parameter partial theorem**.  The unrestricted
complex Hermitian gate and fixed crossing-lens constant remain open.

## Audited domain and branch

Fix `a=3/5,c=4/5,t=4` and let

```text
ell in [8,10],
w   in [-31/100,-29/100],
k   in [-301/100,-299/100],
z   in [-101/100,-99/100],
r   in [99/100,101/100].
```

Define

```text
Delta = 4*r-z^2-w^2,
n = 4(k^2+ell^2)+r-2(k*z+ell*w),
g = (12/25)*ell-z*k-w*ell-4.
```

The dangerous scalar `3*r/5+4*z/5` is strictly negative on the full box.
The complete strict legal scale half-line is exactly `T>0` for `g<=0` and
`T>Delta*g/n` for `g>0`.  The original fully conjugated gate is strictly
positive throughout that half-line and at the finite closed endpoint, with
no equality.

## Source certificate

The source verifier
`tmp/research/verify_common_metric_tilted_rankone_complex_scale_rbox_theorem.py`
reconstructs the original Hermitian matrix, positive active block, zero Schur
complement, rank-two boundary, danger, scalar gate center, even scale cubic,
endpoint, derivative, curvature, and discriminant.  Its direct exact
power-to-interval-Bernstein transformation checks all 734,288 controls:

```text
danger       4
Delta       18
n           72
C0         245
C1        1764
N0       30492
N1        8000
ND      693693
```

Every control is strictly positive.  The exact five-degrees and least
controls are recorded in
`tmp/research/common_metric_tilted_rankone_complex_scale_rbox_theorem.md`.

## Isolated nodal referee

The referee
`audit/verify_common_metric_tilted_rankone_complex_scale_rbox_referee.py`
imports neither discovery nor source code and uses no floating-point
interpolation or cached control tensor.  It independently:

1. extracts the even-in-scale cubic from the original fully conjugated gate;
2. rebuilds PSD feasibility, danger, `q_g`, and the full legal scale branch;
3. derives the endpoint, derivative, curvature, and universal discriminant
   identities;
4. evaluates every certificate polynomial on its complete five-axis exact
   rational node tensor;
5. recovers all 734,288 controls by five staged Bernstein-collocation
   inversions and reconstructs every original node; and
6. checks a new exact boundary witness at
   `r=99/100,z=-101/100,k=-301/100`.

The largest `ND` tensor contains 693,693 nodes and is included in the direct
node comparison.  The witness has positive original gate, negative real-part
phase increment, and opposite imaginary-coordinate signs.  Therefore the
proof does not use CE-046, CE-048, or the old simultaneous-phase cone.

## Reproduction

```sh
.venv/bin/python tmp/research/discover_complex_scale_cubic_r_box.py
.venv/bin/python tmp/research/verify_common_metric_tilted_rankone_complex_scale_rbox_theorem.py
.venv/bin/python audit/verify_common_metric_tilted_rankone_complex_scale_rbox_referee.py
```

Discovery prints `ALL_POSITIVE True`.  Source and referee each print four
`PASS` records and exit zero.  Both certificate programs fail closed under
optimized Python before assertions can be skipped.

## Scope

This opens one more active-block coordinate but is still only a rational
local shape box with all scales.  It does not cover arbitrary active blocks
or coupling directions, the feasible-center branch, unbalanced densities,
higher rank or dimension, arbitrary nodes, or the fixed crossing-lens
problem.  No submission-ready manuscript or PDF is authorized.
