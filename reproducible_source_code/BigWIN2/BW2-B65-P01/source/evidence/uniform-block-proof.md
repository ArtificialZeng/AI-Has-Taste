# Uniform block proof of the claimed preperiod and period

This document proves the universal statement in `source.md`.  All word
concatenations below are literal, and exponents mean repeated concatenation.
Put

```text
A = 0000111122,   B = 2331020010,   D = 1121020010,
F = 112102,       W = 02101.
```

## The exact word

For every integer `K>=1`, with `c=10K+1` and `q=2c+5`, the SG word is

```text
G_K = A^K 0 B D^(K-1) F W^infinity.                 (1)
```

The prefix before `W` has length
`10K+1+10+10(K-1)+6=20K+7=q`, as required.  We prove
(1) directly from the mex recurrence.  Since that recurrence determines each
new term from earlier terms, verification at every index also proves uniqueness.

Before index `c`, the move `c` is unavailable.  Direct calculation at indices
`0,...,9` gives `A`.  For a full later `A` block, the pairs of values at offsets
4 and 6, in residue order `0,...,9` modulo 10, are

```text
11 11 21 21 02 02 00 00 10 10,
```

whose mex word is `A`.  This also covers the final `0` at index
`c-1=10K`.

Write an index in the next part as `n=c+t`.  For `0<=t<10`, the value at
distance `c` is `A[t]`; using the already determined values at distances 4 and
6 gives the following option triples (in move order `4,6,c`):

```text
110 210 210 020 221 301 321 131 032 212.
```

Their mex word is `2331020010=B`.

If a `D` block is present, its residue-`j` option triples are

```text
000 020 100 000 111 101 211 111 022 212,
```

whose mex word is `1121020010=D`.  Indeed, the short-move predecessors are
the circular `D` entries at residues `j-4` and `j-6`, while the `c`-predecessor
is `A[j]`: throughout the `D` region its index is still below `c`.  At the
first `B|D` seam the same calculation applies because `B[4:10]=D[4:10]`, the
entire part of the preceding block that offsets 4 and 6 can inspect.  Later
seams are `D|D`.  When `K=1`, this region is empty.

The word `F` starts at index `2c-1`.  Whether its preceding length-10 block is
`B` (`K=1`) or `D` (`K>=2`), the inspected suffix is the same.  Its six option
triples are

```text
000 022 103 003 111 100,
```

and their mex word is `112102=F`.  This proves (1) through index `q-1`.

It remains to prove the infinite tail.  For `n=q+u`, the first six option
triples, which include every boundary interaction of the 4- and 6-moves with
`F`, are

```text
212 110 020 211 000 221.
```

Their mex word is `021010`, the first six symbols of `W^infinity`.  The sixth
triple is the same for `K=1` and `K>=2`: its `c`-predecessor is respectively
the first entry of `F` or of `D`, and both entries equal 1.

For `u>=6`, put `r=u mod 5` and
`h_u=G_K(c+5+u)`, the value at distance `c`.  The two short-move options are
`W[r+1]` and `W[r-1]` (indices modulo 5).  The complete local criterion is

| `r` | short-move pair | proposed value `W[r]` | necessary and sufficient condition |
|---:|:---:|---:|:---|
| 0 | 2,1 | 0 | `h_u != 0` |
| 1 | 1,0 | 2 | `h_u != 2` |
| 2 | 0,2 | 1 | `h_u != 1` |
| 3 | 1,1 | 0 | `h_u != 0` |
| 4 | 0,0 | 1 | `h_u != 1` |

Thus in every row the condition is simply `h_u != W[r]`.  It holds throughout:

- if `K>=2`, the `D` part of the `c`-predecessor word starts at `u=5`;
  aligned against the proposed tail the two length-10 words are
  `D=1121020010` and `WW=0210102101`, unequal at every position;
- the `F` part starts at `u=c-6`, a multiple of 5, and
  `F=112102` differs positionwise from `021010`, the aligned part of the tail;
- from `u=c` onward, `h_u=W[u-c]`.  Since `c=1 mod 5`, this is `W[r-1]`,
  which differs from `W[r]` at every cyclic position.

For `K=1` the `D` interval is empty; the same `F` and final-tail checks meet
the already verified `u=0,...,5` boundary.  This completes the recurrence
verification at every index and proves (1).

## Minimality

Equation (1) makes 5 a period from index `q`.  It cannot begin at any earlier
index: at the immediately preceding comparison,

```text
G_K(q-1) = F[5] = 2,        G_K(q-1+5) = W[4] = 1.   (2)
```

It remains to exclude a smaller eventual period.  If an infinite word has two
eventual periods, their greatest common divisor is also an eventual period:
the Euclidean step follows because periods `r>s` imply period `r-s` after
discarding a further finite prefix.  Hence an eventual period in
`{1,2,3,4}`, together with period 5, would force eventual period 1.  But
`W^infinity` is not eventually constant (it contains both 0 and 2 in every
block).  Therefore the least eventual period is 5.  With that least period
fixed, (2) proves that its least preperiod is exactly
`q=2c+5=20K+7`.

## Machine-checkable finite identities

`evidence/verify_uniform_blocks.py` checks every local mex table and every
pointwise mismatch used above with exact integers.  Its additional finite
recurrence replays are implementation checks only; the proof of the universal
quantifier is the block reduction just given.
