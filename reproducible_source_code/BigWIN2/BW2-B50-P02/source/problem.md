# Precise interpreted problem

## Frozen source and finite domain

The immutable statement is `source.md` (SHA-256
`7a1de458ae0a1f0348123b6d7b4245c3d6e0f2d668670f6fcf75028bcffc6390`).
It is interpreted as a finite classification problem, not as a solution of the
unrestricted classification problem in the cited paper.

For each integer \(n\in\{2,3,4,5,6\}\), let \(\mathcal G_n\) be the set of
isomorphism classes of connected, undirected, loopless simple graphs with
exactly \(n\) vertices.  Thus the quantifier “for every connected unlabeled
finite simple graph” means

\[
  \forall n\in\{2,3,4,5,6\}\quad\forall [G]\in\mathcal G_n.
\]

A computation may choose one canonically labeled representative of each class,
with vertex set \([n]\), and identify it by its canonical graph6 string.  The
expected numbers of representatives for \(n=2,3,4,5,6\) are respectively
\(1,2,6,21,112\), hence 142 graphs in all; completeness of the eventual domain
file is part of the required certificate, not an assumption.

## Orientations, the flip graph, and Hamiltonicity

For a labeled representative \(G=([n],E)\), order the edges lexicographically
as \(e_1,\ldots,e_m\), and take the base orientation \(D_0\) that directs every
edge from its smaller to its larger endpoint.  Encode an orientation \(A\) by
a bit vector \(x(A)\in\{0,1\}^m\), where bit \(i\) records whether the direction
of \(e_i\) is reversed relative to \(D_0\).  An orientation is *acyclic* exactly
when the resulting digraph contains no directed cycle.

The simple undirected flip graph \(AO(G)\) has all acyclic orientations of
\(G\) as its vertices.  Two vertices \(A,B\) are adjacent exactly when
\(x(A)\) and \(x(B)\) have Hamming distance one.  These definitions, and the
answers below, are invariant under changing the labeled representative.

A Hamilton cycle is a cyclic list \((A_1,\ldots,A_r)\) containing every vertex
of \(AO(G)\) exactly once and satisfying \(A_iA_{i+1}\in E(AO(G))\), with
indices read modulo \(r\).  Following the cyclic-Gray-code convention and the
literal cycle definition in the cited paper (PDF p. 7), a two-item list is
allowed; consequently the single edge \(AO(K_2)=K_2\) is treated as a cyclic
Gray code.  Under the alternative convention that a simple cycle must have at
least three vertices, the \(K_2\) boundary answer changes and \(K_2\) becomes a
trivial zero-signature counterexample.  The present interpretation fixes the
former convention rather than silently leaving this boundary ambiguous.

## Acyclic signature

For any base orientation \(D\) of \(G\), set

\[
 \operatorname{rk}_D(A)=|\{e\in E(G):A\text{ and }D\text{ orient }e
 \text{ oppositely}\}|,
 \qquad
 \sigma(D)=\sum_{A\text{ acyclic}}(-1)^{\operatorname{rk}_D(A)},
\]

and define \(\sigma(G)=|\sigma(D)|\).  Changing \(D\) changes at most the sign,
so \(\sigma(G)\) is well defined.  Equivalently, if
\(\Psi(D;t)=\sum_{A\text{ acyclic}}t^{\operatorname{rk}_D(A)}\), then
\(\sigma(G)=|\Psi(D;-1)|\).  The parity lemma says
\(\sigma(G)\ne0\Rightarrow AO(G)\) is non-Hamiltonian; its converse is not
assumed.

## Exact deliverables and quantifiers

The requested atlas must, for every one of the 142 canonical representatives:

1. record its graph6 identifier, vertex and edge lists, all acyclic-orientation
   bit vectors, all flip-graph edges, and \(\sigma(G)\);
2. decide whether \(AO(G)\) has a Hamilton cycle;
3. provide a replayable cyclic list for every positive case; and
4. for every negative case with \(\sigma(G)=0\), provide an independently
   replayable complete non-Hamiltonicity certificate (exact exhaustive DP,
   SAT plus a checked UNSAT proof such as DRAT, or an equally complete method).

The subsidiary universal assertion to decide is

\[
 \forall n\in\{2,\ldots,6\}\ \forall[G]\in\mathcal G_n,
 \qquad \sigma(G)=0\Longrightarrow AO(G)\text{ is Hamiltonian}.
\]

If it is false, let \(n_0\) be the least order in this finite domain for which
a graph has \(\sigma(G)=0\) and non-Hamiltonian \(AO(G)\).  “Classify all
minimum-order counterexamples” means output every isomorphism class in
\(\mathcal G_{n_0}\) with those two properties, and no others, using canonical
graph6 identifiers.  A timeout or incomplete search has status unknown and is
not a negative case.

## Nearest prior result and proposed delta

Primary source inspected on 2026-09-07: Leonie Mühlherr and Germain Poullot,
*Hamiltonicity of graphs of acyclic orientations and acyclic polynomials*,
arXiv:2609.02249v1, <https://arxiv.org/abs/2609.02249v1>.  The local 58-page PDF
has SHA-256
`fc43647a3fd3beb1173645f93504570e546cb99edb531b62bee6319b0e6abaaf`.
Formulations 1--3 occur on PDF pp. 2 and 4; Definition 2.8 and Lemma 2.9 on
PDF p. 10 define the signature and its necessary parity condition; Appendix D,
Table 5 on PDF p. 56 reports 22 selected named graphs and explicitly includes
unknown outcomes.  The paper itself says this is a selected named-graph table,
not the complete connected atlas through six vertices.

Exact-title and equivalent-language searches on arXiv on 2026-09-07 found the
above paper but no primary source claiming the complete 142-class atlas.  This
is a literature screen, not proof of priority.  Source status is therefore
`new-question` (a finite refinement of a broader classification problem), not
a verified historical open problem.

The triage target is: nearest result = the paper's 22 selected examples;
proposed delta = a complete certificate-backed atlas for all 142 classes;
verification route = canonical graph6 enumeration, direct orientation/flip
reconstruction, checked Hamilton cycles, and proof-producing exact resolution
of zero-signature negative cases.
