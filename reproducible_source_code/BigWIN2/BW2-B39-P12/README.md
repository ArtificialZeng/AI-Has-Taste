# BW2-B39-P12 — Local rigidity of component-triangle Cayley deformations at order-seven permutation Euler points

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B39-P12_Local_rigidity_of_component_triangle_Cayley_deformations_at_order_seven_permutation_Euler_points.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B39-P12/)

Original ID / 原始编号: `win-00039-p12`. Origin / 来源: 39.

## Accepted scope / 已接受范围

Partial-result note; parent problem not fully solved / 部分结果札记；母题未完整解决.

Let P be any unsigned 7 by 7 permutation matrix having exactly one diagonal 1, exactly one antidiagonal 1, and no eigenvalue -1. Then P has cycle type 1+3+3. Let {s} be its singleton cycle and C1,C2 its 3-cycles. For arbitrary u,v in C1 and w,t in C2, let F_ab be the elementary skew matrix on the unordered edge {a,b}, put S_P=(I-P)(I+P)^(-1), S(x,y,z)=S_P+x F_su+y F_vw+z F_st, and Q(x,y,z)=(I-S)(I+S)^(-1). The origin is an isolated real common zero of D(Q)-1 and A(Q)-1 in this affine three-coordinate family. Consequently, no nonconstant real-continuous solution germ passes through the anchor, and no rational parametrization defined over R can map a real parameter value to the anchor while parametrizing nearby Euler points. This is only a local obstruction for the stated families; it does not exclude a rational algebraic component having the anchor as an isolated real point, and it does not resolve whether a proper Euler magic matrix of order seven exists.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B39-P12
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B39-P12
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/cayley_100_slices.py`
- `evidence/cayley_triangle_slices.py`
- `evidence/verify_cayley_triangle_tangents.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- sympy

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- The original question is unresolved; the released artifact is a partial result or unproved conjecture, according to its frozen claim.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
