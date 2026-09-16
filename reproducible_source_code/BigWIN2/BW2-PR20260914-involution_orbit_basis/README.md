# BW2-PR20260914-involution_orbit_basis — Quadratic standard monomials for fixed involution classes

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-PR20260914-involution_orbit_basis_Quadratic_standard_monomials_for_fixed_involution_classes.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-PR20260914-involution_orbit_basis/)

Original ID / 原始编号: `primary-20260914-involution-orbit-basis`. Origin / 来源: primary-20260914.

## Accepted scope / 已接受范围

Partial-result note; parent problem not fully solved / 部分结果札记；母题未完整解决.

For every n&gt;0 and 0&lt;=a&lt;=n with a congruent to n modulo 2, a&gt;=2, and k=(n-a)/2&gt;=2, let H_n be all squarefree two-edge matching monomials in off-diagonal variables y_ij, i&lt;j, and let T_n={y_12\*y_ij:3&lt;=i&lt;j&lt;=n} union {y_13\*y_2j:4&lt;=j&lt;=n} union {y_1j\*y_23:4&lt;=j&lt;=n} union {y_15\*y_24,y_15\*y_34,y_25\*y_34}. The literal Pieri-RSK candidate specified in problem.md in degree 2 equals H_n minus T_n and is a basis of R(M_(n,a))_2. For the presentation Q\[y_ij\]/ker(y_ij maps to \[x_ij\]), or its scalar extension to C, H_n minus T_n is its degree-2 standard monomial set for every monomial order refining the positive variable weights n^2-ij. Every t in T_n has a unique homogeneous straightening into H_n minus T_n, and a nonzero coefficient at h implies sum_(ij in t) ij &lt; sum_(ij in h) ij. Degrees 0 and 1 have the literal candidate and standard monomial sets {1} and {y_ij:(i,j)!=(1,2)}. Consequently, for every n&gt;=6 their union is a complete explicit standard monomial basis of R(M_(n,n-4)), with Hilbert series 1+(C(n,2)-1)q+(3\*C(n,4)-C(n,2))q^2. No universal higher-degree assertion or complete resolution of original Problem 29 is claimed.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-PR20260914-involution_orbit_basis
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-PR20260914-involution_orbit_basis
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/coherence_attack.py`
- `evidence/desk_calibration.py`
- `evidence/product_weight_test.py`
- `evidence/research_rank.py`
- `evidence/triage_rank.py`
- `evidence/verify_quadratic.py`
- `evidence/verify_triage_rank.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- flint
- numpy
- scipy
- sympy

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- The original question is unresolved; the released artifact is a partial result or unproved conjecture, according to its frozen claim.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
