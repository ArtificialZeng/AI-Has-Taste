# Proof dependency graph

## Endpoint

**T9.** For every simple graph \(G\) on nine vertices with
\(e(\overline G)\le6\), \(q(G)=2\).

The same certificate independently reconstructs the published baseline at
orders seven and eight.

## Dependencies

```text
D1 exact definition of S(G), q(G)
  |
  +--> L1 two eigenvalues <=> symmetric involution
  |
  +--> L2 rational weighted Parseval frame => exact involution in S(G)
  |       |
  |       +--> C1 exact Fraction checks for 14 residual graph types
  |
  +--> L3 complement-component partition => graph join
          |
          +--> E2 balanced connected-join theorem (source verified)

E1 bipartite-complement theorem (source verified)

L4 unique connected-component decomposition; each <=6-edge connected
   component has at most seven vertices
  |
  +--> C2 graph-atlas component-multiset reconstruction
  +--> C3 independent Burnside counts by edge number
          |
          +--> C4 exhaustive route partition BIP / JOIN / FRAME

L1 + L2 + L3 + L4 + E1 + E2 + C1--C4
  |
  +--> T7 (baseline reproduction)
  +--> T8 (last published baseline reproduction)
  +--> T9 (new finite endpoint)
```

## Lemmas reconstructed from definitions

### L1: orthogonal normalization

If a real symmetric \(A\in S(G)\) has precisely the eigenvalues
\(\lambda\ne\mu\), then
\[
Q=\frac{2A-(\lambda+\mu)I}{\lambda-\mu}
\]
is symmetric, lies in \(S(G)\), and obeys \(Q^2=I\).  Conversely, a
non-scalar symmetric involution in \(S(G)\) has exactly two eigenvalues.  The
graphs in T7--T9 are nonempty, so a realizing involution cannot be scalar.

### L2: exact frame lemma

Let \(H=\overline G\).  Suppose \(0<r<n\), \(w_i\in\mathbb Q^r\), and
\(x_i\in\mathbb Q_{>0}\) satisfy
\[
w_i^\top w_j=0\iff ij\in E(H),\qquad
\sum_i x_iw_iw_i^\top=I_r.
\]
For row \(i\) of \(V\) equal to \(\sqrt{x_i}w_i^\top\), the second identity
is \(V^\top V=I_r\).  Hence \(P=VV^\top\) satisfies \(P^2=P=P^\top\) and has
rank \(r\).  Positivity of the \(x_i\) makes
\(P_{ij}=0\iff w_i^\top w_j=0\).  Thus \(Q=I-2P\) is a nontrivial symmetric
involution whose off-diagonal support is exactly \(E(G)\).

### L3: join routing

If the connected components of \(H\) can be divided into nonempty unions
\(H_L,H_R\), there are no \(H\)-edges between their vertex sets.  Every such
cross pair is therefore an edge of \(G\), and
\[
G=\overline{H_L}\vee\overline{H_R}.
\]
When both factors are connected and their orders differ by at most two, the
source-verified balanced connected-join theorem gives \(q(G)=2\).

### L4: enumeration completeness

Every graph is uniquely the disjoint union of its connected components.  A
nontrivial connected graph with at most six edges has at most seven vertices,
because it contains a spanning tree.  Consequently all possible components
occur in the graph atlas through order seven.  The verifier forms every
multiset of these component types within the vertex/edge budgets and fills
the unused vertices with isolates.  Component uniqueness prevents duplicate
isomorphism types.  Independently, Burnside's lemma counts fixed edge sets for
each conjugacy class of \(S_n\); the component enumeration agrees edge by edge
for \(n=7,8,9\).

## Exact route counts

| order | all types | bipartite theorem | balanced join | exact frame |
|---:|---:|---:|---:|---:|
| 7 | 19 | 16 | 2 | 1 |
| 8 | 44 | 33 | 10 | 1 |
| 9 | 108 | 72 | 24 | 12 |

The routes are applied in the displayed priority order, so these columns are
disjoint and sum to the total.  Every exact-frame case has \(r=3\).

## External theorem bindings

- **E1:** Barrett et al. (2026), Theorem 3.7: the conjectured threshold holds
  when the complement is bipartite.
- **E2:** Levene--Oblak--Šmigoc (2024), Theorem 3.4 with one connected
  component on each side: connected factors whose orders differ by at most
  two have a join with \(q=2\).

Both statements, endpoints, DOI records, and original text locations are
recorded in `literature/claim_ledger.md`.
