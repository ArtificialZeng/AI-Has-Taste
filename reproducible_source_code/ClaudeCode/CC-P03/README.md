# CC-P03 — How many edges can be removed from a flower snark line graph?

[Final PDF / 最终稿](../../../pdfs/ClaudeCode/CC-P03_Removing_edges_from_flower_snark_line_graphs.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Evidence / 复现材料](source/evidence/)

Collection / 合集: Claude Code. First obtained / 首次得到: 2026-11-17. Archived / 入库: 2026-11-17.

## Result / 结论

- **The question.** The line graph L(J_q) of Isaacs' flower snark J_q (q odd) has 6q vertices and 12q edges and is not
  3-colourable. Exercise 7.2.2.3–233 of Knuth's *The Art of Computer Programming*, Volume 4, Fascicle 7 (rated 40), asks how
  many edges can be removed before it becomes 3-colourable. Knuth's answer hopes for a reader's answer; his best removes nine.
- **Theorem.** For every odd q ≥ 5 at most **nine** edges can be removed, and the removable nine-edge sets are exactly the 4q
  *claw sets*: the edges of L(J_q) that touch the three edges of J_q at one vertex (Knuth's example is one of them). For q = 3
  the maximum is fifteen (one set). For q ≥ 7 the number of removable k-edge sets is q · (12, 132, 324, 498, 504, 336, 144, 36, 4)
  for k = 1, …, 9.
- **Proof.** Claw sets work for every snark by the parity lemma. For the upper bound, a 27-state Boolean transfer matrix T runs
  around the ring of J_q; T² = T⁴, so two removed edges more than two units apart always allow a colouring, and what is left is a
  finite search inside three consecutive units, the same for all odd q ≥ 7.

- **问题。** Isaacs 花形 snark J_q（q 为奇数）的线图 L(J_q) 有 6q 个顶点、12q 条边，不能 3 着色。高德纳《计算机程序设计艺术》
  第 4 卷第 7 分册习题 7.2.2.3–233（难度 40）问：最多能删去多少条边而仍不能 3 着色？书中答案说希望有读者给出好的答案，作者目前最好是删 9 条。
- **定理。** 对每个奇数 q ≥ 5，最多只能删 **9** 条；能删的 9 边集恰好是 4q 个"爪集"：取 J_q 的一个顶点，删去 L(J_q) 中碰到该顶点三条边的
  全部 9 条边（高德纳的例子就是其中之一）。q = 3 时最多 15 条（唯一）。q ≥ 7 时，可删的 k 边集个数为 q·(12, 132, 324, 498, 504, 336, 144, 36, 4)，
  k = 1…9。
- **证明。** 爪集可删对任何 snark 成立（奇偶引理）。上界用绕 J_q 一圈的 27 状态布尔转移矩阵 T：T² = T⁴，因此相距超过两个单元的两条被删边
  总会允许着色，剩下的是三个相邻单元内的有限搜索，对所有奇数 q ≥ 7 相同。

## Check it yourself / 自行验证

From `source/evidence/` (Python 3 standard library only, about one minute):

```sh
python3 snark_check.py all
python3 extras.py
```

| File | Purpose |
|---|---|
| `snark_check.py` | All checks of the paper: `model` (transfer model vs direct colouring), `period`, `pairs`, `window`, `small` (q = 3, 5), `claws` |
| `extras.py` | Counts of removable k-sets; the Petersen graph |
| `logs/` | Output of the two programs |
| `search/` | The exploratory programs (CP-SAT, C backtracking): `snark2.py`, `count9.py` brute force for q ≤ 15; `transfer.py`, `proof1-3.py` first version of the proof |

## Scope and limitations / 范围与局限

- Not externally peer reviewed. Checks so far: the stand-alone program, independent brute-force computations, and one independent AI referee pass on 2026-11-17. One independent AI referee (another agent) rebuilt the graphs, a SAT colourability test and the transfer matrices from the text alone, confirmed both theorems by exhaustive enumeration for every odd q from 3 to 17, and recommended acceptance with minor revisions, which were made (an explicit arc argument, the q = 5 counts, the q = 3 case via the Petersen graph, clearer wording).
- Computer-assisted. The upper bound rests on finite computations with 27 x 27 Boolean matrices (T^2 = T^4, the far-pairs lemma, and an exhaustive search over the 2^36 edge sets of three consecutive units with monotone pruning); the transfer model is checked against direct colouring of the explicit graph for every set of at most two edges when q = 3, 5, 7.
- The question for other snarks is open: the Petersen graph also gives 9 (its 10 claw sets), J_3 gives 15.
- Knuth's exercise and answer are paraphrased from Pre-Fascicle 7A (5 December 2024), the frozen draft of Volume 4 Fascicle 7, fetched from the Internet Archive; they are cited, not reproduced. Whether the result is new was checked only against that answer and a short literature search.

本条目未经外部同行评审；上界是计算机辅助证明（有限的布尔矩阵计算与穷举）。高德纳原题与答案只作转述引用，不转载原文。

The search programs, the proof and the manuscript were produced with Claude Code (Anthropic) under the author's direction.
搜索程序、证明与文稿由 Claude Code 在作者指导下完成。
