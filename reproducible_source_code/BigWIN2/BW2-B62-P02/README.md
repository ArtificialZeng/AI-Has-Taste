# BW2-B62-P02 — The Maximum Popular Dimension on Tied Unweighted K3,3 Is Two

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B62-P02_The_Maximum_Popular_Dimension_on_Tied_Unweighted_K3_3_Is_Two.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B62-P02/)

Original ID / 原始编号: `win-00062-p02`. Origin / 来源: 62.

## Accepted scope / 已接受范围

Resolution of the frozen statement · proved / 冻结命题的证明／反证（见精确范围） · proved.

For every one of the 13^6 labelled weak-order preference profiles on the unweighted complete bipartite graph K_{3,3}, with every acceptable partner strictly preferred to being unmatched and with all 34 partial matchings admitted as alternatives, there is a popular-winning singleton or a popular-winning unordered pair of distinct matchings. Moreover, the profile ((0,0,0),(0,1,2),(0,2,1),(0,2,1),(1,2,0),(1,0,0)) has no popular-winning singleton. Therefore the maximum popular dimension over the frozen domain is exactly 2.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B62-P02
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B62-P02
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/orbit_pair_census.cpp`
- `evidence/orbit_pair_census.py`
- `evidence/triage_singleton_check.py`
- `evidence/verify_dimension_two_witness.py`
- `evidence/verify_unreduced.py`

Bounded replay status in this packaging task: **passed**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.

Exact six-agent profile witness: all singleton failures and one successful pair checked against every matching.

## Dependencies and limitations / 依赖与限制

- numba
- numpy

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
