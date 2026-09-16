# BW2-PR20260913-fgn_positivity — Positivity of one-sided fractional Gaussian noise predictors for five increments

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-PR20260913-fgn_positivity_Positivity_of_one_sided_fractional_Gaussian_noise_predictors_for_five_increments.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-PR20260913-fgn_positivity/)

Original ID / 原始编号: `primary-20260913-fgn-positivity`. Origin / 来源: primary.

## Accepted scope / 已接受范围

Partial-result note; parent problem not fully solved / 部分结果札记；母题未完整解决.

For every real H with 1/2&lt;H&lt;1, define rho_0(H)=1 and rho_j(H)=((j+1)^(2H)-2\*j^(2H)+&#124;j-1&#124;^(2H))/2 for integers j&gt;=1. For every integer n with 2&lt;=n&lt;=5, let Gamma_n^k(H), 2&lt;=k&lt;=n, be the unique solution of sum_{k=2}^n Gamma_n^k(H)\*rho_&#124;l-k&#124;(H)=rho_{l-1}(H), 2&lt;=l&lt;=n. Then all these coefficients are strictly positive. Moreover, for t in (1,2), put T_4(t)=(rho_&#124;i-j&#124;(t/2))_{i,j=1}^4, b_4(t)=(rho_1(t/2),...,rho_4(t/2))^T, and let P(t)=16\*det(T_4(t) with column 3 replaced by b_4(t)). The function P(t)/((t-1)\*(2-t)^3) extends analytically to \[1,2\] and is strictly greater than 27/10 there. This subsidiary theorem does not resolve the original all-n claim.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-PR20260913-fgn_positivity
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-PR20260913-fgn_positivity
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/certify_n5.py`
- `evidence/crosscheck_n5_arb.py`
- `evidence/triage_algebra.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- flint
- sympy

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- The original question is unresolved; the released artifact is a partial result or unproved conjecture, according to its frozen claim.
- {'path': '/home/ailab/4math-open-problems/projects/primary-20260913-fgn-positivity/evidence/n5-proof.md', 'indicators': ['third-party-attribution-or-license-marker']}
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
