# Fresh mathematical audit

## Frozen scope and integrity

I reviewed the exact `resolution-paper` claim frozen in `claim.json`, namely

\[
W_2(L,R,d)=c_2^2L^2R^2
\quad(d\geq1,\ L>0,\ R\geq0),
\]

for the queried-gradient FGM recurrence in `source.md` and `problem.md`.  The
snapshot digest is
`6a00a06eb5398d38ae7fbf777eaafd922f200ff5cc110f0d64e3ee2ee0b09344`.
I recomputed every listed file hash and the canonical digest of the snapshot's
file map; all agree with `audit/snapshot.json`.  The source hash remains
`cb630d3906f2a0db9b936972143987f99a01faad43bec348a26b8f7c81dfadf8`.

The submitted theorem has not weakened the frozen statement: it retains every
finite dimension, every positive smoothness constant, the boundary `R=0`, and
the minimum over precisely the gradients queried at `x_0,x_1,x_2`.

## Reconstruction of the decisive argument

For `R>0`, translation and scaling reduce the upper bound to `L=R=1`, with
`x_*=0`, `f_*=0`, and `||x_0||<=1`.  Writing `a=1+beta` and
`c=1/(a+2)=c_2`, the two algorithmic updates are exactly

\[
x_1=x_0-g_0,\qquad x_2=x_0-g_0-a g_1.
\]

For every ordered pair of distinct indices in `{*,0,1,2}`, the proof uses

\[
h_{ij}=f_i-f_j-\langle g_j,x_i-x_j\rangle
       -\tfrac12\|g_i-g_j\|^2\geq0.
\]

The direction and constants are correct for differentiable convex
1-smooth interpolation.  They also follow directly by applying the unit-step
descent inequality to `f-<g_j,·>`, whose minimizer is `x_j`.

I reconstructed the coefficient identity in the Gram basis
`(x_0,g_0,g_1,g_2)`.  The ten nonzero interpolation multipliers in
`evidence/proof.md` have zero net coefficient on every function value; the
three performance multipliers sum to one.  With

\[
r=1-\|x_0\|^2,\qquad p_k=\|g_k\|^2-\tau,
\qquad \tau=\min_k\|g_k\|^2,
\]

the displayed slack matrix gives the exact identity

\[
c^2-\tau=c^2r+\sum_k\mu_kp_k+
\sum_{i\ne j}\lambda_{ij}h_{ij}+\langle S,\Gamma\rangle.
\]

Here `Gamma` is the Gram matrix and hence is positive semidefinite.  The
rational radical enclosure `1.281<a<1.282` proves every displayed multiplier
is nonnegative.  I checked the potentially smallest numerator
`172a^2-485a+342` at the correct decreasing endpoint; its stated positive
lower bound is exact.  The same endpoint arguments for the other nonconstant
multipliers are valid.

For the slack, the algebraic relation

\[
a^4-8a^3+10a^2-a-1=0
\]

holds for the specified radical, and the printed matrix satisfies
`S(1,c,c,c)^T=0`.  Its lower-right `3 x 3` block has three positive leading
principal minors.  Reducing their numerators by the algebraic relation gives
the two stated cubics; termwise outward evaluation on
`[1281/1000,641/500]` gives the positive rational lower bounds

\[
2445271097527/5000000,
\qquad 205845508080081/7812500.
\]

Thus that block is positive definite by Sylvester's criterion.  The kernel
identity then rewrites the full quadratic form as
`(z-cu*1)^T B (z-cu*1)`, proving `S` is positive semidefinite.  Every term on
the right of the certificate identity is therefore nonnegative, and
`tau<=c^2` uniformly in dimension.

The lower construction also checks out.  For the segment `K=[0,ce]`, the
function

\[
f(x)=\max_{g\in K}\{\langle x,g\rangle-\tfrac12\|g\|^2\}
\]

has gradient `Proj_K`, so it is convex and 1-smooth.  Since `c<1/2`, its first
two queried points lie in the required projection regions, and

\[
x_1=(1-c)e,\qquad x_2=(1-c-ac)e=ce,
\]

with all three queried gradients equal to `ce`.  This matches the upper bound
in every dimension by embedding the line.  The scaling
`f_{L,R}(x)=LR^2 f((x-x_*)/R)` has gradient Lipschitz constant `L` and gives
the factor `L^2R^2`.  When `R=0`, `x_0=x_*`, all updates remain at the
minimizer, and both sides vanish.  No division by `R` is used for that boundary
case.

## Independent checks and attack results

I ran `evidence/verify_exact_dual.py`; it completed and reported exact
coefficient cancellation, twelve interpolation inequalities, a rank-three
positive-semidefinite slack test, and objective `c_2^2`.

I also wrote and ran `audit/referee_recheck.py`.  This second check entered the
matrix printed in the proof independently from the multiplier construction,
then rebuilt all function-value and Gram coefficients and reduced them modulo
the algebraic polynomial.  It verified zero flow, the exact printed-slack
identity, the kernel, the three positive Sylvester bounds, and the lower
witness recurrence.  A separate high-precision eigenvalue sanity check gave
one numerical zero and three positive eigenvalues; this was used only as a
sanity check, not as the PSD proof.

I specifically attacked the recurrence coefficient, interpolation-inequality
orientation, omitted zero multipliers, radius inequality, algebraic-root
selection, PSD-to-trace step, dimension quantifier, equality construction,
scaling, and `R=0` degeneracy.  I found no gap or hidden scope restriction.

## Source comparison and verdict

Within the frozen source record, the nearest cited analytic result is Du's
general upper bound `W_2<=L^2R^2/S_2`, which is strictly weaker, and the
analytic cases `2<=N<=6` are recorded as open.  The submitted exact dual
certificate supplies precisely the missing sharp upper bound at `N=2`, while
the frozen one-dimensional witness supplies equality.  The claim makes no
broader literature-priority assertion beyond this comparison.

**Verdict: accept.**  The evidence proves the original frozen claim in its
full scope, so the candidate qualifies as a `resolution-paper` with original
status `proved`.  There is no unresolved mathematical repair item in the
reviewed scope.
