# Proof dependency graph

Status: partial exact reductions only; no proof of F1.

## Target and source frontier

- **F1**: every finite simple triangle-free graph with \(\Delta\le6\) is
  5-colourable.
- **S1 (verified external)**: Brooks' theorem.
- **S2 (verified external)**: Abrishami--Erfanian Theorem 3 excludes an F1
  counterexample through order 32.
- **S3 (verified external)**: the current literature still treats F1 as open.
- **S4 (verified external)**: Gallai's theorem says that the vertices of
  degree \(k-1\) in a \(k\)-critical graph induce a Gallai forest.
- **S5 (verified external)**: Gao--Postle's \(K_4\)-free 6-critical density
  theorem gives
  \[
    |E(G)|\ge \left(\frac{14}{5}+\frac1{1050}\right)|V(G)|-\frac95.
  \]

## Exact reduction DAG

1. `F1 false`
   -> choose a counterexample \(G\) with minimum \(|V|\), and subject to that
   maximum \(|E|\).
2. `S1 + triangle-free + Delta<=6`
   -> \(\chi(G)=6\).
3. `minimum |V|`
   -> \(G-v\) is 5-colourable for every \(v\)
   -> \(G\) is 6-vertex-critical
   -> \(5\le d(v)\le6\) for every \(v\).
4. `maximum |E| under minimum |V|`
   -> if \(x,y\) are nonadjacent with no common neighbour and both have
   degree five, then adding \(xy\) preserves triangle-freeness, the degree
   cap, and \(\chi=6\), contradiction
   -> every two degree-five vertices have distance at most two.
5. Let \(L=\{v:d(v)=5\}\). If \(L\ne\varnothing\), choose \(v\in L\).
   By step 4, \(L\subseteq N[v]\cup N_2(v)\).  If \(t\) neighbours of \(v\)
   have degree five, triangle-freeness and the degree cap give
   \[
     |L|\le1+t+4t+5(5-t)=26.
   \]
   (`4t+5(5-t)` is an upper bound with overlaps ignored.)
6. `S2`
   -> \(|V(G)|\ge33\)
   -> steps 3--5 give at least seven degree-six vertices (also if \(L\) is
   empty).
7. Take a 6-critical subgraph \(H\subseteq G\).  Vertex-criticality of \(G\)
   forces \(H\) to be spanning.  By `S4 + triangle-free`, every nontrivial
   block of the subgraph induced by the degree-five vertices of \(H\) is
   either an edge or an odd cycle of length at least five.  Separately, the
   handshake lemma gives \(|L|\equiv0\pmod2\) for the degree-five set of
   \(G\), since the other vertices of \(G\) have degree six.
8. `S5 + triangle-free` -> if \(n=|V(H)|=|V(G)|\) and \(h_H\) is the number
   of degree-six vertices of \(H\), then
   \[
      \frac{5n+h_H}{2}=|E(H)|
      \ge \left(\frac{14}{5}+\frac1{1050}\right)n-\frac95,
   \]
   and hence
   \[
      h_H\ge \left\lceil\frac{316n-1890}{525}\right\rceil.
   \]
   Every degree-six vertex of \(H\) also has degree six in \(G\).  At the
   first possible order \(n=33\), this sharpens step 6 to at least 17
   degree-six vertices in \(G\), hence \(|L|\le16\).  This is
   still only a necessary condition.
9. For a degree-five vertex \(v\), any 5-colouring of \(G-v\) uses each
   colour exactly once on \(N(v)\).  For any pair of colours, the two
   corresponding neighbours lie in one connected component of the induced
   bichromatic graph; otherwise a Kempe swap frees a colour for \(v\).
   Hence every pair is joined by an alternating path and with \(v\) gives an
   odd cycle of length at least five.

Steps 1--9 are necessary conditions, not a contradiction.

## Partition route

10. **D23 (proved elementary decomposition)**: every graph with
   \(\Delta\le6\) has a partition \(V=A\sqcup B\) with
   \(\Delta(G[A])\le2\) and \(\Delta(G[B])\le3\).  Proof: minimize
   \(4|E(G[A])|+3|E(G[B])|\); moving a vertex that violates either degree
   bound strictly decreases this integer potential.
11. For triangle-free \(G\), every component of \(G[A]\) is a path or a cycle
   of length at least four.  If all its cycle components are even, then
   \(G[A]\) is bipartite (two colours), while `S1` gives
   \(\chi(G[B])\le3\); therefore \(\chi(G)\le5\).
12. **C001 (unproved)**: D23 can always be chosen with no odd-cycle component
    in \(G[A]\).
13. `C001 + steps 10--11` -> `F1`.

14. **C001 minimum-degree reduction (proved)**: a vertex-minimal
    counterexample to C001 has minimum degree at least two.  An isolated
    deleted vertex can be put in \(A\).  If a deleted leaf's neighbour lies in
    \(A\), put the leaf in \(B\); if its neighbour lies in \(B\), put the leaf
    in either side of \(A\).  In each case the new vertex has no neighbour in
    its own induced part, so no old induced degree changes.
15. **Naive stronger induction refuted.**  The eight-vertex tree in
    `data/false-fixed-partition-extension.json` has a displayed C001 partition
    after deleting a degree-two vertex \(v\), but no assignment of only \(v\)
    to \(A_0,A_1\), or \(B\) extends that fixed partition: one choice creates
    a same-side \(A\)-edge, one raises an old \(A\)-degree from two to three,
    and one raises an old \(B\)-degree from three to four.  The full tree has a
    different C001 partition, so this refutes only fixed-partition induction,
    not C001.  Any stronger minimum-degree reduction needs a multi-vertex
    recolouring theorem.

The only open dependency on this route is C001.  Finite SMT and random
certificates support it only on the scopes recorded in `data/`; they do not
close step 12.  The lazy CEGIS run in `data/c001-cegis-block02.json` excludes
only the minimum-degree-at-least-five stratum at order 11; the unrestricted
order-11, proved minimum-degree-two order-11, and restricted order-12 runs
failed to finish; a sound degree-ordered minimum-degree-two variant also
returned `unknown`.  Thus exhaustive solver evidence remains only through
order 10.

## Refuted stronger route

16. **H2 (false)**: every triangle-free graph with \(5\le\delta\le\Delta\le6\)
    has an independent set \(I\) with at least two neighbours in \(I\) for
    every vertex outside \(I\).  H2 would imply F1 because \(G-I\) would have
    maximum degree at most four.
17. `data/false-independent-2dom.json` + exhaustive verifier
    -> exact 16-vertex counterexample to H2.  This graph is 3-colourable, so it
    does not refute F1.

No node reaches a proved or disproved endpoint for F1.
