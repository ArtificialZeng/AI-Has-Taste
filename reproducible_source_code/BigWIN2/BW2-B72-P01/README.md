# BW2-B72-P01 — The Least Positive Layer of the P4–Paw Blow-Up Coefficient System

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B72-P01_The_Least_Positive_Layer_of_the_P4Paw_Blow_Up_Coefficient_System.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B72-P01/)

Original ID / 原始编号: `win-00072-p01`. Origin / 来源: 72.

## Accepted scope / 已接受范围

Resolution of the frozen statement · proved / 冻结命题的证明／反证（见精确范围） · proved.

Let b=(b0,b1,b2,b3) and a=(a0,a1,a2,a3) be ordered elements of Z_{&gt;0}^4 satisfying the four-equation P4/Paw coefficient system (3.3) reproduced verbatim in source.md, and let s=sum_i b_i=sum_i a_i. Then the least possible s is 61. At s=61 the complete ordered solution set is the four Cartesian combinations b in {(1,16,8,36),(36,8,16,1)} and a in {(4,9,16,32),(4,16,9,32)}. All four have signature (61,1116,6912,18432), and they constitute one orbit under exactly the two allowed involutions b -&gt; (b3,b2,b1,b0) and a -&gt; (a0,a2,a1,a3). The scope is only the least positive layer of this fixed coefficient system; it does not determine the minimum order among all connected distance-cospectral graph pairs or classify solutions above sum 61.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B72-P01
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B72-P01
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/compare_verifiers.py`
- `evidence/enumerate_signatures.py`
- `evidence/verify_z3_bv.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- z3

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
