# Frozen source — win-00045-p08

For odd `m` and odd `t<=m`, let `I_{m,t}` be the class of tournaments that can be induced as the majority tournament of `m` linear orders while every majority arc has margin at most `t`.  Thus a representation in `I_{5,1}` has exactly a `3:2` split on every arc, whereas a representation in `I_{5,3}` permits `3:2` and `4:1` arcs but no unanimous `5:0` arc.

Determine exactly whether every nine-vertex tournament in the 254 isomorphism/reversal classes reported by the source as

> `I_{3,3} \ I_{3,1}`

belongs to `I_{5,1}`.

Every tournament in this finite family lies in `I_{5,3}`: append a pair of mutually reversed linear orders to a three-voter representation, preserving every majority margin.  Therefore either outcome is meaningful:

1. one class outside `I_{5,1}` is an explicit witness to `I_{5,1} proper_subset I_{5,3}`; or
2. a complete positive census proves that no witness to this inclusion occurs in this first reported boundary family on nine vertices and supplies a checked lower-bound step for the broader hierarchy problem.

For a negative membership result, the publication-level certificate must include the tournament adjacency data, an explicit five-order representation witnessing membership in `I_{5,3}`, and independently checkable UNSAT evidence for the existence of five strict total orders giving exactly `3:2` support on every tournament arc.  Generate a transparent CNF, emit DRAT or preferably LRAT, and verify it with an independent checker; the source program's bare `N` output is not a proof certificate.  For a positive membership result, give five explicit permutations for every class and independently recount every arc.

The primary source is Leonid Chindelevitch and Ararat Harutyunyan, *Tournaments determined by three and five voters*, arXiv:2607.26690v1.  Conjecture 8.1 asks whether all adjacent margin layers are strict.  Do **not** use the paper's bound `12<=N(5)` as a lower bound for the present separation: `N(5)` concerns the smallest non-five-inducible tournament, and that bound does not exclude smaller tournaments in `I_{5,3}\I_{5,1}`.  Begin with the 254 nine-vertex boundary classes, not with `n=12`.

Primary PDF: `bigWin-45-materials/2607.26690.pdf`, SHA-256 `f115bd834f5c9b1129d2664118aa8e63b2fc86c225c99782246fe3f8b47ad569`.

