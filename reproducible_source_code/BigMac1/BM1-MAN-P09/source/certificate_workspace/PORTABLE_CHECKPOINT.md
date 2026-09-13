# Portable checkpoint: fixed crossing-lens spectral constant

Frozen at 2026-08-18, Asia/Shanghai.  This document is the authoritative
entry point when the project is copied to a different computer, path, Codex
account, or operating system.  Every path below is relative to the directory
containing this file; no old absolute path is required.

**v22 continuation notice.** Read `V11_HANDOFF.md` through
`V16_HANDOFF.md`, then `V18_HANDOFF.md`, `V19_HANDOFF.md`, and
`V20_HANDOFF.md`, `V21_HANDOFF.md`, and `V22_HANDOFF.md` immediately after
this file.  The latest handoff records the exact closure of the complete
real-symmetric balanced rank-one-side scalar gate in dimension three, its
independently audited proof and Lean algebra core, the exact endpoint
Minkowski/Gram equivalence, and the exact failure of real-part monotonicity
in the complex chart.  Several genuine one- and simultaneous-phase
subfamilies and an opposite-phase boundary family are proved.  The remaining
Schur-boundary branch is now a strictly convex one-variable scale cubic with
an exact finite sign gate.  Its `g<=0` endpoint is proved, while the `g>0`
endpoint has a lossless compact rank-two Gram gate whose sign remains open;
its complete genuinely complex diagonal-atom face is proved for every legal
parameter by a strict-derivative/concavity split, while a general second Gram
atom remains open.  The complementary feasible-center branch also remains open.  A separate spectral reduction proves
the full equal-positive-eigenvalue rank-two slice for arbitrary complex
phases, sharply.  The full unequal-eigenvalue PSD cone is also proved for
every planar kernel `n_2=0`, and every other fixed spectral ray has an exact
one-parameter copositivity test.  CE-059 proves that its natural fixed
allocation `s=-2` is not universal, even on a legal strictly dangerous
rank-two transverse ray whose actual gate is strictly positive at every
scale; the allocation must remain ray-dependent or be eliminated by a new
invariant argument.  A sharp-to-`e_2` genuinely nonplanar path is
proved for every diagonal compression and every eigenvalue ratio.  Full
off-diagonal mixing on that path is losslessly an explicit quartic on one
danger interval; its sign remains open, and exact witnesses exclude global
concavity and nonnegative-mixing shortcuts.  The complete two-sided complex
phase line `X=3Y` is proved at every scale by an exact square completion and
Bernstein-positive reserves.  A genuine two-real-dimensional local box of
complex spectral frames is proved for every scale, every positive eigenvalue
ratio, and `sqrt(2)/8<=eta<=sqrt(2)/4`: direct and reciprocal five-dimensional
Bernstein certificates plus an adaptive exact seam tree prove the gate on
`(-infinity,-2] union [-2/3,infinity)`, including projective infinity, and an
exact danger calculation proves that the complete `|r|<=2/9` subbox is
strictly dangerous.  The former negative latitude gap contains an exact
strict-danger equality, so its target is nonnegativity plus equality
classification.  The complete meridian face `r=-1` and an explicit uniform
neighborhood were first audited separately.  Exact collars then reduced the
last gap to `[-8/7,-7/8]`; a centered decomposition `J=J_0+kA`, two lossless
dominant projective charts, and 14 off-local leaves now give an independently
audited 96,725-control certificate on that interval.  Therefore the fixed
transverse spectral family is nonnegative on its entire projective latitude
`r in RP^1`, with equality exactly at `r=-1,k=0,t=1`.  The rest of the
compression disk, arbitrary Bloch frames, and the full Bloch sphere remain
open.  The complete dangerous transverse compression cone nevertheless has
an independently audited lossless coordinate: for every nonzero transverse
displacement it is exactly one compact unit-ball shape and one positive
scale, and the raw gate is an explicit rational quartic in that scale.  The
planar zero-displacement face is already proved separately.  The sign of
this compact-ball quartic is now the precise missing transverse theorem.
Its complete center axis `x=y=0` is independently audited strictly positive
for every displacement, determinant parameter, and positive scale, including
rank-one and rank-two data.  In addition, the explicit five-parameter box
`|x|,|y|<=1/8`, `z^2<=31/32` is independently audited strictly positive by
4,146 exact Bernstein controls.  This box is a two-sided neighborhood of the
truncated axis segment, not a superset of the full center axis; the compact
ball outside the box and the separately proved axis caps remains open.
At the distinct fixed kernel `eta=1/2`, a second independently audited
certificate covers the complete phase circle, every scale and spectral ratio,
and `r in [-65/64,-63/64]`.  Its 49,840 positive controls prove nonnegativity
with equality exactly at `r=-1,k=0,t=1`.  This is another interior collar,
not a bridge to the full compact ball.
The positive-`g` endpoint is
also proved on an active-orthogonal two-atom face.  The entire Hermitian PSD
coordinate slice `Q_23=0` is proved at arbitrary rank by reduction to the
reducing-plane theorem.  A strict non-neutral `Q_23>0` endpoint-preserving
three-parameter phase cube is also proved by 245 positive Bernstein controls.
General `Q_23!=0` nonorthogonal Gram columns and
arbitrary nonplanar kernels remain open.  On
the strict `Q_23>0` endpoint-neutral chart, the relative Gram angle is
losslessly one circle and the gate is one real sextic; its sign is open.
For every base `b in [-1/4,-1/16]` in one explicit normalized family, the
entire projective circle and all dangerous second-atom weights are proved
positive by an exact square-dominance identity.  CE-056 shows that this
dominance reserve is not automatic.  A second audited three-dimensional base
box varies the two normalized ratios corresponding to
`b in [-22/125,-87/500]`, `gamma in [8/125,33/500]` at the middle scale and,
independently, a common scale `s in [6/7,117/80]`, ending about `3.42e-5`
below the first PSD degeneration for that shape rectangle.  It has `H<0` throughout but
is nevertheless positive on every projective-circle direction and dangerous
weight by exact five-variable Bernstein certificates.  A second audited
five-parameter `H<0` box with `(a,c)=(3/5,4/5)` varies
`b/e in [-201/200,-199/200]`, `gamma/e in [99/200,101/200]`, and
`e in [8/25,129/400]`; it is disjoint from the near-PSD rectangle in both
normalized shape coordinates and is likewise positive on the complete
projective circle and danger interval.  The general sextic
remains open.
CE-048 through CE-053 remove the naive absorption, fixed-projection,
transverse-concavity, mixing-monotonicity, angular-chord, and weight-monotonicity shortcuts.  The full complex Hermitian gate
remains open.  The unbalanced
and higher-rank three-dimensional layers, arbitrary dimension, arbitrary
node number, and the full fixed-lens problem also remain open.

## 1. Truthful status at the breakpoint

The original problem has **not** been solved.  No formula for the optimal
constant of every fixed crossing lens has been proved.  The present
`lens_constants.tex` is a rigorous partial-results manuscript, not an Annals
or JAMS solution of the open problem.  Numerical SDP feasibility is evidence,
never a theorem.

### v16 delta: a complex-zero quadratic singular-boundary theorem

For `Phi_theta(c)=exp(i theta)c^2` with
`1/sqrt(2)<sin(theta)<=1`, take the three admissible roots of
`(1-i sqrt(2)c)Phi_theta(c)-c=0`.  On this full-support singular ratio-Pick
boundary, the sharp three-node target is now positive definite for every

