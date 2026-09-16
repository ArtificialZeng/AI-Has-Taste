# BW2-B66-P02 — The Smallest Abelian Cayley Graphs with a Goemans–Linial Gap

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B66-P02_The_Smallest_Abelian_Cayley_Graphs_with_a_GoemansLinial_Gap.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B66-P02/)

Original ID / 原始编号: `win-00066-p02`. Origin / 来源: 66.

## Accepted scope / 已接受范围

Resolution of the frozen statement · proved / 冻结命题的证明／反证（见精确范围） · proved.

For every admissible finite Abelian Cayley presentation in source.md, the least group order for which psi(G) &gt; SDP_GL(G) is 10. Every admissible presentation of order at most 9 is exact. The 16 group-automorphism orbits of admissible presentations on Z_10 give 16 pairwise nonisomorphic graphs, and exactly three are non-exact: S={1,3,7,9}, with (psi,SDP_GL)=(4/5,3/4); S={1,4,6,9}, with (psi,SDP_GL)=(4/5,(15+sqrt(5))/22); and S={1,2,5,8,9}, with (psi,SDP_GL)=(5/6,(10+sqrt(5))/15). Thus these are precisely the three order-ten non-exact graph-isomorphism classes, and each has one Cayley-presentation orbit.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B66-P02
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B66-P02
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/cyclic_orbits.py`
- `evidence/exact_cyclic_gl.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- sympy

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
