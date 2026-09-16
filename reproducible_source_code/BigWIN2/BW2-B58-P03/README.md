# BW2-B58-P03 — Pendant Vertices and Total Domination: Corrections at Diameters Two and Three

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B58-P03_Pendant_Vertices_and_Total_Domination_Corrections_at_Diameters_Two_and_Three.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B58-P03/)

Original ID / 原始编号: `win-00058-p03`. Origin / 来源: 58.

## Accepted scope / 已接受范围

Resolution of the frozen statement · disproved / 冻结命题的证明／反证（见精确范围） · disproved.

Under the unchanged open-neighborhood definitions for finite simple connected graphs: (i) a pendant vertex and diameter two force its support to be universal, so no graph also has domination number two and Theorem 4.2 is vacuous; Lemma 4.1's initial minimality step is valid, but its later claim that a vertex at distance two dominates the pendant is invalid, while the remaining diameter arguments are unnecessary; (ii) among graphs with a pendant vertex, diameter three, and domination number two, the assertion gamma_t=2 is false first at order six, where exactly two isomorphism classes fail, with canonical graph6 strings E@V_ and EBYg, and both have gamma_t=3; (iii) independent-part vertex multiplication preserves total domination number, but the Petersen graph has gamma_t=4 rather than the paper's printed value 6, so the actual family H conclusion is gamma_t in {3,4}, with value 3 on the C5 and G0 branches and 4 on the Petersen branch. The instruction in source.md to preserve the value 6 is incompatible with its instruction not to change the definitions: accepting 6 counterfactually would propagate {3,6}, but does not repair the actual graph theorem.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B58-P03
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B58-P03
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/diameter3_census.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- networkx

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
