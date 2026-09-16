# BW2-PR20260914-hypercomb_unimodality — A two-step bound for the modes of uniform hypercomb summands

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-PR20260914-hypercomb_unimodality_A_two_step_bound_for_the_modes_of_uniform_hypercomb_summands.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-PR20260914-hypercomb_unimodality/)

Original ID / 原始编号: `primary-20260914-hypercomb-unimodality`. Origin / 来源: primary-20260914.

## Accepted scope / 已接受范围

Partial-result note; parent problem not fully solved / 部分结果札记；母题未完整解决.

For every pair of integers n&gt;=2 and ell&gt;=3, let a=(1+(ell-2)x)(1+(ell-1)x), b=x(1+(ell-1)x), z0=1+ell\*x, z1=(1+(ell-1)x)(a+2\*x), F0=0, F1=1, and Fj=a\*F_(j-1)+b\*F_(j-2) for j&gt;=2. Set Wn=z1\*Fn and Yn=z0\*b\*F_(n-1), the Galvin-Sharpe Section 2.5 decomposition Cn=Wn+Yn. With zero-extended coefficients define P&lt;=_lr Q by p_i\*q_j&gt;=p_j\*q_i for all integers i&lt;j. Then Wn&lt;=_lr x^2\*Yn and Yn&lt;=_lr x\*Wn. Hence the smallest coefficient-maximizing indices satisfy m(Yn)-1&lt;=m(Wn)&lt;=m(Yn)+2. In particular, Cn is nondecreasing up to r=min(m(Wn),m(Yn)) and nonincreasing from q=max(m(Wn),m(Yn)), where q-r&lt;=2. The summand separation bound two is attained by unique modes 6 and 4 at n=3,ell=5. Full unimodality and log-concavity of Cn for all parameters remain unproved here.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-PR20260914-hypercomb_unimodality
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-PR20260914-hypercomb_unimodality
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/triage_checks.py`
- `evidence/two_step_checks.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- sympy

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- The original question is unresolved; the released artifact is a partial result or unproved conjecture, according to its frozen claim.
- {'path': '/home/ailab/4math-open-problems/projects/primary-20260914-hypercomb-unimodality/evidence/triage-registry-check.json', 'indicators': ['absolute-local-path']}
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