```text
B_a(w)=w(w-a)/(1-conjugate(a)w),       |a|<1.
```

The proof is exact: root elimination gives
`det(T)=rho*N/[4H(sqrt(2)q-1)]`, with `H=8|Delta|^2>0`; a cubic Bernstein
certificate and two local corner estimates prove `N>0`.  The exact verifier
and two independent audits pass.  Read `V16_HANDOFF.md` and
`tmp/research/rank13_phi_theta_complex_a_theorem.md` before working on the
degree-two rank-one-side endpoint.

The scope is strict.  A general degree-two inner `Phi`, a target with two
nonzero zeros, the unrestricted rank-`(2,2)` face, arbitrary node number,
and the general fixed-lens constant remain open.

### v15 delta: a complete symmetric three-node cone theorem

For the right-angle curve, take `rho=(-a,0,a)`, `0<a<1`, the corresponding
physical nodes `z=(-2a/(1+a^2),0,2a/(1+a^2))`, and multiplier `h(z)=z`.
For every Hermitian admissible kernel `L`, the sharp target

```text
(2-z*z).*L >= 0
```

is now proved. This covers the entire three-node cone on this one-parameter
family, not just a numerical sample or a rank-`(2,2)` face. The proof uses
the exact extreme-ray rank list, scalar Pick closure of rank-one faces, and
an exact phase/Bernstein elimination of the rank-`(2,2)` face. Read
`V15_HANDOFF.md` and `RIGHT_ANGLE_THREE_NODE_SYMMETRIC_THEOREM.md` before
working on three nodes.

The scope is strict. General rank-`(1,3)`/`(3,1)` faces still leave a
degree-two Blaschke `3 x 3` determinant, and nonsymmetric rank-`(2,2)` faces
still leave the sign of the exact `F,S` criterion. The arbitrary-node
right-angle constant and the general fixed-lens constant remain open.

There is also an exact nonsymmetric patch for the identity multiplier:
`rho=(-a,0,b)` with `1/6<=a,b<=5/6`. A nested rational Bernstein
certificate proves every rank-`(2,2)` target determinant there; the existing
extreme-ray and rank-one arguments then cover the full three-node cone on
that parameter rectangle. This is genuinely two-dimensional in the nodes,
but it still concerns only `h=z` and does not imply the arbitrary-Schur
right-angle theorem.

The strongest current structural lead is the right-angle lens.  For sector
nodes `beta_i`, disk-Schur values `lambda_i`, and their Pick-derived matrix
`Q`, the exact identities are recorded in `RIGHT_ANGLE_KERNEL_NOTE.md`.  With

```text
K+ = 1/(2d+) + 4 d- .* Q + d- .* X,
K- = 1/(2d-) + 4 d+ .* Q - d+ .* X,
```

the unknown Hermitian correction `X` cancels exactly and the sharp target
would follow if `K+` and `K-` can always be made positive semidefinite.

The finite SDP now has an exact dual. With

```text
H_ij = (2-conjugate(lambda_i)lambda_j)/d+_ij,
S = conjugate(d-)/conjugate(d+),
```

the missing completion is equivalent to

```text
<H,Y> >= 0 whenever Y >= 0 and S.*Y >= 0.
```

`RIGHT_ANGLE_DUAL_NOTE.md` proves this for every Schur datum on at most two
interior nodes. The proof uses a sharp radial pseudohyperbolic scaling lemma
and an exact right-angle two-point geometry inequality. Thus the two-node
case is no longer a conjecture; the first unresolved case has at least three
nodes.

Small SDPs found feasible corrections in all 80 finite-Blaschke trials
reported in `tmp/research/right_angle_agler_completion_*.json`, through ten
nodes and degree twelve.  This is discovery evidence only.  The choice `X=0`
fails, arbitrary positive `Q` fails, and an arbitrary subkernel condition
`0 <= P <= K` is also too weak: at this final breakpoint, random interval
subkernels were feasible for the tested `n=2,3` cases but produced negative
optimal margins for some `n=4,6,8` cases.  Thus a new proof must preserve the
full scalar-Schur/rank-one relation

```text
K - P = (h h*) .* K,
```

not replace it by order inequalities alone. A corrected primal--dual audit
also agrees to about `1.7e-7` through six nodes; this is a regression check,
not a proof.

Two tempting strengthenings have been rejected:

- membership of the right-angle Cayley transform in the operator-radius
  class `C_sqrt(2)` fails by an exact `2 x 2` sectorial counterexample;
- numerical dual optimizers for `n=3,4,6,8` need not admit a decomposition
  into positive one- and two-index supports.

The best present reformulation is an admissible-kernel/multiplier problem on
the bidisk curve `C-D+i sqrt(2) CD=0`. It is equivalent to the unresolved
dimension-free completion, so it is a target for a new factorization rather
than an already available theorem.

The newest exact nonlinear datum on that curve is

```text
F(c,d)=(c+d)^2/2 + (c-d+i sqrt(2)cd)*(51i/100+41(d-c)/400),
||F|| = 276889/127200-6103sqrt(2)/10600 < sqrt(2),
```

with `F=w^2` on the curve.  `RIGHT_ANGLE_SQUARE_EXTENSION.md` gives the
exact torus maximization.  This improves the manuscript's arbitrary-
dimension central-square bound but is not an arbitrary-Schur extension.

### Latest delta after the earlier v2 checkpoint

The v3 checkpoint also preserves a second right-angle route developed in
`tmp/research/pi4_state_reduction.md`. Put `B=A^2`. The existence of a common
similarity metric

```text
I <= G <= 2I,              B^*G+GB >= 0
```

is exactly equivalent, by finite-dimensional separation, to

```text
||BW+WB^*||_1 + 6 Re tr(BW) >= 0             for every W >= 0.
```

The rank-one case is proved; the mixed-state case is open. Inversion
preserves the right-angle sector by congruence, so both `B` and `B^{-1}` have
one-factor sum-of-squares certificates. A finite-frequency degree-one
quadratic module generated only by those certificates fails numerically
(CE-011); this rejects that ansatz, not the metric inequality.

A small rank-`(1,2,2)` Gram selector was specialized near the difficult
negative parameter axis. The gauge `s=u=B=0`, `A=-a^2 r` leaves four
degree-six equations in `(r,t,C,E)`. Important correction: this gauge kills
only `Im G_02`; it does not make `G_02=0`. A global lexicographic Groebner
basis over `Q(a)` was extremely large, so the efficient next step is a local
continuation/interval-Newton certificate in the blow-up chart, using the
positive middle `2 x 2` pivot and its vanishing Schur complement. Do not
restart the global elimination before testing that small chart numerically.

The v3 Lean audit adds `formalization/TwoNodeGeometry.lean`, which proves the
denominator-free affine majorant and sharp scalar inequality at the core of
the two-node theorem. The full arbitrary-node completion and the full
two-node paper argument are still not formalized.

### v4 delta: scaled low-rank continuation

After v3, the negative-axis selector was rewritten in the correct variables
`h=tau^2` and `R`.  The exact factor is

```text
|1+rho*zeta| = h^2 sqrt(R^4+64*rho/(1+4h^4)^2),
rho=1-h^2 R^2.
```

