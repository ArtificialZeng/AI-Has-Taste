# CC-P01 — Whirling knight's tours with n coils exist only when n = 3 or 4 divides n

[Final PDF / 最终稿](../../../pdfs/ClaudeCode/CC-P01_Whirling_knights_tours_with_n_coils_exist_only_when_n_is_3_or_4_divides_n.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Evidence: tours, certificates, programs / 复现材料](source/evidence/)

Collection / 合集: Claude Code. First obtained / 首次得到: 2026-11-14. Archived / 入库: 2026-11-16.

## Result / 结论

- **Theorem.** For every n ≥ 5 that is not a multiple of 4, no n×n whirling knight's tour has exactly n coils.
- **Corollary.** An n×n whirling knight's tour with exactly n coils exists if and only if n = 3, or n ≥ 12 and 4 | n.
  This answers exercise 7.2.2.4–231(b) of Knuth's *The Art of Computer Programming*, Pre-Fascicle 8A (draft of
  8 May 2026), where the cases 13 ≤ n ≤ 27 and all non-multiples of 4 were open.
- **New tours.** n coils: n = 16, 20, 24 (and every multiple of 4 from 12 to 48). n/2 coils: every n ≡ 0 or 2 (mod 8)
  with 16 ≤ n ≤ 66.

- **定理。** 对每个不是 4 的倍数的 n ≥ 5，不存在恰好 n 圈的 n×n 旋转马步巡回。
- **推论。** 恰好 n 圈的巡回存在，当且仅当 n = 3，或 n ≥ 12 且 n 是 4 的倍数。这回答了高德纳 TAOCP 预印分册 8A
  第 7.2.2.4–231(b) 题；此前 13 ≤ n ≤ 27 以及所有非 4 倍数的情形未解决。
- **新巡回。** n 圈：n = 16、20、24（以及 12 到 48 之间所有 4 的倍数）。n/2 圈：16 ≤ n ≤ 66 中所有 n ≡ 0、2 (mod 8)。

## Check it yourself / 自行验证

From `source/evidence/` (Python 3 standard library only):

```sh
python3 verify_weights.py 70
python3 check_tour.py tours_n_coils.txt
python3 check_tour.py tours_half_coils.txt
```

- `verify_weights.py` checks, in exact arithmetic and over every arc, the two facts the proof needs (every arc term
  ≤ 0; the total is positive) for all n ≤ 70 not divisible by 4.
- `check_tour.py` checks every tour against the definitions and counts its coils exactly.

Other files:

| File | Purpose |
|---|---|
| `whirl_sat.py` | SAT search with lazy subtour elimination (needs `python-sat`); also reproduces Knuth's counts for n ≤ 9 |
| `lp_certificates.py` | LP relaxation and exact Farkas certificates for 13 ≤ n ≤ 27 (needs numpy, scipy); outputs in `certificates/` |
| `draw_tours.py` | Regenerates the figure |
| `tours_n_coils.txt`, `tours_half_coils.txt` | The tours, one per line: `n=… coils=… tour=i,j i,j …` |

## Scope and limitations / 范围与局限

- Not externally peer reviewed. Checks so far: exact verification scripts, and an independent re-implementation from the text of the proof by a second AI agent.
- The existence direction for n >= 28 is quoted from Knuth's draft (answer 232, Beluhov and Stappers) and was not re-derived; tours for multiples of 4 up to 48 are supplied independently.
- The cases n = 4 and n = 8 rest on exhaustive enumeration (Knuth's counts, reproduced by whirl_sat.py).
- The n/2-coil statement for n <= 66 is computational; no general construction is claimed.
- The proof technique (closed-form Farkas certificates for a cycle-cover LP relaxation) follows S. Li, arXiv:2605.04603.
- Knuth's draft is cited, not reproduced. Priority has not been established by an external party.

本条目未经外部同行评审。n ≥ 28 的存在性引自高德纳草稿（答案 232），未重新推导；本包另行给出了 12 到 48 之间所有
4 的倍数的巡回。n/2 圈的结论仅为计算结果。高德纳草稿只作引用，不转载原文。

The search programs, the proofs and the manuscript were produced with Claude Code (Anthropic) under the author's
direction. 搜索程序、证明与文稿由 Claude Code 在作者指导下完成。
