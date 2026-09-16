# Exact census and first structural reduction

Provenance: `win-00050-p04-research-a6f065c5a129` (research pass 1,
2026-09-07). Coordinates below are one-based. This is exact finite evidence,
not an all-`n` proof.

## Reproducible census

Run

```text
python3 evidence/enumerate_two_black.py --min-n 3 --max-n 8 \
  --output evidence/census_n3_n8.json
```

For each of the `binom(n^2,2)` unordered black-square pairs, the program scans
white cells to construct the across/down word graph. It counts its perfect
matchings both by a row-ordered subset-DP permanent and by direct graph
deletion recursion with minimum-degree branching. It asserts equality for
every configuration. It separately generates all eight reflection/transpose
images, assigns a canonical representative, asserts count invariance, and
checks that the sum of the computed orbit sizes is `binom(n^2,2)`.

| `n` | configurations | D4 orbits | zero-count configurations | `M_2(n)` | maximizing representative |
|---:|---:|---:|---:|---:|:---|
| 3 | 36 | 8 | 14 | 3 | `{(1,1),(3,3)}` |
| 4 | 120 | 21 | 72 | 14 | `{(1,1),(4,4)}` |
| 5 | 300 | 49 | 194 | 78 | `{(1,1),(5,5)}` |
| 6 | 630 | 93 | 404 | 504 | `{(1,1),(6,6)}` |
| 7 | 1176 | 171 | 726 | 3720 | `{(1,1),(7,7)}` |
| 8 | 2016 | 278 | 1184 | 30960 | `{(1,1),(8,8)}` |

There is exactly one maximizing D4 orbit at every enumerated `n`. The complete
histograms and every canonical orbit record, including its size and count, are
in `census_n3_n8.json`. Its SHA-256 is
`355a1d184588707692a485fbb9b1cb6dd332018b0c019ae99985125439682b48`.

## Proved construction formula

For black squares at two opposite corners, neither square splits a word, and
the word graph is `K_{n,n}` with two vertex-disjoint edges deleted. By
inclusion-exclusion its permanent is

```text
n! - 2(n-1)! + (n-2)! = ((n-1)(n-2)+1)(n-2)!.
```

This formula gives the entire observed maximum column, but the census alone
does not prove that it is maximal for arbitrary `n`.

If two black squares lie in the same boundary row and leave exactly one
nonempty segment in that row (the column pairs `{1,2}`, `{1,n}`, or
`{n-1,n}`), the graph is `K_{n,n}` with two edges incident to one vertex
deleted. Its count is `n!-2(n-1)!`, strictly smaller than the opposite-corner
count by `(n-2)!`. The transposed statement holds for a boundary column.

## Proved word-count reduction

The following reduction identifies all configurations that can have nonzero
count. If the black squares are in distinct rows, the number of across words
is `n+a`, where `a` is the number of the two squares whose columns are
interior. If they are also in distinct columns, the number of down words is
`n+d`, where `d` is the number whose rows are interior. Thus such a
configuration can be nonzero only when `a=d`. The three remaining word-count
classes are:

- `a=d=0`: necessarily two opposite corners;
- `a=d=1`: a square pair with `n+1` words on each side;
- `a=d=2`: two nonattacking interior squares, with `n+2` words on each side.

If the black squares are in one row, let their columns be `c_1<c_2` and let

```text
s = 1[c_1>1] + 1[c_2>c_1+1] + 1[c_2<n].
```

There are `n-1+s` across words. There are `n` down words if that row is a
boundary row and `n+2` if it is interior. Equality of word-class sizes leaves
only (i) a boundary row with `s=1`, exactly the three column pairs above, or
(ii) an interior row with `s=3`, i.e. two nonadjacent interior columns. The
same alternatives hold after transposition. Every excluded case has zero
perfect matchings because the two word classes have unequal sizes.

The unresolved kernel is therefore to count/bound the `n+1` class and the two
`n+2` classes (nonattacking interior squares and nonadjacent squares in one
interior row), and to compare them with the opposite-corner formula for all
`n` while retaining equality information.
