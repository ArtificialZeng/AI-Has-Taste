# Frozen source — win-00041-p04

## Source

Joel Brewster Lewis, Robert Won, *Non-attacking rook placements on crossword grids*, arXiv:2609.03081v1 (2026), Question 3.13, Conjecture 3.14, Proposition 3.15.
Primary text: https://arxiv.org/abs/2609.03081v1

## Immutable problem statement

For `w in S_n`, let `Grid(w)` and its set `RP(Grid(w))` of non-attacking rook placements be as defined by Lewis--Won, and let

`r(n)=max_{w in S_n} |RP(Grid(w))|`.

Determine `r(9)` exactly. In particular, prove that `r(9)=28549`, or disprove this value by an exact permutation with a larger count. The layered permutation of shape `(3,1,1,1,3)` supplies the exact lower bound `1+48^2+162^2=28549` via source Proposition 3.15. Any exhaustive proof must justify full coverage of `S_9` and the exact counting recurrence; classification of all maximizers is a desirable strengthening but is not silently part of the frozen equality claim.
