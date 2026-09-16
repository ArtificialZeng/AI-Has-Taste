# Fresh mathematical referee report

## Frozen scope and verdict

The submitted candidate is the `result-note` claim that, for
\(H=K_{1,3}\sqcup K_2\) interpreted as an ordinary (not necessarily
induced) subgraph, every red-blue colouring of every finite simple maximal
planar graph on at least 21 vertices has a monochromatic copy of \(H\).
Equivalently, it proves \(P(21)\) and hence
\(r_{\mathrm{MP}}(H,H)\le 21\), without claiming that 21 is least.

**Verdict: accept.** The elementary structural and planar-counting argument
proves the exact frozen statement uniformly at every order \(n\ge21\). The
result is a genuine partial answer to the unresolved original problem, not a
resolution of its least-threshold part.

The SHA-256 hashes of `source.md`, `problem.md`, `claim.json`,
`evidence/upper-bound.md`, and `evidence/external/2609.05268.pdf` were
recomputed and agree with all five entries of `audit/snapshot.json`.

## Reconstruction of the decisive argument

Let \(F\) be one colour graph. A subgraph claw on vertex set \(C\) and an
edge whose endpoints avoid \(C\) are exactly a copy of
\(K_{1,3}\sqcup K_2\). Therefore an \(H\)-free graph either has maximum
degree at most two, or the four vertices of every selected claw cover all
of its edges. This uses the non-induced convention correctly: extra edges
among the selected vertices are harmless.

For a maximum-degree vertex \(v\) of degree \(d\ge3\) in an \(H\)-free
colour graph:

- If \(d=3\), the claw consisting of \(v\) and its three neighbours gives
  a four-vertex cover of all edges.
- If \(d=4\), any edge not incident with \(v\) must have both endpoints in
  \(N(v)\). Otherwise at most one of the four neighbours is excluded by
  the edge, leaving three neighbours that form with \(v\) a disjoint
  claw. Thus every nonisolated vertex belongs to \(\{v\}\cup N(v)\).
- If \(d\ge5\), an edge not incident with \(v\) excludes at most two of
  its neighbours, leaving three for a disjoint claw. Hence every edge is
  incident with \(v\).

Call a colour type L when its maximum degree is at most two, and type C
otherwise. For a simple maximal planar graph of the relevant orders,
\(e(G)=3n-6\) and \(\delta(G)\ge3\).

In case LL, each colour has at most \(n\) edges, so
\(3n-6=e(G)\le2n\), which is impossible for \(n\ge7\).

In a mixed case, take red to be L and choose a maximum-degree blue vertex
\(v\):

- For \(d_B(v)=3\), the four-set \(S=\{v\}\cup N_B(v)\) covers the blue
  edges. Each vertex outside \(S\) has host degree at least three but red
  degree at most two, and so is incident with a blue edge. That edge must
  meet \(S\). Distinct outside vertices require distinct cross-edges, while
  the sum of the blue degrees in \(S\) is at most 12. Hence
  \(|V(G)\setminus S|\le12\) and \(n\le16\).
- For \(d_B(v)=4\), the preceding one-colour analysis makes every vertex
  outside \(\{v\}\cup N_B(v)\) blue-isolated. Such a vertex would have at
  least three red incident edges, contradicting type L. Hence \(n\le5\).
- For \(d_B(v)\ge5\), every blue edge is incident with \(v\), so all
  edges of \(G-v\) are red. Since \(d_G(v)\le n-1\),
  \[
  e(G-v)=3n-6-d_G(v)\ge2n-5.
  \]
  But a graph on \(n-1\) vertices with maximum degree at most two has at
  most \(n-1\) edges. These inequalities conflict for \(n\ge5\).

The colour-swapped mixed case is identical.

In case CC, select one claw in each colour and let their vertex sets be
\(S_R,S_B\). Each is a four-vertex cover of its own colour graph. Put
\(S=S_R\cup S_B\), \(s=|S|\le8\), and
\(T=V(G)\setminus S\), \(t=|T|\). No edge can have both endpoints in
\(T\), because either colour would miss its corresponding cover. Every
vertex of \(T\) consequently sends all of its at least three host edges to
\(S\). The graph formed by the \(S\)-\(T\) edges is simple, planar, and
bipartite, so its standard Euler bound gives
\[
3t\le e_G(S,T)\le2(s+t)-4.
\]
Thus \(t\le2s-4\), and
\(n=s+t\le3s-4\le20\). All possible type pairs are covered. An avoiding
colouring at any \(n\ge21\) is therefore impossible, exactly proving the
candidate statement.

## Stress tests and scope checks

- The quantifiers are uniform: the proof assumes an arbitrary maximal
  planar host and arbitrary two-colouring, and its contradiction applies
  separately for every \(n\ge21\). It does not rely on one finite host.
- At the candidate orders there are no small-order exceptions to
  \(e(G)=3n-6\), \(\delta(G)\ge3\), or the bipartite planar edge bound.
- Overlap between \(S_R\) and \(S_B\) is allowed; it only decreases
  \(s\) and strengthens the final estimate. Edges internal to \(S\) are
  irrelevant to the cross-edge planar subgraph.
- The choices of three neighbours in the degree-four and degree-at-least-
  five cases remain valid even when the candidate edge has endpoints in
  the neighbourhood: respectively at most one and at most two neighbours
  are excluded.
- No limiting argument, division, compactness step, computation, or
  external theorem beyond standard elementary planar facts is used.
- The proof establishes only \(r_{\mathrm{MP}}(H,H)\le21\). It supplies
  neither an avoiding colouring below 21 nor the least threshold, so the
  original exact-value question correctly remains unresolved.

## Source comparison and contribution

The supplied paper PDF has the requested SHA-256 digest
`d2c05952bb165545210571a572678338e7766162141549adbf62411e3cf881b2`.
Direct inspection confirms the relevant boundary:

- Definition 1 uses the same “every graph of order at least \(N\)”
  unavoidability convention.
- Corollary 2 covers trees on at most four vertices, hence the claw alone,
  but not its disjoint union with an additional edge.
- Proposition 4 gives necessary conditions for a diagonal MP-unavoidable
  graph. The present forest satisfies them: it has only one component of
  order greater than three and both component diameters are at most five.
- Theorem 11 and Remark 5 cover subgraphs of
  \(P_5\sqcup tK_2\). Those graphs have maximum degree at most two, so
  they cannot contain the degree-three graph \(H\).
- Section 5, Problem 2 asks for the complete disconnected diagonal
  classification and does not single out or settle this graph.

Relative to that verified source boundary, the candidate supplies a
specific membership result and an explicit uniform upper bound for a
previously untreated disconnected graph. The claw-cover reduction and the
CC planar bipartite count are not a restatement of any cited theorem, and
the result can serve as a bounded starting point for determining the exact
threshold. This is a nontrivial and coherent result-note contribution.

The frozen evidence contains one directly audited primary source and does
not establish global priority. That limitation is already stated honestly
in `claim.json` and `problem.md`; acceptance here does not strengthen it
into a priority claim.
