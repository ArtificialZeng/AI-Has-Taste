# Precise problem reading

## Frozen object and probability space

Let
\[
B=\{x\in\mathbb R^3:|x|<1\},\qquad \Gamma=\partial B,
\]
and let \((X_t)_{t\geq0}\) be reflected Brownian motion in the closed unit
ball with diffusion coefficient \(D=1\) (hence interior generator \(\Delta\)).
The initial point \(X_0\) is independent of all other randomness and has
normalized Lebesgue measure on \(B\), i.e. density \(3/(4\pi)\).

Use the boundary-local-time normalization of Ye, arXiv:2609.05247v1.  In
the present normalization it is
\[
 \ell_t=\lim_{\varepsilon\downarrow0}\frac1\varepsilon
 \int_0^t {\bf1}_{\Gamma^{(\varepsilon)}}(X_s)\,ds,
\]
in the sense used in that paper, where \(\Gamma^{(\varepsilon)}\) is the
interior boundary layer of thickness \(\varepsilon\).  (The paper's general
formula has the factor \(D/\varepsilon\); here \(D=1\).)

For fixed \(p,q>0\), let
\[
 \delta\sim\operatorname{Exp}(p),\qquad
 \widehat\ell\sim\operatorname{Exp}(q),
\]
so that \(\Pr(\delta>t)=e^{-pt}\) and
\(\Pr(\widehat\ell>u)=e^{-qu}\).  The two thresholds are mutually
independent and independent of the entire reflected path.  Define
\[
 \tau=\inf\{t>0:\ell_t>\widehat\ell\},\qquad
 T=\min\{\delta,\tau\},\qquad L=\ell_T.
\]
By continuity of \(\ell_t\) and the continuous independent thresholds,
the tie event has probability zero and, as in the source,
\(L=\min\{\ell_\delta,\widehat\ell\}\) almost surely.  Every expectation,
variance, and covariance below averages jointly over \(X_0\), the reflected
path, and both thresholds.

## Quantified assertion and alternatives

The frozen assertion is
\[
 \boxed{\quad \forall(p,q)\in(0,\infty)^2,
 \quad \operatorname{Cov}_{p,q}(T,L)>0.\quad}
\]
The allowed resolution is symmetric:

1. prove this strict inequality on the entire open positive quadrant; or
2. give an exact (not floating-point) pair \((p,q)\in(0,\infty)^2\) with
   nonpositive covariance and classify the complete zero set
   \(\{(p,q)>0:\operatorname{Cov}_{p,q}(T,L)=0\}\).

Axes and limiting points \(p=0\), \(q=0\), or infinity are not themselves
in the quantified domain.  They may be used only for asymptotic arguments.
A finite heat map, numerical sampling, or a bounded-box interval check cannot
resolve the assertion.

## Exact Appendix-F reduction to be audited

For the uniform initial distribution (the symbol \(\circ\) in the paper
means volume-uniform in the ball, not a boundary starting point), Appendix F,
equations (F4)--(F5), gives the Pearson correlation
\[
C(p,q\mid\circ)=\sqrt{\frac38}\,
 \frac{\xi_1(p)+q\xi_2(p)}{
 \sqrt{\xi_3(p)\xi_4(p)
 [\xi_5(p)+q\xi_6(p)+q^2\xi_7(p)]}},
\]
where
\[
\begin{aligned}
\xi_1(p)&=4p\xi_3(p)^2,\\
\xi_2(p)&=2p(p+3)-\sqrt p\,(p+12)\sinh(2\sqrt p)
 +6(p+1)\cosh(2\sqrt p)-6,\\
\xi_3(p)&=\sqrt p\cosh(\sqrt p)-\sinh(\sqrt p),\\
\xi_4(p)&=(2p+3)\sinh(\sqrt p)-3\sqrt p\cosh(\sqrt p),\\
\xi_5(p)&=2p^2\xi_3(p)^2,\\
\xi_6(p)&=2p\!\left[-2p+(p+6)\sqrt p\sinh(2\sqrt p)
 -(4p+3)\cosh(2\sqrt p)+3\right],\\
\xi_7(p)&=-p(7p+15)-3(p-6)\sqrt p\sinh(2\sqrt p)\\
&\qquad+((p-3)p-9)\cosh(2\sqrt p)+9.
\end{aligned}
\]
Since
\(C=\operatorname{Cov}(T,L)/\sqrt{\operatorname{Var}(T)
\operatorname{Var}(L)}\), sign equivalence requires verification that both
variances (equivalently, the displayed radical after the algebraic
simplification) are finite and strictly positive throughout the open
quadrant.  Subject to that audit, the sign target is exactly
\[
N(p,q)=\xi_1(p)+q\xi_2(p).
\]

An exact tractability lead is obtained by setting \(x=\sqrt p\).  Direct
Taylor-coefficient collection in (F5b) gives
\[
 \xi_2(x^2)=-\sum_{n=5}^{\infty}
 \frac{2^{2n-3}(2n-1)(2n-6)(2n-8)}{(2n)!}\,x^{2n},
\]
so the transcription predicts \(\xi_2(p)<0\) for every \(p>0\).  Also
\(\xi_3(x^2)=x\cosh x-\sinh x>0\), because its derivative is
\(x\sinh x>0\), and hence \(\xi_1(p)>0\).  This is a strong counterexample
lead: after auditing (F4) and its denominator, the numerator would have the
unique zero
\[
 q_0(p)=-\frac{\xi_1(p)}{\xi_2(p)}>0
\]
on every vertical line \(p>0\), with the opposite signs on the two sides.
This triage observation is not yet recorded as a resolution because the
source formula and denominator have not received an independent derivation.

## Nearest prior result and contribution target

The nearest prior result is Yilin Ye, *Diffusion under competing bulk and
surface stopping mechanisms*, arXiv:2609.05247v1 (submitted 2026-09-04),
especially equations (D8)--(D9), (57), and (F4)--(F5), and Figure 8.  It
derives the closed formula and reports positivity only over its explored
parameter range; it does not give a full-quadrant sign proof.  The local PDF
was checked against the SHA-256 frozen in `source.md`.  The arXiv record was
at <https://arxiv.org/abs/2609.05247> and was inspected on 2026-09-07.  No
claim of established open-problem status or novelty is made here; this is
presently a new question with literature status otherwise unverified.

Target delta: independently validate the Appendix-F reduction and then give
an exact global sign/zero-set classification (or identify and correct an
algebraic transcription/derivation error).  The first decisive test is a
symbolic re-derivation of covariance and both variances from equations (57)
and (D8), followed by exact positivity checks for every denominator factor.
