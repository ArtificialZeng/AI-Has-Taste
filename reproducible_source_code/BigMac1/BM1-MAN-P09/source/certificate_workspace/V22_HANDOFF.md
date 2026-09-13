# V22 handoff: the real three-dimensional gate is closed; the complex phase is live

Date: 2026-08-18.

## 1. Honest status

The optimal spectral constant of a general fixed crossing lens remains open.
No result in this checkpoint covers both every admissible operator and every
admissible rational function.  The current PDF is a rigorous partial-results
paper, not a solution of the original problem.

The primary live route is the common-metric theorem.  For finite-dimensional
positive semidefinite matrices `P,Q`, put

```text
A=((1+i)P+(1-i)Q)/2,       B=A^2.
```

The target is a Hermitian metric

```text
I <= G <= 2I,              B^*G+GB >= 0.
```

Equivalently, every positive density `W` should satisfy

```text
||BW+WB^*||_1 + 6 Re tr(BW) >= 0.
```

The theorem is known in dimension two.  V22 records the exact closure of the
first full real-symmetric rank-one-side chart in dimension three and isolates
the remaining irreducible complex phase.

## 2. New exact real-symmetric theorem

Take the balanced rank-two density

```text
W=diag(1,1,0)/2,
```

and suppose one positive side is rank one.  After the audited unitary and
scale normalizations, write its range vector as `p=(a,0,c)` with
`a^2+c^2=1`.  If the other side `Q` is an arbitrary real symmetric positive
semidefinite `3 x 3` matrix, then the dangerous scalar compression/leakage
gate is always nonnegative.

The final identity is stronger than the earlier endpoint split.  In the
notation of the proof,

```text
G(Q)=(ac-sigma^2 u)^2/4
     +sigma^2(B+tH)
     +s^2(q-q0)^2/4,
```

where `B>=0` and `H>0` on the whole dangerous domain.  It handles, without
separate optimization assumptions,

- `q_min>q0` and `q0>=q_min`;
- every feasible scalar completion `q>=q_min`;
- the singular active-block boundary;
- the coordinate face `Q_32=0`;
- all scale and endpoint degeneracies by exact limits.

Read:

```text
tmp/research/common_metric_tilted_rankone_real_symmetric_full_gate.md
tmp/research/verify_common_metric_tilted_rankone_real_symmetric_full_gate.py
audit/COMMON_METRIC_TILTED_RANKONE_REAL_SYMMETRIC_FULL_GATE_REFEREE_AUDIT.md
```

The independent referee reconstructed the original gate entries, the Schur
completion and kernel, every boundary branch, and exact test data.  This is a
theorem for the stated scalar gate.  It is not yet the full complex Hermitian
chart, the full `M_3` common-metric theorem, or the fixed-lens theorem.

## 3. Lean trust boundary

The stable algebraic core of the real theorem is formalized in

```text
formal/RightAngleTiltedRankOneRealGateAlgebra.lean
```

under the locked Lean 4.28.0/mathlib environment.  It contains no `sorry`,
`admit`, or project axiom; its printed axioms are only the standard mathlib
ones.  It formalizes the arbitrary-`q` identity, the two scalar completions,
the final square decomposition, and conditional nonnegativity.

It deliberately does not formalize the unitary normalization, extraction of
the PSD parameters, the singular boundary, the `Q_32=0` bridge, or any
complex/common-metric/fixed-lens conclusion.  Read the exact scope before
using it:

```text
tmp/research/common_metric_tilted_rankone_real_gate_lean_scope.md
tmp/research/right_angle_tilted_rankone_real_gate_lean_build.log
```

## 4. Exact endpoint Minkowski interface

For the stronger endpoint pencil

```text
M(t)=[[G+t^2 I, t w], [t w^T, delta+beta t^2]],
```

positivity for every real `t` is exactly equivalent to the Minkowski
inclusion

```text
w in sqrt(beta) G^(1/2) Ball + sqrt(delta) Ball,
```

equivalently to a split `w=w0+w1` with

```text
w0^T G^(-1) w0 <= beta,       ||w1||^2 <= delta.
```

This equivalence has an explicit degree-one `6 x 6` Gram completion.  It is
useful as a separate structural interface but is no longer needed to prove
the real-symmetric actual gate, which the identity in Section 2 closes
directly.  The sector-specific Minkowski inclusion is not proved in general.

Read:

```text
tmp/research/common_metric_endpoint_minkowski_equivalence.md
tmp/research/verify_common_metric_endpoint_minkowski_equivalence.py
audit/COMMON_METRIC_ENDPOINT_MINKOWSKI_EQUIVALENCE_REFEREE_AUDIT.md
```

## 5. The complex phase cannot be discarded

The shortcut `G(Q)>=G(Re Q)` is exactly false, even when both matrices are
strictly positive and both scalar gates are positive.  The recorded witness
has

```text
G(Q)-G(Re Q)=-49803/800000<0.
```

Thus a proof of the complex chart must retain the irreducible Hermitian
phase.  This is CE-046, a route obstruction only, not a scalar-gate,
common-metric, or fixed-lens counterexample.

Read:

```text
tmp/research/common_metric_tilted_rankone_complex_phase_realpart_no_go.md
tmp/research/verify_common_metric_tilted_rankone_complex_phase_realpart_no_go.py
audit/COMMON_METRIC_TILTED_RANKONE_COMPLEX_PHASE_REALPART_NO_GO_REFEREE_AUDIT.md
```

## 6. New complex partial theorems

No legal negative scalar-gate datum has been found.  Two exact families are
now proved:

1. In the slice with real `Q_12` and one phase in `Q_13`, the entire half
   phase `tau<=0` is positive whenever the unconstrained scalar minimizer is
   feasible, `q0>=q_min`; the exact lifting then covers every
   `q>=q_min`.
2. Two explicit one-phase sign cones, one for an imaginary part in `Q_13`
   and one for an imaginary part in `Q_12`, are positive by an exact phase
   increment from the real theorem.  The notes also contain strictly
   positive genuinely complex interval families.
3. A genuine simultaneous-phase cone is positive whenever the three exact
   phase pairings have the required signs.  It contains a strict positive-
   definite two-parameter family with both imaginary phases nonzero.

Read:

