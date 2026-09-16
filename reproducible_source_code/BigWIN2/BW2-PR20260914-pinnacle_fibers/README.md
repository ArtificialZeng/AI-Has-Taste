# BW2-PR20260914-pinnacle_fibers — A counterexample to distributivity of fixed pinnacle-order fibers

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-PR20260914-pinnacle_fibers_A_counterexample_to_distributivity_of_fixed_pinnacle_order_fibers.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-PR20260914-pinnacle_fibers/)

Original ID / 原始编号: `primary-20260914-pinnacle-fibers`. Origin / 来源: primary.

## Accepted scope / 已接受范围

Resolution of the frozen statement · disproved / 冻结命题的证明／反证（见精确范围） · disproved.

Let P_5((5)) be all permutations of \[5\] whose complete left-to-right list of interior pinnacle values is exactly (5), with endpoints excluded from peaks. Order this fiber by coordinatewise comparison of I_v(pi), the number of values smaller than v to the right of v. This nonempty induced poset is not a distributive lattice. An exact witness consists of e=12354, b=12534, a=13524, c=13452, d=13542. All five lie in the fiber, and their meets and joins computed among every element of the fiber satisfy b join c=d, a meet d=a, a meet b=b, a meet c=e, b join e=b, with a different from b. Thus a meet (b join c) differs from (a meet b) join (a meet c). This disproves the universal assertion asked in Liang--Sagan Question 8.6(a) in the published version, equivalently Question 8.7(a) of arXiv:2408.02782v1, including its explicitly qualified nonempty-fiber version. No assertion about counting part (b), minimality in n, or a classification of other fibers is submitted.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-PR20260914-pinnacle_fibers
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-PR20260914-pinnacle_fibers
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/recovery_check.py`
- `evidence/research_certificate.py`
- `evidence/triage_exact.py`
- `evidence/verify_triage.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- No third-party Python import detected by static inspection; this is not a tested environment lock.

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
