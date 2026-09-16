# BW2-PR20260914-triangular_square_roots — Simple negative roots for the rows of the Delannoy matrix square

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-PR20260914-triangular_square_roots_Simple_negative_roots_for_the_rows_of_the_Delannoy_matrix_square.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-PR20260914-triangular_square_roots/)

Original ID / 原始编号: `primary-20260914-triangular-square-roots`. Origin / 来源: primary-20260914.

## Accepted scope / 已接受范围

Partial-result note; parent problem not fully solved / 部分结果札记；母题未完整解决.

Let D(n,k) count paths from (0,0) to (n-k,k) using steps (1,0), (0,1), and (1,1), with D(n,k)=0 outside 0&lt;=k&lt;=n and the empty path counted once. For the ordinary matrix square define G_n(x)=sum_{k=0}^n sum_{i=k}^n D(n,i)D(i,k)x^k. Then G_0=1, and for every integer n&gt;=1, G_n is monic of degree n and has n distinct real roots, all in the open interval (-4-3\*sqrt(2), -3+2\*sqrt(2)). This claim concerns only D^2; it does not assert the A^2 part of the frozen original or consecutive interlacing.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-PR20260914-triangular_square_roots
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-PR20260914-triangular_square_roots
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/phase_checks.py`
- `evidence/replay_phase_certificates.py`
- `evidence/triage_checks.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- mpmath
- sympy

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- The original question is unresolved; the released artifact is a partial result or unproved conjecture, according to its frozen claim.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
