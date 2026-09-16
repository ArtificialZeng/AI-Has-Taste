# Independent mathematical referee report

Job: `win-00050-p04-referee-63e3dfeaceed`  
Frozen snapshot: `89d7f7938a78ae8c598d3836b5b5107c6fcfaf4209ce07380c5c1d3b763f3d7d`

## Scope reviewed

I reviewed the exact frozen `result-note` claim. It asserts an exhaustive
all-`n` counting formula for every unordered pair of black squares, not a
solution of the discrete maximization problem. The original status therefore
remains unresolved. All hashes in `audit/snapshot.json` agree with the current
copies of the frozen claim and its nine listed evidence files.

## Reconstruction of the decisive argument

For squares in distinct rows and columns, starting from the all-white grid
shows that the across-word count is `n+a`, where `a` is the number of black
squares in interior columns, while the down-word count is `n+d`, where `d` is
the number in interior rows. Hence unequal `a,d` gives count zero. When the
squares share a row, direct segmentation gives `n-1+s` across words, with
`s=1[c1>1]+1[c2>c1+1]+1[c2<n]`; comparison with the down-word count leaves
exactly the boundary-row exceptions and the nonadjacent-interior common-row
case stated in the evidence. Transposition covers common columns. Thus the
surviving distinct-row/column geometries are precisely opposite corners,
corner--interior, edge-cross, and two squares with both rows and columns
interior. This establishes exhaustion of the case split.

The counts can then be recovered by separating the split words from the
ordinary words. Once a matching among special words is fixed, unmatched
special across words inject into ordinary columns, unmatched special down
words inject into ordinary rows, and the unused ordinary vertices contribute
a factorial. This partitions perfect matchings without overlap.

For split coordinates `x<y`, let `a=x-1`, `b=y-x-1`, and `c=n-y`. The two
outer special intervals force distinct choices in regions of sizes `a,c`.
With all four interval words unmatched, conditioning on whether the
lower-right choice lies in the middle or right region gives

`ac[b(a+b-2)+(c-1)(a+b-1)]`,

which expands to the stated `I4`. Removing the lower-right word, the
upper-left word, or both gives respectively `U=ac(a+b-1)`,
`V=ac(b+c-1)`, and `I2=ac`. For two interior squares, the only
special-to-special edges are the two white cross-intersections. Selecting
zero, one, or both yields the `(n-6)!`, `(n-5)!`, and `(n-4)!` terms in
formula (I). Tracking which middle-facing word disappears gives
`U_col V_row+V_col U_row` in parallel order and
`U_col U_row+V_col V_row` in crossed order, exactly as claimed.

In the corner--interior case there are no special-to-special edges. The
all-one ordinary-core count is the first term behind (C); subtracting
matchings that use the deleted corner edge forces the adjacent injection
choices to avoid its row and column and gives the second term. For `n=3` the
single such geometry has one matching, as separately stated. In the
edge-cross case the sole special-to-special edge is the white corner, and
splitting on its use gives the two terms of (E). In a common interior row,
the three disjoint horizontal interval choices and the ordered pairs of
distinct choices above and below the row give (S). Finally, opposite corners
delete two vertex-disjoint edges from `K_{n,n}`, while each surviving
boundary-row exception deletes two edges incident with one vertex; ordinary
inclusion-exclusion gives the two formulas in `finite_census.md`. These
derivations cover all small-dimension zero factors and the stated convention
for absent negative-factorial terms.

## Exact checks performed

I independently rebuilt across and down words from white-cell runs and used a
fresh Ryser inclusion-exclusion permanent implementation, without importing
the candidate's formula or counting modules. I compared those exact counts
with a separately transcribed evaluator of (C), (E), (S), and (I) on every
one of the 4,278 unordered configurations for `3<=n<=8`. There were no
mismatches. The recomputed nonzero totals were respectively
`22,48,106,226,450,832`, consistent with the frozen census's zero counts.
I also ran the frozen verifier, which checked all 620 canonical records and
their orbit sizes summing to 4,278.

As a separate larger test, direct deletion recurrence on the word graph for
`n=15`, `B={(1,7),(7,1)}` gave `1,164,931,891,200`. Formula (E) gave the
same integer. The opposite-corner value is `1,139,544,806,400`, so the exact
difference is `25,387,084,800 = 53*12!`, confirming the asserted subsidiary
counterexample.

## Source comparison and contribution

The frozen Lewis--Won PDF defines rook placements as perfect matchings of the
word-intersection graph, gives the `k=0` and `k=1` counts, and poses the
fixed-`k` extremal problem in Question 2.2. Its Proposition 3.1 supplies an
ASM correspondence for the applicable sparse interior grids but does not give
these two-black-square coordinate formulas or their order-sensitive
classification. The present result is therefore a genuine mathematical delta
relative to the cited source: it resolves all counting cases and reduces the
still-open extremal question to explicit integer optimization. It is not a
routine restatement or a toy restriction, and the `n=15` comparison
demonstrates a concrete use. The literature statement is appropriately
limited to a targeted negative search and does not claim priority.

## Gaps and verdict

The all-`n` maximum `M_2(n)` and its equality-orbit classification remain
unproved, exactly as the claim discloses. This is a limitation of the original
problem's resolution, not a gap in the frozen subsidiary theorem. I found no
incorrect formula, missing relative-position class, hidden division or
limiting step, or unsupported promotion of finite computation to proof.

**Verdict: accept.** The frozen `result-note` scope, mathematical correctness,
and contribution all pass.
