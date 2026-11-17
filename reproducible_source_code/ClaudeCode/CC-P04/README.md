# CC-P04 — The largest removable edge sets of the pinched Sierpinski gasket

[Final PDF / 最终稿](../../../pdfs/ClaudeCode/CC-P04_Largest_removable_edge_sets_of_the_pinched_Sierpinski_gasket.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Evidence / 复现材料](source/evidence/)

Collection / 合集: Claude Code. First obtained / 首次得到: 2026-11-17. Archived / 入库: 2026-11-17.

## Result / 结论

- **The question.** The Sierpiński gasket graph S_n has a unique 3-colouring, with three different colours at its corners, so the
  *pinched* gasket (corners 0…0 and 1…1 identified) is not 3-colourable. Exercise 7.2.2.3–227 of Knuth's *The Art of Computer
  Programming*, Volume 4, Fascicle 7 (rated 40), asks how many edges can be removed before it becomes 3-colourable. The answer gives
  Filip Stappers' 2^(n−1) sets of 2^(n−1)+1 edges, says they are all the largest sets for n ≤ 4, and asks whether that is true for all n.
- **Theorem.** Yes: for every n ≥ 2 the largest removable sets have **2^(n−1)+1** edges, and they are exactly Stappers' 2^(n−1) sets.
- **Proof.** An exact recursion over the colour patterns of the three corners of a gasket (fifteen profiles occur). Every profile has a
  closed form (for example 2^(n−1) edges with a unique optimal set when only the patterns 01 and D are allowed), proved by an induction
  whose step is a finite computation. The maximizing terms of the recursion are exactly Stappers' refinement rule.

- **问题。** Sierpiński 垫片图 S_n 的 3 着色唯一，三个角颜色两两不同；把角 0…0 与 1…1 粘合（"捏合"）后就不能 3 着色。高德纳
  《计算机程序设计艺术》第 4 卷第 7 分册习题 7.2.2.3–227（难度 40）问：最多删多少条边仍不能 3 着色？书中答案给出 Filip Stappers 的
  2^(n−1) 个 2^(n−1)+1 边集，说 n ≤ 4 时它们就是全部最大可删集，并问这对所有 n 是否成立。
- **定理。** 成立：对每个 n ≥ 2，最大可删集恰有 **2^(n−1)+1** 条边，且恰好就是 Stappers 的 2^(n−1) 个集合。
- **证明。** 对垫片三个角的着色模式做精确递推（共 15 种"角轮廓"），每种轮廓都有闭式，用归纳法证明，归纳步是一个有限计算；
  递推中取到最大值的组合正好就是 Stappers 的细分规则。

## Check it yourself / 自行验证

From `source/evidence/` (Python 3 standard library only, about 1.5 minutes):

```sh
python3 gasket_check.py all
```

| File | Purpose |
|---|---|
| `gasket_check.py` | `proof` (DP, closed forms, induction step, maximizing triples), `sets` (all largest sets for n ≤ 10 = Stappers' sets; Knuth's example), `model` (direct colouring, exhaustive search n = 2, 3) |
| `logs/` | Output of `gasket_check.py all` and of the C-colourer cross-check |
| `search/` | First versions: `gdp.py`, `gproof.py`, `explicit.py`, `xcheck.py` + `color3.c` (direct colouring for n ≤ 5, exhaustive search for n ≤ 4) |

## Scope and limitations / 范围与局限

- Not externally peer reviewed. Checks so far: the stand-alone program, a separate C colourer, and one independent AI referee pass on 2026-11-17. One independent AI referee (another agent) rebuilt the graphs, a SAT colourability test and the recursion from the text alone, found by exhaustive search the largest removable sets for n = 2..5 (3, 5, 9, 17 edges; 2, 4, 8, 16 sets, equal to Stappers' sets), checked the induction step exactly, and found no mathematical gap; its wording corrections were made.
- Computer-assisted. The closed forms for the 15 profiles are proved by induction; the induction step is a finite computation (15^3 triples, explicit thresholds, polynomial identities) done by the program; the profile recursion is checked against direct colouring of the explicit graph.
- Knuth's exercise and answer are paraphrased from Pre-Fascicle 7A (5 December 2024), the frozen draft of Volume 4 Fascicle 7, fetched from the Internet Archive; they are cited, not reproduced. Novelty was checked only against that answer.

本条目未经外部同行评审；证明是计算机辅助的（归纳步为有限计算）。高德纳原题与答案只作转述引用，不转载原文。

The recursion, the programs and the manuscript were produced with Claude Code (Anthropic) under the author's direction.
递推、程序与文稿由 Claude Code 在作者指导下完成。
