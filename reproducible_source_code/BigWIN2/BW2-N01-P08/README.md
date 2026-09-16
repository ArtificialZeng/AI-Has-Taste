# BW2-N01-P08 — The NNE distribution on Fuss–Catalan paths with a fixed number of peaks

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-N01-P08_The_NNE_distribution_on_FussCatalan_paths_with_a_fixed_number_of_peaks.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-N01-P08/)

Original ID / 原始编号: `newwin-00001-p08`. Origin / 来源: 新WIN-1批次.

## Accepted scope / 已接受范围

Resolution of the frozen statement · proved / 冻结命题的证明／反证（见精确范围） · proved.

For every pair of integers m&gt;=2,n&gt;=1 and every integer 1&lt;=k&lt;=n, let W^(m)_(n,k)(t) sum t^nne(D) over all N=(0,1),E=(1,0) paths from (0,0) to (n,mn) whose every prefix satisfies #N&gt;=m#E and which have exactly k consecutive NE factors; nne(D) counts consecutive NNE factors, without cyclic counting. Then W^(m)_(n,k)(t)=(binom(n,k)/n)\*sum_{j=1}^k binom(k,j)\*binom(mn-k,j-1)\*t^j. This polynomial has degree k, a simple root at 0, and k-1 distinct strictly negative roots, so every complex zero is real, proving the complete assertion of source.md.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-N01-P08
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-N01-P08
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/check-p08-small.py`
- `evidence/check-research.py`
- `evidence/check-triage-first-return.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- sympy

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
