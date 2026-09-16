# BW2-B73-P02 — The Exact Prime Threshold for a Short Arithmetic Point-Count Formula for Weierstrass Cubics

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B73-P02_The_Exact_Prime_Threshold_for_a_Short_Arithmetic_Point_Count_Formula_for_Weierstrass_Cubics.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B73-P02/)

Original ID / 原始编号: `win-00073-p02`. Origin / 来源: 73.

## Accepted scope / 已接受范围

Resolution of the frozen statement · proved / 冻结命题的证明／反证（见精确范围） · proved.

For every odd prime p&gt;3, let r be computed from A,B in F_p by equation (4) of arXiv:2609.05371v1 using their canonical representatives, and let Nhat_p(A,B) be given by equation (5). Then the universal assertion that Nhat_p(A,B) equals the number of affine pairs (x,y) in F_p^2 satisfying y^2=x^3+Ax+B for every A,B in F_p holds if and only if p&gt;=17. The sufficient direction is Theorem 3 of the cited paper. Necessity is witnessed, for p=5,7,11,13 respectively, by (A,B)=(1,1),(0,1),(1,3),(0,4), for which (N,r,Nhat)=(8,2,3),(11,3,4),(17,5,6),(20,6,7).

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B73-P02
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B73-P02
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/referee_independent_check.py`
- `evidence/verify_small_primes.py`

Bounded replay status in this packaging task: **passed**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.

Independent exact extraction and square-fiber point counts for four hard-coded elliptic witnesses.

## Dependencies and limitations / 依赖与限制

- No third-party Python import detected by static inspection; this is not a tested environment lock.

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