Three continuation programs now show why the former four-variable gauge was
not robust: the `s=u=0` chart folds, while a full eight-variable atlas can
cross representative failures by solving four Schur equations in four
locally selected active coordinates.  These runs are numerical discovery,
not interval proofs.  The Schur residual scales as `h^3=tau^6`, so raw
coordinates are inherently singular near `tau=0`.

Section 52 of `tmp/research/pi4_state_reduction.md` records the twice-scaled
limiting four-equation system, an exact obstruction to a particular
`z=R^2`-analytic branch, the rank-one corner approached by the positive
branch, and a simpler outer radial subbranch whose discriminant is explicit.
At the v4 breakpoint the corner still needed a second `R`-blow-up/facial
chart.  That task has now been completed in the v5 delta below.

### Final v5 delta: exact limiting-rectangle theorem

Sections 53--55 of `tmp/research/pi4_state_reduction.md` now give a complete
and exactly replayable theorem for the singular face `h=0`.  The outer
subbranch has an explicit quadratic solution for

```text
z=R^2 >= 8/sqrt(3),       P=sqrt(z^2+64),
```

with the corrected discriminant factor `-32768 z^2 Q`.  The identity

```text
[3zP(z^2+12)]^2-[3z^4+124z^2+256]^2
  =16(z^2-8)^2(3z^2-64)
```

is audited symbolically by `derive_blowup_limit_branch.py --outer-branch`.

At the rank-one corner `z=0`, a second radial blow-up and two analytic
implicit-function arguments construct the inner rank-two branch.  Its
leading coefficients, nonzero Jacobian minor, divided compatibility
equation, and positive eigenvalue slope are audited by the same script with
`--inner-branch`.

Most importantly, two exact rational parametric Krawczyk atlases cover the
whole limiting interval `0 <= z <= 25/4`:

- 15 desingularized boxes cover `0 <= z <= 1/2`;
- 373 direct-coordinate boxes cover `1/2 <= z <= 25/4`;
- an exact interval map proves that the two atlases select the same root at
  `z=1/2`;
- exact pivot bounds prove rank one at `z=0` and rank two for `z>0`.

The accepted certificate data are the two JSON files named in Section 55.
Floating-point SciPy is used only to propose boxes when regenerating them;
certificate replay uses exact `Fraction` interval arithmetic for every
acceptance decision.

This is a real new partial theorem, but its scope is precise: it concerns
only the limiting system at `h=0`.  It does **not** yet prove a Gram completion
for any positive `h=tau^2`, does not fill the original missing phase
rectangle, and does not prove the right-angle or general fixed-lens optimal
constant.  The next bounded task is to lift this branch to

```text
0 <= h <= 1/9,       0 <= z <= 25/4,
```

first by testing and deriving a finite-`h` scaled rank-two ansatz, then by a
two-parameter interval atlas only if the analytic chart remains regular.

### Final v6 delta: exact finite-`h` blocks and the second boundary face

Section 56 of `tmp/research/pi4_state_reduction.md` now derives the full
finite-`h` scaled rank-`(1,2,2)` Gram blocks exactly in the eight selector
coordinates

```text
(a,sigma,b,v,A2,B2,k,e).
```

The identity is not inferred from floating-point continuation:
`tmp/research/derive_finite_h_rank2_blocks.py` expands both the scaled block
formula and the original Section 46 Gram matrix symbolically and proves that
every entry agrees.  The positive-rank-two equations are

```text
det(H) K - Z* adj(H) Z = 0,
```

subject to positivity of the middle block `H`.

The entire second parameter face is also solved exactly.  At `z=0`, hence
`rho=1` and `|c|=1`, one has

```text
N_c = c^(-1) D_c,                 N_c* N_c = D_c* D_c.
```

With `L=1+4h^4`, `g=1-4h^4`,

```text
p=8h^2/L,  r=s=t=A=B=C=E=0,  u=-4g/L,
```

the edge Gram is exactly zero and the ordinary vector is a unit-phase
multiple of the `D_c` vector.  Therefore the Section 46 family has an exact
one-square certificate on

```text
0 <= h <= 1/9,                    z=0.
```

The new floating continuation files show two further facts, with numerical
status only:

- the restricted four-variable gauge really folds and must not be treated as
  a global chart;
- the full eight-variable selector crosses representative folds, covers the
  tested vertical segment at `z=0.39071875`, and covers most sampled vertical
  lines on the finite rectangle after changing active coordinates.

The corner and a thin positive-`z` collar still require a facial or
`R=sqrt(z)` blow-up.  No exact two-parameter Krawczyk atlas for positive `h`
exists at this checkpoint.  Even if that atlas is completed, it proves only
the centered degree-two Section 46 family, not arbitrary Schur functions.

The three-way workflow audit is also frozen.  Its principal conclusions are:

1. do not restart the giant sampled-SDP route;
2. transfer Jin's exact nuisance-annihilation pattern, not the media story or
   an alleged numerical sampling workflow that is absent from the repository;
3. preserve the two separate one-spectral-set constraints before applying a
   numerical-range theorem, because that is where angle information lives;
4. use Lean for a stable analytic lemma, not for numerical continuation or a
   moving manuscript;
5. the reference Lean project verifies the earlier constant-two core, while
   its manuscript map does not bind the current 1,979-line v4 extension.

### v13 delta: coherent factor and exact quadratic quotient representative

`RIGHT_ANGLE_COHERENT_FACTOR_NOTE.md` closes the algebraic part of the
two-atom variance problem.  A single self-adjoint `H` satisfying

```text
E=B*H+HB+3(B+B*) >= 0,
R0=F0-(B-H)*(B-H)=I+E-H^2 >= 0
```

produces affine factors common to every resolvent frequency.  Their common
expansive defect proves arbitrary-atom resolvent convexity, and the two-atom
target has the exact sum of squares

```text
T=(D-HN)*(D-HN)+N*R0 N+vE.
```

All identities are replayed in a free-star algebra.  The essential negative
conclusion is equally exact: after Herglotz mass normalization, requiring
this LMI on every positive scale is equivalent to the unresolved common-
metric conjecture.  It is therefore a useful structural reduction, not a
complete proof.  `RIGHT_ANGLE_COHERENT_DUAL_NOTE.md` records its exact
finite-dimensional separator and a numerically rejected shortcut.

The affine-curve route has meanwhile produced the explicit quadratic
representative displayed above, with exact norm
`276889/127200-6103sqrt(2)/10600`.  Its correction is constant plus antisymmetric
linear state.  The next bounded target is to make that state part of a
two-channel Schur/Redheffer recursion with a uniform norm bound; estimates
on individual Taylor powers do not suffice.

### v14 delta: exact route gates and three-node rank reduction

`RIGHT_ANGLE_THREE_NODE_RANK_REDUCTION.md` now proves that every extreme ray
of the `n`-node admissible-kernel cone satisfies
`rank(P)^2+rank(Q)^2<=n^2+1`.  For three nodes this rigorously reduces every
genuinely two-channel extreme face to rank `(2,2)`; the determinant
inequality and scalar rank-one/full-rank faces remain open.

The one-factor companion has an explicit unequal rank-one Agler split, but
`RIGHT_ANGLE_SIGNED_RECURSION_NOTE.md` proves that the exact recursion carries
this defect with a negative sign.  A two-node exact dual witness rejects
positive scalar carry-over even for `w^2`.  The surviving constructive route
must retain an evolving matrix/off-diagonal state.