```text
tmp/research/common_metric_tilted_rankone_complex_phase_half_slice_theorem.md
tmp/research/verify_common_metric_tilted_rankone_complex_phase_half_slice_theorem.py
tmp/research/audit/COMMON_METRIC_TILTED_RANKONE_COMPLEX_PHASE_HALF_SLICE_REFEREE_AUDIT.md
tmp/research/common_metric_tilted_rankone_complex_onephase_cones.md
tmp/research/verify_common_metric_tilted_rankone_complex_onephase_cones.py
tmp/research/audit/COMMON_METRIC_TILTED_RANKONE_COMPLEX_ONEPHASE_CONES_REFEREE_AUDIT.md
tmp/research/common_metric_tilted_rankone_complex_simultaneous_phase_cone.md
tmp/research/verify_common_metric_tilted_rankone_complex_simultaneous_phase_cone.py
tmp/research/audit/COMMON_METRIC_TILTED_RANKONE_COMPLEX_SIMULTANEOUS_PHASE_CONE_REFEREE_AUDIT.md
```

All three partial theorems have independent PASS audits.  The complementary
simultaneous-phase region, the opposite half phase, and the universal sign
on the branch `q0<q_min` remain open.
Numerical searches with no negative values are discovery evidence only.

Two exact reductions now preserve the whole remaining two-phase problem.
On the strict active Schur chart,

```text
q_min=[t(u^2+v^2)+r s^2-2s(uz+vw)]/[rt-z^2-w^2],
```

and the gate is a single quadratic in the scalar completion.  The full phase
increment from the entrywise-real datum has an exact square completion with
a strictly positive leading coefficient.  On the complementary branch
`q_min>q_0`, clearing denominators gives one polynomial identity

```text
4 Delta^2 G(q_min)
 =Delta^2[4a^2(L^2+a^2v^2)+R1^2+I1^2+R2^2-32a^2x^2]+J^2.
```

The formula and branch direction are independently audited; universal
nonnegativity of this polynomial is the smallest current sign problem.

```text
tmp/research/common_metric_tilted_rankone_complex_full_phase_reduction.md
tmp/research/verify_common_metric_tilted_rankone_complex_full_phase_reduction.py
audit/COMMON_METRIC_TILTED_RANKONE_COMPLEX_FULL_PHASE_REDUCTION_REFEREE_AUDIT.md
tmp/research/common_metric_tilted_rankone_complex_schur_boundary_polynomial.md
tmp/research/verify_common_metric_tilted_rankone_complex_schur_boundary_polynomial.py
tmp/research/audit/COMMON_METRIC_TILTED_RANKONE_COMPLEX_SCHUR_BOUNDARY_POLYNOMIAL_REFEREE_AUDIT.md
```

The boundary sign problem has a further exact one-variable reduction.  Write
`u=s k`, `v=s ell`, and `T=s^2`.  Once the active block and the coupling
direction are fixed, the legal complementary branch is a half-line and the
cleared actual gate is a strictly convex cubic

```text
P(T)=C0+C1 T+C2 T^2+n^2 T^3.
```

Its sign on the whole half-line is equivalent to the finite endpoint,
derivative, and cubic-discriminant alternatives in the following audited
note.  The remaining task is therefore a uniform shape-sign theorem, not an
eight-variable blind polynomial expansion.

```text
tmp/research/common_metric_tilted_rankone_complex_boundary_scale_cubic.md
tmp/research/verify_common_metric_tilted_rankone_complex_boundary_scale_cubic.py
audit/COMMON_METRIC_TILTED_RANKONE_COMPLEX_BOUNDARY_SCALE_CUBIC_REFEREE_AUDIT.md
```

One genuinely opposite-phase rank-two boundary family is proved positive on
a closed parameter interval, but this is only a strict partial theorem.  On
the feasible-center branch, CE-048 shows that the proposed phase-absorption
inequality is not implied by positive definiteness; the actual gate on that
witness stays positive.  CE-049 separately rules out the four fixed metrics
obtained from the kernel/support projection of `Q` or the range/kernel
projection of `P`; the same datum has an explicit strict unrestricted metric.
Neither certificate is a gate, common-metric, or fixed-lens counterexample.

The first scale-cubic endpoint sign is now partly closed.  If `g<=0`, then
`T_L=0` and the endpoint is exactly the proved reducing-plane face, so
`g_0=P(0)>=0`.  If `g>0`, every legal endpoint admits a lossless two-column
rank-two Gram chart; the condition `q_min=q_g` becomes one exact relation and
the remaining endpoint sign is the compact identity
`g_0=4 Delta^2 G(Q)`.  The latter sign remains open.  Read:

```text
tmp/research/common_metric_tilted_rankone_complex_endpoint_shape_partial.md
tmp/research/verify_common_metric_tilted_rankone_complex_endpoint_shape_partial.py
audit/COMMON_METRIC_TILTED_RANKONE_COMPLEX_ENDPOINT_SHAPE_PARTIAL_REFEREE_AUDIT.md
```

On the positive-`g` side, one genuine complex rank-two face is completely
closed.  For `Q(rho)=uu^*+rho e_1e_1^*`, the endpoint gate is quadratic on a
finite danger interval.  The earlier nonpositive-leading-coefficient case
uses concavity; the complementary case follows from the exact strict identity
`F'(0)/2=a(32a^2H+cK)>0`.  Thus every legal parameter on this face is covered.
Read:

```text
tmp/research/common_metric_tilted_rankone_complex_endpoint_diagonal_atom_face.md
tmp/research/verify_common_metric_tilted_rankone_complex_endpoint_diagonal_atom_face.py
audit/COMMON_METRIC_TILTED_RANKONE_COMPLEX_ENDPOINT_DIAGONAL_ATOM_FACE_REFEREE_AUDIT.md
tmp/research/common_metric_tilted_rankone_complex_endpoint_diagonal_atom_face_complete.md
tmp/research/verify_common_metric_tilted_rankone_complex_endpoint_diagonal_atom_face_complete.py
audit/COMMON_METRIC_TILTED_RANKONE_COMPLEX_ENDPOINT_DIAGONAL_ATOM_FACE_COMPLETE_REFEREE_AUDIT.md
```

A general second Gram atom is not covered.

There is also an exact spectral reduction of every rank-two boundary matrix
`Q=lambda_1 q_1q_1^*+lambda_2 q_2q_2^*` to a two-variable quartic retaining
all mixed terms.  Its leading homogeneous form is a positive Gram.  The
entire equal-positive-eigenvalue slice `Q=lambda(I-nn^*)` is now proved for
arbitrary complex phases, and the coefficient `8` is sharp on an explicit
rank-two projector.  The proof and independent audit are:

