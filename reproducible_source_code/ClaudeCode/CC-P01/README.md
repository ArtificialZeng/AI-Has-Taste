# CC-P01 — Whirling knight's tours with n coils and with n/2 coils

[Final PDF / 最终稿](../../../pdfs/ClaudeCode/CC-P01_Whirling_knights_tours_with_n_coils_and_with_n_over_2_coils.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Evidence: tours, certificates, programs / 复现材料](source/evidence/)

Collection / 合集: Claude Code. First obtained / 首次得到: 2026-11-14 (n coils), 2026-11-16 (n/2 coils).
Archived / 入库: 2026-11-16. Revised the same day to add the n/2-coil theorem / 当日修订，加入 n/2 圈定理.

## Result / 结论

Knuth's exercise 7.2.2.4–231 (*The Art of Computer Programming*, Pre-Fascicle 8A, draft of 8 May 2026) asks for n×n
whirling knight's tours with exactly n/2 coils (the least possible) and with exactly n coils (the most possible).

- **n coils.** Such a tour exists if and only if n = 3, or n ≥ 12 and 4 | n.
  - New: for every n ≥ 5 that is not a multiple of 4, no such tour exists (a two-page weighted counting proof).
  - New: tours for n = 16, 20, 24 (and for every multiple of 4 from 12 to 48).
- **n/2 coils.** Such a tour exists if and only if n ≥ 16 and n ≡ 0 or 2 (mod 8).
  - Nonexistence for n ≡ 4, 6 (mod 8) is S. Li's theorem (arXiv:2605.04603); n = 8, 10 are Knuth's counts.
  - New: existence for every such n. Explicit tours for the 20 values n ≤ 90. For n ≥ 96, nested rings of width 12
    around a tour of side 72–90: six seed tours (n = 96, 98, 104, 106, 112, 114) whose ring is periodic in three
    stretches of each side, so that 6, 12, 6 rows and columns can be inserted to reach n + 24, n + 48, …

- **Other n (computations only).** A table of the least number of coils for 6 ≤ n ≤ 37, and a question: it seems to be
  n/2 + 2 for n ≡ 4, 6 (mod 8), (n+1)/2 for odd n ≡ 1, 19 (mod 24), and (n+3)/2 for the other odd n.

- **n 圈。** 存在，当且仅当 n = 3，或 n ≥ 12 且 n 是 4 的倍数。新结果：非 4 倍数的 n ≥ 5 全部不存在（两页证明）；
  n = 16、20、24 的巡回。
- **n/2 圈。** 存在，当且仅当 n ≥ 16 且 n ≡ 0、2 (mod 8)。不存在的一半是 Li 的定理；新结果是存在的一半：
  n ≤ 90 的 20 个尺寸直接给出巡回，n ≥ 96 用 12 格宽的环带逐层外套，六个种子巡回的环带可以按周期拉长。

## Check it yourself / 自行验证

From `source/evidence/` (Python 3 standard library only):

```sh
python3 verify_weights.py 70
python3 check_tour.py tours_n_coils.txt
python3 check_tour.py tours_least_coils.txt
python3 half_family.py tours_half_coils.txt seeds_half_coils.txt
python3 half_family.py tours_half_coils.txt seeds_half_coils.txt -n 1000 -o tour1000.txt
```

- `verify_weights.py` checks, in exact arithmetic and over every arc, the two facts the n-coil proof needs (every arc
  term ≤ 0; the total is positive) for all n ≤ 70 not divisible by 4.
- `check_tour.py` checks every tour against the definitions and counts its coils exactly.
- `half_family.py` checks the 20 explicit n/2-coil tours, checks the four finite conditions (Z), (S), (W), (C) of the
  paper for the six seeds, then builds T_k for 8 levels of each family (`-K 20` for 20 levels, up to n = 570) and
  checks each one directly as a tour. With `-n` it writes and checks the tour for one admissible n.

Other files:

| File | Purpose |
|---|---|
| `tours_n_coils.txt`, `tours_half_coils.txt`, `seeds_half_coils.txt`, `tours_least_coils.txt` | The tours, one per line: `n=… coils=… tour=i,j i,j …` |
| `least_coils_scan.py` | For each n, the least c for which `whirl_sat.py` finds a tour (the table of least coil numbers) |
| `whirl_sat.py` | SAT search with lazy subtour elimination (needs `python-sat`); also reproduces Knuth's counts for n ≤ 9 |
| `extend_sat.py` | SAT search for a ring of width 12 around a given tour (used for n = 72, …, 90) |
| `ring_sat.py` | SAT search for a stretchable ring (the six seeds) |
| `lp_certificates.py` | LP relaxation and exact Farkas certificates for 13 ≤ n ≤ 27 (needs numpy, scipy); outputs in `certificates/` |
| `draw_tours.py`, `draw_ring.py` | Regenerate the figures |

## Scope and limitations / 范围与局限

- Not externally peer reviewed. Checks so far: exact verification scripts, and independent re-implementations from the text of the paper by separate AI agents. A third AI referee pass (2026-11-16), given only the paper and the data files, found no mathematical error in the n/2-coil section, confirmed conditions (Z), (S), (W), (C) for the six seeds, and checked the construction directly for every admissible n from 72 to 810 and for n = 1000.
- n coils: the existence direction for n >= 28 is quoted from Knuth's draft (answer 232, Beluhov and Stappers) and was not re-derived; tours for multiples of 4 up to 48 are supplied independently. The cases n = 4 and n = 8 rest on exhaustive enumeration (Knuth's counts, reproduced by whirl_sat.py).
- n/2 coils: nonexistence is not ours (Li's theorem; Knuth's counts for n = 8, 10). The existence proof is computer-assisted: the six seeds were found by SAT search, and the proof for all n rests on a lemma plus finite conditions that half_family.py checks.
- The table of least coil numbers for other n is computational only: tours are verified, but the absence of tours with fewer coils rests on the SAT solver's answers.
- We found no published construction for n/2 coils, but cannot rule out that one is known to others (Beluhov, Stappers) and unpublished. Knuth's site was unreachable on 2026-11-16, so we could not check for a newer draft.
- The n-coil proof technique (closed-form Farkas certificates for a cycle-cover LP relaxation) follows S. Li, arXiv:2605.04603.
- Knuth's draft is cited, not reproduced. Priority has not been established by an external party.

本条目未经外部同行评审。n 圈：n ≥ 28 的存在性引自高德纳草稿（答案 232），未重新推导。n/2 圈：不存在的一半是 Li 的定理；
存在的一半是计算机辅助证明，六个种子由 SAT 搜出，对所有 n 的证明依赖一条引理和程序核对的有限条件。没有查到已发表的
同类构造，但不排除他人已有未发表的结果。高德纳草稿只作引用，不转载原文。

The search programs, the proofs and the manuscript were produced with Claude Code (Anthropic) under the author's
direction. 搜索程序、证明与文稿由 Claude Code 在作者指导下完成。