The full common Pick coupling and Mellin nuisance unitary are recorded in
`tmp/research/right_angle_hardy_cauchy_note.md`.  Finite node-identification
cycles are impossible, and the natural analytic continuation of the unitary
has an indefinite Schur defect off the real diameter.  The metric branch has
also been narrowed exactly: `tmp/research/common_metric_branch_audit.md`
rejects every metric commuting with the normalized effect on explicit
rational data, although a noncommuting metric succeeds.

The checkpoint was taken with no research solver intentionally left running.
An anonymous project-local Python calculation with no output artifact was
terminated before packaging; it is not a resumable dependency.

### v8 delta: arbitrary-node tangential-cascade mainline

`CURRENT_BREAKPOINT_DELTA.md` records the work after v6.  The decisive route
is now the arbitrary-node admissible-kernel problem, not the finite-`h`
centered degree-two atlas.  Exact right-angle coordinate identities identify
the affine bidisk curve

```text
C-D+i sqrt(2) C D=0
```

and the missing theorem as a norm-`sqrt(2)` extension or positive-kernel
factorization problem.  The known norm-`sqrt(2)` extension of the coordinate
function does not extend arbitrary Schur compositions and is not a proof.

A proposed trace-moment bridge for the common-metric route was rejected
numerically, including on sector-square data with negative real first
moment.  It must not be reused.  This rejection does not disprove the true
mixed-state inequality.

Every finite right-angle admissible kernel now has an exact
operator-valued tangential-Schur parametrization, recorded in
`RIGHT_ANGLE_TANGENTIAL_MODEL.md`.  With the inner product linear in its first
variable, the correct Gram convention is `<x_i,x_j>=P_ij`; the standard
left-tangential Pick matrix is then `conjugate(Q)`.  The complete
arbitrary-node target is equivalent to constructing a norm-`sqrt(2)`
operator-valued tangential interpolant.  This is an exact reduction, not the
missing proof: the tangential cascade lemma remains open.

The hardened thin-strip verifier has been fully replayed from the current
candidate and exact compatibility solution.  All 9,184 compatibility
equations and all 74,313 exact Bernstein--LDL controls passed, and the
regenerated certificate has the same SHA-256 as the stored certificate.  The
portable verifier includes targeted LDL-indexing and nondivisible-quotient
regressions; `./verify_checkpoint.sh --strip` performs the expensive full
strip replay.  This remains a local partial certificate only.

The user explicitly authorizes Lean and environment installation.  The
policy remains to formalize the smallest stable breakthrough lemma after its
paper proof and adversarial checks, then bind it to the manuscript by hash.
No research solver or Lean process is running at this v8 breakpoint.

## 2. Rigorously checked versus still open

Checked:

- the exact right-angle support-product and square-Cayley/Pick identities;
- the affine correction cancellation, entrywise and at matrix level;
- the finite complex Schur-product bridge from positive completed kernels to
  the desired target;
- the exact finite SDP dual and its objective cancellation;
- the complete at-most-two-node right-angle completion theorem in
  `RIGHT_ANGLE_DUAL_NOTE.md`;
- the exact tangential-Schur parametrization of every finite right-angle
  admissible kernel and the exact reformulation as an open norm-`sqrt(2)`
  tangential cascade problem;
- the complete `h=0`, `0<=R<=5/2` limiting rank-`(1,2,2)` branch theorem,
  including the inner desingularization, exact outer factorization, 388
  rational Krawczyk boxes, pivot positivity, and exact chart stitch;
- the exact full finite-`h` scaled block identities and the complete `z=0`,
  `0<=h<=1/9` one-square boundary certificate in Section 56;
- an exact rational counterexample to the stronger `C_sqrt(2)` operator-radius
  route, reproducible by `tmp/research/right_angle_crho_counterexample.py`;
- the corresponding eight Lean endpoints in `formalization/`, with no `sorry`,
  `admit`, or project-specific axiom; their printed axioms are only
  `propext`, `Classical.choice`, and `Quot.sound`;
- the supplied Crouzeix reference Lean project built all 3,120 jobs under its
  locked toolchain and its `AxiomAudit.lean` passed;
- the older polynomial route produced a genuine exact thin-strip
  certificate, after hardening the verifier against artifact mis-pairing and
  silent monomial truncation.

Not checked/proved:

- existence of the right-angle correction `X` for all Schur data;
- a sharp upper bound for the full right-angle lens problem;
- persistence of the limiting rank-two branch for any positive `h`, and the
  required two-parameter finite-`h` interval atlas;
- a matching new lower extremizer beyond the partial families in the paper;
- a formula or strict angle-dependent bound for general crossing lenses;
- line-by-line Lean coverage of the current 1,979-line Crouzeix manuscript.
  The reference formalization map names an older 1,106-line manuscript hash.

## 3. Decisions that must survive the restart

1. Do not restart the 9,978-variable, 177-million-nonzero sampled SDP.  It
   consumed about 20--21GB, mostly in sparse factorization, and could only
   certify grid points.  `WORKFLOW_AUDIT.md` supersedes Sections 8--9 of the
   older `RESEARCH_HANDOFF.md`.
2. Do not infer whole-domain positivity from the old exact thin strips.  The
   same candidate is strongly negative in the interior.
3. Do not trust an NPZ flag such as `exact_verified=1` without independently
   binding and rebuilding every input.  The retained exact scripts contain
   the fail-closed remediation; any future certificate needs an independent
   full hereditary replay plus SHA-256 bindings.
4. Do not describe the Crouzeix media story as a one-shot, independently
   reproducible 16-hour workflow.  The repository shows an analytic sampling
   idea followed by about 19 days of substantive revisions, and contains no
   numerical discovery transcript.
5. Use Lean only after isolating a mathematically meaningful lemma.  The
   two-atom algebraic variance identity is now stable enough to formalize;
   the missing coherent-variance positivity theorem is not.  Formalizing
   more numerical evidence adds no rigor.
13. Read `CURRENT_BREAKPOINT_DELTA.md` before resuming: it selects the
    arbitrary-node affine-line extension/factorization problem as the main
    route and records a newly rejected trace-moment bridge.
6. Do not retry the `C_sqrt(2)` route or assume the arbitrary-node dual cone
   is generated by two-index supports; both are recorded failures.
7. The negative-axis script name `derive_negative_axis_g02.py` is historical:
   its live gauge sets only `Im G_02=0`. Any argument treating the full entry
   as zero is invalid.
8. The `s=u=0` rank-two selector is only a local chart.  Failure of that chart
   is not a counterexample to a Gram completion; continuation must use the
   full eight-variable selector and a pivot/gauge atlas.
9. The rank-one limiting corner at `(tau,R)=(0,0)` cannot be handled by the
   ordinary middle-pivot implicit function theorem.  The required second
   radial blow-up is now complete in Sections 54--55; do not redo it.  The
   remaining singular perturbation is finite `h`, not inner limiting `z`.
10. The Section 55 JSON atlases are exact certificates for the displayed
    limiting equations only.  Their successful replay must never be cited as
    a finite-`h` or whole-lens positivity certificate.
11. The exact `z=0` selector lies on a different Gram face (`u=O(1)`, `t=0`)
    from the local finite-`h` chart (`u=hv`, `t=4+hb`).  A valid interior
    proof needs an explicit chart overlap or facial blow-up; juxtaposing the
    two boundary theorems is not a rectangle proof.
