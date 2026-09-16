# Fresh mathematical referee report

## Verdict

**Accept** the exact frozen `resolution-paper` claim.  The submitted exact
enumeration proves

\[
\max_{w\in S_9}|\operatorname{RP}(\operatorname{Grid}(w))|=28549,
\]

and its retained equality cases prove the stated strengthening that the only
maximizers in one-line notation are `321456987` and `789654123`.

I reviewed the snapshot with digest
`013dcd017570e4604e0dc22905ad1165b5828740980b2566761f6866968320ad`.
Before review, the SHA-256 digests of `claim.json` and all five listed evidence
files were recomputed and found to agree with `audit/snapshot.json`.

## Reconstruction of the decisive argument

For a permutation grid of order (n), a row whose black square is not on an
edge has two nonempty white runs, while a row whose black square is in the
first or last column has one.  Exactly one row is of each edge type, so there
are (2n-2) across words.  The same argument applied to columns gives
(2n-2) down words.  At (n=9), both word sets therefore have size 16.

Make the bipartite incidence graph whose two vertex classes are the across and
down words and whose edges are their white-square intersections.  Every white
square belongs to exactly one word of each type, and a pair of words has at
most one intersection.  Thus choosing one white square in every across word
and every down word is bijective with a perfect matching in this graph.  The
rook-placement count is consequently the permanent of its (16\times16)
zero-one incidence matrix.

The routine `make_rows` implements this graph exactly.  It assigns separate
IDs to the nonempty runs above and below each column's black square.  For a
white square in row `i` and column `j`, `i < inv[j]` selects the upper run and
the opposite strict inequality selects the lower run; equality cannot occur
because the square is white.  The left and right row loops are exactly the
two possible across runs.  Hence each returned bit mask is precisely one
incidence-matrix row.

After an irrelevant row reordering by degree, `permanent` maintains the
invariant that `cur[s]` is the number of injective assignments of all
processed across words onto exactly the set `s` of down words.  Extending by
each incident unused bit proves the invariant inductively.  The full-mask
entry after all 16 rows is therefore the permanent.  All operations involved
in this count are integer operations.  Every partial-matching count is at most
(16! = 20922789888000 < 2^{64}); the serialized aggregate values are also
below (2^{64}), so the unsigned 64-bit arithmetic used here does not
overflow.

The enumeration begins at the increasing permutation.  On every nonfinal
permutation, `next_permutation` finds the rightmost ascent, swaps with the
least larger suffix value, and reverses the decreasing suffix.  This is the
immediate lexicographic successor.  It stops only at the decreasing
permutation.  Accordingly, the loop covers every element of (S_9) exactly
once, with no symmetry reduction, and the recorded count 362880 equals
(9!).  Updating the maximum and appending every equality case at each visit
therefore establishes both the universal upper bound and the complete
classification.  The exact output gives maximum 28549 and exactly the two
permutations stated in the claim.  Either retained case also supplies the
needed equality witness.

## Checks performed

I ran the frozen program afresh to a separate temporary output.  It exited
successfully, visited 362880 permutations at (n=9), returned maximum 28549
with exactly the two stated maximizers, and produced output byte-for-byte
identical to `evidence/exhaustive-results.json`, including SHA-256 digest
`7f8ccd085ba65e9486e17ae46501f1c20e82e4d5d51a8a0e8dd3194b16411ef2`.

I also wrote and executed an independent in-memory checker for the following
tests.  It constructed the white array directly, found maximal across and
down runs by scanning contiguous white cells, built their incidence masks,
and counted perfect matchings by recursive memoized branching.  This checker:

- exhaustively reproduced the maxima (1,1,1,5,17,73,469,3493) and the
  corresponding maximizer counts (1,2,6,2,2,2,2,2) for every (S_n),
  (1\le n\le8);
- counted 28549 for each of `321456987` and `789654123`; and
- agreed with the submitted plain-Python incidence construction on 256
  deterministic pseudorandom permutations in (S_9).

The full (S_9) result still rests on the audited exhaustive program, not on
the spot checks.  The separate construction and lower-order exhaustive tests
serve to attack matrix-construction, convention, and recurrence errors; the
source-code argument above establishes full coverage.

## Scope, source comparison, and limitations

The frozen original question asks only for (r(9)), and the claim resolves
that exact finite scope rather than a restriction or surrogate.  The
classification of maximizers is a genuine strengthening and is supported by
the same exhaustive pass.  According to the frozen source statement and
source comparison in `problem.md`, Lewis--Won report exhaustive maxima only
through (n=8), while their layered construction supplies the lower bound
28549 at (n=9).  The submitted computation adds the missing exhaustive upper
bound.  Under the job's restriction to the snapshot-listed files, I did not
perform a new external literature search; I therefore make no broader priority
claim beyond this comparison.

There is one non-decisive factual error in `evidence/exhaustive-proof.md`: the
two displayed maximizers are said to be related by a half-turn.  Directly,
the half-turn action on a permutation is
(w'(i)=10-w(10-i)), and each displayed permutation is fixed by that action.
They are related to each other by a horizontal or vertical reflection.  This
sentence should be corrected in the eventual manuscript, but it is not part
of the frozen claim and is not used in the enumeration, permanent proof,
equality, or uniqueness argument.  No division, limit, floating-point
comparison, probabilistic coverage assumption, or unverified symmetry
reduction enters the decisive computation.

