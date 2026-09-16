# BW2-N01-P12 — All partition-restricted counts of nondegenerate 2 by 4 by 3 hypermatrices

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-N01-P12_All_partition_restricted_counts_of_nondegenerate_2_by_4_by_3_hypermatrices.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-N01-P12/)

Original ID / 原始编号: `newwin-00001-p12`. Origin / 来源: 新WIN-1批次.

## Accepted scope / 已接受范围

Resolution of the frozen statement · proved / 冻结命题的证明／反证（见精确范围） · proved.

For every prime power q and every pair of weakly decreasing nonnegative integer triples lambda and mu with mu_j &lt;= lambda_j, lambda_j &lt;= 4-j and mu_j &lt;= 3-j for j=1,2,3, the number of ordered pairs (A,B) of 4-by-3 matrices over F_q with A_rj=0 whenever r&gt;4-lambda_j and B_rj=0 whenever r&gt;4-mu_j, and with nonzero boundary-format hyperdeterminant, is q^9 (q-1)^6 times product_{j=1}^3 \[5-j-lambda_j\]_q times product_{j=1}^3 \[4-j-mu_j\]_q, where \[r\]_q=sum_{a=0}^{r-1} q^a. Nondegeneracy equivalently means rank(sA+tB)=3 for all nonzero (s,t) over the algebraic closure of F_q. All 55 permitted shapes and all prime powers are included. No assertion for k&gt;3 is made.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-N01-P12
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-N01-P12
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/exhaust_f2.py`
- `evidence/triage_symbolic.py`
- `evidence/verify_sparse.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- numpy

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
