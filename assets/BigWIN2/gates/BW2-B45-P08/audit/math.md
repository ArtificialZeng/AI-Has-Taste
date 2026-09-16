# Fresh mathematical referee report

**Job:** `win-00045-p08-referee-83e1a61a96bd`  
**Snapshot:** `0fd2a613b66f5afc39ce421b008c38787d03955b6c1d145a9c993dde1fa12070`  
**Candidate:** `resolution-paper`  
**Verdict:** **accept**

## Frozen scope

The candidate asserts exactly the frozen finite claim: every one of the 254
source-reported non-isomorphic nine-vertex representatives in
\(I_{3,3}\setminus I_{3,1}\) admits five strict total orders for which each
tournament arc has exactly three supporters. This is a positive census of the
specified boundary family. It does not assert a global equality or strictness
result for \(I_{5,1}\) and \(I_{5,3}\), and it does not concern the minimum
order of a non-five-inducible tournament.

All hashes of `claim.json` and its eight enumerated evidence files agree with
`audit/snapshot.json`. The snapshot therefore binds the exact claim, source
statement, interpretation, serialized 254-matrix input, programs, result data,
verification record, and research note reviewed here.

## Reconstruction of the decisive argument

For each serialized \(9\times9\) tournament matrix, the certificate stores the
36 upper-triangle orientations and five lists of the vertices \(0,\ldots,8\).
Each list is a permutation, hence a strict total order. For every unordered
pair \(\{i,j\}\), the matrix chooses exactly one target arc. Direct comparison
of the positions of \(i\) and \(j\) in the five permutations gives exactly
three votes for that target arc. Thus its majority margin is \(3-2=1\), so the
five orders witness membership in \(I_{5,1}\).

This verification is performed for all 36 pairs of each of all 254 matrices,
not for a sample. Membership is invariant under vertex relabelling. It is also
invariant under converse by reversing all five orders, so the normalization in
`problem.md` between isomorphism classes and possible isomorphism/converse
orbits cannot invalidate the positive conclusion.

## Checks actually performed

1. I recomputed the SHA-256 hashes of every frozen file. Every value equals the
   corresponding entry in the snapshot.
2. I wrote and ran `audit/referee_recheck.py`, which imports neither frozen
   research program. It strictly base64-decodes and gzip-decompresses the RDS,
   parses its fixed XDR serialization from the byte-level layout, validates all
   matrix entries and tournament identities, and rejects an unparsed suffix.
   It consumed all 173,778 uncompressed bytes and obtained exactly 254 matrices.
3. The fresh parser independently derived each matrix's 36 orientation bits
   and matched all 254 bitstrings, in order, to the frozen JSON certificates.
   Hence the explicit orders are bound to the pinned serialized input rather
   than merely to adjacencies restated by the producer.
4. The fresh checker verified 1,270 permutations and recounted all
   \(254\cdot36=9{,}144\) target arcs. Every target support was exactly 3. Its
   canonical certificate digest is
   `9980abffc70e05ae3befe908cd623330589e39c7a5c92bc005e599ee498e207e`,
   agreeing with the frozen verifier's value.
5. I reran `evidence/research_pass2_verify.py`. It again returned `PASS`, and
   its exact directed-graph isomorphism tests found no isomorphic pair among
   the 254 matrices after checking all 5,284 degree-compatible candidate pairs.

The fresh results are recorded in `audit/referee_recheck.json`. The proof does
not depend on trusting Z3's SAT reasoning: the five orders are finite witnesses
whose required property is directly recounted. There are no negative solver
answers, limiting arguments, division, compactness, or theorem hypotheses in
the decisive step. Repetition of voters is permitted by the frozen definition,
while every individual order was checked to be a genuine permutation.

## Source comparison, contribution, and limits

The frozen source and precise reading identify the primary paper's prior result
as the 254-class \(I_{3,3}\setminus I_{3,1}\) census and its broader adjacent
margin-layer conjecture. The present certificates add a complete margin-one
five-voter census for precisely that reported family. This resolves the frozen
finite universal question and is more than an isolated example or a routine
restatement of the source census.

The review does not independently reconstruct the much larger enumeration that
selected the 254 source classes; identification of the pinned official RDS as
that reported family is the source/data provenance premise explicitly built
into the frozen question and documented in the enumerated evidence. This does
not weaken the accepted candidate to a smaller family: the accepted scope is
exactly the 254 source-reported representatives. The global relation between
\(I_{5,1}\) and \(I_{5,3}\) remains unresolved, as the claim itself states.

## Verdict

**Accept.** The exact finite witnesses cover the full frozen candidate scope,
the independent byte-to-certificate binding and exhaustive recount establish
correctness, and the contribution is a substantive complete positive census of
the specified first boundary family. The appropriate kind is
`resolution-paper`, with original status `proved`.
