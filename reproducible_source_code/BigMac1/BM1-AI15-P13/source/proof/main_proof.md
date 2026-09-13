# Exact disproof and structural refinement theorem

## Result and scope

The condition-number-only conjecture is false for the literal SM-IR
Algorithm 2 of Hashemi--Nakatsukasa.  The counterexample is an exact
round-to-nearest/ties-to-even fixed point, not a numerical experiment.  It
does not contradict their conditional Theorems 4.6--4.7, and it leaves open a
repaired algorithm with a scale/denominator guard or fallback solve.

## Theorem 1 (all-precision scalar counterexample)

Let arithmetic have radix two, precision \(p\ge2\), round-to-nearest with
ties-to-even, unit roundoff \(\epsilon=2^{-p}\), and enough exponent range for
\(2^p\).  Apply the operation order in Algorithms 1--2 to

\[
 A=[1],\qquad u=[1],\qquad v=[2^p],\qquad b=[1].
\]

Then the exact updated matrix is \(B=[2^p+1]\),
\(\kappa_2(A)=\kappa_2(B)=1\), and every computed iterate is
\(\widehat x_k=0\).  Its normwise and componentwise relative backward errors
are exactly one.  Therefore SM-IR is not uniformly backward stable under the
two condition-number hypotheses alone.

### Proof

At \(2^p\), the adjacent precision-\(p\) binary numbers are \(2^p\) and
\(2^p+2\).  The exact number \(2^p+1\) is their midpoint.  The lower endpoint
has even integer significand \(2^{p-1}\), whereas the upper endpoint has odd
integer significand \(2^{p-1}+1\).  Hence

\[
 \operatorname{RN}_{\rm even}(2^p+1)=2^p. \tag{1}
\]

The initial SM computation is otherwise exact:

\[
 \widehat y=1,\quad \widehat z=1,\quad
 \widehat\alpha=2^p,\quad \widehat\beta=2^p,\quad
 \widehat\theta=1,\quad \widehat x_0=1-1=0. \tag{2}
\]

If \(\widehat x_k=0\), the separated residual of Algorithm 2 is exactly
\(\widehat r_k=1\).  The correction repeats (2):
\(\widehat y_{r,k}=1\), \(\widehat\alpha_{r,k}=2^p\),
\(\widehat\theta_{r,k}=1\), so the correction is \(1-1=0\).  Every common
association of Step 5 uses only exact zeros and ones and gives
\(\widehat x_{k+1}=0\).  Induction proves the claim for all \(k\).

Finally,

\[
 \eta_B(0)=\frac{|1-(2^p+1)0|}{|2^p+1|\,|0|+|1|}=1. \tag{3}
\]

If backward error permits perturbing only \(B\), it is even worse: no matrix
perturbation can make \((B+\Delta B)0=1\).  Since
\(\eta_B(0)/\epsilon=2^p\to\infty\), no precision-independent constant hidden
in \(O(\epsilon)\) repairs the conclusion.  This proves the theorem. \(\square\)

For binary64, \(p=53\); the source paper's experimental success threshold
\(5\epsilon\) is missed by the exact factor \(1/(5\epsilon)=2^{53}/5\).

## Theorem 2 (two-dimensional safely-conditioned embedding)

For \(p\ge4\), set \(m=\lfloor p/2\rfloor\) and

\[
 A=\operatorname{diag}(1,2^m),\quad
 u=b=e_1,\quad v=2^p e_1,\quad
 B=\operatorname{diag}(2^p+1,2^m).
\]

With exact diagonal division as the backward-stable \(A\)-solver, the same
calculation in the first coordinate gives \(\widehat x_k=0\) and
\(\eta_B(\widehat x_k)=1\) for all \(k\).  Moreover,

\[
 \kappa_2(A)=2^m,\qquad
 \kappa_2(B)=\frac{2^p+1}{2^m}=2^{p-m}+2^{-m},
\]

so

\[
 \epsilon\kappa_2(A)=2^{m-p}\to0,qquad
 \epsilon\kappa_2(B)=2^{-m}+2^{-p-m}\to0.
\]

Thus both condition numbers are asymptotically *safely* below
\(\epsilon^{-1}\), even in a fixed nontrivial dimension.  The proof is the
scalar proof in the invariant first coordinate; the second coordinate is
exactly zero throughout.  For binary64, \(m=26\),

\[
 \kappa_2(A)=2^{26},\qquad
 \kappa_2(B)=2^{27}+2^{-26},
\]

versus \(\epsilon^{-1}=2^{53}\). \(\square\)

## Lemma 3 (condition numbers permit a dangerous denominator scale)

Let \(n\ge2\), \(B=A+uv^T\), and
\(\beta=1+v^TA^{-1}u\ne0\).  Then

\[
 \frac1{\kappa_2(A)\kappa_2(B)}
 \le |\beta|\le
 \kappa_2(A)\kappa_2(B). \tag{4}
\]

