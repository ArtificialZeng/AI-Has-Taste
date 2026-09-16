# BW2-B34-P05 — A Conjectural Bipartite-(2)/Subcubic Partition for Triangle-Free Graphs of Maximum Degree Six

[Final PDF / 最终稿](../../../pdfs/ai-conjecture/BW2-B34-P05_A_Conjectural_Bipartite_2_Subcubic_Partition_for_Triangle_Free_Graphs_of_Maximum_Degree_Six.pdf) · [LaTeX entry / 入口](source/conjecture-note/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B34-P05/)

Original ID / 原始编号: `Win34-p05`. Origin / 来源: 34.

## Accepted scope / 已接受范围

Conjectural note; original problem unresolved / 猜想札记；原问题仍未解决.



The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B34-P05
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B34-P05
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `code/audit_c001_families.py`
- `code/cegis_partition_counterexample.py`
- `code/partition_probe.py`
- `code/synthesize_partition_counterexample.py`
- `code/verify_false_fixed_partition_extension.py`
- `code/verify_false_independent_2dom.py`
- `code/verify_partition_data.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- networkx
- z3

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- The original question is unresolved; the released artifact is a partial result or unproved conjecture, according to its frozen claim.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
