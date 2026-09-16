# BW2-PR20260914-brugidou_positivity — Positive initial coefficients and a positivity region for Brugidou's hook polynomials

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-PR20260914-brugidou_positivity_Positive_initial_coefficients_and_a_positivity_region_for_Brugidou_s_hook_polynomials.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-PR20260914-brugidou_positivity/)

Original ID / 原始编号: `primary-20260914-brugidou-positivity`. Origin / 来源: primary.

## Accepted scope / 已接受范围

Partial-result note; parent problem not fully solved / 部分结果札记；母题未完整解决.

Let phi_q(e_j)=q^(j(j-1)/2)/j! and define J_lambda by phi_q(m_lambda)=(1-q)^(n-r) q^nu(lambda) J_lambda/((n-1)! product_j a_j(lambda)!), where n=&#124;lambda&#124;, r=l(lambda), nu(lambda)=sum_i(i-1)lambda_i and a_j(lambda) is the multiplicity of j. For all integers a&gt;=2,b&gt;=0, set K_(a,b)=J_(a,1^b)/b!, d=binom(a-1,2)+(a-1)b and D=binom(a-2,2). Then K_(a,b) is in Z\[q\], and \[q^k\]K_(a,b)&gt;0 for every integer 0&lt;=k&lt;=min(d,2b+3). If b&gt;=max(0,ceil((D-4)/2)), every coefficient from degree 0 through d is strictly positive. With the established one-row cases b=0, this covers all hooks with 2&lt;=a&lt;=6. No assertion of optimality, log-concavity, or full all-partition positivity is made.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-PR20260914-brugidou_positivity
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-PR20260914-brugidou_positivity
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/intake/calibrate.py`
- `evidence/research/hook_prefix_check.py`
- `evidence/triage/hook_check.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- No third-party Python import detected by static inspection; this is not a tested environment lock.

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- The original question is unresolved; the released artifact is a partial result or unproved conjecture, according to its frozen claim.
- {'path': '/home/ailab/4math-open-problems/projects/primary-20260914-brugidou-positivity/evidence/triage/recovery-verification.json', 'indicators': ['absolute-local-path']}
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