```text
tmp/research/common_metric_tilted_rankone_ranktwo_spectral_quartic.md
tmp/research/verify_common_metric_tilted_rankone_ranktwo_spectral_quartic.py
audit/COMMON_METRIC_TILTED_RANKONE_RANKTWO_SPECTRAL_QUARTIC_REFEREE_AUDIT.md
audit/verify_common_metric_tilted_rankone_ranktwo_spectral_quartic_referee.py
```

Unequal positive eigenvalues remain an exact coercive half-line quartic sign
problem.  This new theorem attacks the rank-two boundary only; it does not
settle the feasible-center rank-three branch.

That unequal-eigenvalue interface has two additional audited advances.  On
each fixed dangerous spectral frame and eigenvalue-ratio ray, the coercive
quartic is nonnegative exactly when one scalar allocation `s<=-2` leaves a
copositive quadratic.  Separately, if the kernel is fixed to the sharp
projector kernel, every `2 x 2` PSD compression on its orthogonal complement
is positive; this covers arbitrary unequal eigenvalues and complex spectral
directions and has unequal-eigenvalue sharp equalities.  Read:

```text
tmp/research/common_metric_ranktwo_spectral_ray_one_parameter_copositivity.md
audit/COMMON_METRIC_RANKTWO_SPECTRAL_RAY_ONE_PARAMETER_COPOSITIVITY_REFEREE_AUDIT.md
tmp/research/common_metric_ranktwo_sharp_kernel_full_cone.md
audit/COMMON_METRIC_RANKTWO_SHARP_KERNEL_FULL_CONE_REFEREE_AUDIT.md
```

Do not freeze that allocation at `s=-2`.  CE-059 gives an independently
audited legal rank-two transverse ray with eigenvalues `1` and `1/1000` and
strict danger for which the normalized quartic has `b+4<0`; the `s=-2`
residual quadratic therefore has a negative leading coefficient.  An exact
Sturm certificate simultaneously proves that the actual gate is strictly
positive for every scale on the same ray.  The fixed-ray criterion remains
existential in a ray-dependent `s`; the obstruction is not a gate,
common-metric, or fixed-lens counterexample.  Read:

```text
tmp/research/common_metric_transverse_fixed_minus_two_allocation_no_go.md
tmp/research/verify_common_metric_transverse_fixed_minus_two_allocation_no_go.py
audit/COMMON_METRIC_TRANSVERSE_FIXED_MINUS_TWO_ALLOCATION_NO_GO_REFEREE_AUDIT.md
audit/verify_common_metric_transverse_fixed_minus_two_allocation_no_go_referee.py
```

The fixed sharp kernel is now subsumed by a larger theorem: every planar
kernel `n=(b,0,d zeta)` and every `2 x 2` PSD compression on `n^perp`
satisfy the gate, with arbitrary unequal eigenvalues and complex mixing.
The full-phase separation and two convex KKT branches are independently
audited in:

```text
tmp/research/common_metric_ranktwo_planar_kernel_full_cone.md
tmp/research/verify_common_metric_ranktwo_planar_kernel_full_cone.py
audit/COMMON_METRIC_RANKTWO_PLANAR_KERNEL_FULL_CONE_REFEREE_AUDIT.md
audit/verify_common_metric_ranktwo_planar_kernel_full_cone_referee.py
```

The remaining rank-two issue is therefore specifically the nonplanar kernel
layer `n_2!=0`, not unequal eigenvalues on a planar kernel.  One exact
nonplanar path is now known: starting at the sharp planar kernel and ending
at `e_2`, every diagonal compression in the co-moving support basis satisfies
the gate for every eigenvalue ratio.  Here `36 Gamma` is a strictly concave
quadratic in the squared transverse displacement, so its planar,
danger-zero, and reducing-plane endpoints close the full danger interval.
Read:

```text
tmp/research/common_metric_ranktwo_sharp_kernel_transverse_diagonal_cone.md
tmp/research/verify_common_metric_ranktwo_sharp_kernel_transverse_diagonal_cone.py
audit/COMMON_METRIC_RANKTWO_SHARP_KERNEL_TRANSVERSE_DIAGONAL_CONE_REFEREE_AUDIT.md
audit/verify_common_metric_ranktwo_sharp_kernel_transverse_diagonal_cone_referee.py
```

This path does not yet allow a complex off-diagonal compression in its
moving support basis, and it does not cover arbitrary nonplanar kernels.

For the full off-diagonal compression on this path there is nevertheless a
lossless one-variable reduction.  With compression
`[[u,X+iY],[X-iY,v]]`, `X^2+Y^2<=uv`, danger is a single displacement
interval and `36 Gamma` is an explicit phase-retaining quartic with both
closed endpoints controlled.  Two exact positive-gate witnesses show that
the quartic need not be concave and that mixing need not increase the gate.
Read:

```text
tmp/research/common_metric_ranktwo_sharp_kernel_transverse_offdiagonal_quartic.md
tmp/research/verify_common_metric_ranktwo_sharp_kernel_transverse_offdiagonal_quartic.py
audit/COMMON_METRIC_RANKTWO_SHARP_KERNEL_TRANSVERSE_OFFDIAGONAL_QUARTIC_REFEREE_AUDIT.md
audit/verify_common_metric_ranktwo_sharp_kernel_transverse_offdiagonal_quartic_referee.py
```

The quartic interior sign remains open.

The complete dangerous transverse compression cone now has a lossless
compact chart.  For every `h>0`, an exact Cholesky parameterization covers
all complex `2 x 2` PSD compressions in danger, and affine shape coordinates
turn the condition exactly into `x^2+y^2+z^2<1`.  The original Hermitian
gate is

```text
36 Gamma = 5 + h^2 sum_(m=1)^4 lambda^m F_m(h^2,x,y,z),
```

with rational `F_m` and one positive unbounded scale `lambda`.  The
independent audit reconstructs the inverse map, raw `Q,Q^2` identity,
coefficient counts `6,38,69,225`, degree bounds, and leading Gram square.
The `h=0` planar cone is the separately proved boundary; the polynomial
value at `h=0` is only a closure, not a fixed-scale inverse chart.  Read:

```text
tmp/research/common_metric_ranktwo_transverse_full_cone_compact_ball_reduction.md
tmp/research/verify_common_metric_ranktwo_transverse_full_cone_compact_ball_reduction.py
audit/COMMON_METRIC_RANKTWO_TRANSVERSE_FULL_CONE_COMPACT_BALL_REDUCTION_REFEREE_AUDIT.md
audit/verify_common_metric_ranktwo_transverse_full_cone_compact_ball_reduction_referee.py
```

