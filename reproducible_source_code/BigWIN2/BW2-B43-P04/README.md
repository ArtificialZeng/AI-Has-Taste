# BW2-B43-P04 — Nine B-Colors Suffice Through Ten Vertices for 3-Degenerate K3,4-Free Graphs of Maximum Degree at Most Four

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B43-P04_Nine_B_Colors_Suffice_Through_Ten_Vertices_for_3_Degenerate_K3_4_Free_Graphs_of_Maximum_Degree_at_Most_Four.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B43-P04/)

Original ID / 原始编号: `win-00043-p04`. Origin / 来源: 43.

## Accepted scope / 已接受范围

Partial-result note; parent problem not fully solved / 部分结果札记；母题未完整解决.

For every finite simple graph G on at most ten vertices that is 3-degenerate (degeneracy at most 3), has maximum degree at most 4, and contains no K_{3,4} subgraph, q_B(G) is at most 9. This bound is sharp because q_B(K_{3,3})=9. Consequently, any legal graph with q_B(G)=10 must have a connected component on at least eleven vertices. This is an exact exhaustive computational result and does not determine M_3(4).

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B43-P04
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B43-P04
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/atlas_screen.py`
- `evidence/n10_sat_screen.py`
- `evidence/n8_sat_screen.py`
- `evidence/n9_sat_screen.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- networkx
- pysat

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- The original question is unresolved; the released artifact is a partial result or unproved conjecture, according to its frozen claim.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
