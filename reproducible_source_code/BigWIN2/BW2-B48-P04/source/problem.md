# Precise problem reading

Provenance: triage job win-00048-p04-triage-38ec7280bd85 (2026-09-06).
The immutable input is source.md, whose SHA-256 at triage was
77497af47aed92acbca8315b367c3e806160368e352ed35e8b6bd9de2247fc7c.

## Objects and quantifiers

Label

\[
V=\{o,b_1,b_2,b_3,b_4\},\qquad B=\{b_1,b_2,b_3,b_4\},
\]

and let \(E(K_5)\) be the ten unordered vertex pairs. For every
\(p\in(0,1)\), let \(\pi\in\{0,1\}^{E(K_5)}\) have product Bernoulli-\(p\)
law

\[
\mu_p(\omega)=p^{|\omega|}(1-p)^{10-|\omega|}.
\]

The quantification is also over every probability space carrying this random
configuration together with arbitrary auxiliary randomness, every
\(\varepsilon\in(0,1/4]\), and every jointly defined family of events
\((E_b)_{b\in B}\) such that, writing

\[
q_b(\omega)=\mathbb P(E_b\mid\pi=\omega),
\]

one has, for every \(b\in B\),

\[
\omega\leq\omega'\Longrightarrow q_b(\omega)\leq q_b(\omega'),
\qquad
\sum_\omega\mu_p(\omega)q_b(\omega)\geq1-\varepsilon.
\]

Here \(\omega\leq\omega'\) is coordinatewise order. Because \(0<p<1\),
every configuration atom has positive probability, so each conditional kernel
is unambiguous. No independence is assumed among the events \(E_b\), nor
between their auxiliary randomness and \(\pi\).

For a configuration \(\omega\), let \(C_o(\omega)\subseteq B\) be the set of
vertices joined to \(o\) by an open path, and put
\(C=\{C_o(\pi)\ne\varnothing\}=\{o\leftrightarrow B\}\). Since every other
vertex is in \(B\), \(C\) is exactly the event that at least one of the four
edges incident to \(o\) is open. Consequently

\[
\mathbb P_p(C)=1-(1-p)^4>0.
\]

## Frozen assertion to prove or disprove

Under all of the quantifiers above, determine whether

\[
\mathbb P\!\left(\exists b\in C_o(\pi):E_b\text{ occurs}\mid C\right)
\geq 1-2\sqrt\varepsilon.
\]

Equivalently,

\[
\mathbb P\!\left(\bigcup_{b\in B}
  (\{o\leftrightarrow b\}\cap E_b)\right)
\geq(1-2\sqrt\varepsilon)\,[1-(1-p)^4].
\]

At \(\varepsilon=1/4\) the right side is zero, so that boundary is trivial;
the substantive range is \(0<\varepsilon<1/4\). The endpoints \(p=0,1\) are
not part of the frozen claim. Sampled parameters or a restricted class of
auxiliary events cannot prove the assertion.

## Lossless finite formulation

Let \(S=\{b\in B:E_b\text{ occurs}\}\) and define

\[
Q_\omega(S)=\mathbb P(S\text{ is the occurring set}\mid\pi=\omega)
\qquad(S\subseteq B).
\]

For each \(\omega\), these 16 numbers are nonnegative and sum to one. Their
marginals are

\[
q_b(\omega)=\sum_{S\ni b}Q_\omega(S).
\]

Only these marginals must be coordinatewise increasing; no joint stochastic
monotonicity is required of \(Q_\omega\). Conversely, every such table is
realizable using auxiliary randomness, so this representation loses no
allowed event families. Its success probability is

\[
\sum_{\omega}\mu_p(\omega)
 \sum_{S\subseteq B}Q_\omega(S)
 \mathbf 1\{S\cap C_o(\omega)\ne\varnothing\}.
\]

For fixed rational \(p\) and rational \(t=\sqrt\varepsilon\), counterexample
search is therefore a rational LP with \(1024\cdot16=16384\) variables. A
strict optimum below \((1-2t)[1-(1-p)^4]\), accompanied by the complete
rational joint table, is a disproof certificate at that parameter pair.
Marginal tables alone are not a certificate. A proof must instead cover the
whole real domain \(0<p<1,\ 0<t\leq1/2\).

## Source status, nearest result, and scope

The exact \(K_5\) assertion is a newly formulated finite refinement, not a
claim stated in the cited paper. The nearest primary result is Lucas Flammant,
“A conjecture implying \(\theta(p_c)=0\) for Bernoulli bond percolation on
\(\mathbb Z^d\),” arXiv:2609.03492v1 (submitted 2026-09-03):

- Definition 2.1 and Conjecture 2.2 give the same auxiliary-randomness model
  and conjecture some universal modulus \(\varphi(\varepsilon)\to1\) for all
  finite graphs.
- Theorem 2.3 proves \(\varphi(\varepsilon)=1-2\sqrt\varepsilon\) only for a
  planar embedding with \(\{o\}\cup B\) on the outer-face boundary. It does
  not apply to nonplanar \(K_5\).
- Theorem 2.4 is not an available dependency: v1 explicitly says its proof is
  omitted and promised for a later revision.

The official abstract and 18-page v1 PDF were inspected on 2026-09-06 at
<https://arxiv.org/abs/2609.03492> and
<https://arxiv.org/pdf/2609.03492>. The abstract page still listed only v1;
the PDF confirms Definition 2.1, Conjecture 2.2, Theorems 2.3--2.4, and the
omitted-proof warning on PDF pp. 2--3. Exact-phrase and equivalent-language
web searches on the same date found no primary source settling the explicit
\(K_5\) modulus. This limited screen supports only the label
new-question/status-uncertain, not a priority or open-status claim.

## Triage target

Nearest prior result \(X\): the planar explicit modulus in Theorem 2.3.
Proposed delta \(Y\): prove that modulus for \(K_5\), or give one exact
joint-kernel counterexample, which would refute only this refinement and not
the source's unspecified-modulus Conjecture 2.2. Verification route \(Z\):
exact rational LP search with an unreduced replay, followed, if no witness is
found, by a symmetry-reduced parametric dual or a rigorous human inequality.
