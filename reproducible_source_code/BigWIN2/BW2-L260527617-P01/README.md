# BW2-L260527617-P01 — A Proof-Carrying Exclusion Through Length 18 for the 3-out-of-5 Picture-Hanging Word

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-L260527617-P01_A_Proof_Carrying_Exclusion_Through_Length_18_for_the_3_out_of_5_Picture_Hanging_Word.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-L260527617-P01/)

Original ID / 原始编号: `lit-260527617-p01`. Origin / 来源: 本地文献跟进.

## Accepted scope / 已接受范围

Partial-result note; parent problem not fully solved / 部分结果札记；母题未完整解决.

For the 3-out-of-5 picture-hanging problem in the free group F_5 as defined in source.md and interpreted in problem.md, no admissible element has reduced length at most 18. Hence L(3,5) &gt;= 20. The explicit independently checked length-26 element also gives L(3,5) &lt;= 26, so the certified window is 20 &lt;= L(3,5) &lt;= 26. This is a strict subsidiary bound and does not determine the exact value requested by the original problem.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-L260527617-P01
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-L260527617-P01
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/audit_drat_trim.py`
- `evidence/audit_exact_encoding.py`
- `evidence/audit_glucose_reproduction.py`
- `evidence/check_drup.py`
- `evidence/search_exact_sat.py`
- `evidence/search_exact_z3.py`
- `evidence/verify_upper26.py`

Bounded replay status in this packaging task: **passed**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.

Exact free-group reduction of the hard-coded length-26 deletion word.

## Dependencies and limitations / 依赖与限制

- pysat
- z3

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- The original question is unresolved; the released artifact is a partial result or unproved conjecture, according to its frozen claim.
- {'path': '/home/ailab/4math-open-problems/projects/lit-260527617-p01/evidence/audit_drat_trim.py', 'indicators': ['absolute-local-path']}
- {'path': '/home/ailab/4math-open-problems/projects/lit-260527617-p01/evidence/drat_trim_audit.json', 'indicators': ['absolute-local-path']}
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
