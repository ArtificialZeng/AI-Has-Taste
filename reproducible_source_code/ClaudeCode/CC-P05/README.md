# CC-P05 — Three remarks on TAOCP Pre-Fascicle 8A: exercises 157(b), 204(b) and 205

[Final PDF / 最终稿](../../../pdfs/ClaudeCode/CC-P05_Three_remarks_on_Pre-Fascicle_8A_157b_204b_205.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Evidence / 复现材料](source/evidence/)

Collection / 合集: Claude Code. First obtained / 首次得到: 2026-11-17. Archived / 入库: 2026-11-18.

## Result / 结论

- **157(b).** Knuth's draft answer says no explanation is known for why no closed 8×8 knight's tour has at least two moves in each
  of the 21 symmetry classes of moves. Explanation: the classes D, I, K, L, N always contain exactly **eight** moves together. Each of
  the eight cells next to a corner spends one move on its corner, its other move lies in these five classes, and every move of these
  classes touches exactly one such cell. The same holds on every n×n board with n ≥ 7 (not n = 6).
- **204(b).** In the trie-building loop the non-tight field count should be TMS + 2 when l + TMS = q − 1 and TMS + 3 otherwise;
  the draft has 3 and 2 interchanged. Run literally as printed, the loop writes outside the node it just allocated.
- **205, one key.** The average number of pointers for one random key of length q has an exact formula in terms of the marked
  involution numbers T_q (checked against all keys for q ≤ 9) and equals q²/6 − q^{3/2}/3 + 7q/2 − c√q + O(1),
  c = 31/12 − e²√(π/2)·erfc√2 ≈ 2.1619.

- **157(b)。** 高德纳草稿说"不知道为什么"不存在每一类棋步都至少用两次的 8×8 闭合马步巡游。解释：D、I、K、L、N 五类棋步合计**恰好 8 步**——
  八个"离角一步马"的格子各有一步走向角，另一步必落在这五类中，而这五类的每一步恰好碰到一个这样的格子。对所有 n ≥ 7 的 n×n 棋盘同样成立（n = 6 不成立）。
- **204(b)。** 字典树构建循环里非紧情形的字段数，3 和 2 印反了；按印刷版逐字运行会写出刚分配的结点之外。
- **205（单键情形）。** 一个随机键的平均指针数有精确公式（q ≤ 9 时与全体键的暴力平均一致），渐近为 q²/6 − q^{3/2}/3 + 7q/2 − c√q + O(1)。

## Check it yourself / 自行验证

From `source/evidence/` (Python 3 standard library only, a few seconds):

```sh
python3 notes8a_check.py all
```

| File | Purpose |
|---|---|
| `notes8a_check.py` | 157: the two structural facts for 7 ≤ n ≤ 20; 204: runs `trie204.py`; 205: runs `one_key.py` |
| `trie204.py` | The loop of answer 204(b), literally, as printed and with the two cases interchanged, on random keys |
| `one_key.py` | Exact formula for one key vs the brute-force average over all keys (q ≤ 9); asymptotic values |
| `search/` | CP-SAT models for 157: classes, the minimal infeasible set of classes, the identity on random tours (need OR-Tools) |
| `logs/` | Output of `notes8a_check.py all` |

## Scope and limitations / 范围与局限

- Not externally peer reviewed and no separate AI referee pass; checks by the stand-alone program (structural facts, literal simulation, brute-force averages for q <= 9).
- The letters of the classes in 157 were read from the figure of the draft; the argument itself only uses the orbits of moves.
- In 205 only the case of one key is treated; the sqrt q constant is a standard Laplace estimate checked numerically to q = 6400, while the first three terms follow rigorously from the exact formula.
- Knuth's draft is cited, not reproduced; exercise numbers are those of the draft of 8 May 2026.

本条目未经外部同行评审，也没有单独的 AI 审稿；由独立程序核对。高德纳草稿只作引用，不转载原文。

The computations, the arguments and the manuscript were produced with Claude Code (Anthropic) under the author's direction.
计算、论证与文稿由 Claude Code 在作者指导下完成。
