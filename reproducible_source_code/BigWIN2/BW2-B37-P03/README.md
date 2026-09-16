# BW2-B37-P03 — A 2-adic obstruction for an eighteen-variable rational moment system

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B37-P03_A_2_adic_obstruction_for_an_eighteen_variable_rational_moment_system.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B37-P03/)

Original ID / 原始编号: `win-00037-p03`. Origin / 来源: 37.

## Accepted scope / 已接受范围

Resolution of the frozen statement · disproved / 冻结命题的证明／反证（见精确范围） · disproved.

There is no tuple (x_1,...,x_18) in Q^18 satisfying sum_j x_j^2 = 9, sum_j x_j^4 = 27/4, and sum_j x_j^6 = 45/8, with no distinctness, nonzero-coordinate, or interval restriction.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B37-P03
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B37-P03
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/triage_pair_search.py`
- `evidence/verify_mod32_obstruction.py`

Bounded replay status in this packaging task: **passed**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.

Exact modulo-32 dynamic-programming obstruction for the three target residue states in 18 coordinates.

## Dependencies and limitations / 依赖与限制

- No third-party Python import detected by static inspection; this is not a tested environment lock.

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