The sign of this compact-ball quartic is now the precise transverse theorem.

Its complete center axis is already proved.  On `x=y=0`, for every
`0<h<=1`, `-1<=z<=1`, and every positive scale, the raw gate is strictly
positive.  In `S=h^2,Z=z^2`, all coefficients except possibly `C_2` are
strictly positive.  Exact localization confines `C_2<0` to
`S>55/72,Z<1/20`, where twenty positive Bernstein controls certify
`4C_0C_4-C_2^2>0`.  The independent audit works with signed `z` and covers
the rank-one, rank-two, and zero-danger boundaries.  Read:

```text
tmp/research/common_metric_ranktwo_transverse_compact_ball_center_axis_theorem.md
tmp/research/verify_common_metric_ranktwo_transverse_compact_ball_center_axis_theorem.py
audit/COMMON_METRIC_RANKTWO_TRANSVERSE_COMPACT_BALL_CENTER_AXIS_THEOREM_REFEREE_AUDIT.md
audit/verify_common_metric_ranktwo_transverse_compact_ball_center_axis_theorem_referee.py
```

The center axis has now been opened transversely on a large truncated
segment.  For every `0<h<=1`, every positive scale,

```text
|x|,|y|<=1/8,   z^2<=31/32,
```

the raw gate is strictly positive.  Exact coefficient certificates prove
`C_1,C_3,C_4>0`, localize `C_2<0` to `S>1/4,Z<1/6`, and prove
`4C_0C_4-C_2^2>0` there.  An independent nodal/affine Bernstein
reconstruction verifies all 4,146 positive controls.  This is a genuine
five-real-parameter neighborhood of the truncated axis segment, not a
superset of the complete center-axis theorem: it omits the two caps
`31/32<z^2<=1`.  Read:

```text
tmp/research/common_metric_ranktwo_transverse_compact_ball_center_box_theorem.md
tmp/research/verify_common_metric_ranktwo_transverse_compact_ball_center_box_theorem.py
audit/COMMON_METRIC_RANKTWO_TRANSVERSE_COMPACT_BALL_CENTER_BOX_THEOREM_REFEREE_AUDIT.md
audit/verify_common_metric_ranktwo_transverse_compact_ball_center_box_theorem_referee.py
```

The full compact ball outside the union of the center box and the two
axis caps remains open.

A second interior region is proved around the negative meridian at a
different fixed nonplanar kernel.  Set `eta=1/2`, take every phase
`s in RP^1`, every positive scale, every spectral ratio `0<=k<=1`, and

```text
-65/64 <= r <= -63/64.
```

The gate is nonnegative and the datum is strictly dangerous throughout.
Two projective phase charts, a double blow-up at the equality, and off-local
Bernstein covers give 49,840 exact positive controls.  Equality is exactly
`r=-1,k=0,t=1`, with arbitrary phase.  The independent audit reconstructs
the raw Hermitian gate and every control using a separate nodal transform.
Read:

```text
tmp/research/common_metric_ranktwo_sharp_kernel_transverse_full_phase_negative_meridian_collar.md
tmp/research/verify_common_metric_ranktwo_sharp_kernel_transverse_full_phase_negative_meridian_collar.py
audit/COMMON_METRIC_RANKTWO_SHARP_KERNEL_TRANSVERSE_FULL_PHASE_NEGATIVE_MERIDIAN_COLLAR_REFEREE_AUDIT.md
audit/verify_common_metric_ranktwo_sharp_kernel_transverse_full_phase_negative_meridian_collar_referee.py
```

This is a fixed-kernel collar, not a full-ball theorem.

A first genuinely complex off-diagonal ray is nevertheless proved.  On
`u=v+1`, `(X,Y)=(3 omega,omega)`, `omega<=0`, the phase contribution to the
danger scalar cancels and the gate is a concave even quadratic in the squared
displacement plus a nonnegative odd reserve.  Exact formulas control both
possible right endpoints and preserve sharpness.  Read:

```text
tmp/research/common_metric_ranktwo_sharp_kernel_transverse_phase_ray_theorem.md
tmp/research/verify_common_metric_ranktwo_sharp_kernel_transverse_phase_ray_theorem.py
audit/COMMON_METRIC_RANKTWO_SHARP_KERNEL_TRANSVERSE_PHASE_RAY_THEOREM_REFEREE_AUDIT.md
audit/verify_common_metric_ranktwo_sharp_kernel_transverse_phase_ray_theorem_referee.py
```

At this intermediate stage the opposite ray `omega>0` was open; it is
completed in the next paragraph.  All other mixing ratios remain open.

The opposite ray is now also closed, so the complete two-sided phase line
`(X,Y)=(3 omega,omega)` is proved.  The new proof completes the phase quartic
square and reduces the remaining sign to two shape polynomials with exact
Bernstein-positive certificates on both danger charts.  Read:

```text
tmp/research/common_metric_ranktwo_sharp_kernel_transverse_phase_line_completion.md
tmp/research/verify_common_metric_ranktwo_sharp_kernel_transverse_phase_line_completion.py
audit/COMMON_METRIC_RANKTWO_SHARP_KERNEL_TRANSVERSE_PHASE_LINE_COMPLETION_REFEREE_AUDIT.md
audit/verify_common_metric_ranktwo_sharp_kernel_transverse_phase_line_completion_referee.py
```

All phase ratios away from `X=3Y` remain open.

A complementary exact box controls an entire spectral-ratio direction rather
than one phase line.  For the fixed complex spectral frame in the following
files, every scale `t>0`, every ratio `0<=k<=1`, and the nonplanar interval
`sqrt(2)/8<=eta<=sqrt(2)/4` are strictly positive.  Compactifying scale
produces a rational tridegree-`(4,4,4)` polynomial whose `41^3` degree-forty
tensor Bernstein coefficients are all strictly positive.  Two independent
algorithms reconstruct the same exact certificate.

```text
tmp/research/common_metric_ranktwo_sharp_kernel_transverse_spectral_ratio_box.md
tmp/research/verify_common_metric_ranktwo_sharp_kernel_transverse_spectral_ratio_box.py
audit/COMMON_METRIC_RANKTWO_SHARP_KERNEL_TRANSVERSE_SPECTRAL_RATIO_BOX_REFEREE_AUDIT.md
audit/verify_common_metric_ranktwo_sharp_kernel_transverse_spectral_ratio_box_referee.py
```