12. The full eight-variable finite-`h` JSON files are numerical discovery
    artifacts.  Small residuals and successful gauge switches do not replace
    exact interval inclusion and pivot bounds.

## 4. Recommended next research sequence

**V22 priority.**  Read `V22_HANDOFF.md` and the real-symmetric theorem,
complex one-phase theorems, complex real-part obstruction, and referee files
listed there.  The actual balanced rank-one-side scalar gate is closed for
every real-symmetric positive `Q`; do not return to the older strengthened
endpoint pencil as though it were still the missing real theorem.  Prove or
refute the gate for arbitrary complex Hermitian `Q`, retaining the
irreducible phase and the legal Schur-completion constraint.  The exact
failure of `G(Q)>=G(Re Q)` rules out the naive reduction.  On the boundary,
use the audited scale-cubic endpoint/derivative/discriminant criterion rather
than re-expanding the original eight-variable polynomial.  Do not assume the
failed feasible-center absorption inequality or any of the four failed fixed
projection metrics.  After the complex
balanced layer, proceed to unbalanced rank-two densities, neither-side-rank-
one data, arbitrary dimension, and only then the all-node/operator bridge.
Do not restart the large breaker as though more sampling were proof.

**V20 priority (supersedes the older sequences below).**  First enlarge the
uniform two-zero bidisk extension in
`tmp/research/global_two_small_zero_target_family.md`: either characterize
the maximal parameter domain of that explicit rational ansatz or find a new
state whose certified parameter domain is strictly larger.  This is the
smallest exact constructive endpoint and already preserves the all-operator
quantifier for the restricted function family.  In parallel, attack the
sharp singular rank-one-side scalar

```text
theta=y*(A+xx*)^(-1)y <= 1.
```

Read `tmp/research/rank13_root_free_factor_insertion_gate.md` and
`tmp/research/rank13_sharp_theta_geometry_and_collar.md`.  The latter gives
an exact block completion, cyclic volume formula, a pointwise nonuniform
collar, and one audited positive compact family outside that collar.  A
valid universal result must prove the scalar on the whole root-free domain
or give an exact feasible `theta>1` counterexample.  The former canonical-
start two-dimensional cascade endpoint is now closed negatively: no
successor direction or cross column works for its exact three-node witness.
Any new cascade must change the first realization or use at least three
states.  Unrelated finite-node choices do not bridge to arbitrary nodes.
Do not return to the giant sampled SDP route.

The smallest new state-space sequence is now:

1. read `TWO_ATOM_VARIANCE_NOTE.md` and replay the exact expansion;
2. retain the square-root/Kolmogorov coefficients of the one-frequency
   three-square proof rather than replacing them by an arbitrary Gram;
3. seek a Schur complement whose residual is exactly
   `p(1-p)(t-s)^2 I`;
4. require the resulting state to survive insertion of a third atom;
5. use the saved generic rank-`(1,2,2)` SDP solutions only to guess a gauge,
   never as proof.

The parallel dimension-free sequence remains:

1. Start from the exact dual already derived in
   `RIGHT_ANGLE_DUAL_NOTE.md`; do not rederive or numerically rediscover the
   two-node theorem.
2. Normalize a dual witness as an admissible kernel `L`, so that
   `conjugate(d+).*L` and `conjugate(d-).*L` are positive. Seek a
   dimension-free factorization proving
   `(2-lambda^*lambda).*L >= 0` for the full scalar-Schur relation.
3. In parallel, seek a norm-`sqrt(2)` bounded extension from the bidisk curve
   `C-D+i sqrt(2)CD=0`. Attack each proposed section/extension formula with
   three-node Agler--Pick dual certificates before general proof work.
4. Maintain a separate lower-bound program: at least two spectral points,
   higher nilpotent chains, or periodic weighted shifts with exact
   rational/Blaschke witnesses.
5. Only after an existence proof is complete, formalize that theorem in Lean,
   rerun the axiom audit, update the manuscript, and reassess the venue.

For the current metric branch, the immediate bounded theorem is instead:

1. expand the independently audited full-projective-latitude theorem for the
   fixed transverse family to arbitrary Bloch frames and the full transverse
   compression cone;
2. prove the remaining transverse off-diagonal danger-interval quartic or
   exactify a strict legal negative; the fixed-ray copositivity allocation
   may depend on the ray, since CE-059 rejects the universal choice `s=-2`;
3. prove the strict-chart endpoint-neutral projective sextic and the
   remaining non-neutral `Q_23!=0` endpoint strata; the full `Q_23=0` PSD
   coordinate slice is already closed;
4. then pass from the balanced rank-one-side chart to unbalanced rank-two
   densities, cases where neither positive side has rank one, and arbitrary
   dimension;
5. keep every low-dimensional theorem separate from the arbitrary-node
   right-angle affine Agler completion, which remains necessary for the full
   fixed-lens problem.

## 5. Reading order for a fresh Codex

Read these files completely before doing new work:

