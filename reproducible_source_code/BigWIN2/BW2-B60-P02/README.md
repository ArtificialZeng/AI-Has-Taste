# BW2-B60-P02 — Exact Cut-Uniform Ghost-Penalty Thresholds in the Aligned Two-Cell CutFEM Model for Degrees One Through Five

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B60-P02_Exact_Cut_Uniform_Ghost_Penalty_Thresholds_in_the_Aligned_Two_Cell_CutFEM_Model_for_Degrees_One_Through_Five.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B60-P02/)

Original ID / 原始编号: `win-00060-p02`. Origin / 来源: 60.

## Accepted scope / 已接受范围

Resolution of the frozen statement · proved / 冻结命题的证明／反证（见精确范围） · proved.

For every p in {1,2,3,4,5}, with gamma_D=5p(p+1) and a^(2)_{kappa,gamma} interpreted exactly as in source.md and problem.md, Gamma_p=sup_{0&lt;kappa&lt;1} inf{gamma&gt;0 : a^(2)_{kappa,gamma} is positive semidefinite}=1/\[p(4p+5)\]. Thus the exact values for p=1,2,3,4,5 are respectively 1/9, 1/26, 1/51, 1/84, and 1/125. For each p there is no maximizing kappa in (0,1); the supremum is attained only as the one-sided limit kappa-&gt;0+, while kappa-&gt;1- is not a limiting maximizer. Consequently the paper's vanishing-cut necessary threshold is globally sharp in all five requested degrees.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B60-P02
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B60-P02
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/verify_p3_p5.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- sympy

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
