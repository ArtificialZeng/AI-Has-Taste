# Fresh mathematical referee report

Referee job: `win-00062-p04-referee-5ffded10110a`  
Frozen snapshot: `e29b1a1ce4401ba5474317a758bce57dfbfc1da2e9ed763464850477cf537fe9`

## Scope and integrity

I reviewed the exact `resolution-paper` claim for every integer (n\geq 1)
and every (0\leq\alpha<1), without extending the claim to \(\alpha=1\) or
to general atomic bandwidth laws. I independently recomputed the SHA-256
digest of every file in `audit/snapshot.json`; all five file hashes match.
Canonical sorted compact JSON serialization of the recorded file map also
recomputes the snapshot digest displayed above.

## Reconstruction of the decisive argument

Put (R_{n+1}=1),

\[
\Delta_i=R_{i+1}-R_i\quad(0\leq i<n),\qquad
\Delta_n=1-R_n.
\]

This is a bijective reparameterization of the feasible ladders by

\[
\Delta_0,\ldots,\Delta_{n-1}>0,\qquad \Delta_n\geq0,
\qquad \sum_{i=0}^n\Delta_i=1.
\]

In particular, only the last gap may vanish. On the uniform part, cell (i)
contributes

\[
\int_{R_i}^{R_{i+1}}(B-R_i)\,dB=\frac{\Delta_i^2}{2}.
\]

Whether the right endpoint is included is immaterial for this continuous
integral. At the point mass, however, the selection rule gives
(R(1)=R_n), so the atomic loss is exactly (1-R_n=\Delta_n), including
the case (R_n=1). Thus, writing (c=1-\alpha>0), the exact objective is

\[
F(\Delta)=\frac c2\sum_{i=0}^n\Delta_i^2+\alpha\Delta_n.
\]

Fix (t=\Delta_n\). Feasibility gives (0\leq t<1). Since the first (n)
gaps have sum (1-t), Cauchy--Schwarz gives

\[
\sum_{i=0}^{n-1}\Delta_i^2\geq\frac{(1-t)^2}{n},
\]

with equality precisely when every one of those gaps is
((1-t)/n>0). Hence the original problem reduces without relaxing any
strict inequality to minimizing

\[
g(t)=\frac c2\left(\frac{(1-t)^2}{n}+t^2\right)+\alpha t,
\qquad 0\leq t<1.
\]

Here

\[
g''(t)=\frac{c(n+1)}n>0,
\qquad
g'(0)=\frac{(n+1)\alpha-1}{n},
\]

and the unconstrained critical point is

\[
t_0=\frac{1-(n+1)\alpha}{(n+1)(1-\alpha)}.
\]

For (0\leq\alpha<1/(n+1)), one has (0<t_0<1), and the unique minimum
has

\[
\Delta_n=t_0,\qquad
\Delta_0=\cdots=\Delta_{n-1}
=\frac1{(n+1)(1-\alpha)}.
\]

At and above the transition, (g'(0)\geq0), so the unique constrained
minimum is (t=0), with every first gap equal to (1/n). All first gaps
are strictly positive in both cases. Thus the minimum is attained in the
original partly open feasible set, not merely in its closure.

Substitution gives exactly

\[
L^*_{n,\alpha}=
\begin{cases}
\dfrac{1-(n+1)\alpha^2}{2(n+1)(1-\alpha)},
&0\leq\alpha\leq\dfrac1{n+1},\\[6pt]
\dfrac{1-\alpha}{2n},
&\dfrac1{n+1}\leq\alpha<1.
\end{cases}
\]

The equality condition in Cauchy--Schwarz together with strict convexity of
(g) proves uniqueness. Summing the gaps recovers precisely the two ladders
stated in `claim.json`. At (alpha=1/(n+1)), both descriptions give
(R_i=i/n), so there is no missing equality case.

## Adversarial and endpoint checks

- There is no empty quantified domain: (n\geq1). Division by (n) and by
  (1-\alpha) is therefore valid throughout.
- The open endpoint (t=1) corresponds to all first gaps summing to zero and
  is infeasible. Neither candidate minimum approaches it; the proof does not
  rely on compactness of the open feasible set.
- The feasible equality (Delta_n=0) is used exactly in the second regime.
  No vanishing interior gap is introduced.
- For (n=1), direct differentiation of
  (c(r^2+(1-r)^2)/2+\alpha(1-r)) gives (r=1/(2c)) until
  (alpha=1/2), then (r=1), with the claimed values.
- For (n=2), the two direct stationarity equations give
  ((R_1,R_2)=(1/(3c),2/(3c))) while (alpha\leq1/3); the active face
  (R_2=1) gives (R_1=1/2) thereafter. These are the claimed special
  cases.
- At (alpha=0), all (n+1) gaps equal (1/(n+1)), and the value is
  (1/(2(n+1))). At the transition, the two value formulas both give
  (1/(2(n+1))). As (alpha\uparrow1), the optimizer remains (R_i=i/n)
  and the value tends to zero. The excluded case (alpha=1) would have
  nonunique minimizers and is correctly kept outside the theorem.

## Source comparison and contribution

The supplied Reznik preprint has the recorded PDF hash
`9204ad1b5dccb6812c5374d4041982ce44ce6c8a3c6486e71bee4cbbbc48523e`.
Its client rule and one-sided loss match the frozen interpretation. Its
Proposition 1 concerns a high-resolution compact-interval setting with a
(C^1) density; Remark 1 explicitly leaves extension to distributions with
atoms open. Example 1 gives the exact atom-free uniform value
(1/(2(n+1))) by equal gaps. The candidate adds the exact finite-(n)
endpoint-atom active-set solution while expressly making no novelty or priority
claim and no claim about general atomic laws. This is a complete resolution of
the frozen original scope and does not silently substitute the broader open
problem.

## Verdict

**Accept.** The objective, constraints, transition, value, attainment, all
optimizers, low-dimensional checks, and endpoint cases are correct in the exact
frozen scope. I found no unresolved mathematical gap in the submitted claim.
