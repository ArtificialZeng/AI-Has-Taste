# BW2-B68-P02 — The least Type 1 cubic graphs without equitable 4-total colorings have order 16

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B68-P02_The_least_Type_1_cubic_graphs_without_equitable_4_total_colorings_have_order_16.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B68-P02/)

Original ID / 原始编号: `win-00068-p02`. Origin / 来源: 68.

## Accepted scope / 已接受范围

Resolution of the frozen statement · disproved / 冻结命题的证明／反证（见精确范围） · disproved.

The frozen assertion is false. Among connected simple cubic graphs of order below 20, the minimum order of a Type 1 graph with no equitable proper 4-total coloring is 16; there are exactly 16 such isomorphism classes at that least order, with the canonical graph6 codes listed in evidence/disproof.md.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B68-P02
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B68-P02
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/scripts/audit_resolution.py`
- `evidence/scripts/canonical_small.c`
- `evidence/scripts/certify_unsat.py`
- `evidence/scripts/check_cnf_bindings.py`
- `evidence/scripts/final_verify.py`
- `evidence/scripts/independent_census.py`
- `evidence/scripts/labeled_cubic_count.py`
- `evidence/scripts/make_claim.py`
- `evidence/scripts/regenerate_census.py`
- `evidence/scripts/second_encoding.py`
- `evidence/scripts/sweep_colorings.py`
- `evidence/scripts/verify_census.py`
- `evidence/scripts/verify_second_encoding.py`
- `evidence/scripts/verify_witnesses.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- networkx
- pysat

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- {'path': '/home/ailab/4math-open-problems/projects/win-00068-p02/evidence/final_verification.json', 'indicators': ['absolute-local-path']}
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
