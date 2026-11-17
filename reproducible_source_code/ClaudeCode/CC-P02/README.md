# CC-P02 — Closed knight's tours with 7.5 n + O(1) crossings

[Final PDF / 最终稿](../../../pdfs/ClaudeCode/CC-P02_Closed_knights_tours_with_7_5_n_crossings.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Evidence: tours and programs / 复现材料](source/evidence/)

Collection / 合集: Claude Code. First obtained / 首次得到: 2026-11-17. Archived / 入库: 2026-11-17.

## Result / 结论

Two moves of a knight's tour *cross* if the segments between the centres of their cells meet at a point interior to both.

- **Known.** Besa, Johnson, Mamano, Osegueda and Williams (Theoret. Comput. Sci. 902 (2022), 1–20; arXiv:1904.02824) construct closed
  tours of the n×n board with 12n + O(1) crossings and prove that 4n − O(1) are necessary. Exercise 7.2.2.4–161 of Knuth's
  *The Art of Computer Programming*, Pre-Fascicle 8A (rated 46), asks: "Can a closed n × n knight's tour have fewer than
  12n + O(1) intersections?"
- **Theorem.** For every even n ≥ 30 there is a closed knight's tour of the n×n board with exactly **7.5 n + 13** crossings.
  So the answer to the exercise is yes, and the gap between the bounds drops from a factor 3 to a factor 1.875.
- **The tours.** Away from the walls every cell is joined to the cells (x+1, y+2) and (x−1, y−2); these parallel moves do not
  cross. Along the walls there are four periodic patterns: one crossing per column at the top wall, two per column on the left
  half and one on the right half of the bottom wall, and 2.5 per row at the left and right walls. That gives n + 1.5 n + 5 n.
  Near the corners and near the middle of the bottom wall 179 cells are taken from one tour of side 40 that a solver
  completed; the same cells serve for every n.
- **Why it is a single tour for every n.** The parallel moves form 3n − 32 lines. The paper lists every join between the ends
  of these lines: fourteen exceptional joins near the patches and five arithmetic rules. The list is checked by program for
  30 ≤ n ≤ 54 and follows for larger n from the periodicity of the patterns; from the list one sees directly that the tour
  runs through all lines in fourteen passes and closes up. The program also checks the list on the tours up to n = 300 and
  the single cycle up to n = 3000.
- **A variant, checked but not proved.** With a side pattern of period 6 the same method gives closed tours with
  43n/6 + 24 crossings (about 7.17 n) for n = 48, 60, 72, …; the program checks them up to n = 600. The other classes of n
  and a proof for all n are not worked out, so the theorem is stated with 7.5.

两步棋"交叉"，是指连接格子中心的两条线段在各自内部相交。

- **已知。** Besa、Johnson、Mamano、Osegueda、Williams 构造出交叉数为 12n + O(1) 的 n×n 闭合马步巡游，并证明至少需要
  4n − O(1) 个交叉。高德纳《计算机程序设计艺术》预印分册 8A 的习题 7.2.2.4–161 问：交叉数能否少于 12n + O(1)？
- **定理。** 对每个偶数 n ≥ 30，存在恰有 **7.5 n + 13** 个交叉的 n×n 闭合马步巡游。所以习题的答案是"能"，上下界之比
  从 3 降到 1.875。
- **巡游的样子。** 离墙远的格子都与 (x+1, y+2)、(x−1, y−2) 相连，这些平行的棋步互不交叉。四面墙边各有一种周期图样：
  上墙每列 1 个交叉；下墙左半每列 2 个、右半每列 1 个；左右两墙每行 2.5 个。合计 n + 1.5 n + 5 n。四个角和下墙中点附近
  共 179 个格子取自求解器补全的一条边长 40 的巡游，同一套格子对所有 n 通用。
- **为什么对所有 n 都是一条巡游。** 平行棋步连成 3n − 32 条线。论文列出了这些线端点之间的全部连接：补丁附近 14 个例外连接，
  其余服从 5 条算术规则。这张表在 30 ≤ n ≤ 54 由程序核对，更大的 n 由图样的周期性推出；由这张表可以直接看出巡游分 14 段
  穿过所有线并闭合成一圈。程序还在 n ≤ 300 的巡游上核对了这张表，并对 n ≤ 3000 核对了单圈。
- **一个已核对、未证明的变体。** 侧墙换成周期为 6 的图样，同样的方法给出交叉数为 43n/6 + 24（约 7.17 n）的闭合巡游，
  n = 48, 60, 72, …；程序核对到 n = 600。其余的 n 和一般证明没有做，所以定理只写 7.5。

## Check it yourself / 自行验证

From `source/evidence/` (Python 3 standard library only):

