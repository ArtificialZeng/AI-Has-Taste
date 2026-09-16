# BW2-N01-P07 — A bijection for 312/321-avoiding permutations whose cubes avoid 2143

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-N01-P07_A_bijection_for_312_321_avoiding_permutations_whose_cubes_avoid_2143.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-N01-P07/)

Original ID / 原始编号: `newwin-00001-p07`. Origin / 来源: 新WIN-1批次.

## Accepted scope / 已接受范围

Resolution of the frozen statement · proved / 冻结命题的证明／反证（见精确范围） · proved.

For every integer n&gt;=0, let B_n be the permutations pi of \[n\] avoiding classical patterns 312 and 321 whose third compositional power pi^3 avoids 2143; no condition is imposed on pi^2. Let C_n be the ordered compositions of n with at most one part outside {1,3}, with one empty object in each set at n=0. Writing epsilon_d=(2,3,...,d,1), with epsilon_1=(1), the direct-sum map F(d_1,...,d_m)=epsilon_{d_1} direct-sum ... direct-sum epsilon_{d_m} restricts to a size-preserving bijection C_n -&gt; B_n. Its inverse repeatedly records the position d of the minimum, removes the forced prefix epsilon_d, and subtracts d from the suffix. For every finite list of positive parts, F(d)^3 avoids 2143 if and only if at most one part is outside {1,3}. Consequently b_n=&#124;B_n&#124;=&#124;C_n&#124; for all n&gt;=0 and, as a formal power-series identity, sum_{n&gt;=0} b_n z^n = 1/(1-z-z^3) + (z^2+z^4/(1-z))/(1-z-z^3)^2.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-N01-P07
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-N01-P07
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/recovery_check.py`
- `evidence/research_check.py`
- `evidence/triage_check.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- No third-party Python import detected by static inspection; this is not a tested environment lock.

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
