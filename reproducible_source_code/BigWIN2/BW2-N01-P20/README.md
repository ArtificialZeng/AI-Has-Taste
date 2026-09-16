# BW2-N01-P20 — A uniform two-term expansion for the lane-merging gap near capacity

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-N01-P20_A_uniform_two_term_expansion_for_the_lane_merging_gap_near_capacity.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-N01-P20/)

Original ID / 原始编号: `newwin-00001-p20`. Origin / 来源: 新WIN-1批次.

## Accepted scope / 已接受范围

Resolution of the frozen statement · proved / 冻结命题的证明／反证（见精确范围） · proved.

For integers m&gt;=1 and 0&lt;=k&lt;=2m-1, let E_{m,k}=G_{m,k}/binom(2m-1,k), where G_{m,k}=sum_{i=0}^k binom(2m-1,i) if k&lt;m, and G_{m,k}=sum_{i=0}^{2m-2-k} binom(2m-1,i)+(k-m+1)binom(2m,k+1) if k&gt;=m, with a sum with negative upper endpoint equal to zero. Define x_+=max(x,0), erfc(t)=(2/sqrt(pi))\*integral_t^infinity exp(-u^2)du, H(x)=(sqrt(pi)/2)exp(x^2)erfc(&#124;x&#124;), F0(x)=H(x)+2x_+, and F1(x,delta)=(2delta+1)xH(x)+delta+1-2x_+^2 for real x and -1&lt;delta&lt;=0. For every real A&gt;0 there exist a finite C_A&gt;=0 and an integer M_A&gt;=1 such that for every integer m&gt;=M_A and every real &#124;x&#124;&lt;=A, k=m+floor(x sqrt(m)) is admissible and &#124;E_{m,k}-sqrt(m)F0(x)-F1(x,delta_m(x))&#124;&lt;=C_A/sqrt(m), where delta_m(x)=floor(x sqrt(m))-x sqrt(m). This includes x=0, all floor jumps, and m-dependent real x. Explicit nonoptimized C_A and M_A are given in equations (6), (11), (13), (18), and (19) of evidence/research-proof.md. No growing-window extension is claimed.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-N01-P20
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-N01-P20
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/research-check.py`
- `evidence/triage-check.py`
- `evidence/triage-product-check.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- mpmath

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