```sh
python3 crossing_tours.py 100
python3 crossing_tours.py --range 30 500
python3 crossing_tours.py --joins 30 300
python3 crossing_tours.py --arith 30 3000
python3 crossing_tours.py --patterns 40 500
python3 crossing_tours.py --steps 40 300
python3 crossing_tours.py --variant 48 600
```

- `crossing_tours.py n` builds the tour of side n, checks that it is one closed knight's tour through all n² cells, and counts
  its crossings by testing pairs of moves in exact integer arithmetic.
- `--range` does this for every even n in the range.
- `--joins` checks, on the tours themselves, that the joins between the lines of the field are exactly those of Lemma 6
  (Table 1 and the five rules), that the passes are those of Table 2, and the facts about the patches used in the proof.
- `--arith` checks, from the list of joins alone and without building a tour, that the lines form one cycle with the passes
  of Table 2 (a cross-check of Lemma 7, which is proved directly in the paper).
- `--patterns` checks that the description of the paper and a second construction, by inserting periods into the tours of
  side 40 and 42, give the same tour.
- `--steps` checks that the cyclic order of the lines in the tour of side n + 8 is that of side n with 24 more.
- `--variant` builds and checks the tours with 43n/6 + 24 crossings from `variant48.txt`.
- `tour40.txt` is the tour of side 40 from which the 179 patch cells are taken, as a list of moves `x,y-x,y`;
  `logs/` holds the output of the runs quoted in the paper.

Other files:

| File | Purpose |
|---|---|
| `draw_figures.py` | Regenerates the three figures (needs matplotlib) |
| `search/template.py`, `search/scan_tpl.py`, `search/small_tpl.py` | The search for the patches: everything else is prescribed, CP-SAT completes the tour (needs OR-Tools) |
| `search/strip.py`, `search/states2.py`, `search/iface.py`, `search/pairing.py`, `search/shallow_pair.py` | Periodic problems for one wall or one seam: least crossings per period, all patterns up to a cost, which patterns can be combined |
| `search/min_cross.py`, `search/uniform.py` | Least crossings on small boards; a board with free layers along the walls |
| `search/stretch.py`, `search/stretch2.py`, `search/kx.py`, `search/shallow4.json`, `search/shallow6.json`, `search/scan6b.py` | Helpers and data used by the search programs; `scan6b.py` is the search for the variant |
| `search/starburst.py`, `search/sb2.py`, `search/sbdiag.py`, `search/flux.py`, `search/torus_fields.py` | The experiments behind the last remarks of the paper (eight sectors, colours at the corners, periodic configurations without crossings) |

## Scope and limitations / 范围与局限

- Not externally peer reviewed. Checks so far: a stand-alone verification program, and two independent AI referee passes on 2026-11-17. First pass: an AI agent given only the text and the tour files rebuilt the tours with its own programs for every even n from 40 to 700 and for six larger n up to 2002, found the same tours move for move and no error in the construction; it asked for explicit tables of joins and passes in place of a sketched induction, and noticed that one set of patches serves every n >= 30. Second pass: another AI agent checked Sections 3-4 against the program and judged the proof complete after minor fixes, which were applied (full lists of the ends of the strands, a counting argument that every cell near the walls lies on one join, the boxes of the induction named, and a direct proof that the joins form a single cycle); it also ran the arithmetic check up to n = 10000.
- Computer-assisted. The list of joins between the lines of the field is checked by program for 30 <= n <= 54 and proved for larger n by induction from n - 2 to n (the joins near the patches are translates); that these joins form one cycle is proved directly; the program also checks every even n from 30 to 500, and n = 1000, 1002, 2000, directly, the list of joins on the tours up to n = 300, and the arithmetic of the passes up to n = 3000. The 179 cells of the patches were found by the CP-SAT solver.
- Only an upper bound. The least number of crossings lies between 4n - O(1) (Besa et al.) and 7.5 n + 13; the right constant is open. The remarks on what a solver finds for single walls are reports of computations, not theorems, and are not used in the proof.
- Knuth's exercise is quoted from the draft of 8 May 2026 (checked on 2026-11-17 against the copy of fasc8a.ps.gz in the Internet Archive). The draft is cited, not reproduced.
- Whether the result is new was checked only by a literature search (no later improvement of Besa et al. was found). Priority has not been established by an external party.

本条目未经外部同行评审。结论只是上界：最少交叉数介于 4n − O(1) 与 7.5 n + 13 之间，最优常数未知。证明是计算机辅助的：
连接表在 30 ≤ n ≤ 54 由程序核对，一般的 n 用从 n − 2 到 n 的归纳法；单圈由连接表直接证明。高德纳草稿只作引用，不转载原文；习题原话已对照 2026 年 5 月 8 日的草稿核对。

The search programs, the construction, the proofs and the manuscript were produced with Claude Code (Anthropic) under the
author's direction. 搜索程序、构造、证明与文稿由 Claude Code 在作者指导下完成。
