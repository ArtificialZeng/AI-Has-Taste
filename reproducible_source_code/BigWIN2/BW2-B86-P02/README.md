# BW2-B86-P02 — The Disconnected Graph A(4,4,3): Classification and a Counterexample to Pan's arXiv-v1 Conjecture

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B86-P02_The_Disconnected_Graph_A_4_4_3_Classification_and_a_Counterexample_to_Pan_s_arXiv_v1_Conjecture.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B86-P02/)

Original ID / 原始编号: `win-00086-p02`. Origin / 来源: 86.

## Accepted scope / 已接受范围

Resolution of the frozen statement · disproved / 冻结命题的证明／反证（见精确范围） · disproved.

Let F_1 be the permutations of S_4 with exactly one fixed point and use Pan's left-Cayley convention. Then F_1 is the set of eight 3-cycles and equals A_4 minus V_4, where V_4={1,(12)(34),(13)(24),(14)(23)}. The graph Cay(S_4,F_1) is isomorphic to A(4,4,3) and to the disjoint union 2K_{4,4,4}; its two components are the parity classes and the three parts in each component are the left V_4-cosets. Its full graph automorphism group is (S_4 wr S_3) wr S_2, of order 13,759,414,272. Pan's Conjecture 3.1 in arXiv:2407.19745v1 prescribes a group of order 1,152 at (n,t)=(4,1), so that conjecture is disproved at this parameter.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B86-P02
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B86-P02
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/triage_exact_check.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- No third-party Python import detected by static inspection; this is not a tested environment lock.

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
