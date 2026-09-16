# Precise problem statement

## Interpreted statement

All graphs below are finite, simple, and undirected. Let
\[
V(H)=\mathbb Z_3\times\mathbb Z_4
\]
and let `H` be the Cartesian product `C_3 square C_4`. Thus two distinct
vertices `(i,j)` and `(i',j')` are adjacent precisely when either

- `j=j'` and `i-i'` is `1` or `-1` in `Z_3`, or
- `i=i'` and `j-j'` is `1` or `-1` in `Z_4`.

Equivalently, its 24 edges are the 12 unordered pairs
`{(i,j),(i+1,j)}` and the 12 unordered pairs `{(i,j),(i,j+1)}`, with
coordinates reduced modulo 3 and 4. The graph has 12 vertices and is
4-regular.

For `A,B subseteq E(H)`, write
\[
A\mathbin{\triangle}B=(A\setminus B)\cup(B\setminus A).
\]
A connectivity code is an arbitrary family `C subseteq 2^{E(H)}` such
that, for every ordered or unordered pair of **distinct** members
`A,B in C`, the spanning subgraph `(V(H), A triangle B)` is connected.
The word “spanning” fixes the vertex set to all 12 vertices; connectivity
therefore also excludes isolated vertices.

Determine the exact integer
\[
m(H)=\max\bigl\{|C|:C\subseteq 2^{E(H)},\ 
 (V(H),A\triangle B)\text{ is connected for all distinct }A,B\in C\bigr\}.
\]
The maximum is over all families, not only linear subspaces of
`F_2^{E(H)}`.

## Normalizations and bounds

Symmetric-difference translation preserves the condition: for any fixed
`D subseteq E(H)`, the family `{A triangle D:A in C}` has the same size
and pairwise differences. Hence a search may normalize one codeword to
the empty set without assuming linearity.

For any vertex `v`, restriction `A -> A intersect delta_H(v)` is injective
on a connectivity code: equal restrictions for two distinct words would
make `v` isolated in their difference. Since `|delta_H(v)|=4`,
\[
m(H)\le 2^4=16.
\]
Thus a family of 16 explicitly encoded words plus an exact replay of all
120 pairwise connectivity checks proves `m(H)=16`. If no such family
exists, determining the exact value requires both a construction attaining
some `k<16` and a complete, independently checkable upper-bound
certificate for all arbitrary (possibly nonlinear) families of size
`k+1`.

The phrase “smallest natural non-diagonal product” in the lead is
descriptive only. The frozen mathematical task has no quantifier over
other products: it concerns exactly `C_3 square C_4`.

## Prior result, status, and proposed delta

Source status: **open-supported**, not certified open in an absolute sense.

- Bai, Gao, Ma, and Wu, *Phase Transitions of Structured Codes of Graphs*,
  arXiv:2307.08266v1 (retrieved 2026-09-07), Proposition 1.7 and its proof,
  establish `m(C_m square C_n)<=16` for all `m,n>=3` and equality for
  `m=n=3`; their Problem 4.1 asks whether equality holds for all such
  products. Primary source:
  https://arxiv.org/html/2307.08266v1 (Proposition 1.7, proof in Section
  3.6, and Problem 4.1).
- Tian, *Alon's Question on Connectivity Graph-Codes: f(d)=2^d for Every
  d>=4*, arXiv:2609.02953v1 (retrieved 2026-09-07), defines the same
  invariant and repeats in Section 6(d) that determining products of cycles
  remains open. Primary source: https://arxiv.org/abs/2609.02953v1. The
  inspected local PDF is the 10-page file identified in `source.md`; its
  relevant statement is on PDF page 8.
- Bounded searches on 2026-09-07 for the exact pair `C_3,C_4`, toroidal-grid
  terminology, and connectivity graph-codes found no primary source
  settling this instance. This is a literature-screening result, not proof
  of novelty or present open status.

Nearest prior result `X`: the universal 16 upper bound and the 16-word
construction for `C_3 square C_3`. Proposed delta `Y`: determine the exact
value for the first fixed non-diagonal instance `C_3 square C_4`.
Verification route `Z`: first seek a 16-word witness, beginning with the
more constrained four-dimensional linear-labeling model and replaying all
15 nonzero differences exactly. If that model is unsatisfiable, the
unsatisfiability proves only nonexistence of a linear optimum; the original
problem must then be attacked as a general normalized maximum-clique/SAT
problem, with proof certificates checked independently.