Indeed, choose nonzero \(q\in\ker v^T\).  Since \(Aq=Bq\),

\[
 \frac{\|B\|_2}{\|A\|_2}\le\kappa_2(B),
 \qquad
 \frac{\|A\|_2}{\|B\|_2}\le\kappa_2(A). \tag{5}
\]

The rank-one matrix \(BA^{-1}=I+uv^TA^{-1}\) has exceptional eigenvalue
\(\beta\), hence

\[
 |\beta|\le\|BA^{-1}\|_2
 \le \kappa_2(A)\frac{\|B\|_2}{\|A\|_2}
 \le\kappa_2(A)\kappa_2(B).
\]

Applying the same argument to \(AB^{-1}\), whose exceptional eigenvalue is
\(\beta^{-1}\), gives the lower bound.  The two-dimensional family saturates
the upper bound:
\(\beta=\kappa_2(A)\kappa_2(B)=2^p+1\).  Thus the separate assumptions
\(\epsilon\kappa_2(A),\epsilon\kappa_2(B)\ll1\) still allow
\(\epsilon|\beta|\asymp1\).  A product condition may block this particular
mechanism, but is not asserted sufficient for the complete rounded algorithm.

## Lemma 4 (exact denominator-error reduction)

This lemma explains the obstruction and identifies a missing hypothesis.
Suppose \(A\)-solves and vector operations are exact but a fixed nonzero
\(\widehat\beta\) replaces

\[
 z=A^{-1}u,\qquad t=v^Tz,\qquad \beta=1+t.
\]

The reusable SM corrector is

\[
 M=A^{-1}-\frac{zv^TA^{-1}}{\widehat\beta}.
\]

Writing \(d=\widehat\beta-\beta\), direct multiplication gives

\[
 I-BM=-\frac{d}{\widehat\beta}uv^TA^{-1}=:R. \tag{6}
\]

It has rank at most one and its only possibly nonzero eigenvalue is

\[
 \lambda=-\frac{dt}{\widehat\beta}. \tag{7}
\]

Thus \(R^2=\lambda R\); with exact residual/update,
\(r_{k+1}=Rr_k\), and after the first step
\(r_{k+1}=\lambda^k r_1\).  Outside the exceptional nullspace, contraction is
equivalent to \(|\lambda|<1\).  In Theorem 1,
\(t=2^p,\beta=2^p+1,\widehat\beta=2^p,d=-1\), hence
\(\lambda=1\) and \(M=0\).

If \(|d|\le\sigma|\beta|\) with \(0\le\sigma<1\), then

\[
 |\lambda|\le\frac{\sigma|t|}{1-\sigma};
\]

the scale-sensitive condition \(\sigma(1+|t|)<1\) is sufficient for
contraction.  Neither spectral condition number controls \(t\).

## Proposition 5 (conditional positive recurrence)

Let \(r_k=b-Bx_k\) be the exact residual.  Represent one implemented step by

\[
 \widehat r_k=r_k+f_k,\qquad
 c_k=\widehat r_k-Bd_k,\qquad
 x_{k+1}=x_k+d_k+s_k.
\]

Here \(f_k\) is residual-evaluation error, \(c_k\) is the correction solver's
remaining residual, and \(s_k\) is update rounding.  Exact substitution gives

\[
 r_{k+1}=-f_k+c_k-Bs_k. \tag{8}
\]

If \(\|c_k\|_2\le\rho\|\widehat r_k\|_2\) uniformly for some
\(0\le\rho<1\), and relative to a fixed scale \(D>0\),

\[
 \|f_k\|_2\le C_r\epsilon D,\qquad
 \|B\|_2\|s_k\|_2\le C_a\epsilon D,
\]

then \(\zeta_k=\|r_k\|_2/D\) satisfies the requested recurrence

\[
 \zeta_{k+1}\le\rho\zeta_k+C\epsilon,qquad
 C=(1+\rho)C_r+C_a, \tag{9}
\]

and therefore

\[
 \zeta_k\le\rho^k\zeta_0+\frac{C}{1-\rho}\epsilon. \tag{10}
\]

This is a genuine positive theorem, but its contraction hypothesis does not
follow from \(\kappa_2(A)\) and \(\kappa_2(B)\); Theorems 1--2 prove that it
cannot.

## Limitations and algorithmic repair

The result targets the literal split SM-IR algorithm and its reuse of
\(\widehat z,\widehat\beta\).  It does not disprove variants that rescale or
refactor the update, form \(B\), recompute a correction operator, use
compensated/higher precision, or fall back to a stable direct solve.  Merely
testing that the denominator is nonzero or not small does not fix this
example: both denominators are large.  A repaired theorem must specify
exception handling and stopping and control the full corrector contraction,
including scale/cancellation and same-precision residual representation
growth.