This fixed-frame theorem is subsumed by the equatorial interval below.

The fixed frame can be rotated along a nontrivial equatorial phase interval.
For `|s|<=1/100`, every scale, all spectral ratios, and the same nonplanar
kernel interval remain strictly positive.  The compact gate is a rational
multidegree-`(4,4,4,4)` polynomial; 256 local boxes contain 160,000 strictly
positive Bernstein controls, and an independent transform verifies 96,000
shared-face identities.

```text
tmp/research/common_metric_ranktwo_sharp_kernel_transverse_spectral_frame_open_box.md
tmp/research/verify_common_metric_ranktwo_sharp_kernel_transverse_spectral_frame_open_box.py
audit/COMMON_METRIC_RANKTWO_SHARP_KERNEL_TRANSVERSE_SPECTRAL_FRAME_OPEN_BOX_REFEREE_AUDIT.md
audit/verify_common_metric_ranktwo_sharp_kernel_transverse_spectral_frame_open_box_referee.py
```

The word “interval” is essential: this varies only one Bloch-equator phase
parameter, not the transverse latitude.  It is not an open neighborhood in
the full two-real-dimensional spectral-frame manifold, and is subsumed by
the local two-parameter theorem below.

The latitude parameter is now opened as well.  With the same equatorial
coordinate `|s|<=1/100` and an independent latitude coordinate `r`, the two
tangent directions are independent on the Bloch sphere.  For every scale,
every ratio `0<=k<=1`, and `sqrt(2)/8<=eta<=sqrt(2)/4`, a direct latitude
Bernstein certificate proves the gate throughout `|r|<=1/2`.  It substitutes
`r=R(2u-1)` before converting to Bernstein form, so cancellations among all
eight latitude powers are retained.  On 256 base-variable subboxes, all
1,440,000 exact five-dimensional controls are strictly positive at `R=1/2`.
An independent implementation based on nodal interpolation rather than the
source binomial conversion reproduces the same unique minimum.  Separately,
exact maximization of the danger functional proves that every datum in the
complete smaller box `|r|<=2/9` is strictly dangerous.  The outer band is
claimed only gate-positive.

```text
tmp/research/common_metric_ranktwo_sharp_kernel_transverse_spectral_frame_two_parameter_box.md
tmp/research/verify_common_metric_ranktwo_sharp_kernel_transverse_spectral_frame_two_parameter_box.py
audit/COMMON_METRIC_RANKTWO_SHARP_KERNEL_TRANSVERSE_SPECTRAL_FRAME_TWO_PARAMETER_BOX_REFEREE_AUDIT.md
audit/verify_common_metric_ranktwo_sharp_kernel_transverse_spectral_frame_two_parameter_box_referee.py
tmp/research/common_metric_ranktwo_sharp_kernel_transverse_spectral_frame_two_parameter_box_enlargement.md
tmp/research/verify_common_metric_ranktwo_sharp_kernel_transverse_spectral_frame_two_parameter_box_enlargement.py
tmp/research/audit/COMMON_METRIC_RANKTWO_SHARP_KERNEL_TRANSVERSE_SPECTRAL_FRAME_TWO_PARAMETER_BOX_ENLARGEMENT_REFEREE_AUDIT.md
tmp/research/audit/verify_common_metric_ranktwo_sharp_kernel_transverse_spectral_frame_two_parameter_box_enlargement_audit.py
tmp/research/common_metric_ranktwo_sharp_kernel_transverse_spectral_frame_local_bernstein_enlargement.md
tmp/research/verify_common_metric_ranktwo_sharp_kernel_transverse_spectral_frame_local_bernstein_enlargement.py
tmp/research/audit/COMMON_METRIC_RANKTWO_SHARP_KERNEL_TRANSVERSE_SPECTRAL_FRAME_LOCAL_BERNSTEIN_ENLARGEMENT_REFEREE_AUDIT.md
tmp/research/audit/verify_common_metric_ranktwo_sharp_kernel_transverse_spectral_frame_local_bernstein_enlargement_audit.py
tmp/research/common_metric_ranktwo_sharp_kernel_transverse_spectral_frame_direct_r_bernstein.md
tmp/research/verify_common_metric_ranktwo_sharp_kernel_transverse_spectral_frame_direct_r_bernstein.py
audit/COMMON_METRIC_RANKTWO_SHARP_KERNEL_TRANSVERSE_SPECTRAL_FRAME_DIRECT_R_BERNSTEIN_REFEREE_AUDIT.md
audit/verify_common_metric_ranktwo_sharp_kernel_transverse_spectral_frame_direct_r_bernstein_referee.py
tmp/research/common_metric_ranktwo_sharp_kernel_transverse_spectral_frame_subboxed_reciprocal.md
tmp/research/verify_common_metric_ranktwo_sharp_kernel_transverse_spectral_frame_subboxed_reciprocal.py
audit/COMMON_METRIC_RANKTWO_SHARP_KERNEL_TRANSVERSE_SPECTRAL_FRAME_SUBBOXED_RECIPROCAL_REFEREE_AUDIT.md
audit/verify_common_metric_ranktwo_sharp_kernel_transverse_spectral_frame_subboxed_reciprocal_referee.py
tmp/research/common_metric_ranktwo_sharp_kernel_transverse_spectral_frame_positive_seam.md
tmp/research/verify_common_metric_ranktwo_sharp_kernel_transverse_spectral_frame_positive_seam.py
audit/COMMON_METRIC_RANKTWO_SHARP_KERNEL_TRANSVERSE_SPECTRAL_FRAME_POSITIVE_SEAM_REFEREE_AUDIT.md
audit/verify_common_metric_ranktwo_sharp_kernel_transverse_spectral_frame_positive_seam_referee.py
tmp/research/common_metric_ranktwo_sharp_kernel_transverse_spectral_frame_negative_seam_equality.md
tmp/research/verify_common_metric_ranktwo_sharp_kernel_transverse_spectral_frame_negative_seam_equality.py
audit/COMMON_METRIC_RANKTWO_SHARP_KERNEL_TRANSVERSE_SPECTRAL_FRAME_NEGATIVE_SEAM_EQUALITY_REFEREE_AUDIT.md
audit/verify_common_metric_ranktwo_sharp_kernel_transverse_spectral_frame_negative_seam_equality_referee.py
tmp/research/common_metric_ranktwo_sharp_kernel_transverse_spectral_frame_negative_meridian_face.md
tmp/research/verify_common_metric_ranktwo_sharp_kernel_transverse_spectral_frame_negative_meridian_face.py
audit/COMMON_METRIC_RANKTWO_SHARP_KERNEL_TRANSVERSE_SPECTRAL_FRAME_NEGATIVE_MERIDIAN_FACE_REFEREE_AUDIT.md
audit/verify_common_metric_ranktwo_sharp_kernel_transverse_spectral_frame_negative_meridian_face_referee.py
tmp/research/common_metric_negative_meridian_uniform_local_minimum.md
tmp/research/verify_common_metric_negative_meridian_uniform_local_minimum.py
audit/COMMON_METRIC_NEGATIVE_MERIDIAN_UNIFORM_LOCAL_MINIMUM_REFEREE_AUDIT.md
audit/verify_common_metric_negative_meridian_uniform_local_minimum_referee.py
tmp/research/common_metric_ranktwo_sharp_kernel_transverse_spectral_frame_negative_seam_collars.md
tmp/research/verify_common_metric_ranktwo_sharp_kernel_transverse_spectral_frame_negative_seam_collars.py
audit/COMMON_METRIC_RANKTWO_SHARP_KERNEL_TRANSVERSE_SPECTRAL_FRAME_NEGATIVE_SEAM_COLLARS_REFEREE_AUDIT.md
audit/verify_common_metric_ranktwo_sharp_kernel_transverse_spectral_frame_negative_seam_collars_referee.py
tmp/research/common_metric_ranktwo_sharp_kernel_transverse_spectral_frame_negative_gap_blowup.md
tmp/research/verify_common_metric_ranktwo_sharp_kernel_transverse_spectral_frame_negative_gap_blowup.py
audit/COMMON_METRIC_RANKTWO_SHARP_KERNEL_TRANSVERSE_SPECTRAL_FRAME_NEGATIVE_GAP_BLOWUP_REFEREE_AUDIT.md
audit/verify_common_metric_ranktwo_sharp_kernel_transverse_spectral_frame_negative_gap_blowup_referee.py
```

