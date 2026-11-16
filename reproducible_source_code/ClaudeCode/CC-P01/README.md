# CC-P01 — Whirling knight's tours with n coils and with the least number of coils

[Final PDF / 最终稿](../../../pdfs/ClaudeCode/CC-P01_Whirling_knights_tours_with_n_coils_and_with_the_least_number_of_coils.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Evidence: tours, certificates, programs / 复现材料](source/evidence/)

Collection / 合集: Claude Code. First obtained / 首次得到: 2026-11-14 (n coils), 2026-11-16 (least number of coils).
Archived / 入库: 2026-11-16; revised twice the same day / 当日两次修订.

## Result / 结论

Knuth's exercise 7.2.2.4–231 (*The Art of Computer Programming*, Pre-Fascicle 8A, draft of 8 May 2026) asks for n×n
whirling knight's tours with exactly n/2 coils (the least conceivable number) and with exactly n coils (the greatest).

- **n coils.** Such a tour exists if and only if n = 3, or n ≥ 12 and 4 | n.
  - New: for every n ≥ 5 that is not a multiple of 4, no such tour exists (a two-page weighted counting proof).
  - New: tours for n = 16, 20, 24 (and for every multiple of 4 from 12 to 48).
- **A lower bound (new).** Every n×n whirling knight's tour has at least n/2 + 2 coils if n ≡ 4 or 6 (mod 8), and at
  least (n+3)/2 coils if n ≥ 5 is odd and n ≢ 1, 19 (mod 24); also at least (n+1)/2 coils for odd n ≥ 9, and at least
  6 coils for n = 8, 10. The proof is short: a tour passes through any wedge of
  the board in at most c pieces, which form a path cover of the wedge, and an explicit labelling of the wedge bounds
  the number of paths. For n ≡ 4, 6 (mod 8) this contains S. Li's theorem (arXiv:2605.04603: no tour with n/2 coils)
  and also excludes n/2 + 1 coils.
