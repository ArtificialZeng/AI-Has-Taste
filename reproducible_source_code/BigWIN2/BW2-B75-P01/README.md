# BW2-B75-P01 — The Subfield-Coefficient Root Distribution for a Seventh-Degree Unit-Circle Polynomial

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B75-P01_The_Subfield_Coefficient_Root_Distribution_for_a_Seventh_Degree_Unit_Circle_Polynomial.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B75-P01/)

Original ID / 原始编号: `win-00075-p01`. Origin / 来源: 75.

## Accepted scope / 已接受范围

Resolution of the frozen statement · proved / 冻结命题的证明／反证（见精确范围） · proved.

For every integer m &gt;= 1, let q=2^m, U_{q+1}={x in F_{q^2}^\*: x^(q+1)=1}, N_m(a)=#{x in U_{q+1}: x^7+a\*x^4+a\*x^3+1=0} for a in F_q, and M_j(m)=#{a in F_q: N_m(a)=j}. If c_1=1, c_2=-3, c_m=c_{m-1}-2c_{m-2} for m&gt;=3, and d_m=-2+(-1)^m+c_m, then M_5(m)=(2^m+d_m)/8, M_3(m)=(2^m-d_m)/4, and M_1(m)=(5\*2^m+d_m)/8 for every m&gt;=1, with distinct roots counted without multiplicity.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B75-P01
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B75-P01
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/verify_character_sum_curve.py`
- `evidence/verify_subfield_distribution.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- No third-party Python import detected by static inspection; this is not a tested environment lock.

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
