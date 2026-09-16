# BW2-B62-P03 — Exact Diameters and Sorting Times for Full Cycles of Orders 6, 7, and 8

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B62-P03_Exact_Diameters_and_Sorting_Times_for_Full_Cycles_of_Orders_6_7_and_8.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B62-P03/)

Original ID / 原始编号: `win-00062-p03`. Origin / 来源: 62.

## Accepted scope / 已接受范围

Resolution of the frozen statement · proved / 冻结命题的证明／反证（见精确范围） · proved.

For Gamma_n exactly as defined in source.md, the exact pairs (D_n, Sort_n) are (7,6) for n=6, (10,10) for n=7, and (14,13) for n=8. Lexicographically selected diameter witnesses are ((1,2,3,5,6,4),(1,5,3,4,2,6)), ((1,2,3,4,5,6,7),(1,6,5,4,3,2,7)), and ((1,2,3,4,7,8,5,6),(1,8,5,4,2,7,6,3)); selected sorting witnesses are (1,5,4,3,2,6), (1,6,5,4,3,2,7), and (1,7,6,4,5,3,2,8). The evidence gives explicit shortest conjugation paths and certifies the upper bounds by exhaustive exact BFS from every one of the (n-1)! vertices in two distinct encodings.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B62-P03
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B62-P03
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/verifier_a.py`
- `evidence/verifier_b.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- No third-party Python import detected by static inspection; this is not a tested environment lock.

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
