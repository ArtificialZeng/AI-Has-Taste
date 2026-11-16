# CC-P01 — Whirling knight's tours with n coils and with the least number of coils

[Final PDF / 最终稿](../../../pdfs/ClaudeCode/CC-P01_Whirling_knights_tours_with_n_coils_and_with_the_least_number_of_coils.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Evidence: tours, certificates, programs / 复现材料](source/evidence/)

Collection / 合集: Claude Code. First obtained / 首次得到: 2026-11-14 (n coils), 2026-11-16 (least number of coils).
Archived / 入库: 2026-11-16; revised several times the same day / 当日多次修订.

## Result / 结论

Knuth's exercise 7.2.2.4–231 (*The Art of Computer Programming*, Pre-Fascicle 8A, draft of 8 May 2026) asks for n×n
whirling knight's tours with exactly n/2 coils (the least conceivable number) and with exactly n coils (the greatest).

- **n coils.** Such a tour exists if and only if n = 3, or n ≥ 12 and 4 | n.
  - New: for every n ≥ 5 that is not a multiple of 4, no such tour exists (a two-page weighted counting proof).
  - New: tours for n = 16, 20, 24 (and for every multiple of 4 from 12 to 48).
- **The greatest number of coils (new).** For every n ≥ 10 it is n if 4 | n, and n − 1 otherwise. The tours are nests
  of rings of width 12 of a second kind, which add 24 coils each ("fast" rings: zigzag lanes of two rows that advance
  two columns per move) and replace three to eight short pieces in a corner of the inner tour. For the multiples of 4
  this is a construction of tours with n coils that is independent of the one in Knuth's draft (answer 232).
  With rotational symmetry: the greatest number of coils of a tour invariant under the half turn is n − 1 for even n
  and n − 2 for odd n (n ≥ 10), and for 4 ∤ n it is attained by a tour invariant under the quarter turn.
- **A lower bound (new).** Every n×n whirling knight's tour has at least n/2 + 2 coils if n ≡ 4 or 6 (mod 8), and at
  least (n+3)/2 coils if n ≥ 5 is odd and n ≢ 1, 19 (mod 24); also at least (n+1)/2 coils for odd n ≥ 9, and at least
  6 coils for n = 8, 10. The proof is short: a tour passes through any wedge of
  the board in at most c pieces, which form a path cover of the wedge, and an explicit labelling of the wedge bounds
  the number of paths. For n ≡ 4, 6 (mod 8) this contains S. Li's theorem (arXiv:2605.04603: no tour with n/2 coils)
  and also excludes n/2 + 1 coils.
