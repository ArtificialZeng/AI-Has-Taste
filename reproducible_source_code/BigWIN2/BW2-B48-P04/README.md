# BW2-B48-P04 — Exact Worst-Case Success Probability for Increasing Event Kernels on K₅ at p = 1/2

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B48-P04_Exact_Worst_Case_Success_Probability_for_Increasing_Event_Kernels_on_K5_at_p_1_2.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B48-P04/)

Original ID / 原始编号: `win-00048-p04`. Origin / 来源: 48.

## Accepted scope / 已接受范围

Partial-result note; parent problem not fully solved / 部分结果札记；母题未完整解决.

For the frozen K_5 problem at p=1/2, let F(r), 3/4 &lt;= r &lt;= 1, be the minimum unconditional success probability over every admissible jointly defined family of auxiliary events with each event probability at least r. Then F(r) equals (182/207)r on \[3/4,207/256\], (19/18)r-73/512 on \[207/256,243/256\], (4/3)r-13/32 on \[243/256,63/64\], and 2r-17/16 on \[63/64,1\]. In particular, for r=1-t^2 and every 0&lt;t&lt;=1/2, F(1-t^2)&gt;(15/16)(1-2t), so the frozen inequality holds for the complete p=1/2 slice.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B48-P04
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B48-P04
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/lp_p_half_parametric.py`
- `evidence/lp_p_half_t_quarter.py`
- `evidence/verify_lp_p_half_parametric.py`
- `evidence/verify_lp_p_half_t_quarter.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- numpy
- scipy

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- The original question is unresolved; the released artifact is a partial result or unproved conjecture, according to its frozen claim.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
