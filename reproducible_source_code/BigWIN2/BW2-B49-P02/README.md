# BW2-B49-P02 — Strong Optimality of Two-Color Permutation Wordle at n=3

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B49-P02_Strong_Optimality_of_Two_Color_Permutation_Wordle_at_n_3.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B49-P02/)

Original ID / 原始编号: `win-00049-p02`. Origin / 来源: 49.

## Accepted scope / 已接受范围

Resolution of the frozen statement · proved / 冻结命题的证明／反证（见精确范围） · proved.

For the exact two-color Permutation Wordle game at n=3 frozen in source.md and interpreted in problem.md, the optimal deterministic success counts are (N_1,N_2,N_3,N_4,N_5,N_6)=(1,8,24,40,47,48), and N_r=48 for every r&gt;=6. The Kutin--Smithline multicolor CircularShift algorithm, read by its circuit-completion prose, Figure 6, and the proof of Lemma 4.4 in arXiv:2408.00903v3, has exact-round counts (1,7,16,16,7,1) and therefore attains N_r simultaneously for every r&gt;=1. The displayed color-update cases in Definition 4.3 conflict with those parts of the primary source; this claim uses the exact operational interpretation documented in evidence/circular-shift-interpretation.md and does not assert that the inconsistent displayed cases literally produce the same strategy.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B49-P02
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B49-P02
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/bellman_exact.cpp`
- `evidence/bellman_exact.py`
- `evidence/circular_shift_sim.py`
- `evidence/verify_bellman_certificate.py`
- `evidence/verify_circular_shift_transcripts.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- No third-party Python import detected by static inspection; this is not a tested environment lock.

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
