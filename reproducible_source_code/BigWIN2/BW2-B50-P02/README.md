# BW2-B50-P02 — A Complete Hamiltonicity Atlas for Acyclic-Orientation Flip Graphs Through Six Vertices

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B50-P02_A_Complete_Hamiltonicity_Atlas_for_Acyclic_Orientation_Flip_Graphs_Through_Six_Vertices.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B50-P02/)

Original ID / 原始编号: `win-00050-p02`. Origin / 来源: 50.

## Accepted scope / 已接受范围

Resolution of the frozen statement · proved / 冻结命题的证明／反证（见精确范围） · proved.

Under the two-item cyclic-Gray-code convention fixed in problem.md, for every connected unlabeled loopless simple graph G with 2 &lt;= &#124;V(G)&#124; &lt;= 6, AO(G) has a Hamiltonian cycle if and only if sigma(G)=0. The complete domain has 142 isomorphism classes by orders 2,3,4,5,6 in counts 1,2,6,21,112. Exactly 125 classes are Hamiltonian, in counts 1,2,5,18,99 by order; they are exactly the sigma-zero entries of evidence/atlas-through-6.json and each has the explicit cycle in evidence/hamilton-cycles.json. The other 17 classes are non-Hamiltonian by parity imbalance, with canonical graph6 identifiers C\], DFw, DLs, D\]{, E?~o, E@vg, E@vo, EBj?, EBjW, EBjg, EBz_, EBzw, EB~o, EJeg, EJnW, ELvg, E\]~o. Consequently sigma(G)=0 is sufficient throughout the frozen domain and there are no counterexamples, minimum-order or otherwise, in it.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B50-P02
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B50-P02
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/atlas-enumerate.py`
- `evidence/atlas-verify.py`
- `evidence/hamilton-search.py`
- `evidence/hamilton-verify.py`
- `evidence/triage-smoke.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- networkx
- ortools

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