- **The least number of coils for every n ≥ 11 (new).** It is n/2 if n ≡ 0, 2 (mod 8); n/2 + 2 if n ≡ 4, 6 (mod 8);
  (n+1)/2 if n ≡ 1 or 19 (mod 24); and (n+3)/2 for every other odd n. The tours: explicit ones for small n, and for
  larger n nested rings of width 12 built from twenty-four seed tours, one for each class modulo 24. The ring is
  periodic in three stretches of each side, so that 6, 12, 6 rows and columns can be inserted to reach n + 24, n + 48, …
  (The bound (n+1)/2 for odd n ≥ 9 is Knuth's exercise 229(c); a short proof is included.)
- **Exercise 231(a).** A tour with exactly n/2 coils exists if and only if n ≥ 16 and n ≡ 0 or 2 (mod 8).
- **n ≡ 3 (mod 4): a ring attached at many pieces (new).** For n ≢ 3 (mod 4) each ring is one path, and it replaces a
  single arc of the tour inside it. For n ≡ 3 (mod 4) the solver finds no such ring around any tour that we tried. The
  six seeds for this case (n = 147, …, 167) replace 28 to 31 short pieces of the inner tour by paths with the same ends,
  which between them pass through all cells of the ring. The pieces lie in the five outer layers of the inner tour, near the eight places where
  the lanes of the ring change their period; only 47 to 60 arcs of the inner tour are dropped. The five outer layers of
  the new tour are the stretched copy of those of the inner tour, so the step repeats. Explicit tours are given for
  11 ≤ n ≤ 143.

- **Tours with rotational symmetry (new).** A whirling tour that is invariant under the half turn of the board has an
  odd number of coils, and one that is invariant under the quarter turn exists only if 4 ∤ n. For every n ≥ 11 the
  least number of coils of a tour with half-turn symmetry is the least odd number that is at least the least number
  of coils of all tours; for 4 ∤ n it is attained by a tour with quarter-turn symmetry. So for n ≡ 2 (mod 4) the
  overall minimum is attained by a tour with quarter-turn symmetry, and no tour with n coils (n ≥ 4) has either
  symmetry. The tours come from explicit lists and twenty-four further seeds in which two or four arcs, or several
  orbits of pieces, are replaced. (According to a report in The New Stack, Knuth closed his 2025 Christmas lecture
  with an 18×18 whirling tour with quarter-turn symmetry.)

- **n 圈。** 存在，当且仅当 n = 3，或 n ≥ 12 且 n 是 4 的倍数。
- **最多圈数（新）。** 对所有 n ≥ 10：n 是 4 的倍数时最多 n 圈，否则最多 n − 1 圈。巡回由另一种 12 格宽的环带逐层外套得到：
  每套一圈多转 24 圈（"快环带"），在里面巡回的一个角上替换三到八小段。对 4 的倍数，这给出了转 n 圈的巡回的另一种构造，
  不依赖高德纳草稿答案 232 中的构造。带旋转对称时：转 180° 不变的巡回最多转 n − 1 圈（n 为偶数）或 n − 2 圈（n 为奇数），
  n ≥ 10；n 不是 4 的倍数时，这个圈数由转 90° 不变的巡回达到。
- **下界（新）。** n ≡ 4、6 (mod 8) 时至少 n/2 + 2 圈；n 为奇数且 n ≢ 1、19 (mod 24) 时至少 (n+3)/2 圈。证明很短：
  巡回穿过棋盘上任何一个扇形区域时至多分成 c 段，这些段是覆盖该区域的不相交路径，再用一个显式标号给出路径数的下界。
  对 n ≡ 4、6 (mod 8)，它包含 Li 的定理（不存在 n/2 圈），并进一步排除了 n/2 + 1 圈。
- **所有 n ≥ 11 的最少圈数（新）。** n ≡ 0、2 (mod 8) 时为 n/2；n ≡ 4、6 (mod 8) 时为 n/2 + 2；
  n ≡ 1、19 (mod 24) 时为 (n+1)/2；其余奇数为 (n+3)/2。小棋盘直接给出巡回；大棋盘由二十四个种子巡回的
  12 格宽可拉伸环带逐层外套得到，每个模 24 的余数类一个种子。
- **第 231(a) 题。** 恰好 n/2 圈的巡回存在，当且仅当 n ≥ 16 且 n ≡ 0、2 (mod 8)。
- **带旋转对称的巡回（新）。** 绕中心转 180° 后与自身重合的旋转马步巡回，圈数一定是奇数；转 90° 后与自身重合的，只在
  n 不是 4 的倍数时存在。对所有 n ≥ 11，180° 对称巡回的最少圈数是"不小于普通最少圈数的最小奇数"；n 不是 4 的倍数时，
  这个圈数由 90° 对称的巡回达到。所以 n ≡ 2 (mod 4) 时，普通最少圈数就能由 90° 对称的巡回达到；恰好转 n 圈的巡回
  （n ≥ 4）则不可能有这两种对称。巡回由显式列表和另外二十四个种子给出。
- **n ≡ 3 (mod 4)：多处拼接的环带（新）。** 这类棋盘上找不到只替换一步棋的环带。六个种子（n = 147 到 167）把里面
  巡回最外五层中的 28 到 31 小段路径换成两端相同的新路径，这些新路径合起来走遍环带，位置在环带车道换周期的八处附近；里面的巡回
  只有 47 到 60 步被换掉。新巡回的外五层是旧巡回外五层拉长后的复制，所以这一步可以重复。11 ≤ n ≤ 143 直接给出巡回。

## Check it yourself / 自行验证

From `source/evidence/` (Python 3 standard library only):

```sh
python3 verify_weights.py 70
python3 check_tour.py tours_n_coils.txt
python3 lower_bounds.py
python3 half_family.py tours_half_coils.txt seeds_half_coils.txt
python3 half_family.py tours_plus2_coils.txt seeds_plus2_coils.txt
python3 half_family.py tours_odd_coils.txt seeds_odd_coils.txt
python3 half_family.py tours_odd3_coils.txt seeds_odd3_coils.txt
python3 half_family.py tours_max_coils.txt seeds_max_coils.txt
python3 half_family.py tours_symmax_coils.txt seeds_symmax_coils.txt --symmetric 1
python3 half_family.py tours_sym_coils.txt seeds_sym_coils.txt --symmetric
python3 half_family.py tours_sym_coils.txt seeds_sym3_coils.txt --symmetric
python3 half_family.py tours_half_turn_coils.txt seeds_half_turn_coils.txt --symmetric 2
python3 check_tour.py tours_least_coils.txt
```

- `verify_weights.py` checks, in exact arithmetic and over every arc, the two facts the n-coil proof needs (every arc
  term ≤ 0; the total is positive) for all n ≤ 70 not divisible by 4.
- `check_tour.py` checks every tour against the definitions and counts its coils exactly.
- `lower_bounds.py` builds the labelled wedges of the lower-bound proof for every even n ≤ 300 and odd n ≤ 201
  (larger bounds as arguments) and checks that each is a wedge, that no arc leads from a cell labelled B or O to one
  labelled B or I, and that |B| − |N| has the stated value.
- `half_family.py` checks the explicit tours, determines the replaced pieces and the new paths of the six seeds in the
  given file, checks the four finite conditions (Z), (S), (W), (C) of the paper, then builds T_k for 8 levels of each
  family (`-K 20` for 20 levels) and checks each one directly as a tour. With `-n` it writes and checks the tour for
  one n, for example `python3 half_family.py tours_odd3_coils.txt seeds_odd3_coils.txt -n 1003`. With `--symmetric`
  (quarter turn) or `--symmetric 2` (half turn) it also checks the symmetry of every tour.

Other files:

| File | Purpose |
|---|---|
| `tours_n_coils.txt` | Tours with n coils, one per line: `n=… coils=… tour=i,j i,j …` |
| `tours_half_coils.txt`, `seeds_half_coils.txt` | n ≡ 0, 2 (mod 8): tours with n/2 coils for n ≤ 90, and six seeds |
| `tours_plus2_coils.txt`, `seeds_plus2_coils.txt` | n ≡ 4, 6 (mod 8): tours with n/2 + 2 coils for n ≤ 94, and six seeds |
| `tours_odd_coils.txt`, `seeds_odd_coils.txt` | n ≡ 1 (mod 4): tours with (n+3)/2 coils, or (n+1)/2 if n ≡ 1 (mod 24), for n ≤ 93, and six seeds |
| `tours_least_coils.txt` | Tours with the least number of coils for 6 ≤ n ≤ 49 (and n = 67, 73) |
| `tours_odd3_coils.txt`, `seeds_odd3_coils.txt` | n ≡ 3 (mod 4): tours with (n+3)/2 coils, or (n+1)/2 if n ≡ 19 (mod 24), for n ≤ 143, and six seeds (header: `shift=3 omega=…`) |
| `tours_max_coils.txt`, `seeds_max_coils.txt` | Tours with the greatest number of coils for 10 ≤ n ≤ 47, and 24 fast seeds of sides 48 to 71 (header: `fast=1 obox=…`) |
| `fast_sat.py` | SAT search for a fast seed (a ring of width 12 that adds 24 coils) |
| `tours_symmax_coils.txt`, `seeds_symmax_coils.txt` | Symmetric tours with the greatest odd number of coils for 10 ≤ n ≤ 47 (quarter turn if 4 ∤ n, half turn if 4 | n), and 24 symmetric fast seeds of sides 48 to 71 (header: `fast=1 obox=… osym=…`) |
| `fast_sym_sat.py` | SAT search for a symmetric fast seed (one variable per orbit of arcs) |
| `tours_sym_coils.txt`, `seeds_sym_coils.txt`, `seeds_sym3_coils.txt` | Tours with quarter-turn symmetry and the least possible number of coils (4 ∤ n; n ≤ 95, and n ≤ 143 for n ≡ 3 mod 4), twelve seeds with four replaced arcs, six seeds for n ≡ 3 (mod 4) |
| `tours_half_turn_coils.txt`, `seeds_half_turn_coils.txt` | 4 | n: tours with half-turn symmetry and the least possible number of coils for n ≤ 92, and six seeds |
| `sym_sat.py`, `ring_sym_sat.py`, `splice_sym_sat.py` | SAT searches for symmetric tours and symmetric seeds (one variable per orbit of arcs) |
| `whirl_sat.py` | SAT search with lazy subtour elimination (needs `python-sat`); also reproduces Knuth's counts for n ≤ 9 |
| `extend_sat.py` | SAT search for a ring of width 12 around a given tour |
| `frame_sat.py` | SAT search for a tour that keeps the inner tour except at its boundary cells (n ≡ 3 mod 4, sides 51 to 119) |
| `frame_clean_sat.py` | The same with a regular boundary (n ≡ 3 mod 4, sides 123 to 143) |
| `splice_sat.py` | SAT search for a ring attached at many pieces (the six seeds for n ≡ 3 mod 4) |
| `ring_sat.py` | SAT search for a stretchable ring (the seeds) |
| `least_coils_scan.py` | For each n, the least c for which `whirl_sat.py` finds a tour |
| `lp_certificates.py` | LP relaxation and exact Farkas certificates for 13 ≤ n ≤ 27 (needs numpy, scipy); outputs in `certificates/` |
| `draw_tours.py`, `draw_ring.py`, `draw_teeth.py`, `draw_sym.py`, `draw_fast.py`, `draw_labels.py` | Regenerate the figures |

## Scope and limitations / 范围与局限

- Not externally peer reviewed. Checks so far: exact verification scripts, and independent re-implementations from the text of the paper by separate AI agents. Referee passes on 2026-11-16, each given only the paper and data files: a third found no mathematical error in the n/2-coil construction; a fourth found no error in the lower-bound section or in the n/2 + 2 families beyond one misstated proposition for the 3 x 3 board, now corrected. A fifth found no error in the families for odd n = 1 (mod 4) or in the two propositions added last, and two misstatements, now corrected. A sixth, on the ring construction with several replaced pieces and the case n = 3 (mod 4), re-implemented the seeds and conditions from the text, confirmed all 97 listed tours and all 24 seeds, and built the tours directly up to n = 1103; it found no mathematical error, one misstatement (the number of replaced pieces) and two proof steps that were not spelled out, all corrected. A seventh, in two rounds on the tours with rotational symmetry, re-implemented the checks from the text, confirmed the 103 listed symmetric tours and the 24 symmetric seeds, built a checked tour with the stated coils and symmetry for every n from 11 to 2012, and enumerated the symmetric tours of small boards without a SAT solver; it found no mathematical error, and its remarks on wording are taken into account. An eighth agent, given only the text and the data files, refereed the section on the greatest number of coils in two rounds. From the text alone it re-implemented the fast seeds and their conditions, confirmed the 76 listed tours and the 48 fast seeds (24 of them with rotational symmetry), built the tours directly for every n from 10 to 1007 (with their symmetry in the symmetric families), carried out the insertions of the lemma one by one, and enumerated all tours for n ≤ 10 (77,640,818 tours for n = 10) and all centrally symmetric tours for n ≤ 13 without a SAT solver. It found no mathematical error; three steps of a proof that were not spelled out and six sentences that claimed more than was shown were corrected.
- n coils: existence for n >= 28 was known from Knuth's draft (answer 232, Beluhov and Stappers). The fast rings give an independent, computer-assisted construction for every multiple of 4 from 12 on. The cases n = 4 and n = 8 rest on exhaustive enumeration (Knuth's counts, reproduced by whirl_sat.py).
- Least number of coils: the lower bound has a complete written proof. The existence proofs are computer-assisted: the ninety-six seeds (twenty-four for the least number of coils, twenty-four symmetric, twenty-four fast, twenty-four fast and symmetric) were found by SAT search, and the proof for all n rests on a lemma plus finite conditions that half_family.py checks. The cases n = 8, 10 of exercise 231(a) are covered by two small labelled wedges, and also by Knuth's counts.
- The least number of coils for n = 8, 9 rests on exhaustive enumeration (ours and Knuth's counts), and for n = 10 on the SAT search and on exhaustive enumerations by two of the AI referee passes. For n = 3 (mod 4), that no ring can replace a single arc is a solver report for the tours we tried, not a theorem.
- We found no published construction for n/2 coils, but cannot rule out that one is known to others (Beluhov, Stappers) and unpublished. Knuth's site was unreachable from our machine on 2026-11-16. The Internet Archive's captures of fasc8a.ps.gz have one content digest from 2026-05-09 to 2026-11-04, so the draft had not changed by early November, and a web search on 2026-11-16 found no other work on these questions besides Li's paper.
- The n-coil proof technique (closed-form Farkas certificates for a cycle-cover LP relaxation) follows S. Li, arXiv:2605.04603. Li's theorem on n/2 coils is reproved here by a different method.
- Knuth's draft is cited, not reproduced. Priority has not been established by an external party.

本条目未经外部同行评审。n 圈：n ≥ 28 的存在性此前见于高德纳草稿（答案 232）；快环带给出了一个独立的、计算机辅助的构造。最少圈数：下界有完整的书面证明；
存在性是计算机辅助证明，九十六个种子（最少圈数、带对称、最多圈数、带对称的最多圈数各二十四个）由 SAT 搜出，对所有 n 的证明依赖一条引理和程序核对的有限条件。n = 8、9 的最少圈数靠穷举，
n = 10 靠 SAT 搜索。没有查到已发表的同类构造，但不排除他人已有未发表的结果。
高德纳草稿只作引用，不转载原文。

The search programs, the proofs and the manuscript were produced with Claude Code (Anthropic) under the author's
direction. 搜索程序、证明与文稿由 Claude Code 在作者指导下完成。
