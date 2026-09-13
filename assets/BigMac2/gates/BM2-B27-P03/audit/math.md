# Fresh mathematical audit

## Scope reviewed

I reviewed the frozen `result-note` claim bound to snapshot
`67a9ad102f9c06b2ad1eb8ba87fc50c7e8788ce28044350978f67f60278681dc`.
The claim is only the following finite-length theorem with a global starting
position quantifier: no adjacent factors in the fixed point have equal
normalized Parikh vectors when their total length is at most 2745.  It does
not assert that the original infinite claim is proved.

All files named by the snapshot have the recorded SHA-256 digests.  In
particular, `source.md` remained at
`4bbc9b373dd34a149fe4e10b662d96d60386a356aeced534d189fd9856e08f5c`.

## Reconstruction of the decisive argument

Put (B=14^3=2744).  The first and last symbols of
(b=01213101314310) are both 0, and consecutive symbols within (b) are
unequal.  If consecutive letters (a,c) of a word are unequal, then the
boundary symbols of (h(a)h(c)) are (a,c), while all internal adjacencies
in either image are translates of adjacencies in (b).  Induction, followed
by passage to the nested fixed-point limit, therefore shows that every
adjacent pair of letters in (w) is unequal.

Use the aligned decomposition

\[
w=h^3(w_0)h^3(w_1)h^3(w_2)\cdots .
\]

A factor of length at most (B+1) meets at most two level-3 blocks: even
when it starts at the last position of one block, reaching a third block
would require length (1+B+1=B+2).  A factor contained in one block can be
translated letterwise into a factor of (h^3(0)), which is a block of
(h^4(0)=h^3(b)).  If a factor meets the consecutive blocks
(h^3(a)h^3(c)), then (a\ne c).  For
(d=c-a\pmod 5), the word (b) has an adjacent pair of each possible
nonzero difference:

\[
01,quad 13,quad 14,quad 21
\]

for differences (1,2,3,4), respectively.  The identity
(h^3(r+t)=h^3(r)+t\pmod 5) follows directly from the cyclic definition of
(h).  Hence a common cyclic translation maps
(h^3(a)h^3(c)) to the corresponding literal two-block subword of
(h^4(0)).  It maps the original factor and its internal split to a factor
and split of (h^4(0)).  Such a translation only permutes Parikh
coordinates.

It remains to check all splits of factors of (h^4(0)).  For a nonempty
Parikh vector (v), let (v^*=v/\gcd(v_0,\ldots,v_4)).  Two nonzero
Parikh vectors have equal normalized frequencies exactly when their
primitive vectors are equal.  Thus, for each (q), inserting every
primitive signature for ([p,q)), (0\le p<q), and querying every signature
for ([q,r)), (q<r\le38416), checks every admissible triple exactly once.
The completed exact sweep found no match.  Applying the embedding above to
the concatenated factor (xy), whose length is (m+n\le2745), proves the
submitted theorem.  Its integer contrapositive gives the lower bound 2746
for any counterexample to the original claim.

## Computational and implementation checks

I performed the following checks rather than relying on the certificate's
conclusion alone.

1. I independently checked the factor-coverage endpoint (B+1=2745), the
   four cyclic differences, equivariance, and preservation of the split and
   Parikh equality.  The supplied verifier, run with the prescribed research
   interpreter, regenerated (h^3(0)) and (h^4(0)), verified their raw-byte
   SHA-256 digests, all completion counts, all four block representatives,
   and reported `outcome: verified`.
2. I inspected the exhaustive C++ implementation.  Its packed signature is
   lossless here because every coordinate is at most 38416, below (2^{16}).
   Computing the gcd from the interval length and the first four coordinates
   is exact because the fifth coordinate is the length minus their sum.
   Hash collisions are resolved by equality of both packed key fields.  The
   epoch table has ample capacity and the monotonically increasing split
   sizes do not invalidate probing.  The unsigned loop endpoints cover
   exactly (0\le p<q<r\le38416).
3. I compiled the frozen C++ source afresh and ran it in a temporary working
   directory, so it could not overwrite the frozen certificate.  The rerun
   regenerated the same (h^4(0)) digest
   `9734d1c142cd0712871db7e12e0a68304797fba7d9ab8ee6266af3fe7a06a6f2`,
   completed all 38415 splits, inserted 737875320 left intervals, queried
   737875320 right intervals, and again returned no violation and no witness.
   Its independent (h^3) cross-check also passed.

The strict inequalities (p<q<r) enforce the required positivity of both
lengths.  The one-sided boundary (s=0), factors aligned with substitution
boundaries, factors crossing a boundary at either endpoint, and the maximal
allowed length 2745 are all included in the argument.

## Source comparison, contribution, and limitations

Within the frozen source record, the nearest stated prior result is Shallit's
proved 16-letter construction together with this five-letter morphism as an
unproved proposal.  The submitted delta is not a resolution and makes no
priority or open-status claim: it combines an all-starting-position
substitution argument with an exact finite certificate to rule out every
counterexample of total length at most 2745.  This is a precise, reproducible,
and nontrivial obstruction to short counterexamples, with direct use in
future proof or falsification attempts; it is not merely an observation about
one prefix of (w).

The source record itself labels the broader current literature status
uncertain, so this audit does not infer priority or that claim (C) is open.
Nothing here controls total lengths at least 2746, and the original problem
therefore remains unresolved.

## Verdict

**Accept the exact frozen `result-note` scope.**  The quantified bound is
correctly proved by the global factor embedding plus the exact completed
sweep, the evidence is reproducible, and the stated contribution is
appropriately limited.  This verdict does not accept a proof of the original
infinite claim or any stronger novelty statement.
