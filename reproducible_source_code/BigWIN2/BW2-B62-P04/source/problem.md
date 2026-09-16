# Precise problem reading

## Frozen scope

For every integer \(n\ge 1\) and every real \(\alpha\in[0,1)\), consider the probability measure
\[
P_\alpha=(1-\alpha)\,\mathrm{Unif}[0,1]+\alpha\,\delta_1
\]
on \([0,1]\).  A feasible ladder is an \(n\)-tuple
\[
(R_1,\ldots,R_n)\quad\text{with}\quad 0=R_0<R_1<\cdots<R_n\le 1.
\]
For each \(B\in[0,1]\), including \(B=1\), define
\[
R(B)=\max\{R_i:0\le i\le n,\ R_i\le B\}.
\]
The loss is \(\ell(B)=B-R(B)\).  The requested quantity is the infimum
\[
L^*_{n,\alpha}=\inf_{0<R_1<\cdots<R_n\le1}
\mathbb E_{B\sim P_\alpha}[\ell(B)].
\]
The task is to give, with proof:

1. a piecewise closed form for \(L^*_{n,\alpha}\) for all quantified \((n,\alpha)\), including every transition value of \(\alpha\);
2. whether the infimum is attained in the stated (partly open) feasible set;
3. all feasible ladders attaining it whenever it is attained;
4. checks for \(n=1,2\), \(\alpha=0\), every active-set transition, and the one-sided limit \(\alpha\uparrow1\).

The excluded parameter \(\alpha=1\) is not silently added to the theorem.  It may be discussed only as an endpoint limit (or as a separately labelled observation).

## Exact gap formulation to be proved

Set
\[
\Delta_i=R_{i+1}-R_i\quad(0\le i<n),\qquad
\Delta_n=1-R_n.
\]
Then the ladder constraints are exactly
\[
\Delta_i>0\ (0\le i<n),\qquad \Delta_n\ge0,
\qquad \sum_{i=0}^n\Delta_i=1.
\]
Thus \(\Delta_n=0\) is feasible and means \(R_n=1\), whereas setting any
\(\Delta_i=0\) for \(i<n\) violates strict ladder increase.

On a uniform draw, the interval \([R_i,R_{i+1})\) contributes
\(\int_{R_i}^{R_{i+1}}(B-R_i)\,dB=\Delta_i^2/2\), with
\(R_{n+1}=1\); endpoint conventions do not affect the continuous integral.
At the atom, however, \(R(1)=R_n\), so its loss is exactly
\(1-R_n=\Delta_n\).  Consequently the original problem is equivalent to
proving the optimum and equality cases of
\[
\inf\left\{
\frac{1-\alpha}{2}\sum_{i=0}^n\Delta_i^2+\alpha\Delta_n:
\Delta_0,\ldots,\Delta_{n-1}>0,\ \Delta_n\ge0,\
\sum_{i=0}^n\Delta_i=1
\right\}.
\]
This equivalence is part of the required proof, not an assumption imported into
the frozen statement.

## Source status and nearest prior result

Status at triage: **new-question / exact status not independently established**.
The frozen problem is a finite-\(n\), single-endpoint-atom specialization, not
the full atom extension mentioned by the source.  No claim of novelty or priority
is made.

The primary source inspected on 2026-09-07 was Yuriy A. Reznik,
*A Quantization Problem Posed by Adaptive Streaming*, arXiv:2609.03745v1,
<https://arxiv.org/abs/2609.03745>.  Its relevant locations are:

- Eq. (1) and the client rule leading to the one-sided quality gap, pp. 4--5;
- Proposition 1, p. 8, for the asymptotic \(C^1\)-density setting;
- Remark 1 and Example 1, pp. 8--9: the broad atom extension is identified as
  open, while the atom-free uniform/linear case has exact value
  \(1/(2(n+1))\) with equal cells;
- concluding open problems, p. 16, again naming distributions with atoms.

Exact-assertion and equivalent-language searches on 2026-09-07 recovered the
Reznik preprint but no primary source stating this exact endpoint-mixture,
finite-\(n\) formula.  Standard scalar-quantization results returned by the broad
search use free/centroid reproduction points or a different distortion/constraint
and therefore do not settle this edge-constrained problem.  This is a limited
literature screen, not evidence of priority.

## Proposed contribution and bounded verification route

Nearest prior result \(X\): Reznik's exact atom-free uniform example and its
broader open invitation for atomic bandwidth laws.  Proposed delta \(Y\): solve
the above one-endpoint-atom specialization exactly at every finite \(n\), including
the boundary active set and every equality case.  Verification route \(Z\): reduce
the first \(n\) gaps by strict convexity/Cauchy--Schwarz at fixed \(\Delta_n\),
solve the resulting one-variable convex quadratic with the constraint
\(\Delta_n\ge0\), and independently check \(n=1,2\) and transition/endpoints by
direct symbolic optimization.

