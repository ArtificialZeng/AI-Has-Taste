# Exact classification result

## Theorem submitted for review

For the fixed labelled graph in `source.md` and the canonical convention in
`problem.md`, the family

\[
\mathcal B_5(G)=\{F\in\tbinom{E(G)}5:\gamma(G-F)>6\}
\]

has exactly 801 labelled members and exactly 140 orbits under
\(\operatorname{Aut}(G)\).  Every member satisfies \(\gamma(G-F)=7\).
There are 127 orbits of size 6 with setwise stabilizer order 1 and 13 orbits
of size 3 with setwise stabilizer order 2.  The complete exact answer is the
`orbits` array in `evidence/bondage5_classification.json`: each record gives
the lexicographically canonical five-edge representative, its domination
number, orbit size, one size-7 dominating witness, and the complete list of
setwise-stabilizing vertex permutations.  That JSON also gives all six
automorphisms and all 801 qualifying labelled edge-index sets.

## Exhaustive proof and certificate construction

The first implementation, `evidence/enumerate_bondage5.py`, uses standard
library integer bitsets.  Exhaustion of all vertex subsets gives zero
dominating sets in sizes 0 through 5 and exactly 297 in size 6, so
\(\gamma(G)=6\).

For each of the 297 base-graph size-6 dominators \(D\), and each
\(v\notin D\), the program forms the nonempty edge set
\(C_{D,v}=\{vd\in E:d\in D\}\).  After deleting \(F\), the same \(D\)
dominates if and only if no \(C_{D,v}\) is contained in \(F\).  This is an
exact equivalence: vertices of \(D\) dominate themselves, while an external
vertex remains dominated precisely when at least one of its edges into
\(D\) remains.  The program applies this test to every one of the
\(\binom{27}{5}=80{,}730\) edge sets.  It finds exactly 801 with no size-6
dominator.  Deleting edges cannot lower a domination number, and an exhaustive
size-7 search supplies a dominating witness for each of those 801 graphs;
hence all 801 values are exactly 7.

An adjacency-equivalence backtrack exhausts all vertex bijections and obtains
exactly six automorphisms.  Acting with all six on the 801-set family produces
the 140 canonical records.  For each record, the code explicitly checks the
setwise stabilizer and
\(|\operatorname{Orb}(F)|\,|\operatorname{Stab}(F)|=6\); the orbit sizes sum
to \(127\cdot6+13\cdot3=801\).

## Independent replay

`evidence/verify_bondage5.py` does not use the critical-edge test.  It rebuilds
each of the 80,730 deleted graphs, computes its closed neighborhoods, and
directly unions them for all relevant six-vertex sets.  It independently finds
the same 801 masks, with SHA-256
`d84f0d0011e2a07f214f2f80db42aa048ab40f0d452419867ce586c71744c589`,
and directly finds a size-7 dominator for every one.

The replay also computes the all-pairs graph-distance matrix and exhausts its
bijective isometries.  This is a complete independent automorphism test because
a graph automorphism preserves all distances, while a distance-preserving
bijection preserves adjacency (distance one).  It obtains the same six
permutations and reconstructs every canonical representative, orbit size, and
stabilizer list.  The machine-readable successful replay is
`evidence/bondage5_verification.json`.

The cited paper copied to `evidence/external/2609.04257.pdf` has the exact
SHA-256 stated in `source.md`.  It supplies the fixed graph and earlier facts
\(\gamma(G)=6\), \(b(G)=5\), but the inspected source does not give this
complete five-edge orbit classification.  No broader priority claim is made.
