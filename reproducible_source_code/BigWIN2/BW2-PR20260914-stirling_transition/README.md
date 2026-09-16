# BW2-PR20260914-stirling_transition — The log-concavity to log-convexity transition in fixed columns of Stirling numbers

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-PR20260914-stirling_transition_The_log_concavity_to_log_convexity_transition_in_fixed_columns_of_Stirling_numbers.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-PR20260914-stirling_transition/)

Original ID / 原始编号: `primary-20260914-stirling-transition`. Origin / 来源: primary.

## Accepted scope / 已接受范围

Resolution of the frozen statement · proved / 冻结命题的证明／反证（见精确范围） · proved.

Let c(n,k) count permutations of n elements with k cycles, with c(0,0)=1 and c(n,k)=0 outside 0&lt;=k&lt;=n. For each integer k&gt;=1 there exists an integer N_k&gt;=k+1 such that D_k(n)=c(n,k)^2-c(n-1,k)c(n+1,k) is nonnegative for every integer 1&lt;=n&lt;N_k and strictly negative for every integer n&gt;=N_k. Hence the full weak-inequality assertion frozen in source.md holds. The proof establishes the sufficient inequality q_k(n)-2q_k(n+1)+q_k(n+2)&gt;=0 for every n&gt;=k&gt;=1, where q_k(n)=c(n,k-1)/c(n,k); it is strict for k&gt;=2 and an equality for k=1. An admissible finite threshold is N_k=1+min{j&gt;=k:q_k(j)-q_k(j+1)&lt;1}.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-PR20260914-stirling_transition
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-PR20260914-stirling_transition
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/triage_exact.py`
- `evidence/triage_recovery_check.py`
- `evidence/verify_ratio_proof.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- sympy

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
