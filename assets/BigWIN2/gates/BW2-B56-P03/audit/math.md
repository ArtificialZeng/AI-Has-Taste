# Fresh mathematical referee report

## Frozen scope and integrity

I reviewed the exact `resolution-paper` claim frozen by snapshot
`f799fc924c3fa972528c1b744ca78acb22a0c2f5611d79df27f9bc1d1018948c`.
It concerns all zero-dimensional Borel-fixed monomial ideals of colength 15 in
\(\mathbb C[x,y,z]\), with the fixed order \(x<y<z\), and only those ideals.
The asserted maximum is 81, with four specified equality cases, and the best
case with \(m_1\leq 2\) is asserted to have dimension 69. No assertion about
non-Borel points is part of the claim.

I recomputed the SHA-256 digest of every file in `audit/snapshot.json`. Every
digest matched the snapshot, including the immutable `source.md` digest
`488760e5c9a3b14b4faa7f66c512041b56bedb96e7241f36f63db3895fe5e996`.

## Reconstruction of the finite domain

For an ideal in the frozen scope, its 15 standard monomials form a
coordinatewise downset \(O\subset\mathbb N^3\). Strong stability of the ideal
is equivalent to closure of \(O\) under moving one unit from \(x\) to \(y\) or
\(z\), and from \(y\) to \(z\). Thus the proposed atlas is an exact finite
encoding of the domain if and only if it contains every 15-element set with
these closure properties exactly once.

I checked the two completeness arguments in `enumerate_borel15.py`.

1. Adding every available outer corner generates every finite downset:
   deleting a coordinatewise maximal point from any nonempty finite downset
   gives the reverse induction. Filtering by all three standard-set Borel
   moves therefore retains exactly the desired sets.
2. The second enumeration takes unions of the closures forced by coordinate
   predecessors and the Borel moves. Every closed target is the union of the
   one-point closures of its elements. The total-degree bound \(d\leq14\) is
   complete because a point of degree \(d\) forces a coordinate chain of
   \(d+1\) standard points. Hence pruning only sets of size greater than 15
   cannot remove a target.

Both constructions give the same canonical set of 107 records, not merely
the same count. I also performed a third census from a different finite
encoding. Slice \(O\) by the \(z\)-exponent. A slice is encoded by a strict
partition \(\lambda^c\), where strictness is exactly the within-slice
\(x\)-to-\(y\) Borel condition. Consecutive slices obey, for every row \(i\),

\[
\max(\lambda^c_i-1,\lambda^c_{i+1})
\leq \lambda^{c+1}_i\leq\lambda^c_i.
\]

Enumerating all compatible strict-partition sequences of total size 15
produced 107 sets. Their symmetric difference with the frozen atlas was
empty in both directions. On every atlas record I separately checked
cardinality 15, the origin, all coordinate predecessors, all Borel moves,
the minimal-generator boundary, and the pure-power tuple. There were no
failures. These checks establish completeness, absence of duplicates, and
correct recovery of the minimal generators.

## Reconstruction of the tangent calculation

Let \(g_1,\ldots,g_s\) be the minimal generators and \(A=R/I\). The Taylor
relations

\[
\frac{\operatorname{lcm}(g_i,g_j)}{g_i}e_i-
\frac{\operatorname{lcm}(g_i,g_j)}{g_j}e_j
\]

generate the kernel of \(\bigoplus_i Re_i\to I\). Therefore a tuple in
\(A^s\) defines an element of \(\operatorname{Hom}_R(I,A)\) exactly when it
annihilates all these relations. Expansion in the 15 standard monomials
gives a matrix with integer entries. Its nullity over \(\mathbb Q\) is its
nullity over \(\mathbb C\).

I rebuilt these matrices directly from the frozen atlas and computed their
exact rational ranks for all 107 records. Every rank and nullity agreed with
`borel-tangents-15.jsonl`; there were zero discrepancies. I also rebuilt the
Eliahou--Kervaire relations for all records and counted the unpinned
components of the resulting equality graph. This second exact calculation
again agreed on all 107 dimensions. The separately supplied extrema
verifier imports none of the primary tangent implementation and agrees on
the five decisive records.

The exact decisive ranks are:

| Atlas id | \(m\) | Variables | Rank over \(\mathbb Q\) | Nullity |
|---|---:|---:|---:|---:|
| `ee15bf030546148d` | \((3,3,5)\) | 150 | 69 | 81 |
| `ddf69a6eddf5b96d` | \((3,3,6)\) | 150 | 69 | 81 |
| `4f8d65beca9235f3` | \((3,4,4)\) | 165 | 84 | 81 |
| `a9efd314748d5f68` | \((3,4,5)\) | 165 | 84 | 81 |
| `b81dda0d28a57052` | \((2,4,5)\) | 135 | 66 | 69 |

The complete recomputed dimension histogram is

\[
45^{(27)},51^{(8)},53^{(11)},55^{(5)},57^{(8)},59^{(10)},
61^{(7)},63^{(10)},65^{(4)},67^{(5)},69^{(1)},75^{(7)},81^{(4)}.
\]

Consequently 81 is the global maximum on the complete atlas and exactly the
four listed records attain it. Direct comparison with the atlas confirms
that their minimal generating sets are exactly those printed in
`claim.json`. The 96 records with \(m_1\leq2\) have maximum 69, attained only
by `b81dda0d28a57052`, whose generators also match the claim. Since all four
global maximizers have \(m_1=3\), the frozen necessary condition follows.

## Source comparison and limitations

I checked the supplied Rezaee--Saberi primary PDF. Its definition of
Borel-fixedness matches the convention used here, and its Theorem 5.1 proves
Conjecture B only for degree families (0.1)--(0.3). At \(k=3\), those families
cover \(10,11,12,13,14,16,17,18,19\), leaving 15 outside that theorem. The
bounded literature record reports a prior candidate of dimension 81 and the
stratum maxima \(45,69,81\); the new exact census agrees with those values and
adds the complete atlas and all four equality cases. The other underlying
papers summarized in that record were not included as frozen source files,
so I do not treat the record as proof of priority. This does not enlarge the
claim: `claim.json` expressly makes no priority claim over unsearched
literature.

The proof is a Borel-only finite classification. It neither computes the
maximum among non-Borel points nor claims that the four Borel points are
globally most singular on the full Hilbert scheme. This limitation is stated
correctly and is consistent with the immutable problem. I found no empty
case, variable-order ambiguity, field/rank mismatch, missing equality case,
or unsupported limiting argument.

## Verdict

**Accept.** The exact frozen scope is fully proved: the atlas is complete,
the tangent dimensions are exact and independently reproducible, the maximum
and all equality cases are classified, and the claimed \(m_1=3\) consequence
follows. No substantive mathematical revision is required.
