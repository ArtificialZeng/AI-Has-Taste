# BW2-B87-P04 — Coloop Multiplication for Radial Mobius Hilbert Series

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B87-P04_Coloop_Multiplication_for_Radial_Mobius_Hilbert_Series.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B87-P04/)

Original ID / 原始编号: `win-00087-p04`. Origin / 来源: 87.

## Accepted scope / 已接受范围

Resolution of the frozen statement · proved / 冻结命题的证明／反证（见精确范围） · proved.

Let G be a connected simple graph with 1 &lt;= &#124;V(G)&#124; &lt;= 5, and define its cycle-matroid flats, the lowering operators L_e and D, the cyclic spaces C_j, H_M(q), the coloop extension M^+, and Delta_G(q) exactly as frozen in source.md and interpreted in problem.md. Then Delta_G(q)=0 for every graph on at most four vertices. On five vertices, Delta_G(q) is nonzero if and only if the complement of G is a linear forest. For complement types P5, P4+P1, and P3+P2 it equals 2q^2+2q^3; for P3+2P1 it equals q^2+2q^3; and for 2P2+P1, P2+3P1, and 5P1 it equals 4q^2. Within this frozen range, five is the first failing order and the unique least-edge failure among the five-vertex graphs has six edges: K5-P5, isomorphic to Theta(1,2,3), with Hilbert vectors (1,6,11,6,1) and (1,7,19,19,7,1) before and after adjoining the coloop.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B87-P04
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B87-P04
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/independent_subset_check.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- No third-party Python import detected by static inspection; this is not a tested environment lock.

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- {'path': '/home/ailab/4math-open-problems/projects/win-00087-p04/evidence/triage_replay.md', 'indicators': ['absolute-local-path']}
- {'path': '/home/ailab/4math-open-problems/projects/win-00087-p04/evidence/finite_classification_proof.md', 'indicators': ['absolute-local-path']}
- {'path': '/home/ailab/4math-open-problems/projects/win-00087-p04/evidence/subset_closure_census.json', 'indicators': ['absolute-local-path']}

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
