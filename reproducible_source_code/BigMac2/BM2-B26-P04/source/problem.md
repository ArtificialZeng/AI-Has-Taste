# Precise problem statement

## Frozen question

The immutable question in `source.md` is read literally as follows. Does there
exist a finite undirected simple graph \(G=(V,E)\) with \(|V|=13\) such that

\[
  \beta(G):=\max_{H\in [G]_{\mathrm{LC}}}\alpha(H)\le 4?
\]

Equivalently, the quantified assertion to decide is

\[
 \exists G\ (|V(G)|=13)\quad
 \forall H\in [G]_{\mathrm{LC}}\quad
 \forall S\in\binom{V(H)}5,
 \qquad E(H[S])\ne\varnothing.                 \tag{1}
\]

Graphs have exactly 13 vertices, not at most 13. Isomorphic copies represent
the same mathematical witness, although an exact computation may retain fixed
vertex labels.

## Definitions

- A **simple graph** is finite, undirected, loopless, and has no parallel
  edges.
- The **independence number** \(\alpha(H)\) is the largest cardinality of a vertex
  subset inducing no edges.
- For a vertex \(v\), the **local complement** \(\tau_v(H)\) is obtained by
  toggling adjacency for every pair of distinct vertices in the neighborhood
  \(N_H(v)\). All other adjacencies, including those incident with \(v\), are
  unchanged.
- The **local-complementation orbit** is
  \[
    [G]_{\mathrm{LC}}
      =\{\tau_{v_t}\cdots\tau_{v_1}(G):t\ge0,
          \ v_i\in V(G)\}.
  \]
  The empty sequence is allowed, so \(G\in[G]_{\mathrm{LC}}\). The orbit is
  finite, hence the maximum defining \(\beta\) exists.
- A graph \(K\) is a **vertex-minor** of \(G\) if it can be obtained using local
  complementations and vertex deletions. Deletions can be commuted to the end
  of such a sequence, so \(K\) is a vertex-minor precisely when it is isomorphic
  to an induced subgraph of some member of \([G]_{\mathrm{LC}}\).
- \(E_5\) denotes the edgeless graph on five vertices.

Consequently, \(E_5\) is a vertex-minor of \(G\) exactly when some
\(H\in[G]_{\mathrm{LC}}\) has an independent five-set. Thus (1) is exactly the
assertion that a 13-vertex graph exists with no \(E_5\) vertex-minor; it is not
merely a one-way implication.

## Resolution and certificate scope

For an affirmative resolution, the frozen source requires all of the following:

1. an explicit graph6 string that decodes to a 13-vertex simple graph;
2. an exact breadth-first traversal starting from that labeled graph and applying
   local complementation at every one of the 13 vertices of every reached state
   until the queue is empty;
3. lossless duplicate handling—for example, the complete labeled adjacency
   bitstring with equality checked, or a certified canonical isomorphism key if
   the traversal is quotiented by isomorphism; and
4. a separate exact verifier showing that every enumerated orbit member has no
   independent five-set (equivalently, has independence number at most four).

The orbit traversal must establish closure under all 13 local-complement moves;
a collection of sampled states or a collision-prone hash alone is not a
certificate. The independent checker may exhaust all \(\binom{13}{5}=1287\)
five-subsets for every orbit member, since excluding independent five-sets also
excludes all larger independent sets.

A negative resolution would require the universal negation of (1): every
13-vertex simple graph must have an orbit member containing an independent
five-set. Failure to find a witness, including failure of a bounded search,
does not establish this. The frozen target does not request an exhaustive
classification of all 13-vertex graphs.

## Status boundary and proposed contribution

As reported in `source.md` (not independently literature-verified in this
triage job), Bae, arXiv:2604.13434v1, proves \(R_{\mathrm{vm}}(5)\ge13\),
conjectures \(R_{\mathrm{vm}}(5)=15\), and leaves the relevant \(k=5\) case
unresolved. Under the convention stated there, a certified graph satisfying
(1) would improve the lower bound to \(R_{\mathrm{vm}}(5)\ge14\).

The proposed delta is therefore one explicit 13-vertex witness with a complete,
independently checkable exact orbit certificate. Current literature and
candidate-database status remain unverified; no novelty or resolution claim is
made at triage.
