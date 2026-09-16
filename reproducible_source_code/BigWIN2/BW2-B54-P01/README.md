# BW2-B54-P01 — Minimum Shift-Equivalence Lag for the 2 × 2 k = 11 Baker Pair: A Partial Result on Strong Shift Equivalence

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B54-P01_Minimum_Shift_Equivalence_Lag_for_the_2_x_2_k_11_Baker_Pair_A_Partial_Result_on_Strong_Shift_Equival.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B54-P01/)

Original ID / 原始编号: `win-00054-p01`. Origin / 来源: 54.

## Accepted scope / 已接受范围

Partial-result note; parent problem not fully solved / 部分结果札记；母题未完整解决.

Let A=\[\[1,12\],\[11,1\]\] and B=\[\[1,132\],\[1,1\]\]. If L&gt;=1 and R,S are 2-by-2 matrices over the nonnegative integers satisfying AR=RB, SA=BS, RS=A^L, and SR=B^L, then L&gt;=22. Such R,S exist at L=22, so 22 is the minimum lag within this precisely delimited 2-by-2 class. Consequently every strong-shift-equivalence chain from A to B, if one exists, has at least 22 elementary steps, because an m-step chain composes to a 2-by-2 shift equivalence of lag m. This does not settle whether any such unrestricted chain exists.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B54-P01
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B54-P01
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/lag1_22_2x2_minimality.py`
- `evidence/lag4_shift_equivalence.py`
- `evidence/triage_check.py`

Bounded replay status in this packaging task: **passed**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.

Exact finite arithmetic/discriminant check for the coded 2-by-2 lag-four nonnegative shift-equivalence obstruction.

## Dependencies and limitations / 依赖与限制

- No third-party Python import detected by static inspection; this is not a tested environment lock.

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- The original question is unresolved; the released artifact is a partial result or unproved conjecture, according to its frozen claim.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
