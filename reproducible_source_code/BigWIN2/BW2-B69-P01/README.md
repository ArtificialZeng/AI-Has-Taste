# BW2-B69-P01 — Subtraction-Free Bounded Ratios in One Sign Chamber at Degree Four in Three Variables

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B69-P01_Subtraction_Free_Bounded_Ratios_in_One_Sign_Chamber_at_Degree_Four_in_Three_Variables.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B69-P01/)

Original ID / 原始编号: `win-00069-p01`. Origin / 来源: 69.

## Accepted scope / 已接受范围

Partial-result note; parent problem not fully solved / 部分结果札记；母题未完整解决.

Use the H(4,3) coordinate order (004,013,022,031,040,103,112,121,130,202,211,220,301,310,400). For every gamma in BR_{\\mathring Q}(4,3) intersect Z^{H(4,3)} satisfying gamma_103 &lt;= 0, gamma_112 &lt;= 0, gamma_301 &lt;= 0, and gamma_alpha &gt;= 0 at each of the other twelve coordinates, there exists C(gamma)&gt;0 such that C(gamma)D_gamma-N_gamma is coefficientwise nonnegative in the twelve formal variables a_ri. This claim includes all boundary lattice points of that closed sign chamber and makes no assertion about integral cone points outside it; in particular it does not resolve the frozen universal conjecture.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B69-P01
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B69-P01
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/verify_chamber_hilbert.py`
- `evidence/verify_sign_chamber.py`
- `evidence/verify_triangular_rays.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- PyNormaliz
- sympy
- z3

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- The original question is unresolved; the released artifact is a partial result or unproved conjecture, according to its frozen claim.
- {'path': '/home/ailab/4math-open-problems/projects/win-00069-p01/evidence/chamber-hilbert-audit.md', 'indicators': ['absolute-local-path']}
- {'path': '/home/ailab/4math-open-problems/projects/win-00069-p01/evidence/verify_chamber_hilbert.py', 'indicators': ['absolute-local-path']}

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
