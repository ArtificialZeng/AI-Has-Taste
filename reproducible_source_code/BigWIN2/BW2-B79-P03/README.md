# BW2-B79-P03 — A Covariance Separator for an Explicit Dean–Goldsmith Lemma 7 Sample Family

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B79-P03_A_Covariance_Separator_for_an_Explicit_DeanGoldsmith_Lemma_7_Sample_Family.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B79-P03/)

Original ID / 原始编号: `win-00079-p03`. Origin / 来源: 79.

## Accepted scope / 已接受范围

Resolution of the frozen statement · proved / 冻结命题的证明／反证（见精确范围） · proved.

For every sufficiently large integer n, with epsilon=2^(-n), L=Z^n, A=I_n, r=k=n^2, alpha=1/2, m=3n^5, every integer M&gt;m\*2^(n log(log n)/log n), c=2M\*1_n, delta=e_1/4, and y=c+delta, the displayed data satisfy the smoothing, constellation/parameter, effective-noise, BDD-distance, and uniqueness promises used by the Dean--Goldsmith Lemma 7 sample construction. For N=n^8 independent resulting samples, the test that declares constructed exactly when D=sum_i(sum_j a_ij)^2 is positive and (sum_i (sum_j a_ij)b_i)/D&gt;3/2 distinguishes the constructed law from every fixed legal D_(M,beta,k) law, uniformly over s in \[0,M)^n intersect Z^n and 0&lt;beta&lt;=1/2. Under either hypothesis its error is at most 2n^9 exp(-pi n^2)+2n^2 exp(-exp(-2pi)n^2/1280000)+2 exp(-49 pi exp(-pi)n^13/1600), hence negligible; D=0 is classified as legal.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B79-P03
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B79-P03
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
