# BW2-B66-P01 — A Uniform Upper Bound for the Diagonal Maximal-Planar Ramsey Number of K1,3 disjoint union K2

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B66-P01_A_Uniform_Upper_Bound_for_the_Diagonal_Maximal_Planar_Ramsey_Number_of_K1_3_disjoint_union_K2.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B66-P01/)

Original ID / 原始编号: `win-00066-p01`. Origin / 来源: 66.

## Accepted scope / 已接受范围

Partial-result note; parent problem not fully solved / 部分结果札记；母题未完整解决.

Let H=K_{1,3} disjoint-union K_2, with copies understood as ordinary (not necessarily induced) subgraphs. Every red-blue edge-colouring of every finite simple maximal planar graph G with &#124;V(G)&#124; at least 21 contains a monochromatic copy of H. Equivalently, P(21) holds and r_MP(H,H) exists with r_MP(H,H) at most 21. No claim is made that 21 is the least threshold.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B66-P01
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B66-P01
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- No standalone program is archived; the proof and exact evidence are the reproduction assets.

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- No third-party Python import detected by static inspection; this is not a tested environment lock.

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- The original question is unresolved; the released artifact is a partial result or unproved conjecture, according to its frozen claim.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
