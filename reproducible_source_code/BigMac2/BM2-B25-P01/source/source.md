# bigMac-00025-p01 — 最小四层 r=3 Hamilton starter

## Immutable source statement

Let
\[
C_4(3)=\operatorname{Cay}(\mathbb Z_{12},\{1,2,3\})
\]
be the directed circulant in which an arc from `x` to `x+s` has step `s`.
Using Definitions 2.1--2.3 of arXiv:2609.01256v1, determine whether there
exists a four-layer balanced Hamilton starter whose three developed Hamilton
cycles admit one selected arc each such that the selected arcs form the
simple directed arithmetic step-two path
\[
0\longrightarrow2\longrightarrow4\longrightarrow6.
\]

An affirmative answer requires an explicit cycle/deletion certificate.  A
negative answer requires a complete exact obstruction or independently
replayable exhaustive certificate.  Ordinary Hamiltonicity or the path-number
equality alone does not answer the question.

## Source and status boundary

- Primary source: arXiv:2609.01256v1, *Hamilton Starters and Path
  Decompositions in Directed Circulants*, Definitions 2.1--2.3 and Section 9.
- Local primary PDF: `batches/literature/bigMac-25/2609.01256v1.pdf`, SHA-256
  `1ec8a1fc02a7736128e659f5ea152523a2aae73a2ff1ea621555e3b451e8b63c`.
- The paper constructs the `q=4`, `r=1 mod 4`, `r>=9` family and explicitly
  leaves `r=3 mod 4` open to a different construction or obstruction.  The
  present `r=3` layer is status-uncertain until literature triage is complete.

