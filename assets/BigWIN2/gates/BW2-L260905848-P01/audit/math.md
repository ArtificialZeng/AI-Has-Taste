# Fresh mathematical referee report

## Verdict

**Accept.** The frozen candidate proves the full statement in `source.md`: the
product is at most (35^3), and equality occurs exactly for three copies of one
full star. The proof is finite and computer-assisted. I found no unresolved
mathematical gap in the submitted scope.

This review is bound to snapshot
`bd51ecf84e603742284f839d6c6b9c001fc2e4d9f4227fe64b12e7f70b3f4521`
and referee job `lit-260905848-p01-referee-bf27a87b311f`. I recomputed all
listed file hashes; they agree with `audit/snapshot.json`. In particular, the
immutable source still has SHA-256
`0e66f97af065e8d995c6efe336a1812c57822a0fd2bfd9d3653518bf563c44ba`.

## Scope reconstruction

The original domain consists of ordered triples
((\mathcal F_1,\mathcal F_2,\mathcal F_3)), where each family is an ordinary
subset of the 3-dimensional linear subspaces of \(\mathbb F_2^5\). The
condition forbids exactly a choice whose common intersection is \(\{0\}\).
The claim in `claim.json` includes both requested conclusions and does not
weaken any quantifier. Empty families cause no difficulty: their product is
zero, while every product violating the bound or attaining (35^3) is
positive.

There are

\[
 {5\brack3}_2=155
\]

3-subspaces. A full star through a nonzero vector (equivalently, through its
1-space over \(\mathbb F_2\)) has

\[
 {4\brack2}_2=35
\]

members. Three copies of such a star are feasible, so (35^3=42875) is
attained.

## Exact finite model

I independently reconstructed the finite model in
`audit/referee_verify_encoding.py`; its durable result is
`audit/referee_encoding_replay.json`.

1. I enumerated 3-spaces independently as the distinct 8-element spans of
   independent triples of nonzero binary vectors. The resulting set has 155
   elements and agrees exactly with the spaces represented by the submitted
   RREF bases.
2. For every one of the (155^3=3,723,875) ordered triples, I recomputed the
   three mask intersection. It contains only zero precisely when its bit count
   is one. I compared the resulting lexicographic stream record by record with
   `forbidden_triples_u8.bin`; all 2,499,840 forbidden triples, and no others,
   occur in that file.
3. I reconstructed the Boolean insertion sorters from their gate equations.
   Each comparator's high output is exactly the disjunction of its inputs and
   its low output is exactly their conjunction. Thus output position (j) is
   true exactly when the family has at least (j+1) members.
4. I then regenerated the expected clauses semantically and compared them in
   order with every clause of both frozen DIMACS files. All 2,718,299 clauses
   of `product_above_bound.cnf` and all 2,715,035 clauses of
   `nonstar_equality.cnf` matched. Their hashes also matched the snapshot.

This closes the possible gap between an UNSAT certificate and the mathematical
statement encoded by its input CNF.

## Losslessness of the normalizations

For a positive product, permuting the three family labels permits
(a\ge b\ge c\ge1). The submitted unary implications encode exactly these
cardinality inequalities. Simultaneous action by \(\mathrm{GL}(5,2)\) is
transitive on the 155 3-spaces, so a selected member of the first family can be
sent to vertex 0. The stabilizer of vertex 0 has exactly three orbits on
3-spaces, distinguished by intersection dimension 1, 2, or 3. Exhaustive
replay enumerated all 64,512 stabilizer maps and obtained orbit sizes 112, 42,
and 1 with representatives 13, 1, and 0. Hence a selected member of the second
nonempty family can be sent to one of those three representatives. The CNF
requires at least one corresponding membership bit, exactly as needed; it does
not assume that the representative is unique. Undoing these transformations
preserves feasibility, cardinalities, and the common-star property.

The replay result `audit/referee_reduction_replay.json` is byte-for-byte equal
to the frozen `evidence/reduction_audit.json`.

## Product bound

On the complete sorted cube (1\le c\le b\le a\le155), I recomputed the 829
componentwise-minimal triples whose upward closure is exactly

\[
 abc\ge42876.
\]

For each boundary triple, the product CNF has a Tseitin variable equivalent to
the conjunction of the three relevant exact unary thresholds, followed by a
clause requiring at least one boundary term. Therefore this CNF is satisfiable
exactly when a normalized feasible triple has product greater than 42875.

I reran the recorded `drat-trim` executable, whose SHA-256 is
`9d9c6f706cc5ad81f569ac429faf0c3269c5806c7be0ac936af9c2d1daa7260f`,
on the frozen CNF and binary DRAT trace. It returned exit code zero and
`s VERIFIED`, with 325,972 input clauses and 418,136 lemmas in the core and
603,299,890 resolution steps. Thus the product CNF is unsatisfiable, proving
the upper bound.

## Equality classification

I exhaustively recomputed the possible sorted positive size triples with
product 42,875 and bounds at most 155. They are exactly

\[
 (35,35,35),\qquad(49,35,25),\qquad(125,49,7).
\]

The equality CNF imposes a disjunction of these three exact cardinality
patterns. For each of the 31 nonzero vectors, its additional 465-literal clause
is false on exactly one membership assignment: all three families equal the
complete star through that vector. Thus the 31 clauses exclude exactly the 31
common full-star triples and do not exclude a merely similar or partially
star-shaped assignment.

I independently replayed the second frozen DRAT trace. The checker returned
exit code zero and `s VERIFIED`, with 208,823 input clauses and 239,171 lemmas
in the core and 183,039,602 resolution steps. The exact replay data for both
certificates is in `audit/referee_certificate_replay.json`. Consequently no
feasible non-star equality assignment exists after normalization. Since a
common full-star triple is invariant under family permutation and maps to a
common full-star triple under an invertible simultaneous linear map, the same
classification holds before normalization. Together with the explicit
attaining construction, this proves the claimed if-and-only-if statement.

## Source comparison and limits

I checked the two cited primary arXiv sources at the stated theorem locations.
Li--Lv--Wen Theorem 1.1 assumes
(n\ge \frac r{r-1}(k_1+t)+1), which becomes (n\ge7). Shimizu--Tokushige
Theorem 3 assumes (n\ge2k), which becomes (n\ge6), and their reduction from
pairwise cross-intersection therefore does not cover (n=5). Their conjecture
does contain the present parameters and the same product and equality forms.
The candidate resolves only the frozen (q=2,r=3,t=1,k=3,n=5) instance and
makes no priority, exhaustive-literature, or broader-parameter claim. The
scope correction in `problem.md` concerning the word "first" is therefore not
part of the mathematical claim being accepted.

The result depends on inspectable finite encodings and checked DRAT
certificates rather than a human-only derivation. That dependence must remain
plainly disclosed in any manuscript, but it is not an unresolved gap in this
computer-assisted candidate.
