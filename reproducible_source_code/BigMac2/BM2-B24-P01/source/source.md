# Immutable source — bigMac-00024-p01

## Frozen source statement

Let
\[
p_{18}(z)=z(z^{18}-1)
\]
and let its Chebyshev map be
\[
C_{18}(z)=
\frac{z^{19}\left(12654z^{36}-684z^{18}-306\right)}
{2(19z^{18}-1)^3}.
\]
Prove or disprove that `C_18` is convergent in the root-finding sense: every connected component of its Fatou set is contained in the basin of attraction of one of the roots in `\{0\}\cup\{z:z^{18}=1\}`.

Equivalently, using the source's terminology, prove
\[
\forall U\in\pi_0(\mathcal F(C_{18}))\ \exists r\in\{0\}\cup\mu_{18}\
\ \forall z\in U,\qquad \lim_{m\to\infty}C_{18}^{m}(z)=r.
\]

No statement for another even value of `n`, no classification of Julia topology, and no claim about numerical convergence speed is part of the frozen target.

## Source and exact proposed delta

Tarakanta Nayak and Pooja Phogat, *Chebyshev's method applied to polynomials with rotational symmetry*, arXiv:2609.02884v1, defines convergence and `C_n` on PDF pp. 3 and 6, proves convergence for `n<=16` or odd `n` in Theorem D, and asks on PDF p. 27 whether `C_n` is convergent for every even `n>=18`. The source's p. 28 table gives only floating-point evidence at `n=18`.

The proposed contribution is a rigorous resolution of the first omitted layer `n=18`, preferably by an exact certificate for the second iterate of every free critical point followed by a complete complex-dynamical exclusion of every non-root Fatou component.

Fixed local evidence: `batches/literature/bigMac-24/2609.02884v1.pdf`, SHA-256 `afe10caa52713e3a0bff4d5830751e7bebd151d666b1ad28dc98e6cab419f569`.

## Cheapest decisive route to audit

On an odd critical line, use the source's Equation (14)
\[
Q_{18}(x)=\frac{x^{19}(12654x^{36}+684x^{18}-306)}{2(19x^{18}+1)^3}.
\]
For `t=x^{18}` put
\[
q(t)=\frac{Q_{18}(x)}x
=\frac{t(12654t^2+684t-306)}{2(19t+1)^3},
\qquad t_{j+1}=t_jq(t_j)^{18}.
\]
The positive critical-line coordinate has
\[
t_0=\frac{17}{703},\qquad q(t_0)=-\frac{10693}{9747}.
\]
Independently verify, using exact integer arithmetic rather than decimals,
\[
\frac{16}{125}<t_1<\frac{13}{100},\qquad
-\frac1{50}<q(t_1)<0,\qquad t_2<\frac1{100}.
\]
For the source's smallest positive solution `x_*` of `Q_18(x_*)=-x_*`, set `t_*=x_*^{18}` and audit the polynomial
\[
13186t^3+1425t^2-96t+1=0.
\]
An exact Sturm or monotonicity argument should prove `t_*>1/100`. Then verify every logical bridge from `t_2<t_*` to membership in the full attracting basin `A_0`, rotational propagation to every free critical point, and the final exclusion of attracting, parabolic, Siegel, Herman, and wandering components. The source's assertions are inputs to check, not permission to skip this closure.

## Scope and honesty

The source's numerical table is not a proof. A rational inequality certificate without the final Fatou-component argument is only a partial result. If an exact step fails, record the precise failure rather than weakening “convergent” to a finite-orbit observation.

