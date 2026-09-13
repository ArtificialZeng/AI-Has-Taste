# Exact source candidate on the uncovered ray `(x,y,Z)=(5/8,0,1/8)`

Date: 2026-08-26. Status: **strict exact source candidate, frozen before an
independent no-import referee**. This is not yet an independently audited
theorem and does not alter a ledger, release, PDF, or ZIP.

## 1. Scope selected by the coverage audit

The frozen coverage audit separates the stitched five-parameter `X` sheet by
the exact inequality `y>3/5`.  It selects the rational compact-ball shape

```text
(x,y,Z)=(5/8,0,1/8),  Z=z^2,
```

which is outside that sheet and outside the previously joined full-scale box
`x<=1/2`.  This source tests the complete two-parameter family

```text
0<h<=1, lambda>0,
```

for both signed `z` lifts.  It does not claim a neighborhood.

## 2. Exact legality

The compact-ball radius and danger reserve are

```text
x^2+y^2+Z=33/64,
1-x^2-y^2-Z=31/64>0.
```

The affine Cholesky coordinates are

```text
j=11/(8 sqrt(5)),
k=-1/sqrt(5),
ell^2=5/72,
W=j^2+k^2+ell^2=373/576.
```

Hence the transverse compression has

```text
det(C)=(5/72)h^2>0.
```

For every positive scale the reconstructed dangerous scalar is

```text
Re(Qp)_1=-(155 sqrt(6)/2304) lambda h^2<0.
```

Both choices `ell=+-sqrt(5/72)` are reconstructed as Cholesky Gram columns
and give the same Hermitian compression.

## 3. Definition-level original gate reconstruction

The source constructs the exact complex transverse frame, proves its Gram
and kernel identities modulo `q^2=1-h^2`, forms the Hermitian `Q`, computes
all nine entries of `Q^2`, and evaluates the fully conjugated raw scalar gate.
It separately constructs the cyclic Gram-vector expression and proves exact
identity before any sign conclusion.

With `S=h^2`, the raw gate is

```text
36 Gamma=C0+C1 lambda+C2 lambda^2+C3 lambda^3+C4 lambda^4,
```

where

```text
C0 = 5,
C1 = (85/96) S,
C2 = (215/331776) S (21249 S+19037),
C3 = (5/31850496) S (2654208 S^2+8572032 S+4083977),
C4 = S(987426091008 S^3+2214366284160 S^2
       +1677691247279 S+423511736838)/110075314176.
```

Every displayed integer coefficient is strictly positive.  Since `S>0` and
`lambda>0`, every summand is nonnegative and `C0=5>0`; in fact every
nonconstant coefficient is itself strictly positive.  Therefore the original
fully conjugated raw gate satisfies

```text
Gamma(Q)>0 for every 0<h<=1 and lambda>0.
```

This is an exact continuum proof.  No finite nodes, floating-point values,
sampled SDP, coefficient extrapolation, or CE-046/048/059/060 route is used.

## 4. Four-way classification

```text
chart illegality:             absent (reserve 31/64, determinant positive),
Bernstein/certificate failure: absent (direct positive coefficient proof),
implementation/resource failure: absent in the frozen normal replay,
legal raw-gate negative:       absent on the complete stated ray.
```

The result remains a fixed rational shape ray, not the full compact ball,
the general common-metric gate, arbitrary nodes/dimension, or the fixed-lens
constant.

## 5. Replay and independent referee gate

Run

```text
.venv/bin/python -B -u tmp/research/compact_ball_uncovered_ray_x5_8_preflight.py
```

The frozen source retains its historical `preflight` filename, but its final
bytes contain the exact coefficient identities, coverage dependency binding,
both signed lifts, and all proof gates.  Six adversarial runs reject optimized
execution, a bad coverage hash, bad shape normalization, deleted `Q^2`, a
flipped danger sign, and a corrupted terminal coefficient.  External-cache
`py_compile` passes.

Promotion requires a separately written no-import referee that treats this
source only as opaque bytes, reconstructs `Q,Q^2` through a different signed
Gram-column order, independently derives the five coefficient polynomials,
and attacks the source/manifest bindings.  Until then this remains a source
candidate only.
