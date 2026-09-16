# BW2-PR20260913-ascent_0120_0121 — A finite-width enumeration of ascent sequences avoiding 0120 and 0121

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-PR20260913-ascent_0120_0121_A_finite_width_enumeration_of_ascent_sequences_avoiding_0120_and_0121.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-PR20260913-ascent_0120_0121/)

Original ID / 原始编号: `primary-20260913-ascent-0120-0121`. Origin / 来源: primary.

## Accepted scope / 已接受范围

Resolution of the frozen statement · proved / 冻结命题的证明／反证（见精确范围） · proved.

For the exact class A_n frozen in source.md and defined in problem.md (all nonnegative ascent sequences with x_1=0, x_i&lt;=1+asc(x_1...x_(i-1)), simultaneously avoiding classical equality-preserving subsequences 0120 and 0121, with A_0={empty}), the following gives its all-length uniform structural enumeration. For K&gt;=2 set D_K={(k,H):2&lt;=k&lt;=K, empty!=H subset {0,...,k-2}}. For s=(k,H), m=min(H), and 0&lt;=t&lt;k, set f(s,t)=(k,H union {t}) if t&lt;=m; otherwise set r=&#124;{h in H:h&lt;t}&#124; and f(s,t)=(k+1-r,{h-r:h in H,h&gt;=t} union {t-r}). Define T_K(s,u)=&#124;{t:f(s,t)=u}&#124;, the row b_K to have value 1 on (K,{h}) for 0&lt;=h&lt;=K-2 and 0 elsewhere, and the column 1 to be all ones. Then, as an identity in Z\[\[z\]\], F(z)=sum_(n&gt;=0)&#124;A_n&#124;z^n=(1-z)/(1-2z)+sum_(K&gt;=2)(z/(1-z))^(2K-1) b_K(I-zT_K)^(-1)1. Equivalently, for n&gt;=1, &#124;A_n&#124;=2^(n-1)+sum_(K=2)^floor((n+1)/2) sum_(d=0)^(n-2K+1) binom(n-d-1,2K-2)b_K T_K^d 1, and &#124;A_0&#124;=1. The eligible-rank quotient and binary initialization underlying these formulas hold for every prefix, width never increases after the first letter &gt;=2, &#124;D_K&#124;=2^K-K-1, and only K&lt;=floor((N+1)/2) is needed through degree N. The claimed resolution uses the original uniform-structural-enumeration alternative; no simpler scalar closed form, rationality or algebraicity of F, or nonzero analytic convergence radius is asserted.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-PR20260913-ascent_0120_0121
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-PR20260913-ascent_0120_0121
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/canonical_state_test.py`
- `evidence/quotient_enumeration_test.py`
- `evidence/recovery_triage_test.py`
- `evidence/triage_test.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- sympy

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- {'path': '/home/ailab/4math-open-problems/projects/primary-20260913-ascent-0120-0121/evidence/recovery-registry-screen.json', 'indicators': ['absolute-local-path']}
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
