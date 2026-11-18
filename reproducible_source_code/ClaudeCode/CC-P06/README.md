# CC-P06 — A fully clued Slitherlink diagram with exactly five solutions

[Final PDF / 最终稿](../../../pdfs/ClaudeCode/CC-P06_Fully_clued_Slitherlink_with_exactly_five_solutions.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Evidence / 复现材料](source/evidence/)

Collection / 合集: Claude Code. First obtained / 首次得到: 2026-11-18. Archived / 入库: 2026-11-18.

## Result / 结论

In 2023 Knuth amended his answer to TAOCP exercise 7.2.2.1–411 (fully clued Slitherlink diagrams with several solutions) with the
sentence "It's currently unknown whether or not exactly five loops are possible." This diagram (13×13, every cell clued) has
**exactly five** solutions:

```
3222222122223  2222222221122  2222122223232  2222221222112  2212222222222
2222222222221  2221122211222  1222222222222  2222222222122  2112221222222
2323222212222  2211222222222  3222212222223
```

There are also fully clued 12×12 and 13×13 diagrams with **exactly six** solutions, which answers Beluhov's question
(arXiv:2308.08798, §10) whether five or more is possible; and every fully clued diagram with fewer than 144 cells has at most
four, so the 12×12 diagram has the least possible area.

2023 年，高德纳在 TAOCP 第 7.2.2.1–411 题答案的勘误中写道："目前未知是否可能恰好有五个环。"上面这个 13×13 全线索
Slitherlink（数回）盘面**恰好有五个解**。另有恰好六个解的 12×12 与 13×13 全线索盘面，回答了 Beluhov 论文第 10 节"是否
存在至少五个解"的问题；穷举搜索还表明，面积小于 144 格的全线索盘面最多四个解，因此 12×12 的例子面积最小。

## Check it yourself / 自行验证

From `source/evidence/` (Python 3 standard library only, about two seconds):

```sh
python3 slither_check.py
```

| File | Purpose |
|---|---|
| `slither_check.py` | Counts all solutions of the five diagrams by backtracking and by enumerating totally even sets |
| `bcount.c` | Independent C backtracking counter (`cc -O2 bcount.c -o bcount && ./bcount found/m5_13x13.txt`) |
| `found/` | The diagrams, their loops (pictures and `loops.json`) |
| `search/` | The clique search over totally even differences (`teven.py`, `teven2.py`), the generic five-copy model (`satk.py`), notes |
| `logs/` | Search logs, including all square grids up to 12×12 cells and 35 rectangular grids |
| `referee/` | The separate AI referee's report, its frontier-DP counter, totally-even counter and exhaustive searches, with logs |

## Scope and limitations / 范围与局限

- Not externally peer reviewed. The counts were confirmed by four programs: SAT enumeration and plain backtracking (author's side), a frontier dynamic program and an enumeration over totally even sets (written independently by a separate AI referee). slither_check.py repeats two of these with the Python standard library in two seconds.
- Proposition 3 (fewer than 144 cells => at most four solutions) rests on SAT answers without proof certificates; it was confirmed by the referee's independent exhaustive search, which does not use SAT.
- Whether a 12x12 diagram with exactly five solutions exists, and which multiplicities above six occur, is not settled.
- Knuth's book and errata are cited, not reproduced.

本条目未经外部同行评审；结论由四个程序独立核对（其中两个由独立的 AI 审稿代理编写）。高德纳原书与勘误只作引用，不转载原文。

The computations, the arguments and the manuscript were produced with Claude Code (Anthropic) under the author's direction.
计算、论证与文稿由 Claude Code 在作者指导下完成。
