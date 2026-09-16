# Precise problem statement

## Graph and notation

Let \(C_3\) be the simple 3-cycle, and let
\[
G=C_3\square C_3.
\]
Use the concrete model \(V(G)=\mathbb Z_3^2\). Distinct vertices
\((i,j)\) and \((i',j')\) are adjacent exactly when either \(i=i'\) or
\(j=j'\). (For a coordinate of size three, every two distinct coordinate
values are adjacent in \(C_3\).) Thus \(G\) has 9 vertices, 18 edges, and is
4-regular. It is also the Hamming/rook graph \(H(2,3)=K_3\square K_3\),
equivalently the line graph of \(K_{3,3}\).

For a positive integer \(k\), a *proper total \(k\)-coloring* is a map
\[
f:V(G)\cup E(G)\longrightarrow [k]=\{1,\ldots,k\}
\]
(not required to be surjective) such that:

1. for every edge \(uv\), \(f(u)\ne f(v)\);
2. for every two distinct edges sharing an endpoint, their colors differ;
3. for every incident pair \(v,e\), \(f(v)\ne f(e)\).

For every vertex \(u\), define the **set** (not multiset)
\[
C_f(u)=\{f(u)\}\cup\{f(e):e\in E(G),\ e\text{ is incident with }u\}.
\]
The coloring is adjacent-vertex-distinguishing (AVD) when
\[
\forall uv\in E(G),\qquad C_f(u)\ne C_f(v).
\]
The requested number \(\chi''_a(G)\) is the least positive integer \(k\)
for which such a coloring exists. The frozen claim asks to determine this
integer exactly.

## Immediate normalization and bounds

At every vertex, its own color and its four incident-edge colors are pairwise
distinct, so \(|C_f(u)|=5\). Consequently \(k\ge 5\) for a proper total
coloring. If \(k=5\), then \(C_f(u)=[5]\) for every vertex, contradicting the
AVD condition on every edge. Hence
\[
\chi''_a(C_3\square C_3)\ge 6.
\]
This also excludes every \(k<6\), without needing separate searches for
\(k=1,\ldots,4\).

An exact finite solver found a concrete 6-color assignment during triage;
it is recorded in `evidence/triage-6-coloring.json` and checked by
`evidence/verify_coloring.py`. This is triage evidence, not yet an
independent mathematical review.

## Required resolution scope

A resolution must (i) give a reproducible, machine-checkable AVD total
coloring using the claimed optimum number of colors and (ii) prove or provide
an exact UNSAT certificate excluding all smaller palette sizes. For a
6-color upper bound, the preceding local argument supplies the mathematical
lower bound for all smaller sizes; a later research/referee pass must audit
both that argument and the explicit assignment independently.

## Literature/status triage (retrieved 2026-09-07)

- A. Banerjee, J. Geetha, and K. Somasundaram, *Adjacent vertex
  distinguishing total chromatic number of graph products*,
  arXiv:2609.03411v1, <https://arxiv.org/abs/2609.03411>. The definition is in
  Introduction, and the main-results list is in Section 1.2. The HTML text
  states the general lower bound \(\Delta+2\) when adjacent maximum-degree
  vertices exist and cites the AVD-TCC upper bound for 4-regular graphs, but
  it does not state the exact value for \(C_3\square C_3\). Its Cartesian
  product Theorem 3.1 assumes one factor is bipartite, so it does not apply
  directly here. The frozen source's author line omits Banerjee.
- S. Tian, P. Chen, Y. Shao, and Q. Wang, *Adjacent vertex distinguishing
  edge-colorings and total-colorings of the Cartesian product of graphs*,
  Numerical Algebra, Control and Optimization 4 (2014), 49--58,
  <https://doi.org/10.3934/naco.2014.4.49>. The publisher abstract says that
  exact values are obtained for Cartesian products of regular graphs, a
  description broad enough to flag a possible prior result for this graph.
  The theorem statement and hypotheses were not accessible in this bounded
  pass, so prior settlement is **not established**. Source status is therefore
  `status-uncertain`, not verified open.

Target contribution: nearest potentially exact prior result is Tian--Chen--
Shao--Wang (2014); proposed delta is an independently checkable exact
classification of this nine-vertex instance; verification route is direct
checking of the 6-color witness plus the local five-color impossibility
argument, followed by inspection of the 2014 theorem to classify novelty.
