# BW2-L260905848-P01 — An Exact Computer-Assisted Resolution of the Binary (n,k,r)=(5,3,3) Frankl–Tokushige Instance

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-L260905848-P01_An_Exact_Computer_Assisted_Resolution_of_the_Binary_n_k_r_5_3_3_FranklTokushige_Instance.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-L260905848-P01/)

Original ID / 原始编号: `lit-260905848-p01`. Origin / 来源: 本地文献跟进.

## Accepted scope / 已接受范围

Resolution of the frozen statement · proved / 冻结命题的证明／反证（见精确范围） · proved.

Let V = F_2^5. For i = 1,2,3 let F_i be a family of 3-dimensional linear subspaces of V, and suppose dim(U_1 intersection U_2 intersection U_3) &gt;= 1 for every choice U_i in F_i. Then &#124;F_1&#124;&#124;F_2&#124;&#124;F_3&#124; &lt;= 35^3 = 42875. Equality holds if and only if there is a 1-dimensional subspace L &lt;= V such that, for every i, F_i is the full star of all 3-subspaces containing L.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-L260905848-P01
```

- `source/evidence/nonstar_equality.cnf` ← `compressed/evidence/nonstar_equality.cnf.gz` (44431500 original bytes)
- `source/evidence/product_above_bound.cnf` ← `compressed/evidence/product_above_bound.cnf.gz` (44439753 original bytes)

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-L260905848-P01
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/build_rref_hypergraph.py`
- `evidence/cnf_equality_classification.py`
- `evidence/cnf_product_threshold.py`
- `evidence/cpsat_product_search.py`
- `evidence/run_drat_solver.py`
- `evidence/triage_sanity.py`
- `evidence/verify_reductions.py`

Bounded replay status in this packaging task: **passed**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.

Counts the 155 three-dimensional subspaces of F2^5, the 35-member star, and the exact ordered-triple intersection distribution.

## Dependencies and limitations / 依赖与限制

- ortools
- pysat

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
