# BW2-PR20260914-antiprism_total_positivity — A coefficient obstruction for antiprism initial flag determinants

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-PR20260914-antiprism_total_positivity_A_coefficient_obstruction_for_antiprism_initial_flag_determinants.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-PR20260914-antiprism_total_positivity/)

Original ID / 原始编号: `primary-20260914-antiprism-total-positivity`. Origin / 来源: primary-20260914.

## Accepted scope / 已接受范围

Partial-result note; parent problem not fully solved / 部分结果札记；母题未完整解决.

For the unchanged formal determinant R_k defined in evidence/flag-coefficient-hypothesis.md and fully restated in evidence/research-pass3.md, put K=k(k+1)/2 and lambda_k=(product_{r=1}^k r!)/(product_{l=1}^k l^l)&gt;0. For every integer k&gt;=5, \[a^(K-1) n^0 z_1^5 z_6...z_k\]R_k = -lambda_k\*(125k^4-9555k^3+17736k^2-346478k+858264)/20736, where the final z product is empty for k=5. This coefficient is negative for every integer k&gt;=76. Also \[a^252 n^0 z_1^9 z_10...z_22\]R_22 = -lambda_22\*4429926944297146258237/14051921264640000000 &lt; 0. For every k&gt;=1, \[a^(K-1) n^0 z_1...z_k\]R_k = lambda_k\*k(k+1)(2k+1)/6 &gt; 0. These statements refute only the project-generated all-k coefficient-nonnegativity hypothesis in the specified slack variables, and do not disprove or prove total nonnegativity of H_d.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-PR20260914-antiprism_total_positivity
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-PR20260914-antiprism_total_positivity
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/research_flag_hierarchy.py`
- `evidence/research_fourth_flag.py`
- `evidence/research_next_degree.py`
- `evidence/research_pivots.py`
- `evidence/research_third_flag.py`
- `evidence/triage_exact.py`
- `evidence/verify_flag_hierarchy.py`
- `evidence/verify_flag_values.py`
- `evidence/verify_fourth_flag.py`
- `evidence/verify_next_degree.py`
- `evidence/verify_third_flag.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- sympy

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- The original question is unresolved; the released artifact is a partial result or unproved conjecture, according to its frozen claim.
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
