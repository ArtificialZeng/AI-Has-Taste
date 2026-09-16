# BW2-PR20260913-chen_ulc_failure — Higher-index failure of ultra-log-concavity for Chen's recursion polynomials

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-PR20260913-chen_ulc_failure_Higher_index_failure_of_ultra_log_concavity_for_Chen_s_recursion_polynomials.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-PR20260913-chen_ulc_failure/)

Original ID / 原始编号: `primary-20260913-chen-ulc-failure`. Origin / 来源: primary.

## Accepted scope / 已接受范围

Resolution of the frozen statement · proved / 冻结命题的证明／反证（见精确范围） · proved.

For every integer m &gt;= 4, let f_m(s)=((s+1)^m-(-1)^m)/(s+2) and h_m(s)=((s+1)^m+(-1)^m(s+1))/(s+2). For either P in {f_m,h_m}, write P(s)=sum_{j=0}^{m-1} a_j s^j. These are monic degree-(m-1) polynomials with nonnegative integer coefficients. For every integer j satisfying 4 &lt;= j &lt;= m-2, j(m-1-j)a_j^2 &lt; (j+1)(m-j)a_{j-1}a_{j+1}. Moreover, for every m &gt;= 4 the difference j(m-1-j)a_j^2-(j+1)(m-j)a_{j-1}a_{j+1} equals -m at j=m-2. Thus neither f_m nor h_m is ordinary ultra-log-concave, meaning that (a_j/binom(m-1,j)) is not log-concave, for any m &gt;= 4. This includes both clauses of source.md and the m=4,5 cases with empty higher-index range.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-PR20260913-chen_ulc_failure
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-PR20260913-chen_ulc_failure
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/research-verify.py`
- `evidence/triage-verify.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- sympy

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- {'path': '/home/ailab/4math-open-problems/projects/primary-20260913-chen-ulc-failure/evidence/triage-registry.json', 'indicators': ['absolute-local-path']}
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
