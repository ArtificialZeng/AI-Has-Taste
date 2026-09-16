# Precise problem reading

## Frozen object and quantifiers

Let

\[
f_1(x)=x/2,\qquad f_2(x)=(x+2)/4=x/4+1/2,
\]

and let

\[
p=2^{-\log_2\varphi}=\varphi^{-1}=\frac{\sqrt5-1}{2},
\qquad \varphi=\frac{1+\sqrt5}{2}.
\]

Thus `0 < p < 1` and `1-p=p^2`.  The symbol
\(\mu=\mu^p_{1/2,1/4}\) means the unique Borel probability measure on
\(\mathbb R\) satisfying, for every Borel set \(E\subseteq\mathbb R\),

\[
\mu(E)=p\,\mu(f_1^{-1}E)+p^2\,\mu(f_2^{-1}E).
\]

Its support is the compact attractor of \(\{f_1,f_2\}\), contained in
\([0,2/3]\).  Define for every real \(\xi\)

\[
F(\xi)=\widehat\mu(\xi)=\int_{\mathbb R}e^{-2\pi i\xi x}\,d\mu(x).
\]

The frozen assertion is the closed-interval universal statement

\[
\boxed{\ \forall\xi\in\mathbb R,\quad |\xi|\le 10^7
       \Longrightarrow F(\xi)\ne0.\ }
\]

Its negation requires one real \(\xi_0\in[-10^7,10^7]\), endpoints
included, for which both \(\Re F(\xi_0)=0\) and \(\Im F(\xi_0)=0\).
Numerical smallness or a sampled sign pattern is neither statement.

## Equivalent reductions and scope

The invariance equation gives, for every real \(\xi\),

\[
F(\xi)=pF(\xi/2)+p^2e^{-\pi i\xi}F(\xi/4),\qquad F(0)=1.
\]

Because \(\mu\) is real and positive,
\(F(-\xi)=\overline{F(\xi)}\).  It is therefore enough to settle the
nonnegative half.  Mao--Wu Proposition 3.3 already proves zero-freeness on
\([-1.08,1.08]\), so the unresolved certification range is
\([1.08,10^7]\) (with the shared endpoint already covered by the proposition).

The claim is only about this finite real interval.  It does not assert that
\(F\) is zero-free on all of \(\mathbb R\), and by itself it does not settle
spectrality.  A computer-assisted proof must cover every real point, use
outward/directed rounding, prove its terminal recursion or truncation error,
and ship a deterministic independently replayable coverage certificate.

## Source status and proposed contribution

The immutable input has SHA-256
`1d7fe134dedec418a06b3155598b70295df9a6fe07b651280df0e66ab0fadee3`.
Live inspection on 2026-09-08 confirmed arXiv:2609.04701v1 as the primary
source.  Its Section 4 reports a double-precision scan through \(10^7\), while
its final Remark expressly says this is not a formal proof and leaves rigorous
verification for future work.  The source status of this precise upgrade is
therefore **open-supported**, not known.

Nearest prior result X: Mao--Wu Proposition 3.3 on \([-1.08,1.08]\).
Proposed delta Y: a complete rigorous certificate on
\([1.08,10^7]\).  Verification route Z: a finite adaptive rational interval
cover whose leaves use Arb complex balls or Taylor models for the matrix
recursion, a uniform analytic terminal-scale bound, and explicit nonzero
enclosures; symmetry supplies the negative half.  The available python-flint
Arb backend passed a 256-bit local feasibility probe at both deepest reported
valleys, but full coverage remains entirely unproved.

