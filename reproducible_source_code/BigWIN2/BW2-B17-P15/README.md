# BW2-B17-P15 — A Certified Upper Bound for the Supremum of an Autoconvolution

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B17-P15_A_Certified_Upper_Bound_for_the_Supremum_of_an_Autoconvolution.pdf) · [LaTeX entry / 入口](source/paper/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B17-P15/)

Original ID / 原始编号: `legacy-b17-p15`. Origin / 来源: 17.

## Accepted scope / 已接受范围

Historically gated final manuscript; see accepted scope / 历史门控终稿；见已接受范围.

Exact-certification note only; explicitly not a new numerical live record, not a sharp constant or global infimum.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B17-P15
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B17-P15
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `source-root`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `certificates/verifier.cpp`
- `certificates/verifier.py`
- `tests/breaker_step_formula.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- Python 3 standard library; the C++ alternative was not compiled in the root audit.

- Batch final audit distinguishes this from the five new submission-manuscript results: public label must retain 'exact-certification note'.
- PDF audit's hash condition is satisfied by current PDF matching results/release/MANIFEST.json and batch_release_manifest.json.
- Stale 'not yet run' footers are superseded by explicit independent root and batch release evidence.
- Original entrypoints: ['python3 certificates/verifier.py --self-test', 'python3 certificates/verifier.py certificates/witness.txt', 'python3 tests/breaker_step_formula.py']
- Long/full or external-tool entrypoints: []

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
