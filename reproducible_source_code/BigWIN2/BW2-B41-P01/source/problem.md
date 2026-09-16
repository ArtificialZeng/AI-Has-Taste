# Precise problem reading

## Frozen claim and scope

All graphs below are finite, simple, undirected, and connected. Quantification is

\[
\forall (m,\ell)\in\mathbb Z^2\quad
\bigl(m\ge 2,\ \ell\ge 1,\ m\le 2\ell+3\bigr)
\Longrightarrow J_{m,\ell}\text{ is resistance-positive (RP)}.
\]

The alternative requested by the source is to refute this universal assertion by one exact pair
\((m,\ell)\) in that range and an exact certificate that the corresponding graph is not RP. The
word `l` in `source.md` is read as the integer parameter \(\ell\), not the numeral one.

## Graph definition

Let
\[
B=\{b_1,\dots,b_m\},\qquad X=\{x_1,\dots,x_m\},\qquad U=\{u_1,\dots,u_\ell\}.
\]
The graph \(H_m\) has vertex set \(\{a\}\cup B\cup X\) and edge set
\[
E(H_m)=\{b_i b_j:1\le i<j\le m\}\cup
        \{a x_i,x_i b_i:1\le i\le m\}.
\]
Thus each edge \(ab_i\) of the original \(K_{m+1}\) is deleted and replaced by the two-edge path
\(a x_i b_i\); the edges within \(B\) remain. The complete join
\[
J_{m,\ell}=K_\ell\vee H_m
\]
has vertex set \(U\cup V(H_m)\), all edges of \(H_m\), all edges within \(U\), and every edge
between \(U\) and \(V(H_m)\). In particular, \(|V(J_{m,\ell})|=2m+\ell+1\).

## Resistance terminology

For a connected graph \(G=(V,E)\), assign every edge a positive conductance \(c_e>0\). If
\(\omega_e(c)\) is the effective resistance between the endpoints of \(e\), let
\(r_e(c)=c_e\omega_e(c)\) be its relative resistance and define
\[
p_v(c)=1-\frac12\sum_{e\ni v}r_e(c).
\]
The graph is RP if there exists one choice \(c\in\mathbb R_{>0}^{E}\) such that
\(p_v(c)>0\) for every \(v\in V\). It is resistance-nonnegative (RN) when all these inequalities
are weak. Hence RP implies RN using the same conductances.

Theorem 3 of the cited source gives the equivalent proof target: RP holds iff there is a
probability distribution assigning positive probability to every spanning tree \(T\) such that
\(\mathbb E[\deg_T(v)]<2\) for every vertex. Equivalently, the vector of tree-edge marginals lies
in the relative interior of the spanning-tree polytope and has incident sum strictly below two at
every vertex. An exact non-RP certificate may instead be a nonzero \(\lambda:V\to\mathbb Q_{\ge0}\)
with
\[
\sum_v\lambda(v)\deg_T(v)\ge 2\sum_v\lambda(v)
\]
for every spanning tree \(T\), together with an exact proof of that universal inequality (Lemma 14
of the source), or another exact dual infeasibility certificate.

## Known boundary and proposed contribution

Wang's Proposition 16 proves that \(J_{m,\ell}\) is not RN, hence not RP, whenever
\(m\ge2\ell+4\). Proposition 15 gives \(\tau(J_{m,\ell})=1+\ell/m\). Therefore proving the frozen
claim would establish the exact RP threshold
\[
J_{m,\ell}\text{ is RP}\quad\Longleftrightarrow\quad m\le2\ell+3
\]
over \(m\ge2,\ell\ge1\). The nearest direct prior result is the negative half just cited; the
proposed delta is the full positive half. A natural verifier is an exact, symmetry-reduced feasible
point in the relative interior of the spanning-tree polytope with all vertex incident sums below
two; failure should return an exact dual certificate.

## Literature/status triage

- Zhiyu Wang, *Toughness Bounds for Fractional Hamiltonicity and Resistance Positivity*,
  arXiv:2609.03412v1, retrieved 2026-09-06:
  https://arxiv.org/abs/2609.03412v1. Inspected Theorem 3 on PDF page 3 and Propositions 15--16
  on PDF pages 11--12. These establish the spanning-tree characterization and the complementary
  non-RN range, but do not settle the frozen positive range.
- G. Agrahari et al., *On some structural properties of graphs with non-negative resistance
  curvature*, arXiv:2607.13169v2, retrieved 2026-09-06:
  https://arxiv.org/abs/2607.13169v2. Inspected Theorems 1--2 and the spanning-tree/TDM-polytope
  formulation; it supplies the closest general recognition framework, not this threshold.
- Exact-phrase and equivalent-language web searches on 2026-09-06 found no separate source
  proving or disproving the frozen assertion. This is only a limited literature screen, not a
  priority claim. Because Wang's preprint does not explicitly pose the positive half as open, the
  source status is **new-question / status-uncertain**, not verified open.

