# BW2-B65-P02 — The Order-Seven Degree-Square Turan Problem for the Regular Five-Vertex Tournament

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B65-P02_The_Order_Seven_Degree_Square_Turan_Problem_for_the_Regular_Five_Vertex_Tournament.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B65-P02/)

Original ID / 原始编号: `win-00065-p02`. Origin / 来源: 65.

## Accepted scope / 已接受范围

Partial-result note; parent problem not fully solved / 部分结果札记；母题未完整解决.

Let D range over all loopless digraphs on seven labeled vertices, with at most one arc in each ordered direction and with antiparallel arcs allowed. If D contains no not-necessarily-induced copy of the regular five-vertex tournament Reg5, then sum_v d_D^+(v)^2 &lt;= 186. Equality is attained, and it holds exactly for the 105 labeled copies of the balanced complete bidirected four-partite graph T_4(7), whose part sizes are 2,2,2,1. Equivalently, ex^+_{L2}(7,Reg5)=186 with this equality classification.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B65-P02
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B65-P02
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/reg5_m5_enum.py`
- `evidence/reg5_m6_enum.py`
- `evidence/reg5_m7_enum.py`
- `evidence/replay_reg5_m5.py`
- `evidence/replay_reg5_m6.py`
- `evidence/replay_reg5_m7.py`
- `evidence/verify_reg5_m5_bound.py`

Bounded replay status in this packaging task: **passed**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.

Exact m=5 row-pattern threshold certificate for the coded Reg5 degree-square bound.

## Dependencies and limitations / 依赖与限制

- numba
- numpy

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- The original question is unresolved; the released artifact is a partial result or unproved conjecture, according to its frozen claim.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
