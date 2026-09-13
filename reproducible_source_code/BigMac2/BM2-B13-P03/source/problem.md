# Precise problem reading

Provenance: `bigMac-00013-p03-triage-29e9cf5f50a4` (triage, 2026-09-07).
The immutable statement is `source.md` (SHA-256
`e3d10ece2fc71dccdf70f98eef6b53150b533f21e138b19f7310d1ec861d52b5`).
Nothing below changes its quantifiers or contribution boundary.

## Definitions and canonical representative

Write
\[
 \varphi(x)=(2\pi)^{-1/2}e^{-x^2/2},\qquad
 \Phi(x)=\int_{-\infty}^x\varphi(s)\,ds,\qquad
 \overline\Phi=1-\Phi,
\]
so that \(d\gamma _1(x)=\varphi(x)\,dx\). For each real parameter
\(L>0\), define
\[
 Z_L=\int_{\mathbb R}e^{L|t|}\,d\gamma _1(t)
     =2e^{L^2/2}\Phi(L)
\]
and the probability measure with everywhere-positive continuous density
\[
 q_L(t)=\frac{e^{L|t|}\varphi(t)}{Z_L},\qquad d\nu_L(t)=q_L(t)\,dt.
\]
Let \(F_L(t)=\nu_L(( -\infty,t])\). The map in the problem is the
canonical everywhere-defined monotone rearrangement
\[
 T_L(x)=F_L^{-1}(\Phi(x)),\qquad x\in\mathbb R.
\]
It is the one-dimensional quadratic-cost Brenier map (unique
\(\gamma_1\)-almost everywhere). Positivity and continuity of both densities
give a strictly increasing \(C^1\) representative. Symmetry gives
\(T_L(0)=0\), \(T_L(-x)=-T_L(x)\), and
\[
 T_L'(x)=\frac{\varphi(x)}{q_L(T_L(x))}
 =Z_L\exp\!\left(\frac{T_L(x)^2-x^2}{2}-L|T_L(x)|\right),
 \qquad T_L'(0)=Z_L.
\]

For this representative,
\[
 \operatorname{Lip}(T_L):=\sup_{x\ne y}
 \frac{|T_L(x)-T_L(y)|}{|x-y|}
 =\sup_{x\in\mathbb R}T_L'(x)
\]
as an equality of extended real numbers. The phrase “essential derivative
maximizers” is read as the maximizer set of the continuous derivative,
\[
 \mathcal M_L:=\{x\in\mathbb R:T_L'(x)
       =\|T_L'\|_{L^\infty(\mathbb R)}\}.
\]
Thus isolated maximizers are retained; the request is not interpreted as
asking only for positive-measure level sets.

## Frozen quantified task

Decide the single universal assertion
\[
 \boxed{\quad \forall L>0,\qquad
 \operatorname{Lip}(T_L)=T_L'(0)=Z_L
 =2e^{L^2/2}\Phi(L).\quad}
\]
Equivalently, prove \(T_L'(x)\le Z_L\) for every \(L>0\) and every
\(x\in\mathbb R\), or disprove the universal assertion by an exact value of
\(L>0\) and an exact/certified violation. If the equality is true, determine
\(\mathcal M_L\) for every \(L>0\). The excluded boundary value \(L=0\) is a
useful check only: then \(T_0(x)=x\), \(Z_0=1\), and every point maximizes the
derivative.

The requested sharp logarithmic consequence is read as the exact identity
\[
 \log\operatorname{Lip}(T_L)=\frac{L^2}{2}+\log 2+\log\Phi(L)
\]
and hence, at minimum,
\[
 \log\operatorname{Lip}(T_L)=\frac{L^2}{2}+\log 2+o(1)
 \qquad(L\to\infty).
\]
A sharpened form obtainable from the Mills expansion is
\[
 \log\operatorname{Lip}(T_L)
 =\frac{L^2}{2}+\log 2-
   \frac{\varphi(L)}{L}\left(1-\frac1{L^2}+O(L^{-4})\right).
\]
These asymptotics are conditional only on the asserted global Lipschitz
equality; the displayed expansion of \(Z_L\) itself is elementary.

## Exact reduction for the first test

For \(x\ge0\), put \(y=T_L(x)-L\). Completing the square in the target
density gives the exact tail and derivative identities
\[
 \overline\Phi(y)=2\Phi(L)\,\overline\Phi(x),\qquad
 T_L'(x)=2\Phi(L)\frac{\varphi(x)}{\varphi(y)}.
\]
Consequently, the proposed equality reduces on the positive half-line to
the elementary inequality
\[
 y^2-x^2\le L^2,
\]
with equality classification, followed by reflection symmetry. This is an
exact analytic reduction, not numerical evidence and not yet recorded here
as a proof of the global claim.

## Nearest inspected result and contribution delta

The nearest result is Maja Gwóźdź, *Caffarelli Estimates under Lipschitz
Perturbations*, arXiv:2609.04052v1 (2026), Theorem 1.1 and Remark 5.7,
<https://arxiv.org/abs/2609.04052v1>, inspected in the arXiv HTML on
2026-09-07. Theorem 1.1 supplies a general global upper bound. Remark 5.7
defines this same \(\nu_L,T_L\), computes \(T_L'(0)=Z_L\), and concludes only
\(\operatorname{Lip}(T_L)\ge T_L'(0)\ge e^{L^2/2}\). It does not state the
global equality or classify its derivative maximizers.

Exact-assertion and equivalent-form web searches on 2026-09-07 identified no
additional primary source asserting the requested equality. That limited
search is not evidence of novelty or open status. The source status is
therefore **new-question / status-uncertain**, while the proposed delta is an
exact maximization of the explicit one-dimensional map. The verification
route is the preceding quantile-tail reduction and exact Gaussian
inequalities; floating-point maximization is outside the contribution gate.