Splitting the central latitude interval and reversing the degree-eight
polynomial on `q=1/r` improves the audited union to
`(-infinity,-2] union [-2/3,2/3] union [1,infinity)`, including the projective
infinity point.  All 5,760,000 exact controls in the four direct/reciprocal
boxes are positive.  An adaptive 294-leaf exact tree then closes the positive
seam `[2/3,1]`, so the current gate-positive union is
`(-infinity,-2] union [-2/3,infinity)` before the collar refinement below.  This
is still a local phase/kernel box, not the full transverse compression cone.
On the negative seam, CE-058 gives a legal strict-danger equality at
`r=-1,k=0,t=1`: `Gamma=0`, with an exact slice factorization and equality
classification.  Thus the remaining theorem must be nonnegativity, not
strict positivity; CE-058 is not a negative gate counterexample.
The entire meridian face `r=-1` is now independently audited nonnegative for
every remaining kernel displacement, phase, scale, and spectral ratio in the
local box.  Its 160,000 exact Bernstein controls are all nonnegative, exactly
1,600 controls vanish, and the least positive control is `45/128`.  This
contains the CE-058 equality but does not control a neighborhood of `r=-1`
or classify every possible equality with positive spectral ratio.
The equality stratum `r=-1,k=0,x=1/2` is also a uniformly nondegenerate local
minimum.  Its inward `k` derivative is at least `6`, its transverse Hessian
is uniformly positive definite, and an exact Taylor-remainder audit gives an
explicit rational radius with
`J>=m((r+1)^2+(x-1/2)^2)/2+3k`.  This proves a genuine local neighborhood and
classifies equality there, but the certified radius is too conservative to
bridge the whole remaining latitude gap.
Exact direct and reciprocal collars additionally prove strict gate positivity
on `[-2,-8/7] union [-7/8,-2/3]`.  Their independently reconstructed
Bernstein certificates contain 2,880,000 strictly positive controls.  Hence
the last interval was `[-8/7,-7/8]`, with its central meridian already
nonnegative.  The final-gap blow-up now closes that interval exactly.  With
`u=r+1`, `v=2x-1`, the compact gate splits as `J=J_0+kA`; `A` has 4,500
strictly positive controls, while the lossless dominant charts `v=uz` and
`u=vz` divide out the exact quadratic equality and have 11,000 and 2,475
strictly positive controls.  Fourteen off-local leaves add 78,750 positive
controls.  The independent referee reconstructs the raw Hermitian `Q,Q^2`
gate and all 96,725 controls by nodal interpolation.  Consequently this fixed
transverse spectral family is nonnegative on the complete projective latitude
`r in RP^1`, with equality exactly at `r=-1,k=0,t=1`.  This does not extend
the result to arbitrary Bloch frames or kernels.
CE-054 records the obsolete global-bound limit
at `1/6228`.  At radius `1/23`, the current local absolute-coefficient lower
bound is negative; CE-055 records this obsolete route limit, not a negative
gate value.  At `R=1`, the unchanged direct-latitude tensor certificate has a
negative control coefficient; CE-057 records this route limit, again without
a negative gate value.

The diagonal-atom component of the positive-`g` endpoint is now completely
closed for every legal `0<a<1`, superseding the earlier `C_2<=0`/
`a^2>=1/33` partial result.  The exact identity

```text
F'(0)/2 = a(32a^2 H+cK),       H>0, K>0,
```

makes the `C_2>=0` quadratic monotone from the proved rank-one endpoint;
when `C_2<0`, the rank-one and danger-zero endpoints close the interval by
concavity.  Read:

```text
tmp/research/common_metric_tilted_rankone_complex_endpoint_diagonal_atom_face_complete.md
tmp/research/verify_common_metric_tilted_rankone_complex_endpoint_diagonal_atom_face_complete.py
audit/COMMON_METRIC_TILTED_RANKONE_COMPLEX_ENDPOINT_DIAGONAL_ATOM_FACE_COMPLETE_REFEREE_AUDIT.md
audit/verify_common_metric_tilted_rankone_complex_endpoint_diagonal_atom_face_complete_referee.py
```

A general second Gram atom is not diagonal in this sense, so the full
positive-`g` endpoint remains open.

One genuinely non-diagonal second-atom face is also closed.  If the two Gram
columns have nonzero active coordinates but are orthogonal, their spectral
square has no cross term and the exact endpoint gate is strictly increasing
throughout the dangerous interval.  This reduces it to the proved rank-one
endpoint.  Read:

