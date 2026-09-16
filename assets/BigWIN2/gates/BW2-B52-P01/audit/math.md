# Fresh mathematical audit

## Frozen scope and integrity

I reviewed the frozen `resolution-paper` claim that
\(\eta(K_{1,1,5})=15\), in the full sense of minimization over all finite
abelian host groups and all symmetric connection sets.  I verified all ten
hashes in `audit/snapshot.json` against the current files and independently
recomputed the canonical snapshot digest
`d7bc99d35546d541722d838ac67c5f9e7f9000ba86bbbd02132c3def8b628b79`.
The snapshot is internally consistent.

## Reconstruction of the lower bound

Write the two singleton vertices as \(a,b\) and the independent part as
\(C\), with \(|C|=5\).  The cited Theorem 6 applies because \(C\) is an
independent subset of \(N(a)\).  Its relevant argument is also short enough
to check directly: after translating \(f(a)\) to zero, the five labels in
\(f(C)\) lie in the connection set.  For any fixed nonzero label \(s\) among
them, \(f(C)\) and \(f(C)+s\) are disjoint, since an intersection would make
two distinct vertices of \(C\) adjacent.  Thus the host has at least ten
elements.  This proves the claimed floor without relying only on the theorem
label.

The finite-abelian-group classification gives exactly the following host
types at orders 10 through 14:
\[
\mathbb Z_{10},\quad \mathbb Z_{11},\quad \mathbb Z_{12},\quad
\mathbb Z_2\times\mathbb Z_6,\quad \mathbb Z_{13},\quad \mathbb Z_{14}.
\]
In particular, order 12 has precisely the cyclic and noncyclic types listed;
the other five orders each have one type.

For an arbitrary labeling, translation legitimately fixes \(f(a)=0\).
Then \(f(b)\) ranges over every nonzero group element, and the image of the
five interchangeable vertices in \(C\) ranges over every five-subset of the
remaining elements.  Hence the enumeration covers exactly
\((n-1)\binom{n-2}{5}\) normalized labelings.  If \(D_E\) and \(D_N\) are
the symmetrized edge- and nonedge-difference sets, respectively, a symmetric
connection set exists if and only if \(D_E\cap D_N=\varnothing\).  Necessity
is inducedness; for sufficiency, take \(S=D_E\).  Injectivity ensures that
zero is not introduced into this set.

Inspection of `evidence/enumerate_embeddings.py` confirms that it implements
exactly these quantifiers and this criterion.  I reran it and obtained a
byte-for-byte match with `evidence/enumeration-log.json`.  I also performed a
separate exact enumeration using inverse-orbits of differences rather than
the submitted oriented-difference-set routine.  The independently obtained
counts were:

| group | labelings | valid | minimum number of colliding inverse-orbits |
|---|---:|---:|---:|
| \(\mathbb Z_{10}\) | 504 | 0 | 1 |
| \(\mathbb Z_{11}\) | 1,260 | 0 | 3 |
| \(\mathbb Z_{12}\) | 2,772 | 0 | 1 |
| \(\mathbb Z_2\times\mathbb Z_6\) | 2,772 | 0 | 1 |
| \(\mathbb Z_{13}\) | 5,544 | 0 | 2 |
| \(\mathbb Z_{14}\) | 10,296 | 0 | 1 |

Thus all 23,148 normalized possibilities are excluded, and together with the
order floor this proves \(\eta(K_{1,1,5})\geq 15\).

## Reconstruction of the upper bound

In \(\mathbb Z_{15}\), the proposed labels are
\(f(a)=1\), \(f(b)=2\), and \(f(C)=\{0,3,6,9,12\}\), while \(S\) is the set
of residues not divisible by three.  All internal differences in \(C\) are
nonzero multiples of three.  The difference between the singleton labels is
\(1\), and every singleton-to-\(C\) difference is nonzero modulo three.
Consequently precisely the eleven graph edges have differences in \(S\),
and precisely the ten pairs inside \(C\) do not.  The labels are distinct,
zero is absent from \(S\), and \(S=-S\).

I reran the supplied direct witness verifier and reproduced
`evidence/order15-verification.json` byte for byte.  I also separately checked
all 21 unordered pairs from the serialized witness.  Hence the upper
certificate proves \(\eta(K_{1,1,5})\leq15\).

## Source comparison and contribution

Definition 1 in the supplied paper matches the invariant used by the claim.
Theorem 6 gives the local floor used above, and Remark 12 states the bracket
10 to 15 for \(K_{1,1,5}\), says only the obvious order-10 refinement fails,
and leaves unbalanced complete-multipartite values open.  The candidate closes
all intervening abelian host types rather than only cyclic hosts, so it settles
the exact frozen original question and is not a toy restriction or a partial
result.

There is a bibliographic version issue to correct during writing: although
`source.md` names Noel and Scott and calls the source arXiv v1, the snapshotted
PDF itself names Rigobert Fokam Souop and Laurent Bitjoka and is internally
marked arXiv v2.  `problem.md` already identifies the author correction.  This
does not affect the definitions, Theorem 6, Remark 12, or the mathematical
resolution reviewed here, and the candidate makes no broad priority claim.

## Verdict

**Accept.**  The exact upper certificate and complete exact exclusion of every
finite abelian host group below order 15 establish the frozen equality in its
full scope.  I found no mathematical gap.  The source-version metadata should
be stated accurately in the manuscript, but it is not a defect in the proof.
