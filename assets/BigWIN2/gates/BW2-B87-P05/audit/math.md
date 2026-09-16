# Fresh mathematical referee report

## Frozen scope and evidence integrity

I reviewed the exact `resolution-paper` claim in `claim.json`, with original
status `proved`, against the frozen statement in `source.md` and its quantified
reading in `problem.md`.  The review is bound to snapshot digest
`dff598900ca3853ffdfffa450efdc068c19f8c13baf27ece103fb8d84255d785`.
Before reviewing the argument, I recomputed the SHA-256 digest of every file in
the snapshot mapping; all nine file digests agreed with `audit/snapshot.json`.
I did not broaden the claim to Conjecture 6.1 of the cited source.

## Reconstruction of the decisive argument

For an occurrence starting at local position zero, the positions in increasing
letter-value order are

```text
1 < 0 < 3 < 2 < 4.
```

Superimposing two translated copies gives the following exhaustive overlap
classification in lengths at most nine.

- At shift 1 the relations contain the cycle
  `2 < 1 < 0 < 3 < 2`; at shift 3 they contain
  `3 < 2 < 4 < 3`.  Such occurrence pairs are impossible.
- At shift 2 the union is the seven-element chain with position order
  `1,0,3,2,5,4,6`.
- At shift 4 the union is the nine-element poset consisting of
  `a1<a2<a3<a4<c<d1<d2<d3` and `b<c`, with `b` incomparable
  precisely with `a1,a2,a3,a4`.

For `N<=9`, any two occurrence starts differ by at most four, so no other
pair type is relevant.  Three pairwise compatible distinct starts can only be
`{1,3,5}` at `N=9`.  Their relations form the nine-element strict chain

```text
w2 < w1 < w4 < w3 < w6 < w5 < w8 < w7 < w9.
```

Consequently a word of length at most nine whose content has a repeated letter
has at most two occurrences.  This is the needed degree bound; the all-distinct
content has a singleton coordinate orbit and needs no degree bound for
stability.

Let `D=product_j alpha_j!`, let `e_k` be the elementary symmetric polynomial
in the coordinates of `alpha`, and let
`B_k=sum_w binom(c(w),k)`.  Marking one start, choosing the five distinct
ranks used there, and freely placing the remaining multiset gives

```text
B1 = (N-4)(N-5)! e5 / D.
```

For a marked shift-2 pair, the seven-chain similarly gives

```text
C2 = (N-7)! e7 / D,
```

and there are `N-6` such pairs.  Thus, through length nine,

```text
B2 = 1[N>=7](N-6)C2 + 1[N=9]Q,
```

where `Q` counts assignments to the shift-4 poset.  These formulas count
marked occurrences or marked pairs, so additional unmarked occurrences do not
cause overcounting errors.

The only incomparable pairs in the shift-4 poset are `{b,a_j}`.  They all
share `b`; hence a non-injective assignment to its nine positions is possible
only for content `{2,1^7}`, with the two equal positions `b` and one `a_j`.
For all other repeated contents, `Q=0`.  For content `alpha^(r)` with rank `r`
repeated, the four distinct values below `c` must be ranks `1,2,3,4` in their
forced chain order.  Therefore

```text
Q(alpha^(r)) = 1 for r=1,2,3,4,
Q(alpha^(r)) = 0 for r=5,6,7,8.
```

For repeated contents the degree bound permits exact binomial inversion:

```text
A2=B2,  A1=B1-2B2,  A0=N!/D-B1+B2.
```

For `N<=8`, every term is symmetric in the coordinates.  At `N=9`, the same
is true for every repeated content other than `{2,1^7}`, since its shift-4
term is zero.  Together with the singleton all-distinct orbit, this proves the
claimed stability and uniqueness assertions for every positive content vector,
including the `m<5` and `N<5` cases where strictness makes all occurrences
impossible.

For `{2,1^7}`, direct substitution gives

```text
T=181440, e5=91, B1=5460, e7=15, C2=15,
B2=45+Q.
```

Inversion therefore gives

```text
176026 + 5368 t + 46 t^2  for repeated rank 1,2,3,4,
176025 + 5370 t + 45 t^2  for repeated rank 5,6,7,8.
```

The two polynomials differ, and the strict-chain argument already excludes
three or more occurrences for these contents.

## Checks actually performed

I checked the four translated inequality systems directly, including both
cycles, the shift-2 total order, the exact incomparabilities at shift 4, and
the unique compatible triple of starts.  I separately checked the marked-set
counting factors, the numbers of possible start pairs, the exceptional-poset
assignment count, and the three binomial-inversion identities.  The edge cases
of fewer than five ranks, all-distinct content, and every positive composition
through total size nine are all covered by the argument rather than silently
excluded.

As supplementary falsification, I reran both snapshot-listed exact-integer
programs.  `evidence/overlap_moment_check.py` completed successfully over 511
ordered positive contents and 7,685,705 words, recovered the stated overlap
closures, found maximum occurrence count two for repeated contents, and
reproduced all eight exceptional polynomials.  Independently at the
classification level, `evidence/triage_exact_check.py` completed successfully;
at `N=9` it covered all 30 unordered types and all 256 ordered contents and
reported exactly the single unstable type `{2,1^7}`.  Its outputs matched the
frozen `.out` files.  I treat these runs as checks, not as substitutes for the
combinatorial proof.

## Source comparison and limitations

The snapshot-listed source triage identifies Chen--Fang--Kitaev,
arXiv:2602.13566v2, as the nearest source.  According to that inspected-source
record, Proposition 4.12 does not apply to `21435`, Remark 4.13 explicitly
records the all-distinct standard-extension obstruction, and the paper does
not state this first-instability classification or either coefficient list.
The broader Conjecture 6.1 remains outside the claim.  The recorded literature
search is expressly limited and cannot establish priority; the candidate also
expressly disclaims priority.  This limitation is not a gap in the frozen
mathematical resolution, though any later publication should retain bounded
novelty language and undergo its separate citation review.

## Verdict

**Accept.**  The submitted argument proves all three parts of the frozen
original claim in their full quantified scope, meets the required combinatorial
contribution boundary, and is corroborated by reproducible exact checks.  I
found no unresolved mathematical gap or required scope revision.
