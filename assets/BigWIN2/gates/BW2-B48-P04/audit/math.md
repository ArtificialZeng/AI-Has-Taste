# Fresh mathematical referee report

## Frozen scope

I reviewed the `result-note` claim bound to snapshot
`0b47952ae65bd0306a9d705c281d99d79187e1f42c1db505e961a76dcfdf6407`.
The claim is a classification of the exact optimum only on the slice
`p=1/2`; it explicitly leaves every `p != 1/2` case and hence the original
all-`p` problem unresolved.  I did not reinterpret this as a full resolution.

The audited statement defines `F(r)`, for `3/4 <= r <= 1`, as the minimum
unconditional success probability over all admissible jointly defined event
families.  It asserts the four affine branches

\[
 (182r/207),\quad (19r/18-73/512),\quad
 (4r/3-13/32),\quad (2r-17/16)
\]

on the consecutive intervals with breakpoints

\[
 3/4,\quad 207/256,\quad 243/256,\quad 63/64,\quad 1,
\]

and the strict comparison
`F(1-t^2) > (15/16)(1-2t)` for `0<t<=1/2`.

## Reconstruction of the decisive argument

For every percolation configuration `w` and occurring-event subset
`S subseteq B`, the variables `Q_w(S)` give a complete conditional joint law.
The normalization and nonnegativity constraints make each row a probability
distribution.  The only monotonicity constraints required by the original
problem are the one-edge-cover inequalities on each of the four marginals
`q_b(w)=sum_{S contains b} Q_w(S)`.  These cover inequalities imply all
coordinatewise comparisons.  Conversely, any such finite family of
conditional distributions is realizable with auxiliary randomness.  Thus the
LP does not impose independence or otherwise restrict the allowed joint event
families.

At `p=1/2`, all 1024 configurations have equal mass.  Averaging any feasible
table over the 24 automorphisms that fix the origin preserves the objective,
normalization, nonnegativity, and marginal monotonicity.  Every marginal of
the averaged table equals the average of the original four unconditional
event probabilities, and is therefore at least `r`.  Hence restricting to
invariant tables preserves the optimum.  The converse inclusion is immediate.
This justifies the reduction to 996 `(w,S)` orbits, 90 configuration orbits,
984 distinct marginal-cover rows, and one common probability constraint.

In the convention

\[
 \min c^Tx,\qquad Ax\le b(r),\qquad Ex={\bf1},\qquad x\ge0,
\]

the last right-hand side is `-1024r`.  A dual pair with `y<=0` and
`A^T y+E^T z<=c` gives the lower bound

\[
 (-1024y_{\rm marg})r+{\bf1}^Tz.
\]

The certificate supplies feasible primal tables at all five breakpoints with
objectives

\[
 91/138,\quad 91/128,\quad 55/64,\quad 29/32,\quad 15/16,
\]

and feasible duals having precisely the four claimed slope/intercept pairs.
On each adjacent-breakpoint interval, convex interpolation of the two primal
tables is feasible with marginal exactly `r` and has the claimed affine
objective.  The matching dual is a lower bound for every `r` in that interval.
The equal bounds prove the entire piecewise formula, not merely its values at
sampled parameters.  Compactness of the finite feasible polytope also shows
that the minimum is attained.

Finally, substituting `r=1-t^2` makes the gap from
`(15/16)(1-2t)` a concave quadratic on each branch.  Its consecutive endpoint
values are

\[
 91/138,\quad 19/32,\quad (15\sqrt{13}-10)/128,\quad 13/64,\quad 0.
\]

The first four are positive, including the radical value because
`225*13>100`.  Concavity reduces each closed branch to its endpoints.  On the
only branch incident to `t=0`, the gap is
`t(15/8-2t)>0` for `0<t<=1/8`.  This establishes the claimed strict inequality
on the complete positive-`t` range.

## Checks actually performed

- I checked the SHA-256 values of `source.md`, `problem.md`, `claim.json`, and
  every listed mathematical evidence file other than `checkpoint.md` against
  `audit/snapshot.json`; they match.  I did not read `checkpoint.md`, as the
  referee assignment expressly prohibited it.
- I ran the supplied solver-free verifier.  It expanded every endpoint orbit
  table to all 1024 configurations and reported zero normalization and
  monotonicity failures, four exact marginals at each endpoint, and the five
  objectives displayed above.  It also found no positive inequality duals and
  no negative reduced costs for any of the four dual certificates.
- I independently rebuilt the group action, orbit representatives,
  connectivity sets, normalization rows, marginal cover inequalities,
  objective, and dual constraints in `audit/referee_replay.py`, using exact
  rational arithmetic and without importing the supplied verifier.  This
  second replay again obtained 996 pair orbits, 90 configuration orbits, and
  984 distinct monotonicity rows; all five full endpoint replays and all four
  dual checks passed.  Reproduce with
  `python3 audit/referee_replay.py`.
- I separately checked the symmetrization argument, dual sign convention,
  breakpoint intersections, interpolation step, and concave-quadratic target
  comparison.  I found no quantifier loss, dependence assumption, division by
  zero, endpoint omission, or sampled-to-parametric inference.

## Source comparison and contribution

The current official record and HTML for Lucas Flammant,
arXiv:2609.03492v1 (submitted 2026-09-03), were checked on 2026-09-07.  Its
Definition 2.1 permits auxiliary randomness and uses the same conditional
monotonicity.  Conjecture 2.2 asks only for some universal modulus tending to
one.  Theorem 2.3 gives `1-2 sqrt(epsilon)` under a planar outer-face
hypothesis, which does not apply to nonplanar `K_5`; the record still lists
only v1.  A bounded arXiv search for the `K_5` specialization and the exact
certificate slopes found no equivalent result.  This supports only the
limited comparison stated in the claim, not priority or formal open status.

An exact four-branch optimum over arbitrary joint auxiliary-event kernels on
a canonical nonplanar graph slice is a nontrivial subsidiary classification.
It supplies a rigorous benchmark for the remaining `p`-parametric problem and
proves the frozen modulus for the complete `p=1/2` slice.  It is not a routine
application of the planar theorem and is not an arbitrary toy restriction.

## Gaps and verdict

No mathematical or scope gap was found in the frozen result-note.  The result
does not address `p != 1/2`, and the original problem remains unresolved, as
the claim correctly states.  The bounded literature screen is not a priority
claim.

**Verdict: accept.**
