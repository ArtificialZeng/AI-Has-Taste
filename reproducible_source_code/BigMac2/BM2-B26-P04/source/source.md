# bigMac-00026-p04 — a 13-vertex witness for `R_vm(5)`

## Immutable source statement

For a simple graph `G`, let `[G]_{LC}` be its local-complementation orbit and
\[
\beta(G)=\max_{G'\in[G]_{LC}}\alpha(G').
\]
Determine whether there exists a simple graph on exactly 13 vertices such
that `beta(G)<=4`. Equivalently, determine whether some 13-vertex graph does
not contain the edgeless graph `E_5` as a vertex-minor.

An affirmative answer requires an explicit graph6 string, complete exact BFS
enumeration of its local-complementation orbit, canonical duplicate handling,
and an independent exact check that every orbit member has independence
number at most four. A failed witness search proves nothing. Exhaustive
classification of all 13-vertex graphs is outside this frozen target.

## Source and status boundary

- Primary source: Ji Ho Bae, *Vertex-Minor Ramsey Numbers: Exact Values and
  Extremal Structure*, arXiv:2604.13434v1, Conjecture C, Definition 2.4,
  Proposition 2.5, Corollary 6.3, and Sections 6.5--7.
- Local primary PDF: `batches/literature/bigMac-26/2604.13434v1.pdf`,
  SHA-256
  `b9b69284f1862720e3adb6400fb670a6383079635f489d655f2b89b2a89266ea`.
- The source proves `R_vm(4)=11`, obtains `R_vm(5)>=13`, and conjectures
  `R_vm(5)=15`. A 13-vertex witness would improve the lower bound to 14.
  The source calls the `k=5` case unresolved, but current status remains
  uncertain pending a fresh candidate-database and literature check.
