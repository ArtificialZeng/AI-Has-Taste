# Proof dependency graph

## Endpoint

**T0.** The simple Pasch-switch quotient graph on the 80 isomorphism
classes of STS(15) has 258 edges and components of orders 79 and 1.  The
79-vertex component has diameter 11 (and radius 6); the isolated component
has diameter 0.

## Dependencies

- **L1 — Valid seeds.**  The 35 triples from the nonzero vectors of
  \(\mathbf F_2^4\) form the projective STS(15), and the Bose construction
  over \(\mathbf Z_5\times\mathbf Z_3\) forms an STS(15).  Exact pair
  coverage checks pass; the latter has zero Pasches.
- **L2 — Equivariance.**  Point relabeling maps Pasches to Pasches and
  commutes with switching.  Hence all quotient neighbors of a class are
  obtained by switching every Pasch in one representative.
- **L3 — Constructed universe.**  Canonical closure of the projective seed
  under all Pasch switches has 79 classes; adjoining the Bose anti-Pasch
  class gives 80.
- **L4 — Classification cross-check.**  The 80 canonical incidence graphs
  in L3 equal, as a set, the 80 records in the complete
  DesignTheory.org STS(15) catalogue (compressed input SHA-256
  `11310c7e35330e842938dbcc4bb6e59144bf40576323f22499a809364d50f2c9`).
  Completeness ultimately invokes the classical STS(15) classification.
- **L5 — Independent vertex audit.**  The no-nauty verifier checks all
  80 systems have 35 blocks and cover each of the 105 pairs exactly once.
  Their sorted 15-tuples of point-Pasch incidence counts are all distinct,
  which proves pairwise nonisomorphism.
- **L6 — Independent Pasch audit.**  Discovery scans all four-block
  subsets.  Certification instead decomposes the union of the two derived
  matchings for every point pair and selects its 4-cycles.  Both give 1,390
  Pasch occurrences, with the published 1999 count multiset and a unique
  zero.
- **L7 — Complete quotient edge reconstruction.**  For each of the 1,390
  occurrences the verifier forms the exact four-block mate, checks pair
  coverage, and finds an explicit Steiner-quasigroup isomorphism to the
  uniquely signature-matching representative.  Removing 83 self-switch
  occurrences and deduplicating parallel targets gives exactly 258
  undirected nonloop edges; every edge is witnessed from both directions.
- **L8 — Exact graph metric.**  Standalone all-pairs BFS on the 258-edge
  file gives components \(79+1\).  The maximum finite distance is 11,
  attained exactly by `V000–V006` and `V000–V028`.  The distance row
  from `V000` contains no value above 11 and contains value 11 at those
  two vertices.  A stored 12-vertex geodesic proves the matching lower
  bound.

Dependencies: L1 + L2 → L3; L3 + L4 + L5 → complete vertex universe;
L2 + L5 + L6 → L7; L7 + L8 → T0.

## Trust boundary

No floating point, randomness, optimizer, SAT solver, or proof assistant is
used.  nauty is used only during discovery/canonical naming.  The decisive
verifier does not import the discovery module and does not invoke nauty.
The only external mathematical dependency is completeness of the classical
80-class STS(15) classification, cross-checked against the current complete
catalogue.
