# BW2-B17-P13 — The Exact Finite Sumset Value s(12,38)=65

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B17-P13_The_Exact_Finite_Sumset_Value_s_12_38_65.pdf) · [LaTeX entry / 入口](source/paper/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B17-P13/)

Original ID / 原始编号: `legacy-b17-p13`. Origin / 来源: 17.

## Accepted scope / 已接受范围

Historically gated final manuscript; see accepted scope / 历史门控终稿；见已接受范围.

Exact finite value only; no maximizing-set classification or asymptotic consequence.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B17-P13
```

- `source/certificates/no_66.drup` ← `compressed/certificates/no_66.drup.gz` (35331788 original bytes)

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B17-P13
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `code/crosscheck_small.py`
- `code/discover_cpsat.py`
- `code/discover_local.py`
- `code/sat_decision.py`
- `code/verify_witness.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- Witness: Python 3 stdlib. Encoding cross-check: python-sat 1.8.dev24. Full replay: external drat-trim.

- PROOF_AUDIT.md and PDF_AUDIT.md retain stale 'Status: not yet run' footers; ROOT_PROOF_AUDIT.md, SUBMISSION_AUDIT.md and BATCH_FINAL_AUDIT.md record completed checks.
- The .drup certificate is mandatory proof data; do not exclude by extension.
- Exclude bundled third_party binaries; replace their README command with external drat-trim.
- Original entrypoints: ['python3 code/verify_witness.py certificates/witness_65.json --n 38 --k 12 --minimum 65', 'python3 code/crosscheck_small.py', 'drat-trim certificates/no_66.cnf certificates/no_66.drup']
- Long/full or external-tool entrypoints: []

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
