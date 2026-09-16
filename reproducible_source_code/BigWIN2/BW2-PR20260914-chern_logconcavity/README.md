# BW2-PR20260914-chern_logconcavity — Binomial log-concavity of the lower-mode forcing term in a rank-two Chern recurrence

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-PR20260914-chern_logconcavity_Binomial_log_concavity_of_the_lower_mode_forcing_term_in_a_rank_two_Chern_recurrence.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-PR20260914-chern_logconcavity/)

Original ID / 原始编号: `primary-20260914-chern-logconcavity`. Origin / 来源: primary.

## Accepted scope / 已接受范围

Partial-result note; parent problem not fully solved / 部分结果札记；母题未完整解决.

For every integer k&gt;=4 define R_k(x)=(x-k+2)A_{k-1,1}(x)+(x-k+3)(x-k+2)A_{k-2,0}(x)/2+(x+1)(x-k+3)A_{k-2,1}(x)+(x+1)(x-k+4)(x-k+3)A_{k-3,0}(x)/2, where A is exactly as defined in source.md and problem.md. If R_k(x)=sum_{r&gt;=0} rho_{k,r} binom(x,r), extended by zero for r&lt;0, then rho_{k,r}&gt;0 exactly for k-2&lt;=r&lt;=2k-1, vanishes otherwise, and rho_{k,r}^2&gt;=rho_{k,r-1}rho_{k,r+1} for every integer r&gt;=0. This is an auxiliary theorem only; neither the j=2 restriction nor the full original Conjecture 3.3 is resolved.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-PR20260914-chern_logconcavity
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-PR20260914-chern_logconcavity
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/exact_triage.py`
- `evidence/j2_prefix_probe.py`
- `evidence/j2_reduced_prefix.py`
- `evidence/j2_residual_symbolic.py`
- `evidence/verify_j2_defect3_witness.py`
- `evidence/verify_residual_certificate.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- sympy

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- The original question is unresolved; the released artifact is a partial result or unproved conjecture, according to its frozen claim.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
