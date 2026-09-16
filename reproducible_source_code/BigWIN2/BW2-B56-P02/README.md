# BW2-B56-P02 — Exact Condition-Number Asymptotics for Four Matrices in Sylvester Example 6

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B56-P02_Exact_Condition_Number_Asymptotics_for_Four_Matrices_in_Sylvester_Example_6.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B56-P02/)

Original ID / 原始编号: `win-00056-p02`. Origin / 来源: 56.

## Accepted scope / 已接受范围

Resolution of the frozen statement · proved / 冻结命题的证明／反证（见精确范围） · proved.

For the four matrices X_i(delta) frozen in source.md and problem.md, for every 0&lt;delta&lt;=1 all four are nonsingular and their spectral condition numbers have exact asymptotic pairs (p_i,K_i) defined by kappa_2(X_i(delta)) ~ K_i delta^{-p_i}: (p_1,K_1)=(2,27); (p_2,K_2)=(1,sqrt(778752/(57905-5\*sqrt(132562057)))); (p_3,K_3)=(0,sqrt(rho_3/rho_1)), where rho_1&lt;rho_2&lt;rho_3 are the three roots of 45542974464 z^3-13786630308 z^2+429202697 z-330625, uniquely isolated respectively in (1/1300,1/1200), (1/30,1/29), and (1/4,1/3); and (p_4,K_4)=(0,13/3). Moreover, case 1 obeys &#124;kappa_2/(27 delta^-2)-1&#124;&lt;=121 delta/243 on (0,1\]; case 2 obeys the explicit algebraic linear relative-error bound with M_2 and delta_2 defined in evidence/exact_asymptotics.md; case 3 obeys the explicit algebraic linear relative-error bound with M_3 there for 0&lt;delta&lt;=1/10; and case 4 satisfies kappa_2=13/(3+delta) and relative error at most delta/3 on (0,1\].

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B56-P02
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B56-P02
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/verify_asymptotics.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- sympy

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- {'path': '/home/ailab/4math-open-problems/projects/win-00056-p02/evidence/triage.md', 'indicators': ['absolute-local-path']}
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
