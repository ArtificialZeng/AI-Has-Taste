# BW2-B60-P03 — Exact Solution and Optimal Face of a Four-Dimensional Boolean-Quadric Semidefinite Relaxation

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B60-P03_Exact_Solution_and_Optimal_Face_of_a_Four_Dimensional_Boolean_Quadric_Semidefinite_Relaxation.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B60-P03/)

Original ID / 原始编号: `win-00060-p03`. Origin / 来源: 60.

## Accepted scope / 已接受范围

Resolution of the frozen statement · proved / 冻结命题的证明／反证（见精确范围） · proved.

For the finite conic formulation frozen in problem.md, let alpha be the unique root in (-1/24,-1/25) of 32 alpha^3+48 alpha^2+26 alpha+1=0. Its exact optimum is v_\*=-(32 alpha^2+16 alpha+1)/36, the root near -0.0108411477500751 of 576 v^3-16 v^2+92 v+1=0. The complete exposed optimal face in (x,X,p) is the singleton specified exactly in evidence/exact_solution.md; it is fixed by reverse-complement. The same file gives matching exact primal and dual certificates, with exact PSD, nonnegativity, complementary-slackness, and uniqueness verification reproduced by evidence/exact_certificate.py.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B60-P03
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B60-P03
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/exact_certificate.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- sympy

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
