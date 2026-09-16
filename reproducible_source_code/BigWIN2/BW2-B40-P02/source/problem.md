# Precise problem interpretation

## Frozen source and status

The immutable statement is in `source.md`. Its primary source is Rafael S.
González D'León and Michelle L. Wachs, *Weighted bond posets and a new
chromatic symmetric function*, arXiv:2608.08692v1 (2026), especially equations
(7.1), Theorem 7.2, and Conjecture 7.3:
<https://arxiv.org/html/2608.08692v1>. The source was inspected on 2026-09-06.
It states Conjecture 7.3 for every graph and reports computational verification
for all connected graphs on at most seven vertices. Searches on 2026-09-06 for
the exact conjecture and its promised follow-up found no primary paper settling
the eight-vertex layer. This supports the label **open-supported**, but is not a
claim of priority or proof that no later result exists.

## Definitions

All symmetric functions are in the usual ring of symmetric functions over the
integers in countably many variables \(\mathbf{x}=(x_1,x_2,\ldots)\).

Let \(G=(V,E)\) be a finite simple graph. A bond partition of \(G\) is a set
partition \(\pi=\{B_1,\ldots,B_k\}\) of \(V\) such that every induced graph
\(G|_{B_i}\) is connected. The bond lattice is denoted \(\Pi_G\).

A weak composition \(\nu\) of \(m\) is a finitely supported sequence of
nonnegative integers with sum \(m\). An infinitely multiweighted bond
partition is
\[
  \boldsymbol\pi=\{B_1^{\nu_1},\ldots,B_k^{\nu_k}\},
  \qquad \nu_i\models |B_i|-1,
\]
whose underlying partition belongs to \(\Pi_G\). These form the poset
\(\Pi_G^\infty\): refinement may merge blocks, and when blocks with weights
\(\mu_{i_1},\ldots,\mu_{i_\ell}\) merge into a block of weight \(\nu\), one
requires \(\nu\) to dominate their coordinatewise sum. Equivalently, a cover
merges two blocks and adds one standard basis vector to the sum of their
weights. The minimum \(\hat 0\) is the singleton partition with zero weights.
For \(\boldsymbol\pi\), put
\(w(\boldsymbol\pi)=\sum_i\nu_i\) and
\(\mathbf{x}^{w}=\prod_j x_j^{w(j)}\). With \(\mu\) the poset Möbius function,
define
\[
  \Psi_G(\mathbf{x})=
  \sum_{\boldsymbol\pi\in\Pi_G^\infty}
  \mu_{\Pi_G^\infty}(\hat0,\boldsymbol\pi)
  \mathbf{x}^{w(\boldsymbol\pi)}.
\]
Equivalently, as in source equation (7.1),
\(\Psi_G=\sum_{\pi\in\Pi_G}M_{G|_\pi}\), where \(M_H\) is the Möbius
symmetric function and \(G|_\pi\) has components \(G|_B\), \(B\in\pi\).

Write \(F_{G,d}=\Psi_G|_{\deg d}\). Source Theorem 7.2 gives the useful exact
formula
\[
  F_{G,d}=\sum_{\substack{\pi\in\Pi_G\\|\pi|=|V|-d}}M_{G|_\pi}.
\]
A homogeneous symmetric function \(F\) of degree \(m\) is Schur-positive when
its unique expansion \(F=\sum_{\lambda\vdash m}c_\lambda s_\lambda\) has
\(c_\lambda\in\mathbb Z_{\ge0}\) for every partition \(\lambda\vdash m\).

## Quantified claim to decide

For every isomorphism class of connected simple graph \(G\) with
\(|V(G)|=8\), and every integer \(d\ge1\), determine whether
\[
  L_{G,d}:=F_{G,d}^2-F_{G,d-1}F_{G,d+1}
\]
is Schur-positive. Because a connected eight-vertex graph has
\(F_{G,d}=0\) outside \(0\le d\le7\), only \(d=1,\ldots,7\) can be nonzero;
all \(d\ge8\) are automatic zero cases. A universal positive result must
certify every graph class and all seven degrees. A negative result must give a
graph (preferably canonically encoded, e.g. graph6), a degree \(d\), a
partition \(\lambda\vdash2d\), and the exact negative integer coefficient
\([s_\lambda]L_{G,d}\).

Graph labels are irrelevant, so one representative per isomorphism class is
enough. Chordal representatives must be identified in the output. Source
Theorem 7.2 proves that each \((-1)^dF_{G,d}\) is elementary-positive for
chordal \(G\), but it does **not** assert that
\(F_{G,d}^2-F_{G,d-1}F_{G,d+1}\) is Schur-positive; thus chordal graphs are a
separate stratum, not cases already settled by that theorem.

## Triage target

Nearest prior result: the source's complete connected-graph computation through
seven vertices. Proposed delta: the complete connected eight-vertex layer,
with chordal/nonchordal results separated. Verification route: canonical
enumeration of graph representatives; exact integer computation of all
\(M_H\), \(F_{G,d}\), and Schur coefficients; replay from graph encodings; and
an independent recomputation of any negative certificate (or aggregate
coverage certificate) using a second formula or implementation.
