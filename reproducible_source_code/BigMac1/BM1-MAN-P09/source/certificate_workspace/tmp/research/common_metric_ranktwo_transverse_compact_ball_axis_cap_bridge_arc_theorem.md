# High-`Z` axis-to-center-box bridge arc

## Status

This is an exact source-certified candidate awaiting an independently written
referee reconstruction.  It is a one-real-dimensional compact-shape partial
theorem with the complete displacement and positive-scale quantifiers.  It is
not the full axis cap, the full compact ball, the common-metric theorem, or the
fixed crossing-lens theorem.

## Statement

Use the lossless compact-ball chart of
`tmp/research/common_metric_ranktwo_transverse_full_cone_compact_ball_reduction.md`.
Put `S=h^2`.  For

\[
 0<S\le 1,\qquad \lambda>0,\qquad 0\le x\le\frac18,
 \qquad y=0,\qquad Z=z^2=\frac{63}{64}-x^2,
\]

the original fully conjugated Hermitian `Q,Q^2` gate is strictly positive.
Both signs of `z` are included by the compact chart.

The shape is legal with the exact constant reserve

\[
 1-x^2-y^2-Z=\frac1{64},
 \qquad \frac{31}{32}\le Z\le\frac{63}{64}.
\]

The compact compression has

\[
 \det C=\frac59SZ>0.
\]

Thus it is Hermitian positive definite of rank two, and `Q=lambda U C U^*`
is a legal Hermitian PSD rank-two compression for every displayed parameter.

## Exact coefficient certificate

Write the reconstructed quartic as

\[
 36\Gamma=5+\sum_{m=1}^4 C_m(S,x,y,Z)\lambda^m,
 \qquad C_m=S G_m.
\]

Set `u=8x`, so `0<=u<=1`, and substitute

\[
 x=\frac u8,\qquad y=0,\qquad
 Z=\frac{63-u^2}{64}.
\]

The natural bivariate Bernstein tensors of `G_m` on
`(S,u) in [0,1]^2` have the following exact data.

| polynomial | degree | controls | least control |
|---|---:|---:|---:|
| `G_1` | `(0,1)` | 2 | `185/32` |
| `G_2` | `(1,2)` | 6 | `430915/36864` |
| `G_3` | `(2,3)` | 12 | `818465/131072` |
| `G_4` | `(3,4)` | 20 | `34042755/8388608` |

All forty controls are strictly positive.  Therefore every `C_m` is strictly
positive on the original domain `S>0`, and hence

\[
 36\Gamma>5>0
\]

for every finite positive `lambda` in the statement.

## Lossless scale compactification and faces

For audit purposes set

\[
 \tau=\frac{\lambda}{1+\lambda},\qquad
 P=(1-\tau)^4,36\Gamma\!\left(\frac{\tau}{1-\tau}\right).
\]

The natural `(S,u,tau)` degree is `(4,4,4)`.  Its 125 exact Bernstein
controls contain no negative value: 105 are positive and the remaining 20
are exactly

\[
 (i_S,i_u,i_\tau)=(0,i_u,i_\tau),
 \quad 0\le i_u\le4,\quad1\le i_\tau\le4.
\]

They are solely the artificial `S=0` closure zeros.  The least positive full
control is `185/512` at `(1,4,1)`.  Neither `S=0` nor `tau=1` belongs to the
original quantifiers: `S=0` is only the displacement closure, while `tau=1`
is projective positive-scale infinity.

The four requested face checks are exact:

- `tau=0`: its unique control is `5`;
- `tau=1`, after division by the positive actual-domain factor `S`: all 20
  controls are positive, with least value `34042755/8388608`;
- `x=0`: 25 controls, four `S=0` closure zeros, least positive value
  `204996035/509607936`;
- `x=1/8`: 25 controls, four `S=0` closure zeros, least positive value
  `185/512`.

Thus the arc connects the independently proved center axis at
`(x,y,Z)=(0,0,63/64)` to the independently proved center-box boundary at
`(1/8,0,31/32)` without filling either omitted three-dimensional axis cap.

## Original-gate provenance and route exclusions

The source verifier rebuilds the fully conjugated Hermitian matrix `Q`, all
entries of `Q^2`, the two leakage coordinates, the danger identity, the
compression determinant, and the positive-scale quartic from definitions.
At the rational calibration point

\[
 (h,q,\lambda,x,y,Z)=
 \left(\frac35,\frac45,\frac75,\frac1{16},0,\frac{251}{256}\right)
\]

the unreduced raw expression and the reconstructed quartic agree exactly at

\[
 \frac{42247865515794049199}{995328000000000000}.
\]

No real-part monotonicity (CE-046), feasible-center absorption (CE-048),
fixed allocation `s=-2` (CE-059), or `Z=0` baseline quadratic remainder
(CE-060) is used.  There is no numerical sign inference and no negative gate
candidate on this arc.

Run

```sh
PYTHONPATH=tmp/research/pydeps:tmp/research \
python3 tmp/research/verify_common_metric_ranktwo_transverse_compact_ball_axis_cap_bridge_arc_theorem.py
```

The discovery provenance is
`tmp/research/compact_ball_axis_cap_bridge_arc_discovery.py`.  The bound source
set is listed in
`tmp/research/common_metric_ranktwo_transverse_compact_ball_axis_cap_bridge_arc_theorem_manifest.sha256`.
