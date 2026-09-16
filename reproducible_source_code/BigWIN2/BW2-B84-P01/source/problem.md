# Precise reading: diameter of the \(K_{3,3}\) graph associahedron

Provenance: `win-00084-p01-triage-1d1fb59d7fdc`  
Frozen source: `source.md`, SHA-256
`ad57a7fcb9e8fd4626d17086a4c94e4e25059b2e75d86a8a294ec98015c3c5f1`.

## Statement and conventions

Let \(G\) be the finite simple graph with labelled vertex set
\[
V(G)=P\sqcup Q,\qquad P=\{p_1,p_2,p_3\},\quad
Q=\{q_1,q_2,q_3\},
\]
and edge set \(\{\{p_i,q_j\}:1\le i,j\le3\}\). Thus \(G=K_{3,3}\);
there are no edges within either part.

A **tube** is a nonempty set \(S\subseteq V(G)\) for which the induced graph
\(G[S]\) is connected. In particular, singletons and the full set are tubes.
Two distinct tubes \(S,S'\) are **compatible** exactly when either
\(S\subset S'\), \(S'\subset S\), or \(S\cap S'=\varnothing\) and
\(G[S\cup S']\) is disconnected. A **tubing** is a set of pairwise compatible
tubes, and it is **maximal** when it is inclusion-maximal among such sets.

Define \(R(G)\) to be the finite simple graph whose vertices are the labelled
maximal tubings. Distinct maximal tubings \(T,T'\) are adjacent exactly when
\(|T\mathbin\triangle T'|=2\), i.e. one non-full tube is exchanged. This is
equivalently the legal-rotation graph of labelled search trees on \(G\). Let
\(d(T,T')\) be shortest-path length in \(R(G)\), and
\[
\operatorname{diam}R(G)=\max_{(T,T')\in V(R(G))^2}d(T,T').
\]
The frozen assertion, with no free parameters, is
\[
\boxed{\operatorname{diam}R(K_{3,3})=12}.
\]

No quotient by graph automorphisms is intended. Retaining the full tube makes
it a common member of every maximal tubing; omitting that common member gives
the naturally isomorphic flip graph. Taking the maximum over ordered rather
than unordered pairs also does not change the diameter.

## Nearest prior results and status

The following primary sources were inspected locally and their current arXiv
records were checked on 2026-09-10.

- Cardinal--Pournin--Valencia-Pabon, *Diameter estimates for graph
  associahedra*, [arXiv:2106.16130v2](https://arxiv.org/abs/2106.16130), last
  revised 2021-11-17 and published in *Annals of Combinatorics* 26 (2022).
  Definitions and flips occur on PDF pp. 2--3; Theorem 2 gives monotonicity
  under adding graph edges; Theorem 8 gives the complete-split diameter; and
  Question 2 on p. 18 asks for the balanced complete-bipartite family.
- Gargantini--Pastine--Torres, *Effect of graph operations on graph
  associahedra*, [arXiv:2406.06317v2](https://arxiv.org/abs/2406.06317), last
  revised 2024-10-10. Theorem 4.7 on PDF p. 28 compares deleting the clique
  edges among true twins, and Corollary 4.8 on p. 29 improves the balanced
  lower bound. The paper states exact values only for \(K_{2,q}\),
  \(3\le q\le8\), within the balanced cases it treats.

For the complete split graph \(SPK_{3,3}\), Theorem 8 of the first source gives
\(\operatorname{diam}R(SPK_{3,3})=13\). Since \(K_{3,3}\) is obtained by
deleting the three clique edges on its three true twins, Theorem 4.7 gives
\(13-\binom32\le\operatorname{diam}R(K_{3,3})\); monotonicity gives the reverse
comparison with 13. Hence the verified prior range is
\[
10\le\operatorname{diam}R(K_{3,3})\le13.
\]
Corollary 4.8 also specializes to the lower bound 10.

Exact-assertion and equivalent-language searches found no primary source
settling \(K_{3,3}\) beyond these papers. This limited search is not evidence
of priority. The balanced-family problem is explicitly open-supported, while
the fixed proposed value 12 is best classified as a new-question lead rather
than as a literature-certified open conjecture.

## Triage target

Nearest prior result: the interval \([10,13]\) above. Proposed delta: certify
the exact value 12 for the first untreated balanced diagonal case. Verification
route: two structurally independent exhaustive constructions of all labelled
states and legal edges, an exact graph comparison, and complete BFS distance
certificates. The existing single implementation is only a promising triage
observation and is not yet a computer-assisted proof.
