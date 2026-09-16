# BW2-B06-P07 — Starlike Trees and the Diameter Conjecture for Multiset Dimension

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B06-P07_Starlike_Trees_and_the_Diameter_Conjecture_for_Multiset_Dimension.pdf) · [LaTeX entry / 入口](source/paper/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B06-P07/)

Original ID / 原始编号: `legacy-b06-p07`. Origin / 来源: 6.

## Accepted scope / 已接受范围

Historically gated final manuscript; see accepted scope / 历史门控终稿；见已接受范围.

Starlike-tree partial theorem and finite certificate; unrestricted tree conjecture remains open.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B06-P07
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B06-P07
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `scripts/compare_finite_reports.py`
- `scripts/explore_trees.py`
- `scripts/verify_finite_range.py`
- `scripts/verify_starlike_construction.py`
- `tests/test_exact_evaluators.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- Python 3 and NetworkX 3.4.2 for the listed test; independent finite verifier is standard library.

- Final PDF_AUDIT records a root comma correction followed by rebuild and reinspection; audit/release_manifest.json binds that version.
- Original entrypoints: ['python3 tests/test_exact_evaluators.py']
- Long/full or external-tool entrypoints: []

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
