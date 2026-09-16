# Source statement — win-00048-p04

## Original lead and exact frozen question

Let \(G=K_5=(V,E)\), fix an origin \(o\in V\), and put
\(B=V\setminus\{o\}\). For \(p\in(0,1)\), let
\(\pi=(\pi_e)_{e\in E}\in\{0,1\}^{E}\) have independent Bernoulli-\(p\)
coordinates. The underlying probability space may contain auxiliary randomness
in addition to \(\pi\).

An event \(A\) is *increasing with respect to the percolation configuration* if

\[
\omega\longmapsto \mathbb P(A\mid \pi=\omega)
\]

is coordinatewise increasing on \(\{0,1\}^{E}\). For vertices \(u,v\), write
\(\{u\leftrightarrow v\}\) for open-path connectivity and
\(\{o\leftrightarrow B\}=\bigcup_{b\in B}\{o\leftrightarrow b\}\).

Prove or disprove that for every \(p\in(0,1)\), every
\(\varepsilon\in(0,1/4]\), and every family \((E_b)_{b\in B}\) of such
increasing events satisfying

\[
\mathbb P(E_b)\geq1-\varepsilon\qquad\text{for every }b\in B,
\]

one has

\[
\boxed{
\mathbb P\!\left[
  \bigcup_{b\in B}\bigl(\{o\leftrightarrow b\}\cap E_b\bigr)
  \;\middle|\;o\leftrightarrow B
\right]
\geq 1-2\sqrt{\varepsilon}.}
\]

Since \(p>0\), the conditioning event has positive probability. Equivalently,
the boxed assertion is the unconditional inequality

\[
\mathbb P\!\left[
  \bigcup_{b\in B}\bigl(\{o\leftrightarrow b\}\cap E_b\bigr)
\right]
\geq(1-2\sqrt\varepsilon)\,\mathbb P[o\leftrightarrow B].
\]

The upper restriction \(\varepsilon\leq1/4\) keeps the displayed lower bound
nonnegative; it is part of this frozen refinement.

## Primary source and exact locator

Lucas Flammant, *A conjecture implying \(\theta(p_c)=0\) for Bernoulli bond
percolation on \(\mathbb Z^d\)*, arXiv:2609.03492v1, 3 September 2026.

- Section 2 and Definition 2.1 (PDF around p.3) define the finite loopless
  multigraph model, permit auxiliary randomness, and define increasing events
  through their conditional kernels.
- Conjecture 2.2 and equation (2.1) (PDF around pp.3--4) assert the same form of
  inequality on every finite graph for some universal
  \(\varphi(\varepsilon)\to1\), without specifying
  \(1-2\sqrt\varepsilon\) in the nonplanar case.
- Theorem 2.3 (PDF around p.4) proves the explicit value
  \(\varphi(\varepsilon)=1-2\sqrt\varepsilon\) when \(G\) has a planar
  embedding with \(\{o\}\cup B\) on the boundary of the outer face.
- Theorem 2.4 claims that Conjecture 2.2 implies
  \(\theta(p_c)=0\) on \(\mathbb Z^d\), but the source explicitly states that
  its proof is absent from v1 and will be supplied in a forthcoming revision.
  **Theorem 2.4 must not be used as a proved dependency or as evidence for this
  finite \(K_5\) claim.**

Official primary endpoints:

- abstract: `https://arxiv.org/abs/2609.03492`
- HTML: `https://arxiv.org/html/2609.03492`
- PDF: `https://arxiv.org/pdf/2609.03492`

## Nearest result and proposed novelty delta

Theorem 2.3 is the nearest result, but it is inapplicable because \(K_5\) is
nonplanar. Conjecture 2.2 supports only the existence of an unspecified universal
function tending to one; it does not assert that the planar constant
\(1-2\sqrt\varepsilon\) works for \(K_5\).

The proposed delta is therefore a newly formulated sharp finite test: extend
the paper's explicit planar modulus to the smallest canonical nonplanar graph,
with the origin and all four remaining vertices fixed as the boundary. A
counterexample would refute this explicit-modulus refinement but would not by
itself refute Conjecture 2.2 with a weaker function \(\varphi\).

## Cheapest decisive test

There are \(2^{10}=1024\) percolation configurations. To preserve arbitrary
dependence among the four auxiliary events, use variables

\[
Q_{\omega}(S)=\mathbb P\bigl(\{b\in B:E_b\text{ occurs}\}=S\mid
\pi=\omega\bigr),\qquad S\subseteq B,
\]

not merely the four marginal kernels. Impose
\(Q_{\omega}(S)\ge0\), \(\sum_SQ_{\omega}(S)=1\), the four marginal
monotonicity systems

\[
q_b(\omega):=\sum_{S\ni b}Q_{\omega}(S)
\leq q_b(\omega')\quad(\omega\leq\omega'),
\]

and the marginal-probability constraints
\(\sum_\omega \mathbb P_p(\omega)q_b(\omega)\ge1-\varepsilon\).
For fixed rational \(p,\varepsilon\), minimizing the success probability is an
exact rational LP with \(1024\cdot16\) joint-kernel variables before symmetry
reduction. Any joint kernel is realizable using auxiliary randomness, so this
formulation loses no cases.

Test rational \((p,\varepsilon)\) values first, with vertex-stabilizer orbit
reduction and an unreduced replay. If no counterexample appears, seek a
parametric LP dual or a certified semialgebraic partition in \(p\) and
\(t=\sqrt\varepsilon\), \(0<t\le1/2\).

## Fast falsification

A decisive counterexample consists of rational \(p\in(0,1)\), rational
\(t\in(0,1/2]\) with \(\varepsilon=t^2\), and rational tables
\(Q_\omega(S)\) satisfying all normalization, marginal monotonicity, and
probability constraints, for which exact arithmetic gives

\[
\mathbb P\!\left[
\bigcup_{b\in B}(\{o\leftrightarrow b\}\cap E_b)
\right]
<(1-2t)\mathbb P[o\leftrightarrow B].
\]

Reporting only marginal kernels \(q_b\), without a compatible joint
distribution for the events, is not a valid counterexample certificate.

## Reproducible certificate requirement

A disproof certificate must serialize \(p,t\), all nonzero rational
\(Q_\omega(S)\), the ten-edge ordering, and exact checks of normalization,
monotonicity, event marginals, connectivity, and the strict final inequality.
An independent verifier should reconstruct all 1024 configurations.

A proof certificate must cover the full real parameter rectangle
\(0<p<1\), \(0<t\le1/2\), not just a grid of samples. Acceptable forms include
a finite exact parameter-cell decomposition with rational/algebraic LP duals,
or a human proof whose inequalities are independently checked symbolically.
Floating-point optimization, solver `OPTIMAL` lines without dual witnesses, or
failure to find a counterexample are not proofs.

## PDF integrity, source risk, and fallback provenance

The official arXiv v1 PDF bytes fetched from `https://arxiv.org/pdf/2609.03492`
on 2026-09-06 have SHA-256

`0f9e0d2d3b6546221a0025ded05dcb46a39346c980f7d940faaadc83a969949a`.

This intake directory does not contain a local PDF copy. If a later worker must
fall back from HTML, it should retrieve the official versioned record
`arXiv:2609.03492v1`, verify the above hash before relying on page locators, and
record any revised arXiv version separately. In particular, a later version
adding the promised proof of Theorem 2.4 must not be retroactively attributed to
v1, and it does not automatically settle the explicit \(K_5\) refinement.

