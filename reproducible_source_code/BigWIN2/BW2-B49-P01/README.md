# BW2-B49-P01 — All Minimum Bondage Sets of the Truncated-Octahedral Graph, up to Automorphism

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B49-P01_All_Minimum_Bondage_Sets_of_the_Truncated_Octahedral_Graph_up_to_Automorphism.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B49-P01/)

Original ID / 原始编号: `win-00049-p01`. Origin / 来源: 49.

## Accepted scope / 已接受范围

Resolution of the frozen statement · proved / 冻结命题的证明／反证（见精确范围） · proved.

For the exact 24-vertex, 36-edge labeled graph T in problem.md, the family M(T) of five-edge sets F satisfying gamma(T-F)&gt;gamma(T) has cardinality 276. The full abstract automorphism group Aut(T) has order 48, and M(T) has exactly eight orbits. Under the lexicographic canonical convention of problem.md, their representatives, orbit sizes, setwise stabilizer sizes, and gamma(T-F) values are: \[(0,1),(0,2),(0,3),(1,4),(1,5)\]: (24,2,9); \[(0,1),(0,2),(0,3),(1,4),(4,9)\]: (48,1,9); \[(0,1),(0,2),(0,3),(2,6),(2,7)\]: (12,4,9); \[(0,1),(0,2),(0,3),(2,6),(8,14)\]: (48,1,9); \[(0,1),(0,2),(0,3),(5,10),(5,11)\]: (48,1,9); \[(0,1),(0,2),(0,3),(5,10),(8,14)\]: (24,2,9); \[(0,1),(0,2),(0,3),(6,11),(6,12)\]: (48,1,9); \[(0,1),(0,2),(0,3),(6,11),(7,13)\]: (24,2,9). These disjoint orbit sizes sum to 276; in particular, every member of M(T) contains the complete three-edge star at some vertex.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B49-P01
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B49-P01
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/verify_classification.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- networkx

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
