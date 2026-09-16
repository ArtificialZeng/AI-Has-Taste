# BW2-B55-P04 — A Four-Job Counterexample to an Almost-Exact Fathoming Rule for Job Sequencing and Tool Switching

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B55-P04_A_Four_Job_Counterexample_to_an_Almost_Exact_Fathoming_Rule_for_Job_Sequencing_and_Tool_Switching.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B55-P04/)

Original ID / 原始编号: `win-00055-p04`. Origin / 来源: 55.

## Accepted scope / 已接受范围

Resolution of the frozen statement · disproved / 冻结命题的证明／反证（见精确范围） · disproved.

The universal claim in source.md is false. For n=m=4, c=3, T_1={1}, T_2={1,2}, T_3={1,3,4}, and T_4={2,3,4}, the unique maximizing unordered PI root pair is {1,4} and the unique next selected job is 3. If the root orientation is (1,4), the generated proper node (3,1,4) is fathomed under its unique KTNS history and has globally optimal completion (2,3,1,4). If the root orientation is (4,1), the generated proper node (4,3,1) is fathomed under its unique KTNS history and has globally optimal completion (2,4,3,1). The remaining job 2 is not covered by any node configuration in either case, so the Section 6.2 completion-pruning condition does not apply. Thus, under either reversal-symmetry orientation, an unsafe node exists with four jobs.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B55-P04
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B55-P04
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- No standalone program is archived; the proof and exact evidence are the reproduction assets.

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- No third-party Python import detected by static inspection; this is not a tested environment lock.

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
