# BW2-PR20260914-lorentzian_cliques — Two-vertex cuts and a Lorentzian obstruction for bistable bipartite graphs

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-PR20260914-lorentzian_cliques_Two_vertex_cuts_and_a_Lorentzian_obstruction_for_bistable_bipartite_graphs.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-PR20260914-lorentzian_cliques/)

Original ID / 原始编号: `primary-20260914-lorentzian-cliques`. Origin / 来源: primary.

## Accepted scope / 已接受范围

Partial-result note; parent problem not fully solved / 部分结果札记；母题未完整解决.

For every integer k&gt;=2 and every finite connected simple bipartite graph F with parts L,R of size k whose only maximum independent sets are L and R, set A=\[\[0,1,1\],\[1,0,1\],\[1,1,1\]\], f=Z_(F,A) with the unnormalized labeled-assignment convention in problem.md, beta=(k-1,k-1,0), and c=\[x1^(k-1)x2^(k-1)x3^2\]f. For distinct u,v let q(u,v) be the number of connected components of F-{u,v}, including isolated vertices; let s count unordered pairs within L or within R for which q(u,v)&gt;1. Then c=sum_(u in L,v in R)2^q(u,v)+2s and Hessian(partial^beta f)=2(k!)^2 \[\[0,1,1\],\[1,0,1\],\[1,1,c/k^2\]\]. In particular c&gt;=2k^2, with equality exactly when F has no two-vertex cut. Such F is 2-connected. The selected Hessian has two positive eigenvalues exactly when F is not 3-connected, proving that f is not Lorentzian in that case; A is admissible with spectrum -1,1-sqrt(2),1+sqrt(2). If F is 3-connected this Hessian has one positive, one negative, and one zero eigenvalue, without any assertion that f itself is Lorentzian. Corollaries: c=6k(k-1) for C_(2k), k&gt;=2; c=2k^2 for K_(k,k), k&gt;=3; c=12 for K_(2,2)=C4. The original universal connected-clique characterization remains unresolved.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-PR20260914-lorentzian_cliques
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-PR20260914-lorentzian_cliques
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/cycles.py`
- `evidence/probe.py`
- `evidence/recovery-check.py`
- `evidence/separator-check.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- sympy

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- The original question is unresolved; the released artifact is a partial result or unproved conjecture, according to its frozen claim.
- {'path': '/home/ailab/4math-open-problems/projects/primary-20260914-lorentzian-cliques/evidence/source-bindings.json', 'indicators': ['absolute-local-path']}
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
