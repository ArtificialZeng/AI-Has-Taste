# BW2-B76-P03 — A Four-Dimensional Witness for the Modular-Balance Gap

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B76-P03_A_Four_Dimensional_Witness_for_the_Modular_Balance_Gap.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B76-P03/)

Original ID / 原始编号: `win-00076-p03`. Origin / 来源: 76.

## Accepted scope / 已接受范围

Resolution of the frozen statement · proved / 冻结命题的证明／反证（见精确范围） · proved.

The frozen existential assertion in source.md is true.  Let h have ordered real basis (e1,e2,r,z), with the only nonzero brackets up to skew-symmetry \[e1,e2\]=e1+z, \[e1,r\]=-r, and \[z,r\]=r.  Let V=span(e1,e2,r) and q=Rz.  This bracket satisfies Jacobi, V Lie-generates h, and kappa_q vanishes on V.  Every complement of V is q_(x,y,t)=R(z-xe1-ye2-tr); its vertical trace character on (e1,e2,r) is (-y,x,0), while its horizontal trace character on the displayed generator is 1+x+y.  Thus vertical balance forces x=y=0, where horizontal balance fails, so no complement of V is modularly balanced.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B76-P03
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B76-P03
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/verify_witness.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- sympy

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
