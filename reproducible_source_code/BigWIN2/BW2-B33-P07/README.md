# BW2-B33-P07 — Conjectural Infinite Binary-Kernel Rank for Three Subsequences of A182510 (Original Eight-Zero Problem Unresolved)

[Final PDF / 最终稿](../../../pdfs/ai-conjecture/BW2-B33-P07_Conjectural_Infinite_Binary_Kernel_Rank_for_Three_Subsequences_of_A182510_Original_Eight_Zero_Problem_Unresol.pdf) · [LaTeX entry / 入口](source/conjecture-note/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B33-P07/)

Original ID / 原始编号: `Win33-p07`. Origin / 来源: 33.

## Accepted scope / 已接受范围

Conjectural note; original problem unresolved / 猜想札记；原问题仍未解决.



The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B33-P07
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B33-P07
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `experiments/analyze_handoff_extensions.py`
- `experiments/analyze_kernel_rank.py`
- `experiments/analyze_structural_hints.py`
- `experiments/analyze_zero_lifts.py`
- `experiments/falsify_modular_theorem.py`
- `experiments/fast_zero_search.py`
- `experiments/iterate_xor.py`
- `experiments/test_lift_state_features.py`
- `experiments/verify_exact.py`
- `experiments/verify_fast_zero_search.py`
- `experiments/verify_handoff_extensions.py`
- `experiments/verify_kernel_rank.py`
- `experiments/verify_lift_state_features.py`
- `experiments/verify_modular_falsification.py`
- `experiments/verify_structural_hints.py`
- `experiments/verify_zero_lifts.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- numba
- numpy
- sympy

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- The original question is unresolved; the released artifact is a partial result or unproved conjecture, according to its frozen claim.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
