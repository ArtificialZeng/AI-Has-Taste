# Exact optimum on the `p=1/2` slice

## Statement

Fix the graph, origin, boundary, and admissible auxiliary events from
`source.md`, and set `p=1/2`.  For `r in [3/4,1]`, let `F(r)` be the infimum
of the unconditional success probability

\[
 \mathbb P\!\left[\bigcup_{b\in B}
 (\{o\leftrightarrow b\}\cap E_b)\right]
\]

over all jointly defined families whose four increasing conditional marginal
kernels satisfy `P(E_b) >= r`.  Then the infimum is attained and

\[
F(r)=
\begin{cases}
\dfrac{182}{207}r,
 &\dfrac34\le r\le\dfrac{207}{256},\\[4pt]
\dfrac{19}{18}r-\dfrac{73}{512},
 &\dfrac{207}{256}\le r\le\dfrac{243}{256},\\[4pt]
\dfrac43r-\dfrac{13}{32},
 &\dfrac{243}{256}\le r\le\dfrac{63}{64},\\[4pt]
2r-\dfrac{17}{16},
 &\dfrac{63}{64}\le r\le1.
\end{cases}
\]

Consequently, with `r=1-t^2`,

\[
 F(1-t^2)>\frac{15}{16}(1-2t)
 \qquad(0<t\le 1/2).
\]

Thus the frozen inequality is true for the complete `p=1/2` slice.  This does
not settle any `p != 1/2` case, so the original problem remains unresolved.

## Exact finite proof

Write `Q_w(S)` for the conditional joint distribution of the occurring event
set, as in `problem.md`.  At `p=1/2` all 1024 configurations have mass
`1/1024`.  Averaging a feasible joint table over the 24 permutations of the
four boundary vertices preserves normalization, nonnegativity, marginal
monotonicity, and the success objective.  Every averaged event marginal is the
average of the original four event probabilities and is therefore at least
`r`.  Hence restricting to invariant tables does not change the optimum.

The invariant LP has 996 `(configuration, subset)` orbits, 90 normalization
equations, 984 distinct one-edge-cover marginal-monotonicity inequalities, and
one common marginal constraint.  In the convention

\[
 \min c^Tx,\qquad Ax\le b(r),\quad Ex={\bf1},\quad x\ge0,
\]

only the last component of `b(r)` varies, and it equals `-1024r`.  A dual
feasible pair `y <= 0`, `z` with

\[
 A^Ty+E^Tz\le c
\]

therefore supplies the affine lower bound

\[
 (-1024y_{\rm marg})r+{\bf1}^Tz.
\]

The serialized certificate contains invariant primal tables at

\[
 r=\frac34,\ \frac{207}{256},\ \frac{243}{256},\ \frac{63}{64},\ 1
\]

with respective exact objectives

\[
 \frac{91}{138},\ \frac{91}{128},\ \frac{55}{64},\
 \frac{29}{32},\ \frac{15}{16}.
\]

It also contains four exact dual feasible points whose slope-intercept pairs
are

\[
 (182/207,0),\quad(19/18,-73/512),\quad
 (4/3,-13/32),\quad(2,-17/16).
\]

On each interval between consecutive displayed values of `r`, convexly
interpolating its two endpoint primal tables gives a feasible table with
marginal exactly `r` and objective equal to the corresponding affine formula.
The corresponding dual point gives that same affine expression as a lower
bound for every `r` in the interval.  Primal and dual bounds coincide, proving
the stated formula on all of `[3/4,1]`.  The adjacent affine lines intersect
exactly at the three internal breakpoints.

The solver-free verifier expands each of the five primal orbit tables to all
1024 configurations.  It checks every normalization equation, every marginal
for all four vertices, and all one-edge-cover monotonicity comparisons.  It
also reconstructs every dual multiplier and checks all 996 reduced costs.  The
generation script uses HiGHS only to discover rational vertices; none of its
floating-point output is accepted as proof.

## Comparison with the required modulus

For `p=1/2`, the conditioning-event probability is
`1-(1-p)^4=15/16`.  On each affine branch, after substituting `r=1-t^2`, the
gap

\[
 D(t)=F(1-t^2)-\frac{15}{16}(1-2t)
\]

is a concave quadratic.  Its values at the consecutive branch endpoints
`t=1/2, 7/16, sqrt(13)/16, 1/8, 0` are

\[
 \frac{91}{138},\quad \frac{19}{32},\quad
 \frac{15\sqrt{13}-10}{128},\quad \frac{13}{64},\quad 0.
\]

The first four are positive; for the radical term this follows, for example,
by squaring the positive quantities (`225*13 > 100`).  Concavity makes the
gap no smaller than the lesser endpoint value on each closed branch.  On the
last branch incident with zero it factors as

\[
 D(t)=t\left(\frac{15}{8}-2t\right)>0
 \qquad(0<t\le1/8).
\]

This proves strict comparison throughout the frozen positive-`t` range.  The
gap has infimum zero as `t` decreases to zero, but zero is not attained in the
original domain.

## Scope and source comparison

The official arXiv record for Lucas Flammant, arXiv:2609.03492v1, was checked
again on 2026-09-07.  Its Conjecture 2.2 concerns an unspecified universal
modulus, while Theorem 2.3 gives `1-2sqrt(epsilon)` only under the planar
outer-face hypothesis; the record still lists only v1 and says the proof of
Theorem 2.4 is forthcoming.  `K_5` is nonplanar.  Bounded arXiv searches for
the `K_5` specialization, the defining conditional-monotonicity phrase, and
the exact slopes above returned no equivalent result.  This is a limited
comparison, not a claim of priority or proof of formal open status.

Primary endpoints:

- <https://arxiv.org/abs/2609.03492>
- <https://arxiv.org/html/2609.03492>

## Reproducible evidence

- `evidence/lp_p_half_parametric_certificate.json`
- `evidence/verify_lp_p_half_parametric.py`
- `evidence/lp_p_half_parametric.py`
- `evidence/lp_p_half_t_quarter.py` (shared orbit and graph routines)

