# Fresh mathematical referee report

## Frozen scope

I reviewed the snapshot with digest
`c5f1e62a049fce465ab916b073461beaad8518073bcbd66f71dc04fda337b8c8`
for the exact claim in `claim.json`.  The claim is a full-scope computational
resolution of the immutable question: every connected simple graph on eight
vertices, every relevant degree, and every Schur coefficient are included.
No smaller or modified claim is being substituted.

For a connected graph on eight vertices, the formula recorded in `problem.md`
has homogeneous pieces only in degrees 0 through 7.  It is therefore enough to
check `d=1,...,7`; for `d>=8`, both terms in the asserted log-concavity
difference vanish.  For a fixed `d`, checking all partitions of `2d` checks the
entire Schur expansion, including coefficients absent from the sparse internal
representation.

## Reconstruction of the decisive computation

The graph enumeration is exhaustive.  The graph atlas supplies an isomorphism
representative for every seven-vertex graph, including disconnected graphs.
Given any connected eight-vertex graph `G` and any vertex `v`, the graph `G-v`
is isomorphic to an atlas representative and `v` has a nonempty neighborhood.
Transporting that neighborhood across the isomorphism produces `G` among the
127 extensions of that representative.  The implementation retains an
extension only when no exactly isomorphic graph has already been retained in
the same invariant bucket.  Sorted degrees, sorted triangle counts, and the
unattributed Weisfeiler--Lehman graph hash are isomorphism invariants, so
isomorphic graphs cannot be separated into different buckets; NetworkX's exact
`is_isomorphic` test, rather than the hash, decides equality of classes inside
a bucket.  Thus the retained list has exactly one representative of every
class.  The run considered 119,980 connected extensions and retained 11,117
classes.

I reconstructed the symmetric-function recurrence from the definitions.  Let
`A[S,k]` be the sum of the products of the component functions over partitions
of `S` into `k` nonempty connected induced blocks.  For `k>=2`, the block
containing the least vertex of `S` is a unique proper connected subset `B`, so

`A[S,k] = sum_B M_(G|B) A[S-B,k-1]`.

Processing subsets by increasing cardinality makes this an induction, with
the empty-partition and singleton bases explicitly initialized.  For connected
`S`, the implementation then applies the frozen source formula

`M_(G|S) = -sum_(k=2)^|S| h_(k-1) A[S,k]`,

and obtains `F_(G,d)=A[V,8-d]`.  The submask loop excludes the whole block when
forming the `k>=2` entries, and the singleton case is handled separately, so
there is no circular call or empty-block contribution.

Products are computed over the integers in the complete-homogeneous basis.
The conversion `h_mu` to Schur functions successively applies Pieri's rule;
the code's containment and interlacing test is exactly the horizontal-strip
condition.  For each `d`, it explicitly inserts zero for every partition of
`2d` not present in the sparse Schur dictionary before taking the minimum.
At `d=7`, the missing degree-eight part is correctly treated as zero.  Hence a
reported strictly positive minimum certifies every coefficient, rather than
only stored nonzero terms.  There is no floating-point arithmetic.

## Checks performed

All file hashes in `audit/snapshot.json` matched their current bytes.  I ran a
fresh complete replay of `evidence/eight_vertex_scan.py` under Python with
NetworkX 3.4.2.  It regenerated all 11,117 records in 132.316 seconds.  The
record file was byte-for-byte identical to the frozen 12,577,195-byte JSONL
file, with SHA-256
`08142d763b01d1c160a94bdc2caf30d9755c594f5ffa798bd281f86a5d89db65`.
Every summary field except elapsed time was identical.

I also parsed all frozen records afresh and decoded every graph6 string.  The
checks found 11,117 unique encodings, each decoding to a connected graph on
eight vertices; recorded edge counts and chordality flags agreed with fresh
computations; indices were consecutive; and every record contained exactly
degrees 1 through 7 with the expected partition counts.  The split was 1,614
chordal and 9,503 nonchordal classes.  Across 3,268,398 tested coefficients,
the global minimum was 1.  The per-degree minima were
`7,158,490,490,196,28,1` for chordal graphs and
`18,288,1176,1695,946,186,9` for nonchordal graphs.

As a definition-level regression check, I reran
`evidence/p3_exact_check.py`.  Its direct construction of the finite
two-variable multiweighted bond poset and its separate bond-partition
recurrence agreed exactly.  They give
`L_(P3,1)=3 s_(2)+2 s_(1,1)`.  This also confirms the convention used by the
large recurrence directly from the defining poset; the contrary swapped
coefficients printed in the cited source example are an example-level error,
not an ambiguity introduced by the eight-vertex computation.

## Source comparison and limitations

The frozen source statement reports exhaustive verification only through
seven vertices.  The candidate's complete eight-vertex layer is therefore the
precise next finite layer.  The source's chordal elementary-positivity theorem
for individual signed homogeneous pieces does not imply the Schur positivity
of their log-concavity differences, so the 1,614 chordal cases have not been
silently counted as already settled; they were computed and reported
separately from the 9,503 nonchordal cases.

This review was confined, as instructed, to the frozen snapshot and its listed
evidence.  I did not perform a new external literature search.  Accordingly,
the bounded literature statement in `problem.md` remains a search report dated
2026-09-06, not a priority guarantee.  This limitation does not leave a gap in
the mathematical resolution of the frozen eight-vertex claim.

## Verdict

**Accept.**  The quantifiers and boundary degrees are fully covered, the graph
enumeration is exhaustive up to isomorphism, the symmetric-function and Schur
arithmetic are exact, and the complete fresh replay reproduces the positive
certificate.  I found no unresolved correctness or scope gap in the frozen
candidate.
