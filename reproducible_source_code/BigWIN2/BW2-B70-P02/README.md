# BW2-B70-P02 — A Certified Zero-Free Interval Through 1024 for the Golden-Mean Fourier Transform

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B70-P02_A_Certified_Zero_Free_Interval_Through_1024_for_the_Golden_Mean_Fourier_Transform.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B70-P02/)

Original ID / 原始编号: `win-00070-p02`. Origin / 来源: 70.

## Accepted scope / 已接受范围

Partial-result note; parent problem not fully solved / 部分结果札记；母题未完整解决.

For the self-similar measure mu and Fourier transform F fixed in source.md and problem.md, F(xi) is nonzero for every real xi satisfying 27/25 &lt;= &#124;xi&#124; &lt;= 1024. This is a strict subsidiary theorem and does not settle the frozen assertion for 1024 &lt; &#124;xi&#124; &lt;= 10^7.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B70-P02
```

- `source/evidence/research_taylor_cover_1024_certificate.json` ← `compressed/evidence/research_taylor_cover_1024_certificate.json.gz` (53714057 original bytes)

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B70-P02
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/research_taylor_cover_1024.py`
- `evidence/research_taylor_stencils.py`
- `evidence/research_valley_cells.py`
- `evidence/triage_valley_probe.py`
- `evidence/verify_research_taylor_cover_1024.py`
- `evidence/verify_research_taylor_stencils.py`
- `evidence/verify_research_valley_cells.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- flint

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- The original question is unresolved; the released artifact is a partial result or unproved conjecture, according to its frozen claim.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
