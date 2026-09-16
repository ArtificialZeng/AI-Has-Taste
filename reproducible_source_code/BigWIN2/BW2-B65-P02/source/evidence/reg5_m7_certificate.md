# Order-seven exact certificate

## Claim and scope

Under the conventions frozen in `source.md` and made precise in `problem.md`,
the exact finite statement certified here is
\[
\operatorname{ex}_{L_2}^+(7,\mathrm{Reg5})=186.
\]
Moreover, every labeled equality case is a copy of the balanced complete
bidirected four-partite graph `T_4(7)`, with part sizes `2,2,2,1`. This is only
an order-seven result; it does not settle the original assertion for `m>=8`.

## Primary enumeration

`reg5_m7_enum.py` bijectively encodes every loopless labeled digraph on seven
vertices by seven independent six-bit rows, hence by one of `2^42` masks. Its
objective is exactly the sum of the squared row popcounts. At a partial row
tuple of score `s`, the traversal discards the branch only if
`s + 36*(number of rows remaining) < 186`. Consequently every graph of
objective at least 186 reaches a leaf.

An internal integer generating-function computation gives exactly 439,992
row choices at objective 186 and 6,937,603 above it, for 7,377,595 candidates
at or above the threshold. The visited histogram agrees score-by-score with
that independently computed count.

For each leaf, the program generates all five-vertex supports and all
labelings of the cyclic regular tournament. Deduplication produces exactly
`binom(7,5)*24 = 504` distinct ten-arc masks. It declares containment precisely
when such a mask is a subset of the digraph mask, so extra and antiparallel
arcs are correctly permitted. The exhaustive result is: all 6,937,603 strict
candidates contain `Reg5`; at equality exactly 105 candidates are free.

## Separate replay and equality classification

`replay_reg5_m7.py` does not use the score-pruned dense-mask traversal. It first
enumerates the 2,647 degree vectors in `{0,...,6}^7` whose square-sum exceeds
186, then takes Cartesian products of the six-vertex row subsets of those
exact degrees. The sum of these product sizes is 6,937,603. It represents each
forbidden copy as ten indices in a 49-entry adjacency array and again finds a
copy in every strict candidate.

The replay parses all 105 masks saved by the primary run. It recomputes
objective 186 and `Reg5`-freeness for each. It also checks that every unordered
pair is either bidirected or has neither arc, and that the missing-pair graph
consists of three disjoint edges and one isolated vertex. Thus its components
are exactly the four independent parts of sizes `2,2,2,1`. Conversely these
105 masks exhaust the primary run's free equality cases; the count also equals
`7!/(2!^3 3!)`.

All arithmetic and subset tests are exact integers. Numba supplies compiled
execution but no floating-point or heuristic step. Reproduction commands from
the project root are:

```sh
python3 evidence/reg5_m7_enum.py > evidence/reg5_m7_enum.log
python3 evidence/replay_reg5_m7.py > evidence/reg5_m7_replay.log
sha256sum -c evidence/reg5_m7_SHA256SUMS
```

The two computations are differently structured replays, not a substitute for
fresh mathematical referee review of their completeness arguments.