```text
tmp/research/common_metric_tilted_rankone_complex_endpoint_orthogonal_atom_face.md
tmp/research/verify_common_metric_tilted_rankone_complex_endpoint_orthogonal_atom_face.py
audit/COMMON_METRIC_TILTED_RANKONE_COMPLEX_ENDPOINT_ORTHOGONAL_ATOM_FACE_REFEREE_AUDIT.md
audit/verify_common_metric_tilted_rankone_complex_endpoint_orthogonal_atom_face_referee.py
```

General nonorthogonal Gram columns retain the cyclic `Q^2` cross term.

The complete Hermitian PSD coordinate slice `Q_23=0` is nevertheless now
closed, at arbitrary rank.  The gate and danger condition are independent of
the free middle diagonal.  On the Schur boundary there is a lossless Gram
form `u=(beta,d,0)`, `v=(mu,0,e)`, and deleting `d` leaves danger unchanged
while changing four times the gate by

```text
d^2 |beta|^2 [4a^4+(ac-e Im(mu))^2+e^2 Re(mu)^2] >= 0.
```

The `d=0` datum is the proved reducing-plane theorem.  Rank, zero-coordinate,
and positive-completion degeneracies have been audited independently.

```text
tmp/research/common_metric_tilted_rankone_q23_zero_face_theorem.md
tmp/research/verify_common_metric_tilted_rankone_q23_zero_face_theorem.py
audit/COMMON_METRIC_TILTED_RANKONE_Q23_ZERO_FACE_REFEREE_AUDIT.md
audit/verify_common_metric_tilted_rankone_q23_zero_face_referee.py
```

A genuinely non-neutral `Q_23>0` endpoint-preserving three-parameter phase
cube is also closed.  The strict interior is rank two and generically complex
and non-neutral, and `0<lambda<1` is exactly the complete danger interval
within the displayed family.  The independent phase is
`Im zeta=7kappa-7/2`; the older strip is the `kappa=1/2` slice.  The first
Gram atom varies with the parameters to preserve the endpoint, so this is not
a fixed-base weight ray.  Exact controls give `D>=1/4000`, and all 245 native
tensor Bernstein coefficients of the raw cyclic gate are positive.

```text
tmp/research/common_metric_tilted_rankone_complex_endpoint_nonneutral_strip.md
tmp/research/verify_common_metric_tilted_rankone_complex_endpoint_nonneutral_strip.py
audit/COMMON_METRIC_TILTED_RANKONE_COMPLEX_ENDPOINT_NONNEUTRAL_STRIP_REFEREE_AUDIT.md
audit/verify_common_metric_tilted_rankone_complex_endpoint_nonneutral_strip_referee.py
tmp/research/common_metric_tilted_rankone_complex_endpoint_nonneutral_phase_box.md
tmp/research/verify_common_metric_tilted_rankone_complex_endpoint_nonneutral_phase_box.py
audit/COMMON_METRIC_TILTED_RANKONE_COMPLEX_ENDPOINT_NONNEUTRAL_PHASE_BOX_REFEREE_AUDIT.md
audit/verify_common_metric_tilted_rankone_complex_endpoint_nonneutral_phase_box_referee.py
```

General non-neutral endpoints remain open.

On one strict nonorthogonal subchart there is now a lossless exact reduction.
Assume `Q_23>0`, rank two, and a nonzero first entry in the second Gram
column.  Fixed endpoint neutrality is exactly one Euclidean circle in the
relative Gram angle.  The active determinant is strictly positive everywhere
on that circle, and the projective half-angle parameter turns the complete
cyclic gate into `P_6(t)/(1+t^2)^3`.  The sign of this sextic on its dangerous
set remains open.  Two exact positive-gate witnesses prove that the circle
is neither angularly convex/concave and that the gate need not be monotone in
the second-atom weight.  Read:

```text
tmp/research/common_metric_tilted_rankone_complex_endpoint_neutral_circle_reduction.md
tmp/research/verify_common_metric_tilted_rankone_complex_endpoint_neutral_circle_reduction.py
audit/COMMON_METRIC_TILTED_RANKONE_COMPLEX_ENDPOINT_NEUTRAL_CIRCLE_REDUCTION_REFEREE_AUDIT.md
audit/verify_common_metric_tilted_rankone_complex_endpoint_neutral_circle_reduction_referee.py
```

Non-neutral `Q_23!=0` endpoints are not covered by this chart; the separate
`Q_23=0` coordinate slice above is completely proved.

The fixed-base projective-circle theorem has now been enlarged to the broad
interval `b in [-1/4,-1/16]`, with
`a=3/5,c=4/5,gamma=1/8,e=1/4`.  For every base in this interval,
`tau in R union {infinity}` covers the entire neutral circle and
`0<=lambda<=1` is the exact danger closure.  An exact dominance identity
writes the raw gate as a strict reserve plus three squares and the positive
term `32a^2x_0^2 lambda(2-lambda)`; three univariate Bernstein checks prove
the reserve throughout the interval.

```text
tmp/research/common_metric_tilted_rankone_complex_endpoint_neutral_circle_projective_box.md
tmp/research/verify_common_metric_tilted_rankone_complex_endpoint_neutral_circle_projective_box.py
audit/COMMON_METRIC_TILTED_RANKONE_COMPLEX_ENDPOINT_NEUTRAL_CIRCLE_PROJECTIVE_BOX_REFEREE_AUDIT.md
audit/verify_common_metric_tilted_rankone_complex_endpoint_neutral_circle_projective_box_referee.py
tmp/research/common_metric_tilted_rankone_complex_endpoint_neutral_circle_base_interval.md
tmp/research/verify_common_metric_tilted_rankone_complex_endpoint_neutral_circle_base_interval.py
audit/COMMON_METRIC_TILTED_RANKONE_COMPLEX_ENDPOINT_NEUTRAL_CIRCLE_BASE_INTERVAL_REFEREE_AUDIT.md
audit/verify_common_metric_tilted_rankone_complex_endpoint_neutral_circle_base_interval_referee.py
```

CE-056 gives exact legal data with negative dominance reserve but positive
actual gate.  Thus this sufficient dominance method is not universal, and
the general projective sextic remains open.

