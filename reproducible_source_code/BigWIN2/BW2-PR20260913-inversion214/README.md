# BW2-PR20260913-inversion214 — An explicit formal quotient for Class 214 inversion sequences

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-PR20260913-inversion214_An_explicit_formal_quotient_for_Class_214_inversion_sequences.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-PR20260913-inversion214/)

Original ID / 原始编号: `primary-20260913-inversion214`. Origin / 来源: primary.

## Accepted scope / 已接受范围

Partial-result note; parent problem not fully solved / 部分结果札记；母题未完整解决.

For each n&gt;=0, let I_n consist of tuples (e_1,...,e_n) with 0&lt;=e_i&lt;i and with no i&lt;j&lt;k satisfying e_i&gt;=e_k and e_j&gt;=e_k; the empty tuple is counted once. Put F(z)=sum_{n&gt;=0}&#124;I_n&#124;z^n. In formal series at z=0 define X=(1-2z-sqrt(1-4z))/(2z), with sqrt(1-4z)=1+O(z); q=X^2/(1+2X); b=X^3/((1+X)(1+2X)); H(u)=z(1+u)^2-u; R0(u)=-zu^2(1-z-zu)/(1-zu); R1(u)=u^2(1-z-zu)^2/(1-zu). For every j&gt;=0 define t_j=z^j q/(1-q sum_{r=1}^j z^r), with the empty sum zero, and D_j=product_{i=0}^j H(t_i). Then A=sum_{j&gt;=0}R0(t_j)/D_j and L=q+sum_{j&gt;=0}R1(t_j)/D_j converge z-adically in Z\[\[z\]\], their summands having exact orders j+4 and j+3 respectively, and F=(b-A)/(zL). Here L=z^2+O(z^3) and b-A=z^3+O(z^4), so the quotient is well-defined. If A_m,L_m retain exactly j=0,...,m-1 and F_m=(b-A_m)/(zL_m), then for every integer m&gt;=0, F_m belongs to Q(z,X) intersect Z\[\[z\]\] and F_m-F=z^(m+3)+O(z^(m+4)). This solves the explicit generating-function representation part only; no algebraicity, transcendence, analytic continuation, or asymptotic assertion is made.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-PR20260913-inversion214
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-PR20260913-inversion214
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/quotient-check.py`
- `evidence/triage-kernel-check.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- sympy

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- The original question is unresolved; the released artifact is a partial result or unproved conjecture, according to its frozen claim.
- {'path': '/home/ailab/4math-open-problems/projects/primary-20260913-inversion214/evidence/triage-registry.json', 'indicators': ['absolute-local-path']}
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
