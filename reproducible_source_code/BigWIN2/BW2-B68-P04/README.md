# BW2-B68-P04 — Exact Maximal Dynamics of the Normalized Inverse-Weight Lin–Lu–Yau Flow on a Weighted Triangle

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B68-P04_Exact_Maximal_Dynamics_of_the_Normalized_Inverse_Weight_LinLuYau_Flow_on_a_Weighted_Triangle.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B68-P04/)

Original ID / 原始编号: `win-00068-p04`. Origin / 来源: 68.

## Accepted scope / 已接受范围

Resolution of the frozen statement · proved / 冻结命题的证明／反证（见精确范围） · proved.

For the literal normalized inverse-weight LLY flow on the labelled weighted triangle in source.md, all three curvatures are finite exactly on G={(a,b,c)&gt;0:a+b+c=1, max(a,b,c)&lt;=1/2}. On G they are given, for an edge x with other lengths y,z and M=max(y,z), m=min(y,z), by k_x=1+M(x+2m-M)/((x+y)(x+z)); the normalized vector field F_x=-x(k_x-sum_u u k_u) is locally Lipschitz, G is forward invariant, and every datum in G has a unique global classical trajectory that reaches neither a new ordering wall nor the non-finiteness locus in finite time. After permuting labels so a&gt;=b&gt;=c, every trajectory is exactly one of: the constant equal point; a&gt;b=c, converging to (1/2,1/4,1/4); or b&gt;c (allowing a=b), converging to (1/2,1/2,0). The only equilibria in G are (1/3,1/3,1/3) and the three labelled permutations of (1/2,1/4,1/4), and the corresponding singleton limits are all omega-limit sets.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B68-P04
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B68-P04
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/verify_chamber_dynamics.py`
- `evidence/verify_edge12_lp.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- sympy

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
