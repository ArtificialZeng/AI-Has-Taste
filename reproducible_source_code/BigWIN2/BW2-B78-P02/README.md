# BW2-B78-P02 — A Classical-Mass-Action Sensitivity Zero in an Exact Six-Complex Census

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B78-P02_A_Classical_Mass_Action_Sensitivity_Zero_in_an_Exact_Six_Complex_Census.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B78-P02/)

Original ID / 原始编号: `win-00078-p02`. Origin / 来源: 78.

## Accepted scope / 已接受范围

Resolution of the frozen statement · proved / 冻结命题的证明／反证（见精确范围） · proved.

For the ordered complexes (0,X,Y,2X,X+Y,2Y), among all simple directed networks with three or four reactions satisfying rank(S)=2, existence of a strictly positive steady flux, and nonzero independent-symbol det(SR), there does exist a generic-nonzero inverse sensitivity that becomes identically zero under classical mass action on Sv=0. In the canonical species-swap order and the reaction-then-species order fixed in problem.md, the lexicographically first triple is E=(0-&gt;X, 0-&gt;2X, X-&gt;Y, X+Y-&gt;0), reaction rho=0-&gt;X, species m=Y. Its generic signed cofactor is -r_(X-&gt;Y),X+r_(X+Y-&gt;0),X, while its mass-action specialization is -v_(X-&gt;Y)+v_(X+Y-&gt;0)=-(Sv)_Y; the mass-action determinant is nonzero on the positive steady-state locus (for example it equals 8 at v=(2,1,2,2) with the recorded Gale basis).

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B78-P02
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B78-P02
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/exact_census.py`
- `evidence/independent_replay.py`
- `evidence/triage_verification.py`

Bounded replay status in this packaging task: **passed**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.

Exact directed-network orbit count and the fixed positive-flux/rank boundary check.

## Dependencies and limitations / 依赖与限制

- sympy

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