- **The least number of coils for every n ≥ 12 with n ≢ 3 (mod 4) (new).** It is n/2 if n ≡ 0, 2 (mod 8); n/2 + 2 if
  n ≡ 4, 6 (mod 8); (n+1)/2 if n ≡ 1 (mod 24); and (n+3)/2 for the other n ≡ 1 (mod 4). The tours: explicit ones for
  n ≤ 95, and for n ≥ 96 nested rings of width 12 built from eighteen seed tours (n = 96, …, 118) whose ring is
  periodic in three stretches of each side, so that 6, 12, 6 rows and columns can be inserted to reach n + 24, n + 48, …
  (The bound (n+1)/2 for odd n ≥ 9 is Knuth's exercise 229(c); a short proof is included.)
- **Exercise 231(a).** A tour with exactly n/2 coils exists if and only if n ≥ 16 and n ≡ 0 or 2 (mod 8).
- **n ≡ 3 (mod 4) (open).** Tours that attain the lower bound, or (n+1)/2 when n ≡ 19 (mod 24), are given for every
  such n from 11 to 47 and for n = 67. A general construction is not known to us; rings of width 12 do not exist here.

- **n 圈。** 存在，当且仅当 n = 3，或 n ≥ 12 且 n 是 4 的倍数。
- **下界（新）。** n ≡ 4、6 (mod 8) 时至少 n/2 + 2 圈；n 为奇数且 n ≢ 1、19 (mod 24) 时至少 (n+3)/2 圈。证明很短：
  巡回穿过棋盘上任何一个扇形区域时至多分成 c 段，这些段是覆盖该区域的不相交路径，再用一个显式标号给出路径数的下界。
  对 n ≡ 4、6 (mod 8)，它包含 Li 的定理（不存在 n/2 圈），并进一步排除了 n/2 + 1 圈。
- **所有 n ≥ 12、n ≢ 3 (mod 4) 的最少圈数（新）。** n ≡ 0、2 (mod 8) 时为 n/2；n ≡ 4、6 (mod 8) 时为 n/2 + 2；
  n ≡ 1 (mod 24) 时为 (n+1)/2；其余 n ≡ 1 (mod 4) 时为 (n+3)/2。n ≤ 95 直接给出巡回；n ≥ 96 由十八个种子巡回的
  12 格宽可拉伸环带逐层外套得到。
- **第 231(a) 题。** 恰好 n/2 圈的巡回存在，当且仅当 n ≥ 16 且 n ≡ 0、2 (mod 8)。
- **n ≡ 3 (mod 4)（未解决）。** 对 11 到 47 的每个这样的 n 以及 n = 67 给出了达到下界的巡回；一般构造未知。

## Check it yourself / 自行验证

From `source/evidence/` (Python 3 standard library only):

```sh
python3 verify_weights.py 70
python3 check_tour.py tours_n_coils.txt
python3 lower_bounds.py
python3 half_family.py tours_half_coils.txt seeds_half_coils.txt
python3 half_family.py tours_plus2_coils.txt seeds_plus2_coils.txt
python3 half_family.py tours_odd_coils.txt seeds_odd_coils.txt
python3 check_tour.py tours_least_coils.txt
```

- `verify_weights.py` checks, in exact arithmetic and over every arc, the two facts the n-coil proof needs (every arc
  term ≤ 0; the total is positive) for all n ≤ 70 not divisible by 4.
- `check_tour.py` checks every tour against the definitions and counts its coils exactly.
- `lower_bounds.py` builds the labelled wedges of the lower-bound proof for every even n ≤ 300 and odd n ≤ 201
  (larger bounds as arguments) and checks that each is a wedge, that no arc leads from a cell labelled B or O to one
  labelled B or I, and that |B| − |N| has the stated value.
- `half_family.py` checks the explicit tours, checks the four finite conditions (Z), (S), (W), (C) of the paper for the
  six seeds in the given file, then builds T_k for 8 levels of each family (`-K 20` for 20 levels) and checks each one
  directly as a tour. With `-n` it writes and checks the tour for one n.

Other files:

| File | Purpose |
|---|---|
| `tours_n_coils.txt` | Tours with n coils, one per line: `n=… coils=… tour=i,j i,j …` |
| `tours_half_coils.txt`, `seeds_half_coils.txt` | n ≡ 0, 2 (mod 8): tours with n/2 coils for n ≤ 90, and six seeds |
| `tours_plus2_coils.txt`, `seeds_plus2_coils.txt` | n ≡ 4, 6 (mod 8): tours with n/2 + 2 coils for n ≤ 94, and six seeds |
| `tours_odd_coils.txt`, `seeds_odd_coils.txt` | n ≡ 1 (mod 4): tours with (n+3)/2 coils, or (n+1)/2 if n ≡ 1 (mod 24), for n ≤ 93, and six seeds |
| `tours_least_coils.txt` | Tours with the least number of coils for 6 ≤ n ≤ 49 (and n = 67, 73) |
| `whirl_sat.py` | SAT search with lazy subtour elimination (needs `python-sat`); also reproduces Knuth's counts for n ≤ 9 |
| `extend_sat.py` | SAT search for a ring of width 12 around a given tour |
| `ring_sat.py` | SAT search for a stretchable ring (the seeds) |
| `least_coils_scan.py` | For each n, the least c for which `whirl_sat.py` finds a tour |
| `lp_certificates.py` | LP relaxation and exact Farkas certificates for 13 ≤ n ≤ 27 (needs numpy, scipy); outputs in `certificates/` |
| `draw_tours.py`, `draw_ring.py`, `draw_labels.py` | Regenerate the figures |

## Scope and limitations / 范围与局限

- Not externally peer reviewed. Checks so far: exact verification scripts, and independent re-implementations from the text of the paper by separate AI agents. Referee passes on 2026-11-16, each given only the paper and data files: a third found no mathematical error in the n/2-coil construction; a fourth found no error in the lower-bound section or in the n/2 + 2 families beyond one misstated proposition for the 3 x 3 board, now corrected. A fifth found no error in the families for odd n = 1 (mod 4) or in the two propositions added last, and two misstatements, now corrected.
- n coils: the existence direction for n >= 28 is quoted from Knuth's draft (answer 232, Beluhov and Stappers) and was not re-derived; tours for multiples of 4 up to 48 are supplied independently. The cases n = 4 and n = 8 rest on exhaustive enumeration (Knuth's counts, reproduced by whirl_sat.py).
- Least number of coils: the lower bound has a complete written proof. The existence proof is computer-assisted: the eighteen seeds were found by SAT search, and the proof for all n rests on a lemma plus finite conditions that half_family.py checks. The cases n = 8, 10 of exercise 231(a) are covered by two small labelled wedges, and also by Knuth's counts.
- n = 3 (mod 4): only the lower bound is proved. That it is attained is shown by explicit tours for n from 11 to 47 and n = 67; the general case is open. The least number of coils for n = 8, 9 rests on exhaustive enumeration (ours and Knuth's counts), and for n = 10 on the SAT search.
- We found no published construction for n/2 coils, but cannot rule out that one is known to others (Beluhov, Stappers) and unpublished. Knuth's site was unreachable on 2026-11-16, so we could not check for a newer draft.
- The n-coil proof technique (closed-form Farkas certificates for a cycle-cover LP relaxation) follows S. Li, arXiv:2605.04603. Li's theorem on n/2 coils is reproved here by a different method.
- Knuth's draft is cited, not reproduced. Priority has not been established by an external party.

本条目未经外部同行评审。n 圈：n ≥ 28 的存在性引自高德纳草稿（答案 232），未重新推导。最少圈数：下界有完整的书面证明；
存在性是计算机辅助证明，十八个种子由 SAT 搜出，对所有 n 的证明依赖一条引理和程序核对的有限条件。n ≡ 3 (mod 4)：只证明了下界，
达到下界的巡回只对 11 到 47 以及 67 给出，一般情形未解决。没有查到已发表的同类构造，但不排除他人已有未发表的结果。
高德纳草稿只作引用，不转载原文。

The search programs, the proofs and the manuscript were produced with Claude Code (Anthropic) under the author's
direction. 搜索程序、证明与文稿由 Claude Code 在作者指导下完成。
