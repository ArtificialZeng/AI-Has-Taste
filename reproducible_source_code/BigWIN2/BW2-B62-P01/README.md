# BW2-B62-P01 — No New Construction Is Needed for the Product and Łukasiewicz Cases of a Fuzzy-Metric Problem

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B62-P01_No_New_Construction_Is_Needed_for_the_Product_and_ukasiewicz_Cases_of_a_Fuzzy_Metric_Problem.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B62-P01/)

Original ID / 原始编号: `win-00062-p01`. Origin / 来源: 62.

## Accepted scope / 已接受范围

Resolution of the frozen statement · proved / 冻结命题的证明／反证（见精确范围） · proved.

Let N_0={0,1,2,...}; for x,y in N_0 and t&gt;0 let ell(x,y)=min{x,y}, mu_t(x,y)=&#124;x-y&#124;/(2^t-1)-ell(x,y), q_t(x,y)=0 if x=y and q_t(x,y)=2^(mu_t(x,y)-t) otherwise, and M(x,y,t)=1/(1+q_t(x,y)). For each T in {T_P,T_L}, where T_P(a,b)=ab and T_L(a,b)=max(0,a+b-1), (N_0,M,T) satisfies every George--Veeramani fuzzy-metric axiom. Moreover, with x_n=n for n in N and psi(u)=2u/(1+u), the unchanged sequence is strictly fuzzy psi-contractive for every m,n in N and t&gt;0, and it is not Cauchy. Hence the same M, sequence, and psi from Theorem 3.2 and Counterexample 3.4 of arXiv:2609.03372v1 answer its Problem 3 affirmatively for both requested t-norms, exactly as asserted in the frozen original claim.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B62-P01
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B62-P01
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- No standalone program is archived; the proof and exact evidence are the reproduction assets.

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- No third-party Python import detected by static inspection; this is not a tested environment lock.

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
