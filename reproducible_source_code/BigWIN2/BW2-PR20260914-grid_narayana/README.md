# BW2-PR20260914-grid_narayana — A Narayana factorization for a truncated two-row grid polytope

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-PR20260914-grid_narayana_A_Narayana_factorization_for_a_truncated_two_row_grid_polytope.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-PR20260914-grid_narayana/)

Original ID / 原始编号: `primary-20260914-grid-narayana`. Origin / 来源: primary.

## Accepted scope / 已接受范围

Resolution of the frozen statement · proved / 冻结命题的证明／反证（见精确范围） · proved.

For every integer n&gt;=1, let P_n=({1,...,n} x {1,2}) minus {(n,2)}, ordered coordinatewise, and Q_n={x&gt;=0: sum_{v in I}x_v&lt;=&#124;I&#124; for every lower ideal I of P_n}. Then sum_{x in Q_n intersect Z^(2n-1)} t^(number of nonzero coordinates of x) equals A_{n-1}(t) B_n(t), where A_r(t)=sum_{j=0}^r binom(r,j)binom(r+1,j)t^j/(j+1) and B_r(t)=sum_{j=0}^r binom(r,j)^2 t^j. This is the entire frozen original claim, with no change of statistic, hypotheses, or parameter range.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-PR20260914-grid_narayana
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-PR20260914-grid_narayana
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/intake-calibration.py`
- `evidence/research-verifier.py`
- `evidence/triage-transfer.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- No third-party Python import detected by static inspection; this is not a tested environment lock.

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