```text
AGENTS.md
PORTABLE_CHECKPOINT.md
CHECKPOINT_STATE.json
V11_HANDOFF.md
V12_HANDOFF.md
V13_HANDOFF.md
V14_HANDOFF.md
V15_HANDOFF.md
V16_HANDOFF.md
V18_HANDOFF.md
V19_HANDOFF.md
V20_HANDOFF.md
V21_HANDOFF.md
V22_HANDOFF.md
tmp/research/common_metric_2x2_commutator_theorem.md
audit/COMMON_METRIC_2X2_COMMUTATOR_REFEREE_AUDIT.md
tmp/research/common_metric_singular_saddle_reduction.md
audit/COMMON_METRIC_SINGULAR_SADDLE_REDUCTION_REFEREE_AUDIT.md
tmp/research/common_metric_universal_arrowhead_gain.md
audit/COMMON_METRIC_UNIVERSAL_ARROWHEAD_GAIN_REFEREE_AUDIT.md
tmp/research/common_metric_n3_rank2_compression_leakage_gate.md
audit/COMMON_METRIC_N3_RANK2_COMPRESSION_LEAKAGE_REFEREE_AUDIT.md
tmp/research/common_metric_tilted_rankone_real_interior_theorem.md
audit/COMMON_METRIC_TILTED_RANKONE_REAL_INTERIOR_THEOREM_REFEREE_AUDIT.md
tmp/research/common_metric_tilted_rankone_endpoint_pencil.md
tmp/research/common_metric_tilted_rankone_endpoint_c2_positivity.md
audit/COMMON_METRIC_TILTED_RANKONE_ENDPOINT_PENCIL_REFEREE_AUDIT.md
tmp/research/common_metric_tilted_rankone_endpoint_remaining_scratch.md
audit/COMMON_METRIC_TILTED_RANKONE_ENDPOINT_REMAINING_SCRATCH_REFEREE_AUDIT.md
tmp/research/common_metric_tilted_rankone_real_symmetric_full_gate.md
audit/COMMON_METRIC_TILTED_RANKONE_REAL_SYMMETRIC_FULL_GATE_REFEREE_AUDIT.md
formal/RightAngleTiltedRankOneRealGateAlgebra.lean
tmp/research/common_metric_tilted_rankone_real_gate_lean_scope.md
tmp/research/common_metric_endpoint_minkowski_equivalence.md
audit/COMMON_METRIC_ENDPOINT_MINKOWSKI_EQUIVALENCE_REFEREE_AUDIT.md
tmp/research/common_metric_tilted_rankone_complex_phase_realpart_no_go.md
audit/COMMON_METRIC_TILTED_RANKONE_COMPLEX_PHASE_REALPART_NO_GO_REFEREE_AUDIT.md
tmp/research/common_metric_tilted_rankone_complex_phase_half_slice_theorem.md
tmp/research/audit/COMMON_METRIC_TILTED_RANKONE_COMPLEX_PHASE_HALF_SLICE_REFEREE_AUDIT.md
tmp/research/common_metric_tilted_rankone_complex_onephase_cones.md
tmp/research/audit/COMMON_METRIC_TILTED_RANKONE_COMPLEX_ONEPHASE_CONES_REFEREE_AUDIT.md
tmp/research/common_metric_tilted_rankone_complex_simultaneous_phase_cone.md
tmp/research/audit/COMMON_METRIC_TILTED_RANKONE_COMPLEX_SIMULTANEOUS_PHASE_CONE_REFEREE_AUDIT.md
tmp/research/common_metric_tilted_rankone_complex_full_phase_reduction.md
audit/COMMON_METRIC_TILTED_RANKONE_COMPLEX_FULL_PHASE_REDUCTION_REFEREE_AUDIT.md
tmp/research/common_metric_tilted_rankone_complex_schur_boundary_polynomial.md
tmp/research/audit/COMMON_METRIC_TILTED_RANKONE_COMPLEX_SCHUR_BOUNDARY_POLYNOMIAL_REFEREE_AUDIT.md
tmp/research/common_metric_tilted_rankone_complex_boundary_scale_cubic.md
audit/COMMON_METRIC_TILTED_RANKONE_COMPLEX_BOUNDARY_SCALE_CUBIC_REFEREE_AUDIT.md
tmp/research/common_metric_tilted_rankone_complex_endpoint_shape_partial.md
audit/COMMON_METRIC_TILTED_RANKONE_COMPLEX_ENDPOINT_SHAPE_PARTIAL_REFEREE_AUDIT.md
tmp/research/common_metric_tilted_rankone_complex_endpoint_diagonal_atom_face.md
audit/COMMON_METRIC_TILTED_RANKONE_COMPLEX_ENDPOINT_DIAGONAL_ATOM_FACE_REFEREE_AUDIT.md
tmp/research/common_metric_tilted_rankone_complex_endpoint_diagonal_atom_face_complete.md
audit/COMMON_METRIC_TILTED_RANKONE_COMPLEX_ENDPOINT_DIAGONAL_ATOM_FACE_COMPLETE_REFEREE_AUDIT.md
tmp/research/common_metric_tilted_rankone_ranktwo_spectral_quartic.md
audit/COMMON_METRIC_TILTED_RANKONE_RANKTWO_SPECTRAL_QUARTIC_REFEREE_AUDIT.md
tmp/research/common_metric_ranktwo_spectral_ray_one_parameter_copositivity.md
audit/COMMON_METRIC_RANKTWO_SPECTRAL_RAY_ONE_PARAMETER_COPOSITIVITY_REFEREE_AUDIT.md
tmp/research/common_metric_transverse_fixed_minus_two_allocation_no_go.md
audit/COMMON_METRIC_TRANSVERSE_FIXED_MINUS_TWO_ALLOCATION_NO_GO_REFEREE_AUDIT.md
tmp/research/common_metric_ranktwo_sharp_kernel_full_cone.md
audit/COMMON_METRIC_RANKTWO_SHARP_KERNEL_FULL_CONE_REFEREE_AUDIT.md
tmp/research/common_metric_ranktwo_planar_kernel_full_cone.md
audit/COMMON_METRIC_RANKTWO_PLANAR_KERNEL_FULL_CONE_REFEREE_AUDIT.md
tmp/research/common_metric_ranktwo_sharp_kernel_transverse_diagonal_cone.md
audit/COMMON_METRIC_RANKTWO_SHARP_KERNEL_TRANSVERSE_DIAGONAL_CONE_REFEREE_AUDIT.md
tmp/research/common_metric_ranktwo_sharp_kernel_transverse_offdiagonal_quartic.md
audit/COMMON_METRIC_RANKTWO_SHARP_KERNEL_TRANSVERSE_OFFDIAGONAL_QUARTIC_REFEREE_AUDIT.md
tmp/research/common_metric_ranktwo_transverse_full_cone_compact_ball_reduction.md
audit/COMMON_METRIC_RANKTWO_TRANSVERSE_FULL_CONE_COMPACT_BALL_REDUCTION_REFEREE_AUDIT.md
tmp/research/common_metric_ranktwo_transverse_compact_ball_center_axis_theorem.md
audit/COMMON_METRIC_RANKTWO_TRANSVERSE_COMPACT_BALL_CENTER_AXIS_THEOREM_REFEREE_AUDIT.md
tmp/research/common_metric_ranktwo_transverse_compact_ball_center_box_theorem.md
audit/COMMON_METRIC_RANKTWO_TRANSVERSE_COMPACT_BALL_CENTER_BOX_THEOREM_REFEREE_AUDIT.md
tmp/research/common_metric_ranktwo_sharp_kernel_transverse_full_phase_negative_meridian_collar.md
audit/COMMON_METRIC_RANKTWO_SHARP_KERNEL_TRANSVERSE_FULL_PHASE_NEGATIVE_MERIDIAN_COLLAR_REFEREE_AUDIT.md
tmp/research/common_metric_ranktwo_sharp_kernel_transverse_phase_ray_theorem.md
audit/COMMON_METRIC_RANKTWO_SHARP_KERNEL_TRANSVERSE_PHASE_RAY_THEOREM_REFEREE_AUDIT.md
tmp/research/common_metric_ranktwo_sharp_kernel_transverse_phase_line_completion.md
audit/COMMON_METRIC_RANKTWO_SHARP_KERNEL_TRANSVERSE_PHASE_LINE_COMPLETION_REFEREE_AUDIT.md
tmp/research/common_metric_ranktwo_sharp_kernel_transverse_spectral_frame_open_box.md
audit/COMMON_METRIC_RANKTWO_SHARP_KERNEL_TRANSVERSE_SPECTRAL_FRAME_OPEN_BOX_REFEREE_AUDIT.md
tmp/research/common_metric_ranktwo_sharp_kernel_transverse_spectral_frame_two_parameter_box.md
audit/COMMON_METRIC_RANKTWO_SHARP_KERNEL_TRANSVERSE_SPECTRAL_FRAME_TWO_PARAMETER_BOX_REFEREE_AUDIT.md
tmp/research/common_metric_ranktwo_sharp_kernel_transverse_spectral_frame_two_parameter_box_enlargement.md
tmp/research/audit/COMMON_METRIC_RANKTWO_SHARP_KERNEL_TRANSVERSE_SPECTRAL_FRAME_TWO_PARAMETER_BOX_ENLARGEMENT_REFEREE_AUDIT.md
tmp/research/common_metric_ranktwo_sharp_kernel_transverse_spectral_frame_local_bernstein_enlargement.md
tmp/research/audit/COMMON_METRIC_RANKTWO_SHARP_KERNEL_TRANSVERSE_SPECTRAL_FRAME_LOCAL_BERNSTEIN_ENLARGEMENT_REFEREE_AUDIT.md
tmp/research/common_metric_ranktwo_sharp_kernel_transverse_spectral_frame_direct_r_bernstein.md
audit/COMMON_METRIC_RANKTWO_SHARP_KERNEL_TRANSVERSE_SPECTRAL_FRAME_DIRECT_R_BERNSTEIN_REFEREE_AUDIT.md
tmp/research/common_metric_ranktwo_sharp_kernel_transverse_spectral_frame_subboxed_reciprocal.md
audit/COMMON_METRIC_RANKTWO_SHARP_KERNEL_TRANSVERSE_SPECTRAL_FRAME_SUBBOXED_RECIPROCAL_REFEREE_AUDIT.md
tmp/research/common_metric_ranktwo_sharp_kernel_transverse_spectral_frame_positive_seam.md
audit/COMMON_METRIC_RANKTWO_SHARP_KERNEL_TRANSVERSE_SPECTRAL_FRAME_POSITIVE_SEAM_REFEREE_AUDIT.md
tmp/research/common_metric_ranktwo_sharp_kernel_transverse_spectral_frame_negative_seam_equality.md
audit/COMMON_METRIC_RANKTWO_SHARP_KERNEL_TRANSVERSE_SPECTRAL_FRAME_NEGATIVE_SEAM_EQUALITY_REFEREE_AUDIT.md
tmp/research/common_metric_ranktwo_sharp_kernel_transverse_spectral_frame_negative_meridian_face.md
audit/COMMON_METRIC_RANKTWO_SHARP_KERNEL_TRANSVERSE_SPECTRAL_FRAME_NEGATIVE_MERIDIAN_FACE_REFEREE_AUDIT.md
tmp/research/common_metric_negative_meridian_uniform_local_minimum.md
audit/COMMON_METRIC_NEGATIVE_MERIDIAN_UNIFORM_LOCAL_MINIMUM_REFEREE_AUDIT.md
tmp/research/common_metric_ranktwo_sharp_kernel_transverse_spectral_frame_negative_seam_collars.md
audit/COMMON_METRIC_RANKTWO_SHARP_KERNEL_TRANSVERSE_SPECTRAL_FRAME_NEGATIVE_SEAM_COLLARS_REFEREE_AUDIT.md
tmp/research/common_metric_ranktwo_sharp_kernel_transverse_spectral_frame_negative_gap_blowup.md
audit/COMMON_METRIC_RANKTWO_SHARP_KERNEL_TRANSVERSE_SPECTRAL_FRAME_NEGATIVE_GAP_BLOWUP_REFEREE_AUDIT.md
tmp/research/common_metric_tilted_rankone_complex_endpoint_orthogonal_atom_face.md
audit/COMMON_METRIC_TILTED_RANKONE_COMPLEX_ENDPOINT_ORTHOGONAL_ATOM_FACE_REFEREE_AUDIT.md
tmp/research/common_metric_tilted_rankone_q23_zero_face_theorem.md
audit/COMMON_METRIC_TILTED_RANKONE_Q23_ZERO_FACE_REFEREE_AUDIT.md
tmp/research/common_metric_tilted_rankone_complex_endpoint_nonneutral_strip.md
audit/COMMON_METRIC_TILTED_RANKONE_COMPLEX_ENDPOINT_NONNEUTRAL_STRIP_REFEREE_AUDIT.md
tmp/research/common_metric_tilted_rankone_complex_endpoint_nonneutral_phase_box.md
audit/COMMON_METRIC_TILTED_RANKONE_COMPLEX_ENDPOINT_NONNEUTRAL_PHASE_BOX_REFEREE_AUDIT.md
tmp/research/common_metric_tilted_rankone_complex_endpoint_neutral_circle_reduction.md
audit/COMMON_METRIC_TILTED_RANKONE_COMPLEX_ENDPOINT_NEUTRAL_CIRCLE_REDUCTION_REFEREE_AUDIT.md
tmp/research/common_metric_tilted_rankone_complex_endpoint_neutral_circle_projective_box.md
audit/COMMON_METRIC_TILTED_RANKONE_COMPLEX_ENDPOINT_NEUTRAL_CIRCLE_PROJECTIVE_BOX_REFEREE_AUDIT.md
tmp/research/common_metric_tilted_rankone_complex_endpoint_neutral_circle_base_interval.md
audit/COMMON_METRIC_TILTED_RANKONE_COMPLEX_ENDPOINT_NEUTRAL_CIRCLE_BASE_INTERVAL_REFEREE_AUDIT.md
tmp/research/common_metric_endpoint_neutral_dominance_route_obstruction.md
audit/COMMON_METRIC_ENDPOINT_NEUTRAL_DOMINANCE_ROUTE_OBSTRUCTION_REFEREE_AUDIT.md
tmp/research/common_metric_endpoint_neutral_beyond_dominance_base_interval.md
audit/COMMON_METRIC_ENDPOINT_NEUTRAL_BEYOND_DOMINANCE_BASE_INTERVAL_REFEREE_AUDIT.md
tmp/research/common_metric_endpoint_neutral_beyond_dominance_two_base_parameter_box.md
audit/COMMON_METRIC_ENDPOINT_NEUTRAL_BEYOND_DOMINANCE_TWO_BASE_PARAMETER_BOX_REFEREE_AUDIT.md
tmp/research/common_metric_endpoint_neutral_beyond_dominance_three_base_parameter_box.md
audit/COMMON_METRIC_ENDPOINT_NEUTRAL_BEYOND_DOMINANCE_THREE_BASE_PARAMETER_BOX_REFEREE_AUDIT.md
tmp/research/common_metric_endpoint_neutral_beyond_dominance_near_psd_scale_extension.md
audit/COMMON_METRIC_ENDPOINT_NEUTRAL_BEYOND_DOMINANCE_NEAR_PSD_SCALE_EXTENSION_REFEREE_AUDIT.md
tmp/research/common_metric_endpoint_neutral_disjoint_hnegative_shape_box.md
audit/COMMON_METRIC_ENDPOINT_NEUTRAL_DISJOINT_HNEGATIVE_SHAPE_BOX_REFEREE_AUDIT.md
tmp/research/common_metric_tilted_rankone_complex_boundary_opposite_phase_family.md
audit/COMMON_METRIC_TILTED_RANKONE_COMPLEX_BOUNDARY_OPPOSITE_PHASE_FAMILY_REFEREE_AUDIT.md
tmp/research/common_metric_tilted_rankone_complex_qg_absorption_no_go.md
audit/COMMON_METRIC_TILTED_RANKONE_COMPLEX_QG_ABSORPTION_NO_GO_REFEREE_AUDIT.md
tmp/research/common_metric_tilted_rankone_boundary_projection_metric_no_go.md
audit/COMMON_METRIC_TILTED_RANKONE_BOUNDARY_PROJECTION_METRIC_NO_GO_REFEREE_AUDIT.md
TWO_ATOM_VARIANCE_NOTE.md
RIGHT_ANGLE_COHERENT_FACTOR_NOTE.md
RIGHT_ANGLE_COHERENT_DUAL_NOTE.md
RIGHT_ANGLE_SQUARE_EXTENSION.md
RIGHT_ANGLE_SIGNED_RECURSION_NOTE.md
RIGHT_ANGLE_THREE_NODE_RANK_REDUCTION.md
RIGHT_ANGLE_THREE_NODE_DETERMINANT_LINEARIZATION.md
RIGHT_ANGLE_THREE_NODE_RANK13_NOTE.md
RIGHT_ANGLE_THREE_NODE_SYMMETRIC_THEOREM.md
tmp/research/three_node_rank22_elimination.md
tmp/research/right_angle_anchored_pick_no_go.md
tmp/research/three_node_rank22_asymmetric_box.md
RIGHT_ANGLE_RANK13_DEGREE2_OBSTRUCTION.md
tmp/research/rank13_maximum_principle_boundary_reduction.md
tmp/research/rank13_phi_theta_complex_a_theorem.md
audit/RANK13_PHI_THETA_COMPLEX_A_REFEREE_AUDIT.md
audit/RANK13_PHI_THETA_COMPLEX_A_CERTIFICATE_AUDIT.md
tmp/research/g01_phi_theta_degree6_common_metric.md
audit/G01_QUADRATIC_FULL_ARC_BREAKER_REFEREE_AUDIT.md
tmp/research/g01_phi_ta_real_rectangle.md
audit/G01_PHI_TA_REAL_RECTANGLE_REFEREE_AUDIT.md
tmp/research/g01_phi_i_real_zero_half_interval.md
audit/G01_PHI_I_REAL_ZERO_HALF_INTERVAL_REFEREE_AUDIT.md
tmp/research/g01_phi_i_real_zero_nine_tenths_extension.md
audit/G01_PHI_I_REAL_ZERO_NINE_TENTHS_REFEREE_AUDIT.md
tmp/research/g01_phi_i_real_zero_endpoint_diagonal_metric.md
audit/G01_PHI_I_REAL_ZERO_ENDPOINT_DIAGONAL_REFEREE_AUDIT.md
FINITE_NODE_SCHUR_BOUNDARY_REDUCTION.md
audit/FINITE_NODE_SCHUR_BOUNDARY_REDUCTION_REFEREE_AUDIT.md
FINITE_NODE_EXTREME_COUNTEREXAMPLE_REDUCTION.md
audit/FINITE_NODE_EXTREME_COUNTEREXAMPLE_REDUCTION_REFEREE_AUDIT.md
tmp/research/two_channel_evolving_direction_update.md
tmp/research/product_companion_direction_no_go.md
audit/TWO_CHANNEL_EVOLVING_DIRECTION_REFEREE_AUDIT.md
tmp/research/rank13_root_free_factor_insertion_gate.md
audit/RANK13_ROOT_FREE_FACTOR_INSERTION_GATE_REFEREE_AUDIT.md
tmp/research/rank13_global_small_zero_family.md
audit/RANK13_GLOBAL_SMALL_ZERO_FAMILY_REFEREE_AUDIT.md
tmp/research/global_two_small_zero_target_family.md
audit/GLOBAL_TWO_SMALL_ZERO_TARGET_FAMILY_REFEREE_AUDIT.md
tmp/research/two_channel_arbitrary_direction_no_go.md
audit/TWO_CHANNEL_ARBITRARY_DIRECTION_NO_GO_REFEREE_AUDIT.md
tmp/research/rank13_sharp_theta_outside_collar_and_exact_interval.md
audit/RANK13_OUTSIDE_COLLAR_EXACT_INTERVAL_REFEREE_AUDIT.md
tmp/research/rank22_schur_boundary_and_new_box.md
audit/RANK22_SCHUR_BOUNDARY_NEW_BOX_REFEREE_AUDIT.md
tmp/research/k3_to_kfin_n4_support_obstruction.md
audit/K3_TO_KFIN_N4_SUPPORT_OBSTRUCTION_REFEREE_AUDIT.md
RIGHT_ANGLE_ADDITIVE_ROW_OBSTRUCTION.md
audit/RIGHT_ANGLE_ADDITIVE_ROW_OBSTRUCTION_REFEREE_AUDIT.md
tmp/research/audit/n5_degree4_all_real_centers_rational_spline_sos.md
audit/N5_DEGREE4_ALL_REAL_CENTERS_SPLINE_SOS_REFEREE_AUDIT.md
CURRENT_BREAKPOINT_DELTA.md
WORKFLOW_AUDIT.md
RIGHT_ANGLE_THREE_NODE_ADVERSARY.md
RIGHT_ANGLE_KERNEL_NOTE.md
RIGHT_ANGLE_DUAL_NOTE.md
RIGHT_ANGLE_TANGENTIAL_MODEL.md
tmp/research/pi4_state_reduction.md
tmp/research/derive_finite_h_rank2_blocks.py
CLAIM_LEDGER.md
APPROACH_REGISTRY.md
COUNTEREXAMPLE_DB.md
LEAN_FORMALIZATION_PLAN.md
formalization/README.md
lens_constants.tex
```

