# BW2-B17-P06 — The Exact Value of the Finite Erdős–Ruzsa Covering Invariant at 41

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B17-P06_The_Exact_Value_of_the_Finite_Erdos_Ruzsa_Covering_Invariant_at_41.pdf) · [LaTeX entry / 入口](source/paper/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B17-P06/)

Original ID / 原始编号: `legacy-b17-p06`. Origin / 来源: 17.

## Accepted scope / 已接受范围

Historically gated final manuscript; see accepted scope / 历史门控终稿；见已接受范围.

Finite invariant at 41; asymptotic Erdős problem remains open.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B17-P06
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B17-P06
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `code/bruteforce_crosscheck.py`
- `code/exact_search.py`
- `code/verify_certificate.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- Python 3 standard library; recorded full replay about seven minutes.

- Discovery SciPy/HiGHS is not required for certification.
- Original entrypoints: ['python3 code/verify_certificate.py certificates/mu41_witness.json', 'python3 code/bruteforce_crosscheck.py', 'python3 code/exact_search.py --n 41 --witness certificates/mu41_witness.json --output verification_result.json']
- Long/full or external-tool entrypoints: []

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
