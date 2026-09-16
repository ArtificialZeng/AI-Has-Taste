# Source statement — win-00047-p02

## Exact frozen question

Fix a standard normalized Paley Hadamard matrix (H) of order (8). Fix the complete family (mathcal L={L_1,\ldots,L_6}) of six Desarguesian mutually orthogonal Latin squares of order (7) arising from (\mathbb F_7). For each (i\in\{1,\ldots,6\}), let

\[
G_i=\Gamma\bigl(H;\mathcal L\setminus\{L_i\}\bigr)
\]

be the graph defined by Greaves--Tan's construction.

Determine the number of graph-isomorphism classes among (G_1,\ldots,G_6), give a canonical representative for every class, and in particular decide whether the six graphs are pairwise isomorphic. The source theorem implies that every (G_i) is a Neumaier graph with parameters

\[
(v,k,\lambda;e,s)=(280,160,96;18,35)
\]

and the same five eigenvalues. These shared invariants do not settle isomorphism.

Any computational classification must include an independently checkable construction of every adjacency list and either explicit vertex permutations witnessing claimed isomorphisms or canonical labels/stabilizer data plus a complete verifier.

## Primary source and known boundary

Gary Greaves and Zhao Kuang Tan, *Neumaier graphs of coherent rank five*, arXiv:2609.02218v1. See Theorem 4.3 on p.6, Example 5.1 and Question 5.4 on p.7. Question 5.4 explicitly asks how the isomorphism type of (\Gamma(H;L)) depends on the Hadamard matrix and MALS family.

Local primary-source copy: `batches/inbox/bigWin-47-materials/2609.02218.pdf` (SHA-256 `2bb8a878244be3bdf7bfe57da4c1108612dda11e3ecd84f073cfddbe2e15ce9a`).

## Proposed contribution boundary

Only the fixed standard (q=7) Desarguesian family and its six deleted-one subfamilies are in scope. Do not generalize to arbitrary Hadamard matrices or MALS families without new proof.
