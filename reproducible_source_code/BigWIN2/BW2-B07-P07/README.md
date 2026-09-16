# BW2-B07-P07 — Links–Gould positivity for two-block alternating 2-bridge knots

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B07-P07_Links_Gould_positivity_for_two_block_alternating_2_bridge_knots.pdf) · [LaTeX entry / 入口](source/paper/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B07-P07/)

Original ID / 原始编号: `legacy-b07-p07`. Origin / 来源: 7.

## Accepted scope / 已接受范围

Historically gated final manuscript; see accepted scope / 历史门控终稿；见已接受范围.

Two-block alternating 2-bridge knots for all p,q&gt;=1; Ishii's full conjecture unresolved.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B07-P07
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B07-P07
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `certificate/double_twist_certificate.py`
- `certificate/verify_double_twist_sympy.py`
- `code/lg_exact.py`
- `code/lg_v1_sympy.py`
- `code/run_checks.sh`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- Bash, Python 3, SymPy>=1.10.

- The required requirements.txt exists only in the release ZIP, with contents sympy>=1.10; retain its exact member or state the dependency in the new source README.
- Original entrypoints: ['bash code/run_checks.sh']
- Long/full or external-tool entrypoints: []

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
