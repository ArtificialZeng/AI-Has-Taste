# Precise reading of `M_3(4)`

## Frozen target

Let \(\mathcal G\) be the class of all finite simple undirected graphs \(G\)
such that:

1. \(G\) is **3-degenerate**, meaning every nonempty subgraph \(H\subseteq G\)
   has a vertex of degree at most 3 in \(H\) (so the degeneracy is at most 3,
   not necessarily exactly 3);
2. \(\Delta(G)\le 4\); and
3. \(G\) contains no subgraph isomorphic to \(K_{3,4}\). Here “copy” means a
   subgraph, not necessarily an induced subgraph.

A **B-coloring** of \(G\) is a map from \(E(G)\) to a set of colors which is a
proper edge-coloring and for which the four edges of every (simple) 4-cycle
receive pairwise distinct colors. Let \(q_B(G)\) be the minimum number of
colors in such a coloring. Equivalently, define \(\Gamma_B(G)\) to have vertex
set \(E(G)\), with two edges adjacent when they share an endpoint or are
opposite edges of a 4-cycle in \(G\). Then
\[
q_B(G)=\chi(\Gamma_B(G)).
\]

The problem is to determine the integer
\[
M_3(4)=\max_{G\in\mathcal G}q_B(G).
\]
Allowing an empty graph or isolated vertices does not affect this maximum.

## Exact dichotomy and quantifiers

Hu–Kong–Wang, Theorem 2.8, specialized to \(\Delta=4\), proves
\(q_B(G)\le 10\) for every \(G\in\mathcal G\). The graph \(K_{3,3}\) belongs
to \(\mathcal G\), and every pair of its nine edges either meets or is opposite
on a 4-cycle. Thus \(\Gamma_B(K_{3,3})=K_9\), so \(q_B(K_{3,3})=9\). Hence
\[
M_3(4)\in\{9,10\}.
\]
The maximum is well-defined: the legal witness \(K_{3,3}\) supplies value 9,
the universal bound is 10, and \(q_B\) is integer-valued.

Therefore the two possible resolutions are exactly:

- \(M_3(4)=10\): exhibit some \(G\in\mathcal G\) and prove
  \(\chi(\Gamma_B(G))\ge10\). Theorem 2.8 then proves equality.
- \(M_3(4)=9\): prove that for every \(G\in\mathcal G\),
  \(\Gamma_B(G)\) is 9-colorable; the \(K_{3,3}\) example proves sharpness.

Because \(q_B\) of a disjoint union is the maximum of the values on its
components, a search for a value-10 witness may be restricted to connected
graphs without loss.

## Source and status check

Primary source inspected: Xiaoxue Hu, Jiangxu Kong, and Yiqiao Wang,
“Degeneracy bounds, stability, and a sharp gap for B-colorings,”
[arXiv:2609.02845v1](https://arxiv.org/abs/2609.02845v1), submitted 2026-09-02;
retrieved 2026-09-06. The local PDF
`bigWin-43-materials/2609.02845.pdf` has SHA-256
`a79e4af468034794abd8b58e28796a59563943786368e870b23816ac685d6868`,
matching `source.md`. Definitions occur on PDF page 1, Theorem 2.8 on PDF
page 6, the 9-versus-10 consequence on PDF page 7, and Problem 4.1 on PDF
page 15.

Bounded exact-phrase and equivalent-language web searches on 2026-09-06 found
the cited arXiv v1, which explicitly poses the family problem, and no separate
primary source resolving the specialization \(M_3(4)\). This records the
search result, not a claim of priority or proof that the case remains open.

## Triage target

Nearest prior result: the source's \(9\le M_3(4)\le10\). Proposed delta:
settle this one-unit gap, preferably first by finding and certifying a legal
value-10 witness. Verification route: construct \(\Gamma_B(G)\), check all
graph-class predicates independently, and certify non-9-colorability (with an
independently checkable SAT unsatisfiability certificate if computation is
decisive). A failed bounded witness search is only finite evidence and cannot
establish the universal value 9.
