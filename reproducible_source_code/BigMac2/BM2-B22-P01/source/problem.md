# Precise problem: the sharp queried-gradient constant of FGM at horizon 2

## Provenance and status

This file fixes the mathematical reading of the immutable statement in
`source.md`.  The cited primary source is Yi Du, *When a Relaxed PEP Is Exact:
The Sharp Queried-Gradient Rate of Nesterov's Fast Gradient Method*,
arXiv:2608.26719v1 (2026-08-27).  According to the source record, that paper
leaves the analytic characterization for horizons `2 <= N <= 6` open.  The
closed form below is a conjecture of this project, not a theorem or conjecture
stated in that paper.  No independent literature-priority claim is made here.

## Objects and algorithm

Fix

\[
 d\in\mathbb Z_{\ge 1},\qquad L>0,\qquad R\ge 0.
\]

Let \(\mathcal F_{0,L}(\mathbb R^d)\) be the class of everywhere differentiable
convex functions \(f:\mathbb R^d\to\mathbb R\) whose gradients satisfy

\[
 \|\nabla f(x)-\nabla f(y)\|\le L\|x-y\|
 \quad\text{for every }x,y\in\mathbb R^d.
\]

A feasible instance is a triple \((f,x_*,x_0)\) with
\(f\in\mathcal F_{0,L}(\mathbb R^d)\),
\(x_*\in\operatorname*{argmin} f\), and
\(\|x_0-x_*\|\le R\).  Starting with \(y_0=x_0\) and \(t_0=1\), perform exactly
two FGM updates, for \(k=0,1\):

\[
 \begin{aligned}
 y_{k+1}&=x_k-\frac1L\nabla f(x_k),\\
 t_{k+1}&=\frac{1+\sqrt{1+4t_k^2}}2,\\
 x_{k+1}&=y_{k+1}+\frac{t_k-1}{t_{k+1}}(y_{k+1}-y_k).
 \end{aligned}
\]

Thus gradients are queried at the three points \(x_0,x_1,x_2\); the value at
\(x_2\) is measured but is not used in another update.  In particular,

\[
 t_1=\frac{1+\sqrt5}{2},\qquad
 t_2=\frac{1+\sqrt{7+2\sqrt5}}2,
 \qquad x_1=y_1,
\]

and, on writing

\[
 \beta:=\frac{t_1-1}{t_2}
 =\frac{\sqrt5-1}{1+\sqrt{7+2\sqrt5}},
\]

the second extrapolation is \(x_2=y_2+\beta(y_2-y_1)\).

## Performance measure and frozen conjecture

Define

\[
 W_2(L,R,d):=
 \sup_{\substack{f\in\mathcal F_{0,L}(\mathbb R^d),\;
                   x_*\in\arg\min f\\
                   \|x_0-x_*\|\le R}}
 \min_{k\in\{0,1,2\}}\|\nabla f(x_k)\|^2,
\]

where \(x_1,x_2\) are generated from the same feasible instance by the above
recurrence.  Set

\[
 c_2:=\frac1{3+\beta}.
\]

The frozen claim to prove or disprove is

\[
 \boxed{\quad
 \forall d\in\mathbb Z_{\ge1}\ \forall L>0\ \forall R\ge0:\qquad
 W_2(L,R,d)=c_2^2L^2R^2.
 \quad}
\]

Here
\(c_2^2=0.0928513193578614102140718294340\ldots\).  For \(R>0\), the standard
translation and scaling reduce the assertion to \(L=R=1\), separately for
each dimension \(d\).  The boundary case \(R=0\) is part of the claim: then
\(x_0=x_*\), differentiable convex optimality gives \(\nabla f(x_*)=0\), all
iterates remain at \(x_*\), and both sides equal zero.

## Rigorous bounds already supplied

The source records the following exact one-dimensional witness for the lower
bound.  In the normalization \(L=R=1\), take a unit vector \(e\),
\(K=[0,c_2e]\), and

\[
 f(x)=\max_{g\in K}\left\{\langle x,g\rangle-\tfrac12\|g\|^2\right\}.
\]

Then \(f\in\mathcal F_{0,1}(\mathbb R^d)\),
\(\nabla f(x)=\operatorname{Proj}_K(x)\), \(x_*=0\), and \(x_0=e\).  Since
\(c_2<1/2\), direct substitution gives

\[
 x_1=(1-c_2)e,
 \qquad x_2=\bigl(1-(2+\beta)c_2\bigr)e=c_2e,
 \qquad \nabla f(x_0)=\nabla f(x_1)=\nabla f(x_2)=c_2e.
\]

Scaling this witness and embedding its line in every \(\mathbb R^d\) proves

\[
 c_2^2L^2R^2\le W_2(L,R,d).
\]

The nearest cited general analytic result is Theorem 2.1 of the source paper,
which gives, with \(S_2=t_0^2+t_1^2+t_2^2\),

\[
 W_2(L,R,d)\le \frac{L^2R^2}{S_2}.
\]

The bounds are strictly separated:

\[
 c_2^2=0.0928513193578614\ldots
 <\frac1{S_2}=0.1186296604458931\ldots.
\]

Consequently the missing mathematical step is a sharp upper certificate at
\(c_2^2\), or an exact feasible counterexample strictly above \(c_2^2\).

## Scope and completion standard

- The criterion uses only queried gradients at \(x_0,x_1,x_2\), not gradients
  at the post-gradient points \(y_k\).
- The statement covers every finite integer dimension \(d\ge1\); a fixed-
  dimensional computation cannot by itself establish the universal claim.
- The paper's results for \(N=1\) and \(N\ge7\) do not settle this \(N=2\)
  statement.
- The reported floating-point PEP value near \(c_2^2\), numerical sampling,
  and a small numerical primal-dual gap are evidence only, not a proof.
- A proof requires an exact inequality or complete exact-PEP dual certificate
  yielding the upper bound \(W_2(1,1,d)\le c_2^2\) uniformly in dimension.
  A disproof requires exact smooth-convex interpolation/Gram data satisfying
  the full recurrence and radius constraint with all three squared gradient
  norms strictly greater than \(c_2^2\).

