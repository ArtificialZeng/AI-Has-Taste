# BW2-B67-P04 — Exact Sprague–Grundy Words for the Three-Move Subtraction Games {2,5,c}

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B67-P04_Exact_Sprague_Grundy_Words_for_the_Three_Move_Subtraction_Games_2_5_c.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B67-P04/)

Original ID / 原始编号: `win-00067-p04`. Origin / 来源: 67.

## Accepted scope / 已接受范围

Resolution of the frozen statement · proved / 冻结命题的证明／反证（见精确范围） · proved.

For every integer c&gt;5 with c!=7, Conjecture 50 of arXiv:2609.05358v1 holds for the subtraction game S={2,5,c}. More precisely, the source-proved residues 1,2,3,5,6 modulo 7 are purely periodic. In the two remaining residues the exact Sprague-Grundy words and minimal parameters are: for every K&gt;=1, g_{7K+4}=(0011021)^K 0011223 (021021 (0011021)^K)^infinity with (q,p)=(7K+7,7K+6)=(c+3,c+2); and for every K&gt;=2, g_{7K}=(0011021)^K 32203103 (1 (0011021)^(K-1) 02102102)^infinity with (q,p)=(7K+8,7K+2)=(c+8,c+2). Thus both uncovered residue classes have positive minimal preperiod, completing the conjecture on the entire frozen shape.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B67-P04
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B67-P04
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/verify_words.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- No third-party Python import detected by static inspection; this is not a tested environment lock.

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
