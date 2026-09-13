# Precise reading of DM05-02

## Frozen source and conventions

The original request is frozen in `source.md` (SHA-256
`0dcd3cbf037a1923284cfaaead3837a1dd6d1fa6853d2d5de2ed64cd83cb954d`).
It is interpreted for finite, simple, undirected graphs. All parameters below
are integers with
\[
m\ge 2,\qquad \ell\ge 1.
\]

Let
\[
B=\{b_1,\ldots,b_m\},\quad X=\{x_1,\ldots,x_m\},\quad
U=\{u_1,\ldots,u_\ell\},
\]
with these sets and the vertex `a` pairwise disjoint. The graph \(H_m\) has
vertex set \(\{a\}\cup B\cup X\) and edge set
\[
\binom B2\;\cup\;\{ax_i,x_ib_i:i\in[m]\}.
\]
Thus only the edges \(ab_i\) of the original \(K_{m+1}\) are subdivided, the
old edges \(ab_i\) are deleted, and there are no other edges incident with an
\(x_i\) in \(H_m\). The graph
\[
J_{m,\ell}=K_\ell\vee H_m
\]
has vertex set \(U\cup\{a\}\cup B\cup X\) and, in addition to the edges of
\(H_m\), contains every edge inside \(U\) and every edge from \(U\) to
\(V(H_m)\). It has order
\[
n_{m,\ell}=2m+\ell+1.
\]
No unlisted edges are present.

## Fractional Hamiltonicity and the cut LP

For a graph \(G=(V,E)\) and \(\varnothing\ne S\subsetneq V\), write
\[
\delta_G(S)=\{uv\in E:|\{u,v\}\cap S|=1\},\qquad
x(F)=\sum_{e\in F}x_e.
\]
A *fractional Hamiltonian cycle* is a weighting \(f:E\to[0,1]\) satisfying
\[
f(E)=|V|\quad\text{and}\quad f(\delta_G(S))\ge2
\quad(\varnothing\ne S\subsetneq V).
\]
The graph is *fractionally Hamiltonian* precisely when such an \(f\) exists.

For \(G=J_{m,\ell}\), the source's cut program is
\[
\operatorname{OPT}_{m,\ell}:=
\min\left\{\sum_{e\in E(G)}x_e:
x_e\ge0\ (e\in E(G)),\;
x(\delta_G(S))\ge2\ (\varnothing\ne S\subsetneq V(G))\right\}. \tag{P}
\]
Complementary shores give the same cut, so imposing each distinct cut once or
imposing the displayed constraints for all \(S\) is equivalent. Program (P)
does **not** include \(x_e\le1\). For graphs of order at least three, singleton
cuts give \(\operatorname{OPT}(P)\ge |V|\), and Lemma 7 of the inspected source
proves
\[
G\text{ is fractionally Hamiltonian}
\quad\Longleftrightarrow\quad
\operatorname{OPT}(P)=|V|.
\]
In the equality case, every singleton cut has weight \(2\), and the two-vertex
cut inequalities force every optimal \(x_e\le1\).

## Quantified target and required certificates

Determine, for **every** integer pair \((m,\ell)\) in the stated domain:

1. the exact value of \(\operatorname{OPT}_{m,\ell}\) as a function of the
   parameters;
2. a necessary-and-sufficient parameter condition for
   \(J_{m,\ell}\) to be fractionally Hamiltonian; and
3. exact symbolic certificates on every threshold/equality case.

For the yes/no classification, the equivalent LP question is whether
\(\operatorname{OPT}_{m,\ell}=n_{m,\ell}\). Determining the full numerical
value of the optimum on non-fractionally-Hamiltonian branches is stronger than
the yes/no classification, but it is retained because the frozen source asks
for that exact value explicitly.

An exact-value branch requires matching rigorous upper and lower bounds (for
example, a primal weighting and a cut-LP dual certificate). A positive
fractional-Hamiltonicity branch requires verification of all nontrivial cuts,
not merely singleton cuts. A negative branch requires a rigorous obstruction
showing \(\operatorname{OPT}_{m,\ell}>n_{m,\ell}\). Finite rational LP data may
suggest the formula but do not establish an infinite parameter branch.

The full target is the classification above. Under the source's stated scope,
a smaller publishable target may instead be a definition-closed infinite
parameter branch with an if-and-only-if classification, or an exact
counterexample to a precisely stated natural threshold; it must not be
presented as resolving the full target.

## Nearest inspected results and status

The cited arXiv identifier and title resolve to **Zhiyu Wang**, *Toughness
Bounds for Fractional Hamiltonicity and Resistance Positivity*,
arXiv:2609.03412v1 (submitted 3 September 2026), not to Flammant. This is a
bibliographic correction only; it does not alter the graph or target. The
official arXiv abstract/HTML was inspected on 2026-09-06:
<https://arxiv.org/html/2609.03412v1>.

For the same family, Wang proves:

- Lemma 7: the equivalence between fractional Hamiltonicity and
  \(\operatorname{OPT}(P)=|V|\);
- Proposition 15: \(\tau(J_{m,\ell})=1+\ell/m\) for the full parameter domain;
- Proposition 16: \(J_{m,\ell}\) is not resistance nonnegative (RN) when
  \(m\ge2\ell+4\);
- Theorem 4: fractional Hamiltonicity implies resistance positivity (RP).

Because RP implies RN directly from the definitions, these results rigorously
imply the already-settled negative branch
\[
m\ge2\ell+4\quad\Longrightarrow\quad J_{m,\ell}
\text{ is not fractionally Hamiltonian}.
\]
This inference must be recorded through the implication chain; Proposition 16
itself is not a fractional-Hamiltonicity classification. At the other coarse
extreme, Proposition 15 and the source's Theorem 2 imply the known sufficient
branch \(\ell\ge9m\), since then \(J_{m,\ell}\) is \(10\)-tough and hence
fractionally Hamiltonian. Neither statement classifies the remaining
parameters or gives the exact LP value there.

An exact-title/assertion search on 2026-09-06 located the same arXiv paper and
mirrors, but no separately inspected primary source giving the requested
classification. That limited search does not establish novelty or open status.
The problem therefore remains **source-derived / status-uncertain**.

## Proposed delta and verification route

Nearest prior result \(X\): the LP equivalence and the two coarse parameter
branches above. Proposed delta \(Y\): determine the exact LP value and sharp
boundary, beginning with the unresolved strip \(m\le2\ell+3\). Verification
route \(Z\): use the automorphism group \(S_m\times S_\ell\) to average primal
solutions, classify the cut types needed for a symbolic lower-bound proof, and
produce exact rational primal/dual certificates. Computation is a discovery
and checking aid only; every all-parameter cut reduction must be proved.
