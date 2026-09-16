# BW2-B77-P01 — An Every-Order Bipyramid Disproof for S₂,₁,₁ ⊔ K₂ in Maximal Planar Graphs

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B77-P01_An_Every_Order_Bipyramid_Disproof_for_S2_1_1_disjoint_union_K2_in_Maximal_Planar_Graphs.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B77-P01/)

Original ID / 原始编号: `win-00077-p01`. Origin / 来源: 77.

## Accepted scope / 已接受范围

Resolution of the frozen statement · disproved / 冻结命题的证明／反证（见精确范围） · disproved.

Let H be the seven-vertex graph S_{2,1,1} disjoint-union K_2, with copies interpreted injectively and non-induced as in problem.md. For every integer m &gt;= 3, the bipyramid B_m = overline(K_2) + C_m is a finite simple maximal planar graph, and the edge-colouring in which every apex--rim edge is red and every rim-cycle edge is blue contains neither a red nor a blue copy of H. Since &#124;V(B_m)&#124; = m+2, an avoiding maximal-planar graph exists at every order n &gt;= 5. Consequently no eventual-unavoidability threshold N exists, and the frozen assertion in source.md is false.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B77-P01
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B77-P01
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/bipyramid_check.py`
- `evidence/research_independent_check.py`
- `evidence/triage_independent_check.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- networkx

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
