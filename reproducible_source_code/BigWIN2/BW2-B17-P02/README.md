# BW2-B17-P02 — The Exact Value of a Pairwise-GCD Sunflower-Free Function at 126

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B17-P02_The_Exact_Value_of_a_Pairwise_GCD_Sunflower_Free_Function_at_126.pdf) · [LaTeX entry / 入口](source/paper/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B17-P02/)

Original ID / 原始编号: `legacy-b17-p02`. Origin / 来源: 17.

## Accepted scope / 已接受范围

Historically gated final manuscript; see accepted scope / 历史门控终稿；见已接受范围.

Certified finite equality at N=126.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B17-P02
```

- `source/certificates/f3_126_ge17.drat` ← `compressed/certificates/f3_126_ge17.drat.gz` (417189026 original bytes)

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B17-P02
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `code/crosscheck_small.py`
- `code/generate_cnf.py`
- `code/solve_with_proof.py`
- `code/verify_witness.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- Witness: Python 3 stdlib. Encoding cross-check: python-sat 1.8.dev24. Proof replay: external drat-trim (audited version 0.0~git20240428.effa1dc-2).

- The proof certificate is 417,189,026 bytes; do not silently omit it or publish only the witness as complete reproducibility.
- Do not copy bundled binaries, environment dumps or raw logs; public README must replace bundled binary paths with an external drat-trim command.
- Use an appropriate large-file/release-asset mechanism for the proof if ordinary Git storage cannot carry it.
- Original entrypoints: ['python3 code/verify_witness.py certificates/witness_126_16.json --n 126 --size 16', 'python3 code/crosscheck_small.py', 'drat-trim certificates/f3_126_ge17.cnf certificates/f3_126_ge17.drat']
- Long/full or external-tool entrypoints: []

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
