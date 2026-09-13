# A complex-phase tube around the high-`Z` bridge arc

## Status

**Exact source-certified candidate; independent referee pending.**  This is a
two-real-dimensional compact-shape partial theorem with the full positive
displacement and finite positive-scale quantifiers.  It is not either whole
axis cap, the full compact ball, the unrestricted complex Hermitian or
common-metric theorem, the arbitrary-node theorem, or the fixed
crossing-lens theorem.  No Lean proof is claimed.

## Statement

Use the lossless compact-ball chart of
`tmp/research/common_metric_ranktwo_transverse_full_cone_compact_ball_reduction.md`
and put `S=h^2`.  For

\[
 0<S\le1,\qquad \lambda>0,\qquad
 0\le x\le\frac18,\qquad |y|\le\frac1{64},\qquad
 Z=z^2=\frac{63}{64}-x^2,
\]

the original fully conjugated Hermitian `Q,Q^2` gate is strictly positive.
Both signs of `z` are included.

The shape is strictly dangerous and legal, because

\[
 1-x^2-y^2-Z=\frac1{64}-y^2
 \ge \frac{63}{4096}>0,
 \qquad \frac{31}{32}\le Z\le\frac{63}{64}.
\]

The compressed matrix is Hermitian and

\[
 \det C=\frac59SZ>0.
\]

Thus it is positive definite of rank two; the isometric compression frame
preserves positivity and rank, and multiplication by `lambda>0` gives a
legal Hermitian PSD rank-two datum at every displayed point.  The compact
chart depends on `z` only through `Z=z^2`, which proves the two-sign claim.

## Raw gate and exact coefficient certificate

The source verifier reconstructs the orthonormal frame modulo
`q^2=1-h^2`, the Hermitian compression, `Q`, every entry of `Q^2`, and the
three fully conjugated leakage coordinates from definitions.  It obtains

\[
 36\Gamma=5+\sum_{m=1}^4 C_m(S,x,y,Z)\lambda^m,
 \qquad C_m=S G_m.
\]

Map the tube losslessly to a unit cube by

\[
 u=8x,\qquad y=\frac{2v-1}{64},\qquad
 Z=\frac{63-u^2}{64},\qquad 0\le u,v\le1.
\]

The natural tensor Bernstein controls of `G_m` on
`(S,u,v) in [0,1]^3` have the following exact data.

| polynomial | degree `(S,u,v)` | controls | least control and index |
|---|---:|---:|---:|
| `G_1` | `(0,1,2)` | 6 | `33605/6144` at `(0,1,2)` |
| `G_2` | `(1,2,4)` | 30 | `15241448155/1358954496` at `(0,2,4)` |
| `G_3` | `(2,3,6)` | 84 | `49463834927165/8349416423424` at `(0,3,6)` |
| `G_4` | `(3,4,8)` | 180 | `1152452992382662513/307792887033102336` at `(0,4,8)` |

All `300/300` controls are strictly positive.  Hence every `G_m>0` on the
closed cube, every `C_m>0` for `S>0`, and therefore

\[
 36\Gamma=5+S\sum_{m=1}^4G_m\lambda^m>5>0
\]

for every finite positive `lambda` in the statement.  This is an exact
coefficientwise proof, not a sign inference from samples.

## Projective scale and boundary audit

For audit only, set

\[
 \tau=\frac{\lambda}{1+\lambda},\qquad
 P=(1-\tau)^4,36\Gamma\!\left(\frac{\tau}{1-\tau}\right).
\]

The natural degree in `(S,u,v,tau)` is `(4,4,8,4)`.  Its `1125` exact
Bernstein controls comprise `945` positive values and exactly `180` zeros:

\[
 (i_S,i_u,i_v,i_\tau)=(0,i_u,i_v,i_\tau),
 \quad 0\le i_u\le4,\quad0\le i_v\le8,\quad1\le i_\tau\le4.
\]

Thus every zero lies solely on the artificial `S=0` closure; there are no
other zeros and no negative controls.  The least positive full control is
`33605/98304` at `(1,4,8,1)`.  Neither `S=0` nor `tau=1` is an original point:
the former is only the displacement closure, and the latter is projective
positive-scale infinity.

The exact face audit is:

- `tau=0`: one control, equal to `5`;
- `tau=1`, after division by the positive original-domain factor `S`:
  `180/180` controls positive, least
  `1152452992382662513/307792887033102336` at `(0,4,8)`;
- `x=0`: `225` controls, exactly `36` artificial `S=0` zeros, least positive
  `51090800938045/133590662774784` at `(1,8,3)`;
- `x=1/8`: `225` controls, exactly `36` artificial `S=0` zeros, least
  positive `33605/98304` at `(1,8,1)`;
- `y=-1/64`: `125` controls, exactly `20` artificial `S=0` zeros, least
  positive `37445/98304` at `(1,4,1)`;
- `y=+1/64`: `125` controls, exactly `20` artificial `S=0` zeros, least
  positive `33605/98304` at `(1,4,1)`.

The `y=0` center section contains the already independently audited bridge
arc.  The complete `x=1/8` face of this tube lies on the independently
audited center-box boundary `Z=31/32`.  This theorem opens the arc in one
complex-phase direction but does not fill a three-dimensional cap.

## Independent raw calibration and adversarial gates

At the legal nonzero-phase point

\[
 (h,q,\lambda,x,y,Z)=
 \left(\frac35,\frac45,\frac75,\frac1{16},
       \frac1{128},\frac{251}{256}\right),
\]

the unreduced fully conjugated matrix expression and the reduced quartic
agree exactly at

\[
 36\Gamma=
 \frac{2190361703821949821239444799}
      {52776558133248000000000000}.
\]

The source verifier succeeds normally and fails closed under optimized
Python, a deliberately corrupted dependency hash, and deletion of one raw
`C_4` monomial.  The deleted-term attack is detected as the exact residue

\[
 \frac{25}{81}S^4\lambda^4x^4.
\]

Syntax compilation is directed to a temporary path, so the audit adds no
project-local bytecode cache.  No real-part monotonicity (CE-046),
feasible-center absorption (CE-048), fixed allocation `s=-2` (CE-059), or
the rejected `Z=0` baseline quadratic remainder (CE-060) is used.

Run from the checkpoint root:

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=tmp/research/pydeps:tmp/research \
python3 tmp/research/verify_common_metric_ranktwo_transverse_compact_ball_axis_cap_bridge_phase_tube_theorem.py
```

The exact discovery provenance is
`tmp/research/compact_ball_axis_cap_bridge_phase_tube_discovery.py`.  The
bound source set is listed in
`tmp/research/common_metric_ranktwo_transverse_compact_ball_axis_cap_bridge_phase_tube_theorem_manifest.sha256`.

