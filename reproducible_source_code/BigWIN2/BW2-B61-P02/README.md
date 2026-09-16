# BW2-B61-P02 — An Exact Hall-Universality Census Through Six Vertices

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B61-P02_An_Exact_Hall_Universality_Census_Through_Six_Vertices.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B61-P02/)

Original ID / 原始编号: `win-00061-p02`. Origin / 来源: 61.

## Accepted scope / 已接受范围

Resolution of the frozen statement · proved / 冻结命题的证明／反证（见精确范围） · proved.

For every integer n with 0 &lt;= n &lt;= 6, including n=0 under the convention fixed in problem.md, every finite simple graph G on the labelled vertex set {1,...,n} is Hall-universal: for every simple graph H on that same labelled set, the Hilton--Johnson Hall inequalities for the graphic lists L_G(v)=N_G(v) imply the existence of a proper L_G-coloring of H. Up to isomorphism the complete positive census has 1, 1, 2, 4, 11, 34, and 156 classes in orders n=0,...,6, and there are no negative classes.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B61-P02
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B61-P02
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/census.cpp`
- `evidence/census_numba.py`
- `evidence/classify_source_families.py`
- `evidence/generate_reps.py`
- `evidence/make_manifest.py`
- `evidence/verify_census.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- networkx
- numba
- numpy

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
