# Exhaustive exact determination of `r(9)`

## Claim and conclusion

With the definitions frozen in `source.md` and made explicit in `problem.md`,
the exhaustive computation in `exhaustive_numba.py` proves

\[
  r(9)=28549.
\]

It also gives the strengthening that the only maximizers in one-line notation
are

\[
  321456987 \quad\text{and}\quad 789654123.
\]

These two permutations are related by a half-turn of the grid.  The
classification is not needed for the frozen equality claim.

## Exact matrix construction

For a permutation `p` represented by the integers `0,...,n-1`, the routine
`make_rows` first constructs its inverse.  It assigns distinct down-word IDs
column by column: the nonempty run above the black square, followed by the
nonempty run below it.  There are exactly `2*n-2` such IDs, because precisely
one black square lies in the top row and precisely one lies in the bottom row.

It then visits the nonempty left and right white runs in each row.  For every
white square `(i,j)`, comparison of `i` with the black-square row `inv[j]`
selects the upper or lower down word containing that square.  OR-ing the
corresponding bit into the across-word mask therefore records exactly the down
words meeting that across word.  Different columns have different down-word
IDs, so no multiplicity is lost by using a bit mask.  This constructs exactly
the word-incidence matrix described in `problem.md`; for `n=9` it has size
`16` by `16`.

## Exact permanent recurrence and integer bounds

`permanent` sorts the row masks by degree, which merely permutes matrix rows.
It initializes `F_0(0)=1`.  For each live subset `s` and every unused bit in
the next row mask, it performs

```
F_next[s | bit] += F_current[s].
```

Thus, by induction on the number of processed across words, every state is the
number of injective assignments of those words onto exactly that subset of
down words.  The full-mask entry after 16 rows is the permanent and hence the
rook-placement count.  All arrays have unsigned 64-bit integer type.  Every
intermediate state is at most the number of partial injections between sets of
size at most 16, and hence at most `16! = 20922789888000 < 2^64`; no permanent
entry can overflow.  The observed aggregate sums in the output are also below
`2^64`.  The FNV value is only a deterministic stream checksum, not part of
the mathematical proof.

## Exhaustive coverage

`enumerate_n` starts with the increasing permutation and repeatedly calls the
explicit `next_permutation` implementation.  Given a nonfinal permutation,
that routine finds its rightmost ascent, swaps its first element with the
least larger suffix element, and reverses the remaining decreasing suffix.
This is the immediate lexicographic successor.  It returns false only on the
decreasing permutation.  Therefore the loop visits every element of `S_n`
exactly once.  The recorded coverage counts are `n!` for every `1 <= n <= 9`,
including `362880` for `n=9`.

For each visited permutation the program compares its exact count with the
running maximum and retains every equality case.  The `n=9` record is:

- coverage: `362880` permutations;
- maximum: `28549`;
- maximizer count: `2`;
- maximizers: `321456987`, `789654123`;
- sum of all counts: `157952552`;
- `(permutation,count)` stream FNV-1a-64: `06b19af39ce8cb91`.

The resulting universal upper bound, together with either retained equality
case (and independently with the source's layered-family lower bound), proves
the frozen equality.

## Cross-checks and reproduction

The same exhaustive routine reproduces the source's published maxima for
`1 <= n <= 8`:

```
1, 1, 1, 5, 17, 73, 469, 3493.
```

After the maximizers are frozen, a separate plain-Python implementation
reconstructs their incidence masks and directly branches over perfect
matchings, without subset-DP memoization or row sorting.  It returns `28549`
for each of the two maximizers.  These recounts are serialized in
`exhaustive-results.json`.

Run from the project root with Python 3.10, NumPy 2.2.6, and Numba 0.67.0:

```
python3 evidence/exhaustive_numba.py evidence/exhaustive-results.json
```

Two complete runs produced byte-identical JSON.  At candidate handoff the SHA-256
digests were:

```
f2b8721e73432d7673e6d127135950fbde1edd3a8df26ccb936d663779912ea8  evidence/exhaustive_numba.py
7f8ccd085ba65e9486e17ae46501f1c20e82e4d5d51a8a0e8dd3194b16411ef2  evidence/exhaustive-results.json
```

The first attempted native implementation could not be compiled because no
C/C++ compiler is installed in this environment.  No conclusion relies on
that failed route.  The Numba program and its plain-Python recount completed
successfully; Numba is used only to execute the displayed integer algorithm.
