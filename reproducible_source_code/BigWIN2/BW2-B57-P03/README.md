# BW2-B57-P03 — Polynomial Solvability of a Two-Machine Unit-Time Resource-Constrained Job Shop with at Most Three Operations per Job

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B57-P03_Polynomial_Solvability_of_a_Two_Machine_Unit_Time_Resource_Constrained_Job_Shop_with_at_Most_Three_Operations.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B57-P03/)

Original ID / 原始编号: `win-00057-p03`. Origin / 来源: 57.

## Accepted scope / 已接受范围

Resolution of the frozen statement · proved / 冻结命题的证明／反证（见精确范围） · proved.

For every finite instance with two dedicated machines, nonpreemptive unit-time operations, at most three operations per job in a prescribed route whose consecutive operations use different machines, one unit-capacity auxiliary resource, and a job-level demand bit in {0,1} shared by all operations of that job, an optimal makespan schedule can be computed in polynomial time. Specifically, shortest-path dynamic programming over counts of the twelve (route, demand) types at each completed prefix has at most (n+3)^24 states and exactly represents all feasible schedules after an integral-slot normalization. Thus J2 &#124; res^t 111, p_ij=1, m_j&lt;=3 &#124; C_max is polynomial-time solvable under the frozen reading in problem.md. Zero-demand jobs are legal under the cited printed definition; if a nonempty instance is additionally required to contain a demand-one job, marking one existing job as the sole demand-one job leaves the resource constraint vacuous and preserves every feasible schedule and makespan.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B57-P03
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B57-P03
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/aggregate_dp_check.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- No third-party Python import detected by static inspection; this is not a tested environment lock.

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
