# BW2-B58-P02 — A 1/226 Adjacent-Interval Edit Gap in a Fixed Ternary Brinkhuis Framework

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-B58-P02_A_1_226_Adjacent_Interval_Edit_Gap_in_a_Fixed_Ternary_Brinkhuis_Framework.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-B58-P02/)

Original ID / 原始编号: `win-00058-p02`. Origin / 来源: 58.

## Accepted scope / 已接受范围

Partial-result note; parent problem not fully solved / 部分结果札记；母题未完整解决.

Within the fixed Xu--Fu--Qiao--Tao arXiv:2609.04122v1 construction and proof framework specified in problem.md, using the canonical 952 length-54 ternary codewords, the published exact event-volume and dependency construction, and the fixed charges alpha=51/100000 and beta=3/10, C(226) holds: for every integer n&gt;=1 there exists S in {0,1,2}^n such that ED(S\[i,j),S\[j,k)) &gt;= (k-i)/226 for every 1&lt;=i&lt;j&lt;k&lt;=n+1. This statement does not assert that 226 is the least working denominator.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-B58-P02
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-B58-P02
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/audit_one_deletion_shell.py`
- `evidence/audit_two_deletion_shell.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- No third-party Python import detected by static inspection; this is not a tested environment lock.

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- The original question is unresolved; the released artifact is a partial result or unproved conjecture, according to its frozen claim.
- {'path': '/home/ailab/4math-open-problems/projects/win-00058-p02/evidence/research-pass-1.md', 'indicators': ['absolute-local-path']}
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
