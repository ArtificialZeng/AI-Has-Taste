# BW2-PR20260913-multiset_rook — A counterexample to multiset rook-Eulerian interlacing

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-PR20260913-multiset_rook_A_counterexample_to_multiset_rook_Eulerian_interlacing.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-PR20260913-multiset_rook/)

Original ID / 原始编号: `primary-20260913-multiset-rook`. Origin / 来源: primary.

## Accepted scope / 已接受范围

Resolution of the frozen statement · disproved / 冻结命题的证明／反证（见精确范围） · disproved.

Under Definitions 5, 8, 9 and equations (10)--(12) of Alexandersson--Jal--Quemener, arXiv:2502.05939v1, take the non-skew Ferrers board lambda=(3,3,3,3,4,4) and content alpha=(2,2,1,1). There are exactly 60 legal words with strict adjacent ascents and no sentinel, and the first-entry refinements are R3=t(t^2+8t+3), R2=t(8t^2+15t+1), and R1=t^2(t+7)(2t+1). The sequence (R3,R2,R1) is not interlacing: its required ordered pair R3 preceq R1 fails because their degrees are 3 and 4 and minroot(R3)=-4-sqrt(13)&lt;-7=minroot(R1). Thus the interlacing clause of Conjecture 28 is false, disproving the exact original conjunction frozen in source.md. This does not decide the separately quantified total real-rootedness clause. Indeed, all three refinements and the total R=2t(t^3+12t^2+15t+2) in this witness are real-rooted. No minimality or universal total-polynomial counterexample is asserted.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-PR20260913-multiset_rook
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-PR20260913-multiset_rook
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/multiset-rook-calibration.py`
- `evidence/research-verify-six-letter.py`
- `evidence/triage-interlacing.py`
- `evidence/verify-six-letter.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- sympy

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