```text
tmp/research/common_metric_endpoint_neutral_dominance_route_obstruction.md
tmp/research/verify_common_metric_endpoint_neutral_dominance_route_obstruction.py
audit/COMMON_METRIC_ENDPOINT_NEUTRAL_DOMINANCE_ROUTE_OBSTRUCTION_REFEREE_AUDIT.md
audit/verify_common_metric_endpoint_neutral_dominance_route_obstruction_referee.py
```

The negative reserve is nevertheless not a gate obstruction.  Fix
`a=95/193,c=168/193`, vary the normalized ratios `b/e`, `gamma/e` over the
displayed two-base rectangle, and independently vary their common scale
`s in [6/7,8/7]`, with `e=(37/200)s`.  Throughout this three-dimensional
base box one has `D>0`, `x_0<0`, and `H<0`, but the original cyclic gate is
strictly positive for the complete projective circle and all dangerous
weights.  Two rational charts give exact five-variable Bernstein
certificates, independently reconstructed by sparse nodal interpolation.

```text
tmp/research/common_metric_endpoint_neutral_beyond_dominance_base_interval.md
tmp/research/verify_common_metric_endpoint_neutral_beyond_dominance_base_interval.py
audit/COMMON_METRIC_ENDPOINT_NEUTRAL_BEYOND_DOMINANCE_BASE_INTERVAL_REFEREE_AUDIT.md
audit/verify_common_metric_endpoint_neutral_beyond_dominance_base_interval_referee.py
tmp/research/common_metric_endpoint_neutral_beyond_dominance_two_base_parameter_box.md
tmp/research/verify_common_metric_endpoint_neutral_beyond_dominance_two_base_parameter_box.py
audit/COMMON_METRIC_ENDPOINT_NEUTRAL_BEYOND_DOMINANCE_TWO_BASE_PARAMETER_BOX_REFEREE_AUDIT.md
audit/verify_common_metric_endpoint_neutral_beyond_dominance_two_base_parameter_box_referee.py
tmp/research/common_metric_endpoint_neutral_beyond_dominance_three_base_parameter_box.md
tmp/research/verify_common_metric_endpoint_neutral_beyond_dominance_three_base_parameter_box.py
audit/COMMON_METRIC_ENDPOINT_NEUTRAL_BEYOND_DOMINANCE_THREE_BASE_PARAMETER_BOX_REFEREE_AUDIT.md
audit/verify_common_metric_endpoint_neutral_beyond_dominance_three_base_parameter_box_referee.py
tmp/research/common_metric_endpoint_neutral_beyond_dominance_near_psd_scale_extension.md
tmp/research/verify_common_metric_endpoint_neutral_beyond_dominance_near_psd_scale_extension.py
audit/COMMON_METRIC_ENDPOINT_NEUTRAL_BEYOND_DOMINANCE_NEAR_PSD_SCALE_EXTENSION_REFEREE_AUDIT.md
audit/verify_common_metric_endpoint_neutral_beyond_dominance_near_psd_scale_extension_referee.py
```

The one- and two-base files are subsumed slices.  The strongest result varies
the two normalized ratios and, independently, their common scale
`s in [6/7,117/80]`.  Its upper endpoint lies about `3.42e-5` below the
first exact PSD-degeneration scale for this fixed shape rectangle.  Its two
charts contain 378,675 and 236,925 strictly
positive exact controls, independently reconstructed by sparse nodal
interpolation.  This stable three-base-parameter box is beyond the dominance
method, but it is not a proof of the general projective sextic.

A second independently audited five-parameter box is separated from that
near-PSD rectangle in both normalized shape coordinates.  With
`(a,c)=(3/5,4/5)`, it varies
`B=b/e in [-201/200,-199/200]`,
`G=gamma/e in [99/200,101/200]`, and
`e in [8/25,129/400]`.  It also has `D>0`, `x_0<0`, and `H<0` throughout,
yet every projective-circle direction and every dangerous weight has a
strictly positive raw gate.  Independent nodal Bernstein reconstruction
checks 378,675 upper-chart and 236,925 lower-chart controls.  Thus the known
positive region is not confined to one near-degenerate shape island, but no
bridge or universal sextic proof is claimed.  Read:

```text
tmp/research/common_metric_endpoint_neutral_disjoint_hnegative_shape_box.md
tmp/research/verify_common_metric_endpoint_neutral_disjoint_hnegative_shape_box.py
audit/COMMON_METRIC_ENDPOINT_NEUTRAL_DISJOINT_HNEGATIVE_SHAPE_BOX_REFEREE_AUDIT.md
audit/verify_common_metric_endpoint_neutral_disjoint_hnegative_shape_box_referee.py
```

An exact positive-definite witness shows that two positive marginal
one-phase increments can have a negative combined increment while the actual
gate remains positive.  This rejects intersection of marginal cones, not the
gate itself.

## 7. Precise next theorem and later quantifiers

The immediate task is now:

```text
Expand or connect the audited five-parameter center box and full-phase
negative-meridian collar toward the full compact ball and
prove the audited compact-unit-ball positive-scale quartic that losslessly
represents the complete dangerous transverse rank-two compression cone, using
a ray-dependent copositivity allocation or an invariant elimination, or give
an exact legal negative.  Then extend beyond the present kernel path.
In parallel prove the
endpoint-neutral projective sextic, cover the remaining non-neutral
`Q_23!=0` endpoint strata, close the remaining scale-cubic
derivative/discriminant signs and
complementary feasible-center two-phase gate, or give an exact legal P,Q,W
with a strict negative original gate.
```

After that, the required order is:

1. unbalanced rank-two densities in `M_3`;
2. cases where neither positive side has rank one;
3. arbitrary dimension in the common-metric theorem;
4. the arbitrary-finite-node and operator bridge;
5. the exact fixed crossing-lens constant for all operators and all rational
   functions.

A finite-node theorem, an all-operator theorem for a special Blaschke family,
or a special-operator theorem for all functions does not close the original
double quantifier.

## 8. Manuscript and transfer policy

Do not rewrite `lens_constants.tex` as a solution paper until every
quantifier in Section 7 is closed and independently audited.  The PDF must
never contain checksum values, an AI watermark, or an AI declaration.  The
confirmed author metadata is:

```text
Zijian Zeng
Institute of Computer Science and Digital Innovation, UCSI University
Kuala Lumpur 56000, Malaysia
1002266693@ucsiuniversity.edu.my
```

All new documentation and scripts must use paths relative to the checkpoint
root.  Rebuild Python and Lean environments from manifests; never transfer
`.venv`, `.lake`, compiled caches, or a Git object store.
