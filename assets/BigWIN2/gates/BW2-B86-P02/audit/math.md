# Fresh mathematical referee report

## Frozen scope and integrity

I reviewed the exact `resolution-paper` statement in `claim.json`, scoped to
Pan's Conjecture 3.1 as it appears in arXiv:2407.19745v1 and to the single
parameter `(n,t)=(4,1)`.  I recomputed every SHA-256 hash in
`audit/snapshot.json`; all frozen files match, and canonical serialization of
the file-hash mapping gives the recorded snapshot digest
`c9e75599bce9e0c446f1a7d749b446d1e12b6e9440287282b6290d30951b85a8`.

## Reconstruction of the decisive argument

1. A permutation in `S_4` with exactly one fixed point must restrict to a
   fixed-point-free permutation of the other three points, hence is a
   3-cycle.  Conversely every 3-cycle fixes the fourth point.  Thus `F_1`
   consists of the eight 3-cycles.  Since the elements of `A_4` are the
   identity, the three double transpositions, and the eight 3-cycles, this is
   exactly `A_4 \ V_4` for
   `V_4={1,(12)(34),(13)(24),(14)(23)}`.

2. In Pan's left-Cayley convention, `g` and `h` are adjacent precisely when
   `h g^{-1}` lies in `F_1`.  The fixed points of `h g^{-1}` correspond
   bijectively to coordinates where the tuples for `g` and `h` agree: a fixed
   value `x` corresponds to the coordinate `g^{-1}(x)`.  Therefore this
   Cayley adjacency is exactly Hamming distance three, establishing the
   claimed identification with `A(4,4,3)` without reversing a convention.

3. Because `F_1` is even, adjacency preserves parity.  For two vertices of
   the same parity,

   `g ~ h` if and only if `h g^{-1}` is not in `V_4`,

   which is equivalent to `V_4 g` and `V_4 h` being different cosets.  Each
   parity class has twelve elements and splits into three such cosets of size
   four.  There are no edges within a coset and every possible edge between
   two different cosets.  Hence each parity class induces `K_{4,4,4}` and is
   connected; there are no cross-parity edges.  The two parity classes are
   therefore exactly the connected components, so the graph is
   `2K_{4,4,4}`.  Although `V_4 g` is conventionally called a right coset,
   `V_4` is normal in `S_4`, so it equals `g V_4`; the claim's description as
   left `V_4`-cosets names the same three parts and causes no scope defect.

4. In a connected `K_{4,4,4}`, every independent set lies in one of the
   three parts.  Consequently the inclusion-maximal independent sets are
   exactly those parts.  Every graph automorphism permutes the parts, and the
   kernel is the group of arbitrary independent permutations inside them.
   Conversely all such internal permutations and every permutation of the
   three parts preserve adjacency.  Thus

   `Aut(K_{4,4,4}) = (S_4)^3 semidirect S_3 = S_4 wr S_3`

   in its natural imprimitive action, of order `(4!)^3 3! = 82,944`.  An
   automorphism of the disjoint union must permute its two connected
   components; the kernel is the direct product of their two full
   automorphism groups, and a component swap supplies the full `S_2` action.
   Therefore

   `Aut(A(4,4,3)) = (S_4 wr S_3) wr S_2`

   and its order is `82,944^2 * 2 = 13,759,414,272`.

5. The center of `S_4` is trivial, so `Inn(S_4)` has order 24, while the
   right regular group also has order 24.  The iterated semidirect product in
   Pan's conjecture consequently has order `24 * 24 * 2 = 1,152`.  The
   unequal orders prove that the conjectured group cannot be the full graph
   automorphism group at this parameter.  Since Conjecture 3.1 quantifies over
   every admissible `n` and fixed-point count, this one parameter disproves
   that universally quantified v1 statement.

## Independent checks and attacks

I performed a fresh standard-library enumeration directly from the
arrangement-graph rule, rather than re-running the submitted Cayley-graph
program.  On all 24 permutation tuples I joined exactly those pairs at
Hamming distance three.  The independent check found degree 8, two connected
components of size 12, and in each component three nonadjacency classes of
size four with all cross-class pairs adjacent.  Each component had 48 edges.
Independent integer evaluation gave the orders `82,944`, `13,759,414,272`,
and `1,152` above.  These checks agree with the frozen certificate while
using a different adjacency construction.

The proof has no division, limiting argument, compactness step, excluded
degenerate case, or external classification theorem.  `F_1` is nonempty,
inverse-closed, and excludes the identity, so the Cayley graph is a simple
undirected graph.  The component and maximal-independent-set arguments cover
all graph automorphisms, including those far outside the normalizer of a
regular Cayley action.

## Source comparison and limitations

I checked the live official arXiv record and HTML during this review.  The
record still lists only v1 (submitted 29 July 2024).  Its Cayley convention is
the one used above; Conjecture 3.1 ranges over all `n>2` and
`0 <= k <= n-2`, gives the iterated semidirect-product formula used in the
comparison, and contains no connectedness or generation hypothesis.  Its
Theorem 1.2 treats the two extreme arrangement-graph families, not
`A(4,4,3)`.

The later journal full text and priority of this observation remain
unverified in the frozen evidence.  This is not silently promoted to a
novelty claim: the candidate explicitly limits its mathematical conclusion
to the frozen arXiv v1 statement and expressly disclaims priority and any
claim about what the inaccessible journal version says.  That literature
limitation therefore does not create a gap in the exact resolution submitted
for review.

## Verdict

**Accept.**  The frozen statement matches the original requested parameter,
the elementary proof establishes every part of the graph decomposition and
the full automorphism group, and the order comparison rigorously disproves
Pan's Conjecture 3.1 as stated in arXiv:2407.19745v1.  I found no substantive
scope, correctness, or contribution defect in the submitted claim.
