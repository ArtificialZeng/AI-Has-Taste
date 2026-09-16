# BW2-B06-P01 — The least degree of a two-variable polynomial identity for M₃(𝔽₂) is seven

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B06-P01_The_least_degree_of_a_two_variable_polynomial_identity_for_M3_F2_is_seven.pdf) · [LaTeX entry / 入口](source/paper/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B06-P01/)

Original ID / 原始编号: `legacy-b06-p01`. Origin / 来源: 6.

## Accepted scope / 已接受范围

Historically gated final manuscript; see accepted scope / 历史门控终稿；见已接受范围.

The fixed M3(F2) two-variable polynomial identity problem; least degree exactly seven.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B06-P01
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B06-P01
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `src/breaker_independent.py`
- `src/discover_numpy.py`
- `src/make_certificate.py`
- `src/verify_certificate.py`
- `tests/test_exact.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- Verifier: Python 3 standard library. Optional discovery/tests use NumPy 2.2.6 and Numba 0.67.0.

- The main verifier is a finite full certificate check, not advertised as an instant smoke test.
- Original entrypoints: ['python3 src/verify_certificate.py certificates/min_degree_7.json']
- Long/full or external-tool entrypoints: []

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
