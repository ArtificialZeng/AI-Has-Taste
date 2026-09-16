# BW2-B56-P03 — The Borel-fixed colength-15 tangent maximum on  Hilb15(A3)

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B56-P03_The_Borel_fixed_colength_15_tangent_maximum_on_Hilb15_A3.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B56-P03/)

Original ID / 原始编号: `win-00056-p03`. Origin / 来源: 56.

## Accepted scope / 已接受范围

Resolution of the frozen statement · proved / 冻结命题的证明／反证（见精确范围） · proved.

Let R=C\[x,y,z\] with the fixed Borel order x&lt;y&lt;z. Among all zero-dimensional Borel-fixed monomial ideals I of colength 15, max dim_C Hom_R(I,R/I)=81. Exactly four ideals attain 81: (y^3,xyz,xy^2,x^2z,x^2y,x^3,yz^3,y^2z^2,xz^3,z^5), (y^2z,y^3,xyz,xy^2,x^2z,x^2y,x^3,yz^3,xz^3,z^6), (xyz,xy^2,x^2z,x^2y,x^3,z^4,yz^3,y^2z^2,y^3z,y^4,xz^3), and (xz^2,xyz,xy^2,x^2z,x^2y,x^3,yz^3,y^2z^2,y^3z,y^4,z^5). Their pure-power tuples are respectively (3,3,5), (3,3,6), (3,4,4), and (3,4,5). Hence every maximizing Borel-fixed ideal has m_1(I)=3, proving the frozen necessary condition. The maximum among ideals with m_1&lt;=2 is 69, attained uniquely by (x^2,xyz,xy^2,yz^3,y^2z^2,y^3z,y^4,xz^3,z^5). No assertion is made about the maximum among non-Borel points of Hilb^15(A^3).

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B56-P03
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B56-P03
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/enumerate_borel15.py`
- `evidence/tangent_borel15.py`
- `evidence/verify_tangent_extrema.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- sympy

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