Use `RESEARCH_HANDOFF.md` only as historical detail; where it conflicts with
`WORKFLOW_AUDIT.md` or this checkpoint, the newer documents control.

## 6. Portable environment reconstruction

Python 3.11.15 was used at the checkpoint.  The observed key package versions
were NumPy 2.4.6, SciPy 1.17.1, CVXPY 1.9.2, Clarabel 0.11.1, and SymPy 1.14.0.
The portable requirements intentionally specify compatible ranges rather
than machine-specific wheels.  `sparseqr` is not included because it needs a
machine-specific SuiteSparse toolchain and is not used by the live
right-angle route; install it separately only if reviving a historical
diagnostic.  The Lean verifier also expects `rg` (ripgrep).

On macOS or Linux, from the extracted root:

```bash
chmod +x bootstrap_portable.sh
./bootstrap_portable.sh
.venv/bin/python tmp/research/right_angle_agler_completion.py --help
.venv/bin/python tmp/research/right_angle_completion_dual.py --help
./verify_checkpoint.sh
```

For Lean, install `git`, `curl`, and `elan`, then run:

```bash
cd CrouzeixConjecture-main/Lean
lake update
lake build
cd ../..
./formalization/verify.sh
```

The reference project pins Lean `v4.28.0` and mathlib commit
`8f9d9cff6bd728b17a24e163c9402775d9e6a365`.  Its `.lake` directory is not
portable and is deliberately excluded; `lake update` reconstructs it.

To rebuild the current paper when a TeX distribution is available:

```bash
mkdir -p output/pdf
latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=output/pdf lens_constants.tex
```

The archive already contains the last successfully built PDF for comparison.

## 7. Suggested first prompt in the new account

Copy the text of `START_NEW_CODEX.txt` into the new task and attach or extract
the checkpoint archive.  Tell Codex that the extracted directory is the
workspace root.  The prompt forbids invented completion claims and directs it
to use only relative paths.

## 8. Integrity and portability

`CHECKPOINT_MANIFEST.sha256` binds every file inside the portable payload.
After extraction, verify from the payload root with:

```bash
shasum -a 256 -c CHECKPOINT_MANIFEST.sha256
```

On systems with GNU coreutils, `sha256sum -c CHECKPOINT_MANIFEST.sha256` can be
used after converting the manifest format if necessary.  The outer archive
hash is stored beside the archive.  Generated virtual environments, `.lake`,
`.git`, `.DS_Store`, Lean object files, and rejected multi-gigabyte SDP
artifacts are intentionally absent.
