# BW2-B51-P01 — An Exact Certificate for the (n,k) = (4,3) Monomial Lie-Additive Diameter

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B51-P01_An_Exact_Certificate_for_the_n_k_4_3_Monomial_Lie_Additive_Diameter.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B51-P01/)

Original ID / 原始编号: `win-00051-p01`. Origin / 来源: 51.

## Accepted scope / 已接受范围

Resolution of the frozen statement · proved / 冻结命题的证明／反证（见精确范围） · proved.

For V=Sym^3(C^4), U=Sym^3(span(e_1,e_2,e_3)), and rho(X)=sum_{i,j} x_ij e_i partial/partial(e_j), there exist m_1,m_2 in mon(rho(sl_4(C))) with m_1 U+m_2 U=V; hence the monomial Lie-additive diameter in the frozen (n,k)=(4,3) cell is exactly 2. Specifically, m_1 is the identity and m_2=rho(X_1)rho(X_2)rho(X_3) for the three explicit traceless integer matrices in evidence/resolution_argument.md, with X_3 acting first.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B51-P01
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B51-P01
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/research_independent_certificate.py`
- `evidence/triage_exact_certificate.py`

Bounded replay status in this packaging task: **passed**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.

Exact trace-zero Sym^3 matrix certificate and fraction-free 20-by-20 determinant.

## Dependencies and limitations / 依赖与限制

- sympy

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
