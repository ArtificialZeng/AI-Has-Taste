# BW2-PR20260913-binary_subsum_shape — Boundary log-concavity of binary reciprocal-subsum numerators

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-PR20260913-binary_subsum_shape_Boundary_log_concavity_of_binary_reciprocal_subsum_numerators.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-PR20260913-binary_subsum_shape/)

Original ID / 原始编号: `primary-20260913-binary-subsum-shape`. Origin / 来源: primary.

## Accepted scope / 已接受范围

Partial-result note; parent problem not fully solved / 部分结果札记；母题未完整解决.

Let N_n be exactly the binary reciprocal-subsum numerator in source.md and problem.md, d(n)=deg N_n, c_(n,j)=\[x^j\]N_n, and T_j(P)=p_j^2-p_(j-1)p_(j+1). (1) For every real epsilon with 0&lt;epsilon&lt;1 there exists an integer n_epsilon such that for every integer n&gt;=n_epsilon, T_j(N_n)&gt;0 at every integer 1&lt;=j&lt;=floor((1-epsilon)\*sqrt(log_2(n)/2)) and at each reflected index d(n)-j. (2) For every integer n&gt;=6, T_j(N_n)&gt;0 for j=1,2,3,d(n)-1,d(n)-2,d(n)-3; for even n&gt;=6 the stronger inequalities T_j(N_n)&gt;T_j(A_n)&gt;0 hold at these positions, where A_n=(1+x)^n N_(n/2)(x^2). (3) Set M_n=min over integers 0&lt;=K&lt;=floor(log_2 n) of (n+2^(K+1)-K-2)/(K+1). For n&gt;=2 and an internal integer 1&lt;=j&lt;=n, the conditions j\*M_n&lt;n and binom(n,j)^2\*(1-j\*M_n/n)^2&gt;binom(n+j-2,j-1)\*binom(n+j,j+1) imply T_j(N_n)&gt;0. The supporting kernel lemma is K3_m(l,t)&gt;=0 for all integers m&gt;=5 and 0&lt;=l&lt;=t&lt;=m, with exactly the formal-weight definition in equation (10) of evidence/research-boundary-proof.md. None of these statements settles all internal indices of the original conjecture.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-PR20260913-binary_subsum_shape
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-PR20260913-binary_subsum_shape
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/research_boundary.py`
- `evidence/research_growing_boundary.py`
- `evidence/research_kernel3.py`
- `evidence/research_kernel3_verify.py`
- `evidence/research_recurrence.py`
- `evidence/triage_recurrence.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- sympy

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- The original question is unresolved; the released artifact is a partial result or unproved conjecture, according to its frozen claim.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
