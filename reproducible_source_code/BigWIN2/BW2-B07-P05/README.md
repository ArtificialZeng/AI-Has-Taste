# BW2-B07-P05 — Exact Optimization of the Comellas--Yebra Three-Parameter Family for Ten Points in the Square

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B07-P05_Exact_Optimization_of_the_Comellas_Yebra_Three_Parameter_Family_for_Ten_Points_in_the_Square.pdf) · [LaTeX entry / 入口](source/paper/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B07-P05/)

Original ID / 原始编号: `legacy-b07-p05`. Origin / 来源: 7.

## Accepted scope / 已接受范围

Historically gated final manuscript; see accepted scope / 历史门控终稿；见已接受范围.

Full Comellas-Yebra three-parameter cube, including degenerate/unordered values and equality cases; not unrestricted ten-point Heilbronn.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B07-P05
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B07-P05
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `certificates/generate_family_cover.py`
- `certificates/verify_analytic_identities.py`
- `certificates/verify_family_cover.py`
- `certificates/verify_incumbent_stdlib.py`
- `certificates/verify_incumbent_sympy.py`
- `experiments/asymmetric_search.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- Python 3 standard library; optional independent analytic checks use SymPy.

- Current PDF is bound by PDF_AUDIT and output/release_manifest.json; the overall unrestricted problem remains open.
- Original entrypoints: ['python3 certificates/verify_incumbent_stdlib.py', 'python3 certificates/verify_family_cover.py certificates/family_cover.json']
- Long/full or external-tool entrypoints: []

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
