# BW2-B60-P04 — The Exact Six-Term Eliminant in a Two-State Affine-Linear Differential-Input System

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B60-P04_The_Exact_Six_Term_Eliminant_in_a_Two_State_Affine_Linear_Differential_Input_System.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B60-P04/)

Original ID / 原始编号: `win-00060-p04`. Origin / 来源: 60.

## Accepted scope / 已接受范围

Resolution of the frozen statement · proved / 冻结命题的证明／反证（见精确范围） · proved.

Let R=Q\[a11,a12,a21,a22,b1,b2,c1,c2,p1,p2,q\] be a polynomial ring of independent derivation-constant coefficient indeterminates, F=Frac(R), A=((a11,a12),(a21,a22)), b=(b1,b2)^T, c=(c1,c2)^T, and p^T=(p1,p2). For the generic dense characteristic-zero system x'=Ax+bu+c and y=p^Tx+q, put tau=tr(A), delta=det(A), Omega=det((p^T),(p^TA)), and P=Omega\*tau\*delta\*(p^Tb)\*\[p^T(tau I-A)b\]\*\[p^T(tau I-A)c-delta q\]. The polynomial P is nonzero. On the nonempty Zariski-open locus P!=0, the generic eliminant order is nu=2 and the primitive irreducible eliminant, normalized to be monic in y'', is E=y''-tau y'+delta y+p^T(tau I-A)b u-p^Tb u'+p^T(tau I-A)c-delta q. Its exact support is {1,u,u',y,y',y''}. The seven candidates furnished by the specialized Theorem 3.7 inequalities are {1,u,u',u'',y,y',y''}; hence the missing monomial is u'', and every eliminant support exponent satisfies the exact additional equality ell_2=0 (equivalently deg_{u''} E=0). This is only the frozen n=2 affine-linear dense row with one differential input and derivation-constant model coefficients; it asserts nothing for broader nonlinear, sparse, positive-characteristic, or time-varying-coefficient systems.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B60-P04
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B60-P04
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/research_symbolic_certificate.py`
- `evidence/triage_symbolic_check.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- sympy

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
