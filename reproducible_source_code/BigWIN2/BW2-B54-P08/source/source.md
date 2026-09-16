# Frozen source statement: win-00054-p08

For a finite nonempty poset `P`, let `h_P(x)` be the expected rank of `x` in a uniformly random linear extension. For a nonempty maximal chain `C={y_1<...<y_m}`, let `gap_P(C)` be the largest difference between consecutive entries of
\[
0,h_P(y_1),\ldots,h_P(y_m),|P|+1.
\]
Define `m_2(4)` as the minimum `|P|` over all finite posets of width exactly two such that every nonempty maximal chain `C` has `gap_P(C)>4`. Determine `m_2(4)` and classify all minimizers up to poset isomorphism. A complete computational answer must enumerate the whole smaller-order domain, use exact rational expected ranks, emit canonical witnesses, and be independently replayable.

Primary source: *On the Gap of Finite Posets*, arXiv:2608.12678v1, Definition 1.2 and Theorem 5.1. That theorem proves width-two examples with arbitrarily large chain gap, hence the minimum above exists, but it neither asks nor computes this first exact finite threshold.

Frozen intake: `batches/inbox/bigWin-54.raw.md`. Primary PDF: `batches/inbox/bigWin-54-materials/2608.12678.pdf`.
