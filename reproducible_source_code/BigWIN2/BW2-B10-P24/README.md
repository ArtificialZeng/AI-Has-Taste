# BW2-B10-P24 — The Strict-Pair Product Extremal Value at 62 Is 31

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B10-P24_The_Strict_Pair_Product_Extremal_Value_at_62_Is_31.pdf) · [LaTeX entry / 入口](source/paper/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B10-P24/)

Original ID / 原始编号: `legacy-b10-p24`. Origin / 来源: 10.

## Accepted scope / 已接受范围

Historically gated final manuscript; see accepted scope / 历史门控终稿；见已接受范围.

Strict-pair finite equality F(62)=31; no asymptotic or higher-product resolution.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B10-P24
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B10-P24
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `computation/verifiers/exact_cover_verify.py`
- `computation/verifiers/small_crosscheck.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- Python 3 standard library; OR-Tools was used only for discovery and is not needed for this verifier.

- PDF_AUDIT.md has a stale trailing 'Status: not yet run'; later ROOT_DELIVERY_AUDIT.md is the terminal delivery authority.
- Original LaTeX ZIP contains no computation; add both local verifier scripts.
- Original entrypoints: ['python3 computation/verifiers/small_crosscheck.py', 'python3 computation/verifiers/exact_cover_verify.py']
- Long/full or external-tool entrypoints: []

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
