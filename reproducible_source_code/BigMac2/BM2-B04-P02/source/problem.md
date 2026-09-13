# Precise problem statement

## Frozen input and interpretation

The immutable original statement is `source.md` (SHA-256
`ed872b78b52d5cc0ddc57d8a49aaf786dbcf1e0b5091c4967d207fa60f97295a`).
This file fixes the following mathematical reading; it does not alter the
original claim.

All graphs are finite, simple, and undirected, and are classified up to graph
isomorphism.  For a graph \(G=(V,E)\), set \(n=|V|\), and let \(A(G)\) be its
\(n\times n\) adjacency matrix.  Write its real adjacency eigenvalues, counted
with algebraic multiplicity, as \(\lambda_1(G),\ldots,\lambda_n(G)\), and define

\[
s^+(G):=\sum_{i:\,\lambda_i(G)>0}\lambda_i(G)^2
       =\sum_{i=1}^n \max\{\lambda_i(G),0\}^2.
\]

Zero eigenvalues make no contribution.  Equality is exact equality of real
algebraic numbers, not equality within a numerical tolerance.

Here **2-connected** means \(n\ge 3\) and \(G-v\) is connected for every
\(v\in V(G)\) (equivalently, \(G\) is connected and has no cut vertex).
Here **noncycle** means that \(G\not\cong C_n\).  Under these conventions, a
2-connected graph is a cycle exactly when every vertex has degree two;
therefore the input class can equivalently be written as the 2-connected
graphs with \(\Delta(G)\ge 3\).  It is empty at order three, so every graph in
scope has \(n\ge4\).

## Quantified target

Determine an explicit isomorphism-invariant structural class \(\mathcal E\)
such that, for every finite simple undirected graph \(G\),

\[
\bigl[G\text{ is 2-connected and }G\not\cong C_{|V(G)|}\bigr]
\quad\Longrightarrow\quad
\bigl[s^+(G)=|V(G)|\iff G\in\mathcal E\bigr].
\]

The answer must prove both directions for all orders.  “Structural” excludes
the tautology \(\mathcal E=\{G:s^+(G)=|V(G)|\}\), and a finite enumeration up
to a fixed order is not a classification.  Such enumeration may only generate
or falsify proposed structural families.

No assertion about \(s^-(G)\), cycles, disconnected graphs, multigraphs,
directed graphs, weighted adjacency matrices, or infinite graphs is part of
the requested classification.  The identity
\(s^+(G)+s^-(G)=2|E(G)|\) is available as an equivalent bookkeeping relation,
but it does not change the target.

## Nearest verified result and present status

Akbari--Hu--Liu, *Positive and Negative Square Energies of 2-Connected
Graphs*, arXiv:2609.04069v1 (submitted 2026-09-03), was inspected on
2026-09-06 at <https://arxiv.org/abs/2609.04069> and
<https://arxiv.org/pdf/2609.04069>.  Its conventions agree with those above.
Theorem 3.4 proves \(s^+(G)\ge n\) whenever \(G\) is 2-connected and
\(\Delta(G)\ge3\).  It also proves strict inequality when some
maximum-degree vertex belongs to no triangle.  Consequently, any equality
graph in the present noncycle class must have every maximum-degree vertex in
at least one triangle.  Theorems 3.5--3.6 handle cycles and the universal
lower-bound classification, not the noncycle equality cases.

The inspected v1 paper does not state a necessary-and-sufficient structural
classification of its noncycle equality layer.  This establishes the precise
source-derived delta but not global novelty or open status; the problem remains
`status-uncertain` pending a broader primary-literature search.

## Proposed contribution and verification route

Nearest prior result: the lower bound in Theorem 3.4.  Proposed delta: an
all-orders necessary-and-sufficient structural classification of equality.
Verification route: first obtain exact small-order equality examples and
nonexamples, then trace equality simultaneously through vertex deletion, the
Liu--Tang--Zhang bound, the positive-part variational inequality, and the local
energy estimate; finally prove that the resulting structural conditions are
both necessary and sufficient.

Provenance: `bigMac-00004-p02-triage-9fc810db5782`.
