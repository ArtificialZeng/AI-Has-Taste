# BW2-B08-P02 — An Eight-Element Counterexample to Real-Rootedness of Preorder Support Polynomials

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B08-P02_An_Eight_Element_Counterexample_to_Real_Rootedness_of_Preorder_Support_Polynomials.pdf) · [LaTeX entry / 入口](source/paper/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B08-P02/)

Original ID / 原始编号: `legacy-b08-p02`. Origin / 来源: 8.

## Accepted scope / 已接受范围

Historically gated final manuscript; see accepted scope / 历史门控终稿；见已接受范围.

Independent exact certification of Shivam Patel's previously posted MathDB witness; do not claim discovery priority.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B08-P02
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B08-P02
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `code/run_all_checks.sh`
- `code/test_small_cases.py`
- `code/verify_branch_formula.py`
- `code/verify_counterexample.py`
- `code/verify_sturm.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- Python 3 standard-library exact rational arithmetic.

- Strip archive wrapper preorder_counterexample/. Exclude logs/.
- Original entrypoints: ['python3 code/verify_counterexample.py', 'python3 code/verify_branch_formula.py', 'python3 code/verify_sturm.py']
- Long/full or external-tool entrypoints: []

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
