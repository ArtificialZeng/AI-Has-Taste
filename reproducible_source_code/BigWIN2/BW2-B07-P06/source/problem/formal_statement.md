# Formal statement (locked 2026-08-30)

## Definitions

All graphs below are finite, undirected, simple graphs. For a graph \(G\),
Stanley's chromatic symmetric function is
\[
X_G=\sum_{\substack{\kappa:V(G)\to\mathbb N\\ \kappa\ {\rm proper}}}
       \prod_{v\in V(G)}x_{\kappa(v)}.
\]
A connected graph is *unicyclic* when it has exactly one cycle. Write
\(n(G)=|V(G)|\) and \(c(G)\) for the length of its unique cycle.

Delete the cycle edges of a connected unicyclic graph \(G\). The resulting
components, rooted at their unique cycle vertices, are denoted
\(T_v\) for \(v\) on the cycle. Define
\[
r(G)=\#\{v\in V(C): |V(T_v)|>1\}
    =\#\{v\in V(C):\deg_G(v)\ge 3\}.
\]
Thus \(r(G)\) is the number of attached non-trivial rooted trees, not the
number of non-cycle vertices and not the number of rooted-tree isomorphism
types.

An internal vertex has degree at least two. An internal edge has two
internal endpoints, and
\[
k(G)=\#\{uv\in E(G):\deg_G(u),\deg_G(v)\ge2\}.
\]
The degree sequence \(d(G)\) is the multiset of vertex degrees, conventionally
listed in non-increasing order.

## Locked conjecture

For every pair \(G_1,G_2\) of connected unicyclic graphs satisfying either

1. \(c(G_1)=c(G_2)=3\) and \(n(G_1)=n(G_2)\) is odd; or
2. \(c(G_1)=c(G_2)=c\ge4\),

the implication
\[
X_{G_1}=X_{G_2}\quad\Longrightarrow\quad
\bigl(d(G_1),r(G_1),k(G_1)\bigr)
=\bigl(d(G_2),r(G_2),k(G_2)\bigr)
\]
holds.

Equality of the homogeneous symmetric functions already forces equal order.
For connected unicyclic graphs it also forces equal cycle length, by the
source paper's cycle-length result, so explicitly requiring common \(n\) and
\(c\) only removes ambiguity from the quantifier structure.

## Boundary and redundancy audit

- A simple cycle has \(r=0\), \(k=n\), and degree sequence \(2^n\); it is
  included in the \(c\ge4\) clause.
- The excluded class \(c=3\), even \(n\), is known to contain equal-CSF pairs
  with different values of all three listed invariants.
- For every connected unicyclic graph with \(n\ge3\), every non-internal edge
  is incident with exactly one leaf. Hence
  \(k(G)=n(G)-n_1(G)\), where \(n_1(G)\) is the number of degree-one
  vertices. Consequently equality of degree sequences already implies
  equality of internal-edge counts. The conjecture is nevertheless kept in
  its original three-invariant form.

## Source-version correction

The literal problem calls the statement “Conjecture 9.1.” That is the
numbering in arXiv:2505.06486v1 (May 2025). The version of record in *The
Electronic Journal of Combinatorics* 33(3) (2026), article P3.12, renumbers it
as Conjecture 63 without changing the mathematical endpoint.
